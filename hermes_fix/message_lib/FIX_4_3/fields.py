from . import field_types
from ... import fix_enum_type

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
    ENUM_CROSS = 'X'
    ENUM_TRADE = 'T'

class AdvTransType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '5'
    ENUM_NEW = 'N'
    ENUM_CANCEL = 'C'
    ENUM_REPLACE = 'R'

class AvgPx (field_types.Price_Type) :
    _tag = '6'

class BeginSeqNo (field_types.SeqNum_Type) :
    _tag = '7'

class BeginString (field_types.String_Type) :
    _tag = '8'

class BodyLength (field_types.Length_Type) :
    _tag = '9'

class CheckSum (field_types.String_Type) :
    _tag = '10'

class ClOrdID (field_types.String_Type) :
    _tag = '11'

class Commission (field_types.Amt_Type) :
    _tag = '12'

class CommType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '13'
    ENUM_POINTS_PER_BOND_OR_CONTRACT = '6'
    ENUM_PER_UNIT = '1'
    ENUM_PERCENT = '2'
    ENUM_ABSOLUTE = '3'
    ENUM_PERCENTAGE_WAIVED_ENHANCED_UNITS = '5'
    ENUM_PERCENTAGE_WAIVED_CASH_DISCOUNT = '4'

class CumQty (field_types.Qty_Type) :
    _tag = '14'

class Currency (field_types.Currency_Type) :
    _tag = '15'

class EndSeqNo (field_types.SeqNum_Type) :
    _tag = '16'

class ExecID (field_types.String_Type) :
    _tag = '17'

class ExecInst (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '18'
    ENUM_TRY_TO_STOP = 'Y'
    ENUM_MID_PRICE_PEG = 'M'
    ENUM_MARKET_PEG = 'P'
    ENUM_CANCEL_ON_SYSTEM_FAILURE = 'Q'
    ENUM_PRIMARY_PEG = 'R'
    ENUM_SUSPEND = 'S'
    ENUM_CUSTOMER_DISPLAY_INSTRUCTION = 'U'
    ENUM_NETTING = 'V'
    ENUM_PEG_TO_VWAP = 'W'
    ENUM_TRADE_ALONG = 'X'
    ENUM_PERCENT_OF_VOLUME = 'D'
    ENUM_STAY_ON_OFFER_SIDE = '0'
    ENUM_WORK = '2'
    ENUM_OVER_THE_DAY = '4'
    ENUM_HELD = '5'
    ENUM_PARTICIPATE_DO_NOT_INITIATE = '6'
    ENUM_STRICT_SCALE = '7'
    ENUM_TRY_TO_SCALE = '8'
    ENUM_STAY_ON_BID_SIDE = '9'
    ENUM_NO_CROSS = 'A'
    ENUM_OPENING_PEG = 'O'
    ENUM_CALL_FIRST = 'C'
    ENUM_NON_NEGOTIABLE = 'N'
    ENUM_DO_NOT_INCREASE = 'E'
    ENUM_DO_NOT_REDUCE = 'F'
    ENUM_ALL_OR_NONE = 'G'
    ENUM_REINSTATE_ON_SYSTEM_FAILURE = 'H'
    ENUM_INSTITUTIONS_ONLY = 'I'
    ENUM_REINSTATE_ON_TRADING_HALT = 'J'
    ENUM_CANCEL_ON_TRADING_HALT = 'K'
    ENUM_LAST_PEG = 'L'
    ENUM_GO_ALONG = '3'
    ENUM_OK_TO_CROSS = 'B'
    ENUM_NOT_HELD = '1'

class ExecRefID (field_types.String_Type) :
    _tag = '19'

class HandlInst (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '21'
    ENUM_AUTOMATED_EXECUTION_NO_INTERVENTION = '1'
    ENUM_AUTOMATED_EXECUTION_INTERVENTION_OK = '2'
    ENUM_MANUAL_ORDER = '3'

class SecurityIDSource (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '22'
    ENUM_SICOVAM = 'E'
    ENUM_SEDOL = '2'
    ENUM_CUSIP = '1'
    ENUM_QUIK = '3'
    ENUM_BELGIAN = 'F'
    ENUM_VALOREN = 'D'
    ENUM_DUTCH = 'C'
    ENUM_WERTPAPIER = 'B'
    ENUM_BLOOMBERG_SYMBOL = 'A'
    ENUM_CONSOLIDATED_TAPE_ASSOCIATION = '9'
    ENUM_EXCHANGE_SYMBOL = '8'
    ENUM_ISO_COUNTRY_CODE = '7'
    ENUM_ISO_CURRENCY_CODE = '6'
    ENUM_RIC_CODE = '5'
    ENUM_ISIN_NUMBER = '4'
    ENUM_COMMON = 'G'

class IOIid (field_types.String_Type) :
    _tag = '23'

class IOIQltyInd (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '25'
    ENUM_MEDIUM = 'M'
    ENUM_HIGH = 'H'
    ENUM_LOW = 'L'

class IOIRefID (field_types.String_Type) :
    _tag = '26'

class IOIQty (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
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
    ENUM_PRINCIPAL = '4'
    ENUM_CROSS_AS_PRINCIPAL = '3'
    ENUM_AGENT = '1'
    ENUM_CROSS_AS_AGENT = '2'

class LastMkt (field_types.Exchange_Type) :
    _tag = '30'

class LastPx (field_types.Price_Type) :
    _tag = '31'

class LastQty (field_types.Qty_Type) :
    _tag = '32'

class LinesOfText (field_types.NumInGroup_Type) :
    _tag = '33'

class MsgSeqNum (field_types.SeqNum_Type) :
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
    ENUM_QUOTE_STATUS_REQUEST = 'a'
    ENUM_LOGON = 'A'
    ENUM_DERIVATIVE_SECURITY_LIST = 'AA'
    ENUM_NEW_ORDER_MULTILEG = 'AB'
    ENUM_MULTILEG_ORDER_CANCEL_REPLACE = 'AC'
    ENUM_TRADE_CAPTURE_REPORT_REQUEST = 'AD'
    ENUM_TRADE_CAPTURE_REPORT = 'AE'
    ENUM_ORDER_MASS_STATUS_REQUEST = 'AF'
    ENUM_QUOTE_REQUEST_REJECT = 'AG'
    ENUM_RFQ_REQUEST = 'AH'
    ENUM_QUOTE_STATUS_REPORT = 'AI'
    ENUM_MASS_QUOTE_ACKNOWLEDGEMENT = 'b'
    ENUM_NEWS = 'B'
    ENUM_SECURITY_DEFINITION_REQUEST = 'c'
    ENUM_EMAIL = 'C'
    ENUM_SECURITY_DEFINITION = 'd'
    ENUM_NEW_ORDER_SINGLE = 'D'
    ENUM_SECURITY_STATUS_REQUEST = 'e'
    ENUM_NEW_ORDER_LIST = 'E'
    ENUM_SECURITY_STATUS = 'f'
    ENUM_ORDER_CANCEL_REQUEST = 'F'
    ENUM_ORDER_CANCEL_REPLACE_REQUEST = 'G'
    ENUM_TRADING_SESSION_STATUS_REQUEST = 'g'
    ENUM_TRADING_SESSION_STATUS = 'h'
    ENUM_ORDER_STATUS_REQUEST = 'H'
    ENUM_MASS_QUOTE = 'i'
    ENUM_BUSINESS_MESSAGE_REJECT = 'j'
    ENUM_ALLOCATION_INSTRUCTION = 'J'
    ENUM_LIST_CANCEL_REQUEST = 'K'
    ENUM_BID_REQUEST = 'k'
    ENUM_BID_RESPONSE = 'l'
    ENUM_LIST_EXECUTE = 'L'
    ENUM_LIST_STRIKE_PRICE = 'm'
    ENUM_LIST_STATUS_REQUEST = 'M'
    ENUM_LIST_STATUS = 'N'
    ENUM_XML_NON_FIX = 'n'
    ENUM_REGISTRATION_INSTRUCTIONS = 'o'
    ENUM_ALLOCATION_INSTRUCTION_ACK = 'P'
    ENUM_REGISTRATION_INSTRUCTIONS_RESPONSE = 'p'
    ENUM_ORDER_MASS_CANCEL_REQUEST = 'q'
    ENUM_DONT_KNOW_TRADE = 'Q'
    ENUM_ORDER_MASS_CANCEL_REPORT = 'r'
    ENUM_QUOTE_REQUEST = 'R'
    ENUM_NEW_ORDER_CROSS = 's'
    ENUM_QUOTE = 'S'
    ENUM_CROSS_ORDER_CANCEL_REPLACE_REQUEST = 't'
    ENUM_SETTLEMENT_INSTRUCTIONS = 'T'
    ENUM_CROSS_ORDER_CANCEL_REQUEST = 'u'
    ENUM_SECURITY_TYPE_REQUEST = 'v'
    ENUM_MARKET_DATA_REQUEST = 'V'
    ENUM_SECURITY_TYPES = 'w'
    ENUM_MARKET_DATA_SNAPSHOT_FULL_REFRESH = 'W'
    ENUM_SECURITY_LIST_REQUEST = 'x'
    ENUM_MARKET_DATA_INCREMENTAL_REFRESH = 'X'
    ENUM_SECURITY_LIST = 'y'
    ENUM_MARKET_DATA_REQUEST_REJECT = 'Y'
    ENUM_DERIVATIVE_SECURITY_LIST_REQUEST = 'z'
    ENUM_QUOTE_CANCEL = 'Z'

class NewSeqNo (field_types.SeqNum_Type) :
    _tag = '36'

class OrderID (field_types.String_Type) :
    _tag = '37'

class OrderQty (field_types.Qty_Type) :
    _tag = '38'

class OrdStatus (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '39'
    ENUM_NEW = '0'
    ENUM_PARTIALLY_FILLED = '1'
    ENUM_REPLACED = '5'
    ENUM_FILLED = '2'
    ENUM_PENDING_CANCEL = '6'
    ENUM_STOPPED = '7'
    ENUM_REJECTED = '8'
    ENUM_SUSPENDED = '9'
    ENUM_PENDING_NEW = 'A'
    ENUM_CALCULATED = 'B'
    ENUM_EXPIRED = 'C'
    ENUM_ACCEPTED_FOR_BIDDING = 'D'
    ENUM_PENDING_REPLACE = 'E'
    ENUM_DONE_FOR_DAY = '3'
    ENUM_CANCELED = '4'

class OrdType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '40'
    ENUM_PREVIOUSLY_QUOTED = 'D'
    ENUM_LIMIT = '2'
    ENUM_STOP = '3'
    ENUM_STOP_LIMIT = '4'
    ENUM_MARKET_ON_CLOSE = '5'
    ENUM_WITH_OR_WITHOUT = '6'
    ENUM_LIMIT_OR_BETTER = '7'
    ENUM_LIMIT_WITH_OR_WITHOUT = '8'
    ENUM_ON_BASIS = '9'
    ENUM_ON_CLOSE = 'A'
    ENUM_MARKET = '1'
    ENUM_FOREX_MARKET = 'C'
    ENUM_FOREX_LIMIT = 'F'
    ENUM_PREVIOUSLY_INDICATED = 'E'
    ENUM_FOREX_SWAP = 'G'
    ENUM_FUNARI = 'I'
    ENUM_MARKET_IF_TOUCHED = 'J'
    ENUM_MARKET_WITH_LEFT_OVER_AS_LIMIT = 'K'
    ENUM_PREVIOUS_FUND_VALUATION_POINT = 'L'
    ENUM_NEXT_FUND_VALUATION_POINT = 'M'
    ENUM_PEGGED = 'P'
    ENUM_LIMIT_ON_CLOSE = 'B'
    ENUM_FOREX_PREVIOUSLY_QUOTED = 'H'

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

class RefSeqNum (field_types.SeqNum_Type) :
    _tag = '45'

class Rule80A (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '47'
    ENUM_AGENT_FOR_OTHER_MEMBER = 'N'
    ENUM_SHORT_EXEMPT_TRANSACTION_A_TYPE = 'B'
    ENUM_PROGRAM_ORDER_MEMBER = 'D'
    ENUM_SHORT_EXEMPT_TRANSACTION_FOR_PRINCIPAL = 'E'
    ENUM_SHORT_EXEMPT_TRANSACTION_W_TYPE = 'F'
    ENUM_SHORT_EXEMPT_TRANSACTION_I_TYPE = 'H'
    ENUM_INDIVIDUAL_INVESTOR = 'I'
    ENUM_PROPRIETARY_ALGO = 'J'
    ENUM_AGENCY_ALGO = 'K'
    ENUM_PROGRAM_ORDER_OTHER_MEMBER = 'M'
    ENUM_AGENCY_SINGLE_ORDER = 'A'
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
    ENUM_SHORT_EXEMPT_TRANSACTION_MEMBER_AFFLIATED = 'L'
    ENUM_PROPRIETARY_NON_ALGO = 'C'

class SecurityID (field_types.String_Type) :
    _tag = '48'

class SenderCompID (field_types.String_Type) :
    _tag = '49'

class SenderSubID (field_types.String_Type) :
    _tag = '50'

class SendingTime (field_types.UTCTimestamp_Type) :
    _tag = '52'

class Quantity (field_types.Qty_Type) :
    _tag = '53'

class Side (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '54'
    ENUM_SELL_SHORT_EXEMPT = '6'
    ENUM_AS_DEFINED = 'B'
    ENUM_OPPOSITE = 'C'
    ENUM_CROSS = '8'
    ENUM_CROSS_SHORT = '9'
    ENUM_BUY = '1'
    ENUM_SELL = '2'
    ENUM_BUY_MINUS = '3'
    ENUM_SELL_PLUS = '4'
    ENUM_CROSS_SHORT_EXEMPT = 'A'
    ENUM_SELL_SHORT = '5'
    ENUM_UNDISCLOSED = '7'

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
    ENUM_AT_THE_CLOSE = '7'
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
    ENUM_FLASH = '1'
    ENUM_BACKGROUND = '2'
    ENUM_NORMAL = '0'

class ValidUntilTime (field_types.UTCTimestamp_Type) :
    _tag = '62'

class SettlmntTyp (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '63'
    ENUM_T_PLUS4 = '5'
    ENUM_T1 = 'A'
    ENUM_FUTURE = '6'
    ENUM_T_PLUS2 = '3'
    ENUM_NEXT_DAY = '2'
    ENUM_SELLERS_OPTION = '8'
    ENUM_CASH = '1'
    ENUM_WHEN_AND_IF_ISSUED = '7'
    ENUM_REGULAR = '0'
    ENUM_T_PLUS5 = '9'
    ENUM_T_PLUS3 = '4'

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
    ENUM_CALCULATED_WITHOUT_PRELIMINARY = '5'
    ENUM_CALCULATED = '4'
    ENUM_PRELIMINARY = '3'
    ENUM_CANCEL = '2'
    ENUM_REPLACE = '1'
    ENUM_NEW = '0'

class RefAllocID (field_types.String_Type) :
    _tag = '72'

class NoOrders (field_types.NumInGroup_Type) :
    _tag = '73'

class AvgPrxPrecision (field_types.int_Type) :
    _tag = '74'

class TradeDate (field_types.LocalMktDate_Type) :
    _tag = '75'

class PositionEffect (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '77'
    ENUM_FIFO = 'F'
    ENUM_ROLLED = 'R'
    ENUM_CLOSE = 'C'
    ENUM_OPEN = 'O'

class NoAllocs (field_types.NumInGroup_Type) :
    _tag = '78'

class AllocAccount (field_types.String_Type) :
    _tag = '79'

class AllocQty (field_types.Qty_Type) :
    _tag = '80'

class ProcessCode (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '81'
    ENUM_PLAN_SPONSOR = '6'
    ENUM_REGULAR = '0'
    ENUM_SOFT_DOLLAR = '1'
    ENUM_STEP_IN = '2'
    ENUM_STEP_OUT = '3'
    ENUM_SOFT_DOLLAR_STEP_IN = '4'
    ENUM_SOFT_DOLLAR_STEP_OUT = '5'

class NoRpts (field_types.NumInGroup_Type) :
    _tag = '82'

class RptSeq (field_types.int_Type) :
    _tag = '83'

class CxlQty (field_types.Qty_Type) :
    _tag = '84'

class AllocStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '87'
    ENUM_BLOCK_LEVEL_REJECT = 1
    ENUM_ACCOUNT_LEVEL_REJECT = 2
    ENUM_RECEIVED = 3
    ENUM_ACCEPTED = 0

class AllocRejCode (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '88'
    ENUM_UNKNOWN_ACCOUNT = 0
    ENUM_UNKNOWN_LIST_ID = 6
    ENUM_UNKNOWN_EXECUTING_BROKER_MNEMONIC = 3
    ENUM_UNKNOWN_ORDER_ID = 5
    ENUM_OTHER_SEE_TEXT = 7
    ENUM_COMMISSION_DIFFERENCE = 4
    ENUM_INCORRECT_QUANTITY = 1
    ENUM_INCORRECT_AVERAGEG_PRICE = 2

class Signature (field_types.data_Type) :
    _tag = '89'

class SecureDataLen (field_types.Length_Type) :
    _tag = '90'

class SecureData (field_types.data_Type) :
    _tag = '91'

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
    ENUM_DES = 2
    ENUM_PEM = 6
    ENUM_PGPDESMD5 = 5
    ENUM_PKCSDES = 3
    ENUM_NONE = 0
    ENUM_PKCS = 1
    ENUM_PGPDES = 4

class StopPx (field_types.Price_Type) :
    _tag = '99'

class ExDestination (field_types.Exchange_Type) :
    _tag = '100'

class CxlRejReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '102'
    ENUM_UNKNOWN_ORDER = 1
    ENUM_TOO_LATE_TO_CANCEL = 0
    ENUM_DUPLICATE_CL_ORD_ID = 6
    ENUM_ORIG_ORD_MOD_TIME = 5
    ENUM_UNABLE_TO_PROCESS_ORDER_MASS_CANCEL_REQUEST = 4
    ENUM_ORDER_ALREADY_IN_PENDING_STATUS = 3
    ENUM_BROKER_CREDIT = 2

class OrdRejReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '103'
    ENUM_EXCHANGE_CLOSED = 2
    ENUM_UNKNOWN_SYMBOL = 1
    ENUM_ORDER_EXCEEDS_LIMIT = 3
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_UNKNOWN_ORDER = 5
    ENUM_DUPLICATE_OF_A_VERBALLY_COMMUNICATED_ORDER = 7
    ENUM_TRADE_ALONG_REQUIRED = 9
    ENUM_INVALID_INVESTOR_ID = 10
    ENUM_DUPLICATE_ORDER = 6
    ENUM_UNSUPPORTED_ORDER_CHARACTERISTIC = 11
    ENUM_SURVEILLENCE_OPTION = 12
    ENUM_BROKER_CREDIT = 0
    ENUM_STALE_ORDER = 8

class IOIQualifier (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '104'
    ENUM_AT_THE_OPEN = 'O'
    ENUM_CROSSING_OPPORTUNITY = 'X'
    ENUM_INDICATION = 'W'
    ENUM_VERSUS = 'V'
    ENUM_THROUGH_THE_DAY = 'T'
    ENUM_PORTFOLIO_SHOWN = 'S'
    ENUM_READY_TO_TRADE = 'R'
    ENUM_ALL_OR_NONE = 'A'
    ENUM_TAKING_A_POSITION = 'P'
    ENUM_MORE_BEHIND = 'M'
    ENUM_LIMIT = 'L'
    ENUM_IN_TOUCH_WITH = 'I'
    ENUM_VWAP = 'D'
    ENUM_AT_THE_CLOSE = 'C'
    ENUM_MARKET_ON_CLOSE = 'B'
    ENUM_AT_THE_MARKET = 'Q'
    ENUM_AT_THE_MIDPOINT = 'Y'
    ENUM_PRE_OPEN = 'Z'

class Issuer (field_types.String_Type) :
    _tag = '106'

class SecurityDesc (field_types.String_Type) :
    _tag = '107'

class HeartBtInt (field_types.int_Type) :
    _tag = '108'

class MinQty (field_types.Qty_Type) :
    _tag = '110'

class MaxFloor (field_types.Qty_Type) :
    _tag = '111'

class TestReqID (field_types.String_Type) :
    _tag = '112'

class ReportToExch (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '113'
    ENUM_RECEIVER_REPORTS = 'Y'
    ENUM_SENDER_REPORTS = 'N'

class LocateReqd (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '114'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

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
    ENUM_EXECUTE_FOREX_AFTER_SECURITY_TRADE = 'Y'
    ENUM_DO_NOT_EXECUTE_FOREX_AFTER_SECURITY_TRADE = 'N'

class OrigSendingTime (field_types.UTCTimestamp_Type) :
    _tag = '122'

class GapFillFlag (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '123'
    ENUM_GAP_FILL_MESSAGE = 'Y'
    ENUM_SEQUENCE_RESET = 'N'

class NoExecs (field_types.NumInGroup_Type) :
    _tag = '124'

class ExpireTime (field_types.UTCTimestamp_Type) :
    _tag = '126'

class DKReason (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '127'
    ENUM_WRONG_SIDE = 'B'
    ENUM_QUANTITY_EXCEEDS_ORDER = 'C'
    ENUM_NO_MATCHING_ORDER = 'D'
    ENUM_PRICE_EXCEEDS_LIMIT = 'E'
    ENUM_OTHER = 'Z'
    ENUM_UNKNOWN_SYMBOL = 'A'

class DeliverToCompID (field_types.String_Type) :
    _tag = '128'

class DeliverToSubID (field_types.String_Type) :
    _tag = '129'

class IOINaturalFlag (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '130'
    ENUM_NATURAL = 'Y'
    ENUM_NOT_NATURAL = 'N'

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

class NoMiscFees (field_types.NumInGroup_Type) :
    _tag = '136'

class MiscFeeAmt (field_types.Amt_Type) :
    _tag = '137'

class MiscFeeCurr (field_types.Currency_Type) :
    _tag = '138'

class MiscFeeType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '139'
    ENUM_LOCAL_COMMISSION = '3'
    ENUM_EXCHANGE_FEES = '4'
    ENUM_STAMP = '5'
    ENUM_LEVY = '6'
    ENUM_OTHER = '7'
    ENUM_MARKUP = '8'
    ENUM_CONSUMPTION_TAX = '9'
    ENUM_REGULATORY = '1'
    ENUM_TAX = '2'

class PrevClosePx (field_types.Price_Type) :
    _tag = '140'

class ResetSeqNumFlag (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '141'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class SenderLocationID (field_types.String_Type) :
    _tag = '142'

class TargetLocationID (field_types.String_Type) :
    _tag = '143'

class OnBehalfOfLocationID (field_types.String_Type) :
    _tag = '144'

class DeliverToLocationID (field_types.String_Type) :
    _tag = '145'

class NoRelatedSym (field_types.NumInGroup_Type) :
    _tag = '146'

class Subject (field_types.String_Type) :
    _tag = '147'

class Headline (field_types.String_Type) :
    _tag = '148'

class URLLink (field_types.String_Type) :
    _tag = '149'

class ExecType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '150'
    ENUM_PENDING_CANCEL = '6'
    ENUM_NEW = '0'
    ENUM_PARTIAL_FILL = '1'
    ENUM_FILL = '2'
    ENUM_CANCELED = '4'
    ENUM_REPLACED = '5'
    ENUM_REJECTED = '8'
    ENUM_SUSPENDED = '9'
    ENUM_PENDING_NEW = 'A'
    ENUM_CALCULATED = 'B'
    ENUM_EXPIRED = 'C'
    ENUM_RESTATED = 'D'
    ENUM_PENDING_REPLACE = 'E'
    ENUM_TRADE = 'F'
    ENUM_TRADE_CORRECT = 'G'
    ENUM_TRADE_CANCEL = 'H'
    ENUM_ORDER_STATUS = 'I'
    ENUM_DONE_FOR_DAY = '3'
    ENUM_STOPPED = '7'

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

class SettlCurrFxRateCalc (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '156'
    ENUM_DIVIDE = 'D'
    ENUM_MULTIPLY = 'M'

class NumDaysInterest (field_types.int_Type) :
    _tag = '157'

class AccruedInterestRate (field_types.Percentage_Type) :
    _tag = '158'

class AccruedInterestAmt (field_types.Amt_Type) :
    _tag = '159'

class SettlInstMode (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '160'
    ENUM_DEFAULT = '0'
    ENUM_SPECIFIC_ORDER_FOR_A_SINGLE_ACCOUNT = '4'
    ENUM_SPECIFIC_ALLOCATION_ACCOUNT_STANDING = '3'
    ENUM_STANDING_INSTRUCTIONS_PROVIDED = '1'
    ENUM_SPECIFIC_ALLOCATION_ACCOUNT_OVERRIDING = '2'

class AllocText (field_types.String_Type) :
    _tag = '161'

class SettlInstID (field_types.String_Type) :
    _tag = '162'

class SettlInstTransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '163'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'
    ENUM_CANCEL = 'C'

class EmailThreadID (field_types.String_Type) :
    _tag = '164'

class SettlInstSource (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '165'
    ENUM_INSTITUTION = '2'
    ENUM_INVESTOR = '3'
    ENUM_BROKER_CREDIT = '1'

class SecurityType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '167'
    ENUM_COMMERCIAL_PAPER = 'CP'
    ENUM_VARIABLE_RATE_DEMAND_NOTE = 'VRDN'
    ENUM_PLAZOS_FIJOS = 'PZFJ'
    ENUM_PROMISSORY_NOTE = 'PN'
    ENUM_OVERNIGHT = 'ONITE'
    ENUM_MEDIUM_TERM_NOTES = 'MTN'
    ENUM_TAX_EXEMPT_COMMERCIAL_PAPER = 'TECP'
    ENUM_AMENDED = 'AMENDED'
    ENUM_BRIDGE_LOAN = 'BRIDGE'
    ENUM_LETTER_OF_CREDIT = 'LOFC'
    ENUM_SWING_LINE_FACILITY = 'SWING'
    ENUM_DEBTOR_IN_POSSESSION = 'DINP'
    ENUM_DEFAULTED = 'DEFLTED'
    ENUM_WITHDRAWN = 'WITHDRN'
    ENUM_LIQUIDITY_NOTE = 'LQN'
    ENUM_MATURED = 'MATURED'
    ENUM_DEPOSIT_NOTES = 'DN'
    ENUM_RETIRED = 'RETIRED'
    ENUM_BANKERS_ACCEPTANCE = 'BA'
    ENUM_BANK_NOTES = 'BN'
    ENUM_BILL_OF_EXCHANGES = 'BOX'
    ENUM_CERTIFICATE_OF_DEPOSIT = 'CD'
    ENUM_CALL_LOANS = 'CL'
    ENUM_REPLACED = 'REPLACD'
    ENUM_MANDATORY_TENDER = 'MT'
    ENUM_REVOLVER = 'RVLVTRM'
    ENUM_MORTGAGE_PRIVATE_PLACEMENT = 'MPP'
    ENUM_SHORT_TERM_LOAN_NOTE = 'STN'
    ENUM_MISCELLANEOUS_PASS_THROUGH = 'MPT'
    ENUM_TO_BE_ANNOUNCED = 'TBA'
    ENUM_OTHER_ANTICIPATION_NOTES = 'AN'
    ENUM_MORTGAGE_INTEREST_ONLY = 'MIO'
    ENUM_CERTIFICATE_OF_PARTICIPATION = 'COFP'
    ENUM_MORTGAGE_BACKED_SECURITIES = 'MBS'
    ENUM_REVENUE_BONDS = 'REV'
    ENUM_SPECIAL_ASSESSMENT = 'SPCLA'
    ENUM_SPECIAL_OBLIGATION = 'SPCLO'
    ENUM_SPECIAL_TAX = 'SPCLT'
    ENUM_TAX_ANTICIPATION_NOTE = 'TAN'
    ENUM_TAX_ALLOCATION = 'TAXA'
    ENUM_CERTIFICATE_OF_OBLIGATION = 'COFO'
    ENUM_TIME_DEPOSIT = 'TD'
    ENUM_GENERAL_OBLIGATION_BONDS = 'GO'
    ENUM_WILDCARD = '?'
    ENUM_WARRANT = 'WAR'
    ENUM_MUTUAL_FUND = 'MF'
    ENUM_MULTILEG_INSTRUMENT = 'MLEG'
    ENUM_TAX_REVENUE_ANTICIPATION_NOTE = 'TRAN'
    ENUM_MORTGAGE_PRINCIPAL_ONLY = 'MPO'
    ENUM_REPURCHASE_AGREEMENT = 'RP'
    ENUM_NO_SECURITY_TYPE = 'NONE'
    ENUM_EXTENDED_COMM_NOTE = 'XCN'
    ENUM_AGENCY_POOLS = 'POOL'
    ENUM_ASSET_BACKED_SECURITIES = 'ABS'
    ENUM_CORP = 'CMBS'
    ENUM_COLLATERALIZED_MORTGAGE_OBLIGATION = 'CMO'
    ENUM_IOETTE_MORTGAGE = 'IET'
    ENUM_REVERSE_REPURCHASE_AGREEMENT = 'RVRP'
    ENUM_FOREIGN_EXCHANGE_CONTRACT = 'FOR'
    ENUM_REVENUE_ANTICIPATION_NOTE = 'RAN'
    ENUM_REVOLVER_LOAN = 'RVLV'
    ENUM_FEDERAL_AGENCY_COUPON = 'FAC'
    ENUM_FEDERAL_AGENCY_DISCOUNT_NOTE = 'FADN'
    ENUM_PRIVATE_EXPORT_FUNDING = 'PEF'
    ENUM_CORPORATE_BOND = 'CORP'
    ENUM_CORPORATE_PRIVATE_PLACEMENT = 'CPP'
    ENUM_CONVERTIBLE_BOND = 'CB'
    ENUM_DUAL_CURRENCY = 'DUAL'
    ENUM_INDEXED_LINKED = 'XLINKD'
    ENUM_YANKEE_CORPORATE_BOND = 'YANK'
    ENUM_COMMON_STOCK = 'CS'
    ENUM_PREFERRED_STOCK = 'PS'
    ENUM_BRADY_BOND = 'BRADY'
    ENUM_US_TREASURY_BOND = 'TBOND'
    ENUM_INTEREST_STRIP_FROM_ANY_BOND_OR_NOTE = 'TINT'
    ENUM_TREASURY_INFLATION_PROTECTED_SECURITIES = 'TIPS'
    ENUM_PRINCIPAL_STRIP_OF_A_CALLABLE_BOND_OR_NOTE = 'TCAL'
    ENUM_PRINCIPAL_STRIP_FROM_A_NON_CALLABLE_BOND_OR_NOTE = 'TPRN'
    ENUM_US_TREASURY_NOTE_OLD = 'UST'
    ENUM_US_TREASURY_BILL_OLD = 'USTB'
    ENUM_TERM_LOAN = 'TERM'
    ENUM_STRUCTURED_NOTES = 'STRUCT'

class EffectiveTime (field_types.UTCTimestamp_Type) :
    _tag = '168'

class StandInstDbType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '169'
    ENUM_OTHER = 0
    ENUM_DTCSID = 1
    ENUM_A_GLOBAL_CUSTODIAN = 3
    ENUM_THOMSON_ALERT = 2

class StandInstDbName (field_types.String_Type) :
    _tag = '170'

class StandInstDbID (field_types.String_Type) :
    _tag = '171'

class SettlDeliveryType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '172'
    ENUM_FREE = 1
    ENUM_VERSUS = 0

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

class NoIOIQualifiers (field_types.NumInGroup_Type) :
    _tag = '199'

class MaturityMonthYear (field_types.MonthYear_Type) :
    _tag = '200'

class StrikePrice (field_types.Price_Type) :
    _tag = '202'

class CoveredOrUncovered (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '203'
    ENUM_UNCOVERED = 1
    ENUM_COVERED = 0

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
    ENUM_FORWARD_AND_MATCH = 3
    ENUM_FORWARD = 2
    ENUM_MATCH = 1

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

class NoRoutingIDs (field_types.NumInGroup_Type) :
    _tag = '215'

class RoutingType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '216'
    ENUM_TARGET_FIRM = 1
    ENUM_TARGET_LIST = 2
    ENUM_BLOCK_FIRM = 3
    ENUM_BLOCK_LIST = 4

class RoutingID (field_types.String_Type) :
    _tag = '217'

class Spread (field_types.PriceOffset_Type) :
    _tag = '218'

class Benchmark (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '219'
    ENUM_OLD10 = '5'
    ENUM_CURVE = '1'
    ENUM_FIVE_YR = '2'
    ENUM_TEN_YR = '4'
    ENUM_THIRTY_YR = '6'
    ENUM_OLD30 = '7'
    ENUM_THREE_MOLIBOR = '8'
    ENUM_SIX_MOLIBOR = '9'
    ENUM_OLD5 = '3'

class BenchmarkCurveCurrency (field_types.Currency_Type) :
    _tag = '220'

class BenchmarkCurveName (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '221'
    ENUM_SWAP = 'SWAP'
    ENUM_LIBID = 'LIBID'
    ENUM_OTHER = 'OTHER'
    ENUM_TREASURY = 'Treasury'
    ENUM_EURIBOR = 'Euribor'
    ENUM_PFANDBRIEFE = 'Pfandbriefe'
    ENUM_FUTURE_SWAP = 'FutureSWAP'
    ENUM_MUNI_AAA = 'MuniAAA'
    ENUM_LIBOR = 'LIBOR'

class BenchmarkCurvePoint (field_types.String_Type) :
    _tag = '222'

class CouponRate (field_types.Percentage_Type) :
    _tag = '223'

class CouponPaymentDate (field_types.UTCDate_Type) :
    _tag = '224'

class IssueDate (field_types.UTCDate_Type) :
    _tag = '225'

class RepurchaseTerm (field_types.int_Type) :
    _tag = '226'

class RepurchaseRate (field_types.Percentage_Type) :
    _tag = '227'

class Factor (field_types.float_Type) :
    _tag = '228'

class TradeOriginationDate (field_types.UTCDate_Type) :
    _tag = '229'

class ExDate (field_types.UTCDate_Type) :
    _tag = '230'

class ContractMultiplier (field_types.float_Type) :
    _tag = '231'

class NoStipulations (field_types.NumInGroup_Type) :
    _tag = '232'

class StipulationType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '233'
    ENUM_ABSOLUTE_PREPAYMENT_SPEED = 'ABS'
    ENUM_WEIGHTED_AVERAGE_LOAN_AGE = 'WALA'
    ENUM_WEIGHTED_AVERAGE_MATURITY = 'WAM'
    ENUM_CONSTANT_PREPAYMENT_RATE = 'CPR'
    ENUM_FINAL_CPR_OF_HOME_EQUITY_PREPAYMENT_CURVE = 'HEP'
    ENUM_WEIGHTED_AVERAGE_LIFE_COUPON = 'WAL'
    ENUM_PERCENT_OF_MANUFACTURED_HOUSING_PREPAYMENT_CURVE = 'MHP'
    ENUM_SINGLE_MONTHLY_MORTALITY = 'SMM'
    ENUM_MONTHLY_PREPAYMENT_RATE = 'MPR'
    ENUM_PERCENT_OF_BMA_PREPAYMENT_CURVE = 'PSA'
    ENUM_PERCENT_OF_PROSPECTUS_PREPAYMENT_CURVE = 'PPC'
    ENUM_CONSTANT_PREPAYMENT_PENALTY = 'CPP'
    ENUM_LOT_VARIANCE = 'LOTVAR'
    ENUM_CONSTANT_PREPAYMENT_YIELD = 'CPY'
    ENUM_WEIGHTED_AVERAGE_COUPON = 'WAC'
    ENUM_ISSUE_DATE = 'ISSUE'
    ENUM_MATURITY_YEAR_AND_MONTH = 'MAT'
    ENUM_NUMBER_OF_PIECES = 'PIECES'
    ENUM_POOLS_MAXIMUM = 'PMAX'
    ENUM_POOLS_PER_MILLION = 'PPM'
    ENUM_POOLS_PER_LOT = 'PPL'
    ENUM_POOLS_PER_TRADE = 'PPT'
    ENUM_PRODUCTION_YEAR = 'PROD'
    ENUM_TRADE_VARIANCE = 'TRDVAR'
    ENUM_GEOGRAPHICS = 'GEOG'

class StipulationValue (field_types.String_Type) :
    _tag = '234'

class YieldType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '235'
    ENUM_TRUE_YIELD = 'TRUE'
    ENUM_PREVIOUS_CLOSE_YIELD = 'PREVCLOSE'
    ENUM_YIELD_TO_LONGEST_AVERAGE = 'LONGEST'
    ENUM_YIELD_TO_LONGEST_AVERAGE_LIFE = 'LONGAVGLIFE'
    ENUM_YIELD_TO_MATURITY = 'MATURITY'
    ENUM_MARK_TO_MARKET_YIELD = 'MARK'
    ENUM_OPEN_AVERAGE_YIELD = 'OPENAVG'
    ENUM_YIELD_TO_NEXT_PUT = 'PUT'
    ENUM_PROCEEDS_YIELD = 'PROCEEDS'
    ENUM_SEMI_ANNUAL_YIELD = 'SEMIANNUAL'
    ENUM_YIELD_TO_SHORTEST_AVERAGE_LIFE = 'SHORTAVGLIFE'
    ENUM_YIELD_TO_SHORTEST_AVERAGE = 'SHORTEST'
    ENUM_SIMPLE_YIELD = 'SIMPLE'
    ENUM_YIELD_TO_TENDER_DATE = 'TENDER'
    ENUM_YIELD_VALUE_OF32NDS = 'VALUE1/32'
    ENUM_YIELD_TO_WORST = 'WORST'
    ENUM_TAX_EQUIVALENT_YIELD = 'TAXEQUIV'
    ENUM_ANNUAL_YIELD = 'ANNUAL'
    ENUM_CLOSING_YIELD_MOST_RECENT_YEAR = 'LASTYEAR'
    ENUM_YIELD_TO_NEXT_REFUND = 'NEXTREFUND'
    ENUM_AFTER_TAX_YIELD = 'AFTERTAX'
    ENUM_YIELD_AT_ISSUE = 'ATISSUE'
    ENUM_YIELD_TO_AVERAGE_LIFE = 'AVGLIFE'
    ENUM_YIELD_TO_AVERAGE_MATURITY = 'AVGMATURITY'
    ENUM_BOOK_YIELD = 'BOOK'
    ENUM_YIELD_TO_NEXT_CALL = 'CALL'
    ENUM_YIELD_CHANGE_SINCE_CLOSE = 'CHANGE'
    ENUM_COMPOUND_YIELD = 'COMPOUND'
    ENUM_CURRENT_YIELD = 'CURRENT'
    ENUM_TRUE_GROSS_YIELD = 'GROSS'
    ENUM_GVNT_EQUIVALENT_YIELD = 'GOVTEQUIV'
    ENUM_YIELD_WITH_INFLATION_ASSUMPTION = 'INFLATION'
    ENUM_INVERSE_FLOATER_BOND_YIELD = 'INVERSEFLOATER'
    ENUM_CLOSING_YIELD_MOST_RECENT_QUARTER = 'LASTQUARTER'
    ENUM_MOST_RECENT_CLOSING_YIELD = 'LASTCLOSE'
    ENUM_CLOSING_YIELD_MOST_RECENT_MONTH = 'LASTMONTH'
    ENUM_CLOSING_YIELD = 'CLOSE'

class Yield (field_types.Percentage_Type) :
    _tag = '236'

class TotalTakedown (field_types.Amt_Type) :
    _tag = '237'

class Concession (field_types.Amt_Type) :
    _tag = '238'

class RepoCollateralSecurityType (field_types.String_Type) :
    _tag = '239'

class RedemptionDate (field_types.UTCDate_Type) :
    _tag = '240'

class UnderlyingCouponPaymentDate (field_types.UTCDate_Type) :
    _tag = '241'

class UnderlyingIssueDate (field_types.UTCDate_Type) :
    _tag = '242'

class UnderlyingRepoCollateralSecurityType (field_types.String_Type) :
    _tag = '243'

class UnderlyingRepurchaseTerm (field_types.int_Type) :
    _tag = '244'

class UnderlyingRepurchaseRate (field_types.Percentage_Type) :
    _tag = '245'

class UnderlyingFactor (field_types.float_Type) :
    _tag = '246'

class UnderlyingRedemptionDate (field_types.UTCDate_Type) :
    _tag = '247'

class LegCouponPaymentDate (field_types.UTCDate_Type) :
    _tag = '248'

class LegIssueDate (field_types.UTCDate_Type) :
    _tag = '249'

class LegRepoCollateralSecurityType (field_types.String_Type) :
    _tag = '250'

class LegRepurchaseTerm (field_types.int_Type) :
    _tag = '251'

class LegRepurchaseRate (field_types.Percentage_Type) :
    _tag = '252'

class LegFactor (field_types.float_Type) :
    _tag = '253'

class LegRedemptionDate (field_types.UTCDate_Type) :
    _tag = '254'

class CreditRating (field_types.String_Type) :
    _tag = '255'

class UnderlyingCreditRating (field_types.String_Type) :
    _tag = '256'

class LegCreditRating (field_types.String_Type) :
    _tag = '257'

class TradedFlatSwitch (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '258'
    ENUM_NOT_TRADED_FLAT = 'N'
    ENUM_TRADED_FLAT = 'Y'

class BasisFeatureDate (field_types.UTCDate_Type) :
    _tag = '259'

class BasisFeaturePrice (field_types.Price_Type) :
    _tag = '260'

class MDReqID (field_types.String_Type) :
    _tag = '262'

class SubscriptionRequestType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '263'
    ENUM_SNAPSHOT_AND_UPDATES = '1'
    ENUM_DISABLE_PREVIOUS_SNAPSHOT = '2'
    ENUM_SNAPSHOT = '0'

class MarketDepth (field_types.int_Type) :
    _tag = '264'

class MDUpdateType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '265'
    ENUM_FULL_REFRESH = 0
    ENUM_INCREMENTAL_REFRESH = 1

class AggregatedBook (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '266'
    ENUM_BOOK_ENTRIES_TO_BE_AGGREGATED = 'Y'
    ENUM_BOOK_ENTRIES_SHOULD_NOT_BE_AGGREGATED = 'N'

class NoMDEntryTypes (field_types.NumInGroup_Type) :
    _tag = '267'

class NoMDEntries (field_types.NumInGroup_Type) :
    _tag = '268'

class MDEntryType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '269'
    ENUM_TRADING_SESSION_HIGH_PRICE = '7'
    ENUM_OFFER = '1'
    ENUM_IMBALANCE = 'A'
    ENUM_TRADING_SESSION_VWAP_PRICE = '9'
    ENUM_TRADING_SESSION_LOW_PRICE = '8'
    ENUM_CLOSING_PRICE = '5'
    ENUM_OPENING_PRICE = '4'
    ENUM_BID = '0'
    ENUM_TRADE = '2'
    ENUM_INDEX_VALUE = '3'
    ENUM_SETTLEMENT_PRICE = '6'

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
    ENUM_LOCKED = 'E'
    ENUM_NON_FIRM = 'I'
    ENUM_FAST_TRADING = 'H'
    ENUM_CROSSED = 'F'
    ENUM_CONSOLIDATED_BEST = 'D'
    ENUM_EXCHANGE_BEST = 'C'
    ENUM_CLOSED = 'B'
    ENUM_OPEN = 'A'
    ENUM_DEPTH = 'G'

class TradeCondition (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '277'
    ENUM_NEXT_DAY_TRADE = 'J'
    ENUM_OPENED = 'K'
    ENUM_SELLER = 'L'
    ENUM_AVERAGE_PRICE_TRADE = 'B'
    ENUM_SOLD = 'M'
    ENUM_RULE155_TRADE = 'H'
    ENUM_STOPPED_STOCK = 'N'
    ENUM_IMBALANCE_MORE_BUYERS = 'P'
    ENUM_IMBALANCE_MORE_SELLERS = 'Q'
    ENUM_OPENING_PRICE = 'R'
    ENUM_SOLD_LAST = 'I'
    ENUM_CASH = 'A'
    ENUM_CASH_TRADE = 'C'
    ENUM_OPENING = 'E'
    ENUM_INTRADAY_TRADE_DETAIL = 'F'
    ENUM_RULE127_TRADE = 'G'
    ENUM_NEXT_DAY = 'D'

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
    ENUM_UNSUPPORTED_AGGREGATED_BOOK = '7'
    ENUM_DUPLICATE_MD_REQ_ID = '1'
    ENUM_UNSUPPORTED_MD_IMPLICIT_DELETE = 'C'
    ENUM_UNSUPPORTED_OPEN_CLOSE_SETTLE_FLAG = 'B'
    ENUM_UNSUPPORTED_SCOPE = 'A'
    ENUM_UNSUPPORTED_TRADING_SESSION_ID = '9'
    ENUM_UNSUPPORTED_MD_ENTRY_TYPE = '8'
    ENUM_UNSUPPORTED_MD_UPDATE_TYPE = '6'
    ENUM_UNSUPPORTED_MARKET_DEPTH = '5'
    ENUM_UNSUPPORTED_SUBSCRIPTION_REQUEST_TYPE = '4'
    ENUM_INSUFFICIENT_BANDWIDTH = '2'
    ENUM_UNKNOWN_SYMBOL = '0'
    ENUM_INSUFFICIENT_PERMISSIONS = '3'

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

class OpenCloseSettleFlag (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '286'
    ENUM_SESSION_OPEN = '1'
    ENUM_DELIVERY_SETTLEMENT_ENTRY = '2'
    ENUM_EXPECTED_ENTRY = '3'
    ENUM_ENTRY_FROM_PREVIOUS_BUSINESS_DAY = '4'
    ENUM_DAILY_OPEN = '0'

class SellerDays (field_types.int_Type) :
    _tag = '287'

class MDEntryBuyer (field_types.String_Type) :
    _tag = '288'

class MDEntrySeller (field_types.String_Type) :
    _tag = '289'

class MDEntryPositionNo (field_types.int_Type) :
    _tag = '290'

class FinancialStatus (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '291'
    ENUM_BANKRUPT = '1'
    ENUM_PENDING_DELISTING = '2'

class CorporateAction (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '292'
    ENUM_EX_DISTRIBUTION = 'B'
    ENUM_EX_INTEREST = 'E'
    ENUM_EX_RIGHTS = 'C'
    ENUM_EX_DIVIDEND = 'A'
    ENUM_NEW = 'D'

class DefBidSize (field_types.Qty_Type) :
    _tag = '293'

class DefOfferSize (field_types.Qty_Type) :
    _tag = '294'

class NoQuoteEntries (field_types.NumInGroup_Type) :
    _tag = '295'

class NoQuoteSets (field_types.NumInGroup_Type) :
    _tag = '296'

class QuoteStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '297'
    ENUM_REMOVED_FROM_MARKET = 6
    ENUM_CANCEL_FOR_SYMBOL = 1
    ENUM_PENDING = 10
    ENUM_QUOTE_NOT_FOUND = 9
    ENUM_QUERY = 8
    ENUM_EXPIRED = 7
    ENUM_REJECTED = 5
    ENUM_CANCELED_ALL = 4
    ENUM_CANCELED_FOR_UNDERLYING = 3
    ENUM_CANCELED_FOR_SECURITY_TYPE = 2
    ENUM_ACCEPTED = 0

class QuoteCancelType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '298'
    ENUM_CANCEL_ALL_QUOTES = 4
    ENUM_CANCEL_FOR_SECURITY_TYPE = 2
    ENUM_CANCEL_FOR_ONE_OR_MORE_SECURITIES = 1
    ENUM_CANCEL_FOR_UNDERLYING_SECURITY = 3

class QuoteEntryID (field_types.String_Type) :
    _tag = '299'

class QuoteRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '300'
    ENUM_NOT_AUTHORIZED_TO_QUOTE_SECURITY = 9
    ENUM_UNKNOWN_SYMBOL = 1
    ENUM_EXCHANGE = 2
    ENUM_QUOTE_REQUEST_EXCEEDS_LIMIT = 3
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_UNKNOWN_QUOTE = 5
    ENUM_DUPLICATE_QUOTE = 6
    ENUM_INVALID_BID = 7
    ENUM_INVALID_PRICE = 8

class QuoteResponseLevel (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '301'
    ENUM_ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES = 1
    ENUM_NO_ACKNOWLEDGEMENT = 0
    ENUM_ACKNOWLEDGE_EACH_QUOTE_MESSAGE = 2

class QuoteSetID (field_types.String_Type) :
    _tag = '302'

class QuoteRequestType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '303'
    ENUM_AUTOMATIC = 2
    ENUM_MANUAL = 1

class TotQuoteEntries (field_types.int_Type) :
    _tag = '304'

class UnderlyingSecurityIDSource (field_types.String_Type) :
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

class UnderlyingPutOrCall (field_types.int_Type) :
    _tag = '315'

class UnderlyingStrikePrice (field_types.Price_Type) :
    _tag = '316'

class UnderlyingOptAttribute (field_types.char_Type) :
    _tag = '317'

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
    ENUM_REJECT_SECURITY_PROPOSAL = 5
    ENUM_ACCEPT_AS_IS = 1
    ENUM_CANNOT_MATCH_SELECTION_CRITERIA = 6
    ENUM_ACCEPT_WITH_REVISIONS = 2
    ENUM_LIST_OF_SECURITIES_RETURNED_PER_REQUEST = 4
    ENUM_LIST_OF_SECURITY_TYPES_RETURNED_PER_REQUEST = 3

class SecurityStatusReqID (field_types.String_Type) :
    _tag = '324'

class UnsolicitedIndicator (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '325'
    ENUM_MESSAGE_IS_BEING_SENT_UNSOLICITED = 'Y'
    ENUM_MESSAGE_IS_BEING_SENT_AS_A_RESULT_OF_A_PRIOR_REQUEST = 'N'

class SecurityTradingStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '326'
    ENUM_UNKNOWN_OR_INVALID = 20
    ENUM_NO_MARKET_ON_CLOSE_IMBALANCE = 13
    ENUM_ITS_PRE_OPENING = 14
    ENUM_NEW_PRICE_INDICATION = 15
    ENUM_TRADE_DISSEMINATION_TIME = 16
    ENUM_READY_TO_TRADE = 17
    ENUM_NOT_TRADED_ON_THIS_MARKET = 19
    ENUM_OPENING_ROTATION = 22
    ENUM_PRE_OPEN = 21
    ENUM_NO_MARKET_IMBALANCE = 12
    ENUM_NOT_AVAILABLE_FOR_TRADING = 18
    ENUM_MARKET_ON_CLOSE_IMBALANCE_SELL = 10
    ENUM_MARKET_ON_CLOSE_IMBALANCE_BUY = 9
    ENUM_MARKET_IMBALANCE_SELL = 8
    ENUM_MARKET_IMBALANCE_BUY = 7
    ENUM_TRADING_RANGE_INDICATION = 6
    ENUM_PRICE_INDICATION = 5
    ENUM_NO_OPEN = 4
    ENUM_RESUME = 3
    ENUM_OPENING_DELAY = 1
    ENUM_TRADING_HALT = 2
    ENUM_FAST_MARKET = 23

class HaltReason (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '327'
    ENUM_EQUIPMENT_CHANGEOVER = 'X'
    ENUM_ADDITIONAL_INFORMATION = 'M'
    ENUM_ORDER_INFLUX = 'E'
    ENUM_NEWS_PENDING = 'P'
    ENUM_ORDER_IMBALANCE = 'I'
    ENUM_NEWS_DISSEMINATION = 'D'

class InViewOfCommon (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '328'
    ENUM_HALT_WAS_DUE_TO_COMMON_STOCK_BEING_HALTED = 'Y'
    ENUM_HALT_WAS_NOT_RELATED_TO_A_HALT_OF_THE_COMMON_STOCK = 'N'

class DueToRelated (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '329'
    ENUM_RELATED_TO_SECURITY_HALT = 'Y'
    ENUM_NOT_RELATED_TO_SECURITY_HALT = 'N'

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
    ENUM_TWO_PARTY = 3
    ENUM_ELECTRONIC = 1
    ENUM_OPEN_OUTCRY = 2

class TradSesMode (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '339'
    ENUM_PRODUCTION = 3
    ENUM_TESTING = 1
    ENUM_SIMULATED = 2

class TradSesStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '340'
    ENUM_PRE_CLOSE = 5
    ENUM_REQUEST_REJECTED = 6
    ENUM_PRE_OPEN = 4
    ENUM_CLOSED = 3
    ENUM_OPEN = 2
    ENUM_HALTED = 1
    ENUM_UNKNOWN = 0

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
    ENUM_UTF8 = 'UTF-8'
    ENUM_ISO2022_JP = 'ISO-2022-JP'
    ENUM_EUCJP = 'EUC-JP'
    ENUM_SHIFT_JIS = 'Shift_JIS'

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

class QuoteEntryRejectReason (field_types.int_Type) :
    _tag = '368'

class LastMsgSeqNumProcessed (field_types.SeqNum_Type) :
    _tag = '369'

class OnBehalfOfSendingTime (field_types.UTCTimestamp_Type) :
    _tag = '370'

class RefTagID (field_types.int_Type) :
    _tag = '371'

class RefMsgType (field_types.String_Type) :
    _tag = '372'

class SessionRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '373'
    ENUM_XML_VALIDATION_ERROR = 12
    ENUM_NON = 17
    ENUM_INCORRECT_NUM_IN_GROUP_COUNT_FOR_REPEATING_GROUP = 16
    ENUM_REPEATING_GROUP_FIELDS_OUT_OF_ORDER = 15
    ENUM_TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER = 14
    ENUM_INVALID_MSG_TYPE = 11
    ENUM_INVALID_TAG_NUMBER = 0
    ENUM_COMP_ID_PROBLEM = 9
    ENUM_SIGNATURE_PROBLEM = 8
    ENUM_DECRYPTION_PROBLEM = 7
    ENUM_INCORRECT_DATA_FORMAT_FOR_VALUE = 6
    ENUM_VALUE_IS_INCORRECT = 5
    ENUM_TAG_SPECIFIED_WITHOUT_A_VALUE = 4
    ENUM_UNDEFINED_TAG = 3
    ENUM_SENDING_TIME_ACCURACY_PROBLEM = 10
    ENUM_TAG_APPEARS_MORE_THAN_ONCE = 13
    ENUM_TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE = 2
    ENUM_REQUIRED_TAG_MISSING = 1

class BidRequestTransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '374'
    ENUM_NEW = 'N'
    ENUM_CANCEL = 'C'

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
    ENUM_CANCEL_ON_SYSTEM_FAILURE = 7
    ENUM_GT_CORPORATE_ACTION = 0
    ENUM_MARKET = 8
    ENUM_CANCEL_ON_TRADING_HALT = 6
    ENUM_PARTIAL_DECLINE_OF_ORDER_QTY = 5
    ENUM_BROKER_OPTION = 4
    ENUM_REPRICING_OF_ORDER = 3
    ENUM_GT_RENEWAL = 1
    ENUM_VERBAL_CHANGE = 2

class BusinessRejectRefID (field_types.String_Type) :
    _tag = '379'

class BusinessRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '380'
    ENUM_UNSUPPORTED_MESSAGE_TYPE = 3
    ENUM_DELIVER_TO_FIRM_NOT_AVAILABLE_AT_THIS_TIME = 7
    ENUM_APPLICATION_NOT_AVAILABLE = 4
    ENUM_NOT_AUTHORIZED = 6
    ENUM_OTHER = 0
    ENUM_CONDITIONALLY_REQUIRED_FIELD_MISSING = 5
    ENUM_UNKNOWN_ID = 1
    ENUM_UNKNOWN_SECURITY = 2

class GrossTradeAmt (field_types.Amt_Type) :
    _tag = '381'

class NoContraBrokers (field_types.NumInGroup_Type) :
    _tag = '382'

class MaxMessageSize (field_types.Length_Type) :
    _tag = '383'

class NoMsgTypes (field_types.NumInGroup_Type) :
    _tag = '384'

class MsgDirection (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '385'
    ENUM_SEND = 'S'
    ENUM_RECEIVE = 'R'

class NoTradingSessions (field_types.NumInGroup_Type) :
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

class BidType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '394'
    ENUM_NON_DISCLOSED = 1
    ENUM_DISCLOSED = 2
    ENUM_NO_BIDDING_PROCESS = 3

class NumTickets (field_types.int_Type) :
    _tag = '395'

class SideValue1 (field_types.Amt_Type) :
    _tag = '396'

class SideValue2 (field_types.Amt_Type) :
    _tag = '397'

class NoBidDescriptors (field_types.NumInGroup_Type) :
    _tag = '398'

class BidDescriptorType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '399'
    ENUM_INDEX = 3
    ENUM_COUNTRY = 2
    ENUM_SECTOR = 1

class BidDescriptor (field_types.String_Type) :
    _tag = '400'

class SideValueInd (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '401'
    ENUM_SIDE_VALUE1 = 1
    ENUM_SIDE_VALUE2 = 2

class LiquidityPctLow (field_types.Percentage_Type) :
    _tag = '402'

class LiquidityPctHigh (field_types.Percentage_Type) :
    _tag = '403'

class LiquidityValue (field_types.Amt_Type) :
    _tag = '404'

class EFPTrackingError (field_types.Percentage_Type) :
    _tag = '405'

class FairValue (field_types.Amt_Type) :
    _tag = '406'

class OutsideIndexPct (field_types.Percentage_Type) :
    _tag = '407'

class ValueOfFutures (field_types.Amt_Type) :
    _tag = '408'

class LiquidityIndType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '409'
    ENUM_NORMAL_MARKET_SIZE = 3
    ENUM_OTHER = 4
    ENUM_TWENTY_DAY_MOVING_AVERAGE = 2
    ENUM_FIVE_DAY_MOVING_AVERAGE = 1

class WtAverageLiquidity (field_types.Percentage_Type) :
    _tag = '410'

class ExchangeForPhysical (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '411'
    ENUM_FALSE = 'N'
    ENUM_TRUE = 'Y'

class OutMainCntryUIndex (field_types.Amt_Type) :
    _tag = '412'

class CrossPercent (field_types.Percentage_Type) :
    _tag = '413'

class ProgRptReqs (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '414'
    ENUM_REAL_TIME_EXECUTION_REPORTS = 3
    ENUM_SELL_SIDE_SENDS = 2
    ENUM_BUY_SIDE_REQUESTS = 1

class ProgPeriodInterval (field_types.int_Type) :
    _tag = '415'

class IncTaxInd (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '416'
    ENUM_GROSS = 2
    ENUM_NET = 1

class NumBidders (field_types.int_Type) :
    _tag = '417'

class TradeType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '418'
    ENUM_VWAP_GUARANTEE = 'G'
    ENUM_AGENCY = 'A'
    ENUM_GUARANTEED_CLOSE = 'J'
    ENUM_RISK_TRADE = 'R'

class BasisPxType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '419'
    ENUM_VWAP_THROUGH_AN_AFTERNOON_SESSION = '8'
    ENUM_OPEN = 'D'
    ENUM_OTHERS = 'Z'
    ENUM_STRIKE = 'C'
    ENUM_VWAP_THROUGH_AN_AFTERNOON_SESSION_EXCEPT = 'B'
    ENUM_VWAP_THROUGH_A_DAY_EXCEPT = '9'
    ENUM_VWAP_THROUGH_A_MORNING_SESSION = '7'
    ENUM_VWAP_THROUGH_A_DAY = '6'
    ENUM_SQ = '5'
    ENUM_CURRENT_PRICE = '4'
    ENUM_CLOSING_PRICE = '3'
    ENUM_CLOSING_PRICE_AT_MORNING_SESSION = '2'
    ENUM_VWAP_THROUGH_A_MORNING_SESSION_EXCEPT = 'A'

class NoBidComponents (field_types.NumInGroup_Type) :
    _tag = '420'

class Country (field_types.Country_Type) :
    _tag = '421'

class TotNoStrikes (field_types.int_Type) :
    _tag = '422'

class PriceType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '423'
    ENUM_FIXED_AMOUNT = 3
    ENUM_PERCENTAGE = 1
    ENUM_DISCOUNT = 4
    ENUM_SPREAD = 6
    ENUM_TED_PRICE = 7
    ENUM_TED_YIELD = 8
    ENUM_PREMIUM = 5
    ENUM_PER_UNIT = 2

class DayOrderQty (field_types.Qty_Type) :
    _tag = '424'

class DayCumQty (field_types.Qty_Type) :
    _tag = '425'

class DayAvgPx (field_types.Price_Type) :
    _tag = '426'

class GTBookingInst (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '427'
    ENUM_BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION = 0
    ENUM_ACCUMULATE_UNTIL_VERBALLLY_NOTIFIED_OTHERWISE = 2
    ENUM_ACCUMULATE_UNTIL_FILLED_OR_EXPIRED = 1

class NoStrikes (field_types.NumInGroup_Type) :
    _tag = '428'

class ListStatusType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '429'
    ENUM_ALERT = 6
    ENUM_EXEC_STARTED = 4
    ENUM_TIMED = 3
    ENUM_RESPONSE = 2
    ENUM_ACK = 1
    ENUM_ALL_DONE = 5

class NetGrossInd (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '430'
    ENUM_NET = 1
    ENUM_GROSS = 2

class ListOrderStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '431'
    ENUM_CANCELLING = 4
    ENUM_EXECUTING = 3
    ENUM_REJECT = 7
    ENUM_ALL_DONE = 6
    ENUM_ALERT = 5
    ENUM_RECEIVED_FOR_EXECUTION = 2
    ENUM_IN_BIDDING_PROCESS = 1

class ExpireDate (field_types.LocalMktDate_Type) :
    _tag = '432'

class ListExecInstType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '433'
    ENUM_BUY_DRIVEN_CASH_WITHDRAW = '5'
    ENUM_BUY_DRIVEN_CASH_TOP_UP = '4'
    ENUM_WAIT_FOR_INSTRUCTION = '2'
    ENUM_IMMEDIATE = '1'
    ENUM_SELL_DRIVEN = '3'

class CxlRejResponseTo (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '434'
    ENUM_ORDER_CANCEL = '2'
    ENUM_ORDER_CANCEL_REQUEST = '1'

class UnderlyingCouponRate (field_types.Percentage_Type) :
    _tag = '435'

class UnderlyingContractMultiplier (field_types.float_Type) :
    _tag = '436'

class ContraTradeQty (field_types.Qty_Type) :
    _tag = '437'

class ContraTradeTime (field_types.UTCTimestamp_Type) :
    _tag = '438'

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

class PartyIDSource (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '447'
    ENUM_CHINESE_INVESTOR_ID = '5'
    ENUM_US_EMPLOYER_OR_TAX_ID_NUMBER = '8'
    ENUM_AUSTRALIAN_TAX_FILE_NUMBER = 'A'
    ENUM_AUSTRALIAN_BUSINESS_NUMBER = '9'
    ENUM_ISO_COUNTRY_CODE = 'E'
    ENUM_BIC = 'B'
    ENUM_US_SOCIAL_SECURITY_NUMBER = '7'
    ENUM_PROPRIETARY = 'D'
    ENUM_SETTLEMENT_ENTITY_LOCATION = 'F'
    ENUM_KOREAN_INVESTOR_ID = '1'
    ENUM_TAIWANESE_FOREIGN_INVESTOR_ID = '2'
    ENUM_TAIWANESE_TRADING_ACCT = '3'
    ENUM_MALAYSIAN_CENTRAL_DEPOSITORY = '4'
    ENUM_UK_NATIONAL_INSURANCE_OR_PENSION_NUMBER = '6'
    ENUM_GENERAL_IDENTIFIER = 'C'

class PartyID (field_types.String_Type) :
    _tag = '448'

class TotalVolumeTradedDate (field_types.UTCDate_Type) :
    _tag = '449'

class TotalVolumeTradedTime (field_types.UTCTimeOnly_Type) :
    _tag = '450'

class NetChgPrevDay (field_types.PriceOffset_Type) :
    _tag = '451'

class PartyRole (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '452'
    ENUM_CORRESPONDANT_CLEARING_FIRM = 15
    ENUM_CLIENT_ID = 3
    ENUM_UNDERLYING_CONTRA_FIRM = 20
    ENUM_SPONSORING_FIRM = 19
    ENUM_CONTRA_CLEARING_FIRM = 18
    ENUM_CONTRA_FIRM = 17
    ENUM_EXECUTING_SYSTEM = 16
    ENUM_ENTERING_FIRM = 7
    ENUM_EXECUTING_FIRM = 1
    ENUM_BROKER_OF_CREDIT = 2
    ENUM_INVESTOR_ID = 5
    ENUM_INTRODUCING_FIRM = 6
    ENUM_GIVEUP_CLEARING_FIRM = 14
    ENUM_LOCATE = 8
    ENUM_FUND_MANAGER_CLIENT_ID = 9
    ENUM_SETTLEMENT_LOCATION = 10
    ENUM_ORDER_ORIGINATION_TRADER = 11
    ENUM_EXECUTING_TRADER = 12
    ENUM_ORDER_ORIGINATION_FIRM = 13
    ENUM_CLEARING_FIRM = 4

class NoPartyIDs (field_types.NumInGroup_Type) :
    _tag = '453'

class NoSecurityAltID (field_types.NumInGroup_Type) :
    _tag = '454'

class SecurityAltID (field_types.String_Type) :
    _tag = '455'

class SecurityAltIDSource (field_types.String_Type) :
    _tag = '456'

class NoUnderlyingSecurityAltID (field_types.NumInGroup_Type) :
    _tag = '457'

class UnderlyingSecurityAltID (field_types.String_Type) :
    _tag = '458'

class UnderlyingSecurityAltIDSource (field_types.String_Type) :
    _tag = '459'

class Product (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '460'
    ENUM_LOAN = 8
    ENUM_OTHER = 12
    ENUM_MUNICIPAL = 11
    ENUM_AGENCY = 1
    ENUM_CORPORATE = 3
    ENUM_CURRENCY = 4
    ENUM_COMMODITY = 2
    ENUM_GOVERNMENT = 6
    ENUM_MORTGAGE = 10
    ENUM_INDEX = 7
    ENUM_MONEYMARKET = 9
    ENUM_EQUITY = 5

class CFICode (field_types.String_Type) :
    _tag = '461'

class UnderlyingProduct (field_types.int_Type) :
    _tag = '462'

class UnderlyingCFICode (field_types.String_Type) :
    _tag = '463'

class TestMessageIndicator (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '464'
    ENUM_TRUE = 'Y'
    ENUM_FALES = 'N'

class QuantityType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '465'
    ENUM_CONTRACTS = 6
    ENUM_OTHER = 7
    ENUM_CURRENCY = 5
    ENUM_ORIGINALFACE = 4
    ENUM_CURRENTFACE = 3
    ENUM_BONDS = 2
    ENUM_SHARES = 1
    ENUM_PAR = 8

class BookingRefID (field_types.String_Type) :
    _tag = '466'

class IndividualAllocID (field_types.String_Type) :
    _tag = '467'

class RoundingDirection (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '468'
    ENUM_ROUND_TO_NEAREST = '0'
    ENUM_ROUND_DOWN = '1'
    ENUM_ROUND_UP = '2'

class RoundingModulus (field_types.float_Type) :
    _tag = '469'

class CountryOfIssue (field_types.Country_Type) :
    _tag = '470'

class StateOrProvinceOfIssue (field_types.String_Type) :
    _tag = '471'

class LocaleOfIssue (field_types.String_Type) :
    _tag = '472'

class NoRegistDtls (field_types.NumInGroup_Type) :
    _tag = '473'

class MailingDtls (field_types.String_Type) :
    _tag = '474'

class InvestorCountryOfResidence (field_types.Country_Type) :
    _tag = '475'

class PaymentRef (field_types.String_Type) :
    _tag = '476'

class DistribPaymentMethod (field_types.int_Type) :
    _tag = '477'

class CashDistribCurr (field_types.Currency_Type) :
    _tag = '478'

class CommCurrency (field_types.Currency_Type) :
    _tag = '479'

class CancellationRights (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '480'
    ENUM_NO_WAIVER_AGREEMENT = 'M'
    ENUM_NO_EXECUTION_ONLY = 'N'
    ENUM_YES = 'Y'
    ENUM_NO_INSTITUTIONAL = 'O'

class MoneyLaunderingStatus (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '481'
    ENUM_EXEMPT_AUTHORISED = '3'
    ENUM_EXEMPT_MONEY_TYPE = '2'
    ENUM_EXEMPT_BELOW_LIMIT = '1'
    ENUM_PASSED = 'Y'
    ENUM_NOT_CHECKED = 'N'

class MailingInst (field_types.String_Type) :
    _tag = '482'

class TransBkdTime (field_types.UTCTimestamp_Type) :
    _tag = '483'

class ExecPriceType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '484'
    ENUM_SINGLE_PRICE = 'S'
    ENUM_OFFER_PRICE_MINUS_ADJUSTMENT_AMOUNT = 'Q'
    ENUM_OFFER_PRICE_MINUS_ADJUSTMENT_PERCENT = 'P'
    ENUM_OFFER_PRICE = 'O'
    ENUM_CREATION_PRICE_PLUS_ADJUSTMENT_AMOUNT = 'E'
    ENUM_CREATION_PRICE_PLUS_ADJUSTMENT_PERCENT = 'D'
    ENUM_CREATION_PRICE = 'C'
    ENUM_BID_PRICE = 'B'

class ExecPriceAdjustment (field_types.float_Type) :
    _tag = '485'

class DateOfBirth (field_types.LocalMktDate_Type) :
    _tag = '486'

class TradeReportTransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '487'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'
    ENUM_CANCEL = 'C'

class CardHolderName (field_types.String_Type) :
    _tag = '488'

class CardNumber (field_types.String_Type) :
    _tag = '489'

class CardExpDate (field_types.LocalMktDate_Type) :
    _tag = '490'

class CardIssNo (field_types.String_Type) :
    _tag = '491'

class PaymentMethod (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '492'
    ENUM_BPAY = 14
    ENUM_ACH_CREDIT = 13
    ENUM_ACH_DEBIT = 12
    ENUM_CREDIT_CARD = 11
    ENUM_DIRECT_CREDIT = 10
    ENUM_DIRECT_DEBIT = 9
    ENUM_DEBIT_CARD = 8
    ENUM_FED_WIRE = 7
    ENUM_HIGH_VALUE_CLEARING_SYSTEM = 15
    ENUM_EUROCLEAR = 3
    ENUM_TELEGRAPHIC_TRANSFER = 6
    ENUM_CLEARSTREAM = 4
    ENUM_CREST = 1
    ENUM_NSCC = 2
    ENUM_CHEQUE = 5

class RegistAcctType (field_types.String_Type) :
    _tag = '493'

class Designation (field_types.String_Type) :
    _tag = '494'

class TaxAdvantageType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '495'
    ENUM_PROFIT_SHARING_PLAN = 19
    ENUM_EMPLOYER_PRIOR_YEAR = 11
    ENUM_EMPLOYER_CURRENT_YEAR = 12
    ENUM_NON_FUND_PROTOTYPE_IRA = 13
    ENUM_NON_FUND_QUALIFIED_PLAN = 14
    ENUM_DEFINED_CONTRIBUTION_PLAN = 15
    ENUM_EMPLOYEE_CURRENT_YEAR = 10
    ENUM_IRA_ROLLOVER = 17
    ENUM_MINI_INSURANCE_ISA = 5
    ENUM_IRA = 16
    ENUM_EMPLOYEE_PRIOR_YEAR = 9
    ENUM_ASSET_TRANSFER = 8
    ENUM_SELF_DIRECTED_IRA = 21
    ENUM_CURRENT_YEAR_PAYMENT = 6
    ENUM_US401_K = 20
    ENUM_MINI_STOCKS_AND_SHARES_ISA = 4
    ENUM_MINI_CASH_ISA = 3
    ENUM_TESSA = 2
    ENUM_MAXI_ISA = 1
    ENUM_NONE = 0
    ENUM_PRIOR_YEAR_PAYMENT = 7
    ENUM_US457 = 23
    ENUM_ROTH_IRA_PROTOTYPE = 24
    ENUM_ROTH_IRA_NON_PROTOTYPE = 25
    ENUM_ROTH_CONVERSION_IRA_PROTOTYPE = 26
    ENUM_ROTH_CONVERSION_IRA_NON_PROTOTYPE = 27
    ENUM_EDUCATION_IRA_PROTOTYPE = 28
    ENUM_EDUCATION_IRA_NON_PROTOTYPE = 29
    ENUM_KEOGH = 18
    ENUM_US403B = 22

class RegistRejReasonText (field_types.String_Type) :
    _tag = '496'

class FundRenewWaiv (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '497'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class CashDistribAgentName (field_types.String_Type) :
    _tag = '498'

class CashDistribAgentCode (field_types.String_Type) :
    _tag = '499'

class CashDistribAgentAcctNumber (field_types.String_Type) :
    _tag = '500'

class CashDistribPayRef (field_types.String_Type) :
    _tag = '501'

class CardStartDate (field_types.LocalMktDate_Type) :
    _tag = '503'

class PaymentDate (field_types.LocalMktDate_Type) :
    _tag = '504'

class PaymentRemitterID (field_types.String_Type) :
    _tag = '505'

class RegistStatus (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '506'
    ENUM_ACCEPTED = 'A'
    ENUM_REMINDER = 'N'
    ENUM_REJECTED = 'R'
    ENUM_HELD = 'H'

class RegistRejReasonCode (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '507'
    ENUM_INVALID_DISTRIB_INSTNS = 13
    ENUM_INVALID_AGENT_CODE = 17
    ENUM_INVALID_ACCOUNT_NAME = 16
    ENUM_NO_REG_DETAILS = 4
    ENUM_INVALID_PAYMENT_METHOD = 15
    ENUM_INVALID_PERCENTAGE = 14
    ENUM_INVALID_OWNERSHIP_TYPE = 3
    ENUM_INVALID_TAX_EXEMPT_TYPE = 2
    ENUM_INVALID_COUNTRY = 12
    ENUM_INVALID_DATE_OF_BIRTH = 11
    ENUM_INVALID_INVESTOR_ID_SOURCE = 10
    ENUM_INVALID_INVESTOR_ID = 9
    ENUM_INVALID_MAILING_INSTRUCTIONS = 8
    ENUM_INVALID_MAILING_DETAILS = 7
    ENUM_INVALID_REG_SEQ_NO = 5
    ENUM_INVALID_ACCOUNT_TYPE = 1
    ENUM_INVALID_ACCOUNT_NUM = 18
    ENUM_INVALID_REG_DETAILS = 6

class RegistRefID (field_types.String_Type) :
    _tag = '508'

class RegistDetls (field_types.String_Type) :
    _tag = '509'

class NoDistribInsts (field_types.NumInGroup_Type) :
    _tag = '510'

class RegistEmail (field_types.String_Type) :
    _tag = '511'

class DistribPercentage (field_types.Percentage_Type) :
    _tag = '512'

class RegistID (field_types.String_Type) :
    _tag = '513'

class RegistTransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '514'
    ENUM_CANCEL = '2'
    ENUM_NEW = '0'
    ENUM_REPLACE = '1'

class ExecValuationPoint (field_types.UTCTimestamp_Type) :
    _tag = '515'

class OrderPercent (field_types.Percentage_Type) :
    _tag = '516'

class OwnershipType (field_types.char_Type) :
    _tag = '517'

class NoContAmts (field_types.NumInGroup_Type) :
    _tag = '518'

class ContAmtType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '519'
    ENUM_NET_SETTLEMENT_AMOUNT = 15
    ENUM_COMMISSION_AMOUNT = 1
    ENUM_COMMISSION_PERCENT = 2
    ENUM_INITIAL_CHARGE_AMOUNT = 3
    ENUM_INITIAL_CHARGE_PERCENT = 4
    ENUM_DISCOUNT_AMOUNT = 5
    ENUM_DISCOUNT_PERCENT = 6
    ENUM_DILUTION_LEVY_AMOUNT = 7
    ENUM_DILUTION_LEVY_PERCENT = 8
    ENUM_EXIT_CHARGE_AMOUNT = 9
    ENUM_EXIT_CHARGE_PERCENT = 10
    ENUM_FUND_BASED_RENEWAL_COMMISSION_PERCENT = 11
    ENUM_PROJECTED_FUND_VALUE = 12
    ENUM_FUND_BASED_RENEWAL_COMMISSION_ON_FUND = 14
    ENUM_FUND_BASED_RENEWAL_COMMISSION_ON_ORDER = 13

class ContAmtValue (field_types.float_Type) :
    _tag = '520'

class ContAmtCurr (field_types.Currency_Type) :
    _tag = '521'

class OwnerType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '522'
    ENUM_COMPANY_TRUSTEE = 5
    ENUM_NOMINEE = 13
    ENUM_CORPORATE_BODY = 12
    ENUM_NON_PROFIT_ORGANIZATION = 11
    ENUM_NETWORKING_SUB_ACCOUNT = 10
    ENUM_FIDUCIARIES = 9
    ENUM_TRUSTS = 8
    ENUM_PENSION_PLAN = 6
    ENUM_INDIVIDUAL_TRUSTEE = 4
    ENUM_PUBLIC_COMPANY = 2
    ENUM_PRIVATE_COMPANY = 3
    ENUM_INDIVIDUAL_INVESTOR = 1
    ENUM_CUSTODIAN_UNDER_GIFTS_TO_MINORS_ACT = 7

class PartySubID (field_types.String_Type) :
    _tag = '523'

class NestedPartyID (field_types.String_Type) :
    _tag = '524'

class NestedPartyIDSource (field_types.char_Type) :
    _tag = '525'

class SecondaryClOrdID (field_types.String_Type) :
    _tag = '526'

class SecondaryExecID (field_types.String_Type) :
    _tag = '527'

class OrderCapacity (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '528'
    ENUM_RISKLESS_PRINCIPAL = 'R'
    ENUM_INDIVIDUAL = 'I'
    ENUM_PRINCIPAL = 'P'
    ENUM_AGENT_FOR_OTHER_MEMBER = 'W'
    ENUM_AGENCY = 'A'
    ENUM_PROPRIETARY = 'G'

class OrderRestrictions (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '529'
    ENUM_FOREIGN_ENTITY = '7'
    ENUM_RISKLESS_ARBITRAGE = 'A'
    ENUM_PROGRAM_TRADE = '1'
    ENUM_EXTERNAL_MARKET_PARTICIPANT = '8'
    ENUM_ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_UNDERLYING = '6'
    ENUM_ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_SECURITY = '5'
    ENUM_NON_INDEX_ARBITRAGE = '3'
    ENUM_INDEX_ARBITRAGE = '2'
    ENUM_COMPETING_MARKET_MAKER = '4'
    ENUM_EXTERNAL_INTER_CONNECTED_MARKET_LINKAGE = '9'

class MassCancelRequestType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '530'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY = '1'
    ENUM_CANCEL_ALL_ORDERS = '7'
    ENUM_CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY_TYPE = '5'
    ENUM_CANCEL_ORDERS_FOR_ACFI_CODE = '4'
    ENUM_CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    ENUM_CANCEL_ORDERS_FOR_A_PRODUCT = '3'

class MassCancelResponse (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '531'
    ENUM_CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    ENUM_CANCEL_REQUEST_REJECTED = '0'
    ENUM_CANCEL_ALL_ORDERS = '7'
    ENUM_CANCEL_ORDERS_FOR_A_PRODUCT = '3'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY_TYPE = '5'
    ENUM_CANCEL_ORDERS_FOR_ACFI_CODE = '4'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY = '1'
    ENUM_CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'

class MassCancelRejectReason (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '532'
    ENUM_INVALID_OR_UNKOWN_UNDERLYING_SECURITY = '2'
    ENUM_INVALID_OR_UNKNOWN_TRADING_SESSION = '6'
    ENUM_INVALID_OR_UNKNOWN_SECURITY_TYPE = '5'
    ENUM_INVALID_OR_UNKNOWN_PRODUCT = '3'
    ENUM_INVALID_OR_UNKNOWN_SECURITY = '1'
    ENUM_MASS_CANCEL_NOT_SUPPORTED = '0'
    ENUM_INVALID_OR_UNKNOWN_CFI_CODE = '4'

class TotalAffectedOrders (field_types.int_Type) :
    _tag = '533'

class NoAffectedOrders (field_types.NumInGroup_Type) :
    _tag = '534'

class AffectedOrderID (field_types.String_Type) :
    _tag = '535'

class AffectedSecondaryOrderID (field_types.String_Type) :
    _tag = '536'

class QuoteType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '537'
    ENUM_INDICATIVE = 0
    ENUM_TRADEABLE = 1
    ENUM_RESTRICTED_TRADEABLE = 2

class NestedPartyRole (field_types.int_Type) :
    _tag = '538'

class NoNestedPartyIDs (field_types.NumInGroup_Type) :
    _tag = '539'

class TotalAccruedInterestAmt (field_types.Amt_Type) :
    _tag = '540'

class MaturityDate (field_types.LocalMktDate_Type) :
    _tag = '541'

class UnderlyingMaturityDate (field_types.LocalMktDate_Type) :
    _tag = '542'

class InstrRegistry (field_types.String_Type) :
    _tag = '543'

class CashMargin (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '544'
    ENUM_MARGIN_OPEN = '2'
    ENUM_MARGIN_CLOSE = '3'
    ENUM_CASH = '1'

class NestedPartySubID (field_types.String_Type) :
    _tag = '545'

class Scope (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '546'
    ENUM_LOCAL_MARKET = '1'
    ENUM_NATIONAL = '2'
    ENUM_GLOBAL = '3'

class MDImplicitDelete (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '547'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class CrossID (field_types.String_Type) :
    _tag = '548'

class CrossType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '549'
    ENUM_CROSS_AON = 1
    ENUM_CROSS_IOC = 2
    ENUM_CROSS_ONE_SIDE = 3
    ENUM_CROSS_SAME_PRICE = 4

class CrossPrioritization (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '550'
    ENUM_SELL_SIDE_IS_PRIORITIZED = 2
    ENUM_NONE = 0
    ENUM_BUY_SIDE_IS_PRIORITIZED = 1

class OrigCrossID (field_types.String_Type) :
    _tag = '551'

class NoSides (field_types.NumInGroup_Type, field_types.NumInGroup_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '552'
    ENUM_ONE_SIDE = 1
    ENUM_BOTH_SIDES = 2

class Username (field_types.String_Type) :
    _tag = '553'

class Password (field_types.String_Type) :
    _tag = '554'

class NoLegs (field_types.NumInGroup_Type) :
    _tag = '555'

class LegCurrency (field_types.Currency_Type) :
    _tag = '556'

class TotalNumSecurityTypes (field_types.int_Type) :
    _tag = '557'

class NoSecurityTypes (field_types.NumInGroup_Type) :
    _tag = '558'

class SecurityListRequestType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '559'
    ENUM_SECURITY_TYPE_AND = 1
    ENUM_PRODUCT = 2
    ENUM_TRADING_SESSION_ID = 3
    ENUM_ALL_SECURITIES = 4
    ENUM_SYMBOL = 0

class SecurityRequestResult (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '560'
    ENUM_INSTRUMENT_DATA_TEMPORARILY_UNAVAILABLE = 4
    ENUM_VALID_REQUEST = 0
    ENUM_INVALID_OR_UNSUPPORTED_REQUEST = 1
    ENUM_REQUEST_FOR_INSTRUMENT_DATA_NOT_SUPPORTED = 5
    ENUM_NOT_AUTHORIZED_TO_RETRIEVE_INSTRUMENT_DATA = 3
    ENUM_NO_INSTRUMENTS_FOUND = 2

class RoundLot (field_types.Qty_Type) :
    _tag = '561'

class MinTradeVol (field_types.Qty_Type) :
    _tag = '562'

class MultiLegRptTypeReq (field_types.int_Type) :
    _tag = '563'

class LegPositionEffect (field_types.char_Type) :
    _tag = '564'

class LegCoveredOrUncovered (field_types.int_Type) :
    _tag = '565'

class LegPrice (field_types.Price_Type) :
    _tag = '566'

class TradSesStatusRejReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '567'
    ENUM_UNKNOWN_OR_INVALID_TRADING_SESSION_ID = 1

class TradeRequestID (field_types.String_Type) :
    _tag = '568'

class TradeRequestType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '569'
    ENUM_ADVISORIES_THAT_MATCH_CRITERIA = 4
    ENUM_UNREPORTED_TRADES_THAT_MATCH_CRITERIA = 3
    ENUM_UNMATCHED_TRADES_THAT_MATCH_CRITERIA = 2
    ENUM_MATCHED_TRADES_MATCHING_CRITERIA = 1
    ENUM_ALL_TRADES = 0

class PreviouslyReported (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '570'
    ENUM_NOT_REPORTED_TO_COUNTERPARTY = 'N'
    ENUM_PERVIOUSLY_REPORTED_TO_COUNTERPARTY = 'Y'

class TradeReportID (field_types.String_Type) :
    _tag = '571'

class TradeReportRefID (field_types.String_Type) :
    _tag = '572'

class MatchStatus (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '573'
    ENUM_COMPARED = '0'
    ENUM_UNCOMPARED = '1'
    ENUM_ADVISORY_OR_ALERT = '2'

class MatchType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '574'
    ENUM_A5_EXACT_MATCH_SUMMARIZED_QUANTITY = 'S5'
    ENUM_EXACT_MATCH_MINUS_BADGES_TIMES = 'M1'
    ENUM_ACTM6_MATCH = 'M6'
    ENUM_ACT_DEFAULT_AFTER_M2 = 'M5'
    ENUM_ACT_ACCEPTED_TRADE = 'M3'
    ENUM_A2_EXACT_MATCH_SUMMARIZED_QUANTITY = 'S2'
    ENUM_A3_EXACT_MATCH_SUMMARIZED_QUANTITY = 'S3'
    ENUM_A4_EXACT_MATCH_SUMMARIZED_QUANTITY = 'S4'
    ENUM_SUMMARIZED_MATCH_MINUS_BADGES_TIMES = 'M2'
    ENUM_EXACT_MATCH_PLUS4_BADGES = 'A2'
    ENUM_EXACT_MATCH_PLUS2_BADGES_EXEC_TIME = 'A3'
    ENUM_EXACT_MATCH_PLUS2_BADGES = 'A4'
    ENUM_STAMPED_ADVISORIES_OR_SPECIALIST_ACCEPTS = 'AQ'
    ENUM_OCS_LOCKED_IN = 'MT'
    ENUM_ACT_DEFAULT_TRADE = 'M4'
    ENUM_EXACT_MATCH_PLUS4_BADGES_EXEC_TIME = 'A1'
    ENUM_A1_EXACT_MATCH_SUMMARIZED_QUANTITY = 'S1'
    ENUM_EXACT_MATCH_PLUS_EXEC_TIME = 'A5'

class OddLot (field_types.Boolean_Type) :
    _tag = '575'

class NoClearingInstructions (field_types.int_Type) :
    _tag = '576'

class ClearingInstruction (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '577'
    ENUM_MANUAL_MODE = 8
    ENUM_MULTILATERAL_NETTING = 5
    ENUM_AUTOMATIC_POSTING_MODE = 9
    ENUM_BILATERAL_NETTING_ONLY = 2
    ENUM_CLEAR_AGAINST_CENTRAL_COUNTERPARTY = 6
    ENUM_AUTOMATIC_GIVE_UP_MODE = 10
    ENUM_SPECIAL_TRADE = 4
    ENUM_EX_CLEARING = 3
    ENUM_PROCESS_NORMALLY = 0
    ENUM_EXCLUDE_FROM_CENTRAL_COUNTERPARTY = 7
    ENUM_EXCLUDE_FROM_ALL_NETTING = 1

class TradeInputSource (field_types.String_Type) :
    _tag = '578'

class TradeInputDevice (field_types.String_Type) :
    _tag = '579'

class NoDates (field_types.NumInGroup_Type) :
    _tag = '580'

class AccountType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '581'
    ENUM_HOUSE_TRADER = 3
    ENUM_HOUSE_TRADER_CROSS_MARGINED = 7
    ENUM_CARRIED_NON_CUSTOMER_SIDE_CROSS_MARGINED = 6
    ENUM_FLOOR_TRADER = 4
    ENUM_CARRIED_NON_CUSTOMER_SIDE = 2
    ENUM_CARRIED_CUSTOMER_SIDE = 1
    ENUM_JOINT_BACK_OFFICE_ACCOUNT = 8

class CustOrderCapacity (field_types.int_Type) :
    _tag = '582'

class ClOrdLinkID (field_types.String_Type) :
    _tag = '583'

class MassStatusReqID (field_types.String_Type) :
    _tag = '584'

class MassStatusReqType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '585'
    ENUM_STATUS_FOR_ORDERS_FOR_A_SECURITY = 1
    ENUM_STATUS_FOR_ORDERS_FOR_AN_UNDERLYING_SECURITY = 2
    ENUM_STATUS_FOR_ORDERS_FOR_A_PRODUCT = 3
    ENUM_STATUS_FOR_ORDERS_FOR_ACFI_CODE = 4
    ENUM_STATUS_FOR_ORDERS_FOR_A_SECURITY_TYPE = 5
    ENUM_STATUS_FOR_ORDERS_FOR_A_TRADING_SESSION = 6
    ENUM_STATUS_FOR_ORDERS_FOR_A_PARTY_ID = 8
    ENUM_STATUS_FOR_ALL_ORDERS = 7

class OrigOrdModTime (field_types.UTCTimestamp_Type) :
    _tag = '586'

class LegSettlmntTyp (field_types.char_Type) :
    _tag = '587'

class LegFutSettDate (field_types.LocalMktDate_Type) :
    _tag = '588'

class DayBookingInst (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '589'
    ENUM_AUTO = '0'
    ENUM_SPEAK_WITH_ORDER_INITIATOR_BEFORE_BOOKING = '1'

class BookingUnit (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '590'
    ENUM_AGGREGATE_PARTIAL_EXECUTIONS_ON_THIS_ORDER = '1'
    ENUM_AGGREGATE_EXECUTIONS_FOR_THIS_SYMBOL = '2'
    ENUM_EACH_PARTIAL_EXECUTION_IS_A_BOOKABLE_UNIT = '0'

class PreallocMethod (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '591'
    ENUM_PRO_RATA = '0'
    ENUM_DO_NOT_PRO_RATA = '1'

class UnderlyingCountryOfIssue (field_types.Country_Type) :
    _tag = '592'

class UnderlyingStateOrProvinceOfIssue (field_types.String_Type) :
    _tag = '593'

class UnderlyingLocaleOfIssue (field_types.String_Type) :
    _tag = '594'

class UnderlyingInstrRegistry (field_types.String_Type) :
    _tag = '595'

class LegCountryOfIssue (field_types.Country_Type) :
    _tag = '596'

class LegStateOrProvinceOfIssue (field_types.String_Type) :
    _tag = '597'

class LegLocaleOfIssue (field_types.String_Type) :
    _tag = '598'

class LegInstrRegistry (field_types.String_Type) :
    _tag = '599'

class LegSymbol (field_types.String_Type) :
    _tag = '600'

class LegSymbolSfx (field_types.String_Type) :
    _tag = '601'

class LegSecurityID (field_types.String_Type) :
    _tag = '602'

class LegSecurityIDSource (field_types.String_Type) :
    _tag = '603'

class NoLegSecurityAltID (field_types.NumInGroup_Type) :
    _tag = '604'

class LegSecurityAltID (field_types.String_Type) :
    _tag = '605'

class LegSecurityAltIDSource (field_types.String_Type) :
    _tag = '606'

class LegProduct (field_types.int_Type) :
    _tag = '607'

class LegCFICode (field_types.String_Type) :
    _tag = '608'

class LegSecurityType (field_types.String_Type) :
    _tag = '609'

class LegMaturityMonthYear (field_types.MonthYear_Type) :
    _tag = '610'

class LegMaturityDate (field_types.LocalMktDate_Type) :
    _tag = '611'

class LegStrikePrice (field_types.Price_Type) :
    _tag = '612'

class LegOptAttribute (field_types.char_Type) :
    _tag = '613'

class LegContractMultiplier (field_types.float_Type) :
    _tag = '614'

class LegCouponRate (field_types.Percentage_Type) :
    _tag = '615'

class LegSecurityExchange (field_types.Exchange_Type) :
    _tag = '616'

class LegIssuer (field_types.String_Type) :
    _tag = '617'

class EncodedLegIssuerLen (field_types.Length_Type) :
    _tag = '618'

class EncodedLegIssuer (field_types.data_Type) :
    _tag = '619'

class LegSecurityDesc (field_types.String_Type) :
    _tag = '620'

class EncodedLegSecurityDescLen (field_types.Length_Type) :
    _tag = '621'

class EncodedLegSecurityDesc (field_types.data_Type) :
    _tag = '622'

class LegRatioQty (field_types.float_Type) :
    _tag = '623'

class LegSide (field_types.char_Type) :
    _tag = '624'

class TradingSessionSubID (field_types.String_Type) :
    _tag = '625'

class AllocType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '626'
    ENUM_BUYSIDE_READY_TO_BOOK = 6
    ENUM_PRELIMINARY = 2
    ENUM_SELLSIDE_CALCULATED_USING_PRELIMINARY = 3
    ENUM_READY_TO_BOOK = 5
    ENUM_CALCULATED = 1
    ENUM_SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY = 4

class NoHops (field_types.NumInGroup_Type) :
    _tag = '627'

class HopCompID (field_types.String_Type) :
    _tag = '628'

class HopSendingTime (field_types.UTCTimestamp_Type) :
    _tag = '629'

class HopRefID (field_types.SeqNum_Type) :
    _tag = '630'

class MidPx (field_types.Price_Type) :
    _tag = '631'

class BidYield (field_types.Percentage_Type) :
    _tag = '632'

class MidYield (field_types.Percentage_Type) :
    _tag = '633'

class OfferYield (field_types.Percentage_Type) :
    _tag = '634'

class ClearingFeeIndicator (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '635'
    ENUM_FIRMS106_H_AND106_J = 'H'
    ENUM_FIFTH_YEAR_DELEGATE = '5'
    ENUM_FOURTH_YEAR_DELEGATE = '4'
    ENUM_THIRD_YEAR_DELEGATE = '3'
    ENUM_SECOND_YEAR_DELEGATE = '2'
    ENUM_FIRST_YEAR_DELEGATE = '1'
    ENUM_ALL_OTHER_OWNERSHIP_TYPES = 'M'
    ENUM_GIM = 'I'
    ENUM_SIXTH_YEAR_DELEGATE = '9'
    ENUM_FULL_AND_ASSOCIATE_MEMBER = 'F'
    ENUM_EQUITY_MEMBER_AND_CLEARING_MEMBER = 'E'
    ENUM_NON_MEMBER_AND_CUSTOMER = 'C'
    ENUM_CBOE_MEMBER = 'B'
    ENUM_LESSEE106_F_EMPLOYEES = 'L'

class WorkingIndicator (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '636'
    ENUM_NOT_WORKING = 'N'
    ENUM_WORKING = 'Y'

class LegLastPx (field_types.Price_Type) :
    _tag = '637'

class PriorityIndicator (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '638'
    ENUM_PRIORITY_UNCHANGED = 0
    ENUM_LOST_PRIORITY_AS_RESULT_OF_ORDER_CHANGE = 1

class PriceImprovement (field_types.PriceOffset_Type) :
    _tag = '639'

class Price2 (field_types.Price_Type) :
    _tag = '640'

class LastForwardPoints2 (field_types.PriceOffset_Type) :
    _tag = '641'

class BidForwardPoints2 (field_types.PriceOffset_Type) :
    _tag = '642'

class OfferForwardPoints2 (field_types.PriceOffset_Type) :
    _tag = '643'

class RFQReqID (field_types.String_Type) :
    _tag = '644'

class MktBidPx (field_types.Price_Type) :
    _tag = '645'

class MktOfferPx (field_types.Price_Type) :
    _tag = '646'

class MinBidSize (field_types.Qty_Type) :
    _tag = '647'

class MinOfferSize (field_types.Qty_Type) :
    _tag = '648'

class QuoteStatusReqID (field_types.String_Type) :
    _tag = '649'

class LegalConfirm (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '650'
    ENUM_LEGAL_CONFIRM = 'Y'
    ENUM_DOES_NOT_CONSITUTE_A_LEGAL_CONFIRM = 'N'

class UnderlyingLastPx (field_types.Price_Type) :
    _tag = '651'

class UnderlyingLastQty (field_types.Qty_Type) :
    _tag = '652'

class LegRefID (field_types.String_Type) :
    _tag = '654'

class ContraLegRefID (field_types.String_Type) :
    _tag = '655'

class SettlCurrBidFxRate (field_types.float_Type) :
    _tag = '656'

class SettlCurrOfferFxRate (field_types.float_Type) :
    _tag = '657'

class QuoteRequestRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '658'
    ENUM_UNKNOWN_SYMBOL = 1
    ENUM_EXCHANGE = 2
    ENUM_QUOTE_REQUEST_EXCEEDS_LIMIT = 3
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_INVALID_PRICE = 5
    ENUM_NOT_AUTHORIZED_TO_REQUEST_QUOTE = 6

class SideComplianceID (field_types.String_Type) :
    _tag = '659'
