import asyncio
import concurrent
import io
import logging
import importlib
import os

from . import fix_errors, fix_message, message_lib
from .message_lib import *
from .utils.constants import EQU, SEP, b_EQU, b_SEP
from .utils.log import logger
from .utils import fix_msg_generator

MESSAGE_BASE_LIBRARY = {}
MESSAGE_BASE_LIBRARY[FIX_4_0.fix_messages.BEGINSTRING] = FIX_4_0
MESSAGE_BASE_LIBRARY[FIX_4_1.fix_messages.BEGINSTRING] = FIX_4_1
MESSAGE_BASE_LIBRARY[FIX_4_2.fix_messages.BEGINSTRING] = FIX_4_2
MESSAGE_BASE_LIBRARY[FIX_4_3.fix_messages.BEGINSTRING] = FIX_4_3
MESSAGE_BASE_LIBRARY[FIX_4_4.fix_messages.BEGINSTRING] = FIX_4_4
MESSAGE_BASE_LIBRARY[FIX_5_0.fix_messages.BEGINSTRING] = FIX_5_0
MESSAGE_BASE_LIBRARY[FIX_5_0SP1.fix_messages.BEGINSTRING] = FIX_5_0SP1
MESSAGE_BASE_LIBRARY[FIX_5_0SP2.fix_messages.BEGINSTRING] = FIX_5_0SP2

DEFAULT_MESSAGE_READ_TIMEOUT = 2

def load_data_dict(data_dict, engine_key):
    gen_file_name = fix_msg_generator.generate_fix_classes(data_dict, message_lib.__path__[0], '_'.join(engine_key))

    #mod = importlib.import_module('.' + gen_file_name, 'hermes_fix.message_lib')
    mod = importlib.import_module('.' + gen_file_name, message_lib.__name__)
    return mod

async def create_message_from_stream(reader, messages, settings):
    read_timeout = settings.get(
        "MessageReadTimeout", fallback=DEFAULT_MESSAGE_READ_TIMEOUT)
    buffer = io.BytesIO()
    try:
        # read 1 byte to make sure strem has data on it
        byte = await reader.read(1)
        return await asyncio.wait_for(_parse_into_buffer(byte, reader, buffer, messages, settings),
                                      timeout=read_timeout)
    except (asyncio.IncompleteReadError, ConnectionAbortedError, concurrent.futures.CancelledError):
        raise
    except (fix_errors.FIXInvalidMessageTypeError, fix_errors.FIXInvalidMessageFieldError, fix_errors.FIXRejectError):
        raise
    except Exception as e:
        logger.exception(
            f"Failed to create message from stream [{buffer.getvalue()}]")
        raise fix_errors.FIXGarbledMessageError(e)


async def _parse_into_buffer(first_byte, reader, buffer, messages, settings):
    """
    What constitutes a garbled message
    BeginString(8) is not the first tag in a message or is not of the format 8=FIX.n.m.
    BodyLength(9) is not the second tag in a message or does not contain the correct byte count.
    MsgType(35) is not the third tag in a message.
    Checksum(10) is not the last tag or contains an incorrect value.
    """

    ignore_checksum = settings.getboolean("IgnoreChecksum", fallback=False)
    ignore_invalid_field_vals = settings.getboolean(
        "IgnoreInvalidFieldValues", fallback=False)

    buffer_size = 1

    beginString = first_byte + await reader.readuntil(b_SEP)
    buffer_size += buffer.write(beginString)
    beginString = beginString.decode()
    beginStringTag, beginStringValue = beginString[:-len(SEP)].split(EQU, 1)

    if not messages:
        messages = MESSAGE_BASE_LIBRARY[beginStringValue]

    if beginStringTag != messages.fields.BeginString._tag:
        raise fix_errors.FIXGarbledMessageError(
            "BeginString is not first field")

    bodyLength = await reader.readuntil(b_SEP)
    buffer_size += buffer.write(bodyLength)
    bodyLength = bodyLength.decode()
    bodyLengthTag, bodyLengthValue = bodyLength[:-len(SEP)].split(EQU, 1)

    if bodyLengthTag != messages.fields.BodyLength._tag:
        raise fix_errors.FIXGarbledMessageError(
            "BodyLength is not second field")

    msgType = await reader.readuntil(b_SEP)
    buffer_size += buffer.write(msgType)
    msgType = msgType.decode()
    msgTypeTag, msgTypeValue = msgType[:-len(SEP)].split(EQU, 1)

    if msgTypeTag != messages.fields.MsgType._tag:
        raise fix_errors.FIXGarbledMessageError("MsgType is not third field")

    data = await reader.readexactly(int(bodyLengthValue) - len(msgType))
    buffer_size += buffer.write(data)
    data_list = data.decode().split(SEP)
    data_list.pop(-1)  # removes last empty item

    checkSum = await reader.readuntil(b_SEP)
    checkSumTag, checkSumValue = checkSum[:-len(b_SEP)].split(b_EQU, 1)
    checkSumTag = checkSumTag.decode()

    if checkSumTag != messages.fields.CheckSum._tag:
        raise fix_errors.FIXGarbledMessageError(f"CheckSum is not last field")

    calced_checksum = fix_message.calc_checksum(buffer)
    buffer.write(checkSum)
    if not ignore_checksum and (len(checkSumValue) != 3 or checkSumValue.decode() != calced_checksum):
        raise fix_errors.FIXCheckSumError(
            f"Faield Checksum got {checkSumValue.decode()} but expected {calced_checksum}")

    msg_class = messages.fix_messages.MESSAGE_TYPES.get(msgTypeValue)
    if not msg_class:
        error = fix_errors.FIXInvalidMessageTypeError(
            None, msgTypeValue, msgTypeTag, "Invalid MsgType", messages.fields.SessionRejectReason.ENUM_INVALID_MSG_TYPE)
        raise error

    header = messages.fix_messages.Header()
    header.BeginString = beginStringValue
    header.BodyLength = bodyLengthValue

    missed_fields = _build_from_list(
        header, data_list, True, messages, msg_class, ignore_invalid_field_vals)

    msg = msg_class()
    msg.Header = header
    missed_fields += _build_from_list(msg, data_list, False,
                                      messages, msg_class, ignore_invalid_field_vals)

    trailer = messages.fix_messages.Trailer()
    trailer.CheckSum = checkSumValue
    missed_fields += _build_from_list(trailer, data_list,
                                      True, messages, msg_class, ignore_invalid_field_vals)
    msg.Trailer = trailer

    return msg, buffer.getvalue(), missed_fields


def create_message_from_binary(data, msg_class, messages):
    data_list = data.decode().split(SEP)
    data_list.pop(-1)  # removes last empty item
    header = messages.fix_messages.Header()
    _build_from_list(header, data_list, True, messages, msg_class)

    msg = messages.fix_messages.MESSAGE_TYPES[msg_class]()
    _build_from_list(msg, data_list, False, messages, msg_class)

    trailer = messages.fix_messages.Trailer()
    _build_from_list(trailer, data_list, True, messages, msg_class)

    msg.Header = header
    msg.Trailer = trailer

    strip_msg_for_resend(messages, msg)

    return msg


def _build_from_list(obj, data_list, stop_if_field_not_defined, messages, msg_class, ignore_invalid_field_vals=False):
    try:
        missed_fields = obj.build_from_list(
            data_list, stop_if_field_not_defined, ignore_invalid_field_vals)
        return missed_fields
    except fix_errors.FIXEnumValueError as e:
        raise fix_errors.FIXInvalidMessageFieldError(None, msg_class._msgtype, e.tag,
                                                     "Value is incorrect (out of range) for this tag", messages.fields.SessionRejectReason.ENUM_VALUE_IS_INCORRECT)
    except fix_errors.FIXTagEmptyError as e:
        raise fix_errors.FIXInvalidMessageFieldError(None, msg_class._msgtype, e.tag,
                                                     "Tag specified without a value", messages.fields.SessionRejectReason.ENUM_TAG_SPECIFIED_WITHOUT_A_VALUE)
    except fix_errors.FIXValueError as e:
        raise fix_errors.FIXInvalidMessageFieldError(None, msg_class._msgtype, e.tag,
                                                     "Incorrect data format for value", messages.fields.SessionRejectReason.ENUM_INCORRECT_DATA_FORMAT_FOR_VALUE)
    except fix_errors.FIXRepeatingFieldError as e:
        e.RefMsgType = msg_class._msgtype
        if messages.fix_messages.BEGINSTRING >= 'FIX.4.3':
            e.SessionRejectReason = messages.fields.SessionRejectReason.ENUM_TAG_APPEARS_MORE_THAN_ONCE
        raise e


def strip_msg_for_resend(messages, msg):
    """
    Cleans up all required header and trailer fields for resending a message
    Fields like SenderCompID,TargetCompD,SndingTime, CheckSum, etc... need to be cleaned
    """
    msg.Header.PossDupFlag = messages.fields.PossDupFlag.ENUM_POSSIBLE_DUPLICATE
    msg.Header.OrigSendingTime = msg.Header.SendingTime

    msg.Header.BeginString = None
    msg.Header.BodyLength = None
    msg.Header.MsgType = None
    msg.Header.SenderCompID = None
    msg.Header.TargetCompID = None
    msg.Header.SendingTime = None
    msg.Trailer.CheckSum = None
