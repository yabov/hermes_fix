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
    ENUM_PER_UNIT = '1'
    ENUM_PERCENT = '2'
    ENUM_ABSOLUTE = '3'
    ENUM_PERCENTAGE_WAIVED_CASH_DISCOUNT = '4'
    ENUM_PERCENTAGE_WAIVED_ENHANCED_UNITS = '5'
    ENUM_POINTS_PER_BOND_OR_CONTRACT = '6'

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
    ENUM_NOT_HELD = '1'
    ENUM_WORK = '2'
    ENUM_GO_ALONG = '3'
    ENUM_OVER_THE_DAY = '4'
    ENUM_HELD = '5'
    ENUM_PARTICIPATE_DO_NOT_INITIATE = '6'
    ENUM_STRICT_SCALE = '7'
    ENUM_TRY_TO_SCALE = '8'
    ENUM_STAY_ON_BID_SIDE = '9'
    ENUM_STAY_ON_OFFER_SIDE = '0'
    ENUM_NO_CROSS = 'A'
    ENUM_OK_TO_CROSS = 'B'
    ENUM_CALL_FIRST = 'C'
    ENUM_PERCENT_OF_VOLUME = 'D'
    ENUM_DO_NOT_INCREASE = 'E'
    ENUM_DO_NOT_REDUCE = 'F'
    ENUM_ALL_OR_NONE = 'G'
    ENUM_REINSTATE_ON_SYSTEM_FAILURE = 'H'
    ENUM_INSTITUTIONS_ONLY = 'I'
    ENUM_REINSTATE_ON_TRADING_HALT = 'J'
    ENUM_CANCEL_ON_TRADING_HALT = 'K'
    ENUM_LAST_PEG = 'L'
    ENUM_MID_PRICE_PEG = 'M'
    ENUM_NON_NEGOTIABLE = 'N'
    ENUM_OPENING_PEG = 'O'
    ENUM_MARKET_PEG = 'P'
    ENUM_CANCEL_ON_SYSTEM_FAILURE = 'Q'
    ENUM_PRIMARY_PEG = 'R'
    ENUM_SUSPEND = 'S'
    ENUM_CUSTOMER_DISPLAY_INSTRUCTION = 'U'
    ENUM_NETTING = 'V'
    ENUM_PEG_TO_VWAP = 'W'
    ENUM_TRADE_ALONG = 'X'
    ENUM_TRY_TO_STOP = 'Y'
    ENUM_CANCEL_IF_NOT_BEST = 'Z'
    ENUM_TRAILING_STOP_PEG = 'a'
    ENUM_STRICT_LIMIT = 'b'
    ENUM_IGNORE_PRICE_VALIDITY_CHECKS = 'c'
    ENUM_PEG_TO_LIMIT_PRICE = 'd'
    ENUM_WORK_TO_TARGET_STRATEGY = 'e'

class ExecRefID (field_types.String_Type) :
    _tag = '19'

class HandlInst (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '21'
    ENUM_AUTOMATED_EXECUTION_NO_INTERVENTION = '1'
    ENUM_AUTOMATED_EXECUTION_INTERVENTION_OK = '2'
    ENUM_MANUAL_ORDER = '3'

class SecurityIDSource (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
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
    ENUM_BLOOMBERG_SYMBOL = 'A'
    ENUM_WERTPAPIER = 'B'
    ENUM_DUTCH = 'C'
    ENUM_VALOREN = 'D'
    ENUM_SICOVAM = 'E'
    ENUM_BELGIAN = 'F'
    ENUM_COMMON = 'G'
    ENUM_CLEARING_HOUSE = 'H'
    ENUM_ISDA_FP_ML_SPECIFICATION = 'I'
    ENUM_OPTION_PRICE_REPORTING_AUTHORITY = 'J'

class IOIID (field_types.String_Type) :
    _tag = '23'

class IOIQltyInd (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '25'
    ENUM_LOW = 'L'
    ENUM_MEDIUM = 'M'
    ENUM_HIGH = 'H'

class IOIRefID (field_types.String_Type) :
    _tag = '26'

class IOIQty (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '27'
    ENUM_SMALL = 'S'
    ENUM_MEDIUM = 'M'
    ENUM_LARGE = 'L'

class IOITransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '28'
    ENUM_NEW = 'N'
    ENUM_CANCEL = 'C'
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

class LastQty (field_types.Qty_Type) :
    _tag = '32'

class NoLinesOfText (field_types.NumInGroup_Type) :
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
    ENUM_XML_NON_FIX = 'n'
    ENUM_REGISTRATION_INSTRUCTIONS = 'o'
    ENUM_REGISTRATION_INSTRUCTIONS_RESPONSE = 'p'
    ENUM_ORDER_MASS_CANCEL_REQUEST = 'q'
    ENUM_ORDER_MASS_CANCEL_REPORT = 'r'
    ENUM_NEW_ORDER_CROSS = 's'
    ENUM_CROSS_ORDER_CANCEL_REPLACE_REQUEST = 't'
    ENUM_CROSS_ORDER_CANCEL_REQUEST = 'u'
    ENUM_SECURITY_TYPE_REQUEST = 'v'
    ENUM_SECURITY_TYPES = 'w'
    ENUM_SECURITY_LIST_REQUEST = 'x'
    ENUM_SECURITY_LIST = 'y'
    ENUM_DERIVATIVE_SECURITY_LIST_REQUEST = 'z'
    ENUM_DERIVATIVE_SECURITY_LIST = 'AA'
    ENUM_NEW_ORDER_MULTILEG = 'AB'
    ENUM_MULTILEG_ORDER_CANCEL_REPLACE = 'AC'
    ENUM_TRADE_CAPTURE_REPORT_REQUEST = 'AD'
    ENUM_TRADE_CAPTURE_REPORT = 'AE'
    ENUM_ORDER_MASS_STATUS_REQUEST = 'AF'
    ENUM_QUOTE_REQUEST_REJECT = 'AG'
    ENUM_RFQ_REQUEST = 'AH'
    ENUM_QUOTE_STATUS_REPORT = 'AI'
    ENUM_QUOTE_RESPONSE = 'AJ'
    ENUM_CONFIRMATION = 'AK'
    ENUM_POSITION_MAINTENANCE_REQUEST = 'AL'
    ENUM_POSITION_MAINTENANCE_REPORT = 'AM'
    ENUM_REQUEST_FOR_POSITIONS = 'AN'
    ENUM_REQUEST_FOR_POSITIONS_ACK = 'AO'
    ENUM_POSITION_REPORT = 'AP'
    ENUM_TRADE_CAPTURE_REPORT_REQUEST_ACK = 'AQ'
    ENUM_TRADE_CAPTURE_REPORT_ACK = 'AR'
    ENUM_ALLOCATION_REPORT = 'AS'
    ENUM_ALLOCATION_REPORT_ACK = 'AT'
    ENUM_CONFIRMATION_ACK = 'AU'
    ENUM_SETTLEMENT_INSTRUCTION_REQUEST = 'AV'
    ENUM_ASSIGNMENT_REPORT = 'AW'
    ENUM_COLLATERAL_REQUEST = 'AX'
    ENUM_COLLATERAL_ASSIGNMENT = 'AY'
    ENUM_COLLATERAL_RESPONSE = 'AZ'
    ENUM_COLLATERAL_REPORT = 'BA'
    ENUM_COLLATERAL_INQUIRY = 'BB'
    ENUM_NETWORK_COUNTERPARTY_SYSTEM_STATUS_REQUEST = 'BC'
    ENUM_NETWORK_COUNTERPARTY_SYSTEM_STATUS_RESPONSE = 'BD'
    ENUM_USER_REQUEST = 'BE'
    ENUM_USER_RESPONSE = 'BF'
    ENUM_COLLATERAL_INQUIRY_ACK = 'BG'
    ENUM_CONFIRMATION_REQUEST = 'BH'

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
    ENUM_FILLED = '2'
    ENUM_DONE_FOR_DAY = '3'
    ENUM_CANCELED = '4'
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
    ENUM_WITH_OR_WITHOUT = '6'
    ENUM_LIMIT_OR_BETTER = '7'
    ENUM_LIMIT_WITH_OR_WITHOUT = '8'
    ENUM_ON_BASIS = '9'
    ENUM_PREVIOUSLY_QUOTED = 'D'
    ENUM_PREVIOUSLY_INDICATED = 'E'
    ENUM_FOREX_SWAP = 'G'
    ENUM_FUNARI = 'I'
    ENUM_MARKET_IF_TOUCHED = 'J'
    ENUM_MARKET_WITH_LEFT_OVER_AS_LIMIT = 'K'
    ENUM_PREVIOUS_FUND_VALUATION_POINT = 'L'
    ENUM_NEXT_FUND_VALUATION_POINT = 'M'
    ENUM_PEGGED = 'P'

class OrigClOrdID (field_types.String_Type) :
    _tag = '41'

class OrigTime (field_types.UTCTimestamp_Type) :
    _tag = '42'

class PossDupFlag (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '43'
    ENUM_POSSIBLE_DUPLICATE = 'Y'
    ENUM_ORIGINAL_TRANSMISSION = 'N'

class Price (field_types.Price_Type) :
    _tag = '44'

class RefSeqNum (field_types.SeqNum_Type) :
    _tag = '45'

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
    ENUM_BUY = '1'
    ENUM_SELL = '2'
    ENUM_BUY_MINUS = '3'
    ENUM_SELL_PLUS = '4'
    ENUM_SELL_SHORT = '5'
    ENUM_SELL_SHORT_EXEMPT = '6'
    ENUM_UNDISCLOSED = '7'
    ENUM_CROSS = '8'
    ENUM_CROSS_SHORT = '9'
    ENUM_CROSS_SHORT_EXEMPT = 'A'
    ENUM_AS_DEFINED = 'B'
    ENUM_OPPOSITE = 'C'
    ENUM_SUBSCRIBE = 'D'
    ENUM_REDEEM = 'E'
    ENUM_LEND = 'F'
    ENUM_BORROW = 'G'

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
    ENUM_AT_THE_CLOSE = '7'

class TransactTime (field_types.UTCTimestamp_Type) :
    _tag = '60'

class Urgency (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '61'
    ENUM_NORMAL = '0'
    ENUM_FLASH = '1'
    ENUM_BACKGROUND = '2'

class ValidUntilTime (field_types.UTCTimestamp_Type) :
    _tag = '62'

class SettlType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
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

class SettlDate (field_types.LocalMktDate_Type) :
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

class RefAllocID (field_types.String_Type) :
    _tag = '72'

class NoOrders (field_types.NumInGroup_Type) :
    _tag = '73'

class AvgPxPrecision (field_types.int_Type) :
    _tag = '74'

class TradeDate (field_types.LocalMktDate_Type) :
    _tag = '75'

class PositionEffect (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '77'
    ENUM_OPEN = 'O'
    ENUM_CLOSE = 'C'
    ENUM_ROLLED = 'R'
    ENUM_FIFO = 'F'

class NoAllocs (field_types.NumInGroup_Type) :
    _tag = '78'

class AllocAccount (field_types.String_Type) :
    _tag = '79'

class AllocQty (field_types.Qty_Type) :
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

class NoDlvyInst (field_types.NumInGroup_Type) :
    _tag = '85'

class AllocStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '87'
    ENUM_ACCEPTED = 0
    ENUM_BLOCK_LEVEL_REJECT = 1
    ENUM_ACCOUNT_LEVEL_REJECT = 2
    ENUM_RECEIVED = 3
    ENUM_INCOMPLETE = 4
    ENUM_REJECTED_BY_INTERMEDIARY = 5

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
    ENUM_INCORRECT_ALLOCATED_QUANTITY = 8
    ENUM_CALCULATION_DIFFERENCE = 9
    ENUM_UNKNOWN_OR_STALE_EXEC_ID = 10
    ENUM_MISMATCHED_DATA = 11
    ENUM_UNKNOWN_CL_ORD_ID = 12
    ENUM_WAREHOUSE_REQUEST_REJECTED = 13

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
    ENUM_POSSIBLE_RESEND = 'Y'
    ENUM_ORIGINAL_TRANSMISSION = 'N'

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
    ENUM_UNABLE_TO_PROCESS_ORDER_MASS_CANCEL_REQUEST = 4
    ENUM_ORIG_ORD_MOD_TIME = 5
    ENUM_DUPLICATE_CL_ORD_ID = 6
    ENUM_OTHER = 99

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
    ENUM_TRADE_ALONG_REQUIRED = 9
    ENUM_INVALID_INVESTOR_ID = 10
    ENUM_UNSUPPORTED_ORDER_CHARACTERISTIC = 11
    ENUM_INCORRECT_QUANTITY = 13
    ENUM_INCORRECT_ALLOCATED_QUANTITY = 14
    ENUM_UNKNOWN_ACCOUNT = 15
    ENUM_OTHER = 99

class IOIQualifier (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '104'
    ENUM_ALL_OR_NONE = 'A'
    ENUM_MARKET_ON_CLOSE = 'B'
    ENUM_AT_THE_CLOSE = 'C'
    ENUM_VWAP = 'D'
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
    ENUM_UNKNOWN_SYMBOL = 'A'
    ENUM_WRONG_SIDE = 'B'
    ENUM_QUANTITY_EXCEEDS_ORDER = 'C'
    ENUM_NO_MATCHING_ORDER = 'D'
    ENUM_PRICE_EXCEEDS_LIMIT = 'E'
    ENUM_CALCULATION_DIFFERENCE = 'F'
    ENUM_OTHER = 'Z'

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
    ENUM_REGULATORY = '1'
    ENUM_TAX = '2'
    ENUM_LOCAL_COMMISSION = '3'
    ENUM_EXCHANGE_FEES = '4'
    ENUM_STAMP = '5'
    ENUM_LEVY = '6'
    ENUM_OTHER = '7'
    ENUM_MARKUP = '8'
    ENUM_CONSUMPTION_TAX = '9'
    ENUM_PER_TRANSACTION = '10'
    ENUM_CONVERSION = '11'
    ENUM_AGENT = '12'

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
    ENUM_NEW = '0'
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
    ENUM_TRADE = 'F'
    ENUM_TRADE_CORRECT = 'G'
    ENUM_TRADE_CANCEL = 'H'
    ENUM_ORDER_STATUS = 'I'

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
    ENUM_MULTIPLY = 'M'
    ENUM_DIVIDE = 'D'

class NumDaysInterest (field_types.int_Type) :
    _tag = '157'

class AccruedInterestRate (field_types.Percentage_Type) :
    _tag = '158'

class AccruedInterestAmt (field_types.Amt_Type) :
    _tag = '159'

class SettlInstMode (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '160'
    ENUM_STANDING_INSTRUCTIONS_PROVIDED = '1'
    ENUM_SPECIFIC_ORDER_FOR_A_SINGLE_ACCOUNT = '4'
    ENUM_REQUEST_REJECT = '5'

class AllocText (field_types.String_Type) :
    _tag = '161'

class SettlInstID (field_types.String_Type) :
    _tag = '162'

class SettlInstTransType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '163'
    ENUM_NEW = 'N'
    ENUM_CANCEL = 'C'
    ENUM_REPLACE = 'R'
    ENUM_RESTATE = 'T'

class EmailThreadID (field_types.String_Type) :
    _tag = '164'

class SettlInstSource (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '165'
    ENUM_BROKER_CREDIT = '1'
    ENUM_INSTITUTION = '2'
    ENUM_INVESTOR = '3'

class SecurityType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '167'
    ENUM_EURO_SUPRANATIONAL_COUPONS = 'EUSUPRA'
    ENUM_FEDERAL_AGENCY_COUPON = 'FAC'
    ENUM_FEDERAL_AGENCY_DISCOUNT_NOTE = 'FADN'
    ENUM_PRIVATE_EXPORT_FUNDING = 'PEF'
    ENUM_USD_SUPRANATIONAL_COUPONS = 'SUPRA'
    ENUM_CORPORATE_BOND = 'CORP'
    ENUM_CORPORATE_PRIVATE_PLACEMENT = 'CPP'
    ENUM_CONVERTIBLE_BOND = 'CB'
    ENUM_DUAL_CURRENCY = 'DUAL'
    ENUM_EURO_CORPORATE_BOND = 'EUCORP'
    ENUM_INDEXED_LINKED = 'XLINKD'
    ENUM_STRUCTURED_NOTES = 'STRUCT'
    ENUM_YANKEE_CORPORATE_BOND = 'YANK'
    ENUM_FOREIGN_EXCHANGE_CONTRACT = 'FOR'
    ENUM_COMMON_STOCK = 'CS'
    ENUM_PREFERRED_STOCK = 'PS'
    ENUM_BRADY_BOND = 'BRADY'
    ENUM_EURO_SOVEREIGNS = 'EUSOV'
    ENUM_US_TREASURY_BOND = 'TBOND'
    ENUM_INTEREST_STRIP_FROM_ANY_BOND_OR_NOTE = 'TINT'
    ENUM_TREASURY_INFLATION_PROTECTED_SECURITIES = 'TIPS'
    ENUM_PRINCIPAL_STRIP_OF_A_CALLABLE_BOND_OR_NOTE = 'TCAL'
    ENUM_PRINCIPAL_STRIP_FROM_A_NON_CALLABLE_BOND_OR_NOTE = 'TPRN'
    ENUM_US_TREASURY_NOTE_OLD = 'UST'
    ENUM_US_TREASURY_BILL_OLD = 'USTB'
    ENUM_US_TREASURY_NOTE = 'TNOTE'
    ENUM_US_TREASURY_BILL = 'TBILL'
    ENUM_REPURCHASE = 'REPO'
    ENUM_FORWARD = 'FORWARD'
    ENUM_BUY_SELLBACK = 'BUYSELL'
    ENUM_SECURITIES_LOAN = 'SECLOAN'
    ENUM_SECURITIES_PLEDGE = 'SECPLEDGE'
    ENUM_TERM_LOAN = 'TERM'
    ENUM_REVOLVER_LOAN = 'RVLV'
    ENUM_REVOLVER = 'RVLVTRM'
    ENUM_BRIDGE_LOAN = 'BRIDGE'
    ENUM_LETTER_OF_CREDIT = 'LOFC'
    ENUM_SWING_LINE_FACILITY = 'SWING'
    ENUM_DEBTOR_IN_POSSESSION = 'DINP'
    ENUM_DEFAULTED = 'DEFLTED'
    ENUM_WITHDRAWN = 'WITHDRN'
    ENUM_REPLACED = 'REPLACD'
    ENUM_MATURED = 'MATURED'
    ENUM_AMENDED = 'AMENDED'
    ENUM_RETIRED = 'RETIRED'
    ENUM_BANKERS_ACCEPTANCE = 'BA'
    ENUM_BANK_NOTES = 'BN'
    ENUM_BILL_OF_EXCHANGES = 'BOX'
    ENUM_CERTIFICATE_OF_DEPOSIT = 'CD'
    ENUM_CALL_LOANS = 'CL'
    ENUM_COMMERCIAL_PAPER = 'CP'
    ENUM_DEPOSIT_NOTES = 'DN'
    ENUM_EURO_CERTIFICATE_OF_DEPOSIT = 'EUCD'
    ENUM_EURO_COMMERCIAL_PAPER = 'EUCP'
    ENUM_LIQUIDITY_NOTE = 'LQN'
    ENUM_MEDIUM_TERM_NOTES = 'MTN'
    ENUM_OVERNIGHT = 'ONITE'
    ENUM_PROMISSORY_NOTE = 'PN'
    ENUM_PLAZOS_FIJOS = 'PZFJ'
    ENUM_SHORT_TERM_LOAN_NOTE = 'STN'
    ENUM_TIME_DEPOSIT = 'TD'
    ENUM_EXTENDED_COMM_NOTE = 'XCN'
    ENUM_YANKEE_CERTIFICATE_OF_DEPOSIT = 'YCD'
    ENUM_ASSET_BACKED_SECURITIES = 'ABS'
    ENUM_CORP = 'CMBS'
    ENUM_COLLATERALIZED_MORTGAGE_OBLIGATION = 'CMO'
    ENUM_IOETTE_MORTGAGE = 'IET'
    ENUM_MORTGAGE_BACKED_SECURITIES = 'MBS'
    ENUM_MORTGAGE_INTEREST_ONLY = 'MIO'
    ENUM_MORTGAGE_PRINCIPAL_ONLY = 'MPO'
    ENUM_MORTGAGE_PRIVATE_PLACEMENT = 'MPP'
    ENUM_MISCELLANEOUS_PASS_THROUGH = 'MPT'
    ENUM_PFANDBRIEFE = 'PFAND'
    ENUM_TO_BE_ANNOUNCED = 'TBA'
    ENUM_OTHER_ANTICIPATION_NOTES = 'AN'
    ENUM_CERTIFICATE_OF_OBLIGATION = 'COFO'
    ENUM_CERTIFICATE_OF_PARTICIPATION = 'COFP'
    ENUM_GENERAL_OBLIGATION_BONDS = 'GO'
    ENUM_MANDATORY_TENDER = 'MT'
    ENUM_REVENUE_ANTICIPATION_NOTE = 'RAN'
    ENUM_REVENUE_BONDS = 'REV'
    ENUM_SPECIAL_ASSESSMENT = 'SPCLA'
    ENUM_SPECIAL_OBLIGATION = 'SPCLO'
    ENUM_SPECIAL_TAX = 'SPCLT'
    ENUM_TAX_ANTICIPATION_NOTE = 'TAN'
    ENUM_TAX_ALLOCATION = 'TAXA'
    ENUM_TAX_EXEMPT_COMMERCIAL_PAPER = 'TECP'
    ENUM_TAX_REVENUE_ANTICIPATION_NOTE = 'TRAN'
    ENUM_VARIABLE_RATE_DEMAND_NOTE = 'VRDN'
    ENUM_WARRANT = 'WAR'
    ENUM_MUTUAL_FUND = 'MF'
    ENUM_MULTILEG_INSTRUMENT = 'MLEG'
    ENUM_NO_SECURITY_TYPE = 'NONE'
    ENUM_FUTURE = 'FUT'
    ENUM_OPTION = 'OPT'

class EffectiveTime (field_types.UTCTimestamp_Type) :
    _tag = '168'

class StandInstDbType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '169'
    ENUM_OTHER = 0
    ENUM_DTCSID = 1
    ENUM_THOMSON_ALERT = 2
    ENUM_A_GLOBAL_CUSTODIAN = 3
    ENUM_ACCOUNT_NET = 4

class StandInstDbName (field_types.String_Type) :
    _tag = '170'

class StandInstDbID (field_types.String_Type) :
    _tag = '171'

class SettlDeliveryType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '172'
    ENUM_VERSUS = 0
    ENUM_FREE = 1
    ENUM_TRI_PARTY = 2
    ENUM_HOLD_IN_CUSTODY = 3

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

class SettlDate2 (field_types.LocalMktDate_Type) :
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

class OptAttribute (field_types.char_Type) :
    _tag = '206'

class SecurityExchange (field_types.Exchange_Type) :
    _tag = '207'

class NotifyBrokerOfCredit (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '208'
    ENUM_DETAILS_SHOULD_BE_COMMUNICATED = 'Y'
    ENUM_DETAILS_SHOULD_NOT_BE_COMMUNICATED = 'N'

class AllocHandlInst (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '209'
    ENUM_MATCH = 1
    ENUM_FORWARD = 2
    ENUM_FORWARD_AND_MATCH = 3

class MaxShow (field_types.Qty_Type) :
    _tag = '210'

class PegOffsetValue (field_types.float_Type) :
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

class BenchmarkCurveCurrency (field_types.Currency_Type) :
    _tag = '220'

class BenchmarkCurveName (field_types.String_Type) :
    _tag = '221'

class BenchmarkCurvePoint (field_types.String_Type) :
    _tag = '222'

class CouponRate (field_types.Percentage_Type) :
    _tag = '223'

class CouponPaymentDate (field_types.LocalMktDate_Type) :
    _tag = '224'

class IssueDate (field_types.LocalMktDate_Type) :
    _tag = '225'

class RepurchaseTerm (field_types.int_Type) :
    _tag = '226'

class RepurchaseRate (field_types.Percentage_Type) :
    _tag = '227'

class Factor (field_types.float_Type) :
    _tag = '228'

class TradeOriginationDate (field_types.LocalMktDate_Type) :
    _tag = '229'

class ExDate (field_types.LocalMktDate_Type) :
    _tag = '230'

class ContractMultiplier (field_types.float_Type) :
    _tag = '231'

class NoStipulations (field_types.NumInGroup_Type) :
    _tag = '232'

class StipulationType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '233'
    ENUM_ALTERNATIVE_MINIMUM_TAX = 'AMT'
    ENUM_AUTO_REINVESTMENT = 'AUTOREINV'
    ENUM_BANK_QUALIFIED = 'BANKQUAL'
    ENUM_BARGAIN_CONDITIONS = 'BGNCON'
    ENUM_COUPON_RANGE = 'COUPON'
    ENUM_ISO_CURRENCY_CODE = 'CURRENCY'
    ENUM_CUSTOM_START = 'CUSTOMDATE'
    ENUM_GEOGRAPHICS = 'GEOG'
    ENUM_VALUATION_DISCOUNT = 'HAIRCUT'
    ENUM_INSURED = 'INSURED'
    ENUM_ISSUE_DATE = 'ISSUE'
    ENUM_ISSUER = 'ISSUER'
    ENUM_ISSUE_SIZE_RANGE = 'ISSUESIZE'
    ENUM_LOOKBACK_DAYS = 'LOOKBACK'
    ENUM_EXPLICIT_LOT_IDENTIFIER = 'LOT'
    ENUM_LOT_VARIANCE = 'LOTVAR'
    ENUM_MATURITY_YEAR_AND_MONTH = 'MAT'
    ENUM_MATURITY_RANGE = 'MATURITY'
    ENUM_MAXIMUM_SUBSTITUTIONS = 'MAXSUBS'
    ENUM_MINIMUM_QUANTITY = 'MINQTY'
    ENUM_MINIMUM_INCREMENT = 'MININCR'
    ENUM_MINIMUM_DENOMINATION = 'MINDNOM'
    ENUM_PAYMENT_FREQUENCY = 'PAYFREQ'
    ENUM_NUMBER_OF_PIECES = 'PIECES'
    ENUM_POOLS_MAXIMUM = 'PMAX'
    ENUM_POOLS_PER_MILLION = 'PPM'
    ENUM_POOLS_PER_LOT = 'PPL'
    ENUM_POOLS_PER_TRADE = 'PPT'
    ENUM_PRICE_RANGE = 'PRICE'
    ENUM_PRICING_FREQUENCY = 'PRICEFREQ'
    ENUM_PRODUCTION_YEAR = 'PROD'
    ENUM_CALL_PROTECTION = 'PROTECT'
    ENUM_PURPOSE = 'PURPOSE'
    ENUM_BENCHMARK_PRICE_SOURCE = 'PXSOURCE'
    ENUM_RATING_SOURCE_AND_RANGE = 'RATING'
    ENUM_TYPE_OF_REDEMPTION = 'REDEMPTION'
    ENUM_RESTRICTED = 'RESTRICTED'
    ENUM_MARKET_SECTOR = 'SECTOR'
    ENUM_SECURITY_TYPE_INCLUDED_OR_EXCLUDED = 'SECTYPE'
    ENUM_STRUCTURE = 'STRUCT'
    ENUM_SUBSTITUTIONS_FREQUENCY = 'SUBSFREQ'
    ENUM_SUBSTITUTIONS_LEFT = 'SUBSLEFT'
    ENUM_FREEFORM_TEXT = 'TEXT'
    ENUM_TRADE_VARIANCE = 'TRDVAR'
    ENUM_WEIGHTED_AVERAGE_COUPON = 'WAC'
    ENUM_WEIGHTED_AVERAGE_LIFE_COUPON = 'WAL'
    ENUM_WEIGHTED_AVERAGE_LOAN_AGE = 'WALA'
    ENUM_WEIGHTED_AVERAGE_MATURITY = 'WAM'
    ENUM_WHOLE_POOL = 'WHOLE'
    ENUM_YIELD_RANGE = 'YIELD'

class StipulationValue (field_types.String_Type) :
    _tag = '234'

class YieldType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '235'
    ENUM_AFTER_TAX_YIELD = 'AFTERTAX'
    ENUM_ANNUAL_YIELD = 'ANNUAL'
    ENUM_YIELD_AT_ISSUE = 'ATISSUE'
    ENUM_YIELD_TO_AVERAGE_MATURITY = 'AVGMATURITY'
    ENUM_BOOK_YIELD = 'BOOK'
    ENUM_YIELD_TO_NEXT_CALL = 'CALL'
    ENUM_YIELD_CHANGE_SINCE_CLOSE = 'CHANGE'
    ENUM_CLOSING_YIELD = 'CLOSE'
    ENUM_COMPOUND_YIELD = 'COMPOUND'
    ENUM_CURRENT_YIELD = 'CURRENT'
    ENUM_TRUE_GROSS_YIELD = 'GROSS'
    ENUM_GVNT_EQUIVALENT_YIELD = 'GOVTEQUIV'
    ENUM_YIELD_WITH_INFLATION_ASSUMPTION = 'INFLATION'
    ENUM_INVERSE_FLOATER_BOND_YIELD = 'INVERSEFLOATER'
    ENUM_MOST_RECENT_CLOSING_YIELD = 'LASTCLOSE'
    ENUM_CLOSING_YIELD_MOST_RECENT_MONTH = 'LASTMONTH'
    ENUM_CLOSING_YIELD_MOST_RECENT_QUARTER = 'LASTQUARTER'
    ENUM_CLOSING_YIELD_MOST_RECENT_YEAR = 'LASTYEAR'
    ENUM_YIELD_TO_LONGEST_AVERAGE_LIFE = 'LONGAVGLIFE'
    ENUM_MARK_TO_MARKET_YIELD = 'MARK'
    ENUM_YIELD_TO_MATURITY = 'MATURITY'
    ENUM_YIELD_TO_NEXT_REFUND = 'NEXTREFUND'
    ENUM_OPEN_AVERAGE_YIELD = 'OPENAVG'
    ENUM_YIELD_TO_NEXT_PUT = 'PUT'
    ENUM_PREVIOUS_CLOSE_YIELD = 'PREVCLOSE'
    ENUM_PROCEEDS_YIELD = 'PROCEEDS'
    ENUM_SEMI_ANNUAL_YIELD = 'SEMIANNUAL'
    ENUM_YIELD_TO_SHORTEST_AVERAGE_LIFE = 'SHORTAVGLIFE'
    ENUM_SIMPLE_YIELD = 'SIMPLE'
    ENUM_TAX_EQUIVALENT_YIELD = 'TAXEQUIV'
    ENUM_YIELD_TO_TENDER_DATE = 'TENDER'
    ENUM_TRUE_YIELD = 'TRUE'
    ENUM_YIELD_VALUE_OF132 = 'VALUE1/32'
    ENUM_YIELD_TO_WORST = 'WORST'

class Yield (field_types.Percentage_Type) :
    _tag = '236'

class TotalTakedown (field_types.Amt_Type) :
    _tag = '237'

class Concession (field_types.Amt_Type) :
    _tag = '238'

class RepoCollateralSecurityType (field_types.String_Type) :
    _tag = '239'

class RedemptionDate (field_types.LocalMktDate_Type) :
    _tag = '240'

class UnderlyingCouponPaymentDate (field_types.LocalMktDate_Type) :
    _tag = '241'

class UnderlyingIssueDate (field_types.LocalMktDate_Type) :
    _tag = '242'

class UnderlyingRepoCollateralSecurityType (field_types.String_Type) :
    _tag = '243'

class UnderlyingRepurchaseTerm (field_types.int_Type) :
    _tag = '244'

class UnderlyingRepurchaseRate (field_types.Percentage_Type) :
    _tag = '245'

class UnderlyingFactor (field_types.float_Type) :
    _tag = '246'

class UnderlyingRedemptionDate (field_types.LocalMktDate_Type) :
    _tag = '247'

class LegCouponPaymentDate (field_types.LocalMktDate_Type) :
    _tag = '248'

class LegIssueDate (field_types.LocalMktDate_Type) :
    _tag = '249'

class LegRepoCollateralSecurityType (field_types.String_Type) :
    _tag = '250'

class LegRepurchaseTerm (field_types.int_Type) :
    _tag = '251'

class LegRepurchaseRate (field_types.Percentage_Type) :
    _tag = '252'

class LegFactor (field_types.float_Type) :
    _tag = '253'

class LegRedemptionDate (field_types.LocalMktDate_Type) :
    _tag = '254'

class CreditRating (field_types.String_Type) :
    _tag = '255'

class UnderlyingCreditRating (field_types.String_Type) :
    _tag = '256'

class LegCreditRating (field_types.String_Type) :
    _tag = '257'

class TradedFlatSwitch (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '258'
    ENUM_TRADED_FLAT = 'Y'
    ENUM_NOT_TRADED_FLAT = 'N'

class BasisFeatureDate (field_types.LocalMktDate_Type) :
    _tag = '259'

class BasisFeaturePrice (field_types.Price_Type) :
    _tag = '260'

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
    ENUM_BOOK_ENTRIES_TO_BE_AGGREGATED = 'Y'
    ENUM_BOOK_ENTRIES_SHOULD_NOT_BE_AGGREGATED = 'N'

class NoMDEntryTypes (field_types.NumInGroup_Type) :
    _tag = '267'

class NoMDEntries (field_types.NumInGroup_Type) :
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
    ENUM_IMBALANCE = 'A'
    ENUM_TRADE_VOLUME = 'B'
    ENUM_OPEN_INTEREST = 'C'

class MDEntryPx (field_types.Price_Type) :
    _tag = '270'

class MDEntrySize (field_types.Qty_Type) :
    _tag = '271'

class MDEntryDate (field_types.UTCDateOnly_Type) :
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
    ENUM_IMBALANCE_MORE_BUYERS = 'P'
    ENUM_IMBALANCE_MORE_SELLERS = 'Q'
    ENUM_OPENING_PRICE = 'R'

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
    ENUM_UNSUPPORTED_TRADING_SESSION_ID = '9'
    ENUM_UNSUPPORTED_SCOPE = 'A'
    ENUM_UNSUPPORTED_OPEN_CLOSE_SETTLE_FLAG = 'B'
    ENUM_UNSUPPORTED_MD_IMPLICIT_DELETE = 'C'

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

class OpenCloseSettlFlag (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '286'
    ENUM_DAILY_OPEN = '0'
    ENUM_SESSION_OPEN = '1'
    ENUM_DELIVERY_SETTLEMENT_ENTRY = '2'
    ENUM_EXPECTED_ENTRY = '3'
    ENUM_ENTRY_FROM_PREVIOUS_BUSINESS_DAY = '4'
    ENUM_THEORETICAL_PRICE_VALUE = '5'

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
    ENUM_EX_DIVIDEND = 'A'
    ENUM_EX_DISTRIBUTION = 'B'
    ENUM_EX_RIGHTS = 'C'
    ENUM_NEW = 'D'
    ENUM_EX_INTEREST = 'E'

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
    ENUM_ACCEPTED = 0
    ENUM_CANCEL_FOR_SYMBOL = 1
    ENUM_CANCELED_FOR_SECURITY_TYPE = 2
    ENUM_CANCELED_FOR_UNDERLYING = 3
    ENUM_CANCELED_ALL = 4
    ENUM_REJECTED = 5
    ENUM_REMOVED_FROM_MARKET = 6
    ENUM_EXPIRED = 7
    ENUM_QUERY = 8
    ENUM_QUOTE_NOT_FOUND = 9
    ENUM_PENDING = 10
    ENUM_PASS = 11
    ENUM_LOCKED_MARKET_WARNING = 12
    ENUM_CROSS_MARKET_WARNING = 13
    ENUM_CANCELED_DUE_TO_LOCK_MARKET = 14
    ENUM_CANCELED_DUE_TO_CROSS_MARKET = 15

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
    ENUM_OTHER = 99

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

class TotNoQuoteEntries (field_types.int_Type) :
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

class UnderlyingCurrency (field_types.Currency_Type) :
    _tag = '318'

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
    ENUM_REJECT_SECURITY_PROPOSAL = 5
    ENUM_CANNOT_MATCH_SELECTION_CRITERIA = 6

class SecurityStatusReqID (field_types.String_Type) :
    _tag = '324'

class UnsolicitedIndicator (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '325'
    ENUM_MESSAGE_IS_BEING_SENT_UNSOLICITED = 'Y'
    ENUM_MESSAGE_IS_BEING_SENT_AS_A_RESULT_OF_A_PRIOR_REQUEST = 'N'

class SecurityTradingStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '326'
    ENUM_OPENING_DELAY = 1
    ENUM_TRADING_HALT = 2
    ENUM_RESUME = 3
    ENUM_NO_OPEN = 4
    ENUM_PRICE_INDICATION = 5
    ENUM_TRADING_RANGE_INDICATION = 6
    ENUM_MARKET_IMBALANCE_BUY = 7
    ENUM_MARKET_IMBALANCE_SELL = 8
    ENUM_MARKET_ON_CLOSE_IMBALANCE_BUY = 9
    ENUM_MARKET_ON_CLOSE_IMBALANCE_SELL = 10
    ENUM_NO_MARKET_IMBALANCE = 12
    ENUM_NO_MARKET_ON_CLOSE_IMBALANCE = 13
    ENUM_ITS_PRE_OPENING = 14
    ENUM_NEW_PRICE_INDICATION = 15
    ENUM_TRADE_DISSEMINATION_TIME = 16
    ENUM_READY_TO_TRADE = 17
    ENUM_NOT_AVAILABLE_FOR_TRADING = 18
    ENUM_NOT_TRADED_ON_THIS_MARKET = 19
    ENUM_UNKNOWN_OR_INVALID = 20
    ENUM_PRE_OPEN = 21
    ENUM_OPENING_ROTATION = 22
    ENUM_FAST_MARKET = 23

class HaltReason (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '327'
    ENUM_ORDER_IMBALANCE = 'I'
    ENUM_EQUIPMENT_CHANGEOVER = 'X'
    ENUM_NEWS_PENDING = 'P'
    ENUM_NEWS_DISSEMINATION = 'D'
    ENUM_ORDER_INFLUX = 'E'
    ENUM_ADDITIONAL_INFORMATION = 'M'

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
    ENUM_UNKNOWN = 0
    ENUM_HALTED = 1
    ENUM_OPEN = 2
    ENUM_CLOSED = 3
    ENUM_PRE_OPEN = 4
    ENUM_PRE_CLOSE = 5
    ENUM_REQUEST_REJECTED = 6

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
    ENUM_ISO2022_JP = 'ISO-2022-JP'
    ENUM_EUCJP = 'EUC-JP'
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

class QuoteEntryRejectReason (field_types.int_Type) :
    _tag = '368'

class LastMsgSeqNumProcessed (field_types.SeqNum_Type) :
    _tag = '369'

class RefTagID (field_types.int_Type) :
    _tag = '371'

class RefMsgType (field_types.String_Type) :
    _tag = '372'

class SessionRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '373'
    ENUM_INVALID_TAG_NUMBER = 0
    ENUM_REQUIRED_TAG_MISSING = 1
    ENUM_TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE = 2
    ENUM_UNDEFINED_TAG = 3
    ENUM_TAG_SPECIFIED_WITHOUT_A_VALUE = 4
    ENUM_VALUE_IS_INCORRECT = 5
    ENUM_INCORRECT_DATA_FORMAT_FOR_VALUE = 6
    ENUM_DECRYPTION_PROBLEM = 7
    ENUM_SIGNATURE_PROBLEM = 8
    ENUM_COMP_ID_PROBLEM = 9
    ENUM_SENDING_TIME_ACCURACY_PROBLEM = 10
    ENUM_INVALID_MSG_TYPE = 11
    ENUM_XML_VALIDATION_ERROR = 12
    ENUM_TAG_APPEARS_MORE_THAN_ONCE = 13
    ENUM_TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER = 14
    ENUM_REPEATING_GROUP_FIELDS_OUT_OF_ORDER = 15
    ENUM_INCORRECT_NUM_IN_GROUP_COUNT_FOR_REPEATING_GROUP = 16
    ENUM_NON = 17
    ENUM_OTHER = 99

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
    ENUM_WAS_SOLICITED = 'Y'
    ENUM_WAS_NOT_SOLICITED = 'N'

class ExecRestatementReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '378'
    ENUM_GT_CORPORATE_ACTION = 0
    ENUM_GT_RENEWAL = 1
    ENUM_VERBAL_CHANGE = 2
    ENUM_REPRICING_OF_ORDER = 3
    ENUM_BROKER_OPTION = 4
    ENUM_PARTIAL_DECLINE_OF_ORDER_QTY = 5
    ENUM_CANCEL_ON_TRADING_HALT = 6
    ENUM_CANCEL_ON_SYSTEM_FAILURE = 7
    ENUM_MARKET = 8
    ENUM_CANCELED = 9
    ENUM_WAREHOUSE_RECAP = 10
    ENUM_OTHER = 99

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
    ENUM_NOT_AUTHORIZED = 6
    ENUM_DELIVER_TO_FIRM_NOT_AVAILABLE_AT_THIS_TIME = 7

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
    ENUM_RELATED_TO_VWAP = '6'

class DiscretionOffsetValue (field_types.float_Type) :
    _tag = '389'

class BidID (field_types.String_Type) :
    _tag = '390'

class ClientBidID (field_types.String_Type) :
    _tag = '391'

class ListName (field_types.String_Type) :
    _tag = '392'

class TotNoRelatedSym (field_types.int_Type) :
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
    ENUM_SECTOR = 1
    ENUM_COUNTRY = 2
    ENUM_INDEX = 3

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
    ENUM_FIVE_DAY_MOVING_AVERAGE = 1
    ENUM_TWENTY_DAY_MOVING_AVERAGE = 2
    ENUM_NORMAL_MARKET_SIZE = 3
    ENUM_OTHER = 4

class WtAverageLiquidity (field_types.Percentage_Type) :
    _tag = '410'

class ExchangeForPhysical (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '411'
    ENUM_TRUE = 'Y'
    ENUM_FALSE = 'N'

class OutMainCntryUIndex (field_types.Amt_Type) :
    _tag = '412'

class CrossPercent (field_types.Percentage_Type) :
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

class BidTradeType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '418'
    ENUM_RISK_TRADE = 'R'
    ENUM_VWAP_GUARANTEE = 'G'
    ENUM_AGENCY = 'A'
    ENUM_GUARANTEED_CLOSE = 'J'

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

class NoBidComponents (field_types.NumInGroup_Type) :
    _tag = '420'

class Country (field_types.Country_Type) :
    _tag = '421'

class TotNoStrikes (field_types.int_Type) :
    _tag = '422'

class PriceType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '423'
    ENUM_PERCENTAGE = 1
    ENUM_PER_UNIT = 2
    ENUM_FIXED_AMOUNT = 3
    ENUM_DISCOUNT = 4
    ENUM_PREMIUM = 5
    ENUM_SPREAD = 6
    ENUM_TED_PRICE = 7
    ENUM_TED_YIELD = 8
    ENUM_YIELD = 9
    ENUM_FIXED_CABINET_TRADE_PRICE = 10
    ENUM_VARIABLE_CABINET_TRADE_PRICE = 11

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

class NoStrikes (field_types.NumInGroup_Type) :
    _tag = '428'

class ListStatusType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '429'
    ENUM_ACK = 1
    ENUM_RESPONSE = 2
    ENUM_TIMED = 3
    ENUM_EXEC_STARTED = 4
    ENUM_ALL_DONE = 5
    ENUM_ALERT = 6

class NetGrossInd (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '430'
    ENUM_NET = 1
    ENUM_GROSS = 2

class ListOrderStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '431'
    ENUM_IN_BIDDING_PROCESS = 1
    ENUM_RECEIVED_FOR_EXECUTION = 2
    ENUM_EXECUTING = 3
    ENUM_CANCELLING = 4
    ENUM_ALERT = 5
    ENUM_ALL_DONE = 6
    ENUM_REJECT = 7

class ExpireDate (field_types.LocalMktDate_Type) :
    _tag = '432'

class ListExecInstType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '433'
    ENUM_IMMEDIATE = '1'
    ENUM_WAIT_FOR_INSTRUCTION = '2'
    ENUM_SELL_DRIVEN = '3'
    ENUM_BUY_DRIVEN_CASH_TOP_UP = '4'
    ENUM_BUY_DRIVEN_CASH_WITHDRAW = '5'

class CxlRejResponseTo (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '434'
    ENUM_ORDER_CANCEL_REQUEST = '1'
    ENUM_ORDER_CANCEL = '2'

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
    ENUM_BIC = 'B'
    ENUM_GENERAL_IDENTIFIER = 'C'
    ENUM_PROPRIETARY = 'D'
    ENUM_ISO_COUNTRY_CODE = 'E'
    ENUM_SETTLEMENT_ENTITY_LOCATION = 'F'
    ENUM_MIC = 'G'
    ENUM_CSD_PARTICIPANT = 'H'
    ENUM_KOREAN_INVESTOR_ID = '1'
    ENUM_TAIWANESE_FOREIGN_INVESTOR_ID = '2'
    ENUM_TAIWANESE_TRADING_ACCT = '3'
    ENUM_MALAYSIAN_CENTRAL_DEPOSITORY = '4'
    ENUM_CHINESE_INVESTOR_ID = '5'
    ENUM_UK_NATIONAL_INSURANCE_OR_PENSION_NUMBER = '6'
    ENUM_US_SOCIAL_SECURITY_NUMBER = '7'
    ENUM_US_EMPLOYER_OR_TAX_ID_NUMBER = '8'
    ENUM_AUSTRALIAN_BUSINESS_NUMBER = '9'
    ENUM_AUSTRALIAN_TAX_FILE_NUMBER = 'A'
    ENUM_ISITC_ACRONYM = 'I'

class PartyID (field_types.String_Type) :
    _tag = '448'

class NetChgPrevDay (field_types.PriceOffset_Type) :
    _tag = '451'

class PartyRole (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '452'
    ENUM_EXECUTING_FIRM = 1
    ENUM_BROKER_OF_CREDIT = 2
    ENUM_CLIENT_ID = 3
    ENUM_CLEARING_FIRM = 4
    ENUM_INVESTOR_ID = 5
    ENUM_INTRODUCING_FIRM = 6
    ENUM_ENTERING_FIRM = 7
    ENUM_LOCATE = 8
    ENUM_FUND_MANAGER_CLIENT_ID = 9
    ENUM_SETTLEMENT_LOCATION = 10
    ENUM_ORDER_ORIGINATION_TRADER = 11
    ENUM_EXECUTING_TRADER = 12
    ENUM_ORDER_ORIGINATION_FIRM = 13
    ENUM_GIVEUP_CLEARING_FIRM = 14
    ENUM_CORRESPONDANT_CLEARING_FIRM = 15
    ENUM_EXECUTING_SYSTEM = 16
    ENUM_CONTRA_FIRM = 17
    ENUM_CONTRA_CLEARING_FIRM = 18
    ENUM_SPONSORING_FIRM = 19
    ENUM_UNDERLYING_CONTRA_FIRM = 20
    ENUM_CLEARING_ORGANIZATION = 21
    ENUM_EXCHANGE = 22
    ENUM_CUSTOMER_ACCOUNT = 24
    ENUM_CORRESPONDENT_CLEARING_ORGANIZATION = 25
    ENUM_CORRESPONDENT_BROKER = 26
    ENUM_BUYER = 27
    ENUM_CUSTODIAN = 28
    ENUM_INTERMEDIARY = 29
    ENUM_AGENT = 30
    ENUM_SUB_CUSTODIAN = 31
    ENUM_BENEFICIARY = 32
    ENUM_INTERESTED_PARTY = 33
    ENUM_REGULATORY_BODY = 34
    ENUM_LIQUIDITY_PROVIDER = 35
    ENUM_ENTERING_TRADER = 36
    ENUM_CONTRA_TRADER = 37
    ENUM_POSITION_ACCOUNT = 38

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
    ENUM_AGENCY = 1
    ENUM_COMMODITY = 2
    ENUM_CORPORATE = 3
    ENUM_CURRENCY = 4
    ENUM_EQUITY = 5
    ENUM_GOVERNMENT = 6
    ENUM_INDEX = 7
    ENUM_LOAN = 8
    ENUM_MONEYMARKET = 9
    ENUM_MORTGAGE = 10
    ENUM_MUNICIPAL = 11
    ENUM_OTHER = 12
    ENUM_FINANCING = 13

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

class DistribPaymentMethod (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '477'
    ENUM_CREST = 1
    ENUM_NSCC = 2
    ENUM_EUROCLEAR = 3
    ENUM_CLEARSTREAM = 4
    ENUM_CHEQUE = 5
    ENUM_TELEGRAPHIC_TRANSFER = 6
    ENUM_FED_WIRE = 7
    ENUM_DIRECT_CREDIT = 8
    ENUM_ACH_CREDIT = 9
    ENUM_BPAY = 10
    ENUM_HIGH_VALUE_CLEARING_SYSTEM_HVACS = 11
    ENUM_REINVEST_IN_FUND = 12

class CashDistribCurr (field_types.Currency_Type) :
    _tag = '478'

class CommCurrency (field_types.Currency_Type) :
    _tag = '479'

class CancellationRights (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '480'
    ENUM_YES = 'Y'
    ENUM_NO_EXECUTION_ONLY = 'N'
    ENUM_NO_WAIVER_AGREEMENT = 'M'
    ENUM_NO_INSTITUTIONAL = 'O'

class MoneyLaunderingStatus (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '481'
    ENUM_PASSED = 'Y'
    ENUM_NOT_CHECKED = 'N'
    ENUM_EXEMPT_BELOW_LIMIT = '1'
    ENUM_EXEMPT_MONEY_TYPE = '2'
    ENUM_EXEMPT_AUTHORISED = '3'

class MailingInst (field_types.String_Type) :
    _tag = '482'

class TransBkdTime (field_types.UTCTimestamp_Type) :
    _tag = '483'

class ExecPriceType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '484'
    ENUM_BID_PRICE = 'B'
    ENUM_CREATION_PRICE = 'C'
    ENUM_CREATION_PRICE_PLUS_ADJUSTMENT_PERCENT = 'D'
    ENUM_CREATION_PRICE_PLUS_ADJUSTMENT_AMOUNT = 'E'
    ENUM_OFFER_PRICE = 'O'
    ENUM_OFFER_PRICE_MINUS_ADJUSTMENT_PERCENT = 'P'
    ENUM_OFFER_PRICE_MINUS_ADJUSTMENT_AMOUNT = 'Q'
    ENUM_SINGLE_PRICE = 'S'

class ExecPriceAdjustment (field_types.float_Type) :
    _tag = '485'

class DateOfBirth (field_types.LocalMktDate_Type) :
    _tag = '486'

class TradeReportTransType (field_types.int_Type) :
    _tag = '487'

class CardHolderName (field_types.String_Type) :
    _tag = '488'

class CardNumber (field_types.String_Type) :
    _tag = '489'

class CardExpDate (field_types.LocalMktDate_Type) :
    _tag = '490'

class CardIssNum (field_types.String_Type) :
    _tag = '491'

class PaymentMethod (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '492'
    ENUM_CREST = 1
    ENUM_NSCC = 2
    ENUM_EUROCLEAR = 3
    ENUM_CLEARSTREAM = 4
    ENUM_CHEQUE = 5
    ENUM_TELEGRAPHIC_TRANSFER = 6
    ENUM_FED_WIRE = 7
    ENUM_DEBIT_CARD = 8
    ENUM_DIRECT_DEBIT = 9
    ENUM_DIRECT_CREDIT = 10
    ENUM_CREDIT_CARD = 11
    ENUM_ACH_DEBIT = 12
    ENUM_ACH_CREDIT = 13
    ENUM_BPAY = 14
    ENUM_HIGH_VALUE_CLEARING_SYSTEM = 15

class RegistAcctType (field_types.String_Type) :
    _tag = '493'

class Designation (field_types.String_Type) :
    _tag = '494'

class TaxAdvantageType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '495'
    ENUM_NONE = 0
    ENUM_MAXI_ISA = 1
    ENUM_TESSA = 2
    ENUM_MINI_CASH_ISA = 3
    ENUM_MINI_STOCKS_AND_SHARES_ISA = 4
    ENUM_MINI_INSURANCE_ISA = 5
    ENUM_CURRENT_YEAR_PAYMENT = 6
    ENUM_PRIOR_YEAR_PAYMENT = 7
    ENUM_ASSET_TRANSFER = 8
    ENUM_EMPLOYEE_PRIOR_YEAR = 9
    ENUM_EMPLOYEE_CURRENT_YEAR = 10
    ENUM_EMPLOYER_PRIOR_YEAR = 11
    ENUM_EMPLOYER_CURRENT_YEAR = 12
    ENUM_NON_FUND_PROTOTYPE_IRA = 13
    ENUM_NON_FUND_QUALIFIED_PLAN = 14
    ENUM_DEFINED_CONTRIBUTION_PLAN = 15
    ENUM_IRA = 16
    ENUM_IRA_ROLLOVER = 17
    ENUM_KEOGH = 18
    ENUM_PROFIT_SHARING_PLAN = 19
    ENUM_US401_K = 20
    ENUM_SELF_DIRECTED_IRA = 21
    ENUM_US403B = 22
    ENUM_US457 = 23
    ENUM_ROTH_IRA_PROTOTYPE = 24
    ENUM_ROTH_IRA_NON_PROTOTYPE = 25
    ENUM_ROTH_CONVERSION_IRA_PROTOTYPE = 26
    ENUM_ROTH_CONVERSION_IRA_NON_PROTOTYPE = 27
    ENUM_EDUCATION_IRA_PROTOTYPE = 28
    ENUM_EDUCATION_IRA_NON_PROTOTYPE = 29

class RegistRejReasonText (field_types.String_Type) :
    _tag = '496'

class FundRenewWaiv (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '497'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class CashDistribAgentName (field_types.String_Type) :
    _tag = '498'

class CashDistribAgentCode (field_types.String_Type) :
    _tag = '499'

class CashDistribAgentAcctNumber (field_types.String_Type) :
    _tag = '500'

class CashDistribPayRef (field_types.String_Type) :
    _tag = '501'

class CashDistribAgentAcctName (field_types.String_Type) :
    _tag = '502'

class CardStartDate (field_types.LocalMktDate_Type) :
    _tag = '503'

class PaymentDate (field_types.LocalMktDate_Type) :
    _tag = '504'

class PaymentRemitterID (field_types.String_Type) :
    _tag = '505'

class RegistStatus (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '506'
    ENUM_ACCEPTED = 'A'
    ENUM_REJECTED = 'R'
    ENUM_HELD = 'H'
    ENUM_REMINDER = 'N'

class RegistRejReasonCode (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '507'
    ENUM_INVALID_ACCOUNT_TYPE = 1
    ENUM_INVALID_TAX_EXEMPT_TYPE = 2
    ENUM_INVALID_OWNERSHIP_TYPE = 3
    ENUM_NO_REG_DETAILS = 4
    ENUM_INVALID_REG_SEQ_NO = 5
    ENUM_INVALID_REG_DETAILS = 6
    ENUM_INVALID_MAILING_DETAILS = 7
    ENUM_INVALID_MAILING_INSTRUCTIONS = 8
    ENUM_INVALID_INVESTOR_ID = 9
    ENUM_INVALID_INVESTOR_ID_SOURCE = 10
    ENUM_INVALID_DATE_OF_BIRTH = 11
    ENUM_INVALID_COUNTRY = 12
    ENUM_INVALID_DISTRIB_INSTNS = 13
    ENUM_INVALID_PERCENTAGE = 14
    ENUM_INVALID_PAYMENT_METHOD = 15
    ENUM_INVALID_ACCOUNT_NAME = 16
    ENUM_INVALID_AGENT_CODE = 17
    ENUM_INVALID_ACCOUNT_NUM = 18
    ENUM_OTHER = 99

class RegistRefID (field_types.String_Type) :
    _tag = '508'

class RegistDtls (field_types.String_Type) :
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
    ENUM_NEW = '0'
    ENUM_REPLACE = '1'
    ENUM_CANCEL = '2'

class ExecValuationPoint (field_types.UTCTimestamp_Type) :
    _tag = '515'

class OrderPercent (field_types.Percentage_Type) :
    _tag = '516'

class OwnershipType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '517'
    ENUM_JOINT_INVESTORS = 'J'
    ENUM_TENANTS_IN_COMMON = 'T'
    ENUM_JOINT_TRUSTEES = '2'

class NoContAmts (field_types.NumInGroup_Type) :
    _tag = '518'

class ContAmtType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '519'
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
    ENUM_FUND_BASED_RENEWAL_COMMISSION_ON_ORDER = 13
    ENUM_FUND_BASED_RENEWAL_COMMISSION_ON_FUND = 14
    ENUM_NET_SETTLEMENT_AMOUNT = 15

class ContAmtValue (field_types.float_Type) :
    _tag = '520'

class ContAmtCurr (field_types.Currency_Type) :
    _tag = '521'

class OwnerType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '522'
    ENUM_INDIVIDUAL_INVESTOR = 1
    ENUM_PUBLIC_COMPANY = 2
    ENUM_PRIVATE_COMPANY = 3
    ENUM_INDIVIDUAL_TRUSTEE = 4
    ENUM_COMPANY_TRUSTEE = 5
    ENUM_PENSION_PLAN = 6
    ENUM_CUSTODIAN_UNDER_GIFTS_TO_MINORS_ACT = 7
    ENUM_TRUSTS = 8
    ENUM_FIDUCIARIES = 9
    ENUM_NETWORKING_SUB_ACCOUNT = 10
    ENUM_NON_PROFIT_ORGANIZATION = 11
    ENUM_CORPORATE_BODY = 12
    ENUM_NOMINEE = 13

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
    ENUM_AGENCY = 'A'
    ENUM_PROPRIETARY = 'G'
    ENUM_INDIVIDUAL = 'I'
    ENUM_PRINCIPAL = 'P'
    ENUM_RISKLESS_PRINCIPAL = 'R'
    ENUM_AGENT_FOR_OTHER_MEMBER = 'W'

class OrderRestrictions (field_types.MultipleValueString_Type, field_types.MultipleValueString_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '529'
    ENUM_PROGRAM_TRADE = '1'
    ENUM_INDEX_ARBITRAGE = '2'
    ENUM_NON_INDEX_ARBITRAGE = '3'
    ENUM_COMPETING_MARKET_MAKER = '4'
    ENUM_ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_SECURITY = '5'
    ENUM_ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_UNDERLYING = '6'
    ENUM_FOREIGN_ENTITY = '7'
    ENUM_EXTERNAL_MARKET_PARTICIPANT = '8'
    ENUM_EXTERNAL_INTER_CONNECTED_MARKET_LINKAGE = '9'
    ENUM_RISKLESS_ARBITRAGE = 'A'

class MassCancelRequestType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '530'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY = '1'
    ENUM_CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    ENUM_CANCEL_ORDERS_FOR_A_PRODUCT = '3'
    ENUM_CANCEL_ORDERS_FOR_ACFI_CODE = '4'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY_TYPE = '5'
    ENUM_CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    ENUM_CANCEL_ALL_ORDERS = '7'

class MassCancelResponse (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '531'
    ENUM_CANCEL_REQUEST_REJECTED = '0'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY = '1'
    ENUM_CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    ENUM_CANCEL_ORDERS_FOR_A_PRODUCT = '3'
    ENUM_CANCEL_ORDERS_FOR_ACFI_CODE = '4'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY_TYPE = '5'
    ENUM_CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    ENUM_CANCEL_ALL_ORDERS = '7'

class MassCancelRejectReason (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '532'
    ENUM_MASS_CANCEL_NOT_SUPPORTED = '0'
    ENUM_INVALID_OR_UNKNOWN_SECURITY = '1'
    ENUM_INVALID_OR_UNKOWN_UNDERLYING_SECURITY = '2'
    ENUM_INVALID_OR_UNKNOWN_PRODUCT = '3'
    ENUM_INVALID_OR_UNKNOWN_CFI_CODE = '4'
    ENUM_INVALID_OR_UNKNOWN_SECURITY_TYPE = '5'
    ENUM_INVALID_OR_UNKNOWN_TRADING_SESSION = '6'
    ENUM_OTHER = '99'

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
    ENUM_COUNTER = 3

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
    ENUM_CASH = '1'
    ENUM_MARGIN_OPEN = '2'
    ENUM_MARGIN_CLOSE = '3'

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
    ENUM_NONE = 0
    ENUM_BUY_SIDE_IS_PRIORITIZED = 1
    ENUM_SELL_SIDE_IS_PRIORITIZED = 2

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

class TotNoSecurityTypes (field_types.int_Type) :
    _tag = '557'

class NoSecurityTypes (field_types.NumInGroup_Type) :
    _tag = '558'

class SecurityListRequestType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '559'
    ENUM_SYMBOL = 0
    ENUM_SECURITY_TYPE_AND = 1
    ENUM_PRODUCT = 2
    ENUM_TRADING_SESSION_ID = 3
    ENUM_ALL_SECURITIES = 4

class SecurityRequestResult (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '560'
    ENUM_VALID_REQUEST = 0
    ENUM_INVALID_OR_UNSUPPORTED_REQUEST = 1
    ENUM_NO_INSTRUMENTS_FOUND = 2
    ENUM_NOT_AUTHORIZED_TO_RETRIEVE_INSTRUMENT_DATA = 3
    ENUM_INSTRUMENT_DATA_TEMPORARILY_UNAVAILABLE = 4
    ENUM_REQUEST_FOR_INSTRUMENT_DATA_NOT_SUPPORTED = 5

class RoundLot (field_types.Qty_Type) :
    _tag = '561'

class MinTradeVol (field_types.Qty_Type) :
    _tag = '562'

class MultiLegRptTypeReq (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '563'
    ENUM_REPORT_BY_MULITLEG_SECURITY_ONLY = 0
    ENUM_REPORT_BY_MULTILEG_SECURITY_AND_INSTRUMENT_LEGS = 1
    ENUM_REPORT_BY_INSTRUMENT_LEGS_ONLY = 2

class LegPositionEffect (field_types.char_Type) :
    _tag = '564'

class LegCoveredOrUncovered (field_types.int_Type) :
    _tag = '565'

class LegPrice (field_types.Price_Type) :
    _tag = '566'

class TradSesStatusRejReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '567'
    ENUM_UNKNOWN_OR_INVALID_TRADING_SESSION_ID = 1
    ENUM_OTHER = 99

class TradeRequestID (field_types.String_Type) :
    _tag = '568'

class TradeRequestType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '569'
    ENUM_ALL_TRADES = 0
    ENUM_MATCHED_TRADES_MATCHING_CRITERIA = 1
    ENUM_UNMATCHED_TRADES_THAT_MATCH_CRITERIA = 2
    ENUM_UNREPORTED_TRADES_THAT_MATCH_CRITERIA = 3
    ENUM_ADVISORIES_THAT_MATCH_CRITERIA = 4

class PreviouslyReported (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '570'
    ENUM_PERVIOUSLY_REPORTED_TO_COUNTERPARTY = 'Y'
    ENUM_NOT_REPORTED_TO_COUNTERPARTY = 'N'

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
    ENUM_EXACT_MATCH_PLUS4_BADGES_EXEC_TIME = 'A1'
    ENUM_EXACT_MATCH_PLUS4_BADGES = 'A2'
    ENUM_EXACT_MATCH_PLUS2_BADGES_EXEC_TIME = 'A3'
    ENUM_EXACT_MATCH_PLUS2_BADGES = 'A4'
    ENUM_EXACT_MATCH_PLUS_EXEC_TIME = 'A5'
    ENUM_STAMPED_ADVISORIES_OR_SPECIALIST_ACCEPTS = 'AQ'
    ENUM_A1_EXACT_MATCH_SUMMARIZED_QUANTITY = 'S1'
    ENUM_A2_EXACT_MATCH_SUMMARIZED_QUANTITY = 'S2'
    ENUM_A3_EXACT_MATCH_SUMMARIZED_QUANTITY = 'S3'
    ENUM_A4_EXACT_MATCH_SUMMARIZED_QUANTITY = 'S4'
    ENUM_A5_EXACT_MATCH_SUMMARIZED_QUANTITY = 'S5'
    ENUM_EXACT_MATCH_MINUS_BADGES_TIMES = 'M1'
    ENUM_SUMMARIZED_MATCH_MINUS_BADGES_TIMES = 'M2'
    ENUM_OCS_LOCKED_IN = 'MT'
    ENUM_ACT_ACCEPTED_TRADE = 'M3'
    ENUM_ACT_DEFAULT_TRADE = 'M4'
    ENUM_ACT_DEFAULT_AFTER_M2 = 'M5'
    ENUM_ACTM6_MATCH = 'M6'

class OddLot (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '575'
    ENUM_TREAT_AS_ODD_LOT = 'Y'
    ENUM_TREAT_AS_ROUND_LOT = 'N'

class NoClearingInstructions (field_types.NumInGroup_Type) :
    _tag = '576'

class ClearingInstruction (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '577'
    ENUM_PROCESS_NORMALLY = 0
    ENUM_EXCLUDE_FROM_ALL_NETTING = 1
    ENUM_BILATERAL_NETTING_ONLY = 2
    ENUM_EX_CLEARING = 3
    ENUM_SPECIAL_TRADE = 4
    ENUM_MULTILATERAL_NETTING = 5
    ENUM_CLEAR_AGAINST_CENTRAL_COUNTERPARTY = 6
    ENUM_EXCLUDE_FROM_CENTRAL_COUNTERPARTY = 7
    ENUM_MANUAL_MODE = 8
    ENUM_AUTOMATIC_POSTING_MODE = 9
    ENUM_AUTOMATIC_GIVE_UP_MODE = 10
    ENUM_QUALIFIED_SERVICE_REPRESENTATIVE_QSR = 11
    ENUM_CUSTOMER_TRADE = 12
    ENUM_SELF_CLEARING = 13

class TradeInputSource (field_types.String_Type) :
    _tag = '578'

class TradeInputDevice (field_types.String_Type) :
    _tag = '579'

class NoDates (field_types.NumInGroup_Type) :
    _tag = '580'

class AccountType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '581'
    ENUM_CARRIED_CUSTOMER_SIDE = 1
    ENUM_CARRIED_NON_CUSTOMER_SIDE = 2
    ENUM_HOUSE_TRADER = 3
    ENUM_FLOOR_TRADER = 4
    ENUM_CARRIED_NON_CUSTOMER_SIDE_CROSS_MARGINED = 6
    ENUM_HOUSE_TRADER_CROSS_MARGINED = 7
    ENUM_JOINT_BACK_OFFICE_ACCOUNT = 8

class CustOrderCapacity (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '582'
    ENUM_MEMBER_TRADING_FOR_THEIR_OWN_ACCOUNT = 1
    ENUM_CLEARING_FIRM_TRADING_FOR_ITS_PROPRIETARY_ACCOUNT = 2
    ENUM_MEMBER_TRADING_FOR_ANOTHER_MEMBER = 3
    ENUM_ALL_OTHER = 4

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
    ENUM_STATUS_FOR_ALL_ORDERS = 7
    ENUM_STATUS_FOR_ORDERS_FOR_A_PARTY_ID = 8

class OrigOrdModTime (field_types.UTCTimestamp_Type) :
    _tag = '586'

class LegSettlType (field_types.char_Type) :
    _tag = '587'

class LegSettlDate (field_types.LocalMktDate_Type) :
    _tag = '588'

class DayBookingInst (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '589'
    ENUM_AUTO = '0'
    ENUM_SPEAK_WITH_ORDER_INITIATOR_BEFORE_BOOKING = '1'
    ENUM_ACCUMULATE = '2'

class BookingUnit (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '590'
    ENUM_EACH_PARTIAL_EXECUTION_IS_A_BOOKABLE_UNIT = '0'
    ENUM_AGGREGATE_PARTIAL_EXECUTIONS_ON_THIS_ORDER = '1'
    ENUM_AGGREGATE_EXECUTIONS_FOR_THIS_SYMBOL = '2'

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
    ENUM_CALCULATED = 1
    ENUM_PRELIMINARY = 2
    ENUM_READY_TO_BOOK = 5
    ENUM_WAREHOUSE_INSTRUCTION = 7
    ENUM_REQUEST_TO_INTERMEDIARY = 8

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
    ENUM_CBOE_MEMBER = 'B'
    ENUM_NON_MEMBER_AND_CUSTOMER = 'C'
    ENUM_EQUITY_MEMBER_AND_CLEARING_MEMBER = 'E'
    ENUM_FULL_AND_ASSOCIATE_MEMBER = 'F'
    ENUM_FIRMS106_H_AND106_J = 'H'
    ENUM_GIM = 'I'
    ENUM_LESSEE106_F_EMPLOYEES = 'L'
    ENUM_ALL_OTHER_OWNERSHIP_TYPES = 'M'
    ENUM_FIRST_YEAR_DELEGATE = '1'
    ENUM_SECOND_YEAR_DELEGATE = '2'
    ENUM_THIRD_YEAR_DELEGATE = '3'
    ENUM_FOURTH_YEAR_DELEGATE = '4'
    ENUM_FIFTH_YEAR_DELEGATE = '5'
    ENUM_SIXTH_YEAR_DELEGATE = '9'

class WorkingIndicator (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '636'
    ENUM_WORKING = 'Y'
    ENUM_NOT_WORKING = 'N'

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
    ENUM_NO_MATCH_FOR_INQUIRY = 7
    ENUM_NO_MARKET_FOR_INSTRUMENT = 8
    ENUM_NO_INVENTORY = 9
    ENUM_PASS = 10
    ENUM_OTHER = 99

class SideComplianceID (field_types.String_Type) :
    _tag = '659'

class AcctIDSource (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '660'
    ENUM_BIC = 1
    ENUM_SID_CODE = 2
    ENUM_TFM = 3
    ENUM_OMGEO = 4
    ENUM_DTCC_CODE = 5
    ENUM_OTHER = 99

class AllocAcctIDSource (field_types.int_Type) :
    _tag = '661'

class BenchmarkPrice (field_types.Price_Type) :
    _tag = '662'

class BenchmarkPriceType (field_types.int_Type) :
    _tag = '663'

class ConfirmID (field_types.String_Type) :
    _tag = '664'

class ConfirmStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '665'
    ENUM_RECEIVED = 1
    ENUM_MISMATCHED_ACCOUNT = 2
    ENUM_MISSING_SETTLEMENT_INSTRUCTIONS = 3
    ENUM_CONFIRMED = 4
    ENUM_REQUEST_REJECTED = 5

class ConfirmTransType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '666'
    ENUM_NEW = 0
    ENUM_REPLACE = 1
    ENUM_CANCEL = 2

class ContractSettlMonth (field_types.MonthYear_Type) :
    _tag = '667'

class DeliveryForm (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '668'
    ENUM_BOOK_ENTRY = 1
    ENUM_BEARER = 2

class LastParPx (field_types.Price_Type) :
    _tag = '669'

class NoLegAllocs (field_types.NumInGroup_Type) :
    _tag = '670'

class LegAllocAccount (field_types.String_Type) :
    _tag = '671'

class LegIndividualAllocID (field_types.String_Type) :
    _tag = '672'

class LegAllocQty (field_types.Qty_Type) :
    _tag = '673'

class LegAllocAcctIDSource (field_types.String_Type) :
    _tag = '674'

class LegSettlCurrency (field_types.Currency_Type) :
    _tag = '675'

class LegBenchmarkCurveCurrency (field_types.Currency_Type) :
    _tag = '676'

class LegBenchmarkCurveName (field_types.String_Type) :
    _tag = '677'

class LegBenchmarkCurvePoint (field_types.String_Type) :
    _tag = '678'

class LegBenchmarkPrice (field_types.Price_Type) :
    _tag = '679'

class LegBenchmarkPriceType (field_types.int_Type) :
    _tag = '680'

class LegBidPx (field_types.Price_Type) :
    _tag = '681'

class LegIOIQty (field_types.String_Type) :
    _tag = '682'

class NoLegStipulations (field_types.NumInGroup_Type) :
    _tag = '683'

class LegOfferPx (field_types.Price_Type) :
    _tag = '684'

class LegPriceType (field_types.int_Type) :
    _tag = '686'

class LegQty (field_types.Qty_Type) :
    _tag = '687'

class LegStipulationType (field_types.String_Type) :
    _tag = '688'

class LegStipulationValue (field_types.String_Type) :
    _tag = '689'

class LegSwapType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '690'
    ENUM_PAR_FOR_PAR = 1
    ENUM_MODIFIED_DURATION = 2
    ENUM_RISK = 4
    ENUM_PROCEEDS = 5

class Pool (field_types.String_Type) :
    _tag = '691'

class QuotePriceType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '692'
    ENUM_PERCENT = 1
    ENUM_PER_SHARE = 2
    ENUM_FIXED_AMOUNT = 3
    ENUM_DISCOUNT = 4
    ENUM_PREMIUM = 5
    ENUM_SPREAD = 6
    ENUM_TED_PRICE = 7
    ENUM_TED_YIELD = 8
    ENUM_YIELD_SPREAD = 9
    ENUM_YIELD = 10

class QuoteRespID (field_types.String_Type) :
    _tag = '693'

class QuoteRespType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '694'
    ENUM_HIT = 1
    ENUM_COUNTER = 2
    ENUM_EXPIRED = 3
    ENUM_COVER = 4
    ENUM_DONE_AWAY = 5
    ENUM_PASS = 6

class QuoteQualifier (field_types.char_Type) :
    _tag = '695'

class YieldRedemptionDate (field_types.LocalMktDate_Type) :
    _tag = '696'

class YieldRedemptionPrice (field_types.Price_Type) :
    _tag = '697'

class YieldRedemptionPriceType (field_types.int_Type) :
    _tag = '698'

class BenchmarkSecurityID (field_types.String_Type) :
    _tag = '699'

class ReversalIndicator (field_types.Boolean_Type) :
    _tag = '700'

class YieldCalcDate (field_types.LocalMktDate_Type) :
    _tag = '701'

class NoPositions (field_types.NumInGroup_Type) :
    _tag = '702'

class PosType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '703'
    ENUM_TRANSACTION_QUANTITY = 'TQ'
    ENUM_INTRA_SPREAD_QTY = 'IAS'
    ENUM_INTER_SPREAD_QTY = 'IES'
    ENUM_END_OF_DAY_QTY = 'FIN'
    ENUM_START_OF_DAY_QTY = 'SOD'
    ENUM_OPTION_EXERCISE_QTY = 'EX'
    ENUM_OPTION_ASSIGNMENT = 'AS'
    ENUM_TRANSACTION_FROM_EXERCISE = 'TX'
    ENUM_TRANSACTION_FROM_ASSIGNMENT = 'TA'
    ENUM_PIT_TRADE_QTY = 'PIT'
    ENUM_TRANSFER_TRADE_QTY = 'TRF'
    ENUM_ELECTRONIC_TRADE_QTY = 'ETR'
    ENUM_ALLOCATION_TRADE_QTY = 'ALC'
    ENUM_ADJUSTMENT_QTY = 'PA'
    ENUM_AS_OF_TRADE_QTY = 'ASF'
    ENUM_DELIVERY_QTY = 'DLV'
    ENUM_TOTAL_TRANSACTION_QTY = 'TOT'
    ENUM_CROSS_MARGIN_QTY = 'XM'
    ENUM_INTEGRAL_SPLIT = 'SPL'

class LongQty (field_types.Qty_Type) :
    _tag = '704'

class ShortQty (field_types.Qty_Type) :
    _tag = '705'

class PosQtyStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '706'
    ENUM_SUBMITTED = 0
    ENUM_ACCEPTED = 1
    ENUM_REJECTED = 2

class PosAmtType (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '707'
    ENUM_FINAL_MARK_TO_MARKET_AMOUNT = 'FMTM'
    ENUM_INCREMENTAL_MARK_TO_MARKET_AMOUNT = 'IMTM'
    ENUM_TRADE_VARIATION_AMOUNT = 'TVAR'
    ENUM_START_OF_DAY_MARK_TO_MARKET_AMOUNT = 'SMTM'
    ENUM_PREMIUM_AMOUNT = 'PREM'
    ENUM_CASH_RESIDUAL_AMOUNT = 'CRES'
    ENUM_CASH_AMOUNT = 'CASH'
    ENUM_VALUE_ADJUSTED_AMOUNT = 'VADJ'

class PosAmt (field_types.Amt_Type) :
    _tag = '708'

class PosTransType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '709'
    ENUM_EXERCISE = 1
    ENUM_DO_NOT_EXERCISE = 2
    ENUM_POSITION_ADJUSTMENT = 3
    ENUM_POSITION_CHANGE_SUBMISSION = 4
    ENUM_PLEDGE = 5

class PosReqID (field_types.String_Type) :
    _tag = '710'

class NoUnderlyings (field_types.NumInGroup_Type) :
    _tag = '711'

class PosMaintAction (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '712'
    ENUM_NEW = 1
    ENUM_REPLACE = 2
    ENUM_CANCEL = 3

class OrigPosReqRefID (field_types.String_Type) :
    _tag = '713'

class PosMaintRptRefID (field_types.String_Type) :
    _tag = '714'

class ClearingBusinessDate (field_types.LocalMktDate_Type) :
    _tag = '715'

class SettlSessID (field_types.String_Type, field_types.String_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '716'
    ENUM_INTRADAY = 'ITD'
    ENUM_REGULAR_TRADING_HOURS = 'RTH'
    ENUM_ELECTRONIC_TRADING_HOURS = 'ETH'

class SettlSessSubID (field_types.String_Type) :
    _tag = '717'

class AdjustmentType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '718'
    ENUM_PROCESS_REQUEST_AS_MARGIN_DISPOSITION = 0
    ENUM_DELTA_PLUS = 1
    ENUM_DELTA_MINUS = 2
    ENUM_FINAL = 3

class ContraryInstructionIndicator (field_types.Boolean_Type) :
    _tag = '719'

class PriorSpreadIndicator (field_types.Boolean_Type) :
    _tag = '720'

class PosMaintRptID (field_types.String_Type) :
    _tag = '721'

class PosMaintStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '722'
    ENUM_ACCEPTED = 0
    ENUM_ACCEPTED_WITH_WARNINGS = 1
    ENUM_REJECTED = 2
    ENUM_COMPLETED = 3
    ENUM_COMPLETED_WITH_WARNINGS = 4

class PosMaintResult (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '723'
    ENUM_SUCCESSFUL_COMPLETION = 0
    ENUM_REJECTED = 1
    ENUM_OTHER = 99

class PosReqType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '724'
    ENUM_POSITIONS = 0
    ENUM_TRADES = 1
    ENUM_EXERCISES = 2
    ENUM_ASSIGNMENTS = 3

class ResponseTransportType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '725'
    ENUM_INBAND = 0
    ENUM_OUT_OF_BAND = 1

class ResponseDestination (field_types.String_Type) :
    _tag = '726'

class TotalNumPosReports (field_types.int_Type) :
    _tag = '727'

class PosReqResult (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '728'
    ENUM_VALID_REQUEST = 0
    ENUM_INVALID_OR_UNSUPPORTED_REQUEST = 1
    ENUM_NO_POSITIONS_FOUND_THAT_MATCH_CRITERIA = 2
    ENUM_NOT_AUTHORIZED_TO_REQUEST_POSITIONS = 3
    ENUM_REQUEST_FOR_POSITION_NOT_SUPPORTED = 4
    ENUM_OTHER = 99

class PosReqStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '729'
    ENUM_COMPLETED = 0
    ENUM_COMPLETED_WITH_WARNINGS = 1
    ENUM_REJECTED = 2

class SettlPrice (field_types.Price_Type) :
    _tag = '730'

class SettlPriceType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '731'
    ENUM_FINAL = 1
    ENUM_THEORETICAL = 2

class UnderlyingSettlPrice (field_types.Price_Type) :
    _tag = '732'

class UnderlyingSettlPriceType (field_types.int_Type) :
    _tag = '733'

class PriorSettlPrice (field_types.Price_Type) :
    _tag = '734'

class NoQuoteQualifiers (field_types.NumInGroup_Type) :
    _tag = '735'

class AllocSettlCurrency (field_types.Currency_Type) :
    _tag = '736'

class AllocSettlCurrAmt (field_types.Amt_Type) :
    _tag = '737'

class InterestAtMaturity (field_types.Amt_Type) :
    _tag = '738'

class LegDatedDate (field_types.LocalMktDate_Type) :
    _tag = '739'

class LegPool (field_types.String_Type) :
    _tag = '740'

class AllocInterestAtMaturity (field_types.Amt_Type) :
    _tag = '741'

class AllocAccruedInterestAmt (field_types.Amt_Type) :
    _tag = '742'

class DeliveryDate (field_types.LocalMktDate_Type) :
    _tag = '743'

class AssignmentMethod (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '744'
    ENUM_RANDOM = 'R'
    ENUM_PRO_RATA = 'P'

class AssignmentUnit (field_types.Qty_Type) :
    _tag = '745'

class OpenInterest (field_types.Amt_Type) :
    _tag = '746'

class ExerciseMethod (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '747'
    ENUM_AUTOMATIC = 'A'
    ENUM_MANUAL = 'M'

class TotNumTradeReports (field_types.int_Type) :
    _tag = '748'

class TradeRequestResult (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '749'
    ENUM_SUCCESSFUL = 0
    ENUM_INVALID_OR_UNKNOWN_INSTRUMENT = 1
    ENUM_INVALID_TYPE_OF_TRADE_REQUESTED = 2
    ENUM_INVALID_PARTIES = 3
    ENUM_INVALID_TRANSPORT_TYPE_REQUESTED = 4
    ENUM_INVALID_DESTINATION_REQUESTED = 5
    ENUM_TRADE_REQUEST_TYPE_NOT_SUPPORTED = 8
    ENUM_NOT_AUTHORIZED = 9
    ENUM_OTHER = 99

class TradeRequestStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '750'
    ENUM_ACCEPTED = 0
    ENUM_COMPLETED = 1
    ENUM_REJECTED = 2

class TradeReportRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '751'
    ENUM_SUCCESSFUL = 0
    ENUM_INVALID_PARTY_ONFORMATION = 1
    ENUM_UNKNOWN_INSTRUMENT = 2
    ENUM_UNAUTHORIZED_TO_REPORT_TRADES = 3
    ENUM_INVALID_TRADE_TYPE = 4
    ENUM_OTHER = 99

class SideMultiLegReportingType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '752'
    ENUM_SINGLE_SECURITY = 1
    ENUM_INDIVIDUAL_LEG_OF_A_MULTILEG_SECURITY = 2
    ENUM_MULTILEG_SECURITY = 3

class NoPosAmt (field_types.NumInGroup_Type) :
    _tag = '753'

class AutoAcceptIndicator (field_types.Boolean_Type) :
    _tag = '754'

class AllocReportID (field_types.String_Type) :
    _tag = '755'

class NoNested2PartyIDs (field_types.NumInGroup_Type) :
    _tag = '756'

class Nested2PartyID (field_types.String_Type) :
    _tag = '757'

class Nested2PartyIDSource (field_types.char_Type) :
    _tag = '758'

class Nested2PartyRole (field_types.int_Type) :
    _tag = '759'

class Nested2PartySubID (field_types.String_Type) :
    _tag = '760'

class BenchmarkSecurityIDSource (field_types.String_Type) :
    _tag = '761'

class SecuritySubType (field_types.String_Type) :
    _tag = '762'

class UnderlyingSecuritySubType (field_types.String_Type) :
    _tag = '763'

class LegSecuritySubType (field_types.String_Type) :
    _tag = '764'

class AllowableOneSidednessPct (field_types.Percentage_Type) :
    _tag = '765'

class AllowableOneSidednessValue (field_types.Amt_Type) :
    _tag = '766'

class AllowableOneSidednessCurr (field_types.Currency_Type) :
    _tag = '767'

class NoTrdRegTimestamps (field_types.NumInGroup_Type) :
    _tag = '768'

class TrdRegTimestamp (field_types.UTCTimestamp_Type) :
    _tag = '769'

class TrdRegTimestampType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '770'
    ENUM_EXECUTION_TIME = 1
    ENUM_TIME_IN = 2
    ENUM_TIME_OUT = 3
    ENUM_BROKER_RECEIPT = 4
    ENUM_BROKER_EXECUTION = 5

class TrdRegTimestampOrigin (field_types.String_Type) :
    _tag = '771'

class ConfirmRefID (field_types.String_Type) :
    _tag = '772'

class ConfirmType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '773'
    ENUM_STATUS = 1
    ENUM_CONFIRMATION = 2
    ENUM_CONFIRMATION_REQUEST_REJECTED = 3

class ConfirmRejReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '774'
    ENUM_MISMATCHED_ACCOUNT = 1
    ENUM_MISSING_SETTLEMENT_INSTRUCTIONS = 2
    ENUM_OTHER = 99

class BookingType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '775'
    ENUM_REGULAR_BOOKING = 0
    ENUM_CFD = 1
    ENUM_TOTAL_RETURN_SWAP = 2

class IndividualAllocRejCode (field_types.int_Type) :
    _tag = '776'

class SettlInstMsgID (field_types.String_Type) :
    _tag = '777'

class NoSettlInst (field_types.NumInGroup_Type) :
    _tag = '778'

class LastUpdateTime (field_types.UTCTimestamp_Type) :
    _tag = '779'

class AllocSettlInstType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '780'
    ENUM_USE_DEFAULT_INSTRUCTIONS = 0
    ENUM_DERIVE_FROM_PARAMETERS_PROVIDED = 1
    ENUM_FULL_DETAILS_PROVIDED = 2
    ENUM_SSIDBI_DS_PROVIDED = 3
    ENUM_PHONE_FOR_INSTRUCTIONS = 4

class NoSettlPartyIDs (field_types.NumInGroup_Type) :
    _tag = '781'

class SettlPartyID (field_types.String_Type) :
    _tag = '782'

class SettlPartyIDSource (field_types.char_Type) :
    _tag = '783'

class SettlPartyRole (field_types.int_Type) :
    _tag = '784'

class SettlPartySubID (field_types.String_Type) :
    _tag = '785'

class SettlPartySubIDType (field_types.int_Type) :
    _tag = '786'

class DlvyInstType (field_types.char_Type, field_types.char_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '787'
    ENUM_SECURITIES = 'S'
    ENUM_CASH = 'C'

class TerminationType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '788'
    ENUM_OVERNIGHT = 1
    ENUM_TERM = 2
    ENUM_FLEXIBLE = 3
    ENUM_OPEN = 4

class NextExpectedMsgSeqNum (field_types.SeqNum_Type) :
    _tag = '789'

class OrdStatusReqID (field_types.String_Type) :
    _tag = '790'

class SettlInstReqID (field_types.String_Type) :
    _tag = '791'

class SettlInstReqRejCode (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '792'
    ENUM_UNABLE_TO_PROCESS_REQUEST = 0
    ENUM_UNKNOWN_ACCOUNT = 1
    ENUM_NO_MATCHING_SETTLEMENT_INSTRUCTIONS_FOUND = 2
    ENUM_OTHER = 99

class SecondaryAllocID (field_types.String_Type) :
    _tag = '793'

class AllocReportType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '794'
    ENUM_SELLSIDE_CALCULATED_USING_PRELIMINARY = 3
    ENUM_SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY = 4
    ENUM_WAREHOUSE_RECAP = 5
    ENUM_REQUEST_TO_INTERMEDIARY = 8

class AllocReportRefID (field_types.String_Type) :
    _tag = '795'

class AllocCancReplaceReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '796'
    ENUM_ORIGINAL_DETAILS_INCOMPLETE = 1
    ENUM_CHANGE_IN_UNDERLYING_ORDER_DETAILS = 2
    ENUM_OTHER = 99

class CopyMsgIndicator (field_types.Boolean_Type) :
    _tag = '797'

class AllocAccountType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '798'
    ENUM_CARRIED_CUSTOMER_SIDE = 1
    ENUM_CARRIED_NON_CUSTOMER_SIDE = 2
    ENUM_HOUSE_TRADER = 3
    ENUM_FLOOR_TRADER = 4
    ENUM_CARRIED_NON_CUSTOMER_SIDE_CROSS_MARGINED = 6
    ENUM_HOUSE_TRADER_CROSS_MARGINED = 7
    ENUM_JOINT_BACK_OFFICE_ACCOUNT = 8

class OrderAvgPx (field_types.Price_Type) :
    _tag = '799'

class OrderBookingQty (field_types.Qty_Type) :
    _tag = '800'

class NoSettlPartySubIDs (field_types.NumInGroup_Type) :
    _tag = '801'

class NoPartySubIDs (field_types.NumInGroup_Type) :
    _tag = '802'

class PartySubIDType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '803'
    ENUM_FIRM = 1
    ENUM_PERSON = 2
    ENUM_SYSTEM = 3
    ENUM_APPLICATION = 4
    ENUM_FULL_LEGAL_NAME_OF_FIRM = 5
    ENUM_POSTAL_ADDRESS = 6
    ENUM_PHONE_NUMBER = 7
    ENUM_EMAIL_ADDRESS = 8
    ENUM_CONTACT_NAME = 9
    ENUM_SECURITIES_ACCOUNT_NUMBER = 10
    ENUM_REGISTRATION_NUMBER = 11
    ENUM_REGISTERED_ADDRESS_FOR_CONFIRMATION = 12
    ENUM_REGULATORY_STATUS = 13
    ENUM_REGISTRATION_NAME = 14
    ENUM_CASH_ACCOUNT_NUMBER = 15
    ENUM_BIC = 16
    ENUM_CSD_PARTICIPANT_MEMBER_CODE = 17
    ENUM_REGISTERED_ADDRESS = 18
    ENUM_FUND_ACCOUNT_NAME = 19
    ENUM_TELEX_NUMBER = 20
    ENUM_FAX_NUMBER = 21
    ENUM_SECURITIES_ACCOUNT_NAME = 22
    ENUM_CASH_ACCOUNT_NAME = 23
    ENUM_DEPARTMENT = 24
    ENUM_LOCATION_DESK = 25
    ENUM_POSITION_ACCOUNT_TYPE = 26

class NoNestedPartySubIDs (field_types.NumInGroup_Type) :
    _tag = '804'

class NestedPartySubIDType (field_types.int_Type) :
    _tag = '805'

class NoNested2PartySubIDs (field_types.NumInGroup_Type) :
    _tag = '806'

class Nested2PartySubIDType (field_types.int_Type) :
    _tag = '807'

class AllocIntermedReqType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '808'
    ENUM_PENDING_ACCEPT = 1
    ENUM_PENDING_RELEASE = 2
    ENUM_PENDING_REVERSAL = 3
    ENUM_ACCEPT = 4
    ENUM_BLOCK_LEVEL_REJECT = 5
    ENUM_ACCOUNT_LEVEL_REJECT = 6

class UnderlyingPx (field_types.Price_Type) :
    _tag = '810'

class PriceDelta (field_types.float_Type) :
    _tag = '811'

class ApplQueueMax (field_types.int_Type) :
    _tag = '812'

class ApplQueueDepth (field_types.int_Type) :
    _tag = '813'

class ApplQueueResolution (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '814'
    ENUM_NO_ACTION_TAKEN = 0
    ENUM_QUEUE_FLUSHED = 1
    ENUM_OVERLAY_LAST = 2
    ENUM_END_SESSION = 3

class ApplQueueAction (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '815'
    ENUM_NO_ACTION_TAKEN = 0
    ENUM_QUEUE_FLUSHED = 1
    ENUM_OVERLAY_LAST = 2
    ENUM_END_SESSION = 3

class NoAltMDSource (field_types.NumInGroup_Type) :
    _tag = '816'

class AltMDSourceID (field_types.String_Type) :
    _tag = '817'

class SecondaryTradeReportID (field_types.String_Type) :
    _tag = '818'

class AvgPxIndicator (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '819'
    ENUM_NO_AVERAGE_PRICING = 0
    ENUM_TRADE = 1
    ENUM_LAST_TRADE = 2

class TradeLinkID (field_types.String_Type) :
    _tag = '820'

class OrderInputDevice (field_types.String_Type) :
    _tag = '821'

class UnderlyingTradingSessionID (field_types.String_Type) :
    _tag = '822'

class UnderlyingTradingSessionSubID (field_types.String_Type) :
    _tag = '823'

class TradeLegRefID (field_types.String_Type) :
    _tag = '824'

class ExchangeRule (field_types.String_Type) :
    _tag = '825'

class TradeAllocIndicator (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '826'
    ENUM_ALLOCATION_NOT_REQUIRED = 0
    ENUM_ALLOCATION_REQUIRED = 1
    ENUM_USE_ALLOCATION_PROVIDED_WITH_THE_TRADE = 2

class ExpirationCycle (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '827'
    ENUM_EXPIRE_ON_TRADING_SESSION_CLOSE = 0
    ENUM_EXPIRE_ON_TRADING_SESSION_OPEN = 1

class TrdType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '828'
    ENUM_REGULAR_TRADE = 0
    ENUM_BLOCK_TRADE = 1
    ENUM_EFP = 2
    ENUM_TRANSFER = 3
    ENUM_LATE_TRADE = 4
    ENUM_T_TRADE = 5
    ENUM_WEIGHTED_AVERAGE_PRICE_TRADE = 6
    ENUM_BUNCHED_TRADE = 7
    ENUM_LATE_BUNCHED_TRADE = 8
    ENUM_PRIOR_REFERENCE_PRICE_TRADE = 9
    ENUM_AFTER_HOURS_TRADE = 10

class TrdSubType (field_types.int_Type) :
    _tag = '829'

class TransferReason (field_types.String_Type) :
    _tag = '830'

class TotNumAssignmentReports (field_types.int_Type) :
    _tag = '832'

class AsgnRptID (field_types.String_Type) :
    _tag = '833'

class ThresholdAmount (field_types.PriceOffset_Type) :
    _tag = '834'

class PegMoveType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '835'
    ENUM_FLOATING = 0
    ENUM_FIXED = 1

class PegOffsetType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '836'
    ENUM_PRICE = 0
    ENUM_BASIS_POINTS = 1
    ENUM_TICKS = 2
    ENUM_PRICE_TIER = 3

class PegLimitType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '837'
    ENUM_OR_BETTER = 0
    ENUM_STRICT = 1
    ENUM_OR_WORSE = 2

class PegRoundDirection (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '838'
    ENUM_MORE_AGGRESSIVE = 1
    ENUM_MORE_PASSIVE = 2

class PeggedPrice (field_types.Price_Type) :
    _tag = '839'

class PegScope (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '840'
    ENUM_LOCAL = 1
    ENUM_NATIONAL = 2
    ENUM_GLOBAL = 3
    ENUM_NATIONAL_EXCLUDING_LOCAL = 4

class DiscretionMoveType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '841'
    ENUM_FLOATING = 0
    ENUM_FIXED = 1

class DiscretionOffsetType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '842'
    ENUM_PRICE = 0
    ENUM_BASIS_POINTS = 1
    ENUM_TICKS = 2
    ENUM_PRICE_TIER = 3

class DiscretionLimitType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '843'
    ENUM_OR_BETTER = 0
    ENUM_STRICT = 1
    ENUM_OR_WORSE = 2

class DiscretionRoundDirection (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '844'
    ENUM_MORE_AGGRESSIVE = 1
    ENUM_MORE_PASSIVE = 2

class DiscretionPrice (field_types.Price_Type) :
    _tag = '845'

class DiscretionScope (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '846'
    ENUM_LOCAL = 1
    ENUM_NATIONAL = 2
    ENUM_GLOBAL = 3
    ENUM_NATIONAL_EXCLUDING_LOCAL = 4

class TargetStrategy (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '847'
    ENUM_VWAP = 1
    ENUM_PARTICIPATE = 2
    ENUM_MININIZE_MARKET_IMPACT = 3

class TargetStrategyParameters (field_types.String_Type) :
    _tag = '848'

class ParticipationRate (field_types.Percentage_Type) :
    _tag = '849'

class TargetStrategyPerformance (field_types.float_Type) :
    _tag = '850'

class LastLiquidityInd (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '851'
    ENUM_ADDED_LIQUIDITY = 1
    ENUM_REMOVED_LIQUIDITY = 2
    ENUM_LIQUIDITY_ROUTED_OUT = 3

class PublishTrdIndicator (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '852'
    ENUM_REPORT_TRADE = 'Y'
    ENUM_DO_NOT_REPORT_TRADE = 'N'

class ShortSaleReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '853'
    ENUM_DEALER_SOLD_SHORT = 0
    ENUM_DEALER_SOLD_SHORT_EXEMPT = 1
    ENUM_SELLING_CUSTOMER_SOLD_SHORT = 2
    ENUM_SELLING_CUSTOMER_SOLD_SHORT_EXEMPT = 3
    ENUM_QUALIFIED_SERVICE_REPRESENTATIVE = 4
    ENUM_QSR_OR_AGU_CONTRA_SIDE_SOLD_SHORT_EXEMPT = 5

class QtyType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '854'
    ENUM_UNITS = 0
    ENUM_CONTRACTS = 1

class SecondaryTrdType (field_types.int_Type) :
    _tag = '855'

class TradeReportType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '856'
    ENUM_SUBMIT = 0
    ENUM_ALLEGED = 1
    ENUM_ACCEPT = 2
    ENUM_DECLINE = 3
    ENUM_ADDENDUM = 4
    ENUM_NO = 5
    ENUM_TRADE_REPORT_CANCEL = 6
    ENUM_LOCKED_IN = 7

class AllocNoOrdersType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '857'
    ENUM_NOT_SPECIFIED = 0
    ENUM_EXPLICIT_LIST_PROVIDED = 1

class SharedCommission (field_types.Amt_Type) :
    _tag = '858'

class ConfirmReqID (field_types.String_Type) :
    _tag = '859'

class AvgParPx (field_types.Price_Type) :
    _tag = '860'

class ReportedPx (field_types.Price_Type) :
    _tag = '861'

class NoCapacities (field_types.NumInGroup_Type) :
    _tag = '862'

class OrderCapacityQty (field_types.Qty_Type) :
    _tag = '863'

class NoEvents (field_types.NumInGroup_Type) :
    _tag = '864'

class EventType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '865'
    ENUM_PUT = 1
    ENUM_CALL = 2
    ENUM_TENDER = 3
    ENUM_SINKING_FUND_CALL = 4
    ENUM_OTHER = 99

class EventDate (field_types.LocalMktDate_Type) :
    _tag = '866'

class EventPx (field_types.Price_Type) :
    _tag = '867'

class EventText (field_types.String_Type) :
    _tag = '868'

class PctAtRisk (field_types.Percentage_Type) :
    _tag = '869'

class NoInstrAttrib (field_types.NumInGroup_Type) :
    _tag = '870'

class InstrAttribType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '871'
    ENUM_FLAT = 1
    ENUM_ZERO_COUPON = 2
    ENUM_INTEREST_BEARING = 3
    ENUM_NO_PERIODIC_PAYMENTS = 4
    ENUM_VARIABLE_RATE = 5
    ENUM_LESS_FEE_FOR_PUT = 6
    ENUM_STEPPED_COUPON = 7
    ENUM_COUPON_PERIOD = 8
    ENUM_WHEN = 9
    ENUM_ORIGINAL_ISSUE_DISCOUNT = 10
    ENUM_CALLABLE = 11
    ENUM_ESCROWED_TO_MATURITY = 12
    ENUM_ESCROWED_TO_REDEMPTION_DATE = 13
    ENUM_PRE_REFUNDED = 14
    ENUM_IN_DEFAULT = 15
    ENUM_UNRATED = 16
    ENUM_TAXABLE = 17
    ENUM_INDEXED = 18
    ENUM_SUBJECT_TO_ALTERNATIVE_MINIMUM_TAX = 19
    ENUM_ORIGINAL_ISSUE_DISCOUNT_PRICE = 20
    ENUM_CALLABLE_BELOW_MATURITY_VALUE = 21
    ENUM_CALLABLE_WITHOUT_NOTICE = 22
    ENUM_TEXT = 99

class InstrAttribValue (field_types.String_Type) :
    _tag = '872'

class DatedDate (field_types.LocalMktDate_Type) :
    _tag = '873'

class InterestAccrualDate (field_types.LocalMktDate_Type) :
    _tag = '874'

class CPProgram (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '875'
    ENUM_PROGRAM3A3 = 1
    ENUM_PROGRAM42 = 2
    ENUM_OTHER = 99

class CPRegType (field_types.String_Type) :
    _tag = '876'

class UnderlyingCPProgram (field_types.String_Type) :
    _tag = '877'

class UnderlyingCPRegType (field_types.String_Type) :
    _tag = '878'

class UnderlyingQty (field_types.Qty_Type) :
    _tag = '879'

class TrdMatchID (field_types.String_Type) :
    _tag = '880'

class SecondaryTradeReportRefID (field_types.String_Type) :
    _tag = '881'

class UnderlyingDirtyPrice (field_types.Price_Type) :
    _tag = '882'

class UnderlyingEndPrice (field_types.Price_Type) :
    _tag = '883'

class UnderlyingStartValue (field_types.Amt_Type) :
    _tag = '884'

class UnderlyingCurrentValue (field_types.Amt_Type) :
    _tag = '885'

class UnderlyingEndValue (field_types.Amt_Type) :
    _tag = '886'

class NoUnderlyingStips (field_types.NumInGroup_Type) :
    _tag = '887'

class UnderlyingStipType (field_types.String_Type) :
    _tag = '888'

class UnderlyingStipValue (field_types.String_Type) :
    _tag = '889'

class MaturityNetMoney (field_types.Amt_Type) :
    _tag = '890'

class MiscFeeBasis (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '891'
    ENUM_ABSOLUTE = 0
    ENUM_PER_UNIT = 1
    ENUM_PERCENTAGE = 2

class TotNoAllocs (field_types.int_Type) :
    _tag = '892'

class LastFragment (field_types.Boolean_Type, field_types.Boolean_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '893'
    ENUM_LAST_MESSAGE = 'Y'
    ENUM_NOT_LAST_MESSAGE = 'N'

class CollReqID (field_types.String_Type) :
    _tag = '894'

class CollAsgnReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '895'
    ENUM_INITIAL = 0
    ENUM_SCHEDULED = 1
    ENUM_TIME_WARNING = 2
    ENUM_MARGIN_DEFICIENCY = 3
    ENUM_MARGIN_EXCESS = 4
    ENUM_FORWARD_COLLATERAL_DEMAND = 5
    ENUM_EVENT_OF_DEFAULT = 6
    ENUM_ADVERSE_TAX_EVENT = 7

class CollInquiryQualifier (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '896'
    ENUM_TRADE_DATE = 0
    ENUM_GC_INSTRUMENT = 1
    ENUM_COLLATERAL_INSTRUMENT = 2
    ENUM_SUBSTITUTION_ELIGIBLE = 3
    ENUM_NOT_ASSIGNED = 4
    ENUM_PARTIALLY_ASSIGNED = 5
    ENUM_FULLY_ASSIGNED = 6
    ENUM_OUTSTANDING_TRADES = 7

class NoTrades (field_types.NumInGroup_Type) :
    _tag = '897'

class MarginRatio (field_types.Percentage_Type) :
    _tag = '898'

class MarginExcess (field_types.Amt_Type) :
    _tag = '899'

class TotalNetValue (field_types.Amt_Type) :
    _tag = '900'

class CashOutstanding (field_types.Amt_Type) :
    _tag = '901'

class CollAsgnID (field_types.String_Type) :
    _tag = '902'

class CollAsgnTransType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '903'
    ENUM_NEW = 0
    ENUM_REPLACE = 1
    ENUM_CANCEL = 2
    ENUM_RELEASE = 3
    ENUM_REVERSE = 4

class CollRespID (field_types.String_Type) :
    _tag = '904'

class CollAsgnRespType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '905'
    ENUM_RECEIVED = 0
    ENUM_ACCEPTED = 1
    ENUM_DECLINED = 2
    ENUM_REJECTED = 3

class CollAsgnRejectReason (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '906'
    ENUM_UNKNOWN_DEAL = 0
    ENUM_UNKNOWN_OR_INVALID_INSTRUMENT = 1
    ENUM_UNAUTHORIZED_TRANSACTION = 2
    ENUM_INSUFFICIENT_COLLATERAL = 3
    ENUM_INVALID_TYPE_OF_COLLATERAL = 4
    ENUM_EXCESSIVE_SUBSTITUTION = 5
    ENUM_OTHER = 99

class CollAsgnRefID (field_types.String_Type) :
    _tag = '907'

class CollRptID (field_types.String_Type) :
    _tag = '908'

class CollInquiryID (field_types.String_Type) :
    _tag = '909'

class CollStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '910'
    ENUM_UNASSIGNED = 0
    ENUM_PARTIALLY_ASSIGNED = 1
    ENUM_ASSIGNMENT_PROPOSED = 2
    ENUM_ASSIGNED = 3
    ENUM_CHALLENGED = 4

class TotNumReports (field_types.int_Type) :
    _tag = '911'

class LastRptRequested (field_types.Boolean_Type) :
    _tag = '912'

class AgreementDesc (field_types.String_Type) :
    _tag = '913'

class AgreementID (field_types.String_Type) :
    _tag = '914'

class AgreementDate (field_types.LocalMktDate_Type) :
    _tag = '915'

class StartDate (field_types.LocalMktDate_Type) :
    _tag = '916'

class EndDate (field_types.LocalMktDate_Type) :
    _tag = '917'

class AgreementCurrency (field_types.Currency_Type) :
    _tag = '918'

class DeliveryType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '919'
    ENUM_VERSUS_PAYMENT = 0
    ENUM_FREE = 1
    ENUM_TRI_PARTY = 2
    ENUM_HOLD_IN_CUSTODY = 3

class EndAccruedInterestAmt (field_types.Amt_Type) :
    _tag = '920'

class StartCash (field_types.Amt_Type) :
    _tag = '921'

class EndCash (field_types.Amt_Type) :
    _tag = '922'

class UserRequestID (field_types.String_Type) :
    _tag = '923'

class UserRequestType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '924'
    ENUM_LOG_ON_USER = 1
    ENUM_LOG_OFF_USER = 2
    ENUM_CHANGE_PASSWORD_FOR_USER = 3
    ENUM_REQUEST_INDIVIDUAL_USER_STATUS = 4

class NewPassword (field_types.String_Type) :
    _tag = '925'

class UserStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '926'
    ENUM_LOGGED_IN = 1
    ENUM_NOT_LOGGED_IN = 2
    ENUM_USER_NOT_RECOGNISED = 3
    ENUM_PASSWORD_INCORRECT = 4
    ENUM_PASSWORD_CHANGED = 5
    ENUM_OTHER = 6

class UserStatusText (field_types.String_Type) :
    _tag = '927'

class StatusValue (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '928'
    ENUM_CONNECTED = 1
    ENUM_NOT_CONNECTED_UNEXPECTED = 2
    ENUM_NOT_CONNECTED_EXPECTED = 3
    ENUM_IN_PROCESS = 4

class StatusText (field_types.String_Type) :
    _tag = '929'

class RefCompID (field_types.String_Type) :
    _tag = '930'

class RefSubID (field_types.String_Type) :
    _tag = '931'

class NetworkResponseID (field_types.String_Type) :
    _tag = '932'

class NetworkRequestID (field_types.String_Type) :
    _tag = '933'

class LastNetworkResponseID (field_types.String_Type) :
    _tag = '934'

class NetworkRequestType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '935'
    ENUM_SNAPSHOT = 1
    ENUM_SUBSCRIBE = 2
    ENUM_STOP_SUBSCRIBING = 4
    ENUM_LEVEL_OF_DETAIL = 8

class NoCompIDs (field_types.NumInGroup_Type) :
    _tag = '936'

class NetworkStatusResponseType (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '937'
    ENUM_FULL = 1
    ENUM_INCREMENTAL_UPDATE = 2

class NoCollInquiryQualifier (field_types.NumInGroup_Type) :
    _tag = '938'

class TrdRptStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '939'
    ENUM_ACCEPTED = 0
    ENUM_REJECTED = 1

class AffirmStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '940'
    ENUM_RECEIVED = 1
    ENUM_CONFIRM_REJECTED = 2
    ENUM_AFFIRMED = 3

class UnderlyingStrikeCurrency (field_types.Currency_Type) :
    _tag = '941'

class LegStrikeCurrency (field_types.Currency_Type) :
    _tag = '942'

class TimeBracket (field_types.String_Type) :
    _tag = '943'

class CollAction (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '944'
    ENUM_RETAIN = 0
    ENUM_ADD = 1
    ENUM_REMOVE = 2

class CollInquiryStatus (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '945'
    ENUM_ACCEPTED = 0
    ENUM_ACCEPTED_WITH_WARNINGS = 1
    ENUM_COMPLETED = 2
    ENUM_COMPLETED_WITH_WARNINGS = 3
    ENUM_REJECTED = 4

class CollInquiryResult (field_types.int_Type, field_types.int_Type.mro()[-2], metaclass = fix_enum_type.EnumType) :
    _tag = '946'
    ENUM_SUCCESSFUL = 0
    ENUM_INVALID_OR_UNKNOWN_INSTRUMENT = 1
    ENUM_INVALID_OR_UNKNOWN_COLLATERAL_TYPE = 2
    ENUM_INVALID_PARTIES = 3
    ENUM_INVALID_TRANSPORT_TYPE_REQUESTED = 4
    ENUM_INVALID_DESTINATION_REQUESTED = 5
    ENUM_NO_COLLATERAL_FOUND_FOR_THE_TRADE_SPECIFIED = 6
    ENUM_NO_COLLATERAL_FOUND_FOR_THE_ORDER_SPECIFIED = 7
    ENUM_COLLATERAL_INQUIRY_TYPE_NOT_SUPPORTED = 8
    ENUM_UNAUTHORIZED_FOR_COLLATERAL_INQUIRY = 9
    ENUM_OTHER = 99

class StrikeCurrency (field_types.Currency_Type) :
    _tag = '947'

class NoNested3PartyIDs (field_types.NumInGroup_Type) :
    _tag = '948'

class Nested3PartyID (field_types.String_Type) :
    _tag = '949'

class Nested3PartyIDSource (field_types.char_Type) :
    _tag = '950'

class Nested3PartyRole (field_types.int_Type) :
    _tag = '951'

class NoNested3PartySubIDs (field_types.NumInGroup_Type) :
    _tag = '952'

class Nested3PartySubID (field_types.String_Type) :
    _tag = '953'

class Nested3PartySubIDType (field_types.int_Type) :
    _tag = '954'

class LegContractSettlMonth (field_types.MonthYear_Type) :
    _tag = '955'

class LegInterestAccrualDate (field_types.LocalMktDate_Type) :
    _tag = '956'
