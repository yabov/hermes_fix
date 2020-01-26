from . import field_types
from ...utils import fix_enum_type

class Account (field_types.String_Type) :
    _tag = '1'

class AdvId (field_types.String_Type) :
    _tag = '2'

class AdvRefID (field_types.String_Type) :
    _tag = '3'

class AdvSide (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '4'
    ENUM_BUY = 'B'
    ENUM_SELL = 'S'
    ENUM_TRADE = 'T'
    ENUM_CROSS = 'X'

class AdvTransType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '5'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'

class AvgPx (field_types.Price_Type) :
    _tag = '6'

class BeginSeqNo (field_types.int_Type) :
    _tag = '7'

class BeginString (field_types.String_Type) :
    _tag = '8'

class BodyLength (field_types.int_Type) :
    _tag = '9'

class CheckSum (field_types.String_Type) :
    _tag = '10'

class ClOrdID (field_types.String_Type) :
    _tag = '11'

class Commission (field_types.Amt_Type) :
    _tag = '12'

class CommType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '13'
    ENUM_PER_UNIT = '1'
    ENUM_PERCENT = '2'
    ENUM_ABSOLUTE = '3'

class CumQty (field_types.Qty_Type) :
    _tag = '14'

class Currency (field_types.Currency_Type) :
    _tag = '15'

class EndSeqNo (field_types.int_Type) :
    _tag = '16'

class ExecID (field_types.String_Type) :
    _tag = '17'

class ExecInst (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '18'
    ENUM_STAY_ON_OFFER_SIDE = '0'
    ENUM_NOT_HELD = '1'
    ENUM_WORK = '2'
    ENUM_GO_ALONG = '3'
    ENUM_OVER_THE_DAY = '4'
    ENUM_HELD = '5'
    ENUM_PARTICIPATE_DO_NOT_INITIATE = '6'
    ENUM_STRICT_SCALE = '7'
    ENUM_TRY_TO_SCALE = '8'
    ENUM_STAY_ON_BID_SIDE = '9'
    ENUM_NO_CROSS = 'A'
    ENUM_OK_TO_CROSS = 'B'
    ENUM_CALL_FIRST = 'C'
    ENUM_PERCENT_OF_VOLUME = 'D'
    ENUM_DO_NOT_INCREASE = 'E'
    ENUM_DO_NOT_REDUCE = 'F'
    ENUM_ALL_OR_NONE = 'G'
    ENUM_INSTITUTIONS_ONLY = 'I'
    ENUM_LAST_PEG = 'L'
    ENUM_MID_PRICE_PEG = 'M'
    ENUM_NON_NEGOTIABLE = 'N'
    ENUM_OPENING_PEG = 'O'
    ENUM_MARKET_PEG = 'P'
    ENUM_PRIMARY_PEG = 'R'
    ENUM_SUSPEND = 'S'
    ENUM_FIXED_PEG_TO_LOCAL_BEST_BID_OR_OFFER_AT_TIME_OF_ORDER = 'T'
    ENUM_CUSTOMER_DISPLAY_INSTRUCTION = 'U'
    ENUM_NETTING = 'V'
    ENUM_PEG_TO_VWAP = 'W'

class ExecRefID (field_types.String_Type) :
    _tag = '19'

class ExecTransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '20'
    ENUM_NEW = '0'
    ENUM_CANCEL = '1'
    ENUM_CORRECT = '2'
    ENUM_STATUS = '3'

class HandlInst (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '21'
    ENUM_AUTOMATED_EXECUTION_NO_INTERVENTION = '1'
    ENUM_AUTOMATED_EXECUTION_INTERVENTION_OK = '2'
    ENUM_MANUAL_ORDER = '3'

class IDSource (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '22'
    ENUM_CUSIP = '1'
    ENUM_SEDOL = '2'
    ENUM_QUIK = '3'
    ENUM_ISIN_NUMBER = '4'
    ENUM_RIC_CODE = '5'
    ENUM_ISO_CURRENCY_CODE = '6'
    ENUM_ISO_COUNTRY_CODE = '7'
    ENUM_EXCHANGE_SYMBOL = '8'
    ENUM_CONSOLIDATED_TAPE_ASSOCIATION = '9'

class IOIid (field_types.String_Type) :
    _tag = '23'

class IOIOthSvc (field_types.char_Type) :
    _tag = '24'

class IOIQltyInd (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '25'
    ENUM_HIGH = 'H'
    ENUM_LOW = 'L'
    ENUM_MEDIUM = 'M'

class IOIRefID (field_types.String_Type) :
    _tag = '26'

class IOIShares (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '27'
    ENUM_LARGE = 'L'
    ENUM_MEDIUM = 'M'
    ENUM_SMALL = 'S'

class IOITransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '28'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'

class LastCapacity (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '29'
    ENUM_AGENT = '1'
    ENUM_CROSS_AS_AGENT = '2'
    ENUM_CROSS_AS_PRINCIPAL = '3'
    ENUM_PRINCIPAL = '4'

class LastMkt (field_types.Exchange_Type) :
    _tag = '30'

class LastPx (field_types.Price_Type) :
    _tag = '31'

class LastShares (field_types.Qty_Type) :
    _tag = '32'

class LinesOfText (field_types.int_Type) :
    _tag = '33'

class MsgSeqNum (field_types.int_Type) :
    _tag = '34'

class MsgType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '35'
    ENUM_HEARTBEAT = '0'
    ENUM_TEST_REQUEST = '1'
    ENUM_RESEND_REQUEST = '2'
    ENUM_REJECT = '3'
    ENUM_SEQUENCE_RESET = '4'
    ENUM_LOGOUT = '5'
    ENUM_IOI = '6'
    ENUM_ADVERTISEMENT = '7'
    ENUM_EXECUTION_REPORT = '8'
    ENUM_ORDER_CANCEL_REJECT = '9'
    ENUM_LOGON = 'A'
    ENUM_NEWS = 'B'
    ENUM_EMAIL = 'C'
    ENUM_NEW_ORDER_SINGLE = 'D'
    ENUM_NEW_ORDER_LIST = 'E'
    ENUM_ORDER_CANCEL_REQUEST = 'F'
    ENUM_ORDER_CANCEL_REPLACE_REQUEST = 'G'
    ENUM_ORDER_STATUS_REQUEST = 'H'
    ENUM_ALLOCATION_INSTRUCTION = 'J'
    ENUM_LIST_CANCEL_REQUEST = 'K'
    ENUM_LIST_EXECUTE = 'L'
    ENUM_LIST_STATUS_REQUEST = 'M'
    ENUM_LIST_STATUS = 'N'
    ENUM_ALLOCATION_INSTRUCTION_ACK = 'P'
    ENUM_DONT_KNOW_TRADE = 'Q'
    ENUM_QUOTE_REQUEST = 'R'
    ENUM_QUOTE = 'S'
    ENUM_SETTLEMENT_INSTRUCTIONS = 'T'
    ENUM_MARKET_DATA_REQUEST = 'V'
    ENUM_MARKET_DATA_SNAPSHOT_FULL_REFRESH = 'W'
    ENUM_MARKET_DATA_INCREMENTAL_REFRESH = 'X'
    ENUM_MARKET_DATA_REQUEST_REJECT = 'Y'
    ENUM_QUOTE_CANCEL = 'Z'
    ENUM_QUOTE_STATUS_REQUEST = 'a'
    ENUM_MASS_QUOTE_ACKNOWLEDGEMENT = 'b'
    ENUM_SECURITY_DEFINITION_REQUEST = 'c'
    ENUM_SECURITY_DEFINITION = 'd'
    ENUM_SECURITY_STATUS_REQUEST = 'e'
    ENUM_SECURITY_STATUS = 'f'
    ENUM_TRADING_SESSION_STATUS_REQUEST = 'g'
    ENUM_TRADING_SESSION_STATUS = 'h'
    ENUM_MASS_QUOTE = 'i'
    ENUM_BUSINESS_MESSAGE_REJECT = 'j'
    ENUM_BID_REQUEST = 'k'
    ENUM_BID_RESPONSE = 'l'
    ENUM_LIST_STRIKE_PRICE = 'm'

class NewSeqNo (field_types.int_Type) :
    _tag = '36'

class OrderID (field_types.String_Type) :
    _tag = '37'

class OrderQty (field_types.Qty_Type) :
    _tag = '38'

class OrdStatus (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '39'
    ENUM_NEW = '0'
    ENUM_PARTIALLY_FILLED = '1'
    ENUM_FILLED = '2'
    ENUM_DONE_FOR_DAY = '3'
    ENUM_CANCELED = '4'
    ENUM_REPLACED = '5'
    ENUM_PENDING_CANCEL = '6'
    ENUM_STOPPED = '7'
    ENUM_REJECTED = '8'
    ENUM_SUSPENDED = '9'
    ENUM_PENDING_NEW = 'A'
    ENUM_CALCULATED = 'B'
    ENUM_EXPIRED = 'C'
    ENUM_ACCEPTED_FOR_BIDDING = 'D'
    ENUM_PENDING_REPLACE = 'E'

class OrdType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '40'
    ENUM_MARKET = '1'
    ENUM_LIMIT = '2'
    ENUM_STOP = '3'
    ENUM_STOP_LIMIT = '4'
    ENUM_MARKET_ON_CLOSE = '5'
    ENUM_WITH_OR_WITHOUT = '6'
    ENUM_LIMIT_OR_BETTER = '7'
    ENUM_LIMIT_WITH_OR_WITHOUT = '8'
    ENUM_ON_BASIS = '9'
    ENUM_ON_CLOSE = 'A'
    ENUM_LIMIT_ON_CLOSE = 'B'
    ENUM_FOREX_MARKET = 'C'
    ENUM_PREVIOUSLY_QUOTED = 'D'
    ENUM_PREVIOUSLY_INDICATED = 'E'
    ENUM_FOREX_LIMIT = 'F'
    ENUM_FOREX_SWAP = 'G'
    ENUM_FOREX_PREVIOUSLY_QUOTED = 'H'
    ENUM_FUNARI = 'I'
    ENUM_PEGGED = 'P'

class OrigClOrdID (field_types.String_Type) :
    _tag = '41'

class OrigTime (field_types.UTCTimestamp_Type) :
    _tag = '42'

class PossDupFlag (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '43'
    ENUM_ORIGINAL_TRANSMISSION = 'N'
    ENUM_POSSIBLE_DUPLICATE = 'Y'

class Price (field_types.Price_Type) :
    _tag = '44'

class RefSeqNum (field_types.int_Type) :
    _tag = '45'

class RelatdSym (field_types.String_Type) :
    _tag = '46'

class Rule80A (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '47'
    ENUM_AGENCY_SINGLE_ORDER = 'A'
    ENUM_SHORT_EXEMPT_TRANSACTION_A_TYPE = 'B'
    ENUM_PROPRIETARY_NON_ALGO = 'C'
    ENUM_PROGRAM_ORDER_MEMBER = 'D'
    ENUM_SHORT_EXEMPT_TRANSACTION_FOR_PRINCIPAL = 'E'
    ENUM_SHORT_EXEMPT_TRANSACTION_W_TYPE = 'F'
    ENUM_SHORT_EXEMPT_TRANSACTION_I_TYPE = 'H'
    ENUM_INDIVIDUAL_INVESTOR = 'I'
    ENUM_PROPRIETARY_ALGO = 'J'
    ENUM_AGENCY_ALGO = 'K'
    ENUM_SHORT_EXEMPT_TRANSACTION_MEMBER_AFFLIATED = 'L'
    ENUM_PROGRAM_ORDER_OTHER_MEMBER = 'M'
    ENUM_AGENT_FOR_OTHER_MEMBER = 'N'
    ENUM_PROPRIETARY_TRANSACTION_AFFILIATED = 'O'
    ENUM_PRINCIPAL = 'P'
    ENUM_TRANSACTION_NON_MEMBER = 'R'
    ENUM_SPECIALIST_TRADES = 'S'
    ENUM_TRANSACTION_UNAFFILIATED_MEMBER = 'T'
    ENUM_AGENCY_INDEX_ARB = 'U'
    ENUM_ALL_OTHER_ORDERS_AS_AGENT_FOR_OTHER_MEMBER = 'W'
    ENUM_SHORT_EXEMPT_TRANSACTION_MEMBER_NOT_AFFLIATED = 'X'
    ENUM_AGENCY_NON_ALGO = 'Y'
    ENUM_SHORT_EXEMPT_TRANSACTION_NON_MEMBER = 'Z'

class SecurityID (field_types.String_Type) :
    _tag = '48'

class SenderCompID (field_types.String_Type) :
    _tag = '49'

class SenderSubID (field_types.String_Type) :
    _tag = '50'

class SendingDate (field_types.LocalMktDate_Type) :
    _tag = '51'

class SendingTime (field_types.UTCTimestamp_Type) :
    _tag = '52'

class Shares (field_types.Qty_Type) :
    _tag = '53'

class Side (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '54'
    ENUM_BUY = '1'
    ENUM_SELL = '2'
    ENUM_BUY_MINUS = '3'
    ENUM_SELL_PLUS = '4'
    ENUM_SELL_SHORT = '5'
    ENUM_SELL_SHORT_EXEMPT = '6'
    ENUM_UNDISCLOSED = '7'
    ENUM_CROSS = '8'
    ENUM_CROSS_SHORT = '9'

class Symbol (field_types.String_Type) :
    _tag = '55'

class TargetCompID (field_types.String_Type) :
    _tag = '56'

class TargetSubID (field_types.String_Type) :
    _tag = '57'

class Text (field_types.String_Type) :
    _tag = '58'

class TimeInForce (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '59'
    ENUM_DAY = '0'
    ENUM_GOOD_TILL_CANCEL = '1'
    ENUM_AT_THE_OPENING = '2'
    ENUM_IMMEDIATE_OR_CANCEL = '3'
    ENUM_FILL_OR_KILL = '4'
    ENUM_GOOD_TILL_CROSSING = '5'
    ENUM_GOOD_TILL_DATE = '6'

class TransactTime (field_types.UTCTimestamp_Type) :
    _tag = '60'

class Urgency (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '61'
    ENUM_NORMAL = '0'
    ENUM_FLASH = '1'
    ENUM_BACKGROUND = '2'

class ValidUntilTime (field_types.UTCTimestamp_Type) :
    _tag = '62'

class SettlmntTyp (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '63'
    ENUM_REGULAR = '0'
    ENUM_CASH = '1'
    ENUM_NEXT_DAY = '2'
    ENUM_T_PLUS2 = '3'
    ENUM_T_PLUS3 = '4'
    ENUM_T_PLUS4 = '5'
    ENUM_FUTURE = '6'
    ENUM_WHEN_AND_IF_ISSUED = '7'
    ENUM_SELLERS_OPTION = '8'
    ENUM_T_PLUS5 = '9'

class FutSettDate (field_types.LocalMktDate_Type) :
    _tag = '64'

class SymbolSfx (field_types.String_Type) :
    _tag = '65'

class ListID (field_types.String_Type) :
    _tag = '66'

class ListSeqNo (field_types.int_Type) :
    _tag = '67'

class TotNoOrders (field_types.int_Type) :
    _tag = '68'

class ListExecInst (field_types.String_Type) :
    _tag = '69'

class AllocID (field_types.String_Type) :
    _tag = '70'

class AllocTransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '71'
    ENUM_NEW = '0'
    ENUM_REPLACE = '1'
    ENUM_CANCEL = '2'
    ENUM_PRELIMINARY = '3'
    ENUM_CALCULATED = '4'
    ENUM_CALCULATED_WITHOUT_PRELIMINARY = '5'

class RefAllocID (field_types.String_Type) :
    _tag = '72'

class NoOrders (field_types.int_Type) :
    _tag = '73'

class AvgPrxPrecision (field_types.int_Type) :
    _tag = '74'

class TradeDate (field_types.LocalMktDate_Type) :
    _tag = '75'

class ExecBroker (field_types.String_Type) :
    _tag = '76'

class OpenClose (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '77'
    ENUM_CLOSE = 'C'
    ENUM_OPEN = 'O'

class NoAllocs (field_types.int_Type) :
    _tag = '78'

class AllocAccount (field_types.String_Type) :
    _tag = '79'

class AllocShares (field_types.Qty_Type) :
    _tag = '80'

class ProcessCode (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '81'
    ENUM_REGULAR = '0'
    ENUM_SOFT_DOLLAR = '1'
    ENUM_STEP_IN = '2'
    ENUM_STEP_OUT = '3'
    ENUM_SOFT_DOLLAR_STEP_IN = '4'
    ENUM_SOFT_DOLLAR_STEP_OUT = '5'
    ENUM_PLAN_SPONSOR = '6'

class NoRpts (field_types.int_Type) :
    _tag = '82'

class RptSeq (field_types.int_Type) :
    _tag = '83'

class CxlQty (field_types.Qty_Type) :
    _tag = '84'

class NoDlvyInst (field_types.int_Type) :
    _tag = '85'

class DlvyInst (field_types.String_Type) :
    _tag = '86'

class AllocStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '87'
    ENUM_ACCEPTED = 0
    ENUM_BLOCK_LEVEL_REJECT = 1
    ENUM_ACCOUNT_LEVEL_REJECT = 2
    ENUM_RECEIVED = 3

class AllocRejCode (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '88'
    ENUM_UNKNOWN_ACCOUNT = 0
    ENUM_INCORRECT_QUANTITY = 1
    ENUM_INCORRECT_AVERAGEG_PRICE = 2
    ENUM_UNKNOWN_EXECUTING_BROKER_MNEMONIC = 3
    ENUM_COMMISSION_DIFFERENCE = 4
    ENUM_UNKNOWN_ORDER_ID = 5
    ENUM_UNKNOWN_LIST_ID = 6
    ENUM_OTHER_SEE_TEXT = 7

class Signature (field_types.data_Type) :
    _tag = '89'

class SecureDataLen (field_types.Length_Type) :
    _tag = '90'

class SecureData (field_types.data_Type) :
    _tag = '91'

class BrokerOfCredit (field_types.String_Type) :
    _tag = '92'

class SignatureLength (field_types.Length_Type) :
    _tag = '93'

class EmailType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '94'
    ENUM_NEW = '0'
    ENUM_REPLY = '1'
    ENUM_ADMIN_REPLY = '2'

class RawDataLength (field_types.Length_Type) :
    _tag = '95'

class RawData (field_types.data_Type) :
    _tag = '96'

class PossResend (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '97'
    ENUM_ORIGINAL_TRANSMISSION = 'N'
    ENUM_POSSIBLE_RESEND = 'Y'

class EncryptMethod (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '98'
    ENUM_NONE = 0
    ENUM_PKCS = 1
    ENUM_DES = 2
    ENUM_PKCSDES = 3
    ENUM_PGPDES = 4
    ENUM_PGPDESMD5 = 5
    ENUM_PEM = 6

class StopPx (field_types.Price_Type) :
    _tag = '99'

class ExDestination (field_types.Exchange_Type) :
    _tag = '100'

class CxlRejReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '102'
    ENUM_TOO_LATE_TO_CANCEL = 0
    ENUM_UNKNOWN_ORDER = 1
    ENUM_BROKER_CREDIT = 2
    ENUM_ORDER_ALREADY_IN_PENDING_STATUS = 3

class OrdRejReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '103'
    ENUM_BROKER_CREDIT = 0
    ENUM_UNKNOWN_SYMBOL = 1
    ENUM_EXCHANGE_CLOSED = 2
    ENUM_ORDER_EXCEEDS_LIMIT = 3
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_UNKNOWN_ORDER = 5
    ENUM_DUPLICATE_ORDER = 6
    ENUM_DUPLICATE_OF_A_VERBALLY_COMMUNICATED_ORDER = 7
    ENUM_STALE_ORDER = 8

class IOIQualifier (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '104'
    ENUM_ALL_OR_NONE = 'A'
    ENUM_AT_THE_CLOSE = 'C'
    ENUM_IN_TOUCH_WITH = 'I'
    ENUM_LIMIT = 'L'
    ENUM_MORE_BEHIND = 'M'
    ENUM_AT_THE_OPEN = 'O'
    ENUM_TAKING_A_POSITION = 'P'
    ENUM_AT_THE_MARKET = 'Q'
    ENUM_READY_TO_TRADE = 'R'
    ENUM_PORTFOLIO_SHOWN = 'S'
    ENUM_THROUGH_THE_DAY = 'T'
    ENUM_VERSUS = 'V'
    ENUM_INDICATION = 'W'
    ENUM_CROSSING_OPPORTUNITY = 'X'
    ENUM_AT_THE_MIDPOINT = 'Y'
    ENUM_PRE_OPEN = 'Z'

class WaveNo (field_types.String_Type) :
    _tag = '105'

class Issuer (field_types.String_Type) :
    _tag = '106'

class SecurityDesc (field_types.String_Type) :
    _tag = '107'

class HeartBtInt (field_types.int_Type) :
    _tag = '108'

class ClientID (field_types.String_Type) :
    _tag = '109'

class MinQty (field_types.Qty_Type) :
    _tag = '110'

class MaxFloor (field_types.Qty_Type) :
    _tag = '111'

class TestReqID (field_types.String_Type) :
    _tag = '112'

class ReportToExch (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '113'
    ENUM_SENDER_REPORTS = 'N'
    ENUM_RECEIVER_REPORTS = 'Y'

class LocateReqd (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '114'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class OnBehalfOfCompID (field_types.String_Type) :
    _tag = '115'

class OnBehalfOfSubID (field_types.String_Type) :
    _tag = '116'

class QuoteID (field_types.String_Type) :
    _tag = '117'

class NetMoney (field_types.Amt_Type) :
    _tag = '118'

class SettlCurrAmt (field_types.Amt_Type) :
    _tag = '119'

class SettlCurrency (field_types.Currency_Type) :
    _tag = '120'

class ForexReq (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '121'
    ENUM_DO_NOT_EXECUTE_FOREX_AFTER_SECURITY_TRADE = 'N'
    ENUM_EXECUTE_FOREX_AFTER_SECURITY_TRADE = 'Y'

class OrigSendingTime (field_types.UTCTimestamp_Type) :
    _tag = '122'

class GapFillFlag (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '123'
    ENUM_SEQUENCE_RESET = 'N'
    ENUM_GAP_FILL_MESSAGE = 'Y'

class NoExecs (field_types.int_Type) :
    _tag = '124'

class CxlType (field_types.char_Type) :
    _tag = '125'

class ExpireTime (field_types.UTCTimestamp_Type) :
    _tag = '126'

class DKReason (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '127'
    ENUM_UNKNOWN_SYMBOL = 'A'
    ENUM_WRONG_SIDE = 'B'
    ENUM_QUANTITY_EXCEEDS_ORDER = 'C'
    ENUM_NO_MATCHING_ORDER = 'D'
    ENUM_PRICE_EXCEEDS_LIMIT = 'E'
    ENUM_OTHER = 'Z'

class DeliverToCompID (field_types.String_Type) :
    _tag = '128'

class DeliverToSubID (field_types.String_Type) :
    _tag = '129'

class IOINaturalFlag (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '130'
    ENUM_NOT_NATURAL = 'N'
    ENUM_NATURAL = 'Y'

class QuoteReqID (field_types.String_Type) :
    _tag = '131'

class BidPx (field_types.Price_Type) :
    _tag = '132'

class OfferPx (field_types.Price_Type) :
    _tag = '133'

class BidSize (field_types.Qty_Type) :
    _tag = '134'

class OfferSize (field_types.Qty_Type) :
    _tag = '135'

class NoMiscFees (field_types.int_Type) :
    _tag = '136'

class MiscFeeAmt (field_types.Amt_Type) :
    _tag = '137'

class MiscFeeCurr (field_types.Currency_Type) :
    _tag = '138'

class MiscFeeType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '139'
    ENUM_REGULATORY = '1'
    ENUM_TAX = '2'
    ENUM_LOCAL_COMMISSION = '3'
    ENUM_EXCHANGE_FEES = '4'
    ENUM_STAMP = '5'
    ENUM_LEVY = '6'
    ENUM_OTHER = '7'
    ENUM_MARKUP = '8'
    ENUM_CONSUMPTION_TAX = '9'

class PrevClosePx (field_types.Price_Type) :
    _tag = '140'

class ResetSeqNumFlag (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '141'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class SenderLocationID (field_types.String_Type) :
    _tag = '142'

class TargetLocationID (field_types.String_Type) :
    _tag = '143'

class OnBehalfOfLocationID (field_types.String_Type) :
    _tag = '144'

class DeliverToLocationID (field_types.String_Type) :
    _tag = '145'

class NoRelatedSym (field_types.int_Type) :
    _tag = '146'

class Subject (field_types.String_Type) :
    _tag = '147'

class Headline (field_types.String_Type) :
    _tag = '148'

class URLLink (field_types.String_Type) :
    _tag = '149'

class ExecType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '150'
    ENUM_NEW = '0'
    ENUM_PARTIAL_FILL = '1'
    ENUM_FILL = '2'
    ENUM_DONE_FOR_DAY = '3'
    ENUM_CANCELED = '4'
    ENUM_REPLACED = '5'
    ENUM_PENDING_CANCEL = '6'
    ENUM_STOPPED = '7'
    ENUM_REJECTED = '8'
    ENUM_SUSPENDED = '9'
    ENUM_PENDING_NEW = 'A'
    ENUM_CALCULATED = 'B'
    ENUM_EXPIRED = 'C'
    ENUM_RESTATED = 'D'
    ENUM_PENDING_REPLACE = 'E'

class LeavesQty (field_types.Qty_Type) :
    _tag = '151'

class CashOrderQty (field_types.Qty_Type) :
    _tag = '152'

class AllocAvgPx (field_types.Price_Type) :
    _tag = '153'

class AllocNetMoney (field_types.Amt_Type) :
    _tag = '154'

class SettlCurrFxRate (field_types.float_Type) :
    _tag = '155'

class SettlCurrFxRateCalc (field_types.char_Type) :
    _tag = '156'

class NumDaysInterest (field_types.int_Type) :
    _tag = '157'

class AccruedInterestRate (field_types.float_Type) :
    _tag = '158'

class AccruedInterestAmt (field_types.Amt_Type) :
    _tag = '159'

class SettlInstMode (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '160'
    ENUM_DEFAULT = '0'
    ENUM_STANDING_INSTRUCTIONS_PROVIDED = '1'
    ENUM_SPECIFIC_ALLOCATION_ACCOUNT_OVERRIDING = '2'
    ENUM_SPECIFIC_ALLOCATION_ACCOUNT_STANDING = '3'

class AllocText (field_types.String_Type) :
    _tag = '161'

class SettlInstID (field_types.String_Type) :
    _tag = '162'

class SettlInstTransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '163'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'

class EmailThreadID (field_types.String_Type) :
    _tag = '164'

class SettlInstSource (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '165'
    ENUM_BROKER_CREDIT = '1'
    ENUM_INSTITUTION = '2'

class SettlLocation (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '166'
    ENUM_CEDEL = 'CED'
    ENUM_DEPOSITORY_TRUST_COMPANY = 'DTC'
    ENUM_EURO_CLEAR = 'EUR'
    ENUM_FEDERAL_BOOK_ENTRY = 'FED'
    ENUM_LOCAL_MARKET_SETTLE_LOCATION = 'ISO Country Code'
    ENUM_PHYSICAL = 'PNY'
    ENUM_PARTICIPANT_TRUST_COMPANY = 'PTC'

class SecurityType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '167'
    ENUM_WILDCARD = '?'
    ENUM_BANKERS_ACCEPTANCE = 'BA'
    ENUM_CONVERTIBLE_BOND = 'CB'
    ENUM_CERTIFICATE_OF_DEPOSIT = 'CD'
    ENUM_COLLATERALIZED_MORTGAGE_OBLIGATION = 'CMO'
    ENUM_CORPORATE_BOND = 'CORP'
    ENUM_COMMERCIAL_PAPER = 'CP'
    ENUM_CORPORATE_PRIVATE_PLACEMENT = 'CPP'
    ENUM_COMMON_STOCK = 'CS'
    ENUM_FEDERAL_HOUSING_AUTHORITY = 'FHA'
    ENUM_FEDERAL_HOME_LOAN = 'FHL'
    ENUM_FEDERAL_NATIONAL_MORTGAGE_ASSOCIATION = 'FN'
    ENUM_FOREIGN_EXCHANGE_CONTRACT = 'FOR'
    ENUM_FUTURE = 'FUT'
    ENUM_GOVERNMENT_NATIONAL_MORTGAGE_ASSOCIATION = 'GN'
    ENUM_TREASURIES_AGENCY_DEBENTURE = 'GOVT'
    ENUM_IOETTE_MORTGAGE = 'IET'
    ENUM_MUTUAL_FUND = 'MF'
    ENUM_MORTGAGE_INTEREST_ONLY = 'MIO'
    ENUM_MORTGAGE_PRINCIPAL_ONLY = 'MPO'
    ENUM_MORTGAGE_PRIVATE_PLACEMENT = 'MPP'
    ENUM_MISCELLANEOUS_PASS_THROUGH = 'MPT'
    ENUM_MUNICIPAL_BOND = 'MUNI'
    ENUM_NO_SECURITY_TYPE = 'NONE'
    ENUM_OPTION = 'OPT'
    ENUM_PREFERRED_STOCK = 'PS'
    ENUM_REPURCHASE_AGREEMENT = 'RP'
    ENUM_REVERSE_REPURCHASE_AGREEMENT = 'RVRP'
    ENUM_STUDENT_LOAN_MARKETING_ASSOCIATION = 'SL'
    ENUM_TIME_DEPOSIT = 'TD'
    ENUM_US_TREASURY_BILL_OLD = 'USTB'
    ENUM_WARRANT = 'WAR'
    ENUM_CATS_TIGERS_AND_LIONS = 'ZOO'

class EffectiveTime (field_types.UTCTimestamp_Type) :
    _tag = '168'

class StandInstDbType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '169'
    ENUM_OTHER = 0
    ENUM_DTCSID = 1
    ENUM_THOMSON_ALERT = 2
    ENUM_A_GLOBAL_CUSTODIAN = 3

class StandInstDbName (field_types.String_Type) :
    _tag = '170'

class StandInstDbID (field_types.String_Type) :
    _tag = '171'

class SettlDeliveryType (field_types.int_Type) :
    _tag = '172'

class SettlDepositoryCode (field_types.String_Type) :
    _tag = '173'

class SettlBrkrCode (field_types.String_Type) :
    _tag = '174'

class SettlInstCode (field_types.String_Type) :
    _tag = '175'

class SecuritySettlAgentName (field_types.String_Type) :
    _tag = '176'

class SecuritySettlAgentCode (field_types.String_Type) :
    _tag = '177'

class SecuritySettlAgentAcctNum (field_types.String_Type) :
    _tag = '178'

class SecuritySettlAgentAcctName (field_types.String_Type) :
    _tag = '179'

class SecuritySettlAgentContactName (field_types.String_Type) :
    _tag = '180'

class SecuritySettlAgentContactPhone (field_types.String_Type) :
    _tag = '181'

class CashSettlAgentName (field_types.String_Type) :
    _tag = '182'

class CashSettlAgentCode (field_types.String_Type) :
    _tag = '183'

class CashSettlAgentAcctNum (field_types.String_Type) :
    _tag = '184'

class CashSettlAgentAcctName (field_types.String_Type) :
    _tag = '185'

class CashSettlAgentContactName (field_types.String_Type) :
    _tag = '186'

class CashSettlAgentContactPhone (field_types.String_Type) :
    _tag = '187'

class BidSpotRate (field_types.Price_Type) :
    _tag = '188'

class BidForwardPoints (field_types.PriceOffset_Type) :
    _tag = '189'

class OfferSpotRate (field_types.Price_Type) :
    _tag = '190'

class OfferForwardPoints (field_types.PriceOffset_Type) :
    _tag = '191'

class OrderQty2 (field_types.Qty_Type) :
    _tag = '192'

class FutSettDate2 (field_types.LocalMktDate_Type) :
    _tag = '193'

class LastSpotRate (field_types.Price_Type) :
    _tag = '194'

class LastForwardPoints (field_types.PriceOffset_Type) :
    _tag = '195'

class AllocLinkID (field_types.String_Type) :
    _tag = '196'

class AllocLinkType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '197'
    ENUM_FX_NETTING = 0
    ENUM_FX_SWAP = 1

class SecondaryOrderID (field_types.String_Type) :
    _tag = '198'

class NoIOIQualifiers (field_types.int_Type) :
    _tag = '199'

class MaturityMonthYear (field_types.MonthYear_Type) :
    _tag = '200'

class PutOrCall (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '201'
    ENUM_PUT = 0
    ENUM_CALL = 1

class StrikePrice (field_types.Price_Type) :
    _tag = '202'

class CoveredOrUncovered (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '203'
    ENUM_COVERED = 0
    ENUM_UNCOVERED = 1

class CustomerOrFirm (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '204'
    ENUM_CUSTOMER = 0
    ENUM_FIRM = 1

class MaturityDay (field_types.DayOfMonth_Type) :
    _tag = '205'

class OptAttribute (field_types.char_Type) :
    _tag = '206'

class SecurityExchange (field_types.Exchange_Type) :
    _tag = '207'

class NotifyBrokerOfCredit (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '208'
    ENUM_DETAILS_SHOULD_NOT_BE_COMMUNICATED = 'N'
    ENUM_DETAILS_SHOULD_BE_COMMUNICATED = 'Y'

class AllocHandlInst (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '209'
    ENUM_MATCH = 1
    ENUM_FORWARD = 2
    ENUM_FORWARD_AND_MATCH = 3

class MaxShow (field_types.Qty_Type) :
    _tag = '210'

class PegDifference (field_types.PriceOffset_Type) :
    _tag = '211'

class XmlDataLen (field_types.Length_Type) :
    _tag = '212'

class XmlData (field_types.data_Type) :
    _tag = '213'

class SettlInstRefID (field_types.String_Type) :
    _tag = '214'

class NoRoutingIDs (field_types.int_Type) :
    _tag = '215'

class RoutingType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '216'
    ENUM_TARGET_FIRM = 1
    ENUM_TARGET_LIST = 2
    ENUM_BLOCK_FIRM = 3
    ENUM_BLOCK_LIST = 4

class RoutingID (field_types.String_Type) :
    _tag = '217'

class SpreadToBenchmark (field_types.PriceOffset_Type) :
    _tag = '218'

class Benchmark (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '219'
    ENUM_CURVE = '1'
    ENUM_FIVE_YR = '2'
    ENUM_OLD5 = '3'
    ENUM_TEN_YR = '4'
    ENUM_OLD10 = '5'
    ENUM_THIRTY_YR = '6'
    ENUM_OLD30 = '7'
    ENUM_THREE_MOLIBOR = '8'
    ENUM_SIX_MOLIBOR = '9'

class CouponRate (field_types.float_Type) :
    _tag = '223'

class ContractMultiplier (field_types.float_Type) :
    _tag = '231'

class MDReqID (field_types.String_Type) :
    _tag = '262'

class SubscriptionRequestType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '263'
    ENUM_SNAPSHOT = '0'
    ENUM_SNAPSHOT_AND_UPDATES = '1'
    ENUM_DISABLE_PREVIOUS_SNAPSHOT = '2'

class MarketDepth (field_types.int_Type) :
    _tag = '264'

class MDUpdateType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '265'
    ENUM_FULL_REFRESH = 0
    ENUM_INCREMENTAL_REFRESH = 1

class AggregatedBook (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '266'
    ENUM_BOOK_ENTRIES_SHOULD_NOT_BE_AGGREGATED = 'N'
    ENUM_BOOK_ENTRIES_TO_BE_AGGREGATED = 'Y'

class NoMDEntryTypes (field_types.int_Type) :
    _tag = '267'

class NoMDEntries (field_types.int_Type) :
    _tag = '268'

class MDEntryType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '269'
    ENUM_BID = '0'
    ENUM_OFFER = '1'
    ENUM_TRADE = '2'
    ENUM_INDEX_VALUE = '3'
    ENUM_OPENING_PRICE = '4'
    ENUM_CLOSING_PRICE = '5'
    ENUM_SETTLEMENT_PRICE = '6'
    ENUM_TRADING_SESSION_HIGH_PRICE = '7'
    ENUM_TRADING_SESSION_LOW_PRICE = '8'
    ENUM_TRADING_SESSION_VWAP_PRICE = '9'

class MDEntryPx (field_types.Price_Type) :
    _tag = '270'

class MDEntrySize (field_types.Qty_Type) :
    _tag = '271'

class MDEntryDate (field_types.UTCDate_Type) :
    _tag = '272'

class MDEntryTime (field_types.UTCTimeOnly_Type) :
    _tag = '273'

class TickDirection (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '274'
    ENUM_PLUS_TICK = '0'
    ENUM_ZERO_PLUS_TICK = '1'
    ENUM_MINUS_TICK = '2'
    ENUM_ZERO_MINUS_TICK = '3'

class MDMkt (field_types.Exchange_Type) :
    _tag = '275'

class QuoteCondition (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '276'
    ENUM_OPEN = 'A'
    ENUM_CLOSED = 'B'
    ENUM_EXCHANGE_BEST = 'C'
    ENUM_CONSOLIDATED_BEST = 'D'
    ENUM_LOCKED = 'E'
    ENUM_CROSSED = 'F'
    ENUM_DEPTH = 'G'
    ENUM_FAST_TRADING = 'H'
    ENUM_NON_FIRM = 'I'

class TradeCondition (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '277'
    ENUM_CASH = 'A'
    ENUM_AVERAGE_PRICE_TRADE = 'B'
    ENUM_CASH_TRADE = 'C'
    ENUM_NEXT_DAY = 'D'
    ENUM_OPENING = 'E'
    ENUM_INTRADAY_TRADE_DETAIL = 'F'
    ENUM_RULE127_TRADE = 'G'
    ENUM_RULE155_TRADE = 'H'
    ENUM_SOLD_LAST = 'I'
    ENUM_NEXT_DAY_TRADE = 'J'
    ENUM_OPENED = 'K'
    ENUM_SELLER = 'L'
    ENUM_SOLD = 'M'
    ENUM_STOPPED_STOCK = 'N'

class MDEntryID (field_types.String_Type) :
    _tag = '278'

class MDUpdateAction (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '279'
    ENUM_NEW = '0'
    ENUM_CHANGE = '1'
    ENUM_DELETE = '2'

class MDEntryRefID (field_types.String_Type) :
    _tag = '280'

class MDReqRejReason (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '281'
    ENUM_UNKNOWN_SYMBOL = '0'
    ENUM_DUPLICATE_MD_REQ_ID = '1'
    ENUM_INSUFFICIENT_BANDWIDTH = '2'
    ENUM_INSUFFICIENT_PERMISSIONS = '3'
    ENUM_UNSUPPORTED_SUBSCRIPTION_REQUEST_TYPE = '4'
    ENUM_UNSUPPORTED_MARKET_DEPTH = '5'
    ENUM_UNSUPPORTED_MD_UPDATE_TYPE = '6'
    ENUM_UNSUPPORTED_AGGREGATED_BOOK = '7'
    ENUM_UNSUPPORTED_MD_ENTRY_TYPE = '8'

class MDEntryOriginator (field_types.String_Type) :
    _tag = '282'

class LocationID (field_types.String_Type) :
    _tag = '283'

class DeskID (field_types.String_Type) :
    _tag = '284'

class DeleteReason (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '285'
    ENUM_CANCELLATION = '0'
    ENUM_ERROR = '1'

class OpenCloseSettleFlag (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '286'
    ENUM_DAILY_OPEN = '0'
    ENUM_SESSION_OPEN = '1'
    ENUM_DELIVERY_SETTLEMENT_ENTRY = '2'

class SellerDays (field_types.int_Type) :
    _tag = '287'

class MDEntryBuyer (field_types.String_Type) :
    _tag = '288'

class MDEntrySeller (field_types.String_Type) :
    _tag = '289'

class MDEntryPositionNo (field_types.int_Type) :
    _tag = '290'

class FinancialStatus (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '291'
    ENUM_BANKRUPT = '1'

class CorporateAction (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '292'
    ENUM_EX_DIVIDEND = 'A'
    ENUM_EX_DISTRIBUTION = 'B'
    ENUM_EX_RIGHTS = 'C'
    ENUM_NEW = 'D'
    ENUM_EX_INTEREST = 'E'

class DefBidSize (field_types.Qty_Type) :
    _tag = '293'

class DefOfferSize (field_types.Qty_Type) :
    _tag = '294'

class NoQuoteEntries (field_types.int_Type) :
    _tag = '295'

class NoQuoteSets (field_types.int_Type) :
    _tag = '296'

class QuoteAckStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '297'
    ENUM_ACCEPTED = 0
    ENUM_CANCEL_FOR_SYMBOL = 1
    ENUM_CANCELED_FOR_SECURITY_TYPE = 2
    ENUM_CANCELED_FOR_UNDERLYING = 3
    ENUM_CANCELED_ALL = 4
    ENUM_REJECTED = 5

class QuoteCancelType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '298'
    ENUM_CANCEL_FOR_ONE_OR_MORE_SECURITIES = 1
    ENUM_CANCEL_FOR_SECURITY_TYPE = 2
    ENUM_CANCEL_FOR_UNDERLYING_SECURITY = 3
    ENUM_CANCEL_ALL_QUOTES = 4

class QuoteEntryID (field_types.String_Type) :
    _tag = '299'

class QuoteRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '300'
    ENUM_UNKNOWN_SYMBOL = 1
    ENUM_EXCHANGE = 2
    ENUM_QUOTE_REQUEST_EXCEEDS_LIMIT = 3
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_UNKNOWN_QUOTE = 5
    ENUM_DUPLICATE_QUOTE = 6
    ENUM_INVALID_BID = 7
    ENUM_INVALID_PRICE = 8
    ENUM_NOT_AUTHORIZED_TO_QUOTE_SECURITY = 9

class QuoteResponseLevel (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '301'
    ENUM_NO_ACKNOWLEDGEMENT = 0
    ENUM_ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES = 1
    ENUM_ACKNOWLEDGE_EACH_QUOTE_MESSAGE = 2

class QuoteSetID (field_types.String_Type) :
    _tag = '302'

class QuoteRequestType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '303'
    ENUM_MANUAL = 1
    ENUM_AUTOMATIC = 2

class TotQuoteEntries (field_types.int_Type) :
    _tag = '304'

class UnderlyingIDSource (field_types.String_Type) :
    _tag = '305'

class UnderlyingIssuer (field_types.String_Type) :
    _tag = '306'

class UnderlyingSecurityDesc (field_types.String_Type) :
    _tag = '307'

class UnderlyingSecurityExchange (field_types.Exchange_Type) :
    _tag = '308'

class UnderlyingSecurityID (field_types.String_Type) :
    _tag = '309'

class UnderlyingSecurityType (field_types.String_Type) :
    _tag = '310'

class UnderlyingSymbol (field_types.String_Type) :
    _tag = '311'

class UnderlyingSymbolSfx (field_types.String_Type) :
    _tag = '312'

class UnderlyingMaturityMonthYear (field_types.MonthYear_Type) :
    _tag = '313'

class UnderlyingMaturityDay (field_types.DayOfMonth_Type) :
    _tag = '314'

class UnderlyingPutOrCall (field_types.int_Type) :
    _tag = '315'

class UnderlyingStrikePrice (field_types.Price_Type) :
    _tag = '316'

class UnderlyingOptAttribute (field_types.char_Type) :
    _tag = '317'

class UnderlyingCurrency (field_types.Currency_Type) :
    _tag = '318'

class RatioQty (field_types.Qty_Type) :
    _tag = '319'

class SecurityReqID (field_types.String_Type) :
    _tag = '320'

class SecurityRequestType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '321'
    ENUM_REQUEST_SECURITY_IDENTITY_AND_SPECIFICATIONS = 0
    ENUM_REQUEST_SECURITY_IDENTITY_FOR_SPECIFICATIONS = 1
    ENUM_REQUEST_LIST_SECURITY_TYPES = 2
    ENUM_REQUEST_LIST_SECURITIES = 3

class SecurityResponseID (field_types.String_Type) :
    _tag = '322'

class SecurityResponseType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '323'
    ENUM_ACCEPT_AS_IS = 1
    ENUM_ACCEPT_WITH_REVISIONS = 2
    ENUM_LIST_OF_SECURITY_TYPES_RETURNED_PER_REQUEST = 3
    ENUM_LIST_OF_SECURITIES_RETURNED_PER_REQUEST = 4
    ENUM_REJECT_SECURITY_PROPOSAL = 5
    ENUM_CANNOT_MATCH_SELECTION_CRITERIA = 6

class SecurityStatusReqID (field_types.String_Type) :
    _tag = '324'

class UnsolicitedIndicator (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '325'
    ENUM_MESSAGE_IS_BEING_SENT_AS_A_RESULT_OF_A_PRIOR_REQUEST = 'N'
    ENUM_MESSAGE_IS_BEING_SENT_UNSOLICITED = 'Y'

class SecurityTradingStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '326'
    ENUM_OPENING_DELAY = 1
    ENUM_MARKET_ON_CLOSE_IMBALANCE_SELL = 10
    ENUM_NO_MARKET_IMBALANCE = 12
    ENUM_NO_MARKET_ON_CLOSE_IMBALANCE = 13
    ENUM_ITS_PRE_OPENING = 14
    ENUM_NEW_PRICE_INDICATION = 15
    ENUM_TRADE_DISSEMINATION_TIME = 16
    ENUM_READY_TO_TRADE = 17
    ENUM_NOT_AVAILABLE_FOR_TRADING = 18
    ENUM_NOT_TRADED_ON_THIS_MARKET = 19
    ENUM_TRADING_HALT = 2
    ENUM_UNKNOWN_OR_INVALID = 20
    ENUM_RESUME = 3
    ENUM_NO_OPEN = 4
    ENUM_PRICE_INDICATION = 5
    ENUM_TRADING_RANGE_INDICATION = 6
    ENUM_MARKET_IMBALANCE_BUY = 7
    ENUM_MARKET_IMBALANCE_SELL = 8
    ENUM_MARKET_ON_CLOSE_IMBALANCE_BUY = 9

class HaltReason (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '327'
    ENUM_NEWS_DISSEMINATION = 'D'
    ENUM_ORDER_INFLUX = 'E'
    ENUM_ORDER_IMBALANCE = 'I'
    ENUM_ADDITIONAL_INFORMATION = 'M'
    ENUM_NEWS_PENDING = 'P'
    ENUM_EQUIPMENT_CHANGEOVER = 'X'

class InViewOfCommon (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '328'
    ENUM_HALT_WAS_NOT_RELATED_TO_A_HALT_OF_THE_COMMON_STOCK = 'N'
    ENUM_HALT_WAS_DUE_TO_COMMON_STOCK_BEING_HALTED = 'Y'

class DueToRelated (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '329'
    ENUM_NOT_RELATED_TO_SECURITY_HALT = 'N'
    ENUM_RELATED_TO_SECURITY_HALT = 'Y'

class BuyVolume (field_types.Qty_Type) :
    _tag = '330'

class SellVolume (field_types.Qty_Type) :
    _tag = '331'

class HighPx (field_types.Price_Type) :
    _tag = '332'

class LowPx (field_types.Price_Type) :
    _tag = '333'

class Adjustment (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '334'
    ENUM_CANCEL = 1
    ENUM_ERROR = 2
    ENUM_CORRECTION = 3

class TradSesReqID (field_types.String_Type) :
    _tag = '335'

class TradingSessionID (field_types.String_Type) :
    _tag = '336'

class ContraTrader (field_types.String_Type) :
    _tag = '337'

class TradSesMethod (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '338'
    ENUM_ELECTRONIC = 1
    ENUM_OPEN_OUTCRY = 2
    ENUM_TWO_PARTY = 3

class TradSesMode (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '339'
    ENUM_TESTING = 1
    ENUM_SIMULATED = 2
    ENUM_PRODUCTION = 3

class TradSesStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '340'
    ENUM_HALTED = 1
    ENUM_OPEN = 2
    ENUM_CLOSED = 3
    ENUM_PRE_OPEN = 4
    ENUM_PRE_CLOSE = 5

class TradSesStartTime (field_types.UTCTimestamp_Type) :
    _tag = '341'

class TradSesOpenTime (field_types.UTCTimestamp_Type) :
    _tag = '342'

class TradSesPreCloseTime (field_types.UTCTimestamp_Type) :
    _tag = '343'

class TradSesCloseTime (field_types.UTCTimestamp_Type) :
    _tag = '344'

class TradSesEndTime (field_types.UTCTimestamp_Type) :
    _tag = '345'

class NumberOfOrders (field_types.int_Type) :
    _tag = '346'

class MessageEncoding (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '347'
    ENUM_EUCJP = 'EUC-JP'
    ENUM_ISO2022_JP = 'ISO-2022-JP'
    ENUM_SHIFT_JIS = 'Shift_JIS'
    ENUM_UTF8 = 'UTF-8'

class EncodedIssuerLen (field_types.Length_Type) :
    _tag = '348'

class EncodedIssuer (field_types.data_Type) :
    _tag = '349'

class EncodedSecurityDescLen (field_types.Length_Type) :
    _tag = '350'

class EncodedSecurityDesc (field_types.data_Type) :
    _tag = '351'

class EncodedListExecInstLen (field_types.Length_Type) :
    _tag = '352'

class EncodedListExecInst (field_types.data_Type) :
    _tag = '353'

class EncodedTextLen (field_types.Length_Type) :
    _tag = '354'

class EncodedText (field_types.data_Type) :
    _tag = '355'

class EncodedSubjectLen (field_types.Length_Type) :
    _tag = '356'

class EncodedSubject (field_types.data_Type) :
    _tag = '357'

class EncodedHeadlineLen (field_types.Length_Type) :
    _tag = '358'

class EncodedHeadline (field_types.data_Type) :
    _tag = '359'

class EncodedAllocTextLen (field_types.Length_Type) :
    _tag = '360'

class EncodedAllocText (field_types.data_Type) :
    _tag = '361'

class EncodedUnderlyingIssuerLen (field_types.Length_Type) :
    _tag = '362'

class EncodedUnderlyingIssuer (field_types.data_Type) :
    _tag = '363'

class EncodedUnderlyingSecurityDescLen (field_types.Length_Type) :
    _tag = '364'

class EncodedUnderlyingSecurityDesc (field_types.data_Type) :
    _tag = '365'

class AllocPrice (field_types.Price_Type) :
    _tag = '366'

class QuoteSetValidUntilTime (field_types.UTCTimestamp_Type) :
    _tag = '367'

class QuoteEntryRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '368'
    ENUM_UNKNOWN_SYMBOL = 1
    ENUM_EXCHANGE = 2
    ENUM_QUOTE_EXCEEDS_LIMIT = 3
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_UNKNOWN_QUOTE = 5
    ENUM_DUPLICATE_QUOTE = 6
    ENUM_INVALID_BID_ASK_SPREAD = 7
    ENUM_INVALID_PRICE = 8
    ENUM_NOT_AUTHORIZED_TO_QUOTE_SECURITY = 9

class LastMsgSeqNumProcessed (field_types.int_Type) :
    _tag = '369'

class OnBehalfOfSendingTime (field_types.UTCTimestamp_Type) :
    _tag = '370'

class RefTagID (field_types.int_Type) :
    _tag = '371'

class RefMsgType (field_types.String_Type) :
    _tag = '372'

class SessionRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '373'
    ENUM_INVALID_TAG_NUMBER = 0
    ENUM_REQUIRED_TAG_MISSING = 1
    ENUM_SENDING_TIME_ACCURACY_PROBLEM = 10
    ENUM_INVALID_MSG_TYPE = 11
    ENUM_TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE = 2
    ENUM_UNDEFINED_TAG = 3
    ENUM_TAG_SPECIFIED_WITHOUT_A_VALUE = 4
    ENUM_VALUE_IS_INCORRECT = 5
    ENUM_INCORRECT_DATA_FORMAT_FOR_VALUE = 6
    ENUM_DECRYPTION_PROBLEM = 7
    ENUM_SIGNATURE_PROBLEM = 8
    ENUM_COMP_ID_PROBLEM = 9

class BidRequestTransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '374'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'

class ContraBroker (field_types.String_Type) :
    _tag = '375'

class ComplianceID (field_types.String_Type) :
    _tag = '376'

class SolicitedFlag (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '377'
    ENUM_WAS_NOT_SOLICITED = 'N'
    ENUM_WAS_SOLICITED = 'Y'

class ExecRestatementReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '378'
    ENUM_GT_CORPORATE_ACTION = 0
    ENUM_GT_RENEWAL = 1
    ENUM_VERBAL_CHANGE = 2
    ENUM_REPRICING_OF_ORDER = 3
    ENUM_BROKER_OPTION = 4
    ENUM_PARTIAL_DECLINE_OF_ORDER_QTY = 5

class BusinessRejectRefID (field_types.String_Type) :
    _tag = '379'

class BusinessRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '380'
    ENUM_OTHER = 0
    ENUM_UNKNOWN_ID = 1
    ENUM_UNKNOWN_SECURITY = 2
    ENUM_UNSUPPORTED_MESSAGE_TYPE = 3
    ENUM_APPLICATION_NOT_AVAILABLE = 4
    ENUM_CONDITIONALLY_REQUIRED_FIELD_MISSING = 5

class GrossTradeAmt (field_types.Amt_Type) :
    _tag = '381'

class NoContraBrokers (field_types.int_Type) :
    _tag = '382'

class MaxMessageSize (field_types.int_Type) :
    _tag = '383'

class NoMsgTypes (field_types.int_Type) :
    _tag = '384'

class MsgDirection (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '385'
    ENUM_RECEIVE = 'R'
    ENUM_SEND = 'S'

class NoTradingSessions (field_types.int_Type) :
    _tag = '386'

class TotalVolumeTraded (field_types.Qty_Type) :
    _tag = '387'

class DiscretionInst (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '388'
    ENUM_RELATED_TO_DISPLAYED_PRICE = '0'
    ENUM_RELATED_TO_MARKET_PRICE = '1'
    ENUM_RELATED_TO_PRIMARY_PRICE = '2'
    ENUM_RELATED_TO_LOCAL_PRIMARY_PRICE = '3'
    ENUM_RELATED_TO_MIDPOINT_PRICE = '4'
    ENUM_RELATED_TO_LAST_TRADE_PRICE = '5'

class DiscretionOffset (field_types.PriceOffset_Type) :
    _tag = '389'

class BidID (field_types.String_Type) :
    _tag = '390'

class ClientBidID (field_types.String_Type) :
    _tag = '391'

class ListName (field_types.String_Type) :
    _tag = '392'

class TotalNumSecurities (field_types.int_Type) :
    _tag = '393'

class BidType (field_types.int_Type) :
    _tag = '394'

class NumTickets (field_types.int_Type) :
    _tag = '395'

class SideValue1 (field_types.Amt_Type) :
    _tag = '396'

class SideValue2 (field_types.Amt_Type) :
    _tag = '397'

class NoBidDescriptors (field_types.int_Type) :
    _tag = '398'

class BidDescriptorType (field_types.int_Type) :
    _tag = '399'

class BidDescriptor (field_types.String_Type) :
    _tag = '400'

class SideValueInd (field_types.int_Type) :
    _tag = '401'

class LiquidityPctLow (field_types.float_Type) :
    _tag = '402'

class LiquidityPctHigh (field_types.float_Type) :
    _tag = '403'

class LiquidityValue (field_types.Amt_Type) :
    _tag = '404'

class EFPTrackingError (field_types.float_Type) :
    _tag = '405'

class FairValue (field_types.Amt_Type) :
    _tag = '406'

class OutsideIndexPct (field_types.float_Type) :
    _tag = '407'

class ValueOfFutures (field_types.Amt_Type) :
    _tag = '408'

class LiquidityIndType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '409'
    ENUM_FIVE_DAY_MOVING_AVERAGE = 1
    ENUM_TWENTY_DAY_MOVING_AVERAGE = 2
    ENUM_NORMAL_MARKET_SIZE = 3
    ENUM_OTHER = 4

class WtAverageLiquidity (field_types.float_Type) :
    _tag = '410'

class ExchangeForPhysical (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '411'
    ENUM_FALSE = 'N'
    ENUM_TRUE = 'Y'

class OutMainCntryUIndex (field_types.Amt_Type) :
    _tag = '412'

class CrossPercent (field_types.float_Type) :
    _tag = '413'

class ProgRptReqs (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '414'
    ENUM_BUY_SIDE_REQUESTS = 1
    ENUM_SELL_SIDE_SENDS = 2
    ENUM_REAL_TIME_EXECUTION_REPORTS = 3

class ProgPeriodInterval (field_types.int_Type) :
    _tag = '415'

class IncTaxInd (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '416'
    ENUM_NET = 1
    ENUM_GROSS = 2

class NumBidders (field_types.int_Type) :
    _tag = '417'

class TradeType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '418'
    ENUM_AGENCY = 'A'
    ENUM_VWAP_GUARANTEE = 'G'
    ENUM_GUARANTEED_CLOSE = 'J'
    ENUM_RISK_TRADE = 'R'

class BasisPxType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '419'
    ENUM_CLOSING_PRICE_AT_MORNING_SESSION = '2'
    ENUM_CLOSING_PRICE = '3'
    ENUM_CURRENT_PRICE = '4'
    ENUM_SQ = '5'
    ENUM_VWAP_THROUGH_A_DAY = '6'
    ENUM_VWAP_THROUGH_A_MORNING_SESSION = '7'
    ENUM_VWAP_THROUGH_AN_AFTERNOON_SESSION = '8'
    ENUM_VWAP_THROUGH_A_DAY_EXCEPT = '9'
    ENUM_VWAP_THROUGH_A_MORNING_SESSION_EXCEPT = 'A'
    ENUM_VWAP_THROUGH_AN_AFTERNOON_SESSION_EXCEPT = 'B'
    ENUM_STRIKE = 'C'
    ENUM_OPEN = 'D'
    ENUM_OTHERS = 'Z'

class NoBidComponents (field_types.int_Type) :
    _tag = '420'

class Country (field_types.String_Type) :
    _tag = '421'

class TotNoStrikes (field_types.int_Type) :
    _tag = '422'

class PriceType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '423'
    ENUM_PERCENTAGE = 1
    ENUM_PER_UNIT = 2
    ENUM_FIXED_AMOUNT = 3

class DayOrderQty (field_types.Qty_Type) :
    _tag = '424'

class DayCumQty (field_types.Qty_Type) :
    _tag = '425'

class DayAvgPx (field_types.Price_Type) :
    _tag = '426'

class GTBookingInst (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '427'
    ENUM_BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION = 0
    ENUM_ACCUMULATE_UNTIL_FILLED_OR_EXPIRED = 1
    ENUM_ACCUMULATE_UNTIL_VERBALLLY_NOTIFIED_OTHERWISE = 2

class NoStrikes (field_types.int_Type) :
    _tag = '428'

class ListStatusType (field_types.int_Type) :
    _tag = '429'

class NetGrossInd (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '430'
    ENUM_NET = 1
    ENUM_GROSS = 2

class ListOrderStatus (field_types.int_Type) :
    _tag = '431'

class ExpireDate (field_types.LocalMktDate_Type) :
    _tag = '432'

class ListExecInstType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '433'
    ENUM_IMMEDIATE = '1'
    ENUM_WAIT_FOR_INSTRUCTION = '2'

class CxlRejResponseTo (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '434'
    ENUM_ORDER_CANCEL_REQUEST = '1'
    ENUM_ORDER_CANCEL = '2'

class UnderlyingCouponRate (field_types.float_Type) :
    _tag = '435'

class UnderlyingContractMultiplier (field_types.float_Type) :
    _tag = '436'

class ContraTradeQty (field_types.Qty_Type) :
    _tag = '437'

class ContraTradeTime (field_types.UTCTimestamp_Type) :
    _tag = '438'

class ClearingFirm (field_types.String_Type) :
    _tag = '439'

class ClearingAccount (field_types.String_Type) :
    _tag = '440'

class LiquidityNumSecurities (field_types.int_Type) :
    _tag = '441'

class MultiLegReportingType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '442'
    ENUM_SINGLE_SECURITY = '1'
    ENUM_INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY = '2'
    ENUM_MULTI_LEG_SECURITY = '3'

class StrikeTime (field_types.UTCTimestamp_Type) :
    _tag = '443'

class ListStatusText (field_types.String_Type) :
    _tag = '444'

class EncodedListStatusTextLen (field_types.Length_Type) :
    _tag = '445'

class EncodedListStatusText (field_types.data_Type) :
    _tag = '446'
