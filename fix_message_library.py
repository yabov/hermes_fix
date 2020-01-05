import asyncio
import fix_messages_4_2_0_base
import fix_messages_4_4_0_base

import fix_message
from fix_message import SEP, EQU, b_SEP, b_EQU
import io
import logging
import fix_errors
import fix_core_fields

logger = logging.getLogger(__name__)

MESSAGE_BASE_LIBRARY = {}
MESSAGE_BASE_LIBRARY[fix_messages_4_4_0_base.BEGINSTRING] = fix_messages_4_4_0_base
MESSAGE_BASE_LIBRARY[fix_messages_4_2_0_base.BEGINSTRING] = fix_messages_4_2_0_base

DEFAULT_MESSAGE_READ_TIMEOUT = 2

async def create_message_from_stream(reader, messages = None ):
    buffer = io.BytesIO()
    try:
        byte = await reader.read(1) #read 1 byte to make sure strem has data on it        
        return await  asyncio.wait_for(_parse_into_buffer(byte, reader, buffer, messages), timeout = DEFAULT_MESSAGE_READ_TIMEOUT)
    except (asyncio.streams.IncompleteReadError, ConnectionAbortedError):
        raise
    except fix_errors.FIXInvalidMessageTypeError:
        raise
    except Exception as e:
        logger.exception(f"Failed to create message from stream [{buffer.getvalue()}]")
        raise fix_errors.FIXGarbledMessageError(e)

async def _parse_into_buffer(first_byte, reader, buffer, messages):
    """
    What constitutes a garbled message
    BeginString(8) is not the first tag in a message or is not of the format 8=FIX.n.m.
    BodyLength(9) is not the second tag in a message or does not contain the correct byte count.
    MsgType(35) is not the third tag in a message.
    Checksum(10) is not the last tag or contains an incorrect value.
    """

    buffer_size = 1

    beginString = first_byte + await reader.readuntil(b_SEP)
    buffer_size += buffer.write(beginString)
    beginString = beginString.decode()
    beginStringTag, beginStringValue = beginString[:-len(SEP)].split(EQU,1)

    if beginStringTag != fix_core_fields.BeginString._tag:
        raise fix_errors.FIXGarbledMessageError("BeginString is not first field")

    bodyLength = await reader.readuntil(b_SEP)
    buffer_size += buffer.write(bodyLength)
    bodyLength = bodyLength.decode()
    bodyLengthTag, bodyLengthValue = bodyLength[:-len(SEP)].split(EQU,1)

    if bodyLengthTag != fix_core_fields.BodyLength._tag:
        raise fix_errors.FIXGarbledMessageError("BodyLength is not second field")

    msgType = await reader.readuntil(b_SEP)
    buffer_size += buffer.write(msgType)
    msgType = msgType.decode()
    msgTypeTag, msgTypeValue = msgType[:-len(SEP)].split(EQU,1)

    if msgTypeTag != fix_core_fields.MsgType._tag:
        raise fix_errors.FIXGarbledMessageError("MsgType is not third field")

   
    data = await reader.readexactly(int(bodyLengthValue) - len(msgType))
    buffer_size += buffer.write(data)
    data_list = data.decode().split(SEP)
    data_list.pop(-1) #removes last empty item

    checkSum = await reader.readuntil(b_SEP)
    #checkSum = checkSum.decode()
    checkSumTag, checkSumValue = checkSum[:-len(b_SEP)].split(b_EQU,1)
    checkSumTag = checkSumTag.decode()

    if checkSumTag != fix_core_fields.CheckSum._tag:
        raise fix_errors.FIXGarbledMessageError(f"CheckSum is not last field")

    calced_checksum = fix_message.calc_checksum(buffer)
    buffer.write(checkSum)
    if len(checkSumValue) != 3 or checkSumValue.decode() != calced_checksum:
        raise fix_errors.FIXCheckSumError(f"Faield Checksum got {checkSumValue.decode()} but expected {calced_checksum}")

    if not messages:
        messages = MESSAGE_BASE_LIBRARY[beginStringValue]

    header = messages.Header()
    header.BeginString = beginStringValue
    header.BodyLength = bodyLengthValue
    header.build_from_list(data_list, True)

    msg_class = messages.MESSAGE_TYPES.get(msgTypeValue)
    if not msg_class:
        error = fix_errors.FIXInvalidMessageTypeError(header.MsgSeqNum, msgTypeValue, msgTypeTag, "Invalid MsgType", messages.SessionRejectReason.ENUM_INVALID_MSGTYPE)
        raise error



    msg = msg_class()
    msg.Header = header
    msg.build_from_list(data_list)

    trailer = messages.Trailer()
    trailer.CheckSum = checkSumValue
    trailer.build_from_list(data_list, True)

    msg.Trailer = trailer

    return msg, buffer.getvalue()

def create_message_from_binary(data, msg_class, messages):
    data_list = data.decode().split(SEP)
    data_list.pop(-1) #removes last empty item
    header = messages.Header()
    header.build_from_list(data_list, True)

    msg = messages.MESSAGE_TYPES[msg_class]()
    msg.build_from_list(data_list)

    trailer = messages.Trailer()
    trailer.build_from_list(data_list, True)

    #msg.Header = header
    #msg.Trailer = trailer


    return header, msg, trailer

