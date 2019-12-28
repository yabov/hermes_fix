import fields
import fix_message

BEGINSTRING = 'FIX.4.4'
MESSAGE_TYPES = {}

class Account (fields.String) :
    _tag = '1'

class AdvId (fields.String) :
    _tag = '2'

class AdvRefID (fields.String) :
    _tag = '3'

class AdvSide (fields.char) :
    _tag = '4'
    ENUM_BUY = 'B'
    ENUM_SELL = 'S'
    ENUM_CROSS = 'X'
    ENUM_TRADE = 'T'

class AdvTransType (fields.String) :
    _tag = '5'
    ENUM_NEW = 'N'
    ENUM_CANCEL = 'C'
    ENUM_REPLACE = 'R'

class AvgPx (fields.Price) :
    _tag = '6'

class BeginSeqNo (fields.SeqNum) :
    _tag = '7'

class BeginString (fields.String) :
    _tag = '8'

class BodyLength (fields.Length) :
    _tag = '9'

class CheckSum (fields.String) :
    _tag = '10'

class ClOrdID (fields.String) :
    _tag = '11'

class Commission (fields.Amt) :
    _tag = '12'

class CommType (fields.char) :
    _tag = '13'
    ENUM_PER_UNIT = '1'
    ENUM_PERCENTAGE = '2'
    ENUM_ABSOLUTE = '3'
    ENUM_4 = '4'
    ENUM_5 = '5'
    ENUM_POINTS_PER_BOND_OR_CONTRACT_SUPPLY_CONTRACTMULTIPLIER = '6'

class CumQty (fields.Qty) :
    _tag = '14'

class Currency (fields.Currency) :
    _tag = '15'

class EndSeqNo (fields.SeqNum) :
    _tag = '16'

class ExecID (fields.String) :
    _tag = '17'

class ExecInst (fields.MultipleValueString) :
    _tag = '18'
    ENUM_NOT_HELD = '1'
    ENUM_WORK = '2'
    ENUM_GO_ALONG = '3'
    ENUM_OVER_THE_DAY = '4'
    ENUM_HELD = '5'
    ENUM_PARTICIPATE_DONT_INITIATE = '6'
    ENUM_STRICT_SCALE = '7'
    ENUM_TRY_TO_SCALE = '8'
    ENUM_STAY_ON_BIDSIDE = '9'
    ENUM_STAY_ON_OFFERSIDE = '0'
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

class ExecRefID (fields.String) :
    _tag = '19'

class HandlInst (fields.char) :
    _tag = '21'
    ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION = '1'
    ENUM_AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK = '2'
    ENUM_MANUAL_ORDER_BEST_EXECUTION = '3'

class SecurityIDSource (fields.String) :
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
    ENUM_ISDA_FPML_PRODUCT_SPECIFICATION = 'I'
    ENUM_OPTIONS_PRICE_REPORTING_AUTHORITY = 'J'

class IOIID (fields.String) :
    _tag = '23'

class IOIQltyInd (fields.char) :
    _tag = '25'
    ENUM_LOW = 'L'
    ENUM_MEDIUM = 'M'
    ENUM_HIGH = 'H'

class IOIRefID (fields.String) :
    _tag = '26'

class IOIQty (fields.String) :
    _tag = '27'
    ENUM_SMALL = 'S'
    ENUM_MEDIUM = 'M'
    ENUM_LARGE = 'L'

class IOITransType (fields.char) :
    _tag = '28'
    ENUM_NEW = 'N'
    ENUM_CANCEL = 'C'
    ENUM_REPLACE = 'R'

class LastCapacity (fields.char) :
    _tag = '29'
    ENUM_AGENT = '1'
    ENUM_CROSS_AS_AGENT = '2'
    ENUM_CROSS_AS_PRINCIPAL = '3'
    ENUM_PRINCIPAL = '4'

class LastMkt (fields.Exchange) :
    _tag = '30'

class LastPx (fields.Price) :
    _tag = '31'

class LastQty (fields.Qty) :
    _tag = '32'

class NoLinesOfText (fields.NumInGroup) :
    _tag = '33'

class MsgSeqNum (fields.SeqNum) :
    _tag = '34'

class MsgType (fields.String) :
    _tag = '35'
    ENUM_HEARTBEAT = '0'
    ENUM_TEST_REQUEST = '1'
    ENUM_RESEND_REQUEST = '2'
    ENUM_REJECT = '3'
    ENUM_SEQUENCE_RESET = '4'
    ENUM_LOGOUT = '5'
    ENUM_INDICATION_OF_INTEREST = '6'
    ENUM_ADVERTISEMENT = '7'
    ENUM_EXECUTION_REPORT = '8'
    ENUM_ORDER_CANCEL_REJECT = '9'
    ENUM_LOGON = 'A'
    ENUM_NEWS = 'B'
    ENUM_EMAIL = 'C'
    ENUM_ORDER_SINGLE = 'D'
    ENUM_ORDER_LIST = 'E'
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
    ENUM_XML_MESSAGE = 'n'
    ENUM_REGISTRATION_INSTRUCTIONS = 'o'
    ENUM_REGISTRATION_INSTRUCTIONS_RESPONSE = 'p'
    ENUM_ORDER_MASS_CANCEL_REQUEST = 'q'
    ENUM_ORDER_MASS_CANCEL_REPORT = 'r'
    ENUM_NEW_ORDER_s = 's'
    ENUM_CROSS_ORDER_CANCEL_REPLACE_REQUEST = 't'
    ENUM_CROSS_ORDER_CANCEL_REQUEST = 'u'
    ENUM_SECURITY_TYPE_REQUEST = 'v'
    ENUM_SECURITY_TYPES = 'w'
    ENUM_SECURITY_LIST_REQUEST = 'x'
    ENUM_SECURITY_LIST = 'y'
    ENUM_DERIVATIVE_SECURITY_LIST_REQUEST = 'z'
    ENUM_DERIVATIVE_SECURITY_LIST = 'AA'
    ENUM_NEW_ORDER_AB = 'AB'
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
    ENUM_NETWORK_BC = 'BC'
    ENUM_NETWORK_BD = 'BD'
    ENUM_USER_REQUEST = 'BE'
    ENUM_USER_RESPONSE = 'BF'
    ENUM_COLLATERAL_INQUIRY_ACK = 'BG'
    ENUM_CONFIRMATION_REQUEST = 'BH'

class NewSeqNo (fields.SeqNum) :
    _tag = '36'

class OrderID (fields.String) :
    _tag = '37'

class OrderQty (fields.Qty) :
    _tag = '38'

class OrdStatus (fields.char) :
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

class OrdType (fields.char) :
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
    ENUM_FOREX = 'G'
    ENUM_FUNARI = 'I'
    ENUM_MARKET_IF_TOUCHED = 'J'
    ENUM_MARKET_WITH_LEFTOVER_AS_LIMIT = 'K'
    ENUM_PREVIOUS_FUND_VALUATION_POINT = 'L'
    ENUM_NEXT_FUND_VALUATION_POINT = 'M'
    ENUM_PEGGED = 'P'

class OrigClOrdID (fields.String) :
    _tag = '41'

class OrigTime (fields.UTCTimestamp) :
    _tag = '42'

class PossDupFlag (fields.Boolean) :
    _tag = '43'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class Price (fields.Price) :
    _tag = '44'

class RefSeqNum (fields.SeqNum) :
    _tag = '45'

class SecurityID (fields.String) :
    _tag = '48'

class SenderCompID (fields.String) :
    _tag = '49'

class SenderSubID (fields.String) :
    _tag = '50'

class SendingTime (fields.UTCTimestamp) :
    _tag = '52'

class Quantity (fields.Qty) :
    _tag = '53'

class Side (fields.char) :
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

class Symbol (fields.String) :
    _tag = '55'

class TargetCompID (fields.String) :
    _tag = '56'

class TargetSubID (fields.String) :
    _tag = '57'

class Text (fields.String) :
    _tag = '58'

class TimeInForce (fields.char) :
    _tag = '59'
    ENUM_DAY = '0'
    ENUM_GOOD_TILL_CANCEL = '1'
    ENUM_AT_THE_OPENING = '2'
    ENUM_IMMEDIATE_OR_CANCEL = '3'
    ENUM_FILL_OR_KILL = '4'
    ENUM_GOOD_TILL_CROSSING = '5'
    ENUM_GOOD_TILL_DATE = '6'
    ENUM_AT_THE_CLOSE = '7'

class TransactTime (fields.UTCTimestamp) :
    _tag = '60'

class Urgency (fields.char) :
    _tag = '61'
    ENUM_NORMAL = '0'
    ENUM_FLASH = '1'
    ENUM_BACKGROUND = '2'

class ValidUntilTime (fields.UTCTimestamp) :
    _tag = '62'

class SettlType (fields.char) :
    _tag = '63'
    ENUM_REGULAR = '0'
    ENUM_CASH = '1'
    ENUM_NEXT_DAY = '2'
    ENUM_T_PLUS_2 = '3'
    ENUM_T_PLUS_3 = '4'
    ENUM_T_PLUS_4 = '5'
    ENUM_FUTURE = '6'
    ENUM_WHEN_AND_IF_ISSUED = '7'
    ENUM_SELLERS_OPTION = '8'
    ENUM_T_PLUS_5 = '9'

class SettlDate (fields.LocalMktDate) :
    _tag = '64'

class SymbolSfx (fields.String) :
    _tag = '65'

class ListID (fields.String) :
    _tag = '66'

class ListSeqNo (fields.int) :
    _tag = '67'

class TotNoOrders (fields.int) :
    _tag = '68'

class ListExecInst (fields.String) :
    _tag = '69'

class AllocID (fields.String) :
    _tag = '70'

class AllocTransType (fields.char) :
    _tag = '71'
    ENUM_NEW = '0'
    ENUM_REPLACE = '1'
    ENUM_CANCEL = '2'

class RefAllocID (fields.String) :
    _tag = '72'

class NoOrders (fields.NumInGroup) :
    _tag = '73'

class AvgPxPrecision (fields.int) :
    _tag = '74'

class TradeDate (fields.LocalMktDate) :
    _tag = '75'

class PositionEffect (fields.char) :
    _tag = '77'
    ENUM_OPEN = 'O'
    ENUM_CLOSE = 'C'
    ENUM_ROLLED = 'R'
    ENUM_FIFO = 'F'

class NoAllocs (fields.NumInGroup) :
    _tag = '78'

class AllocAccount (fields.String) :
    _tag = '79'

class AllocQty (fields.Qty) :
    _tag = '80'

class ProcessCode (fields.char) :
    _tag = '81'
    ENUM_REGULAR = '0'
    ENUM_SOFT_DOLLAR = '1'
    ENUM_STEP_IN = '2'
    ENUM_STEP_OUT = '3'
    ENUM_SOFT_DOLLAR_STEP_IN = '4'
    ENUM_SOFT_DOLLAR_STEP_OUT = '5'
    ENUM_PLAN_SPONSOR = '6'

class NoRpts (fields.int) :
    _tag = '82'

class RptSeq (fields.int) :
    _tag = '83'

class CxlQty (fields.Qty) :
    _tag = '84'

class NoDlvyInst (fields.NumInGroup) :
    _tag = '85'

class AllocStatus (fields.int) :
    _tag = '87'
    ENUM_ACCEPTED = 0
    ENUM_BLOCK_LEVEL_REJECT = 1
    ENUM_ACCOUNT_LEVEL_REJECT = 2
    ENUM_RECEIVED = 3
    ENUM_INCOMPLETE = 4
    ENUM_REJECTED_BY_INTERMEDIARY = 5

class AllocRejCode (fields.int) :
    _tag = '88'
    ENUM_UNKNOWN_ACCOUNT = 0
    ENUM_INCORRECT_QUANTITY = 1
    ENUM_INCORRECT_AVERAGE_PRICE = 2
    ENUM_UNKNOWN_EXECUTING_BROKER_MNEMONIC = 3
    ENUM_COMMISSION_DIFFERENCE = 4
    ENUM_UNKNOWN_ORDERID = 5
    ENUM_UNKNOWN_LISTID = 6
    ENUM_OTHER = 7
    ENUM_INCORRECT_ALLOCATED_QUANTITY = 8
    ENUM_CALCULATION_DIFFERENCE = 9
    ENUM_UNKNOWN_OR_STALE_EXECID = 10
    ENUM_MISMATCHED_DATA_VALUE = 11
    ENUM_UNKNOWN_CLORDID = 12
    ENUM_WAREHOUSE_REQUEST_REJECTED = 13

class Signature (fields.data) :
    _tag = '89'

class SecureDataLen (fields.Length) :
    _tag = '90'

class SecureData (fields.data) :
    _tag = '91'

class SignatureLength (fields.Length) :
    _tag = '93'

class EmailType (fields.char) :
    _tag = '94'
    ENUM_NEW = '0'
    ENUM_REPLY = '1'
    ENUM_ADMIN_REPLY = '2'

class RawDataLength (fields.Length) :
    _tag = '95'

class RawData (fields.data) :
    _tag = '96'

class PossResend (fields.Boolean) :
    _tag = '97'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class EncryptMethod (fields.int) :
    _tag = '98'
    ENUM_NONE = 0
    ENUM_PKCS = 1
    ENUM_DES = 2
    ENUM_PKCS_DES = 3
    ENUM_PGP_DES = 4
    ENUM_PGP_DES_MD5 = 5
    ENUM_PEM_DES_MD5 = 6

class StopPx (fields.Price) :
    _tag = '99'

class ExDestination (fields.Exchange) :
    _tag = '100'

class CxlRejReason (fields.int) :
    _tag = '102'
    ENUM_TOO_LATE_TO_CANCEL = 0
    ENUM_UNKNOWN_ORDER = 1
    ENUM_BROKER = 2
    ENUM_ORDER_ALREADY_IN_PENDING_CANCEL_OR_PENDING_REPLACE_STATUS = 3
    ENUM_UNABLE_TO_PROCESS_ORDER_MASS_CANCEL_REQUEST = 4
    ENUM_ORIGORDMODTIME = 5
    ENUM_DUPLICATE_CLORDID = 6
    ENUM_OTHER = 99

class OrdRejReason (fields.int) :
    _tag = '103'
    ENUM_BROKER = 0
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
    ENUM_UNSUPPORTED_ORDER_CHARACTERISTIC12_SURVEILLENCE_OPTION = 11
    ENUM_INCORRECT_QUANTITY = 13
    ENUM_INCORRECT_ALLOCATED_QUANTITY = 14
    ENUM_UNKNOWN_ACCOUNT = 15
    ENUM_OTHER = 99

class IOIQualifier (fields.char) :
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

class Issuer (fields.String) :
    _tag = '106'

class SecurityDesc (fields.String) :
    _tag = '107'

class HeartBtInt (fields.int) :
    _tag = '108'

class MinQty (fields.Qty) :
    _tag = '110'

class MaxFloor (fields.Qty) :
    _tag = '111'

class TestReqID (fields.String) :
    _tag = '112'

class ReportToExch (fields.Boolean) :
    _tag = '113'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class LocateReqd (fields.Boolean) :
    _tag = '114'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class OnBehalfOfCompID (fields.String) :
    _tag = '115'

class OnBehalfOfSubID (fields.String) :
    _tag = '116'

class QuoteID (fields.String) :
    _tag = '117'

class NetMoney (fields.Amt) :
    _tag = '118'

class SettlCurrAmt (fields.Amt) :
    _tag = '119'

class SettlCurrency (fields.Currency) :
    _tag = '120'

class ForexReq (fields.Boolean) :
    _tag = '121'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class OrigSendingTime (fields.UTCTimestamp) :
    _tag = '122'

class GapFillFlag (fields.Boolean) :
    _tag = '123'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class NoExecs (fields.NumInGroup) :
    _tag = '124'

class ExpireTime (fields.UTCTimestamp) :
    _tag = '126'

class DKReason (fields.char) :
    _tag = '127'
    ENUM_UNKNOWN_SYMBOL = 'A'
    ENUM_WRONG_SIDE = 'B'
    ENUM_QUANTITY_EXCEEDS_ORDER = 'C'
    ENUM_NO_MATCHING_ORDER = 'D'
    ENUM_PRICE_EXCEEDS_LIMIT = 'E'
    ENUM_CALCULATION_DIFFERENCE = 'F'
    ENUM_OTHER = 'Z'

class DeliverToCompID (fields.String) :
    _tag = '128'

class DeliverToSubID (fields.String) :
    _tag = '129'

class IOINaturalFlag (fields.Boolean) :
    _tag = '130'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class QuoteReqID (fields.String) :
    _tag = '131'

class BidPx (fields.Price) :
    _tag = '132'

class OfferPx (fields.Price) :
    _tag = '133'

class BidSize (fields.Qty) :
    _tag = '134'

class OfferSize (fields.Qty) :
    _tag = '135'

class NoMiscFees (fields.NumInGroup) :
    _tag = '136'

class MiscFeeAmt (fields.Amt) :
    _tag = '137'

class MiscFeeCurr (fields.Currency) :
    _tag = '138'

class MiscFeeType (fields.char) :
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

class PrevClosePx (fields.Price) :
    _tag = '140'

class ResetSeqNumFlag (fields.Boolean) :
    _tag = '141'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class SenderLocationID (fields.String) :
    _tag = '142'

class TargetLocationID (fields.String) :
    _tag = '143'

class OnBehalfOfLocationID (fields.String) :
    _tag = '144'

class DeliverToLocationID (fields.String) :
    _tag = '145'

class NoRelatedSym (fields.NumInGroup) :
    _tag = '146'

class Subject (fields.String) :
    _tag = '147'

class Headline (fields.String) :
    _tag = '148'

class URLLink (fields.String) :
    _tag = '149'

class ExecType (fields.char) :
    _tag = '150'
    ENUM_NEW = '0'
    ENUM_DONE_FOR_DAY = '3'
    ENUM_CANCELED = '4'
    ENUM_REPLACE = '5'
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

class LeavesQty (fields.Qty) :
    _tag = '151'

class CashOrderQty (fields.Qty) :
    _tag = '152'

class AllocAvgPx (fields.Price) :
    _tag = '153'

class AllocNetMoney (fields.Amt) :
    _tag = '154'

class SettlCurrFxRate (fields.float) :
    _tag = '155'

class SettlCurrFxRateCalc (fields.char) :
    _tag = '156'
    ENUM_MULTIPLY = 'M'
    ENUM_DIVIDE = 'D'

class NumDaysInterest (fields.int) :
    _tag = '157'

class AccruedInterestRate (fields.Percentage) :
    _tag = '158'

class AccruedInterestAmt (fields.Amt) :
    _tag = '159'

class SettlInstMode (fields.char) :
    _tag = '160'
    ENUM_STANDING_INSTRUCTIONS_PROVIDED = '1'
    ENUM_SPECIFIC_ORDER_FOR_A_SINGLE_ACCOUNT = '4'
    ENUM_REQUEST_REJECT = '5'

class AllocText (fields.String) :
    _tag = '161'

class SettlInstID (fields.String) :
    _tag = '162'

class SettlInstTransType (fields.char) :
    _tag = '163'
    ENUM_NEW = 'N'
    ENUM_CANCEL = 'C'
    ENUM_REPLACE = 'R'
    ENUM_RESTATE = 'T'

class EmailThreadID (fields.String) :
    _tag = '164'

class SettlInstSource (fields.char) :
    _tag = '165'
    ENUM_BROKERS_INSTRUCTIONS = '1'
    ENUM_INSTITUTIONS_INSTRUCTIONS = '2'
    ENUM_INVESTOR = '3'

class SecurityType (fields.String) :
    _tag = '167'
    ENUM_FUTURE = 'FUT'
    ENUM_OPTION = 'OPT'
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
    ENUM_US_TREASURY_NOTE_UST = 'UST'
    ENUM_US_TREASURY_BILL_USTB = 'USTB'
    ENUM_US_TREASURY_NOTE_TNOTE = 'TNOTE'
    ENUM_US_TREASURY_BILL_TBILL = 'TBILL'
    ENUM_REPURCHASE = 'REPO'
    ENUM_FORWARD = 'FORWARD'
    ENUM_BUY_SELLBACK = 'BUYSELL'
    ENUM_SECURITIES_LOAN = 'SECLOAN'
    ENUM_SECURITIES_PLEDGE = 'SECPLEDGE'
    ENUM_TERM_LOAN = 'TERM'
    ENUM_REVOLVER_LOAN = 'RVLV'
    ENUM_REVOLVER_TERM_LOAN = 'RVLVTRM'
    ENUM_BRIDGE_LOAN = 'BRIDGE'
    ENUM_LETTER_OF_CREDIT = 'LOFC'
    ENUM_SWING_LINE_FACILITY = 'SWING'
    ENUM_DEBTOR_IN_POSSESSION = 'DINP'
    ENUM_DEFAULTED = 'DEFLTED'
    ENUM_WITHDRAWN = 'WITHDRN'
    ENUM_REPLACED = 'REPLACD'
    ENUM_MATURED = 'MATURED'
    ENUM_AMENDED_RESTATED = 'AMENDED'
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
    ENUM_CORP_MORTGAGE_BACKED_SECURITIES = 'CMBS'
    ENUM_COLLATERALIZED_MORTGAGE_OBLIGATION = 'CMO'
    ENUM_IOETTE_MORTGAGE = 'IET'
    ENUM_MORTGAGE_BACKED_SECURITIES = 'MBS'
    ENUM_MORTGAGE_INTEREST_ONLY = 'MIO'
    ENUM_MORTGAGE_PRINCIPAL_ONLY = 'MPO'
    ENUM_MORTGAGE_PRIVATE_PLACEMENT = 'MPP'
    ENUM_MISCELLANEOUS_PASS_THROUGH = 'MPT'
    ENUM_PFANDBRIEFE = 'PFAND'
    ENUM_TO_BE_ANNOUNCED = 'TBA'
    ENUM_OTHER_ANTICIPATION_NOTES_BAN_GAN_ETC = 'AN'
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
    ENUM_MULTI_LEG_INSTRUMENT = 'MLEG'
    ENUM_NO_SECURITY_TYPE = 'NONE'

class EffectiveTime (fields.UTCTimestamp) :
    _tag = '168'

class StandInstDbType (fields.int) :
    _tag = '169'
    ENUM_OTHER = 0
    ENUM_DTC_SID = 1
    ENUM_THOMSON_ALERT = 2
    ENUM_A_GLOBAL_CUSTODIAN = 3
    ENUM_ACCOUNTNET = 4

class StandInstDbName (fields.String) :
    _tag = '170'

class StandInstDbID (fields.String) :
    _tag = '171'

class SettlDeliveryType (fields.int) :
    _tag = '172'
    ENUM_VERSUS_PAYMENT_DELIVER = 0
    ENUM_FREE_DELIVER = 1
    ENUM_TRI_PARTY = 2
    ENUM_HOLD_IN_CUSTODY = 3

class BidSpotRate (fields.Price) :
    _tag = '188'

class BidForwardPoints (fields.PriceOffset) :
    _tag = '189'

class OfferSpotRate (fields.Price) :
    _tag = '190'

class OfferForwardPoints (fields.PriceOffset) :
    _tag = '191'

class OrderQty2 (fields.Qty) :
    _tag = '192'

class SettlDate2 (fields.LocalMktDate) :
    _tag = '193'

class LastSpotRate (fields.Price) :
    _tag = '194'

class LastForwardPoints (fields.PriceOffset) :
    _tag = '195'

class AllocLinkID (fields.String) :
    _tag = '196'

class AllocLinkType (fields.int) :
    _tag = '197'
    ENUM_F_X_NETTING = 0
    ENUM_F_X_SWAP = 1

class SecondaryOrderID (fields.String) :
    _tag = '198'

class NoIOIQualifiers (fields.NumInGroup) :
    _tag = '199'

class MaturityMonthYear (fields.MonthYear) :
    _tag = '200'

class PutOrCall (fields.int) :
    _tag = '201'
    ENUM_PUT = 0
    ENUM_CALL = 1

class StrikePrice (fields.Price) :
    _tag = '202'

class CoveredOrUncovered (fields.int) :
    _tag = '203'
    ENUM_COVERED = 0
    ENUM_UNCOVERED = 1

class OptAttribute (fields.char) :
    _tag = '206'

class SecurityExchange (fields.Exchange) :
    _tag = '207'

class NotifyBrokerOfCredit (fields.Boolean) :
    _tag = '208'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class AllocHandlInst (fields.int) :
    _tag = '209'
    ENUM_MATCH = 1
    ENUM_FORWARD = 2
    ENUM_FORWARD_AND_MATCH = 3

class MaxShow (fields.Qty) :
    _tag = '210'

class PegOffsetValue (fields.float) :
    _tag = '211'

class XmlDataLen (fields.Length) :
    _tag = '212'

class XmlData (fields.data) :
    _tag = '213'

class SettlInstRefID (fields.String) :
    _tag = '214'

class NoRoutingIDs (fields.NumInGroup) :
    _tag = '215'

class RoutingType (fields.int) :
    _tag = '216'
    ENUM_TARGET_FIRM = 1
    ENUM_TARGET_LIST = 2
    ENUM_BLOCK_FIRM = 3
    ENUM_BLOCK_LIST = 4

class RoutingID (fields.String) :
    _tag = '217'

class Spread (fields.PriceOffset) :
    _tag = '218'

class BenchmarkCurveCurrency (fields.Currency) :
    _tag = '220'

class BenchmarkCurveName (fields.String) :
    _tag = '221'

class BenchmarkCurvePoint (fields.String) :
    _tag = '222'

class CouponRate (fields.Percentage) :
    _tag = '223'

class CouponPaymentDate (fields.LocalMktDate) :
    _tag = '224'

class IssueDate (fields.LocalMktDate) :
    _tag = '225'

class RepurchaseTerm (fields.int) :
    _tag = '226'

class RepurchaseRate (fields.Percentage) :
    _tag = '227'

class Factor (fields.float) :
    _tag = '228'

class TradeOriginationDate (fields.LocalMktDate) :
    _tag = '229'

class ExDate (fields.LocalMktDate) :
    _tag = '230'

class ContractMultiplier (fields.float) :
    _tag = '231'

class NoStipulations (fields.NumInGroup) :
    _tag = '232'

class StipulationType (fields.String) :
    _tag = '233'
    ENUM_AMT = 'AMT'
    ENUM_AUTO_REINVESTMENT_AT_RATE_OR_BETTER = 'AUTOREINV'
    ENUM_BANK_QUALIFIED = 'BANKQUAL'
    ENUM_BARGAIN_CONDITIONS_SEE = 'BGNCON'
    ENUM_COUPON_RANGE = 'COUPON'
    ENUM_ISO_CURRENCY_CODE = 'CURRENCY'
    ENUM_CUSTOM_START_END_DATE = 'CUSTOMDATE'
    ENUM_GEOGRAPHICS_AND_RANGE = 'GEOG'
    ENUM_VALUATION_DISCOUNT = 'HAIRCUT'
    ENUM_INSURED = 'INSURED'
    ENUM_YEAR_OR_YEAR_MONTH_OF_ISSUE = 'ISSUE'
    ENUM_ISSUERS_TICKER = 'ISSUER'
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
    ENUM_PAYMENT_FREQUENCY_CALENDAR = 'PAYFREQ'
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
    ENUM_TYPE_OF_REDEMPTION_VALUES_ARE_NONCALLABLE_CALLABLE_PREFUNDED_ESCROWEDTOMATURITY_PUTABLE_CONVERTIBLE = 'REDEMPTION'
    ENUM_RESTRICTED = 'RESTRICTED'
    ENUM_MARKET_SECTOR = 'SECTOR'
    ENUM_SECURITYTYPE_INCLUDED_OR_EXCLUDED = 'SECTYPE'
    ENUM_STRUCTURE = 'STRUCT'
    ENUM_SUBSTITUTIONS_FREQUENCY = 'SUBSFREQ'
    ENUM_SUBSTITUTIONS_LEFT = 'SUBSLEFT'
    ENUM_FREEFORM_TEXT = 'TEXT'
    ENUM_TRADE_VARIANCE = 'TRDVAR'
    ENUM_WEIGHTED_AVERAGE_COUPONVALUE_IN_PERCENT = 'WAC'
    ENUM_WEIGHTED_AVERAGE_LIFE_COUPON_VALUE_IN_PERCENT = 'WAL'
    ENUM_WEIGHTED_AVERAGE_LOAN_AGE_VALUE_IN_MONTHS = 'WALA'
    ENUM_WEIGHTED_AVERAGE_MATURITY_VALUE_IN_MONTHS = 'WAM'
    ENUM_WHOLE_POOL = 'WHOLE'
    ENUM_YIELD_RANGE = 'YIELD'

class StipulationValue (fields.String) :
    _tag = '234'

class YieldType (fields.String) :
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
    ENUM_GOVERNMENT_EQUIVALENT_YIELD = 'GOVTEQUIV'
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
    ENUM_YIELD_VALUE_OF_1_32 = 'VALUE1/32'
    ENUM_YIELD_TO_WORST = 'WORST'

class Yield (fields.Percentage) :
    _tag = '236'

class TotalTakedown (fields.Amt) :
    _tag = '237'

class Concession (fields.Amt) :
    _tag = '238'

class RepoCollateralSecurityType (fields.String) :
    _tag = '239'

class RedemptionDate (fields.LocalMktDate) :
    _tag = '240'

class UnderlyingCouponPaymentDate (fields.LocalMktDate) :
    _tag = '241'

class UnderlyingIssueDate (fields.LocalMktDate) :
    _tag = '242'

class UnderlyingRepoCollateralSecurityType (fields.String) :
    _tag = '243'

class UnderlyingRepurchaseTerm (fields.int) :
    _tag = '244'

class UnderlyingRepurchaseRate (fields.Percentage) :
    _tag = '245'

class UnderlyingFactor (fields.float) :
    _tag = '246'

class UnderlyingRedemptionDate (fields.LocalMktDate) :
    _tag = '247'

class LegCouponPaymentDate (fields.LocalMktDate) :
    _tag = '248'

class LegIssueDate (fields.LocalMktDate) :
    _tag = '249'

class LegRepoCollateralSecurityType (fields.String) :
    _tag = '250'

class LegRepurchaseTerm (fields.int) :
    _tag = '251'

class LegRepurchaseRate (fields.Percentage) :
    _tag = '252'

class LegFactor (fields.float) :
    _tag = '253'

class LegRedemptionDate (fields.LocalMktDate) :
    _tag = '254'

class CreditRating (fields.String) :
    _tag = '255'

class UnderlyingCreditRating (fields.String) :
    _tag = '256'

class LegCreditRating (fields.String) :
    _tag = '257'

class TradedFlatSwitch (fields.Boolean) :
    _tag = '258'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class BasisFeatureDate (fields.LocalMktDate) :
    _tag = '259'

class BasisFeaturePrice (fields.Price) :
    _tag = '260'

class MDReqID (fields.String) :
    _tag = '262'

class SubscriptionRequestType (fields.char) :
    _tag = '263'
    ENUM_SNAPSHOT = '0'
    ENUM_SNAPSHOT_PLUS_UPDATES = '1'
    ENUM_DISABLE_PREVIOUS_SNAPSHOT_PLUS_UPDATE_REQUEST = '2'

class MarketDepth (fields.int) :
    _tag = '264'

class MDUpdateType (fields.int) :
    _tag = '265'
    ENUM_FULL_REFRESH = 0
    ENUM_INCREMENTAL_REFRESH = 1

class AggregatedBook (fields.Boolean) :
    _tag = '266'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class NoMDEntryTypes (fields.NumInGroup) :
    _tag = '267'

class NoMDEntries (fields.NumInGroup) :
    _tag = '268'

class MDEntryType (fields.char) :
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

class MDEntryPx (fields.Price) :
    _tag = '270'

class MDEntrySize (fields.Qty) :
    _tag = '271'

class MDEntryDate (fields.UTCDateOnly) :
    _tag = '272'

class MDEntryTime (fields.UTCTimeOnly) :
    _tag = '273'

class TickDirection (fields.char) :
    _tag = '274'
    ENUM_PLUS_TICK = '0'
    ENUM_ZERO_PLUS_TICK = '1'
    ENUM_MINUS_TICK = '2'
    ENUM_ZERO_MINUS_TICK = '3'

class MDMkt (fields.Exchange) :
    _tag = '275'

class QuoteCondition (fields.MultipleValueString) :
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

class TradeCondition (fields.MultipleValueString) :
    _tag = '277'
    ENUM_CASH = 'A'
    ENUM_AVERAGE_PRICE_TRADE = 'B'
    ENUM_CASH_TRADE = 'C'
    ENUM_NEXT_DAY = 'D'
    ENUM_OPENING = 'E'
    ENUM_INTRADAY_TRADE_DETAIL = 'F'
    ENUM_RULE_127_TRADE = 'G'
    ENUM_RULE_155_TRADE = 'H'
    ENUM_SOLD_LAST = 'I'
    ENUM_NEXT_DAY_TRADE = 'J'
    ENUM_OPENED = 'K'
    ENUM_SELLER = 'L'
    ENUM_SOLD = 'M'
    ENUM_STOPPED_STOCK = 'N'
    ENUM_IMBALANCE_MORE_BUYERS = 'P'
    ENUM_IMBALANCE_MORE_SELLERS = 'Q'
    ENUM_OPENING_PRICE = 'R'

class MDEntryID (fields.String) :
    _tag = '278'

class MDUpdateAction (fields.char) :
    _tag = '279'
    ENUM_NEW = '0'
    ENUM_CHANGE = '1'
    ENUM_DELETE = '2'

class MDEntryRefID (fields.String) :
    _tag = '280'

class MDReqRejReason (fields.char) :
    _tag = '281'
    ENUM_UNKNOWN_SYMBOL = '0'
    ENUM_DUPLICATE_MDREQID = '1'
    ENUM_INSUFFICIENT_BANDWIDTH = '2'
    ENUM_INSUFFICIENT_PERMISSIONS = '3'
    ENUM_UNSUPPORTED_SUBSCRIPTIONREQUESTTYPE = '4'
    ENUM_UNSUPPORTED_MARKETDEPTH = '5'
    ENUM_UNSUPPORTED_MDUPDATETYPE = '6'
    ENUM_UNSUPPORTED_AGGREGATEDBOOK = '7'
    ENUM_UNSUPPORTED_MDENTRYTYPE = '8'
    ENUM_UNSUPPORTED_TRADINGSESSIONID = '9'
    ENUM_UNSUPPORTED_SCOPE = 'A'
    ENUM_UNSUPPORTED_OPENCLOSESETTLEFLAG = 'B'
    ENUM_UNSUPPORTED_MDIMPLICITDELETE = 'C'

class MDEntryOriginator (fields.String) :
    _tag = '282'

class LocationID (fields.String) :
    _tag = '283'

class DeskID (fields.String) :
    _tag = '284'

class DeleteReason (fields.char) :
    _tag = '285'
    ENUM_CANCELATION = '0'
    ENUM_ERROR = '1'

class OpenCloseSettlFlag (fields.MultipleValueString) :
    _tag = '286'
    ENUM_DAILY_OPEN = '0'
    ENUM_SESSION_OPEN = '1'
    ENUM_DELIVERY_SETTLEMENT_ENTRY = '2'
    ENUM_EXPECTED_ENTRY = '3'
    ENUM_ENTRY_FROM_PREVIOUS_BUSINESS_DAY = '4'
    ENUM_THEORETICAL_PRICE_VALUE = '5'

class SellerDays (fields.int) :
    _tag = '287'

class MDEntryBuyer (fields.String) :
    _tag = '288'

class MDEntrySeller (fields.String) :
    _tag = '289'

class MDEntryPositionNo (fields.int) :
    _tag = '290'

class FinancialStatus (fields.MultipleValueString) :
    _tag = '291'
    ENUM_BANKRUPT = '1'
    ENUM_PENDING_DELISTING = '2'

class CorporateAction (fields.MultipleValueString) :
    _tag = '292'
    ENUM_EX_DIVIDEND = 'A'
    ENUM_EX_DISTRIBUTION = 'B'
    ENUM_EX_RIGHTS = 'C'
    ENUM_NEW = 'D'
    ENUM_EX_INTEREST = 'E'

class DefBidSize (fields.Qty) :
    _tag = '293'

class DefOfferSize (fields.Qty) :
    _tag = '294'

class NoQuoteEntries (fields.NumInGroup) :
    _tag = '295'

class NoQuoteSets (fields.NumInGroup) :
    _tag = '296'

class QuoteStatus (fields.int) :
    _tag = '297'
    ENUM_ACCEPTED = 0
    ENUM_CANCELED_FOR_SYMBOL = 1
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

class QuoteCancelType (fields.int) :
    _tag = '298'
    ENUM_CANCEL_FOR_SYMBOL = 1
    ENUM_CANCEL_FOR_SECURITY_TYPE = 2
    ENUM_CANCEL_FOR_UNDERLYING_SYMBOL = 3
    ENUM_CANCEL_ALL_QUOTES = 4

class QuoteEntryID (fields.String) :
    _tag = '299'

class QuoteRejectReason (fields.int) :
    _tag = '300'
    ENUM_UNKNOWN_SYMBOL = 1
    ENUM_EXCHANGE = 2
    ENUM_QUOTE_REQUEST_EXCEEDS_LIMIT = 3
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_UNKNOWN_QUOTE = 5
    ENUM_DUPLICATE_QUOTE = 6
    ENUM_INVALID_BID_ASK_SPREAD = 7
    ENUM_INVALID_PRICE = 8
    ENUM_NOT_AUTHORIZED_TO_QUOTE_SECURITY = 9
    ENUM_OTHER = 99

class QuoteResponseLevel (fields.int) :
    _tag = '301'
    ENUM_NO_ACKNOWLEDGEMENT = 0
    ENUM_ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES = 1
    ENUM_ACKNOWLEDGE_EACH_QUOTE_MESSAGES = 2

class QuoteSetID (fields.String) :
    _tag = '302'

class QuoteRequestType (fields.int) :
    _tag = '303'
    ENUM_MANUAL = 1
    ENUM_AUTOMATIC = 2

class TotNoQuoteEntries (fields.int) :
    _tag = '304'

class UnderlyingSecurityIDSource (fields.String) :
    _tag = '305'

class UnderlyingIssuer (fields.String) :
    _tag = '306'

class UnderlyingSecurityDesc (fields.String) :
    _tag = '307'

class UnderlyingSecurityExchange (fields.Exchange) :
    _tag = '308'

class UnderlyingSecurityID (fields.String) :
    _tag = '309'

class UnderlyingSecurityType (fields.String) :
    _tag = '310'

class UnderlyingSymbol (fields.String) :
    _tag = '311'

class UnderlyingSymbolSfx (fields.String) :
    _tag = '312'

class UnderlyingMaturityMonthYear (fields.MonthYear) :
    _tag = '313'

class UnderlyingPutOrCall (fields.int) :
    _tag = '315'

class UnderlyingStrikePrice (fields.Price) :
    _tag = '316'

class UnderlyingOptAttribute (fields.char) :
    _tag = '317'

class UnderlyingCurrency (fields.Currency) :
    _tag = '318'

class SecurityReqID (fields.String) :
    _tag = '320'

class SecurityRequestType (fields.int) :
    _tag = '321'
    ENUM_REQUEST_SECURITY_IDENTITY_AND_SPECIFICATIONS = 0
    ENUM_REQUEST_SECURITY_IDENTITY_FOR_THE_SPECIFICATIONS_PROVIDED = 1
    ENUM_REQUEST_LIST_SECURITY_TYPES = 2
    ENUM_REQUEST_LIST_SECURITIES = 3

class SecurityResponseID (fields.String) :
    _tag = '322'

class SecurityResponseType (fields.int) :
    _tag = '323'
    ENUM_ACCEPT_SECURITY_PROPOSAL_AS_IS = 1
    ENUM_ACCEPT_SECURITY_PROPOSAL_WITH_REVISIONS_AS_INDICATED_IN_THE_MESSAGE = 2
    ENUM_REJECT_SECURITY_PROPOSAL = 5
    ENUM_CAN_NOT_MATCH_SELECTION_CRITERIA = 6

class SecurityStatusReqID (fields.String) :
    _tag = '324'

class UnsolicitedIndicator (fields.Boolean) :
    _tag = '325'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class SecurityTradingStatus (fields.int) :
    _tag = '326'
    ENUM_OPENING_DELAY = 1
    ENUM_TRADING_HALT = 2
    ENUM_RESUME = 3
    ENUM_NO_OPEN_NO_RESUME = 4
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

class HaltReasonChar (fields.char) :
    _tag = '327'
    ENUM_ORDER_IMBALANCE = 'I'
    ENUM_EQUIPMENT_CHANGEOVER = 'X'
    ENUM_NEWS_PENDING = 'P'
    ENUM_NEWS_DISSEMINATION = 'D'
    ENUM_ORDER_INFLUX = 'E'
    ENUM_ADDITIONAL_INFORMATION = 'M'

class InViewOfCommon (fields.Boolean) :
    _tag = '328'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class DueToRelated (fields.Boolean) :
    _tag = '329'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class BuyVolume (fields.Qty) :
    _tag = '330'

class SellVolume (fields.Qty) :
    _tag = '331'

class HighPx (fields.Price) :
    _tag = '332'

class LowPx (fields.Price) :
    _tag = '333'

class Adjustment (fields.int) :
    _tag = '334'
    ENUM_CANCEL = 1
    ENUM_ERROR = 2
    ENUM_CORRECTION = 3

class TradSesReqID (fields.String) :
    _tag = '335'

class TradingSessionID (fields.String) :
    _tag = '336'

class ContraTrader (fields.String) :
    _tag = '337'

class TradSesMethod (fields.int) :
    _tag = '338'
    ENUM_ELECTRONIC = 1
    ENUM_OPEN_OUTCRY = 2
    ENUM_TWO_PARTY = 3

class TradSesMode (fields.int) :
    _tag = '339'
    ENUM_TESTING = 1
    ENUM_SIMULATED = 2
    ENUM_PRODUCTION = 3

class TradSesStatus (fields.int) :
    _tag = '340'
    ENUM_UNKNOWN = 0
    ENUM_HALTED = 1
    ENUM_OPEN = 2
    ENUM_CLOSED = 3
    ENUM_PRE_OPEN = 4
    ENUM_PRE_CLOSE = 5
    ENUM_REQUEST_REJECTED = 6

class TradSesStartTime (fields.UTCTimestamp) :
    _tag = '341'

class TradSesOpenTime (fields.UTCTimestamp) :
    _tag = '342'

class TradSesPreCloseTime (fields.UTCTimestamp) :
    _tag = '343'

class TradSesCloseTime (fields.UTCTimestamp) :
    _tag = '344'

class TradSesEndTime (fields.UTCTimestamp) :
    _tag = '345'

class NumberOfOrders (fields.int) :
    _tag = '346'

class MessageEncoding (fields.String) :
    _tag = '347'
    ENUM_JIS = 'ISO-2022-JP'
    ENUM_EUC = 'EUC-JP'
    ENUM_FOR_USING_SJIS = 'Shift_JIS'
    ENUM_UNICODE = 'UTF-8'

class EncodedIssuerLen (fields.Length) :
    _tag = '348'

class EncodedIssuer (fields.data) :
    _tag = '349'

class EncodedSecurityDescLen (fields.Length) :
    _tag = '350'

class EncodedSecurityDesc (fields.data) :
    _tag = '351'

class EncodedListExecInstLen (fields.Length) :
    _tag = '352'

class EncodedListExecInst (fields.data) :
    _tag = '353'

class EncodedTextLen (fields.Length) :
    _tag = '354'

class EncodedText (fields.data) :
    _tag = '355'

class EncodedSubjectLen (fields.Length) :
    _tag = '356'

class EncodedSubject (fields.data) :
    _tag = '357'

class EncodedHeadlineLen (fields.Length) :
    _tag = '358'

class EncodedHeadline (fields.data) :
    _tag = '359'

class EncodedAllocTextLen (fields.Length) :
    _tag = '360'

class EncodedAllocText (fields.data) :
    _tag = '361'

class EncodedUnderlyingIssuerLen (fields.Length) :
    _tag = '362'

class EncodedUnderlyingIssuer (fields.data) :
    _tag = '363'

class EncodedUnderlyingSecurityDescLen (fields.Length) :
    _tag = '364'

class EncodedUnderlyingSecurityDesc (fields.data) :
    _tag = '365'

class AllocPrice (fields.Price) :
    _tag = '366'

class QuoteSetValidUntilTime (fields.UTCTimestamp) :
    _tag = '367'

class QuoteEntryRejectReason (fields.int) :
    _tag = '368'

class LastMsgSeqNumProcessed (fields.SeqNum) :
    _tag = '369'

class RefTagID (fields.int) :
    _tag = '371'

class RefMsgType (fields.String) :
    _tag = '372'

class SessionRejectReason (fields.int) :
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
    ENUM_COMPID_PROBLEM = 9
    ENUM_SENDINGTIME_ACCURACY_PROBLEM = 10
    ENUM_INVALID_MSGTYPE = 11
    ENUM_XML_VALIDATION_ERROR = 12
    ENUM_TAG_APPEARS_MORE_THAN_ONCE = 13
    ENUM_TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER = 14
    ENUM_REPEATING_GROUP_FIELDS_OUT_OF_ORDER = 15
    ENUM_INCORRECT_NUMINGROUP_COUNT_FOR_REPEATING_GROUP = 16
    ENUM_NON_DATA_VALUE_INCLUDES_FIELD_DELIMITER = 17
    ENUM_OTHER = 99

class BidRequestTransType (fields.char) :
    _tag = '374'
    ENUM_NEW = 'N'
    ENUM_CANCEL = 'C'

class ContraBroker (fields.String) :
    _tag = '375'

class ComplianceID (fields.String) :
    _tag = '376'

class SolicitedFlag (fields.Boolean) :
    _tag = '377'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class ExecRestatementReason (fields.int) :
    _tag = '378'
    ENUM_GT_CORPORATE_ACTION = 0
    ENUM_GT_RENEWAL = 1
    ENUM_VERBAL_CHANGE = 2
    ENUM_REPRICING_OF_ORDER = 3
    ENUM_BROKER_OPTION = 4
    ENUM_PARTIAL_DECLINE_OF_ORDERQTY = 5
    ENUM_CANCEL_ON_TRADING_HALT = 6
    ENUM_CANCEL_ON_SYSTEM_FAILURE = 7
    ENUM_MARKET = 8
    ENUM_CANCELED_NOT_BEST = 9
    ENUM_WAREHOUSE_RECAP = 10
    ENUM_OTHER = 99

class BusinessRejectRefID (fields.String) :
    _tag = '379'

class BusinessRejectReason (fields.int) :
    _tag = '380'
    ENUM_OTHER = 0
    ENUM_UNKOWN_ID = 1
    ENUM_UNKNOWN_SECURITY = 2
    ENUM_UNSUPPORTED_MESSAGE_TYPE = 3
    ENUM_APPLICATION_NOT_AVAILABLE = 4
    ENUM_CONDITIONALLY_REQUIRED_FIELD_MISSING = 5
    ENUM_NOT_AUTHORIZED = 6
    ENUM_DELIVERTO_FIRM_NOT_AVAILABLE_AT_THIS_TIME = 7

class GrossTradeAmt (fields.Amt) :
    _tag = '381'

class NoContraBrokers (fields.NumInGroup) :
    _tag = '382'

class MaxMessageSize (fields.Length) :
    _tag = '383'

class NoMsgTypes (fields.NumInGroup) :
    _tag = '384'

class MsgDirection (fields.char) :
    _tag = '385'
    ENUM_SEND = 'S'
    ENUM_RECEIVE = 'R'

class NoTradingSessions (fields.NumInGroup) :
    _tag = '386'

class TotalVolumeTraded (fields.Qty) :
    _tag = '387'

class DiscretionInst (fields.char) :
    _tag = '388'
    ENUM_RELATED_TO_DISPLAYED_PRICE = '0'
    ENUM_RELATED_TO_MARKET_PRICE = '1'
    ENUM_RELATED_TO_PRIMARY_PRICE = '2'
    ENUM_RELATED_TO_LOCAL_PRIMARY_PRICE = '3'
    ENUM_RELATED_TO_MIDPOINT_PRICE = '4'
    ENUM_RELATED_TO_LAST_TRADE_PRICE = '5'
    ENUM_RELATED_TO_VWAP = '6'

class DiscretionOffsetValue (fields.float) :
    _tag = '389'

class BidID (fields.String) :
    _tag = '390'

class ClientBidID (fields.String) :
    _tag = '391'

class ListName (fields.String) :
    _tag = '392'

class TotNoRelatedSym (fields.int) :
    _tag = '393'

class BidType (fields.int) :
    _tag = '394'
    ENUM_NON_DISCLOSED_STYLE = 1
    ENUM_DISCLOSED_STYLE = 2
    ENUM_NO_BIDDING_PROCESS = 3

class NumTickets (fields.int) :
    _tag = '395'

class SideValue1 (fields.Amt) :
    _tag = '396'

class SideValue2 (fields.Amt) :
    _tag = '397'

class NoBidDescriptors (fields.NumInGroup) :
    _tag = '398'

class BidDescriptorType (fields.int) :
    _tag = '399'
    ENUM_SECTOR = 1
    ENUM_COUNTRY = 2
    ENUM_INDEX = 3

class BidDescriptor (fields.String) :
    _tag = '400'

class SideValueInd (fields.int) :
    _tag = '401'
    ENUM_SIDEVALUE1 = 1
    ENUM_SIDEVALUE_2 = 2

class LiquidityPctLow (fields.Percentage) :
    _tag = '402'

class LiquidityPctHigh (fields.Percentage) :
    _tag = '403'

class LiquidityValue (fields.Amt) :
    _tag = '404'

class EFPTrackingError (fields.Percentage) :
    _tag = '405'

class FairValue (fields.Amt) :
    _tag = '406'

class OutsideIndexPct (fields.Percentage) :
    _tag = '407'

class ValueOfFutures (fields.Amt) :
    _tag = '408'

class LiquidityIndType (fields.int) :
    _tag = '409'
    ENUM_5DAY_MOVING_AVERAGE = 1
    ENUM_20_DAY_MOVING_AVERAGE = 2
    ENUM_NORMAL_MARKET_SIZE = 3
    ENUM_OTHER = 4

class WtAverageLiquidity (fields.Percentage) :
    _tag = '410'

class ExchangeForPhysical (fields.Boolean) :
    _tag = '411'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class OutMainCntryUIndex (fields.Amt) :
    _tag = '412'

class CrossPercent (fields.Percentage) :
    _tag = '413'

class ProgRptReqs (fields.int) :
    _tag = '414'
    ENUM_BUYSIDE_EXPLICITLY_REQUESTS_STATUS_USING_STATUSREQUEST = 1
    ENUM_SELLSIDE_PERIODICALLY_SENDS_STATUS_USING_LISTSTATUS_PERIOD_OPTIONALLY_SPECIFIED_IN_PROGRESSPERIOD = 2
    ENUM_REAL_TIME_EXECUTION_REPORTS = 3

class ProgPeriodInterval (fields.int) :
    _tag = '415'

class IncTaxInd (fields.int) :
    _tag = '416'
    ENUM_NET = 1
    ENUM_GROSS = 2

class NumBidders (fields.int) :
    _tag = '417'

class BidTradeType (fields.char) :
    _tag = '418'
    ENUM_RISK_TRADE = 'R'
    ENUM_VWAP_GUARANTEE = 'G'
    ENUM_AGENCY = 'A'
    ENUM_GUARANTEED_CLOSE = 'J'

class BasisPxType (fields.char) :
    _tag = '419'
    ENUM_CLOSING_PRICE_AT_MORNING_SESSION = '2'
    ENUM_CLOSING_PRICE = '3'
    ENUM_CURRENT_PRICE = '4'
    ENUM_SQ = '5'
    ENUM_VWAP_THROUGH_A_DAY = '6'
    ENUM_VWAP_THROUGH_A_MORNING_SESSION = '7'
    ENUM_VWAP_THROUGH_AN_AFTERNOON_SESSION = '8'
    ENUM_VWAP_THROUGH_A_DAY_EXCEPT_YORI = '9'
    ENUM_VWAP_THROUGH_A_MORNING_SESSION_EXCEPT_YORI = 'A'
    ENUM_VWAP_THROUGH_AN_AFTERNOON_SESSION_EXCEPT_YORI = 'B'
    ENUM_STRIKE = 'C'
    ENUM_OPEN = 'D'
    ENUM_OTHERS = 'Z'

class NoBidComponents (fields.NumInGroup) :
    _tag = '420'

class Country (fields.Country) :
    _tag = '421'

class TotNoStrikes (fields.int) :
    _tag = '422'

class PriceType (fields.int) :
    _tag = '423'
    ENUM_PERCENTAGE = 1
    ENUM_PER_UNIT = 2
    ENUM_FIXED_AMOUNT = 3
    ENUM_DISCOUNT_PERCENTAGE_POINTS_BELOW_PAR = 4
    ENUM_PREMIUM_PERCENTAGE_POINTS_OVER_PAR = 5
    ENUM_SPREAD = 6
    ENUM_TED_PRICE = 7
    ENUM_TED_YIELD = 8
    ENUM_YIELD = 9
    ENUM_FIXED_CABINET_TRADE_PRICE = 10
    ENUM_VARIABLE_CABINET_TRADE_PRICE = 11

class DayOrderQty (fields.Qty) :
    _tag = '424'

class DayCumQty (fields.Qty) :
    _tag = '425'

class DayAvgPx (fields.Price) :
    _tag = '426'

class GTBookingInst (fields.int) :
    _tag = '427'
    ENUM_BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION = 0
    ENUM_ACCUMULATE_EXECUTIONS_UNTIL_ORDER_IS_FILLED_OR_EXPIRES = 1
    ENUM_ACCUMULATE_UNTIL_VERBALLY_NOTIFIED_OTHERWISE = 2

class NoStrikes (fields.NumInGroup) :
    _tag = '428'

class ListStatusType (fields.int) :
    _tag = '429'
    ENUM_ACK = 1
    ENUM_RESPONSE = 2
    ENUM_TIMED = 3
    ENUM_EXECSTARTED = 4
    ENUM_ALLDONE = 5
    ENUM_ALERT = 6

class NetGrossInd (fields.int) :
    _tag = '430'
    ENUM_NET = 1
    ENUM_GROSS = 2

class ListOrderStatus (fields.int) :
    _tag = '431'
    ENUM_INBIDDINGPROCESS = 1
    ENUM_RECEIVEDFOREXECUTION = 2
    ENUM_EXECUTING = 3
    ENUM_CANCELING = 4
    ENUM_ALERT = 5
    ENUM_ALL_DONE = 6
    ENUM_REJECT = 7

class ExpireDate (fields.LocalMktDate) :
    _tag = '432'

class ListExecInstType (fields.char) :
    _tag = '433'
    ENUM_IMMEDIATE = '1'
    ENUM_WAIT_FOR_EXECUTE_INSTRUCTION = '2'
    ENUM_EXCHANGE_SWITCH_CIV_ORDER_SELL_DRIVEN = '3'
    ENUM_EXCHANGE_SWITCH_CIV_ORDER_BUY_DRIVEN_CASH_TOP_UP = '4'
    ENUM_EXCHANGE_SWITCH_CIV_ORDER_BUY_DRIVEN_CASH_WITHDRAW = '5'

class CxlRejResponseTo (fields.char) :
    _tag = '434'
    ENUM_ORDER_CANCEL_REQUEST = '1'
    ENUM_ORDER_CANCEL_REPLACE_REQUEST = '2'

class UnderlyingCouponRate (fields.Percentage) :
    _tag = '435'

class UnderlyingContractMultiplier (fields.float) :
    _tag = '436'

class ContraTradeQty (fields.Qty) :
    _tag = '437'

class ContraTradeTime (fields.UTCTimestamp) :
    _tag = '438'

class LiquidityNumSecurities (fields.int) :
    _tag = '441'

class MultiLegReportingType (fields.char) :
    _tag = '442'
    ENUM_SINGLE_SECURITY = '1'
    ENUM_INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY = '2'
    ENUM_MULTI_LEG_SECURITY = '3'

class StrikeTime (fields.UTCTimestamp) :
    _tag = '443'

class ListStatusText (fields.String) :
    _tag = '444'

class EncodedListStatusTextLen (fields.Length) :
    _tag = '445'

class EncodedListStatusText (fields.data) :
    _tag = '446'

class PartyIDSource (fields.char) :
    _tag = '447'
    ENUM_BIC = 'B'
    ENUM_GENERALLY_ACCEPTED_MARKET_PARTICIPANT_IDENTIFIER = 'C'
    ENUM_PROPRIETARY_CUSTOM_CODE = 'D'
    ENUM_ISO_COUNTRY_CODE = 'E'
    ENUM_SETTLEMENT_ENTITY_LOCATION = 'F'
    ENUM_MIC = 'G'
    ENUM_CSD_PARTICIPANT_MEMBER_CODE = 'H'
    ENUM_KOREAN_INVESTOR_ID = '1'
    ENUM_TAIWANESE_QUALIFIED_FOREIGN_INVESTOR_ID_QFII = '2'
    ENUM_TAIWANESE_TRADING_ACCOUNT = '3'
    ENUM_MALAYSIAN_CENTRAL_DEPOSITORY = '4'
    ENUM_CHINESE_B_SHARE = '5'
    ENUM_UK_NATIONAL_INSURANCE_OR_PENSION_NUMBER = '6'
    ENUM_US_SOCIAL_SECURITY_NUMBER = '7'
    ENUM_US_EMPLOYER_IDENTIFICATION_NUMBER = '8'
    ENUM_AUSTRALIAN_BUSINESS_NUMBER = '9'
    ENUM_AUSTRALIAN_TAX_FILE_NUMBER = 'A'
    ENUM_DIRECTED_BROKER_THREE_CHARACTER_ACRONYM_AS_DEFINED_IN_ISITC_ETC_BEST_PRACTICE_GUIDELINES_DOCUMENT = 'I'

class PartyID (fields.String) :
    _tag = '448'

class NetChgPrevDay (fields.PriceOffset) :
    _tag = '451'

class PartyRole (fields.int) :
    _tag = '452'
    ENUM_EXECUTING_FIRM = 1
    ENUM_BROKER_OF_CREDIT = 2
    ENUM_CLIENT_ID = 3
    ENUM_CLEARING_FIRM = 4
    ENUM_INVESTOR_ID = 5
    ENUM_INTRODUCING_FIRM = 6
    ENUM_ENTERING_FIRM = 7
    ENUM_LOCATE_LENDING_FIRM = 8
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
    ENUM_BUYER_SELLER = 27
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

class NoPartyIDs (fields.NumInGroup) :
    _tag = '453'

class NoSecurityAltID (fields.NumInGroup) :
    _tag = '454'

class SecurityAltID (fields.String) :
    _tag = '455'

class SecurityAltIDSource (fields.String) :
    _tag = '456'

class NoUnderlyingSecurityAltID (fields.NumInGroup) :
    _tag = '457'

class UnderlyingSecurityAltID (fields.String) :
    _tag = '458'

class UnderlyingSecurityAltIDSource (fields.String) :
    _tag = '459'

class Product (fields.int) :
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

class CFICode (fields.String) :
    _tag = '461'

class UnderlyingProduct (fields.int) :
    _tag = '462'

class UnderlyingCFICode (fields.String) :
    _tag = '463'

class TestMessageIndicator (fields.Boolean) :
    _tag = '464'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class BookingRefID (fields.String) :
    _tag = '466'

class IndividualAllocID (fields.String) :
    _tag = '467'

class RoundingDirection (fields.char) :
    _tag = '468'
    ENUM_ROUND_TO_NEAREST = '0'
    ENUM_ROUND_DOWN = '1'
    ENUM_ROUND_UP = '2'

class RoundingModulus (fields.float) :
    _tag = '469'

class CountryOfIssue (fields.Country) :
    _tag = '470'

class StateOrProvinceOfIssue (fields.String) :
    _tag = '471'

class LocaleOfIssue (fields.String) :
    _tag = '472'

class NoRegistDtls (fields.NumInGroup) :
    _tag = '473'

class MailingDtls (fields.String) :
    _tag = '474'

class InvestorCountryOfResidence (fields.Country) :
    _tag = '475'

class PaymentRef (fields.String) :
    _tag = '476'

class DistribPaymentMethod (fields.int) :
    _tag = '477'
    ENUM_CREST = 1
    ENUM_NSCC = 2
    ENUM_EUROCLEAR = 3
    ENUM_CLEARSTREAM = 4
    ENUM_CHEQUE = 5
    ENUM_TELEGRAPHIC_TRANSFER = 6
    ENUM_FEDWIRE = 7
    ENUM_DIRECT_CREDIT = 8
    ENUM_ACH_CREDIT = 9
    ENUM_BPAY = 10
    ENUM_HIGH_VALUE_CLEARING_SYSTEM = 11
    ENUM_REINVEST_IN_FUND = 12

class CashDistribCurr (fields.Currency) :
    _tag = '478'

class CommCurrency (fields.Currency) :
    _tag = '479'

class CancellationRights (fields.char) :
    _tag = '480'
    ENUM_YES = 'Y'
    ENUM_NO_EXECUTION_ONLY = 'N'
    ENUM_NO_WAIVER_AGREEMENT = 'M'
    ENUM_NO_INSTITUTIONAL = 'O'

class MoneyLaunderingStatus (fields.char) :
    _tag = '481'
    ENUM_PASSED = 'Y'
    ENUM_NOT_CHECKED = 'N'
    ENUM_EXEMPT_BELOW_THE_LIMIT = '1'
    ENUM_EXEMPT_CLIENT_MONEY_TYPE_EXEMPTION = '2'
    ENUM_EXEMPT_AUTHORISED_CREDIT_OR_FINANCIAL_INSTITUTION = '3'

class MailingInst (fields.String) :
    _tag = '482'

class TransBkdTime (fields.UTCTimestamp) :
    _tag = '483'

class ExecPriceType (fields.char) :
    _tag = '484'
    ENUM_BID_PRICE = 'B'
    ENUM_CREATION_PRICE = 'C'
    ENUM_CREATION_PRICE_PLUS_ADJUSTMENT = 'D'
    ENUM_CREATION_PRICE_PLUS_ADJUSTMENT_AMOUNT = 'E'
    ENUM_OFFER_PRICE = 'O'
    ENUM_OFFER_PRICE_MINUS_ADJUSTMENT = 'P'
    ENUM_OFFER_PRICE_MINUS_ADJUSTMENT_AMOUNT = 'Q'
    ENUM_SINGLE_PRICE = 'S'

class ExecPriceAdjustment (fields.float) :
    _tag = '485'

class DateOfBirth (fields.LocalMktDate) :
    _tag = '486'

class TradeReportTransType (fields.int) :
    _tag = '487'

class CardHolderName (fields.String) :
    _tag = '488'

class CardNumber (fields.String) :
    _tag = '489'

class CardExpDate (fields.LocalMktDate) :
    _tag = '490'

class CardIssNum (fields.String) :
    _tag = '491'

class PaymentMethod (fields.int) :
    _tag = '492'
    ENUM_CREST = 1
    ENUM_NSCC = 2
    ENUM_EUROCLEAR = 3
    ENUM_CLEARSTREAM = 4
    ENUM_CHEQUE = 5
    ENUM_TELEGRAPHIC_TRANSFER = 6
    ENUM_FEDWIRE = 7
    ENUM_DEBIT_CARD = 8
    ENUM_DIRECT_DEBIT = 9
    ENUM_DIRECT_CREDIT = 10
    ENUM_CREDIT_CARD = 11
    ENUM_ACH_DEBIT = 12
    ENUM_ACH_CREDIT = 13
    ENUM_BPAY = 14
    ENUM_HIGH_VALUE_CLEARING_SYSTEM = 15

class RegistAcctType (fields.String) :
    _tag = '493'

class Designation (fields.String) :
    _tag = '494'

class TaxAdvantageType (fields.int) :
    _tag = '495'
    ENUM_NONE_NOT_APPLICABLE = 0
    ENUM_MAXI_ISA = 1
    ENUM_TESSA = 2
    ENUM_MINI_CASH_ISA = 3
    ENUM_MINI_STOCKS_AND_SHARES_ISA = 4
    ENUM_MINI_INSURANCE_ISA = 5
    ENUM_CURRENT_YEAR_PAYMENT = 6
    ENUM_PRIOR_YEAR_PAYMENT = 7
    ENUM_ASSET_TRANSFER = 8
    ENUM_EMPLOYEE = 9
    ENUM_EMPLOYEE_CURRENT_YEAR = 10
    ENUM_EMPLOYER = 11
    ENUM_EMPLOYER_CURRENT_YEAR = 12
    ENUM_NON_FUND_PROTOTYPE_IRA = 13
    ENUM_NON_FUND_QUALIFIED_PLAN = 14
    ENUM_DEFINED_CONTRIBUTION_PLAN = 15
    ENUM_INDIVIDUAL_RETIREMENT_ACCOUNT = 16
    ENUM_INDIVIDUAL_RETIREMENT_ACCOUNT_ROLLOVER = 17
    ENUM_KEOGH = 18
    ENUM_PROFIT_SHARING_PLAN = 19
    ENUM_401K = 20
    ENUM_SELF_DIRECTED_IRA = 21
    ENUM_403 = 22
    ENUM_457 = 23
    ENUM_ROTH_IRA_24 = 24
    ENUM_ROTH_IRA_25 = 25
    ENUM_ROTH_CONVERSION_IRA_26 = 26
    ENUM_ROTH_CONVERSION_IRA_27 = 27
    ENUM_EDUCATION_IRA_28 = 28
    ENUM_EDUCATION_IRA_29 = 29

class RegistRejReasonText (fields.String) :
    _tag = '496'

class FundRenewWaiv (fields.char) :
    _tag = '497'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class CashDistribAgentName (fields.String) :
    _tag = '498'

class CashDistribAgentCode (fields.String) :
    _tag = '499'

class CashDistribAgentAcctNumber (fields.String) :
    _tag = '500'

class CashDistribPayRef (fields.String) :
    _tag = '501'

class CashDistribAgentAcctName (fields.String) :
    _tag = '502'

class CardStartDate (fields.LocalMktDate) :
    _tag = '503'

class PaymentDate (fields.LocalMktDate) :
    _tag = '504'

class PaymentRemitterID (fields.String) :
    _tag = '505'

class RegistStatus (fields.char) :
    _tag = '506'
    ENUM_ACCEPTED = 'A'
    ENUM_REJECTED = 'R'
    ENUM_HELD = 'H'
    ENUM_REMINDER_IE_REGISTRATION_INSTRUCTIONS_ARE_STILL_OUTSTANDING = 'N'

class RegistRejReasonCode (fields.int) :
    _tag = '507'
    ENUM_INVALID_UNACCEPTABLE_ACCOUNT_TYPE = 1
    ENUM_INVALID_UNACCEPTABLE_TAX_EXEMPT_TYPE = 2
    ENUM_INVALID_UNACCEPTABLE_OWNERSHIP_TYPE = 3
    ENUM_INVALID_UNACCEPTABLE_NO_REG_DETLS = 4
    ENUM_INVALID_UNACCEPTABLE_REG_SEQ_NO = 5
    ENUM_INVALID_UNACCEPTABLE_REG_DTLS = 6
    ENUM_INVALID_UNACCEPTABLE_MAILING_DTLS = 7
    ENUM_INVALID_UNACCEPTABLE_MAILING_INST = 8
    ENUM_INVALID_UNACCEPTABLE_INVESTOR_ID = 9
    ENUM_INVALID_UNACCEPTABLE_INVESTOR_ID_SOURCE = 10
    ENUM_INVALID_UNACCEPTABLE_DATE_OF_BIRTH = 11
    ENUM_INVALID_UNACCEPTABLE_INVESTOR_COUNTRY_OF_RESIDENCE = 12
    ENUM_INVALID_UNACCEPTABLE_NODISTRIBINSTNS = 13
    ENUM_INVALID_UNACCEPTABLE_DISTRIB_PERCENTAGE = 14
    ENUM_INVALID_UNACCEPTABLE_DISTRIB_PAYMENT_METHOD = 15
    ENUM_INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_ACCT_NAME = 16
    ENUM_INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_CODE = 17
    ENUM_INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_ACCT_NUM = 18
    ENUM_OTHER = 99

class RegistRefID (fields.String) :
    _tag = '508'

class RegistDtls (fields.String) :
    _tag = '509'

class NoDistribInsts (fields.NumInGroup) :
    _tag = '510'

class RegistEmail (fields.String) :
    _tag = '511'

class DistribPercentage (fields.Percentage) :
    _tag = '512'

class RegistID (fields.String) :
    _tag = '513'

class RegistTransType (fields.char) :
    _tag = '514'
    ENUM_NEW = '0'
    ENUM_REPLACE = '1'
    ENUM_CANCEL = '2'

class ExecValuationPoint (fields.UTCTimestamp) :
    _tag = '515'

class OrderPercent (fields.Percentage) :
    _tag = '516'

class OwnershipType (fields.char) :
    _tag = '517'
    ENUM_JOINT_INVESTORS = 'J'
    ENUM_TENANTS_IN_COMMON = 'T'
    ENUM_JOINT_TRUSTEES = '2'

class NoContAmts (fields.NumInGroup) :
    _tag = '518'

class ContAmtType (fields.int) :
    _tag = '519'
    ENUM_COMMISSION_AMOUNT = 1
    ENUM_COMMISSION = 2
    ENUM_INITIAL_CHARGE_AMOUNT = 3
    ENUM_INITIAL_CHARGE = 4
    ENUM_DISCOUNT_AMOUNT = 5
    ENUM_DISCOUNT = 6
    ENUM_DILUTION_LEVY_AMOUNT = 7
    ENUM_DILUTION_LEVY = 8
    ENUM_EXIT_CHARGE_AMOUNT = 9
    ENUM_EXIT_CHARGE = 10
    ENUM_FUND_BASED_RENEWAL_COMMISSION = 11
    ENUM_PROJECTED_FUND_VALUE = 12
    ENUM_FUND_BASED_RENEWAL_COMMISSION_AMOUNT_13 = 13
    ENUM_FUND_BASED_RENEWAL_COMMISSION_AMOUNT_14 = 14
    ENUM_NET_SETTLEMENT_AMOUNT = 15

class ContAmtValue (fields.float) :
    _tag = '520'

class ContAmtCurr (fields.Currency) :
    _tag = '521'

class OwnerType (fields.int) :
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

class PartySubID (fields.String) :
    _tag = '523'

class NestedPartyID (fields.String) :
    _tag = '524'

class NestedPartyIDSource (fields.char) :
    _tag = '525'

class SecondaryClOrdID (fields.String) :
    _tag = '526'

class SecondaryExecID (fields.String) :
    _tag = '527'

class OrderCapacity (fields.char) :
    _tag = '528'
    ENUM_AGENCY = 'A'
    ENUM_PROPRIETARY = 'G'
    ENUM_INDIVIDUAL = 'I'
    ENUM_PRINCIPAL = 'P'
    ENUM_RISKLESS_PRINCIPAL = 'R'
    ENUM_AGENT_FOR_OTHER_MEMBER = 'W'

class OrderRestrictions (fields.MultipleValueString) :
    _tag = '529'
    ENUM_PROGRAM_TRADE = '1'
    ENUM_INDEX_ARBITRAGE = '2'
    ENUM_NON_INDEX_ARBITRAGE = '3'
    ENUM_COMPETING_MARKET_MAKER = '4'
    ENUM_ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_THE_SECURITY = '5'
    ENUM_ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_THE_UNDERLYING_SECURITY_OF_A_DERIVATIVE_SECURITY = '6'
    ENUM_FOREIGN_ENTITY = '7'
    ENUM_EXTERNAL_MARKET_PARTICIPANT = '8'
    ENUM_EXTERNAL_INTER_CONNECTED_MARKET_LINKAGE = '9'
    ENUM_RISKLESS_ARBITRAGE = 'A'

class MassCancelRequestType (fields.char) :
    _tag = '530'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY = '1'
    ENUM_CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    ENUM_CANCEL_ORDERS_FOR_A_PRODUCT = '3'
    ENUM_CANCEL_ORDERS_FOR_A_CFICODE = '4'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITYTYPE = '5'
    ENUM_CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    ENUM_CANCEL_ALL_ORDERS = '7'

class MassCancelResponse (fields.char) :
    _tag = '531'
    ENUM_CANCEL_REQUEST_REJECTED = '0'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY = '1'
    ENUM_CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    ENUM_CANCEL_ORDERS_FOR_A_PRODUCT = '3'
    ENUM_CANCEL_ORDERS_FOR_A_CFICODE = '4'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITYTYPE = '5'
    ENUM_CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    ENUM_CANCEL_ALL_ORDERS = '7'

class MassCancelRejectReason (fields.char) :
    _tag = '532'
    ENUM_MASS_CANCEL_NOT_SUPPORTED = '0'
    ENUM_INVALID_OR_UNKNOWN_SECURITY = '1'
    ENUM_INVALID_OR_UNKNOWN_UNDERLYING = '2'
    ENUM_INVALID_OR_UNKNOWN_PRODUCT = '3'
    ENUM_INVALID_OR_UNKNOWN_CFICODE = '4'
    ENUM_INVALID_OR_UNKNOWN_SECURITY_TYPE = '5'
    ENUM_INVALID_OR_UNKNOWN_TRADING_SESSION = '6'
    ENUM_OTHER = '99'

class TotalAffectedOrders (fields.int) :
    _tag = '533'

class NoAffectedOrders (fields.NumInGroup) :
    _tag = '534'

class AffectedOrderID (fields.String) :
    _tag = '535'

class AffectedSecondaryOrderID (fields.String) :
    _tag = '536'

class QuoteType (fields.int) :
    _tag = '537'
    ENUM_INDICATIVE = 0
    ENUM_TRADEABLE = 1
    ENUM_RESTRICTED_TRADEABLE = 2
    ENUM_COUNTER = 3

class NestedPartyRole (fields.int) :
    _tag = '538'

class NoNestedPartyIDs (fields.NumInGroup) :
    _tag = '539'

class TotalAccruedInterestAmt (fields.Amt) :
    _tag = '540'

class MaturityDate (fields.LocalMktDate) :
    _tag = '541'

class UnderlyingMaturityDate (fields.LocalMktDate) :
    _tag = '542'

class InstrRegistry (fields.String) :
    _tag = '543'

class CashMargin (fields.char) :
    _tag = '544'
    ENUM_CASH = '1'
    ENUM_MARGIN_OPEN = '2'
    ENUM_MARGIN_CLOSE = '3'

class NestedPartySubID (fields.String) :
    _tag = '545'

class Scope (fields.MultipleValueString) :
    _tag = '546'
    ENUM_LOCAL = '1'
    ENUM_NATIONAL = '2'
    ENUM_GLOBAL = '3'

class MDImplicitDelete (fields.Boolean) :
    _tag = '547'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class CrossID (fields.String) :
    _tag = '548'

class CrossType (fields.int) :
    _tag = '549'
    ENUM_CROSS_TRADE_WHICH_IS_EXECUTED_COMPLETELY_OR_NOT_BOTH_SIDES_ARE_TREATED_IN_THE_SAME_MANNER_THIS_IS_EQUIVALENT_TO_AN_ALL_OR_NONE = 1
    ENUM_CROSS_TRADE_WHICH_IS_EXECUTED_PARTIALLY_AND_THE_REST_IS_CANCELLED_ONE_SIDE_IS_FULLY_EXECUTED_THE_OTHER_SIDE_IS_PARTIALLY_EXECUTED_WITH_THE_REMAINDER_BEING_CANCELLED_THIS_IS_EQUIVALENT_TO_AN_IMMEDIATE_OR_CANCEL_ON_THE_OTHER_SIDE_NOTE_THE_CROSSPRIORITZATION = 2
    ENUM_CROSS_TRADE_WHICH_IS_PARTIALLY_EXECUTED_WITH_THE_UNFILLED_PORTIONS_REMAINING_ACTIVE_ONE_SIDE_OF_THE_CROSS_IS_FULLY_EXECUTED = 3
    ENUM_CROSS_TRADE_IS_EXECUTED_WITH_EXISTING_ORDERS_WITH_THE_SAME_PRICE_IN_THE_CASE_OTHER_ORDERS_EXIST_WITH_THE_SAME_PRICE_THE_QUANTITY_OF_THE_CROSS_IS_EXECUTED_AGAINST_THE_EXISTING_ORDERS_AND_QUOTES_THE_REMAINDER_OF_THE_CROSS_IS_EXECUTED_AGAINST_THE_OTHER_SIDE_OF_THE_CROSS_THE_TWO_SIDES_POTENTIALLY_HAVE_DIFFERENT_QUANTITIES = 4

class CrossPrioritization (fields.int) :
    _tag = '550'
    ENUM_NONE = 0
    ENUM_BUY_SIDE_IS_PRIORITIZED = 1
    ENUM_SELL_SIDE_IS_PRIORITIZED = 2

class OrigCrossID (fields.String) :
    _tag = '551'

class NoSides (fields.NumInGroup) :
    _tag = '552'
    ENUM_ONE_SIDE = 1
    ENUM_BOTH_SIDES = 2

class Username (fields.String) :
    _tag = '553'

class Password (fields.String) :
    _tag = '554'

class NoLegs (fields.NumInGroup) :
    _tag = '555'

class LegCurrency (fields.Currency) :
    _tag = '556'

class TotNoSecurityTypes (fields.int) :
    _tag = '557'

class NoSecurityTypes (fields.NumInGroup) :
    _tag = '558'

class SecurityListRequestType (fields.int) :
    _tag = '559'
    ENUM_SYMBOL = 0
    ENUM_SECURITYTYPE_AND_OR_CFICODE = 1
    ENUM_PRODUCT = 2
    ENUM_TRADINGSESSIONID = 3
    ENUM_ALL_SECURITIES = 4

class SecurityRequestResult (fields.int) :
    _tag = '560'
    ENUM_VALID_REQUEST = 0
    ENUM_INVALID_OR_UNSUPPORTED_REQUEST = 1
    ENUM_NO_INSTRUMENTS_FOUND_THAT_MATCH_SELECTION_CRITERIA = 2
    ENUM_NOT_AUTHORIZED_TO_RETRIEVE_INSTRUMENT_DATA = 3
    ENUM_INSTRUMENT_DATA_TEMPORARILY_UNAVAILABLE = 4
    ENUM_REQUEST_FOR_INSTRUMENT_DATA_NOT_SUPPORTED = 5

class RoundLot (fields.Qty) :
    _tag = '561'

class MinTradeVol (fields.Qty) :
    _tag = '562'

class MultiLegRptTypeReq (fields.int) :
    _tag = '563'
    ENUM_REPORT_BY_MULITLEG_SECURITY_ONLY = 0
    ENUM_REPORT_BY_MULTILEG_SECURITY_AND_BY_INSTRUMENT_LEGS_BELONGING_TO_THE_MULTILEG_SECURITY = 1
    ENUM_REPORT_BY_INSTRUMENT_LEGS_BELONGING_TO_THE_MULTILEG_SECURITY_ONLY = 2

class LegPositionEffect (fields.char) :
    _tag = '564'

class LegCoveredOrUncovered (fields.int) :
    _tag = '565'

class LegPrice (fields.Price) :
    _tag = '566'

class TradSesStatusRejReason (fields.int) :
    _tag = '567'
    ENUM_UNKNOWN_OR_INVALID_TRADINGSESSIONID = 1
    ENUM_OTHER = 99

class TradeRequestID (fields.String) :
    _tag = '568'

class TradeRequestType (fields.int) :
    _tag = '569'
    ENUM_ALL_TRADES = 0
    ENUM_MATCHED_TRADES_MATCHING_CRITERIA_PROVIDED_ON_REQUEST = 1
    ENUM_UNMATCHED_TRADES_THAT_MATCH_CRITERIA = 2
    ENUM_UNREPORTED_TRADES_THAT_MATCH_CRITERIA = 3
    ENUM_ADVISORIES_THAT_MATCH_CRITERIA = 4

class PreviouslyReported (fields.Boolean) :
    _tag = '570'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class TradeReportID (fields.String) :
    _tag = '571'

class TradeReportRefID (fields.String) :
    _tag = '572'

class MatchStatus (fields.char) :
    _tag = '573'
    ENUM_COMPARED_MATCHED_OR_AFFIRMED = '0'
    ENUM_UNCOMPARED_UNMATCHED_OR_UNAFFIRMED = '1'
    ENUM_ADVISORY_OR_ALERT = '2'

class MatchType (fields.String) :
    _tag = '574'
    ENUM_EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_FOUR_BADGES_AND_EXECUTION_TIME = 'A1'
    ENUM_EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_FOUR_BADGES = 'A2'
    ENUM_EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_TWO_BADGES_AND_EXECUTION_TIME = 'A3'
    ENUM_EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_TWO_BADGES = 'A4'
    ENUM_EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_EXECUTION_TIME = 'A5'
    ENUM_COMPARED_RECORDS_RESULTING_FROM_STAMPED_ADVISORIES_OR_SPECIALIST_ACCEPTS_PAIR_OFFS = 'AQ'
    ENUM_SUMMARIZED_MATCH_USING_A1_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = 'S1'
    ENUM_SUMMARIZED_MATCH_USING_A2_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = 'S2'
    ENUM_SUMMARIZED_MATCH_USING_A3_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = 'S3'
    ENUM_SUMMARIZED_MATCH_USING_A4_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = 'S4'
    ENUM_SUMMARIZED_MATCH_USING_A5_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = 'S5'
    ENUM_EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_MINUS_BADGES_AND_TIMES_ACT_M1_MATCH = 'M1'
    ENUM_SUMMARIZED_MATCH_MINUS_BADGES_AND_TIMES_ACT_M2_MATCH = 'M2'
    ENUM_OCS_LOCKED_IN_NON_ACT = 'MT'
    ENUM_ACT_ACCEPTED_TRADE = 'M3'
    ENUM_ACT_DEFAULT_TRADE = 'M4'
    ENUM_ACT_DEFAULT_AFTER_M2 = 'M5'
    ENUM_ACT_M6_MATCH = 'M6'

class OddLot (fields.Boolean) :
    _tag = '575'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class NoClearingInstructions (fields.NumInGroup) :
    _tag = '576'

class ClearingInstruction (fields.int) :
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
    ENUM_QUALIFIED_SERVICE_REPRESENTATIVE = 11
    ENUM_CUSTOMER_TRADE = 12
    ENUM_SELF_CLEARING = 13

class TradeInputSource (fields.String) :
    _tag = '578'

class TradeInputDevice (fields.String) :
    _tag = '579'

class NoDates (fields.NumInGroup) :
    _tag = '580'

class AccountType (fields.int) :
    _tag = '581'
    ENUM_ACCOUNT_IS_CARRIED_ON_CUSTOMER_SIDE_OF_BOOKS = 1
    ENUM_ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS = 2
    ENUM_HOUSE_TRADER = 3
    ENUM_FLOOR_TRADER = 4
    ENUM_ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS_AND_IS_CROSS_MARGINED = 6
    ENUM_ACCOUNT_IS_HOUSE_TRADER_AND_IS_CROSS_MARGINED = 7
    ENUM_JOINT_BACKOFFICE_ACCOUNT = 8

class CustOrderCapacity (fields.int) :
    _tag = '582'
    ENUM_MEMBER_TRADING_FOR_THEIR_OWN_ACCOUNT = 1
    ENUM_CLEARING_FIRM_TRADING_FOR_ITS_PROPRIETARY_ACCOUNT = 2
    ENUM_MEMBER_TRADING_FOR_ANOTHER_MEMBER = 3
    ENUM_ALL_OTHER = 4

class ClOrdLinkID (fields.String) :
    _tag = '583'

class MassStatusReqID (fields.String) :
    _tag = '584'

class MassStatusReqType (fields.int) :
    _tag = '585'
    ENUM_STATUS_FOR_ORDERS_FOR_A_SECURITY = 1
    ENUM_STATUS_FOR_ORDERS_FOR_AN_UNDERLYING_SECURITY = 2
    ENUM_STATUS_FOR_ORDERS_FOR_A_PRODUCT = 3
    ENUM_STATUS_FOR_ORDERS_FOR_A_CFICODE = 4
    ENUM_STATUS_FOR_ORDERS_FOR_A_SECURITYTYPE = 5
    ENUM_STATUS_FOR_ORDERS_FOR_A_TRADING_SESSION = 6
    ENUM_STATUS_FOR_ALL_ORDERS = 7
    ENUM_STATUS_FOR_ORDERS_FOR_A_PARTYID = 8

class OrigOrdModTime (fields.UTCTimestamp) :
    _tag = '586'

class LegSettlType (fields.char) :
    _tag = '587'

class LegSettlDate (fields.LocalMktDate) :
    _tag = '588'

class DayBookingInst (fields.char) :
    _tag = '589'
    ENUM_CAN_TRIGGER_BOOKING_WITHOUT_REFERENCE_TO_THE_ORDER_INITIATOR = '0'
    ENUM_SPEAK_WITH_ORDER_INITIATOR_BEFORE_BOOKING = '1'
    ENUM_ACCUMULATE = '2'

class BookingUnit (fields.char) :
    _tag = '590'
    ENUM_EACH_PARTIAL_EXECUTION_IS_A_BOOKABLE_UNIT = '0'
    ENUM_AGGREGATE_PARTIAL_EXECUTIONS_ON_THIS_ORDER_AND_BOOK_ONE_TRADE_PER_ORDER = '1'
    ENUM_AGGREGATE_EXECUTIONS_FOR_THIS_SYMBOL_SIDE_AND_SETTLEMENT_DATE = '2'

class PreallocMethod (fields.char) :
    _tag = '591'
    ENUM_PRO_RATA = '0'
    ENUM_DO_NOT_PRO_RATA_DISCUSS_FIRST = '1'

class UnderlyingCountryOfIssue (fields.Country) :
    _tag = '592'

class UnderlyingStateOrProvinceOfIssue (fields.String) :
    _tag = '593'

class UnderlyingLocaleOfIssue (fields.String) :
    _tag = '594'

class UnderlyingInstrRegistry (fields.String) :
    _tag = '595'

class LegCountryOfIssue (fields.Country) :
    _tag = '596'

class LegStateOrProvinceOfIssue (fields.String) :
    _tag = '597'

class LegLocaleOfIssue (fields.String) :
    _tag = '598'

class LegInstrRegistry (fields.String) :
    _tag = '599'

class LegSymbol (fields.String) :
    _tag = '600'

class LegSymbolSfx (fields.String) :
    _tag = '601'

class LegSecurityID (fields.String) :
    _tag = '602'

class LegSecurityIDSource (fields.String) :
    _tag = '603'

class NoLegSecurityAltID (fields.NumInGroup) :
    _tag = '604'

class LegSecurityAltID (fields.String) :
    _tag = '605'

class LegSecurityAltIDSource (fields.String) :
    _tag = '606'

class LegProduct (fields.int) :
    _tag = '607'

class LegCFICode (fields.String) :
    _tag = '608'

class LegSecurityType (fields.String) :
    _tag = '609'

class LegMaturityMonthYear (fields.MonthYear) :
    _tag = '610'

class LegMaturityDate (fields.LocalMktDate) :
    _tag = '611'

class LegStrikePrice (fields.Price) :
    _tag = '612'

class LegOptAttribute (fields.char) :
    _tag = '613'

class LegContractMultiplier (fields.float) :
    _tag = '614'

class LegCouponRate (fields.Percentage) :
    _tag = '615'

class LegSecurityExchange (fields.Exchange) :
    _tag = '616'

class LegIssuer (fields.String) :
    _tag = '617'

class EncodedLegIssuerLen (fields.Length) :
    _tag = '618'

class EncodedLegIssuer (fields.data) :
    _tag = '619'

class LegSecurityDesc (fields.String) :
    _tag = '620'

class EncodedLegSecurityDescLen (fields.Length) :
    _tag = '621'

class EncodedLegSecurityDesc (fields.data) :
    _tag = '622'

class LegRatioQty (fields.float) :
    _tag = '623'

class LegSide (fields.char) :
    _tag = '624'

class TradingSessionSubID (fields.String) :
    _tag = '625'

class AllocType (fields.int) :
    _tag = '626'
    ENUM_CALCULATED = 1
    ENUM_PRELIMINARY = 2
    ENUM_READY_TO_BOOK = 5
    ENUM_WAREHOUSE_INSTRUCTION = 7
    ENUM_REQUEST_TO_INTERMEDIARY = 8

class NoHops (fields.NumInGroup) :
    _tag = '627'

class HopCompID (fields.String) :
    _tag = '628'

class HopSendingTime (fields.UTCTimestamp) :
    _tag = '629'

class HopRefID (fields.SeqNum) :
    _tag = '630'

class MidPx (fields.Price) :
    _tag = '631'

class BidYield (fields.Percentage) :
    _tag = '632'

class MidYield (fields.Percentage) :
    _tag = '633'

class OfferYield (fields.Percentage) :
    _tag = '634'

class ClearingFeeIndicator (fields.String) :
    _tag = '635'
    ENUM_CBOE_MEMBER = 'B'
    ENUM_NON_MEMBER_AND_CUSTOMER = 'C'
    ENUM_EQUITY_MEMBER_AND_CLEARING_MEMBER = 'E'
    ENUM_FULL_AND_ASSOCIATE_MEMBER_TRADING_FOR_OWN_ACCOUNT_AND_AS_FLOOR_BROKERS = 'F'
    ENUM_106H_AND_106J_FIRMS = 'H'
    ENUM_GIM_IDEM_AND_COM_MEMBERSHIP_INTEREST_HOLDERS = 'I'
    ENUM_LESSEE_AND_106F_EMPLOYEES = 'L'
    ENUM_ALL_OTHER_OWNERSHIP_TYPES = 'M'
    ENUM_1ST_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '1'
    ENUM_2ND_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '2'
    ENUM_3RD_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '3'
    ENUM_4TH_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '4'
    ENUM_5TH_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '5'
    ENUM_6TH_YEAR_AND_BEYOND_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '9'

class WorkingIndicator (fields.Boolean) :
    _tag = '636'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class LegLastPx (fields.Price) :
    _tag = '637'

class PriorityIndicator (fields.int) :
    _tag = '638'
    ENUM_PRIORITY_UNCHANGED = 0
    ENUM_LOST_PRIORITY_AS_RESULT_OF_ORDER_CHANGE = 1

class PriceImprovement (fields.PriceOffset) :
    _tag = '639'

class Price2 (fields.Price) :
    _tag = '640'

class LastForwardPoints2 (fields.PriceOffset) :
    _tag = '641'

class BidForwardPoints2 (fields.PriceOffset) :
    _tag = '642'

class OfferForwardPoints2 (fields.PriceOffset) :
    _tag = '643'

class RFQReqID (fields.String) :
    _tag = '644'

class MktBidPx (fields.Price) :
    _tag = '645'

class MktOfferPx (fields.Price) :
    _tag = '646'

class MinBidSize (fields.Qty) :
    _tag = '647'

class MinOfferSize (fields.Qty) :
    _tag = '648'

class QuoteStatusReqID (fields.String) :
    _tag = '649'

class LegalConfirm (fields.Boolean) :
    _tag = '650'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class UnderlyingLastPx (fields.Price) :
    _tag = '651'

class UnderlyingLastQty (fields.Qty) :
    _tag = '652'

class LegRefID (fields.String) :
    _tag = '654'

class ContraLegRefID (fields.String) :
    _tag = '655'

class SettlCurrBidFxRate (fields.float) :
    _tag = '656'

class SettlCurrOfferFxRate (fields.float) :
    _tag = '657'

class QuoteRequestRejectReason (fields.int) :
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

class SideComplianceID (fields.String) :
    _tag = '659'

class AcctIDSource (fields.int) :
    _tag = '660'
    ENUM_BIC = 1
    ENUM_SID_CODE = 2
    ENUM_TFM = 3
    ENUM_OMGEO = 4
    ENUM_DTCC_CODE = 5
    ENUM_OTHER = 99

class AllocAcctIDSource (fields.int) :
    _tag = '661'

class BenchmarkPrice (fields.Price) :
    _tag = '662'

class BenchmarkPriceType (fields.int) :
    _tag = '663'

class ConfirmID (fields.String) :
    _tag = '664'

class ConfirmStatus (fields.int) :
    _tag = '665'
    ENUM_RECEIVED = 1
    ENUM_MISMATCHED_ACCOUNT = 2
    ENUM_MISSING_SETTLEMENT_INSTRUCTIONS = 3
    ENUM_CONFIRMED = 4
    ENUM_REQUEST_REJECTED = 5

class ConfirmTransType (fields.int) :
    _tag = '666'
    ENUM_NEW = 0
    ENUM_REPLACE = 1
    ENUM_CANCEL = 2

class ContractSettlMonth (fields.MonthYear) :
    _tag = '667'

class DeliveryForm (fields.int) :
    _tag = '668'
    ENUM_BOOKENTRY = 1
    ENUM_BEARER = 2

class LastParPx (fields.Price) :
    _tag = '669'

class NoLegAllocs (fields.NumInGroup) :
    _tag = '670'

class LegAllocAccount (fields.String) :
    _tag = '671'

class LegIndividualAllocID (fields.String) :
    _tag = '672'

class LegAllocQty (fields.Qty) :
    _tag = '673'

class LegAllocAcctIDSource (fields.String) :
    _tag = '674'

class LegSettlCurrency (fields.Currency) :
    _tag = '675'

class LegBenchmarkCurveCurrency (fields.Currency) :
    _tag = '676'

class LegBenchmarkCurveName (fields.String) :
    _tag = '677'

class LegBenchmarkCurvePoint (fields.String) :
    _tag = '678'

class LegBenchmarkPrice (fields.Price) :
    _tag = '679'

class LegBenchmarkPriceType (fields.int) :
    _tag = '680'

class LegBidPx (fields.Price) :
    _tag = '681'

class LegIOIQty (fields.String) :
    _tag = '682'

class NoLegStipulations (fields.NumInGroup) :
    _tag = '683'

class LegOfferPx (fields.Price) :
    _tag = '684'

class LegPriceType (fields.int) :
    _tag = '686'

class LegQty (fields.Qty) :
    _tag = '687'

class LegStipulationType (fields.String) :
    _tag = '688'

class LegStipulationValue (fields.String) :
    _tag = '689'

class LegSwapType (fields.int) :
    _tag = '690'
    ENUM_PAR_FOR_PAR = 1
    ENUM_MODIFIED_DURATION = 2
    ENUM_RISK = 4
    ENUM_PROCEEDS = 5

class Pool (fields.String) :
    _tag = '691'

class QuotePriceType (fields.int) :
    _tag = '692'
    ENUM_PERCENT = 1
    ENUM_PER_SHARE = 2
    ENUM_FIXED_AMOUNT = 3
    ENUM_DISCOUNT_PERCENTAGE_POINTS_BELOW_PAR = 4
    ENUM_PREMIUM_PERCENTAGE_POINTS_OVER_PAR = 5
    ENUM_BASIS_POINTS_RELATIVE_TO_BENCHMARK = 6
    ENUM_TED_PRICE = 7
    ENUM_TED_YIELD = 8
    ENUM_YIELD_SPREAD = 9
    ENUM_YIELD = 10

class QuoteRespID (fields.String) :
    _tag = '693'

class QuoteRespType (fields.int) :
    _tag = '694'
    ENUM_HIT_LIFT = 1
    ENUM_COUNTER = 2
    ENUM_EXPIRED = 3
    ENUM_COVER = 4
    ENUM_DONE_AWAY = 5
    ENUM_PASS = 6

class QuoteQualifier (fields.char) :
    _tag = '695'

class YieldRedemptionDate (fields.LocalMktDate) :
    _tag = '696'

class YieldRedemptionPrice (fields.Price) :
    _tag = '697'

class YieldRedemptionPriceType (fields.int) :
    _tag = '698'

class BenchmarkSecurityID (fields.String) :
    _tag = '699'

class ReversalIndicator (fields.Boolean) :
    _tag = '700'

class YieldCalcDate (fields.LocalMktDate) :
    _tag = '701'

class NoPositions (fields.NumInGroup) :
    _tag = '702'

class PosType (fields.String) :
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

class LongQty (fields.Qty) :
    _tag = '704'

class ShortQty (fields.Qty) :
    _tag = '705'

class PosQtyStatus (fields.int) :
    _tag = '706'
    ENUM_SUBMITTED = 0
    ENUM_ACCEPTED = 1
    ENUM_REJECTED = 2

class PosAmtType (fields.String) :
    _tag = '707'
    ENUM_FINAL_MARK_TO_MARKET_AMOUNT = 'FMTM'
    ENUM_INCREMENTAL_MARK_TO_MARKET_AMOUNT = 'IMTM'
    ENUM_TRADE_VARIATION_AMOUNT = 'TVAR'
    ENUM_START_OF_DAY_MARK_TO_MARKET_AMOUNT = 'SMTM'
    ENUM_PREMIUM_AMOUNT = 'PREM'
    ENUM_CASH_RESIDUAL_AMOUNT = 'CRES'
    ENUM_CASH_AMOUNT = 'CASH'
    ENUM_VALUE_ADJUSTED_AMOUNT = 'VADJ'

class PosAmt (fields.Amt) :
    _tag = '708'

class PosTransType (fields.int) :
    _tag = '709'
    ENUM_EXERCISE = 1
    ENUM_DO_NOT_EXERCISE = 2
    ENUM_POSITION_ADJUSTMENT = 3
    ENUM_POSITION_CHANGE_SUBMISSION_MARGIN_DISPOSITION = 4
    ENUM_PLEDGE = 5

class PosReqID (fields.String) :
    _tag = '710'

class NoUnderlyings (fields.NumInGroup) :
    _tag = '711'

class PosMaintAction (fields.int) :
    _tag = '712'
    ENUM_NEW_USED_TO_INCREMENT_THE_OVERALL_TRANSACTION_QUANTITY = 1
    ENUM_REPLACE_USED_TO_OVERRIDE_THE_OVERALL_TRANSACTION_QUANTITY_OR_SPECIFIC_ADD_MESSAGES_BASED_ON_THE_REFERENCE_ID = 2
    ENUM_CANCEL_USED_TO_REMOVE_THE_OVERALL_TRANSACTION_OR_SPECIFIC_ADD_MESSAGES_BASED_ON_REFERENCE_ID = 3

class OrigPosReqRefID (fields.String) :
    _tag = '713'

class PosMaintRptRefID (fields.String) :
    _tag = '714'

class ClearingBusinessDate (fields.LocalMktDate) :
    _tag = '715'

class SettlSessID (fields.String) :
    _tag = '716'
    ENUM_INTRADAY = 'ITD'
    ENUM_REGULAR_TRADING_HOURS = 'RTH'
    ENUM_ELECTRONIC_TRADING_HOURS = 'ETH'

class SettlSessSubID (fields.String) :
    _tag = '717'

class AdjustmentType (fields.int) :
    _tag = '718'
    ENUM_PROCESS_REQUEST_AS_MARGIN_DISPOSITION = 0
    ENUM_DELTA_PLUS = 1
    ENUM_DELTA_MINUS = 2
    ENUM_FINAL = 3

class ContraryInstructionIndicator (fields.Boolean) :
    _tag = '719'

class PriorSpreadIndicator (fields.Boolean) :
    _tag = '720'

class PosMaintRptID (fields.String) :
    _tag = '721'

class PosMaintStatus (fields.int) :
    _tag = '722'
    ENUM_ACCEPTED = 0
    ENUM_ACCEPTED_WITH_WARNINGS = 1
    ENUM_REJECTED = 2
    ENUM_COMPLETED = 3
    ENUM_COMPLETED_WITH_WARNINGS = 4

class PosMaintResult (fields.int) :
    _tag = '723'
    ENUM_SUCCESSFUL_COMPLETION = 0
    ENUM_REJECTED = 1
    ENUM_OTHER = 99

class PosReqType (fields.int) :
    _tag = '724'
    ENUM_POSITIONS = 0
    ENUM_TRADES = 1
    ENUM_EXERCISES = 2
    ENUM_ASSIGNMENTS = 3

class ResponseTransportType (fields.int) :
    _tag = '725'
    ENUM_INBAND_TRANSPORT_THE_REQUEST_WAS_SENT_OVER = 0
    ENUM_OUT_OF_BAND_PRE_ARRANGED_OUT_OF_BAND_DELIVERY_MECHANISM = 1

class ResponseDestination (fields.String) :
    _tag = '726'

class TotalNumPosReports (fields.int) :
    _tag = '727'

class PosReqResult (fields.int) :
    _tag = '728'
    ENUM_VALID_REQUEST = 0
    ENUM_INVALID_OR_UNSUPPORTED_REQUEST = 1
    ENUM_NO_POSITIONS_FOUND_THAT_MATCH_CRITERIA = 2
    ENUM_NOT_AUTHORIZED_TO_REQUEST_POSITIONS = 3
    ENUM_REQUEST_FOR_POSITION_NOT_SUPPORTED = 4
    ENUM_OTHER = 99

class PosReqStatus (fields.int) :
    _tag = '729'
    ENUM_COMPLETED = 0
    ENUM_COMPLETED_WITH_WARNINGS = 1
    ENUM_REJECTED = 2

class SettlPrice (fields.Price) :
    _tag = '730'

class SettlPriceType (fields.int) :
    _tag = '731'
    ENUM_FINAL = 1
    ENUM_THEORETICAL = 2

class UnderlyingSettlPrice (fields.Price) :
    _tag = '732'

class UnderlyingSettlPriceType (fields.int) :
    _tag = '733'

class PriorSettlPrice (fields.Price) :
    _tag = '734'

class NoQuoteQualifiers (fields.NumInGroup) :
    _tag = '735'

class AllocSettlCurrency (fields.Currency) :
    _tag = '736'

class AllocSettlCurrAmt (fields.Amt) :
    _tag = '737'

class InterestAtMaturity (fields.Amt) :
    _tag = '738'

class LegDatedDate (fields.LocalMktDate) :
    _tag = '739'

class LegPool (fields.String) :
    _tag = '740'

class AllocInterestAtMaturity (fields.Amt) :
    _tag = '741'

class AllocAccruedInterestAmt (fields.Amt) :
    _tag = '742'

class DeliveryDate (fields.LocalMktDate) :
    _tag = '743'

class AssignmentMethod (fields.char) :
    _tag = '744'
    ENUM_RANDOM = 'R'
    ENUM_PRORATA = 'P'

class AssignmentUnit (fields.Qty) :
    _tag = '745'

class OpenInterest (fields.Amt) :
    _tag = '746'

class ExerciseMethod (fields.char) :
    _tag = '747'
    ENUM_AUTOMATIC = 'A'
    ENUM_MANUAL = 'M'

class TotNumTradeReports (fields.int) :
    _tag = '748'

class TradeRequestResult (fields.int) :
    _tag = '749'
    ENUM_SUCCESSFUL = 0
    ENUM_INVALID_OR_UNKNOWN_INSTRUMENT = 1
    ENUM_INVALID_TYPE_OF_TRADE_REQUESTED = 2
    ENUM_INVALID_PARTIES = 3
    ENUM_INVALID_TRANSPORT_TYPE_REQUESTED = 4
    ENUM_INVALID_DESTINATION_REQUESTED = 5
    ENUM_TRADEREQUESTTYPE_NOT_SUPPORTED = 8
    ENUM_UNAUTHORIZED_FOR_TRADE_CAPTURE_REPORT_REQUEST = 9
    ENUM_OTHER = 99

class TradeRequestStatus (fields.int) :
    _tag = '750'
    ENUM_ACCEPTED = 0
    ENUM_COMPLETED = 1
    ENUM_REJECTED = 2

class TradeReportRejectReason (fields.int) :
    _tag = '751'
    ENUM_SUCCESSFUL = 0
    ENUM_INVALID_PARTY_INFORMATION = 1
    ENUM_UNKNOWN_INSTRUMENT = 2
    ENUM_UNAUTHORIZED_TO_REPORT_TRADES = 3
    ENUM_INVALID_TRADE_TYPE = 4
    ENUM_OTHER = 99

class SideMultiLegReportingType (fields.int) :
    _tag = '752'
    ENUM_SINGLE_SECURITY = 1
    ENUM_INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY = 2
    ENUM_MULTI_LEG_SECURITY = 3

class NoPosAmt (fields.NumInGroup) :
    _tag = '753'

class AutoAcceptIndicator (fields.Boolean) :
    _tag = '754'

class AllocReportID (fields.String) :
    _tag = '755'

class NoNested2PartyIDs (fields.NumInGroup) :
    _tag = '756'

class Nested2PartyID (fields.String) :
    _tag = '757'

class Nested2PartyIDSource (fields.char) :
    _tag = '758'

class Nested2PartyRole (fields.int) :
    _tag = '759'

class Nested2PartySubID (fields.String) :
    _tag = '760'

class BenchmarkSecurityIDSource (fields.String) :
    _tag = '761'

class SecuritySubType (fields.String) :
    _tag = '762'

class UnderlyingSecuritySubType (fields.String) :
    _tag = '763'

class LegSecuritySubType (fields.String) :
    _tag = '764'

class AllowableOneSidednessPct (fields.Percentage) :
    _tag = '765'

class AllowableOneSidednessValue (fields.Amt) :
    _tag = '766'

class AllowableOneSidednessCurr (fields.Currency) :
    _tag = '767'

class NoTrdRegTimestamps (fields.NumInGroup) :
    _tag = '768'

class TrdRegTimestamp (fields.UTCTimestamp) :
    _tag = '769'

class TrdRegTimestampType (fields.int) :
    _tag = '770'
    ENUM_EXECUTION_TIME = 1
    ENUM_TIME_IN = 2
    ENUM_TIME_OUT = 3
    ENUM_BROKER_RECEIPT = 4
    ENUM_BROKER_EXECUTION = 5

class TrdRegTimestampOrigin (fields.String) :
    _tag = '771'

class ConfirmRefID (fields.String) :
    _tag = '772'

class ConfirmType (fields.int) :
    _tag = '773'
    ENUM_STATUS = 1
    ENUM_CONFIRMATION = 2
    ENUM_CONFIRMATION_REQUEST_REJECTED = 3

class ConfirmRejReason (fields.int) :
    _tag = '774'
    ENUM_MISMATCHED_ACCOUNT = 1
    ENUM_MISSING_SETTLEMENT_INSTRUCTIONS = 2
    ENUM_OTHER = 99

class BookingType (fields.int) :
    _tag = '775'
    ENUM_REGULAR_BOOKING = 0
    ENUM_CFD = 1
    ENUM_TOTAL_RETURN_SWAP = 2

class IndividualAllocRejCode (fields.int) :
    _tag = '776'

class SettlInstMsgID (fields.String) :
    _tag = '777'

class NoSettlInst (fields.NumInGroup) :
    _tag = '778'

class LastUpdateTime (fields.UTCTimestamp) :
    _tag = '779'

class AllocSettlInstType (fields.int) :
    _tag = '780'
    ENUM_USE_DEFAULT_INSTRUCTIONS = 0
    ENUM_DERIVE_FROM_PARAMETERS_PROVIDED = 1
    ENUM_FULL_DETAILS_PROVIDED = 2
    ENUM_SSI_DB_IDS_PROVIDED = 3
    ENUM_PHONE_FOR_INSTRUCTIONS = 4

class NoSettlPartyIDs (fields.NumInGroup) :
    _tag = '781'

class SettlPartyID (fields.String) :
    _tag = '782'

class SettlPartyIDSource (fields.char) :
    _tag = '783'

class SettlPartyRole (fields.int) :
    _tag = '784'

class SettlPartySubID (fields.String) :
    _tag = '785'

class SettlPartySubIDType (fields.int) :
    _tag = '786'

class DlvyInstType (fields.char) :
    _tag = '787'
    ENUM_SECURITIES = 'S'
    ENUM_CASH = 'C'

class TerminationType (fields.int) :
    _tag = '788'
    ENUM_OVERNIGHT = 1
    ENUM_TERM = 2
    ENUM_FLEXIBLE = 3
    ENUM_OPEN = 4

class NextExpectedMsgSeqNum (fields.SeqNum) :
    _tag = '789'

class OrdStatusReqID (fields.String) :
    _tag = '790'

class SettlInstReqID (fields.String) :
    _tag = '791'

class SettlInstReqRejCode (fields.int) :
    _tag = '792'
    ENUM_UNABLE_TO_PROCESS_REQUEST = 0
    ENUM_UNKNOWN_ACCOUNT = 1
    ENUM_NO_MATCHING_SETTLEMENT_INSTRUCTIONS_FOUND = 2
    ENUM_OTHER = 99

class SecondaryAllocID (fields.String) :
    _tag = '793'

class AllocReportType (fields.int) :
    _tag = '794'
    ENUM_SELLSIDE_CALCULATED_USING_PRELIMINARY = 3
    ENUM_SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY = 4
    ENUM_WAREHOUSE_RECAP = 5
    ENUM_REQUEST_TO_INTERMEDIARY = 8

class AllocReportRefID (fields.String) :
    _tag = '795'

class AllocCancReplaceReason (fields.int) :
    _tag = '796'
    ENUM_ORIGINAL_DETAILS_INCOMPLETE_INCORRECT = 1
    ENUM_CHANGE_IN_UNDERLYING_ORDER_DETAILS = 2
    ENUM_OTHER = 99

class CopyMsgIndicator (fields.Boolean) :
    _tag = '797'

class AllocAccountType (fields.int) :
    _tag = '798'
    ENUM_ACCOUNT_IS_CARRIED_ON_CUSTOMER_SIDE_OF_BOOKS = 1
    ENUM_ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS = 2
    ENUM_HOUSE_TRADER = 3
    ENUM_FLOOR_TRADER = 4
    ENUM_ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS_AND_IS_CROSS_MARGINED = 6
    ENUM_ACCOUNT_IS_HOUSE_TRADER_AND_IS_CROSS_MARGINED = 7
    ENUM_JOINT_BACKOFFICE_ACCOUNT = 8

class OrderAvgPx (fields.Price) :
    _tag = '799'

class OrderBookingQty (fields.Qty) :
    _tag = '800'

class NoSettlPartySubIDs (fields.NumInGroup) :
    _tag = '801'

class NoPartySubIDs (fields.NumInGroup) :
    _tag = '802'

class PartySubIDType (fields.int) :
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
    ENUM_REGISTERED_ADDRESS_12 = 12
    ENUM_REGULATORY_STATUS = 13
    ENUM_REGISTRATION_NAME = 14
    ENUM_CASH_ACCOUNT_NUMBER = 15
    ENUM_BIC = 16
    ENUM_CSD_PARTICIPANT_MEMBER_CODE = 17
    ENUM_REGISTERED_ADDRESS_18 = 18
    ENUM_FUND_ACCOUNT_NAME = 19
    ENUM_TELEX_NUMBER = 20
    ENUM_FAX_NUMBER = 21
    ENUM_SECURITIES_ACCOUNT_NAME = 22
    ENUM_CASH_ACCOUNT_NAME = 23
    ENUM_DEPARTMENT = 24
    ENUM_LOCATION = 25
    ENUM_POSITION_ACCOUNT_TYPE = 26

class NoNestedPartySubIDs (fields.NumInGroup) :
    _tag = '804'

class NestedPartySubIDType (fields.int) :
    _tag = '805'

class NoNested2PartySubIDs (fields.NumInGroup) :
    _tag = '806'

class Nested2PartySubIDType (fields.int) :
    _tag = '807'

class AllocIntermedReqType (fields.int) :
    _tag = '808'
    ENUM_PENDING_ACCEPT = 1
    ENUM_PENDING_RELEASE = 2
    ENUM_PENDING_REVERSAL = 3
    ENUM_ACCEPT = 4
    ENUM_BLOCK_LEVEL_REJECT = 5
    ENUM_ACCOUNT_LEVEL_REJECT = 6

class UnderlyingPx (fields.Price) :
    _tag = '810'

class PriceDelta (fields.float) :
    _tag = '811'

class ApplQueueMax (fields.int) :
    _tag = '812'

class ApplQueueDepth (fields.int) :
    _tag = '813'

class ApplQueueResolution (fields.int) :
    _tag = '814'
    ENUM_NO_ACTION_TAKEN = 0
    ENUM_QUEUE_FLUSHED = 1
    ENUM_OVERLAY_LAST = 2
    ENUM_END_SESSION = 3

class ApplQueueAction (fields.int) :
    _tag = '815'
    ENUM_NO_ACTION_TAKEN = 0
    ENUM_QUEUE_FLUSHED = 1
    ENUM_OVERLAY_LAST = 2
    ENUM_END_SESSION = 3

class NoAltMDSource (fields.NumInGroup) :
    _tag = '816'

class AltMDSourceID (fields.String) :
    _tag = '817'

class SecondaryTradeReportID (fields.String) :
    _tag = '818'

class AvgPxIndicator (fields.int) :
    _tag = '819'
    ENUM_NO_AVERAGE_PRICING = 0
    ENUM_TRADE_IS_PART_OF_AN_AVERAGE_PRICE_GROUP_IDENTIFIED_BY_THE_TRADELINKID = 1
    ENUM_LAST_TRADE_IN_THE_AVERAGE_PRICE_GROUP_IDENTIFIED_BY_THE_TRADELINKID = 2

class TradeLinkID (fields.String) :
    _tag = '820'

class OrderInputDevice (fields.String) :
    _tag = '821'

class UnderlyingTradingSessionID (fields.String) :
    _tag = '822'

class UnderlyingTradingSessionSubID (fields.String) :
    _tag = '823'

class TradeLegRefID (fields.String) :
    _tag = '824'

class ExchangeRule (fields.String) :
    _tag = '825'

class TradeAllocIndicator (fields.int) :
    _tag = '826'
    ENUM_ALLOCATION_NOT_REQUIRED = 0
    ENUM_ALLOCATION_REQUIRED = 1
    ENUM_USE_ALLOCATION_PROVIDED_WITH_THE_TRADE = 2

class ExpirationCycle (fields.int) :
    _tag = '827'
    ENUM_EXPIRE_ON_TRADING_SESSION_CLOSE = 0
    ENUM_EXPIRE_ON_TRADING_SESSION_OPEN = 1

class TrdType (fields.int) :
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

class TrdSubType (fields.int) :
    _tag = '829'

class TransferReason (fields.String) :
    _tag = '830'

class TotNumAssignmentReports (fields.int) :
    _tag = '832'

class AsgnRptID (fields.String) :
    _tag = '833'

class ThresholdAmount (fields.PriceOffset) :
    _tag = '834'

class PegMoveType (fields.int) :
    _tag = '835'
    ENUM_FLOATING = 0
    ENUM_FIXED = 1

class PegOffsetType (fields.int) :
    _tag = '836'
    ENUM_PRICE = 0
    ENUM_BASIS_POINTS = 1
    ENUM_TICKS = 2
    ENUM_PRICE_TIER = 3

class PegLimitType (fields.int) :
    _tag = '837'
    ENUM_OR_BETTER = 0
    ENUM_STRICT_LIMIT_IS_A_STRICT_LIMIT = 1
    ENUM_OR_WORSE_FOR_A_BUY_THE_PEG_LIMIT_IS_A_MINIMUM_AND_FOR_A_SELL_THE_PEG_LIMIT_IS_A_MAXIMUM = 2

class PegRoundDirection (fields.int) :
    _tag = '838'
    ENUM_MORE_AGGRESSIVE_ON_A_BUY_ORDER_ROUND_THE_PRICE_UP_ROUND_UP_TO_THE_NEAREST_TICK_ON_A_SELL_ROUND_DOWN_TO_THE_NEAREST_TICK = 1
    ENUM_MORE_PASSIVE_ON_A_BUY_ORDER_ROUND_DOWN_TO_NEAREST_TICK_ON_A_SELL_ORDER_ROUND_UP_TO_NEAREST_TICK = 2

class PeggedPrice (fields.Price) :
    _tag = '839'

class PegScope (fields.int) :
    _tag = '840'
    ENUM_LOCAL = 1
    ENUM_NATIONAL = 2
    ENUM_GLOBAL = 3
    ENUM_NATIONAL_EXCLUDING_LOCAL = 4

class DiscretionMoveType (fields.int) :
    _tag = '841'
    ENUM_FLOATING = 0
    ENUM_FIXED = 1

class DiscretionOffsetType (fields.int) :
    _tag = '842'
    ENUM_PRICE = 0
    ENUM_BASIS_POINTS = 1
    ENUM_TICKS = 2
    ENUM_PRICE_TIER = 3

class DiscretionLimitType (fields.int) :
    _tag = '843'
    ENUM_OR_BETTER = 0
    ENUM_STRICT_LIMIT_IS_A_STRICT_LIMIT = 1
    ENUM_OR_WORSE_FOR_A_BUY_THE_DISCRETION_PRICE_IS_A_MINIMUM_AND_FOR_A_SELL_THE_DISCRETION_PRICE_IS_A_MAXIMUM = 2

class DiscretionRoundDirection (fields.int) :
    _tag = '844'
    ENUM_MORE_AGGRESSIVE_ON_A_BUY_ORDER_ROUND_THE_PRICE_UP_ROUND_UP_TO_THE_NEAREST_TICK_ON_A_SELL_ROUND_DOWN_TO_THE_NEAREST_TICK = 1
    ENUM_MORE_PASSIVE_ON_A_BUY_ORDER_ROUND_DOWN_TO_NEAREST_TICK_ON_A_SELL_ORDER_ROUND_UP_TO_NEAREST_TICK = 2

class DiscretionPrice (fields.Price) :
    _tag = '845'

class DiscretionScope (fields.int) :
    _tag = '846'
    ENUM_LOCAL = 1
    ENUM_NATIONAL = 2
    ENUM_GLOBAL = 3
    ENUM_NATIONAL_EXCLUDING_LOCAL = 4

class TargetStrategy (fields.int) :
    _tag = '847'
    ENUM_VWAP = 1
    ENUM_PARTICIPATE = 2
    ENUM_MININIZE_MARKET_IMPACT = 3

class TargetStrategyParameters (fields.String) :
    _tag = '848'

class ParticipationRate (fields.Percentage) :
    _tag = '849'

class TargetStrategyPerformance (fields.float) :
    _tag = '850'

class LastLiquidityInd (fields.int) :
    _tag = '851'
    ENUM_ADDED_LIQUIDITY = 1
    ENUM_REMOVED_LIQUIDITY = 2
    ENUM_LIQUIDITY_ROUTED_OUT = 3

class PublishTrdIndicator (fields.Boolean) :
    _tag = '852'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class ShortSaleReason (fields.int) :
    _tag = '853'
    ENUM_DEALER_SOLD_SHORT = 0
    ENUM_DEALER_SOLD_SHORT_EXEMPT = 1
    ENUM_SELLING_CUSTOMER_SOLD_SHORT = 2
    ENUM_SELLING_CUSTOMER_SOLD_SHORT_EXEMPT = 3
    ENUM_QUALIFED_SERVICE_REPRESENTATIVE = 4
    ENUM_QSR_OR_AGU_CONTRA_SIDE_SOLD_SHORT_EXEMPT = 5

class QtyType (fields.int) :
    _tag = '854'
    ENUM_UNITS = 0
    ENUM_CONTRACTS = 1

class SecondaryTrdType (fields.int) :
    _tag = '855'

class TradeReportType (fields.int) :
    _tag = '856'
    ENUM_SUBMIT = 0
    ENUM_ALLEGED = 1
    ENUM_ACCEPT = 2
    ENUM_DECLINE = 3
    ENUM_ADDENDUM = 4
    ENUM_NO_WAS = 5
    ENUM_TRADE_REPORT_CANCEL = 6
    ENUM_LOCKED_IN_TRADE_BREAK = 7

class AllocNoOrdersType (fields.int) :
    _tag = '857'
    ENUM_NOT_SPECIFIED = 0
    ENUM_EXPLICIT_LIST_PROVIDED = 1

class SharedCommission (fields.Amt) :
    _tag = '858'

class ConfirmReqID (fields.String) :
    _tag = '859'

class AvgParPx (fields.Price) :
    _tag = '860'

class ReportedPx (fields.Price) :
    _tag = '861'

class NoCapacities (fields.NumInGroup) :
    _tag = '862'

class OrderCapacityQty (fields.Qty) :
    _tag = '863'

class NoEvents (fields.NumInGroup) :
    _tag = '864'

class EventType (fields.int) :
    _tag = '865'
    ENUM_PUT = 1
    ENUM_CALL = 2
    ENUM_TENDER = 3
    ENUM_SINKING_FUND_CALL = 4
    ENUM_OTHER = 99

class EventDate (fields.LocalMktDate) :
    _tag = '866'

class EventPx (fields.Price) :
    _tag = '867'

class EventText (fields.String) :
    _tag = '868'

class PctAtRisk (fields.Percentage) :
    _tag = '869'

class NoInstrAttrib (fields.NumInGroup) :
    _tag = '870'

class InstrAttribType (fields.int) :
    _tag = '871'
    ENUM_FLAT = 1
    ENUM_ZERO_COUPON = 2
    ENUM_INTEREST_BEARING = 3
    ENUM_NO_PERIODIC_PAYMENTS = 4
    ENUM_VARIABLE_RATE = 5
    ENUM_LESS_FEE_FOR_PUT = 6
    ENUM_STEPPED_COUPON = 7
    ENUM_COUPON_PERIOD = 8
    ENUM_WHEN_AND_IF_ISSUED = 9
    ENUM_ORIGINAL_ISSUE_DISCOUNT = 10
    ENUM_CALLABLE_PUTTABLE = 11
    ENUM_ESCROWED_TO_MATURITY = 12
    ENUM_ESCROWED_TO_REDEMPTION_DATE_CALLABLE_SUPPLY_REDEMPTION_DATE_IN_THE_INSTRATTRIBVALUE = 13
    ENUM_PREREFUNDED = 14
    ENUM_IN_DEFAULT = 15
    ENUM_UNRATED = 16
    ENUM_TAXABLE = 17
    ENUM_INDEXED = 18
    ENUM_SUBJECT_TO_ALTERNATIVE_MINIMUM_TAX = 19
    ENUM_ORIGINAL_ISSUE_DISCOUNT_PRICE_SUPPLY_PRICE_IN_THE_INSTRATTRIBVALUE = 20
    ENUM_CALLABLE_BELOW_MATURITY_VALUE = 21
    ENUM_CALLABLE_WITHOUT_NOTICE_BY_MAIL_TO_HOLDER_UNLESS_REGISTERED = 22
    ENUM_TEXT_SUPPLY_THE_TEXT_OF_THE_ATTRIBUTE_OR_DISCLAIMER_IN_THE_INSTRATTRIBVALUE = 99

class InstrAttribValue (fields.String) :
    _tag = '872'

class DatedDate (fields.LocalMktDate) :
    _tag = '873'

class InterestAccrualDate (fields.LocalMktDate) :
    _tag = '874'

class CPProgram (fields.int) :
    _tag = '875'
    ENUM_3 = 1
    ENUM_4 = 2
    ENUM_OTHER = 99

class CPRegType (fields.String) :
    _tag = '876'

class UnderlyingCPProgram (fields.String) :
    _tag = '877'

class UnderlyingCPRegType (fields.String) :
    _tag = '878'

class UnderlyingQty (fields.Qty) :
    _tag = '879'

class TrdMatchID (fields.String) :
    _tag = '880'

class SecondaryTradeReportRefID (fields.String) :
    _tag = '881'

class UnderlyingDirtyPrice (fields.Price) :
    _tag = '882'

class UnderlyingEndPrice (fields.Price) :
    _tag = '883'

class UnderlyingStartValue (fields.Amt) :
    _tag = '884'

class UnderlyingCurrentValue (fields.Amt) :
    _tag = '885'

class UnderlyingEndValue (fields.Amt) :
    _tag = '886'

class NoUnderlyingStips (fields.NumInGroup) :
    _tag = '887'

class UnderlyingStipType (fields.String) :
    _tag = '888'

class UnderlyingStipValue (fields.String) :
    _tag = '889'

class MaturityNetMoney (fields.Amt) :
    _tag = '890'

class MiscFeeBasis (fields.int) :
    _tag = '891'
    ENUM_ABSOLUTE = 0
    ENUM_PER_UNIT = 1
    ENUM_PERCENTAGE = 2

class TotNoAllocs (fields.int) :
    _tag = '892'

class LastFragment (fields.Boolean) :
    _tag = '893'
    ENUM_YES = 'Y'
    ENUM_NO = 'N'

class CollReqID (fields.String) :
    _tag = '894'

class CollAsgnReason (fields.int) :
    _tag = '895'
    ENUM_INITIAL = 0
    ENUM_SCHEDULED = 1
    ENUM_TIME_WARNING = 2
    ENUM_MARGIN_DEFICIENCY = 3
    ENUM_MARGIN_EXCESS = 4
    ENUM_FORWARD_COLLATERAL_DEMAND = 5
    ENUM_EVENT_OF_DEFAULT = 6
    ENUM_ADVERSE_TAX_EVENT = 7

class CollInquiryQualifier (fields.int) :
    _tag = '896'
    ENUM_TRADEDATE = 0
    ENUM_GC_INSTRUMENT = 1
    ENUM_COLLATERALINSTRUMENT = 2
    ENUM_SUBSTITUTION_ELIGIBLE = 3
    ENUM_NOT_ASSIGNED = 4
    ENUM_PARTIALLY_ASSIGNED = 5
    ENUM_FULLY_ASSIGNED = 6
    ENUM_OUTSTANDING_TRADES = 7

class NoTrades (fields.NumInGroup) :
    _tag = '897'

class MarginRatio (fields.Percentage) :
    _tag = '898'

class MarginExcess (fields.Amt) :
    _tag = '899'

class TotalNetValue (fields.Amt) :
    _tag = '900'

class CashOutstanding (fields.Amt) :
    _tag = '901'

class CollAsgnID (fields.String) :
    _tag = '902'

class CollAsgnTransType (fields.int) :
    _tag = '903'
    ENUM_NEW = 0
    ENUM_REPLACE = 1
    ENUM_CANCEL = 2
    ENUM_RELEASE = 3
    ENUM_REVERSE = 4

class CollRespID (fields.String) :
    _tag = '904'

class CollAsgnRespType (fields.int) :
    _tag = '905'
    ENUM_RECEIVED = 0
    ENUM_ACCEPTED = 1
    ENUM_DECLINED = 2
    ENUM_REJECTED = 3

class CollAsgnRejectReason (fields.int) :
    _tag = '906'
    ENUM_UNKNOWN_DEAL = 0
    ENUM_UNKNOWN_OR_INVALID_INSTRUMENT = 1
    ENUM_UNAUTHORIZED_TRANSACTION = 2
    ENUM_INSUFFICIENT_COLLATERAL = 3
    ENUM_INVALID_TYPE_OF_COLLATERAL = 4
    ENUM_EXCESSIVE_SUBSTITUTION = 5
    ENUM_OTHER = 99

class CollAsgnRefID (fields.String) :
    _tag = '907'

class CollRptID (fields.String) :
    _tag = '908'

class CollInquiryID (fields.String) :
    _tag = '909'

class CollStatus (fields.int) :
    _tag = '910'
    ENUM_UNASSIGNED = 0
    ENUM_PARTIALLY_ASSIGNED = 1
    ENUM_ASSIGNMENT_PROPOSED = 2
    ENUM_ASSIGNED = 3
    ENUM_CHALLENGED = 4

class TotNumReports (fields.int) :
    _tag = '911'

class LastRptRequested (fields.Boolean) :
    _tag = '912'

class AgreementDesc (fields.String) :
    _tag = '913'

class AgreementID (fields.String) :
    _tag = '914'

class AgreementDate (fields.LocalMktDate) :
    _tag = '915'

class StartDate (fields.LocalMktDate) :
    _tag = '916'

class EndDate (fields.LocalMktDate) :
    _tag = '917'

class AgreementCurrency (fields.Currency) :
    _tag = '918'

class DeliveryType (fields.int) :
    _tag = '919'
    ENUM_VERSUS_PAYMENT_DELIVER = 0
    ENUM_FREE_DELIVER = 1
    ENUM_TRI_PARTY = 2
    ENUM_HOLD_IN_CUSTODY = 3

class EndAccruedInterestAmt (fields.Amt) :
    _tag = '920'

class StartCash (fields.Amt) :
    _tag = '921'

class EndCash (fields.Amt) :
    _tag = '922'

class UserRequestID (fields.String) :
    _tag = '923'

class UserRequestType (fields.int) :
    _tag = '924'
    ENUM_LOGONUSER = 1
    ENUM_LOGOFFUSER = 2
    ENUM_CHANGEPASSWORDFORUSER = 3
    ENUM_REQUEST_INDIVIDUAL_USER_STATUS = 4

class NewPassword (fields.String) :
    _tag = '925'

class UserStatus (fields.int) :
    _tag = '926'
    ENUM_LOGGED_IN = 1
    ENUM_NOT_LOGGED_IN = 2
    ENUM_USER_NOT_RECOGNISED = 3
    ENUM_PASSWORD_INCORRECT = 4
    ENUM_PASSWORD_CHANGED = 5
    ENUM_OTHER = 6

class UserStatusText (fields.String) :
    _tag = '927'

class StatusValue (fields.int) :
    _tag = '928'
    ENUM_CONNECTED = 1
    ENUM_NOT_CONNECTED_DOWN_EXPECTED_UP = 2
    ENUM_NOT_CONNECTED_DOWN_EXPECTED_DOWN = 3
    ENUM_IN_PROCESS = 4

class StatusText (fields.String) :
    _tag = '929'

class RefCompID (fields.String) :
    _tag = '930'

class RefSubID (fields.String) :
    _tag = '931'

class NetworkResponseID (fields.String) :
    _tag = '932'

class NetworkRequestID (fields.String) :
    _tag = '933'

class LastNetworkResponseID (fields.String) :
    _tag = '934'

class NetworkRequestType (fields.int) :
    _tag = '935'
    ENUM_SNAPSHOT = 1
    ENUM_SUBSCRIBE = 2
    ENUM_STOP_SUBSCRIBING = 4
    ENUM_LEVEL_OF_DETAIL_THEN_NOCOMPIDS_BECOMES_REQUIRED = 8

class NoCompIDs (fields.NumInGroup) :
    _tag = '936'

class NetworkStatusResponseType (fields.int) :
    _tag = '937'
    ENUM_FULL = 1
    ENUM_INCREMENTAL_UPDATE = 2

class NoCollInquiryQualifier (fields.NumInGroup) :
    _tag = '938'

class TrdRptStatus (fields.int) :
    _tag = '939'
    ENUM_ACCEPTED = 0
    ENUM_REJECTED = 1

class AffirmStatus (fields.int) :
    _tag = '940'
    ENUM_RECEIVED = 1
    ENUM_CONFIRM_REJECTED_IE_NOT_AFFIRMED = 2
    ENUM_AFFIRMED = 3

class UnderlyingStrikeCurrency (fields.Currency) :
    _tag = '941'

class LegStrikeCurrency (fields.Currency) :
    _tag = '942'

class TimeBracket (fields.String) :
    _tag = '943'

class CollAction (fields.int) :
    _tag = '944'
    ENUM_RETAIN = 0
    ENUM_ADD = 1
    ENUM_REMOVE = 2

class CollInquiryStatus (fields.int) :
    _tag = '945'
    ENUM_ACCEPTED = 0
    ENUM_ACCEPTED_WITH_WARNINGS = 1
    ENUM_COMPLETED = 2
    ENUM_COMPLETED_WITH_WARNINGS = 3
    ENUM_REJECTED = 4

class CollInquiryResult (fields.int) :
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

class StrikeCurrency (fields.Currency) :
    _tag = '947'

class NoNested3PartyIDs (fields.NumInGroup) :
    _tag = '948'

class Nested3PartyID (fields.String) :
    _tag = '949'

class Nested3PartyIDSource (fields.char) :
    _tag = '950'

class Nested3PartyRole (fields.int) :
    _tag = '951'

class NoNested3PartySubIDs (fields.NumInGroup) :
    _tag = '952'

class Nested3PartySubID (fields.String) :
    _tag = '953'

class Nested3PartySubIDType (fields.int) :
    _tag = '954'

class LegContractSettlMonth (fields.MonthYear) :
    _tag = '955'

class LegInterestAccrualDate (fields.LocalMktDate) :
    _tag = '956'

class Header(fix_message.MessageBase):
    def __init__(self):
        super().__init__()
        self.register_field(BeginString, True)
        self.register_field(BodyLength, True)
        self.register_field(MsgType, True)
        self.register_field(SenderCompID, True)
        self.register_field(TargetCompID, True)
        self.register_field(OnBehalfOfCompID, False)
        self.register_field(DeliverToCompID, False)
        self.register_field(SecureDataLen, False)
        self.register_field(SecureData, False)
        self.register_field(MsgSeqNum, True)
        self.register_field(SenderSubID, False)
        self.register_field(SenderLocationID, False)
        self.register_field(TargetSubID, False)
        self.register_field(TargetLocationID, False)
        self.register_field(OnBehalfOfSubID, False)
        self.register_field(OnBehalfOfLocationID, False)
        self.register_field(DeliverToSubID, False)
        self.register_field(DeliverToLocationID, False)
        self.register_field(PossDupFlag, False)
        self.register_field(PossResend, False)
        self.register_field(SendingTime, True)
        self.register_field(OrigSendingTime, False)
        self.register_field(XmlDataLen, False)
        self.register_field(XmlData, False)
        self.register_field(MessageEncoding, False)
        self.register_field(LastMsgSeqNumProcessed, False)

        class NoHopsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(HopCompID, False)
                self.register_field(HopSendingTime, False)
                self.register_field(HopRefID, False)

        self.register_group(NoHops, NoHopsGroup, False)

class Heartbeat(fix_message.MessageBase):
    _msgtype = '0'
    _msgcat = 'admin'
    def __init__(self):
        super().__init__()
        self.register_field(TestReqID, False)

MESSAGE_TYPES['0'] = Heartbeat

class TestRequest(fix_message.MessageBase):
    _msgtype = '1'
    _msgcat = 'admin'
    def __init__(self):
        super().__init__()
        self.register_field(TestReqID, True)

MESSAGE_TYPES['1'] = TestRequest

class ResendRequest(fix_message.MessageBase):
    _msgtype = '2'
    _msgcat = 'admin'
    def __init__(self):
        super().__init__()
        self.register_field(BeginSeqNo, True)
        self.register_field(EndSeqNo, True)

MESSAGE_TYPES['2'] = ResendRequest

class Reject(fix_message.MessageBase):
    _msgtype = '3'
    _msgcat = 'admin'
    def __init__(self):
        super().__init__()
        self.register_field(RefSeqNum, True)
        self.register_field(RefTagID, False)
        self.register_field(RefMsgType, False)
        self.register_field(SessionRejectReason, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['3'] = Reject

class SequenceReset(fix_message.MessageBase):
    _msgtype = '4'
    _msgcat = 'admin'
    def __init__(self):
        super().__init__()
        self.register_field(GapFillFlag, False)
        self.register_field(NewSeqNo, True)

MESSAGE_TYPES['4'] = SequenceReset

class Logout(fix_message.MessageBase):
    _msgtype = '5'
    _msgcat = 'admin'
    def __init__(self):
        super().__init__()
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['5'] = Logout

class IOI(fix_message.MessageBase):
    _msgtype = '6'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(IOIID, True)
        self.register_field(IOITransType, True)
        self.register_field(IOIRefID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(Side, True)
        self.register_field(QtyType, False)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(IOIQty, True)
        self.register_field(Currency, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)
                self.register_field(LegIOIQty, False)

                class NoLegStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegStipulationType, False)
                        self.register_field(LegStipulationValue, False)

                self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(PriceType, False)
        self.register_field(Price, False)
        self.register_field(ValidUntilTime, False)
        self.register_field(IOIQltyInd, False)
        self.register_field(IOINaturalFlag, False)

        class NoIOIQualifiersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(IOIQualifier, False)

        self.register_group(NoIOIQualifiers, NoIOIQualifiersGroup, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(TransactTime, False)
        self.register_field(URLLink, False)

        class NoRoutingIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(RoutingType, False)
                self.register_field(RoutingID, False)

        self.register_group(NoRoutingIDs, NoRoutingIDsGroup, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)

MESSAGE_TYPES['6'] = IOI

class Advertisement(fix_message.MessageBase):
    _msgtype = '7'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(AdvId, True)
        self.register_field(AdvTransType, True)
        self.register_field(AdvRefID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(AdvSide, True)
        self.register_field(Quantity, True)
        self.register_field(QtyType, False)
        self.register_field(Price, False)
        self.register_field(Currency, False)
        self.register_field(TradeDate, False)
        self.register_field(TransactTime, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(URLLink, False)
        self.register_field(LastMkt, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)

MESSAGE_TYPES['7'] = Advertisement

class ExecutionReport(fix_message.MessageBase):
    _msgtype = '8'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(OrderID, True)
        self.register_field(SecondaryOrderID, False)
        self.register_field(SecondaryClOrdID, False)
        self.register_field(SecondaryExecID, False)
        self.register_field(ClOrdID, False)
        self.register_field(OrigClOrdID, False)
        self.register_field(ClOrdLinkID, False)
        self.register_field(QuoteRespID, False)
        self.register_field(OrdStatusReqID, False)
        self.register_field(MassStatusReqID, False)
        self.register_field(TotNumReports, False)
        self.register_field(LastRptRequested, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(TradeOriginationDate, False)

        class NoContraBrokersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ContraBroker, False)
                self.register_field(ContraTrader, False)
                self.register_field(ContraTradeQty, False)
                self.register_field(ContraTradeTime, False)
                self.register_field(ContraLegRefID, False)

        self.register_group(NoContraBrokers, NoContraBrokersGroup, False)
        self.register_field(ListID, False)
        self.register_field(CrossID, False)
        self.register_field(OrigCrossID, False)
        self.register_field(CrossType, False)
        self.register_field(ExecID, True)
        self.register_field(ExecRefID, False)
        self.register_field(ExecType, True)
        self.register_field(OrdStatus, True)
        self.register_field(WorkingIndicator, False)
        self.register_field(OrdRejReason, False)
        self.register_field(ExecRestatementReason, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(DayBookingInst, False)
        self.register_field(BookingUnit, False)
        self.register_field(PreallocMethod, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(CashMargin, False)
        self.register_field(ClearingFeeIndicator, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(Side, True)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(QtyType, False)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(OrdType, False)
        self.register_field(PriceType, False)
        self.register_field(Price, False)
        self.register_field(StopPx, False)
        self.register_field(PegOffsetValue, False)
        self.register_field(PegMoveType, False)
        self.register_field(PegOffsetType, False)
        self.register_field(PegLimitType, False)
        self.register_field(PegRoundDirection, False)
        self.register_field(PegScope, False)
        self.register_field(DiscretionInst, False)
        self.register_field(DiscretionOffsetValue, False)
        self.register_field(DiscretionMoveType, False)
        self.register_field(DiscretionOffsetType, False)
        self.register_field(DiscretionLimitType, False)
        self.register_field(DiscretionRoundDirection, False)
        self.register_field(DiscretionScope, False)
        self.register_field(PeggedPrice, False)
        self.register_field(DiscretionPrice, False)
        self.register_field(TargetStrategy, False)
        self.register_field(TargetStrategyParameters, False)
        self.register_field(ParticipationRate, False)
        self.register_field(TargetStrategyPerformance, False)
        self.register_field(Currency, False)
        self.register_field(ComplianceID, False)
        self.register_field(SolicitedFlag, False)
        self.register_field(TimeInForce, False)
        self.register_field(EffectiveTime, False)
        self.register_field(ExpireDate, False)
        self.register_field(ExpireTime, False)
        self.register_field(ExecInst, False)
        self.register_field(OrderCapacity, False)
        self.register_field(OrderRestrictions, False)
        self.register_field(CustOrderCapacity, False)
        self.register_field(LastQty, False)
        self.register_field(UnderlyingLastQty, False)
        self.register_field(LastPx, False)
        self.register_field(UnderlyingLastPx, False)
        self.register_field(LastParPx, False)
        self.register_field(LastSpotRate, False)
        self.register_field(LastForwardPoints, False)
        self.register_field(LastMkt, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(TimeBracket, False)
        self.register_field(LastCapacity, False)
        self.register_field(LeavesQty, True)
        self.register_field(CumQty, True)
        self.register_field(AvgPx, True)
        self.register_field(DayOrderQty, False)
        self.register_field(DayCumQty, False)
        self.register_field(DayAvgPx, False)
        self.register_field(GTBookingInst, False)
        self.register_field(TradeDate, False)
        self.register_field(TransactTime, False)
        self.register_field(ReportToExch, False)
        self.register_field(Commission, False)
        self.register_field(CommType, False)
        self.register_field(CommCurrency, False)
        self.register_field(FundRenewWaiv, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)
        self.register_field(GrossTradeAmt, False)
        self.register_field(NumDaysInterest, False)
        self.register_field(ExDate, False)
        self.register_field(AccruedInterestRate, False)
        self.register_field(AccruedInterestAmt, False)
        self.register_field(InterestAtMaturity, False)
        self.register_field(EndAccruedInterestAmt, False)
        self.register_field(StartCash, False)
        self.register_field(EndCash, False)
        self.register_field(TradedFlatSwitch, False)
        self.register_field(BasisFeatureDate, False)
        self.register_field(BasisFeaturePrice, False)
        self.register_field(Concession, False)
        self.register_field(TotalTakedown, False)
        self.register_field(NetMoney, False)
        self.register_field(SettlCurrAmt, False)
        self.register_field(SettlCurrency, False)
        self.register_field(SettlCurrFxRate, False)
        self.register_field(SettlCurrFxRateCalc, False)
        self.register_field(HandlInst, False)
        self.register_field(MinQty, False)
        self.register_field(MaxFloor, False)
        self.register_field(PositionEffect, False)
        self.register_field(MaxShow, False)
        self.register_field(BookingType, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(SettlDate2, False)
        self.register_field(OrderQty2, False)
        self.register_field(LastForwardPoints2, False)
        self.register_field(MultiLegReportingType, False)
        self.register_field(CancellationRights, False)
        self.register_field(MoneyLaunderingStatus, False)
        self.register_field(RegistID, False)
        self.register_field(Designation, False)
        self.register_field(TransBkdTime, False)
        self.register_field(ExecValuationPoint, False)
        self.register_field(ExecPriceType, False)
        self.register_field(ExecPriceAdjustment, False)
        self.register_field(PriorityIndicator, False)
        self.register_field(PriceImprovement, False)
        self.register_field(LastLiquidityInd, False)

        class NoContAmtsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ContAmtType, False)
                self.register_field(ContAmtValue, False)
                self.register_field(ContAmtCurr, False)

        self.register_group(NoContAmts, NoContAmtsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)
                self.register_field(LegQty, False)
                self.register_field(LegSwapType, False)

                class NoLegStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegStipulationType, False)
                        self.register_field(LegStipulationValue, False)

                self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)
                self.register_field(LegPositionEffect, False)
                self.register_field(LegCoveredOrUncovered, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(LegRefID, False)
                self.register_field(LegPrice, False)
                self.register_field(LegSettlType, False)
                self.register_field(LegSettlDate, False)
                self.register_field(LegLastPx, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(CopyMsgIndicator, False)

        class NoMiscFeesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(MiscFeeAmt, False)
                self.register_field(MiscFeeCurr, False)
                self.register_field(MiscFeeType, False)
                self.register_field(MiscFeeBasis, False)

        self.register_group(NoMiscFees, NoMiscFeesGroup, False)

MESSAGE_TYPES['8'] = ExecutionReport

class OrderCancelReject(fix_message.MessageBase):
    _msgtype = '9'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(OrderID, True)
        self.register_field(SecondaryOrderID, False)
        self.register_field(SecondaryClOrdID, False)
        self.register_field(ClOrdID, True)
        self.register_field(ClOrdLinkID, False)
        self.register_field(OrigClOrdID, True)
        self.register_field(OrdStatus, True)
        self.register_field(WorkingIndicator, False)
        self.register_field(OrigOrdModTime, False)
        self.register_field(ListID, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(TradeOriginationDate, False)
        self.register_field(TradeDate, False)
        self.register_field(TransactTime, False)
        self.register_field(CxlRejResponseTo, True)
        self.register_field(CxlRejReason, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['9'] = OrderCancelReject

class Logon(fix_message.MessageBase):
    _msgtype = 'A'
    _msgcat = 'admin'
    def __init__(self):
        super().__init__()
        self.register_field(EncryptMethod, True)
        self.register_field(HeartBtInt, True)
        self.register_field(RawDataLength, False)
        self.register_field(RawData, False)
        self.register_field(ResetSeqNumFlag, False)
        self.register_field(NextExpectedMsgSeqNum, False)
        self.register_field(MaxMessageSize, False)

        class NoMsgTypesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(RefMsgType, False)
                self.register_field(MsgDirection, False)

        self.register_group(NoMsgTypes, NoMsgTypesGroup, False)
        self.register_field(TestMessageIndicator, False)
        self.register_field(Username, False)
        self.register_field(Password, False)

MESSAGE_TYPES['A'] = Logon

class News(fix_message.MessageBase):
    _msgtype = 'B'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(OrigTime, False)
        self.register_field(Urgency, False)
        self.register_field(Headline, True)
        self.register_field(EncodedHeadlineLen, False)
        self.register_field(EncodedHeadline, False)

        class NoRoutingIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(RoutingType, False)
                self.register_field(RoutingID, False)

        self.register_group(NoRoutingIDs, NoRoutingIDsGroup, False)

        class NoRelatedSymGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)

        self.register_group(NoRelatedSym, NoRelatedSymGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLinesOfTextGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Text, True)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)

        self.register_group(NoLinesOfText, NoLinesOfTextGroup, True)
        self.register_field(URLLink, False)
        self.register_field(RawDataLength, False)
        self.register_field(RawData, False)

MESSAGE_TYPES['B'] = News

class Email(fix_message.MessageBase):
    _msgtype = 'C'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(EmailThreadID, True)
        self.register_field(EmailType, True)
        self.register_field(OrigTime, False)
        self.register_field(Subject, True)
        self.register_field(EncodedSubjectLen, False)
        self.register_field(EncodedSubject, False)

        class NoRoutingIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(RoutingType, False)
                self.register_field(RoutingID, False)

        self.register_group(NoRoutingIDs, NoRoutingIDsGroup, False)

        class NoRelatedSymGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)

        self.register_group(NoRelatedSym, NoRelatedSymGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(OrderID, False)
        self.register_field(ClOrdID, False)

        class NoLinesOfTextGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Text, True)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)

        self.register_group(NoLinesOfText, NoLinesOfTextGroup, True)
        self.register_field(RawDataLength, False)
        self.register_field(RawData, False)

MESSAGE_TYPES['C'] = Email

class NewOrderSingle(fix_message.MessageBase):
    _msgtype = 'D'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ClOrdID, True)
        self.register_field(SecondaryClOrdID, False)
        self.register_field(ClOrdLinkID, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(TradeOriginationDate, False)
        self.register_field(TradeDate, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(DayBookingInst, False)
        self.register_field(BookingUnit, False)
        self.register_field(PreallocMethod, False)
        self.register_field(AllocID, False)

        class NoAllocsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AllocAccount, False)
                self.register_field(AllocAcctIDSource, False)
                self.register_field(AllocSettlCurrency, False)
                self.register_field(IndividualAllocID, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(AllocQty, False)

        self.register_group(NoAllocs, NoAllocsGroup, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(CashMargin, False)
        self.register_field(ClearingFeeIndicator, False)
        self.register_field(HandlInst, False)
        self.register_field(ExecInst, False)
        self.register_field(MinQty, False)
        self.register_field(MaxFloor, False)
        self.register_field(ExDestination, False)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(ProcessCode, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(PrevClosePx, False)
        self.register_field(Side, True)
        self.register_field(LocateReqd, False)
        self.register_field(TransactTime, True)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(QtyType, False)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(OrdType, True)
        self.register_field(PriceType, False)
        self.register_field(Price, False)
        self.register_field(StopPx, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)
        self.register_field(Currency, False)
        self.register_field(ComplianceID, False)
        self.register_field(SolicitedFlag, False)
        self.register_field(IOIID, False)
        self.register_field(QuoteID, False)
        self.register_field(TimeInForce, False)
        self.register_field(EffectiveTime, False)
        self.register_field(ExpireDate, False)
        self.register_field(ExpireTime, False)
        self.register_field(GTBookingInst, False)
        self.register_field(Commission, False)
        self.register_field(CommType, False)
        self.register_field(CommCurrency, False)
        self.register_field(FundRenewWaiv, False)
        self.register_field(OrderCapacity, False)
        self.register_field(OrderRestrictions, False)
        self.register_field(CustOrderCapacity, False)
        self.register_field(ForexReq, False)
        self.register_field(SettlCurrency, False)
        self.register_field(BookingType, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(SettlDate2, False)
        self.register_field(OrderQty2, False)
        self.register_field(Price2, False)
        self.register_field(PositionEffect, False)
        self.register_field(CoveredOrUncovered, False)
        self.register_field(MaxShow, False)
        self.register_field(PegOffsetValue, False)
        self.register_field(PegMoveType, False)
        self.register_field(PegOffsetType, False)
        self.register_field(PegLimitType, False)
        self.register_field(PegRoundDirection, False)
        self.register_field(PegScope, False)
        self.register_field(DiscretionInst, False)
        self.register_field(DiscretionOffsetValue, False)
        self.register_field(DiscretionMoveType, False)
        self.register_field(DiscretionOffsetType, False)
        self.register_field(DiscretionLimitType, False)
        self.register_field(DiscretionRoundDirection, False)
        self.register_field(DiscretionScope, False)
        self.register_field(TargetStrategy, False)
        self.register_field(TargetStrategyParameters, False)
        self.register_field(ParticipationRate, False)
        self.register_field(CancellationRights, False)
        self.register_field(MoneyLaunderingStatus, False)
        self.register_field(RegistID, False)
        self.register_field(Designation, False)

MESSAGE_TYPES['D'] = NewOrderSingle

class NewOrderList(fix_message.MessageBase):
    _msgtype = 'E'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ListID, True)
        self.register_field(BidID, False)
        self.register_field(ClientBidID, False)
        self.register_field(ProgRptReqs, False)
        self.register_field(BidType, True)
        self.register_field(ProgPeriodInterval, False)
        self.register_field(CancellationRights, False)
        self.register_field(MoneyLaunderingStatus, False)
        self.register_field(RegistID, False)
        self.register_field(ListExecInstType, False)
        self.register_field(ListExecInst, False)
        self.register_field(EncodedListExecInstLen, False)
        self.register_field(EncodedListExecInst, False)
        self.register_field(AllowableOneSidednessPct, False)
        self.register_field(AllowableOneSidednessValue, False)
        self.register_field(AllowableOneSidednessCurr, False)
        self.register_field(TotNoOrders, True)
        self.register_field(LastFragment, False)

        class NoOrdersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ClOrdID, True)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(ListSeqNo, True)
                self.register_field(ClOrdLinkID, False)
                self.register_field(SettlInstMode, False)

                class NoPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartyID, False)
                        self.register_field(PartyIDSource, False)
                        self.register_field(PartyRole, False)

                        class NoPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(PartySubID, False)
                                self.register_field(PartySubIDType, False)

                        self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

                self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
                self.register_field(TradeOriginationDate, False)
                self.register_field(TradeDate, False)
                self.register_field(Account, False)
                self.register_field(AcctIDSource, False)
                self.register_field(AccountType, False)
                self.register_field(DayBookingInst, False)
                self.register_field(BookingUnit, False)
                self.register_field(AllocID, False)
                self.register_field(PreallocMethod, False)

                class NoAllocsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(AllocAccount, False)
                        self.register_field(AllocAcctIDSource, False)
                        self.register_field(AllocSettlCurrency, False)
                        self.register_field(IndividualAllocID, False)

                        class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartyID, False)
                                self.register_field(NestedPartyIDSource, False)
                                self.register_field(NestedPartyRole, False)

                                class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(NestedPartySubID, False)
                                        self.register_field(NestedPartySubIDType, False)

                                self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                        self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                        self.register_field(AllocQty, False)

                self.register_group(NoAllocs, NoAllocsGroup, False)
                self.register_field(SettlType, False)
                self.register_field(SettlDate, False)
                self.register_field(CashMargin, False)
                self.register_field(ClearingFeeIndicator, False)
                self.register_field(HandlInst, False)
                self.register_field(ExecInst, False)
                self.register_field(MinQty, False)
                self.register_field(MaxFloor, False)
                self.register_field(ExDestination, False)

                class NoTradingSessionsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(TradingSessionID, False)
                        self.register_field(TradingSessionSubID, False)

                self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
                self.register_field(ProcessCode, False)
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)

                class NoUnderlyingsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSymbol, False)
                        self.register_field(UnderlyingSymbolSfx, False)
                        self.register_field(UnderlyingSecurityID, False)
                        self.register_field(UnderlyingSecurityIDSource, False)

                        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingSecurityAltID, False)
                                self.register_field(UnderlyingSecurityAltIDSource, False)

                        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                        self.register_field(UnderlyingProduct, False)
                        self.register_field(UnderlyingCFICode, False)
                        self.register_field(UnderlyingSecurityType, False)
                        self.register_field(UnderlyingSecuritySubType, False)
                        self.register_field(UnderlyingMaturityMonthYear, False)
                        self.register_field(UnderlyingMaturityDate, False)
                        self.register_field(UnderlyingPutOrCall, False)
                        self.register_field(UnderlyingCouponPaymentDate, False)
                        self.register_field(UnderlyingIssueDate, False)
                        self.register_field(UnderlyingRepoCollateralSecurityType, False)
                        self.register_field(UnderlyingRepurchaseTerm, False)
                        self.register_field(UnderlyingRepurchaseRate, False)
                        self.register_field(UnderlyingFactor, False)
                        self.register_field(UnderlyingCreditRating, False)
                        self.register_field(UnderlyingInstrRegistry, False)
                        self.register_field(UnderlyingCountryOfIssue, False)
                        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                        self.register_field(UnderlyingLocaleOfIssue, False)
                        self.register_field(UnderlyingRedemptionDate, False)
                        self.register_field(UnderlyingStrikePrice, False)
                        self.register_field(UnderlyingStrikeCurrency, False)
                        self.register_field(UnderlyingOptAttribute, False)
                        self.register_field(UnderlyingContractMultiplier, False)
                        self.register_field(UnderlyingCouponRate, False)
                        self.register_field(UnderlyingSecurityExchange, False)
                        self.register_field(UnderlyingIssuer, False)
                        self.register_field(EncodedUnderlyingIssuerLen, False)
                        self.register_field(EncodedUnderlyingIssuer, False)
                        self.register_field(UnderlyingSecurityDesc, False)
                        self.register_field(EncodedUnderlyingSecurityDescLen, False)
                        self.register_field(EncodedUnderlyingSecurityDesc, False)
                        self.register_field(UnderlyingCPProgram, False)
                        self.register_field(UnderlyingCPRegType, False)
                        self.register_field(UnderlyingCurrency, False)
                        self.register_field(UnderlyingQty, False)
                        self.register_field(UnderlyingPx, False)
                        self.register_field(UnderlyingDirtyPrice, False)
                        self.register_field(UnderlyingEndPrice, False)
                        self.register_field(UnderlyingStartValue, False)
                        self.register_field(UnderlyingCurrentValue, False)
                        self.register_field(UnderlyingEndValue, False)

                        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingStipType, False)
                                self.register_field(UnderlyingStipValue, False)

                        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

                self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
                self.register_field(PrevClosePx, False)
                self.register_field(Side, True)
                self.register_field(SideValueInd, False)
                self.register_field(LocateReqd, False)
                self.register_field(TransactTime, False)

                class NoStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(StipulationType, False)
                        self.register_field(StipulationValue, False)

                self.register_group(NoStipulations, NoStipulationsGroup, False)
                self.register_field(QtyType, False)
                self.register_field(OrderQty, False)
                self.register_field(CashOrderQty, False)
                self.register_field(OrderPercent, False)
                self.register_field(RoundingDirection, False)
                self.register_field(RoundingModulus, False)
                self.register_field(OrdType, False)
                self.register_field(PriceType, False)
                self.register_field(Price, False)
                self.register_field(StopPx, False)
                self.register_field(Spread, False)
                self.register_field(BenchmarkCurveCurrency, False)
                self.register_field(BenchmarkCurveName, False)
                self.register_field(BenchmarkCurvePoint, False)
                self.register_field(BenchmarkPrice, False)
                self.register_field(BenchmarkPriceType, False)
                self.register_field(BenchmarkSecurityID, False)
                self.register_field(BenchmarkSecurityIDSource, False)
                self.register_field(YieldType, False)
                self.register_field(Yield, False)
                self.register_field(YieldCalcDate, False)
                self.register_field(YieldRedemptionDate, False)
                self.register_field(YieldRedemptionPrice, False)
                self.register_field(YieldRedemptionPriceType, False)
                self.register_field(Currency, False)
                self.register_field(ComplianceID, False)
                self.register_field(SolicitedFlag, False)
                self.register_field(IOIID, False)
                self.register_field(QuoteID, False)
                self.register_field(TimeInForce, False)
                self.register_field(EffectiveTime, False)
                self.register_field(ExpireDate, False)
                self.register_field(ExpireTime, False)
                self.register_field(GTBookingInst, False)
                self.register_field(Commission, False)
                self.register_field(CommType, False)
                self.register_field(CommCurrency, False)
                self.register_field(FundRenewWaiv, False)
                self.register_field(OrderCapacity, False)
                self.register_field(OrderRestrictions, False)
                self.register_field(CustOrderCapacity, False)
                self.register_field(ForexReq, False)
                self.register_field(SettlCurrency, False)
                self.register_field(BookingType, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)
                self.register_field(SettlDate2, False)
                self.register_field(OrderQty2, False)
                self.register_field(Price2, False)
                self.register_field(PositionEffect, False)
                self.register_field(CoveredOrUncovered, False)
                self.register_field(MaxShow, False)
                self.register_field(PegOffsetValue, False)
                self.register_field(PegMoveType, False)
                self.register_field(PegOffsetType, False)
                self.register_field(PegLimitType, False)
                self.register_field(PegRoundDirection, False)
                self.register_field(PegScope, False)
                self.register_field(DiscretionInst, False)
                self.register_field(DiscretionOffsetValue, False)
                self.register_field(DiscretionMoveType, False)
                self.register_field(DiscretionOffsetType, False)
                self.register_field(DiscretionLimitType, False)
                self.register_field(DiscretionRoundDirection, False)
                self.register_field(DiscretionScope, False)
                self.register_field(TargetStrategy, False)
                self.register_field(TargetStrategyParameters, False)
                self.register_field(ParticipationRate, False)
                self.register_field(Designation, False)

        self.register_group(NoOrders, NoOrdersGroup, True)

MESSAGE_TYPES['E'] = NewOrderList

class OrderCancelRequest(fix_message.MessageBase):
    _msgtype = 'F'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(OrigClOrdID, True)
        self.register_field(OrderID, False)
        self.register_field(ClOrdID, True)
        self.register_field(SecondaryClOrdID, False)
        self.register_field(ClOrdLinkID, False)
        self.register_field(ListID, False)
        self.register_field(OrigOrdModTime, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(Side, True)
        self.register_field(TransactTime, True)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(ComplianceID, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['F'] = OrderCancelRequest

class OrderCancelReplaceRequest(fix_message.MessageBase):
    _msgtype = 'G'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(OrderID, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(TradeOriginationDate, False)
        self.register_field(TradeDate, False)
        self.register_field(OrigClOrdID, True)
        self.register_field(ClOrdID, True)
        self.register_field(SecondaryClOrdID, False)
        self.register_field(ClOrdLinkID, False)
        self.register_field(ListID, False)
        self.register_field(OrigOrdModTime, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(DayBookingInst, False)
        self.register_field(BookingUnit, False)
        self.register_field(PreallocMethod, False)
        self.register_field(AllocID, False)

        class NoAllocsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AllocAccount, False)
                self.register_field(AllocAcctIDSource, False)
                self.register_field(AllocSettlCurrency, False)
                self.register_field(IndividualAllocID, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(AllocQty, False)

        self.register_group(NoAllocs, NoAllocsGroup, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(CashMargin, False)
        self.register_field(ClearingFeeIndicator, False)
        self.register_field(HandlInst, False)
        self.register_field(ExecInst, False)
        self.register_field(MinQty, False)
        self.register_field(MaxFloor, False)
        self.register_field(ExDestination, False)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(Side, True)
        self.register_field(TransactTime, True)
        self.register_field(QtyType, False)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(OrdType, True)
        self.register_field(PriceType, False)
        self.register_field(Price, False)
        self.register_field(StopPx, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)
        self.register_field(PegOffsetValue, False)
        self.register_field(PegMoveType, False)
        self.register_field(PegOffsetType, False)
        self.register_field(PegLimitType, False)
        self.register_field(PegRoundDirection, False)
        self.register_field(PegScope, False)
        self.register_field(DiscretionInst, False)
        self.register_field(DiscretionOffsetValue, False)
        self.register_field(DiscretionMoveType, False)
        self.register_field(DiscretionOffsetType, False)
        self.register_field(DiscretionLimitType, False)
        self.register_field(DiscretionRoundDirection, False)
        self.register_field(DiscretionScope, False)
        self.register_field(TargetStrategy, False)
        self.register_field(TargetStrategyParameters, False)
        self.register_field(ParticipationRate, False)
        self.register_field(ComplianceID, False)
        self.register_field(SolicitedFlag, False)
        self.register_field(Currency, False)
        self.register_field(TimeInForce, False)
        self.register_field(EffectiveTime, False)
        self.register_field(ExpireDate, False)
        self.register_field(ExpireTime, False)
        self.register_field(GTBookingInst, False)
        self.register_field(Commission, False)
        self.register_field(CommType, False)
        self.register_field(CommCurrency, False)
        self.register_field(FundRenewWaiv, False)
        self.register_field(OrderCapacity, False)
        self.register_field(OrderRestrictions, False)
        self.register_field(CustOrderCapacity, False)
        self.register_field(ForexReq, False)
        self.register_field(SettlCurrency, False)
        self.register_field(BookingType, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(SettlDate2, False)
        self.register_field(OrderQty2, False)
        self.register_field(Price2, False)
        self.register_field(PositionEffect, False)
        self.register_field(CoveredOrUncovered, False)
        self.register_field(MaxShow, False)
        self.register_field(LocateReqd, False)
        self.register_field(CancellationRights, False)
        self.register_field(MoneyLaunderingStatus, False)
        self.register_field(RegistID, False)
        self.register_field(Designation, False)

MESSAGE_TYPES['G'] = OrderCancelReplaceRequest

class OrderStatusRequest(fix_message.MessageBase):
    _msgtype = 'H'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(OrderID, False)
        self.register_field(ClOrdID, True)
        self.register_field(SecondaryClOrdID, False)
        self.register_field(ClOrdLinkID, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(OrdStatusReqID, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(Side, True)

MESSAGE_TYPES['H'] = OrderStatusRequest

class AllocationInstruction(fix_message.MessageBase):
    _msgtype = 'J'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(AllocID, True)
        self.register_field(AllocTransType, True)
        self.register_field(AllocType, True)
        self.register_field(SecondaryAllocID, False)
        self.register_field(RefAllocID, False)
        self.register_field(AllocCancReplaceReason, False)
        self.register_field(AllocIntermedReqType, False)
        self.register_field(AllocLinkID, False)
        self.register_field(AllocLinkType, False)
        self.register_field(BookingRefID, False)
        self.register_field(AllocNoOrdersType, True)

        class NoOrdersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ClOrdID, False)
                self.register_field(OrderID, False)
                self.register_field(SecondaryOrderID, False)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(ListID, False)

                class NoNested2PartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(Nested2PartyID, False)
                        self.register_field(Nested2PartyIDSource, False)
                        self.register_field(Nested2PartyRole, False)

                        class NoNested2PartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(Nested2PartySubID, False)
                                self.register_field(Nested2PartySubIDType, False)

                        self.register_group(NoNested2PartySubIDs, NoNested2PartySubIDsGroup, False)

                self.register_group(NoNested2PartyIDs, NoNested2PartyIDsGroup, False)
                self.register_field(OrderQty, False)
                self.register_field(OrderAvgPx, False)
                self.register_field(OrderBookingQty, False)

        self.register_group(NoOrders, NoOrdersGroup, False)

        class NoExecsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LastQty, False)
                self.register_field(ExecID, False)
                self.register_field(SecondaryExecID, False)
                self.register_field(LastPx, False)
                self.register_field(LastParPx, False)
                self.register_field(LastCapacity, False)

        self.register_group(NoExecs, NoExecsGroup, False)
        self.register_field(PreviouslyReported, False)
        self.register_field(ReversalIndicator, False)
        self.register_field(MatchType, False)
        self.register_field(Side, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(DeliveryForm, False)
        self.register_field(PctAtRisk, False)

        class NoInstrAttribGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(InstrAttribType, False)
                self.register_field(InstrAttribValue, False)

        self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(Quantity, True)
        self.register_field(QtyType, False)
        self.register_field(LastMkt, False)
        self.register_field(TradeOriginationDate, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(PriceType, False)
        self.register_field(AvgPx, True)
        self.register_field(AvgParPx, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(Currency, False)
        self.register_field(AvgPxPrecision, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(TradeDate, True)
        self.register_field(TransactTime, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(BookingType, False)
        self.register_field(GrossTradeAmt, False)
        self.register_field(Concession, False)
        self.register_field(TotalTakedown, False)
        self.register_field(NetMoney, False)
        self.register_field(PositionEffect, False)
        self.register_field(AutoAcceptIndicator, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(NumDaysInterest, False)
        self.register_field(AccruedInterestRate, False)
        self.register_field(AccruedInterestAmt, False)
        self.register_field(TotalAccruedInterestAmt, False)
        self.register_field(InterestAtMaturity, False)
        self.register_field(EndAccruedInterestAmt, False)
        self.register_field(StartCash, False)
        self.register_field(EndCash, False)
        self.register_field(LegalConfirm, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)
        self.register_field(TotNoAllocs, False)
        self.register_field(LastFragment, False)

        class NoAllocsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AllocAccount, False)
                self.register_field(AllocAcctIDSource, False)
                self.register_field(MatchStatus, False)
                self.register_field(AllocPrice, False)
                self.register_field(AllocQty, False)
                self.register_field(IndividualAllocID, False)
                self.register_field(ProcessCode, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(NotifyBrokerOfCredit, False)
                self.register_field(AllocHandlInst, False)
                self.register_field(AllocText, False)
                self.register_field(EncodedAllocTextLen, False)
                self.register_field(EncodedAllocText, False)
                self.register_field(Commission, False)
                self.register_field(CommType, False)
                self.register_field(CommCurrency, False)
                self.register_field(FundRenewWaiv, False)
                self.register_field(AllocAvgPx, False)
                self.register_field(AllocNetMoney, False)
                self.register_field(SettlCurrAmt, False)
                self.register_field(AllocSettlCurrAmt, False)
                self.register_field(SettlCurrency, False)
                self.register_field(AllocSettlCurrency, False)
                self.register_field(SettlCurrFxRate, False)
                self.register_field(SettlCurrFxRateCalc, False)
                self.register_field(AllocAccruedInterestAmt, False)
                self.register_field(AllocInterestAtMaturity, False)

                class NoMiscFeesGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(MiscFeeAmt, False)
                        self.register_field(MiscFeeCurr, False)
                        self.register_field(MiscFeeType, False)
                        self.register_field(MiscFeeBasis, False)

                self.register_group(NoMiscFees, NoMiscFeesGroup, False)

                class NoClearingInstructionsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(ClearingInstruction, False)

                self.register_group(NoClearingInstructions, NoClearingInstructionsGroup, False)
                self.register_field(AllocSettlInstType, False)
                self.register_field(SettlDeliveryType, False)
                self.register_field(StandInstDbType, False)
                self.register_field(StandInstDbName, False)
                self.register_field(StandInstDbID, False)

                class NoDlvyInstGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SettlInstSource, False)
                        self.register_field(DlvyInstType, False)

                        class NoSettlPartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(SettlPartyID, False)
                                self.register_field(SettlPartyIDSource, False)
                                self.register_field(SettlPartyRole, False)

                                class NoSettlPartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(SettlPartySubID, False)
                                        self.register_field(SettlPartySubIDType, False)

                                self.register_group(NoSettlPartySubIDs, NoSettlPartySubIDsGroup, False)

                        self.register_group(NoSettlPartyIDs, NoSettlPartyIDsGroup, False)

                self.register_group(NoDlvyInst, NoDlvyInstGroup, False)

        self.register_group(NoAllocs, NoAllocsGroup, False)

MESSAGE_TYPES['J'] = AllocationInstruction

class ListCancelRequest(fix_message.MessageBase):
    _msgtype = 'K'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ListID, True)
        self.register_field(TransactTime, True)
        self.register_field(TradeOriginationDate, False)
        self.register_field(TradeDate, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['K'] = ListCancelRequest

class ListExecute(fix_message.MessageBase):
    _msgtype = 'L'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ListID, True)
        self.register_field(ClientBidID, False)
        self.register_field(BidID, False)
        self.register_field(TransactTime, True)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['L'] = ListExecute

class ListStatusRequest(fix_message.MessageBase):
    _msgtype = 'M'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ListID, True)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['M'] = ListStatusRequest

class ListStatus(fix_message.MessageBase):
    _msgtype = 'N'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ListID, True)
        self.register_field(ListStatusType, True)
        self.register_field(NoRpts, True)
        self.register_field(ListOrderStatus, True)
        self.register_field(RptSeq, True)
        self.register_field(ListStatusText, False)
        self.register_field(EncodedListStatusTextLen, False)
        self.register_field(EncodedListStatusText, False)
        self.register_field(TransactTime, False)
        self.register_field(TotNoOrders, True)
        self.register_field(LastFragment, False)

        class NoOrdersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ClOrdID, True)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(CumQty, True)
                self.register_field(OrdStatus, True)
                self.register_field(WorkingIndicator, False)
                self.register_field(LeavesQty, True)
                self.register_field(CxlQty, True)
                self.register_field(AvgPx, True)
                self.register_field(OrdRejReason, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)

        self.register_group(NoOrders, NoOrdersGroup, True)

MESSAGE_TYPES['N'] = ListStatus

class AllocationInstructionAck(fix_message.MessageBase):
    _msgtype = 'P'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(AllocID, True)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(SecondaryAllocID, False)
        self.register_field(TradeDate, False)
        self.register_field(TransactTime, True)
        self.register_field(AllocStatus, True)
        self.register_field(AllocRejCode, False)
        self.register_field(AllocType, False)
        self.register_field(AllocIntermedReqType, False)
        self.register_field(MatchStatus, False)
        self.register_field(Product, False)
        self.register_field(SecurityType, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

        class NoAllocsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AllocAccount, False)
                self.register_field(AllocAcctIDSource, False)
                self.register_field(AllocPrice, False)
                self.register_field(IndividualAllocID, False)
                self.register_field(IndividualAllocRejCode, False)
                self.register_field(AllocText, False)
                self.register_field(EncodedAllocTextLen, False)
                self.register_field(EncodedAllocText, False)

        self.register_group(NoAllocs, NoAllocsGroup, False)

MESSAGE_TYPES['P'] = AllocationInstructionAck

class DontKnowTrade(fix_message.MessageBase):
    _msgtype = 'Q'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(OrderID, True)
        self.register_field(SecondaryOrderID, False)
        self.register_field(ExecID, True)
        self.register_field(DKReason, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(Side, True)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(LastQty, False)
        self.register_field(LastPx, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['Q'] = DontKnowTrade

class QuoteRequest(fix_message.MessageBase):
    _msgtype = 'R'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(QuoteReqID, True)
        self.register_field(RFQReqID, False)
        self.register_field(ClOrdID, False)
        self.register_field(OrderCapacity, False)

        class NoRelatedSymGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)
                self.register_field(AgreementDesc, False)
                self.register_field(AgreementID, False)
                self.register_field(AgreementDate, False)
                self.register_field(AgreementCurrency, False)
                self.register_field(TerminationType, False)
                self.register_field(StartDate, False)
                self.register_field(EndDate, False)
                self.register_field(DeliveryType, False)
                self.register_field(MarginRatio, False)

                class NoUnderlyingsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSymbol, False)
                        self.register_field(UnderlyingSymbolSfx, False)
                        self.register_field(UnderlyingSecurityID, False)
                        self.register_field(UnderlyingSecurityIDSource, False)

                        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingSecurityAltID, False)
                                self.register_field(UnderlyingSecurityAltIDSource, False)

                        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                        self.register_field(UnderlyingProduct, False)
                        self.register_field(UnderlyingCFICode, False)
                        self.register_field(UnderlyingSecurityType, False)
                        self.register_field(UnderlyingSecuritySubType, False)
                        self.register_field(UnderlyingMaturityMonthYear, False)
                        self.register_field(UnderlyingMaturityDate, False)
                        self.register_field(UnderlyingPutOrCall, False)
                        self.register_field(UnderlyingCouponPaymentDate, False)
                        self.register_field(UnderlyingIssueDate, False)
                        self.register_field(UnderlyingRepoCollateralSecurityType, False)
                        self.register_field(UnderlyingRepurchaseTerm, False)
                        self.register_field(UnderlyingRepurchaseRate, False)
                        self.register_field(UnderlyingFactor, False)
                        self.register_field(UnderlyingCreditRating, False)
                        self.register_field(UnderlyingInstrRegistry, False)
                        self.register_field(UnderlyingCountryOfIssue, False)
                        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                        self.register_field(UnderlyingLocaleOfIssue, False)
                        self.register_field(UnderlyingRedemptionDate, False)
                        self.register_field(UnderlyingStrikePrice, False)
                        self.register_field(UnderlyingStrikeCurrency, False)
                        self.register_field(UnderlyingOptAttribute, False)
                        self.register_field(UnderlyingContractMultiplier, False)
                        self.register_field(UnderlyingCouponRate, False)
                        self.register_field(UnderlyingSecurityExchange, False)
                        self.register_field(UnderlyingIssuer, False)
                        self.register_field(EncodedUnderlyingIssuerLen, False)
                        self.register_field(EncodedUnderlyingIssuer, False)
                        self.register_field(UnderlyingSecurityDesc, False)
                        self.register_field(EncodedUnderlyingSecurityDescLen, False)
                        self.register_field(EncodedUnderlyingSecurityDesc, False)
                        self.register_field(UnderlyingCPProgram, False)
                        self.register_field(UnderlyingCPRegType, False)
                        self.register_field(UnderlyingCurrency, False)
                        self.register_field(UnderlyingQty, False)
                        self.register_field(UnderlyingPx, False)
                        self.register_field(UnderlyingDirtyPrice, False)
                        self.register_field(UnderlyingEndPrice, False)
                        self.register_field(UnderlyingStartValue, False)
                        self.register_field(UnderlyingCurrentValue, False)
                        self.register_field(UnderlyingEndValue, False)

                        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingStipType, False)
                                self.register_field(UnderlyingStipValue, False)

                        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

                self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
                self.register_field(PrevClosePx, False)
                self.register_field(QuoteRequestType, False)
                self.register_field(QuoteType, False)
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)
                self.register_field(TradeOriginationDate, False)
                self.register_field(Side, False)
                self.register_field(QtyType, False)
                self.register_field(OrderQty, False)
                self.register_field(CashOrderQty, False)
                self.register_field(OrderPercent, False)
                self.register_field(RoundingDirection, False)
                self.register_field(RoundingModulus, False)
                self.register_field(SettlType, False)
                self.register_field(SettlDate, False)
                self.register_field(SettlDate2, False)
                self.register_field(OrderQty2, False)
                self.register_field(Currency, False)

                class NoStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(StipulationType, False)
                        self.register_field(StipulationValue, False)

                self.register_group(NoStipulations, NoStipulationsGroup, False)
                self.register_field(Account, False)
                self.register_field(AcctIDSource, False)
                self.register_field(AccountType, False)

                class NoLegsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSymbol, False)
                        self.register_field(LegSymbolSfx, False)
                        self.register_field(LegSecurityID, False)
                        self.register_field(LegSecurityIDSource, False)

                        class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegSecurityAltID, False)
                                self.register_field(LegSecurityAltIDSource, False)

                        self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                        self.register_field(LegProduct, False)
                        self.register_field(LegCFICode, False)
                        self.register_field(LegSecurityType, False)
                        self.register_field(LegSecuritySubType, False)
                        self.register_field(LegMaturityMonthYear, False)
                        self.register_field(LegMaturityDate, False)
                        self.register_field(LegCouponPaymentDate, False)
                        self.register_field(LegIssueDate, False)
                        self.register_field(LegRepoCollateralSecurityType, False)
                        self.register_field(LegRepurchaseTerm, False)
                        self.register_field(LegRepurchaseRate, False)
                        self.register_field(LegFactor, False)
                        self.register_field(LegCreditRating, False)
                        self.register_field(LegInstrRegistry, False)
                        self.register_field(LegCountryOfIssue, False)
                        self.register_field(LegStateOrProvinceOfIssue, False)
                        self.register_field(LegLocaleOfIssue, False)
                        self.register_field(LegRedemptionDate, False)
                        self.register_field(LegStrikePrice, False)
                        self.register_field(LegStrikeCurrency, False)
                        self.register_field(LegOptAttribute, False)
                        self.register_field(LegContractMultiplier, False)
                        self.register_field(LegCouponRate, False)
                        self.register_field(LegSecurityExchange, False)
                        self.register_field(LegIssuer, False)
                        self.register_field(EncodedLegIssuerLen, False)
                        self.register_field(EncodedLegIssuer, False)
                        self.register_field(LegSecurityDesc, False)
                        self.register_field(EncodedLegSecurityDescLen, False)
                        self.register_field(EncodedLegSecurityDesc, False)
                        self.register_field(LegRatioQty, False)
                        self.register_field(LegSide, False)
                        self.register_field(LegCurrency, False)
                        self.register_field(LegPool, False)
                        self.register_field(LegDatedDate, False)
                        self.register_field(LegContractSettlMonth, False)
                        self.register_field(LegInterestAccrualDate, False)
                        self.register_field(LegQty, False)
                        self.register_field(LegSwapType, False)
                        self.register_field(LegSettlType, False)
                        self.register_field(LegSettlDate, False)

                        class NoLegStipulationsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegStipulationType, False)
                                self.register_field(LegStipulationValue, False)

                        self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)

                        class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartyID, False)
                                self.register_field(NestedPartyIDSource, False)
                                self.register_field(NestedPartyRole, False)

                                class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(NestedPartySubID, False)
                                        self.register_field(NestedPartySubIDType, False)

                                self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                        self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                        self.register_field(LegBenchmarkCurveCurrency, False)
                        self.register_field(LegBenchmarkCurveName, False)
                        self.register_field(LegBenchmarkCurvePoint, False)
                        self.register_field(LegBenchmarkPrice, False)
                        self.register_field(LegBenchmarkPriceType, False)

                self.register_group(NoLegs, NoLegsGroup, False)

                class NoQuoteQualifiersGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(QuoteQualifier, False)

                self.register_group(NoQuoteQualifiers, NoQuoteQualifiersGroup, False)
                self.register_field(QuotePriceType, False)
                self.register_field(OrdType, False)
                self.register_field(ValidUntilTime, False)
                self.register_field(ExpireTime, False)
                self.register_field(TransactTime, False)
                self.register_field(Spread, False)
                self.register_field(BenchmarkCurveCurrency, False)
                self.register_field(BenchmarkCurveName, False)
                self.register_field(BenchmarkCurvePoint, False)
                self.register_field(BenchmarkPrice, False)
                self.register_field(BenchmarkPriceType, False)
                self.register_field(BenchmarkSecurityID, False)
                self.register_field(BenchmarkSecurityIDSource, False)
                self.register_field(PriceType, False)
                self.register_field(Price, False)
                self.register_field(Price2, False)
                self.register_field(YieldType, False)
                self.register_field(Yield, False)
                self.register_field(YieldCalcDate, False)
                self.register_field(YieldRedemptionDate, False)
                self.register_field(YieldRedemptionPrice, False)
                self.register_field(YieldRedemptionPriceType, False)

                class NoPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartyID, False)
                        self.register_field(PartyIDSource, False)
                        self.register_field(PartyRole, False)

                        class NoPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(PartySubID, False)
                                self.register_field(PartySubIDType, False)

                        self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

                self.register_group(NoPartyIDs, NoPartyIDsGroup, False)

        self.register_group(NoRelatedSym, NoRelatedSymGroup, True)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['R'] = QuoteRequest

class Quote(fix_message.MessageBase):
    _msgtype = 'S'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(QuoteReqID, False)
        self.register_field(QuoteID, True)
        self.register_field(QuoteRespID, False)
        self.register_field(QuoteType, False)

        class NoQuoteQualifiersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(QuoteQualifier, False)

        self.register_group(NoQuoteQualifiers, NoQuoteQualifiersGroup, False)
        self.register_field(QuoteResponseLevel, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(Side, False)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(SettlDate2, False)
        self.register_field(OrderQty2, False)
        self.register_field(Currency, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)
                self.register_field(LegQty, False)
                self.register_field(LegSwapType, False)
                self.register_field(LegSettlType, False)
                self.register_field(LegSettlDate, False)

                class NoLegStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegStipulationType, False)
                        self.register_field(LegStipulationValue, False)

                self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(LegPriceType, False)
                self.register_field(LegBidPx, False)
                self.register_field(LegOfferPx, False)
                self.register_field(LegBenchmarkCurveCurrency, False)
                self.register_field(LegBenchmarkCurveName, False)
                self.register_field(LegBenchmarkCurvePoint, False)
                self.register_field(LegBenchmarkPrice, False)
                self.register_field(LegBenchmarkPriceType, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(BidPx, False)
        self.register_field(OfferPx, False)
        self.register_field(MktBidPx, False)
        self.register_field(MktOfferPx, False)
        self.register_field(MinBidSize, False)
        self.register_field(BidSize, False)
        self.register_field(MinOfferSize, False)
        self.register_field(OfferSize, False)
        self.register_field(ValidUntilTime, False)
        self.register_field(BidSpotRate, False)
        self.register_field(OfferSpotRate, False)
        self.register_field(BidForwardPoints, False)
        self.register_field(OfferForwardPoints, False)
        self.register_field(MidPx, False)
        self.register_field(BidYield, False)
        self.register_field(MidYield, False)
        self.register_field(OfferYield, False)
        self.register_field(TransactTime, False)
        self.register_field(OrdType, False)
        self.register_field(BidForwardPoints2, False)
        self.register_field(OfferForwardPoints2, False)
        self.register_field(SettlCurrBidFxRate, False)
        self.register_field(SettlCurrOfferFxRate, False)
        self.register_field(SettlCurrFxRateCalc, False)
        self.register_field(CommType, False)
        self.register_field(Commission, False)
        self.register_field(CustOrderCapacity, False)
        self.register_field(ExDestination, False)
        self.register_field(OrderCapacity, False)
        self.register_field(PriceType, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['S'] = Quote

class SettlementInstructions(fix_message.MessageBase):
    _msgtype = 'T'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SettlInstMsgID, True)
        self.register_field(SettlInstReqID, False)
        self.register_field(SettlInstMode, True)
        self.register_field(SettlInstReqRejCode, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(ClOrdID, False)
        self.register_field(TransactTime, True)

        class NoSettlInstGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SettlInstID, False)
                self.register_field(SettlInstTransType, False)
                self.register_field(SettlInstRefID, False)

                class NoPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartyID, False)
                        self.register_field(PartyIDSource, False)
                        self.register_field(PartyRole, False)

                        class NoPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(PartySubID, False)
                                self.register_field(PartySubIDType, False)

                        self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

                self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
                self.register_field(Side, False)
                self.register_field(Product, False)
                self.register_field(SecurityType, False)
                self.register_field(CFICode, False)
                self.register_field(EffectiveTime, False)
                self.register_field(ExpireTime, False)
                self.register_field(LastUpdateTime, False)
                self.register_field(SettlDeliveryType, False)
                self.register_field(StandInstDbType, False)
                self.register_field(StandInstDbName, False)
                self.register_field(StandInstDbID, False)

                class NoDlvyInstGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SettlInstSource, False)
                        self.register_field(DlvyInstType, False)

                        class NoSettlPartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(SettlPartyID, False)
                                self.register_field(SettlPartyIDSource, False)
                                self.register_field(SettlPartyRole, False)

                                class NoSettlPartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(SettlPartySubID, False)
                                        self.register_field(SettlPartySubIDType, False)

                                self.register_group(NoSettlPartySubIDs, NoSettlPartySubIDsGroup, False)

                        self.register_group(NoSettlPartyIDs, NoSettlPartyIDsGroup, False)

                self.register_group(NoDlvyInst, NoDlvyInstGroup, False)
                self.register_field(PaymentMethod, False)
                self.register_field(PaymentRef, False)
                self.register_field(CardHolderName, False)
                self.register_field(CardNumber, False)
                self.register_field(CardStartDate, False)
                self.register_field(CardExpDate, False)
                self.register_field(CardIssNum, False)
                self.register_field(PaymentDate, False)
                self.register_field(PaymentRemitterID, False)

        self.register_group(NoSettlInst, NoSettlInstGroup, False)

MESSAGE_TYPES['T'] = SettlementInstructions

class MarketDataRequest(fix_message.MessageBase):
    _msgtype = 'V'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(MDReqID, True)
        self.register_field(SubscriptionRequestType, True)
        self.register_field(MarketDepth, True)
        self.register_field(MDUpdateType, False)
        self.register_field(AggregatedBook, False)
        self.register_field(OpenCloseSettlFlag, False)
        self.register_field(Scope, False)
        self.register_field(MDImplicitDelete, False)

        class NoMDEntryTypesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(MDEntryType, True)

        self.register_group(NoMDEntryTypes, NoMDEntryTypesGroup, True)

        class NoRelatedSymGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)

                class NoUnderlyingsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSymbol, False)
                        self.register_field(UnderlyingSymbolSfx, False)
                        self.register_field(UnderlyingSecurityID, False)
                        self.register_field(UnderlyingSecurityIDSource, False)

                        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingSecurityAltID, False)
                                self.register_field(UnderlyingSecurityAltIDSource, False)

                        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                        self.register_field(UnderlyingProduct, False)
                        self.register_field(UnderlyingCFICode, False)
                        self.register_field(UnderlyingSecurityType, False)
                        self.register_field(UnderlyingSecuritySubType, False)
                        self.register_field(UnderlyingMaturityMonthYear, False)
                        self.register_field(UnderlyingMaturityDate, False)
                        self.register_field(UnderlyingPutOrCall, False)
                        self.register_field(UnderlyingCouponPaymentDate, False)
                        self.register_field(UnderlyingIssueDate, False)
                        self.register_field(UnderlyingRepoCollateralSecurityType, False)
                        self.register_field(UnderlyingRepurchaseTerm, False)
                        self.register_field(UnderlyingRepurchaseRate, False)
                        self.register_field(UnderlyingFactor, False)
                        self.register_field(UnderlyingCreditRating, False)
                        self.register_field(UnderlyingInstrRegistry, False)
                        self.register_field(UnderlyingCountryOfIssue, False)
                        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                        self.register_field(UnderlyingLocaleOfIssue, False)
                        self.register_field(UnderlyingRedemptionDate, False)
                        self.register_field(UnderlyingStrikePrice, False)
                        self.register_field(UnderlyingStrikeCurrency, False)
                        self.register_field(UnderlyingOptAttribute, False)
                        self.register_field(UnderlyingContractMultiplier, False)
                        self.register_field(UnderlyingCouponRate, False)
                        self.register_field(UnderlyingSecurityExchange, False)
                        self.register_field(UnderlyingIssuer, False)
                        self.register_field(EncodedUnderlyingIssuerLen, False)
                        self.register_field(EncodedUnderlyingIssuer, False)
                        self.register_field(UnderlyingSecurityDesc, False)
                        self.register_field(EncodedUnderlyingSecurityDescLen, False)
                        self.register_field(EncodedUnderlyingSecurityDesc, False)
                        self.register_field(UnderlyingCPProgram, False)
                        self.register_field(UnderlyingCPRegType, False)
                        self.register_field(UnderlyingCurrency, False)
                        self.register_field(UnderlyingQty, False)
                        self.register_field(UnderlyingPx, False)
                        self.register_field(UnderlyingDirtyPrice, False)
                        self.register_field(UnderlyingEndPrice, False)
                        self.register_field(UnderlyingStartValue, False)
                        self.register_field(UnderlyingCurrentValue, False)
                        self.register_field(UnderlyingEndValue, False)

                        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingStipType, False)
                                self.register_field(UnderlyingStipValue, False)

                        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

                self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

                class NoLegsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSymbol, False)
                        self.register_field(LegSymbolSfx, False)
                        self.register_field(LegSecurityID, False)
                        self.register_field(LegSecurityIDSource, False)

                        class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegSecurityAltID, False)
                                self.register_field(LegSecurityAltIDSource, False)

                        self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                        self.register_field(LegProduct, False)
                        self.register_field(LegCFICode, False)
                        self.register_field(LegSecurityType, False)
                        self.register_field(LegSecuritySubType, False)
                        self.register_field(LegMaturityMonthYear, False)
                        self.register_field(LegMaturityDate, False)
                        self.register_field(LegCouponPaymentDate, False)
                        self.register_field(LegIssueDate, False)
                        self.register_field(LegRepoCollateralSecurityType, False)
                        self.register_field(LegRepurchaseTerm, False)
                        self.register_field(LegRepurchaseRate, False)
                        self.register_field(LegFactor, False)
                        self.register_field(LegCreditRating, False)
                        self.register_field(LegInstrRegistry, False)
                        self.register_field(LegCountryOfIssue, False)
                        self.register_field(LegStateOrProvinceOfIssue, False)
                        self.register_field(LegLocaleOfIssue, False)
                        self.register_field(LegRedemptionDate, False)
                        self.register_field(LegStrikePrice, False)
                        self.register_field(LegStrikeCurrency, False)
                        self.register_field(LegOptAttribute, False)
                        self.register_field(LegContractMultiplier, False)
                        self.register_field(LegCouponRate, False)
                        self.register_field(LegSecurityExchange, False)
                        self.register_field(LegIssuer, False)
                        self.register_field(EncodedLegIssuerLen, False)
                        self.register_field(EncodedLegIssuer, False)
                        self.register_field(LegSecurityDesc, False)
                        self.register_field(EncodedLegSecurityDescLen, False)
                        self.register_field(EncodedLegSecurityDesc, False)
                        self.register_field(LegRatioQty, False)
                        self.register_field(LegSide, False)
                        self.register_field(LegCurrency, False)
                        self.register_field(LegPool, False)
                        self.register_field(LegDatedDate, False)
                        self.register_field(LegContractSettlMonth, False)
                        self.register_field(LegInterestAccrualDate, False)

                self.register_group(NoLegs, NoLegsGroup, False)

        self.register_group(NoRelatedSym, NoRelatedSymGroup, True)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(ApplQueueAction, False)
        self.register_field(ApplQueueMax, False)

MESSAGE_TYPES['V'] = MarketDataRequest

class MarketDataSnapshotFullRefresh(fix_message.MessageBase):
    _msgtype = 'W'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(MDReqID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(FinancialStatus, False)
        self.register_field(CorporateAction, False)
        self.register_field(NetChgPrevDay, False)

        class NoMDEntriesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(MDEntryType, True)
                self.register_field(MDEntryPx, False)
                self.register_field(Currency, False)
                self.register_field(MDEntrySize, False)
                self.register_field(MDEntryDate, False)
                self.register_field(MDEntryTime, False)
                self.register_field(TickDirection, False)
                self.register_field(MDMkt, False)
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)
                self.register_field(QuoteCondition, False)
                self.register_field(TradeCondition, False)
                self.register_field(MDEntryOriginator, False)
                self.register_field(LocationID, False)
                self.register_field(DeskID, False)
                self.register_field(OpenCloseSettlFlag, False)
                self.register_field(TimeInForce, False)
                self.register_field(ExpireDate, False)
                self.register_field(ExpireTime, False)
                self.register_field(MinQty, False)
                self.register_field(ExecInst, False)
                self.register_field(SellerDays, False)
                self.register_field(OrderID, False)
                self.register_field(QuoteEntryID, False)
                self.register_field(MDEntryBuyer, False)
                self.register_field(MDEntrySeller, False)
                self.register_field(NumberOfOrders, False)
                self.register_field(MDEntryPositionNo, False)
                self.register_field(Scope, False)
                self.register_field(PriceDelta, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)

        self.register_group(NoMDEntries, NoMDEntriesGroup, True)
        self.register_field(ApplQueueDepth, False)
        self.register_field(ApplQueueResolution, False)

MESSAGE_TYPES['W'] = MarketDataSnapshotFullRefresh

class MarketDataIncrementalRefresh(fix_message.MessageBase):
    _msgtype = 'X'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(MDReqID, False)

        class NoMDEntriesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(MDUpdateAction, True)
                self.register_field(DeleteReason, False)
                self.register_field(MDEntryType, False)
                self.register_field(MDEntryID, False)
                self.register_field(MDEntryRefID, False)
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)

                class NoUnderlyingsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSymbol, False)
                        self.register_field(UnderlyingSymbolSfx, False)
                        self.register_field(UnderlyingSecurityID, False)
                        self.register_field(UnderlyingSecurityIDSource, False)

                        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingSecurityAltID, False)
                                self.register_field(UnderlyingSecurityAltIDSource, False)

                        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                        self.register_field(UnderlyingProduct, False)
                        self.register_field(UnderlyingCFICode, False)
                        self.register_field(UnderlyingSecurityType, False)
                        self.register_field(UnderlyingSecuritySubType, False)
                        self.register_field(UnderlyingMaturityMonthYear, False)
                        self.register_field(UnderlyingMaturityDate, False)
                        self.register_field(UnderlyingPutOrCall, False)
                        self.register_field(UnderlyingCouponPaymentDate, False)
                        self.register_field(UnderlyingIssueDate, False)
                        self.register_field(UnderlyingRepoCollateralSecurityType, False)
                        self.register_field(UnderlyingRepurchaseTerm, False)
                        self.register_field(UnderlyingRepurchaseRate, False)
                        self.register_field(UnderlyingFactor, False)
                        self.register_field(UnderlyingCreditRating, False)
                        self.register_field(UnderlyingInstrRegistry, False)
                        self.register_field(UnderlyingCountryOfIssue, False)
                        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                        self.register_field(UnderlyingLocaleOfIssue, False)
                        self.register_field(UnderlyingRedemptionDate, False)
                        self.register_field(UnderlyingStrikePrice, False)
                        self.register_field(UnderlyingStrikeCurrency, False)
                        self.register_field(UnderlyingOptAttribute, False)
                        self.register_field(UnderlyingContractMultiplier, False)
                        self.register_field(UnderlyingCouponRate, False)
                        self.register_field(UnderlyingSecurityExchange, False)
                        self.register_field(UnderlyingIssuer, False)
                        self.register_field(EncodedUnderlyingIssuerLen, False)
                        self.register_field(EncodedUnderlyingIssuer, False)
                        self.register_field(UnderlyingSecurityDesc, False)
                        self.register_field(EncodedUnderlyingSecurityDescLen, False)
                        self.register_field(EncodedUnderlyingSecurityDesc, False)
                        self.register_field(UnderlyingCPProgram, False)
                        self.register_field(UnderlyingCPRegType, False)
                        self.register_field(UnderlyingCurrency, False)
                        self.register_field(UnderlyingQty, False)
                        self.register_field(UnderlyingPx, False)
                        self.register_field(UnderlyingDirtyPrice, False)
                        self.register_field(UnderlyingEndPrice, False)
                        self.register_field(UnderlyingStartValue, False)
                        self.register_field(UnderlyingCurrentValue, False)
                        self.register_field(UnderlyingEndValue, False)

                        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingStipType, False)
                                self.register_field(UnderlyingStipValue, False)

                        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

                self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

                class NoLegsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSymbol, False)
                        self.register_field(LegSymbolSfx, False)
                        self.register_field(LegSecurityID, False)
                        self.register_field(LegSecurityIDSource, False)

                        class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegSecurityAltID, False)
                                self.register_field(LegSecurityAltIDSource, False)

                        self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                        self.register_field(LegProduct, False)
                        self.register_field(LegCFICode, False)
                        self.register_field(LegSecurityType, False)
                        self.register_field(LegSecuritySubType, False)
                        self.register_field(LegMaturityMonthYear, False)
                        self.register_field(LegMaturityDate, False)
                        self.register_field(LegCouponPaymentDate, False)
                        self.register_field(LegIssueDate, False)
                        self.register_field(LegRepoCollateralSecurityType, False)
                        self.register_field(LegRepurchaseTerm, False)
                        self.register_field(LegRepurchaseRate, False)
                        self.register_field(LegFactor, False)
                        self.register_field(LegCreditRating, False)
                        self.register_field(LegInstrRegistry, False)
                        self.register_field(LegCountryOfIssue, False)
                        self.register_field(LegStateOrProvinceOfIssue, False)
                        self.register_field(LegLocaleOfIssue, False)
                        self.register_field(LegRedemptionDate, False)
                        self.register_field(LegStrikePrice, False)
                        self.register_field(LegStrikeCurrency, False)
                        self.register_field(LegOptAttribute, False)
                        self.register_field(LegContractMultiplier, False)
                        self.register_field(LegCouponRate, False)
                        self.register_field(LegSecurityExchange, False)
                        self.register_field(LegIssuer, False)
                        self.register_field(EncodedLegIssuerLen, False)
                        self.register_field(EncodedLegIssuer, False)
                        self.register_field(LegSecurityDesc, False)
                        self.register_field(EncodedLegSecurityDescLen, False)
                        self.register_field(EncodedLegSecurityDesc, False)
                        self.register_field(LegRatioQty, False)
                        self.register_field(LegSide, False)
                        self.register_field(LegCurrency, False)
                        self.register_field(LegPool, False)
                        self.register_field(LegDatedDate, False)
                        self.register_field(LegContractSettlMonth, False)
                        self.register_field(LegInterestAccrualDate, False)

                self.register_group(NoLegs, NoLegsGroup, False)
                self.register_field(FinancialStatus, False)
                self.register_field(CorporateAction, False)
                self.register_field(MDEntryPx, False)
                self.register_field(Currency, False)
                self.register_field(MDEntrySize, False)
                self.register_field(MDEntryDate, False)
                self.register_field(MDEntryTime, False)
                self.register_field(TickDirection, False)
                self.register_field(MDMkt, False)
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)
                self.register_field(QuoteCondition, False)
                self.register_field(TradeCondition, False)
                self.register_field(MDEntryOriginator, False)
                self.register_field(LocationID, False)
                self.register_field(DeskID, False)
                self.register_field(OpenCloseSettlFlag, False)
                self.register_field(TimeInForce, False)
                self.register_field(ExpireDate, False)
                self.register_field(ExpireTime, False)
                self.register_field(MinQty, False)
                self.register_field(ExecInst, False)
                self.register_field(SellerDays, False)
                self.register_field(OrderID, False)
                self.register_field(QuoteEntryID, False)
                self.register_field(MDEntryBuyer, False)
                self.register_field(MDEntrySeller, False)
                self.register_field(NumberOfOrders, False)
                self.register_field(MDEntryPositionNo, False)
                self.register_field(Scope, False)
                self.register_field(PriceDelta, False)
                self.register_field(NetChgPrevDay, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)

        self.register_group(NoMDEntries, NoMDEntriesGroup, True)
        self.register_field(ApplQueueDepth, False)
        self.register_field(ApplQueueResolution, False)

MESSAGE_TYPES['X'] = MarketDataIncrementalRefresh

class MarketDataRequestReject(fix_message.MessageBase):
    _msgtype = 'Y'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(MDReqID, True)
        self.register_field(MDReqRejReason, False)

        class NoAltMDSourceGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AltMDSourceID, False)

        self.register_group(NoAltMDSource, NoAltMDSourceGroup, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['Y'] = MarketDataRequestReject

class QuoteCancel(fix_message.MessageBase):
    _msgtype = 'Z'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(QuoteReqID, False)
        self.register_field(QuoteID, True)
        self.register_field(QuoteCancelType, True)
        self.register_field(QuoteResponseLevel, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)

        class NoQuoteEntriesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)
                self.register_field(AgreementDesc, False)
                self.register_field(AgreementID, False)
                self.register_field(AgreementDate, False)
                self.register_field(AgreementCurrency, False)
                self.register_field(TerminationType, False)
                self.register_field(StartDate, False)
                self.register_field(EndDate, False)
                self.register_field(DeliveryType, False)
                self.register_field(MarginRatio, False)

                class NoUnderlyingsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSymbol, False)
                        self.register_field(UnderlyingSymbolSfx, False)
                        self.register_field(UnderlyingSecurityID, False)
                        self.register_field(UnderlyingSecurityIDSource, False)

                        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingSecurityAltID, False)
                                self.register_field(UnderlyingSecurityAltIDSource, False)

                        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                        self.register_field(UnderlyingProduct, False)
                        self.register_field(UnderlyingCFICode, False)
                        self.register_field(UnderlyingSecurityType, False)
                        self.register_field(UnderlyingSecuritySubType, False)
                        self.register_field(UnderlyingMaturityMonthYear, False)
                        self.register_field(UnderlyingMaturityDate, False)
                        self.register_field(UnderlyingPutOrCall, False)
                        self.register_field(UnderlyingCouponPaymentDate, False)
                        self.register_field(UnderlyingIssueDate, False)
                        self.register_field(UnderlyingRepoCollateralSecurityType, False)
                        self.register_field(UnderlyingRepurchaseTerm, False)
                        self.register_field(UnderlyingRepurchaseRate, False)
                        self.register_field(UnderlyingFactor, False)
                        self.register_field(UnderlyingCreditRating, False)
                        self.register_field(UnderlyingInstrRegistry, False)
                        self.register_field(UnderlyingCountryOfIssue, False)
                        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                        self.register_field(UnderlyingLocaleOfIssue, False)
                        self.register_field(UnderlyingRedemptionDate, False)
                        self.register_field(UnderlyingStrikePrice, False)
                        self.register_field(UnderlyingStrikeCurrency, False)
                        self.register_field(UnderlyingOptAttribute, False)
                        self.register_field(UnderlyingContractMultiplier, False)
                        self.register_field(UnderlyingCouponRate, False)
                        self.register_field(UnderlyingSecurityExchange, False)
                        self.register_field(UnderlyingIssuer, False)
                        self.register_field(EncodedUnderlyingIssuerLen, False)
                        self.register_field(EncodedUnderlyingIssuer, False)
                        self.register_field(UnderlyingSecurityDesc, False)
                        self.register_field(EncodedUnderlyingSecurityDescLen, False)
                        self.register_field(EncodedUnderlyingSecurityDesc, False)
                        self.register_field(UnderlyingCPProgram, False)
                        self.register_field(UnderlyingCPRegType, False)
                        self.register_field(UnderlyingCurrency, False)
                        self.register_field(UnderlyingQty, False)
                        self.register_field(UnderlyingPx, False)
                        self.register_field(UnderlyingDirtyPrice, False)
                        self.register_field(UnderlyingEndPrice, False)
                        self.register_field(UnderlyingStartValue, False)
                        self.register_field(UnderlyingCurrentValue, False)
                        self.register_field(UnderlyingEndValue, False)

                        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingStipType, False)
                                self.register_field(UnderlyingStipValue, False)

                        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

                self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

                class NoLegsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSymbol, False)
                        self.register_field(LegSymbolSfx, False)
                        self.register_field(LegSecurityID, False)
                        self.register_field(LegSecurityIDSource, False)

                        class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegSecurityAltID, False)
                                self.register_field(LegSecurityAltIDSource, False)

                        self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                        self.register_field(LegProduct, False)
                        self.register_field(LegCFICode, False)
                        self.register_field(LegSecurityType, False)
                        self.register_field(LegSecuritySubType, False)
                        self.register_field(LegMaturityMonthYear, False)
                        self.register_field(LegMaturityDate, False)
                        self.register_field(LegCouponPaymentDate, False)
                        self.register_field(LegIssueDate, False)
                        self.register_field(LegRepoCollateralSecurityType, False)
                        self.register_field(LegRepurchaseTerm, False)
                        self.register_field(LegRepurchaseRate, False)
                        self.register_field(LegFactor, False)
                        self.register_field(LegCreditRating, False)
                        self.register_field(LegInstrRegistry, False)
                        self.register_field(LegCountryOfIssue, False)
                        self.register_field(LegStateOrProvinceOfIssue, False)
                        self.register_field(LegLocaleOfIssue, False)
                        self.register_field(LegRedemptionDate, False)
                        self.register_field(LegStrikePrice, False)
                        self.register_field(LegStrikeCurrency, False)
                        self.register_field(LegOptAttribute, False)
                        self.register_field(LegContractMultiplier, False)
                        self.register_field(LegCouponRate, False)
                        self.register_field(LegSecurityExchange, False)
                        self.register_field(LegIssuer, False)
                        self.register_field(EncodedLegIssuerLen, False)
                        self.register_field(EncodedLegIssuer, False)
                        self.register_field(LegSecurityDesc, False)
                        self.register_field(EncodedLegSecurityDescLen, False)
                        self.register_field(EncodedLegSecurityDesc, False)
                        self.register_field(LegRatioQty, False)
                        self.register_field(LegSide, False)
                        self.register_field(LegCurrency, False)
                        self.register_field(LegPool, False)
                        self.register_field(LegDatedDate, False)
                        self.register_field(LegContractSettlMonth, False)
                        self.register_field(LegInterestAccrualDate, False)

                self.register_group(NoLegs, NoLegsGroup, False)

        self.register_group(NoQuoteEntries, NoQuoteEntriesGroup, False)

MESSAGE_TYPES['Z'] = QuoteCancel

class QuoteStatusRequest(fix_message.MessageBase):
    _msgtype = 'a'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(QuoteStatusReqID, False)
        self.register_field(QuoteID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(SubscriptionRequestType, False)

MESSAGE_TYPES['a'] = QuoteStatusRequest

class MassQuoteAcknowledgement(fix_message.MessageBase):
    _msgtype = 'b'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(QuoteReqID, False)
        self.register_field(QuoteID, False)
        self.register_field(QuoteStatus, True)
        self.register_field(QuoteRejectReason, False)
        self.register_field(QuoteResponseLevel, False)
        self.register_field(QuoteType, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

        class NoQuoteSetsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(QuoteSetID, False)
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
                self.register_field(TotNoQuoteEntries, False)
                self.register_field(LastFragment, False)

                class NoQuoteEntriesGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(QuoteEntryID, False)
                        self.register_field(Symbol, False)
                        self.register_field(SymbolSfx, False)
                        self.register_field(SecurityID, False)
                        self.register_field(SecurityIDSource, False)

                        class NoSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(SecurityAltID, False)
                                self.register_field(SecurityAltIDSource, False)

                        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                        self.register_field(Product, False)
                        self.register_field(CFICode, False)
                        self.register_field(SecurityType, False)
                        self.register_field(SecuritySubType, False)
                        self.register_field(MaturityMonthYear, False)
                        self.register_field(MaturityDate, False)
                        self.register_field(PutOrCall, False)
                        self.register_field(CouponPaymentDate, False)
                        self.register_field(IssueDate, False)
                        self.register_field(RepoCollateralSecurityType, False)
                        self.register_field(RepurchaseTerm, False)
                        self.register_field(RepurchaseRate, False)
                        self.register_field(Factor, False)
                        self.register_field(CreditRating, False)
                        self.register_field(InstrRegistry, False)
                        self.register_field(CountryOfIssue, False)
                        self.register_field(StateOrProvinceOfIssue, False)
                        self.register_field(LocaleOfIssue, False)
                        self.register_field(RedemptionDate, False)
                        self.register_field(StrikePrice, False)
                        self.register_field(StrikeCurrency, False)
                        self.register_field(OptAttribute, False)
                        self.register_field(ContractMultiplier, False)
                        self.register_field(CouponRate, False)
                        self.register_field(SecurityExchange, False)
                        self.register_field(Issuer, False)
                        self.register_field(EncodedIssuerLen, False)
                        self.register_field(EncodedIssuer, False)
                        self.register_field(SecurityDesc, False)
                        self.register_field(EncodedSecurityDescLen, False)
                        self.register_field(EncodedSecurityDesc, False)
                        self.register_field(Pool, False)
                        self.register_field(ContractSettlMonth, False)
                        self.register_field(CPProgram, False)
                        self.register_field(CPRegType, False)

                        class NoEventsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(EventType, False)
                                self.register_field(EventDate, False)
                                self.register_field(EventPx, False)
                                self.register_field(EventText, False)

                        self.register_group(NoEvents, NoEventsGroup, False)
                        self.register_field(DatedDate, False)
                        self.register_field(InterestAccrualDate, False)

                        class NoLegsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegSymbol, False)
                                self.register_field(LegSymbolSfx, False)
                                self.register_field(LegSecurityID, False)
                                self.register_field(LegSecurityIDSource, False)

                                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(LegSecurityAltID, False)
                                        self.register_field(LegSecurityAltIDSource, False)

                                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                                self.register_field(LegProduct, False)
                                self.register_field(LegCFICode, False)
                                self.register_field(LegSecurityType, False)
                                self.register_field(LegSecuritySubType, False)
                                self.register_field(LegMaturityMonthYear, False)
                                self.register_field(LegMaturityDate, False)
                                self.register_field(LegCouponPaymentDate, False)
                                self.register_field(LegIssueDate, False)
                                self.register_field(LegRepoCollateralSecurityType, False)
                                self.register_field(LegRepurchaseTerm, False)
                                self.register_field(LegRepurchaseRate, False)
                                self.register_field(LegFactor, False)
                                self.register_field(LegCreditRating, False)
                                self.register_field(LegInstrRegistry, False)
                                self.register_field(LegCountryOfIssue, False)
                                self.register_field(LegStateOrProvinceOfIssue, False)
                                self.register_field(LegLocaleOfIssue, False)
                                self.register_field(LegRedemptionDate, False)
                                self.register_field(LegStrikePrice, False)
                                self.register_field(LegStrikeCurrency, False)
                                self.register_field(LegOptAttribute, False)
                                self.register_field(LegContractMultiplier, False)
                                self.register_field(LegCouponRate, False)
                                self.register_field(LegSecurityExchange, False)
                                self.register_field(LegIssuer, False)
                                self.register_field(EncodedLegIssuerLen, False)
                                self.register_field(EncodedLegIssuer, False)
                                self.register_field(LegSecurityDesc, False)
                                self.register_field(EncodedLegSecurityDescLen, False)
                                self.register_field(EncodedLegSecurityDesc, False)
                                self.register_field(LegRatioQty, False)
                                self.register_field(LegSide, False)
                                self.register_field(LegCurrency, False)
                                self.register_field(LegPool, False)
                                self.register_field(LegDatedDate, False)
                                self.register_field(LegContractSettlMonth, False)
                                self.register_field(LegInterestAccrualDate, False)

                        self.register_group(NoLegs, NoLegsGroup, False)
                        self.register_field(BidPx, False)
                        self.register_field(OfferPx, False)
                        self.register_field(BidSize, False)
                        self.register_field(OfferSize, False)
                        self.register_field(ValidUntilTime, False)
                        self.register_field(BidSpotRate, False)
                        self.register_field(OfferSpotRate, False)
                        self.register_field(BidForwardPoints, False)
                        self.register_field(OfferForwardPoints, False)
                        self.register_field(MidPx, False)
                        self.register_field(BidYield, False)
                        self.register_field(MidYield, False)
                        self.register_field(OfferYield, False)
                        self.register_field(TransactTime, False)
                        self.register_field(TradingSessionID, False)
                        self.register_field(TradingSessionSubID, False)
                        self.register_field(SettlDate, False)
                        self.register_field(OrdType, False)
                        self.register_field(SettlDate2, False)
                        self.register_field(OrderQty2, False)
                        self.register_field(BidForwardPoints2, False)
                        self.register_field(OfferForwardPoints2, False)
                        self.register_field(Currency, False)
                        self.register_field(QuoteEntryRejectReason, False)

                self.register_group(NoQuoteEntries, NoQuoteEntriesGroup, False)

        self.register_group(NoQuoteSets, NoQuoteSetsGroup, False)

MESSAGE_TYPES['b'] = MassQuoteAcknowledgement

class SecurityDefinitionRequest(fix_message.MessageBase):
    _msgtype = 'c'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SecurityReqID, True)
        self.register_field(SecurityRequestType, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(DeliveryForm, False)
        self.register_field(PctAtRisk, False)

        class NoInstrAttribGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(InstrAttribType, False)
                self.register_field(InstrAttribValue, False)

        self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(Currency, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(ExpirationCycle, False)
        self.register_field(SubscriptionRequestType, False)

MESSAGE_TYPES['c'] = SecurityDefinitionRequest

class SecurityDefinition(fix_message.MessageBase):
    _msgtype = 'd'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SecurityReqID, True)
        self.register_field(SecurityResponseID, True)
        self.register_field(SecurityResponseType, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(DeliveryForm, False)
        self.register_field(PctAtRisk, False)

        class NoInstrAttribGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(InstrAttribType, False)
                self.register_field(InstrAttribValue, False)

        self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(Currency, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(ExpirationCycle, False)
        self.register_field(RoundLot, False)
        self.register_field(MinTradeVol, False)

MESSAGE_TYPES['d'] = SecurityDefinition

class SecurityStatusRequest(fix_message.MessageBase):
    _msgtype = 'e'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SecurityStatusReqID, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(DeliveryForm, False)
        self.register_field(PctAtRisk, False)

        class NoInstrAttribGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(InstrAttribType, False)
                self.register_field(InstrAttribValue, False)

        self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(Currency, False)
        self.register_field(SubscriptionRequestType, True)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)

MESSAGE_TYPES['e'] = SecurityStatusRequest

class SecurityStatus(fix_message.MessageBase):
    _msgtype = 'f'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SecurityStatusReqID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(DeliveryForm, False)
        self.register_field(PctAtRisk, False)

        class NoInstrAttribGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(InstrAttribType, False)
                self.register_field(InstrAttribValue, False)

        self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(Currency, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(UnsolicitedIndicator, False)
        self.register_field(SecurityTradingStatus, False)
        self.register_field(FinancialStatus, False)
        self.register_field(CorporateAction, False)
        self.register_field(HaltReasonChar, False)
        self.register_field(InViewOfCommon, False)
        self.register_field(DueToRelated, False)
        self.register_field(BuyVolume, False)
        self.register_field(SellVolume, False)
        self.register_field(HighPx, False)
        self.register_field(LowPx, False)
        self.register_field(LastPx, False)
        self.register_field(TransactTime, False)
        self.register_field(Adjustment, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['f'] = SecurityStatus

class TradingSessionStatusRequest(fix_message.MessageBase):
    _msgtype = 'g'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(TradSesReqID, True)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(TradSesMethod, False)
        self.register_field(TradSesMode, False)
        self.register_field(SubscriptionRequestType, True)

MESSAGE_TYPES['g'] = TradingSessionStatusRequest

class TradingSessionStatus(fix_message.MessageBase):
    _msgtype = 'h'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(TradSesReqID, False)
        self.register_field(TradingSessionID, True)
        self.register_field(TradingSessionSubID, False)
        self.register_field(TradSesMethod, False)
        self.register_field(TradSesMode, False)
        self.register_field(UnsolicitedIndicator, False)
        self.register_field(TradSesStatus, True)
        self.register_field(TradSesStatusRejReason, False)
        self.register_field(TradSesStartTime, False)
        self.register_field(TradSesOpenTime, False)
        self.register_field(TradSesPreCloseTime, False)
        self.register_field(TradSesCloseTime, False)
        self.register_field(TradSesEndTime, False)
        self.register_field(TotalVolumeTraded, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['h'] = TradingSessionStatus

class MassQuote(fix_message.MessageBase):
    _msgtype = 'i'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(QuoteReqID, False)
        self.register_field(QuoteID, True)
        self.register_field(QuoteType, False)
        self.register_field(QuoteResponseLevel, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(DefBidSize, False)
        self.register_field(DefOfferSize, False)

        class NoQuoteSetsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(QuoteSetID, True)
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
                self.register_field(QuoteSetValidUntilTime, False)
                self.register_field(TotNoQuoteEntries, True)
                self.register_field(LastFragment, False)

                class NoQuoteEntriesGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(QuoteEntryID, True)
                        self.register_field(Symbol, False)
                        self.register_field(SymbolSfx, False)
                        self.register_field(SecurityID, False)
                        self.register_field(SecurityIDSource, False)

                        class NoSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(SecurityAltID, False)
                                self.register_field(SecurityAltIDSource, False)

                        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                        self.register_field(Product, False)
                        self.register_field(CFICode, False)
                        self.register_field(SecurityType, False)
                        self.register_field(SecuritySubType, False)
                        self.register_field(MaturityMonthYear, False)
                        self.register_field(MaturityDate, False)
                        self.register_field(PutOrCall, False)
                        self.register_field(CouponPaymentDate, False)
                        self.register_field(IssueDate, False)
                        self.register_field(RepoCollateralSecurityType, False)
                        self.register_field(RepurchaseTerm, False)
                        self.register_field(RepurchaseRate, False)
                        self.register_field(Factor, False)
                        self.register_field(CreditRating, False)
                        self.register_field(InstrRegistry, False)
                        self.register_field(CountryOfIssue, False)
                        self.register_field(StateOrProvinceOfIssue, False)
                        self.register_field(LocaleOfIssue, False)
                        self.register_field(RedemptionDate, False)
                        self.register_field(StrikePrice, False)
                        self.register_field(StrikeCurrency, False)
                        self.register_field(OptAttribute, False)
                        self.register_field(ContractMultiplier, False)
                        self.register_field(CouponRate, False)
                        self.register_field(SecurityExchange, False)
                        self.register_field(Issuer, False)
                        self.register_field(EncodedIssuerLen, False)
                        self.register_field(EncodedIssuer, False)
                        self.register_field(SecurityDesc, False)
                        self.register_field(EncodedSecurityDescLen, False)
                        self.register_field(EncodedSecurityDesc, False)
                        self.register_field(Pool, False)
                        self.register_field(ContractSettlMonth, False)
                        self.register_field(CPProgram, False)
                        self.register_field(CPRegType, False)

                        class NoEventsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(EventType, False)
                                self.register_field(EventDate, False)
                                self.register_field(EventPx, False)
                                self.register_field(EventText, False)

                        self.register_group(NoEvents, NoEventsGroup, False)
                        self.register_field(DatedDate, False)
                        self.register_field(InterestAccrualDate, False)

                        class NoLegsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegSymbol, False)
                                self.register_field(LegSymbolSfx, False)
                                self.register_field(LegSecurityID, False)
                                self.register_field(LegSecurityIDSource, False)

                                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(LegSecurityAltID, False)
                                        self.register_field(LegSecurityAltIDSource, False)

                                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                                self.register_field(LegProduct, False)
                                self.register_field(LegCFICode, False)
                                self.register_field(LegSecurityType, False)
                                self.register_field(LegSecuritySubType, False)
                                self.register_field(LegMaturityMonthYear, False)
                                self.register_field(LegMaturityDate, False)
                                self.register_field(LegCouponPaymentDate, False)
                                self.register_field(LegIssueDate, False)
                                self.register_field(LegRepoCollateralSecurityType, False)
                                self.register_field(LegRepurchaseTerm, False)
                                self.register_field(LegRepurchaseRate, False)
                                self.register_field(LegFactor, False)
                                self.register_field(LegCreditRating, False)
                                self.register_field(LegInstrRegistry, False)
                                self.register_field(LegCountryOfIssue, False)
                                self.register_field(LegStateOrProvinceOfIssue, False)
                                self.register_field(LegLocaleOfIssue, False)
                                self.register_field(LegRedemptionDate, False)
                                self.register_field(LegStrikePrice, False)
                                self.register_field(LegStrikeCurrency, False)
                                self.register_field(LegOptAttribute, False)
                                self.register_field(LegContractMultiplier, False)
                                self.register_field(LegCouponRate, False)
                                self.register_field(LegSecurityExchange, False)
                                self.register_field(LegIssuer, False)
                                self.register_field(EncodedLegIssuerLen, False)
                                self.register_field(EncodedLegIssuer, False)
                                self.register_field(LegSecurityDesc, False)
                                self.register_field(EncodedLegSecurityDescLen, False)
                                self.register_field(EncodedLegSecurityDesc, False)
                                self.register_field(LegRatioQty, False)
                                self.register_field(LegSide, False)
                                self.register_field(LegCurrency, False)
                                self.register_field(LegPool, False)
                                self.register_field(LegDatedDate, False)
                                self.register_field(LegContractSettlMonth, False)
                                self.register_field(LegInterestAccrualDate, False)

                        self.register_group(NoLegs, NoLegsGroup, False)
                        self.register_field(BidPx, False)
                        self.register_field(OfferPx, False)
                        self.register_field(BidSize, False)
                        self.register_field(OfferSize, False)
                        self.register_field(ValidUntilTime, False)
                        self.register_field(BidSpotRate, False)
                        self.register_field(OfferSpotRate, False)
                        self.register_field(BidForwardPoints, False)
                        self.register_field(OfferForwardPoints, False)
                        self.register_field(MidPx, False)
                        self.register_field(BidYield, False)
                        self.register_field(MidYield, False)
                        self.register_field(OfferYield, False)
                        self.register_field(TransactTime, False)
                        self.register_field(TradingSessionID, False)
                        self.register_field(TradingSessionSubID, False)
                        self.register_field(SettlDate, False)
                        self.register_field(OrdType, False)
                        self.register_field(SettlDate2, False)
                        self.register_field(OrderQty2, False)
                        self.register_field(BidForwardPoints2, False)
                        self.register_field(OfferForwardPoints2, False)
                        self.register_field(Currency, False)

                self.register_group(NoQuoteEntries, NoQuoteEntriesGroup, True)

        self.register_group(NoQuoteSets, NoQuoteSetsGroup, True)

MESSAGE_TYPES['i'] = MassQuote

class BusinessMessageReject(fix_message.MessageBase):
    _msgtype = 'j'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(RefSeqNum, False)
        self.register_field(RefMsgType, True)
        self.register_field(BusinessRejectRefID, False)
        self.register_field(BusinessRejectReason, True)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['j'] = BusinessMessageReject

class BidRequest(fix_message.MessageBase):
    _msgtype = 'k'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(BidID, False)
        self.register_field(ClientBidID, True)
        self.register_field(BidRequestTransType, True)
        self.register_field(ListName, False)
        self.register_field(TotNoRelatedSym, True)
        self.register_field(BidType, True)
        self.register_field(NumTickets, False)
        self.register_field(Currency, False)
        self.register_field(SideValue1, False)
        self.register_field(SideValue2, False)

        class NoBidDescriptorsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(BidDescriptorType, False)
                self.register_field(BidDescriptor, False)
                self.register_field(SideValueInd, False)
                self.register_field(LiquidityValue, False)
                self.register_field(LiquidityNumSecurities, False)
                self.register_field(LiquidityPctLow, False)
                self.register_field(LiquidityPctHigh, False)
                self.register_field(EFPTrackingError, False)
                self.register_field(FairValue, False)
                self.register_field(OutsideIndexPct, False)
                self.register_field(ValueOfFutures, False)

        self.register_group(NoBidDescriptors, NoBidDescriptorsGroup, False)

        class NoBidComponentsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ListID, False)
                self.register_field(Side, False)
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)
                self.register_field(NetGrossInd, False)
                self.register_field(SettlType, False)
                self.register_field(SettlDate, False)
                self.register_field(Account, False)
                self.register_field(AcctIDSource, False)

        self.register_group(NoBidComponents, NoBidComponentsGroup, False)
        self.register_field(LiquidityIndType, False)
        self.register_field(WtAverageLiquidity, False)
        self.register_field(ExchangeForPhysical, False)
        self.register_field(OutMainCntryUIndex, False)
        self.register_field(CrossPercent, False)
        self.register_field(ProgRptReqs, False)
        self.register_field(ProgPeriodInterval, False)
        self.register_field(IncTaxInd, False)
        self.register_field(ForexReq, False)
        self.register_field(NumBidders, False)
        self.register_field(TradeDate, False)
        self.register_field(BidTradeType, True)
        self.register_field(BasisPxType, True)
        self.register_field(StrikeTime, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['k'] = BidRequest

class BidResponse(fix_message.MessageBase):
    _msgtype = 'l'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(BidID, False)
        self.register_field(ClientBidID, False)

        class NoBidComponentsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Commission, False)
                self.register_field(CommType, False)
                self.register_field(CommCurrency, False)
                self.register_field(FundRenewWaiv, False)
                self.register_field(ListID, False)
                self.register_field(Country, False)
                self.register_field(Side, False)
                self.register_field(Price, False)
                self.register_field(PriceType, False)
                self.register_field(FairValue, False)
                self.register_field(NetGrossInd, False)
                self.register_field(SettlType, False)
                self.register_field(SettlDate, False)
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)

        self.register_group(NoBidComponents, NoBidComponentsGroup, True)

MESSAGE_TYPES['l'] = BidResponse

class ListStrikePrice(fix_message.MessageBase):
    _msgtype = 'm'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ListID, True)
        self.register_field(TotNoStrikes, True)
        self.register_field(LastFragment, False)

        class NoStrikesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)

        self.register_group(NoStrikes, NoStrikesGroup, True)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
                self.register_field(PrevClosePx, False)
                self.register_field(ClOrdID, False)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(Side, False)
                self.register_field(Price, True)
                self.register_field(Currency, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

MESSAGE_TYPES['m'] = ListStrikePrice

class XMLnonFIX(fix_message.MessageBase):
    _msgtype = 'n'
    _msgcat = 'admin'
    def __init__(self):
        super().__init__()

MESSAGE_TYPES['n'] = XMLnonFIX

class RegistrationInstructions(fix_message.MessageBase):
    _msgtype = 'o'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(RegistID, True)
        self.register_field(RegistTransType, True)
        self.register_field(RegistRefID, True)
        self.register_field(ClOrdID, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(RegistAcctType, False)
        self.register_field(TaxAdvantageType, False)
        self.register_field(OwnershipType, False)

        class NoRegistDtlsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(RegistDtls, False)
                self.register_field(RegistEmail, False)
                self.register_field(MailingDtls, False)
                self.register_field(MailingInst, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(OwnerType, False)
                self.register_field(DateOfBirth, False)
                self.register_field(InvestorCountryOfResidence, False)

        self.register_group(NoRegistDtls, NoRegistDtlsGroup, False)

        class NoDistribInstsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(DistribPaymentMethod, False)
                self.register_field(DistribPercentage, False)
                self.register_field(CashDistribCurr, False)
                self.register_field(CashDistribAgentName, False)
                self.register_field(CashDistribAgentCode, False)
                self.register_field(CashDistribAgentAcctNumber, False)
                self.register_field(CashDistribPayRef, False)
                self.register_field(CashDistribAgentAcctName, False)

        self.register_group(NoDistribInsts, NoDistribInstsGroup, False)

MESSAGE_TYPES['o'] = RegistrationInstructions

class RegistrationInstructionsResponse(fix_message.MessageBase):
    _msgtype = 'p'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(RegistID, True)
        self.register_field(RegistTransType, True)
        self.register_field(RegistRefID, True)
        self.register_field(ClOrdID, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(RegistStatus, True)
        self.register_field(RegistRejReasonCode, False)
        self.register_field(RegistRejReasonText, False)

MESSAGE_TYPES['p'] = RegistrationInstructionsResponse

class OrderMassCancelRequest(fix_message.MessageBase):
    _msgtype = 'q'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ClOrdID, True)
        self.register_field(SecondaryClOrdID, False)
        self.register_field(MassCancelRequestType, True)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(UnderlyingSymbol, False)
        self.register_field(UnderlyingSymbolSfx, False)
        self.register_field(UnderlyingSecurityID, False)
        self.register_field(UnderlyingSecurityIDSource, False)

        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSecurityAltID, False)
                self.register_field(UnderlyingSecurityAltIDSource, False)

        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
        self.register_field(UnderlyingProduct, False)
        self.register_field(UnderlyingCFICode, False)
        self.register_field(UnderlyingSecurityType, False)
        self.register_field(UnderlyingSecuritySubType, False)
        self.register_field(UnderlyingMaturityMonthYear, False)
        self.register_field(UnderlyingMaturityDate, False)
        self.register_field(UnderlyingPutOrCall, False)
        self.register_field(UnderlyingCouponPaymentDate, False)
        self.register_field(UnderlyingIssueDate, False)
        self.register_field(UnderlyingRepoCollateralSecurityType, False)
        self.register_field(UnderlyingRepurchaseTerm, False)
        self.register_field(UnderlyingRepurchaseRate, False)
        self.register_field(UnderlyingFactor, False)
        self.register_field(UnderlyingCreditRating, False)
        self.register_field(UnderlyingInstrRegistry, False)
        self.register_field(UnderlyingCountryOfIssue, False)
        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
        self.register_field(UnderlyingLocaleOfIssue, False)
        self.register_field(UnderlyingRedemptionDate, False)
        self.register_field(UnderlyingStrikePrice, False)
        self.register_field(UnderlyingStrikeCurrency, False)
        self.register_field(UnderlyingOptAttribute, False)
        self.register_field(UnderlyingContractMultiplier, False)
        self.register_field(UnderlyingCouponRate, False)
        self.register_field(UnderlyingSecurityExchange, False)
        self.register_field(UnderlyingIssuer, False)
        self.register_field(EncodedUnderlyingIssuerLen, False)
        self.register_field(EncodedUnderlyingIssuer, False)
        self.register_field(UnderlyingSecurityDesc, False)
        self.register_field(EncodedUnderlyingSecurityDescLen, False)
        self.register_field(EncodedUnderlyingSecurityDesc, False)
        self.register_field(UnderlyingCPProgram, False)
        self.register_field(UnderlyingCPRegType, False)
        self.register_field(UnderlyingCurrency, False)
        self.register_field(UnderlyingQty, False)
        self.register_field(UnderlyingPx, False)
        self.register_field(UnderlyingDirtyPrice, False)
        self.register_field(UnderlyingEndPrice, False)
        self.register_field(UnderlyingStartValue, False)
        self.register_field(UnderlyingCurrentValue, False)
        self.register_field(UnderlyingEndValue, False)

        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingStipType, False)
                self.register_field(UnderlyingStipValue, False)

        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
        self.register_field(Side, False)
        self.register_field(TransactTime, True)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['q'] = OrderMassCancelRequest

class OrderMassCancelReport(fix_message.MessageBase):
    _msgtype = 'r'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ClOrdID, False)
        self.register_field(SecondaryClOrdID, False)
        self.register_field(OrderID, True)
        self.register_field(SecondaryOrderID, False)
        self.register_field(MassCancelRequestType, True)
        self.register_field(MassCancelResponse, True)
        self.register_field(MassCancelRejectReason, False)
        self.register_field(TotalAffectedOrders, False)

        class NoAffectedOrdersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(OrigClOrdID, False)
                self.register_field(AffectedOrderID, False)
                self.register_field(AffectedSecondaryOrderID, False)

        self.register_group(NoAffectedOrders, NoAffectedOrdersGroup, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(UnderlyingSymbol, False)
        self.register_field(UnderlyingSymbolSfx, False)
        self.register_field(UnderlyingSecurityID, False)
        self.register_field(UnderlyingSecurityIDSource, False)

        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSecurityAltID, False)
                self.register_field(UnderlyingSecurityAltIDSource, False)

        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
        self.register_field(UnderlyingProduct, False)
        self.register_field(UnderlyingCFICode, False)
        self.register_field(UnderlyingSecurityType, False)
        self.register_field(UnderlyingSecuritySubType, False)
        self.register_field(UnderlyingMaturityMonthYear, False)
        self.register_field(UnderlyingMaturityDate, False)
        self.register_field(UnderlyingPutOrCall, False)
        self.register_field(UnderlyingCouponPaymentDate, False)
        self.register_field(UnderlyingIssueDate, False)
        self.register_field(UnderlyingRepoCollateralSecurityType, False)
        self.register_field(UnderlyingRepurchaseTerm, False)
        self.register_field(UnderlyingRepurchaseRate, False)
        self.register_field(UnderlyingFactor, False)
        self.register_field(UnderlyingCreditRating, False)
        self.register_field(UnderlyingInstrRegistry, False)
        self.register_field(UnderlyingCountryOfIssue, False)
        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
        self.register_field(UnderlyingLocaleOfIssue, False)
        self.register_field(UnderlyingRedemptionDate, False)
        self.register_field(UnderlyingStrikePrice, False)
        self.register_field(UnderlyingStrikeCurrency, False)
        self.register_field(UnderlyingOptAttribute, False)
        self.register_field(UnderlyingContractMultiplier, False)
        self.register_field(UnderlyingCouponRate, False)
        self.register_field(UnderlyingSecurityExchange, False)
        self.register_field(UnderlyingIssuer, False)
        self.register_field(EncodedUnderlyingIssuerLen, False)
        self.register_field(EncodedUnderlyingIssuer, False)
        self.register_field(UnderlyingSecurityDesc, False)
        self.register_field(EncodedUnderlyingSecurityDescLen, False)
        self.register_field(EncodedUnderlyingSecurityDesc, False)
        self.register_field(UnderlyingCPProgram, False)
        self.register_field(UnderlyingCPRegType, False)
        self.register_field(UnderlyingCurrency, False)
        self.register_field(UnderlyingQty, False)
        self.register_field(UnderlyingPx, False)
        self.register_field(UnderlyingDirtyPrice, False)
        self.register_field(UnderlyingEndPrice, False)
        self.register_field(UnderlyingStartValue, False)
        self.register_field(UnderlyingCurrentValue, False)
        self.register_field(UnderlyingEndValue, False)

        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingStipType, False)
                self.register_field(UnderlyingStipValue, False)

        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
        self.register_field(Side, False)
        self.register_field(TransactTime, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['r'] = OrderMassCancelReport

class NewOrderCross(fix_message.MessageBase):
    _msgtype = 's'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(CrossID, True)
        self.register_field(CrossType, True)
        self.register_field(CrossPrioritization, True)

        class NoSidesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Side, True)
                self.register_field(ClOrdID, True)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(ClOrdLinkID, False)

                class NoPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartyID, False)
                        self.register_field(PartyIDSource, False)
                        self.register_field(PartyRole, False)

                        class NoPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(PartySubID, False)
                                self.register_field(PartySubIDType, False)

                        self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

                self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
                self.register_field(TradeOriginationDate, False)
                self.register_field(TradeDate, False)
                self.register_field(Account, False)
                self.register_field(AcctIDSource, False)
                self.register_field(AccountType, False)
                self.register_field(DayBookingInst, False)
                self.register_field(BookingUnit, False)
                self.register_field(PreallocMethod, False)
                self.register_field(AllocID, False)

                class NoAllocsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(AllocAccount, False)
                        self.register_field(AllocAcctIDSource, False)
                        self.register_field(AllocSettlCurrency, False)
                        self.register_field(IndividualAllocID, False)

                        class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartyID, False)
                                self.register_field(NestedPartyIDSource, False)
                                self.register_field(NestedPartyRole, False)

                                class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(NestedPartySubID, False)
                                        self.register_field(NestedPartySubIDType, False)

                                self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                        self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                        self.register_field(AllocQty, False)

                self.register_group(NoAllocs, NoAllocsGroup, False)
                self.register_field(QtyType, False)
                self.register_field(OrderQty, False)
                self.register_field(CashOrderQty, False)
                self.register_field(OrderPercent, False)
                self.register_field(RoundingDirection, False)
                self.register_field(RoundingModulus, False)
                self.register_field(Commission, False)
                self.register_field(CommType, False)
                self.register_field(CommCurrency, False)
                self.register_field(FundRenewWaiv, False)
                self.register_field(OrderCapacity, False)
                self.register_field(OrderRestrictions, False)
                self.register_field(CustOrderCapacity, False)
                self.register_field(ForexReq, False)
                self.register_field(SettlCurrency, False)
                self.register_field(BookingType, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)
                self.register_field(PositionEffect, False)
                self.register_field(CoveredOrUncovered, False)
                self.register_field(CashMargin, False)
                self.register_field(ClearingFeeIndicator, False)
                self.register_field(SolicitedFlag, False)
                self.register_field(SideComplianceID, False)

        self.register_group(NoSides, NoSidesGroup, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(HandlInst, False)
        self.register_field(ExecInst, False)
        self.register_field(MinQty, False)
        self.register_field(MaxFloor, False)
        self.register_field(ExDestination, False)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(ProcessCode, False)
        self.register_field(PrevClosePx, False)
        self.register_field(LocateReqd, False)
        self.register_field(TransactTime, True)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(OrdType, True)
        self.register_field(PriceType, False)
        self.register_field(Price, False)
        self.register_field(StopPx, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)
        self.register_field(Currency, False)
        self.register_field(ComplianceID, False)
        self.register_field(IOIID, False)
        self.register_field(QuoteID, False)
        self.register_field(TimeInForce, False)
        self.register_field(EffectiveTime, False)
        self.register_field(ExpireDate, False)
        self.register_field(ExpireTime, False)
        self.register_field(GTBookingInst, False)
        self.register_field(MaxShow, False)
        self.register_field(PegOffsetValue, False)
        self.register_field(PegMoveType, False)
        self.register_field(PegOffsetType, False)
        self.register_field(PegLimitType, False)
        self.register_field(PegRoundDirection, False)
        self.register_field(PegScope, False)
        self.register_field(DiscretionInst, False)
        self.register_field(DiscretionOffsetValue, False)
        self.register_field(DiscretionMoveType, False)
        self.register_field(DiscretionOffsetType, False)
        self.register_field(DiscretionLimitType, False)
        self.register_field(DiscretionRoundDirection, False)
        self.register_field(DiscretionScope, False)
        self.register_field(TargetStrategy, False)
        self.register_field(TargetStrategyParameters, False)
        self.register_field(ParticipationRate, False)
        self.register_field(CancellationRights, False)
        self.register_field(MoneyLaunderingStatus, False)
        self.register_field(RegistID, False)
        self.register_field(Designation, False)

MESSAGE_TYPES['s'] = NewOrderCross

class CrossOrderCancelReplaceRequest(fix_message.MessageBase):
    _msgtype = 't'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(OrderID, False)
        self.register_field(CrossID, True)
        self.register_field(OrigCrossID, True)
        self.register_field(CrossType, True)
        self.register_field(CrossPrioritization, True)

        class NoSidesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Side, True)
                self.register_field(ClOrdID, True)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(ClOrdLinkID, False)

                class NoPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartyID, False)
                        self.register_field(PartyIDSource, False)
                        self.register_field(PartyRole, False)

                        class NoPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(PartySubID, False)
                                self.register_field(PartySubIDType, False)

                        self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

                self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
                self.register_field(TradeOriginationDate, False)
                self.register_field(TradeDate, False)
                self.register_field(Account, False)
                self.register_field(AcctIDSource, False)
                self.register_field(AccountType, False)
                self.register_field(DayBookingInst, False)
                self.register_field(BookingUnit, False)
                self.register_field(PreallocMethod, False)
                self.register_field(AllocID, False)

                class NoAllocsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(AllocAccount, False)
                        self.register_field(AllocAcctIDSource, False)
                        self.register_field(AllocSettlCurrency, False)
                        self.register_field(IndividualAllocID, False)

                        class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartyID, False)
                                self.register_field(NestedPartyIDSource, False)
                                self.register_field(NestedPartyRole, False)

                                class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(NestedPartySubID, False)
                                        self.register_field(NestedPartySubIDType, False)

                                self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                        self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                        self.register_field(AllocQty, False)

                self.register_group(NoAllocs, NoAllocsGroup, False)
                self.register_field(QtyType, False)
                self.register_field(OrderQty, False)
                self.register_field(CashOrderQty, False)
                self.register_field(OrderPercent, False)
                self.register_field(RoundingDirection, False)
                self.register_field(RoundingModulus, False)
                self.register_field(Commission, False)
                self.register_field(CommType, False)
                self.register_field(CommCurrency, False)
                self.register_field(FundRenewWaiv, False)
                self.register_field(OrderCapacity, False)
                self.register_field(OrderRestrictions, False)
                self.register_field(CustOrderCapacity, False)
                self.register_field(ForexReq, False)
                self.register_field(SettlCurrency, False)
                self.register_field(BookingType, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)
                self.register_field(PositionEffect, False)
                self.register_field(CoveredOrUncovered, False)
                self.register_field(CashMargin, False)
                self.register_field(ClearingFeeIndicator, False)
                self.register_field(SolicitedFlag, False)
                self.register_field(SideComplianceID, False)

        self.register_group(NoSides, NoSidesGroup, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(HandlInst, False)
        self.register_field(ExecInst, False)
        self.register_field(MinQty, False)
        self.register_field(MaxFloor, False)
        self.register_field(ExDestination, False)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(ProcessCode, False)
        self.register_field(PrevClosePx, False)
        self.register_field(LocateReqd, False)
        self.register_field(TransactTime, True)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(OrdType, True)
        self.register_field(PriceType, False)
        self.register_field(Price, False)
        self.register_field(StopPx, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)
        self.register_field(Currency, False)
        self.register_field(ComplianceID, False)
        self.register_field(IOIID, False)
        self.register_field(QuoteID, False)
        self.register_field(TimeInForce, False)
        self.register_field(EffectiveTime, False)
        self.register_field(ExpireDate, False)
        self.register_field(ExpireTime, False)
        self.register_field(GTBookingInst, False)
        self.register_field(MaxShow, False)
        self.register_field(PegOffsetValue, False)
        self.register_field(PegMoveType, False)
        self.register_field(PegOffsetType, False)
        self.register_field(PegLimitType, False)
        self.register_field(PegRoundDirection, False)
        self.register_field(PegScope, False)
        self.register_field(DiscretionInst, False)
        self.register_field(DiscretionOffsetValue, False)
        self.register_field(DiscretionMoveType, False)
        self.register_field(DiscretionOffsetType, False)
        self.register_field(DiscretionLimitType, False)
        self.register_field(DiscretionRoundDirection, False)
        self.register_field(DiscretionScope, False)
        self.register_field(TargetStrategy, False)
        self.register_field(TargetStrategyParameters, False)
        self.register_field(ParticipationRate, False)
        self.register_field(CancellationRights, False)
        self.register_field(MoneyLaunderingStatus, False)
        self.register_field(RegistID, False)
        self.register_field(Designation, False)

MESSAGE_TYPES['t'] = CrossOrderCancelReplaceRequest

class CrossOrderCancelRequest(fix_message.MessageBase):
    _msgtype = 'u'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(OrderID, False)
        self.register_field(CrossID, True)
        self.register_field(OrigCrossID, True)
        self.register_field(CrossType, True)
        self.register_field(CrossPrioritization, True)

        class NoSidesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Side, True)
                self.register_field(OrigClOrdID, True)
                self.register_field(ClOrdID, True)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(ClOrdLinkID, False)
                self.register_field(OrigOrdModTime, False)

                class NoPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartyID, False)
                        self.register_field(PartyIDSource, False)
                        self.register_field(PartyRole, False)

                        class NoPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(PartySubID, False)
                                self.register_field(PartySubIDType, False)

                        self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

                self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
                self.register_field(TradeOriginationDate, False)
                self.register_field(TradeDate, False)
                self.register_field(OrderQty, False)
                self.register_field(CashOrderQty, False)
                self.register_field(OrderPercent, False)
                self.register_field(RoundingDirection, False)
                self.register_field(RoundingModulus, False)
                self.register_field(ComplianceID, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)

        self.register_group(NoSides, NoSidesGroup, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(TransactTime, True)

MESSAGE_TYPES['u'] = CrossOrderCancelRequest

class SecurityTypeRequest(fix_message.MessageBase):
    _msgtype = 'v'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SecurityReqID, True)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(Product, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)

MESSAGE_TYPES['v'] = SecurityTypeRequest

class SecurityTypes(fix_message.MessageBase):
    _msgtype = 'w'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SecurityReqID, True)
        self.register_field(SecurityResponseID, True)
        self.register_field(SecurityResponseType, True)
        self.register_field(TotNoSecurityTypes, False)
        self.register_field(LastFragment, False)

        class NoSecurityTypesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)

        self.register_group(NoSecurityTypes, NoSecurityTypesGroup, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(SubscriptionRequestType, False)

MESSAGE_TYPES['w'] = SecurityTypes

class SecurityListRequest(fix_message.MessageBase):
    _msgtype = 'x'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SecurityReqID, True)
        self.register_field(SecurityListRequestType, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(DeliveryForm, False)
        self.register_field(PctAtRisk, False)

        class NoInstrAttribGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(InstrAttribType, False)
                self.register_field(InstrAttribValue, False)

        self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(Currency, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(SubscriptionRequestType, False)

MESSAGE_TYPES['x'] = SecurityListRequest

class SecurityList(fix_message.MessageBase):
    _msgtype = 'y'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SecurityReqID, True)
        self.register_field(SecurityResponseID, True)
        self.register_field(SecurityRequestResult, True)
        self.register_field(TotNoRelatedSym, False)
        self.register_field(LastFragment, False)

        class NoRelatedSymGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)
                self.register_field(DeliveryForm, False)
                self.register_field(PctAtRisk, False)

                class NoInstrAttribGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(InstrAttribType, False)
                        self.register_field(InstrAttribValue, False)

                self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)
                self.register_field(AgreementDesc, False)
                self.register_field(AgreementID, False)
                self.register_field(AgreementDate, False)
                self.register_field(AgreementCurrency, False)
                self.register_field(TerminationType, False)
                self.register_field(StartDate, False)
                self.register_field(EndDate, False)
                self.register_field(DeliveryType, False)
                self.register_field(MarginRatio, False)

                class NoUnderlyingsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSymbol, False)
                        self.register_field(UnderlyingSymbolSfx, False)
                        self.register_field(UnderlyingSecurityID, False)
                        self.register_field(UnderlyingSecurityIDSource, False)

                        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingSecurityAltID, False)
                                self.register_field(UnderlyingSecurityAltIDSource, False)

                        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                        self.register_field(UnderlyingProduct, False)
                        self.register_field(UnderlyingCFICode, False)
                        self.register_field(UnderlyingSecurityType, False)
                        self.register_field(UnderlyingSecuritySubType, False)
                        self.register_field(UnderlyingMaturityMonthYear, False)
                        self.register_field(UnderlyingMaturityDate, False)
                        self.register_field(UnderlyingPutOrCall, False)
                        self.register_field(UnderlyingCouponPaymentDate, False)
                        self.register_field(UnderlyingIssueDate, False)
                        self.register_field(UnderlyingRepoCollateralSecurityType, False)
                        self.register_field(UnderlyingRepurchaseTerm, False)
                        self.register_field(UnderlyingRepurchaseRate, False)
                        self.register_field(UnderlyingFactor, False)
                        self.register_field(UnderlyingCreditRating, False)
                        self.register_field(UnderlyingInstrRegistry, False)
                        self.register_field(UnderlyingCountryOfIssue, False)
                        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                        self.register_field(UnderlyingLocaleOfIssue, False)
                        self.register_field(UnderlyingRedemptionDate, False)
                        self.register_field(UnderlyingStrikePrice, False)
                        self.register_field(UnderlyingStrikeCurrency, False)
                        self.register_field(UnderlyingOptAttribute, False)
                        self.register_field(UnderlyingContractMultiplier, False)
                        self.register_field(UnderlyingCouponRate, False)
                        self.register_field(UnderlyingSecurityExchange, False)
                        self.register_field(UnderlyingIssuer, False)
                        self.register_field(EncodedUnderlyingIssuerLen, False)
                        self.register_field(EncodedUnderlyingIssuer, False)
                        self.register_field(UnderlyingSecurityDesc, False)
                        self.register_field(EncodedUnderlyingSecurityDescLen, False)
                        self.register_field(EncodedUnderlyingSecurityDesc, False)
                        self.register_field(UnderlyingCPProgram, False)
                        self.register_field(UnderlyingCPRegType, False)
                        self.register_field(UnderlyingCurrency, False)
                        self.register_field(UnderlyingQty, False)
                        self.register_field(UnderlyingPx, False)
                        self.register_field(UnderlyingDirtyPrice, False)
                        self.register_field(UnderlyingEndPrice, False)
                        self.register_field(UnderlyingStartValue, False)
                        self.register_field(UnderlyingCurrentValue, False)
                        self.register_field(UnderlyingEndValue, False)

                        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingStipType, False)
                                self.register_field(UnderlyingStipValue, False)

                        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

                self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
                self.register_field(Currency, False)

                class NoStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(StipulationType, False)
                        self.register_field(StipulationValue, False)

                self.register_group(NoStipulations, NoStipulationsGroup, False)

                class NoLegsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSymbol, False)
                        self.register_field(LegSymbolSfx, False)
                        self.register_field(LegSecurityID, False)
                        self.register_field(LegSecurityIDSource, False)

                        class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegSecurityAltID, False)
                                self.register_field(LegSecurityAltIDSource, False)

                        self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                        self.register_field(LegProduct, False)
                        self.register_field(LegCFICode, False)
                        self.register_field(LegSecurityType, False)
                        self.register_field(LegSecuritySubType, False)
                        self.register_field(LegMaturityMonthYear, False)
                        self.register_field(LegMaturityDate, False)
                        self.register_field(LegCouponPaymentDate, False)
                        self.register_field(LegIssueDate, False)
                        self.register_field(LegRepoCollateralSecurityType, False)
                        self.register_field(LegRepurchaseTerm, False)
                        self.register_field(LegRepurchaseRate, False)
                        self.register_field(LegFactor, False)
                        self.register_field(LegCreditRating, False)
                        self.register_field(LegInstrRegistry, False)
                        self.register_field(LegCountryOfIssue, False)
                        self.register_field(LegStateOrProvinceOfIssue, False)
                        self.register_field(LegLocaleOfIssue, False)
                        self.register_field(LegRedemptionDate, False)
                        self.register_field(LegStrikePrice, False)
                        self.register_field(LegStrikeCurrency, False)
                        self.register_field(LegOptAttribute, False)
                        self.register_field(LegContractMultiplier, False)
                        self.register_field(LegCouponRate, False)
                        self.register_field(LegSecurityExchange, False)
                        self.register_field(LegIssuer, False)
                        self.register_field(EncodedLegIssuerLen, False)
                        self.register_field(EncodedLegIssuer, False)
                        self.register_field(LegSecurityDesc, False)
                        self.register_field(EncodedLegSecurityDescLen, False)
                        self.register_field(EncodedLegSecurityDesc, False)
                        self.register_field(LegRatioQty, False)
                        self.register_field(LegSide, False)
                        self.register_field(LegCurrency, False)
                        self.register_field(LegPool, False)
                        self.register_field(LegDatedDate, False)
                        self.register_field(LegContractSettlMonth, False)
                        self.register_field(LegInterestAccrualDate, False)
                        self.register_field(LegSwapType, False)
                        self.register_field(LegSettlType, False)

                        class NoLegStipulationsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegStipulationType, False)
                                self.register_field(LegStipulationValue, False)

                        self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)
                        self.register_field(LegBenchmarkCurveCurrency, False)
                        self.register_field(LegBenchmarkCurveName, False)
                        self.register_field(LegBenchmarkCurvePoint, False)
                        self.register_field(LegBenchmarkPrice, False)
                        self.register_field(LegBenchmarkPriceType, False)

                self.register_group(NoLegs, NoLegsGroup, False)
                self.register_field(Spread, False)
                self.register_field(BenchmarkCurveCurrency, False)
                self.register_field(BenchmarkCurveName, False)
                self.register_field(BenchmarkCurvePoint, False)
                self.register_field(BenchmarkPrice, False)
                self.register_field(BenchmarkPriceType, False)
                self.register_field(BenchmarkSecurityID, False)
                self.register_field(BenchmarkSecurityIDSource, False)
                self.register_field(YieldType, False)
                self.register_field(Yield, False)
                self.register_field(YieldCalcDate, False)
                self.register_field(YieldRedemptionDate, False)
                self.register_field(YieldRedemptionPrice, False)
                self.register_field(YieldRedemptionPriceType, False)
                self.register_field(RoundLot, False)
                self.register_field(MinTradeVol, False)
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)
                self.register_field(ExpirationCycle, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)

        self.register_group(NoRelatedSym, NoRelatedSymGroup, False)

MESSAGE_TYPES['y'] = SecurityList

class DerivativeSecurityListRequest(fix_message.MessageBase):
    _msgtype = 'z'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SecurityReqID, True)
        self.register_field(SecurityListRequestType, True)
        self.register_field(UnderlyingSymbol, False)
        self.register_field(UnderlyingSymbolSfx, False)
        self.register_field(UnderlyingSecurityID, False)
        self.register_field(UnderlyingSecurityIDSource, False)

        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSecurityAltID, False)
                self.register_field(UnderlyingSecurityAltIDSource, False)

        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
        self.register_field(UnderlyingProduct, False)
        self.register_field(UnderlyingCFICode, False)
        self.register_field(UnderlyingSecurityType, False)
        self.register_field(UnderlyingSecuritySubType, False)
        self.register_field(UnderlyingMaturityMonthYear, False)
        self.register_field(UnderlyingMaturityDate, False)
        self.register_field(UnderlyingPutOrCall, False)
        self.register_field(UnderlyingCouponPaymentDate, False)
        self.register_field(UnderlyingIssueDate, False)
        self.register_field(UnderlyingRepoCollateralSecurityType, False)
        self.register_field(UnderlyingRepurchaseTerm, False)
        self.register_field(UnderlyingRepurchaseRate, False)
        self.register_field(UnderlyingFactor, False)
        self.register_field(UnderlyingCreditRating, False)
        self.register_field(UnderlyingInstrRegistry, False)
        self.register_field(UnderlyingCountryOfIssue, False)
        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
        self.register_field(UnderlyingLocaleOfIssue, False)
        self.register_field(UnderlyingRedemptionDate, False)
        self.register_field(UnderlyingStrikePrice, False)
        self.register_field(UnderlyingStrikeCurrency, False)
        self.register_field(UnderlyingOptAttribute, False)
        self.register_field(UnderlyingContractMultiplier, False)
        self.register_field(UnderlyingCouponRate, False)
        self.register_field(UnderlyingSecurityExchange, False)
        self.register_field(UnderlyingIssuer, False)
        self.register_field(EncodedUnderlyingIssuerLen, False)
        self.register_field(EncodedUnderlyingIssuer, False)
        self.register_field(UnderlyingSecurityDesc, False)
        self.register_field(EncodedUnderlyingSecurityDescLen, False)
        self.register_field(EncodedUnderlyingSecurityDesc, False)
        self.register_field(UnderlyingCPProgram, False)
        self.register_field(UnderlyingCPRegType, False)
        self.register_field(UnderlyingCurrency, False)
        self.register_field(UnderlyingQty, False)
        self.register_field(UnderlyingPx, False)
        self.register_field(UnderlyingDirtyPrice, False)
        self.register_field(UnderlyingEndPrice, False)
        self.register_field(UnderlyingStartValue, False)
        self.register_field(UnderlyingCurrentValue, False)
        self.register_field(UnderlyingEndValue, False)

        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingStipType, False)
                self.register_field(UnderlyingStipValue, False)

        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
        self.register_field(SecuritySubType, False)
        self.register_field(Currency, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(SubscriptionRequestType, False)

MESSAGE_TYPES['z'] = DerivativeSecurityListRequest

class DerivativeSecurityList(fix_message.MessageBase):
    _msgtype = 'AA'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SecurityReqID, True)
        self.register_field(SecurityResponseID, True)
        self.register_field(SecurityRequestResult, True)
        self.register_field(UnderlyingSymbol, False)
        self.register_field(UnderlyingSymbolSfx, False)
        self.register_field(UnderlyingSecurityID, False)
        self.register_field(UnderlyingSecurityIDSource, False)

        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSecurityAltID, False)
                self.register_field(UnderlyingSecurityAltIDSource, False)

        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
        self.register_field(UnderlyingProduct, False)
        self.register_field(UnderlyingCFICode, False)
        self.register_field(UnderlyingSecurityType, False)
        self.register_field(UnderlyingSecuritySubType, False)
        self.register_field(UnderlyingMaturityMonthYear, False)
        self.register_field(UnderlyingMaturityDate, False)
        self.register_field(UnderlyingPutOrCall, False)
        self.register_field(UnderlyingCouponPaymentDate, False)
        self.register_field(UnderlyingIssueDate, False)
        self.register_field(UnderlyingRepoCollateralSecurityType, False)
        self.register_field(UnderlyingRepurchaseTerm, False)
        self.register_field(UnderlyingRepurchaseRate, False)
        self.register_field(UnderlyingFactor, False)
        self.register_field(UnderlyingCreditRating, False)
        self.register_field(UnderlyingInstrRegistry, False)
        self.register_field(UnderlyingCountryOfIssue, False)
        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
        self.register_field(UnderlyingLocaleOfIssue, False)
        self.register_field(UnderlyingRedemptionDate, False)
        self.register_field(UnderlyingStrikePrice, False)
        self.register_field(UnderlyingStrikeCurrency, False)
        self.register_field(UnderlyingOptAttribute, False)
        self.register_field(UnderlyingContractMultiplier, False)
        self.register_field(UnderlyingCouponRate, False)
        self.register_field(UnderlyingSecurityExchange, False)
        self.register_field(UnderlyingIssuer, False)
        self.register_field(EncodedUnderlyingIssuerLen, False)
        self.register_field(EncodedUnderlyingIssuer, False)
        self.register_field(UnderlyingSecurityDesc, False)
        self.register_field(EncodedUnderlyingSecurityDescLen, False)
        self.register_field(EncodedUnderlyingSecurityDesc, False)
        self.register_field(UnderlyingCPProgram, False)
        self.register_field(UnderlyingCPRegType, False)
        self.register_field(UnderlyingCurrency, False)
        self.register_field(UnderlyingQty, False)
        self.register_field(UnderlyingPx, False)
        self.register_field(UnderlyingDirtyPrice, False)
        self.register_field(UnderlyingEndPrice, False)
        self.register_field(UnderlyingStartValue, False)
        self.register_field(UnderlyingCurrentValue, False)
        self.register_field(UnderlyingEndValue, False)

        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingStipType, False)
                self.register_field(UnderlyingStipValue, False)

        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
        self.register_field(TotNoRelatedSym, False)
        self.register_field(LastFragment, False)

        class NoRelatedSymGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)
                self.register_field(Currency, False)
                self.register_field(ExpirationCycle, False)
                self.register_field(DeliveryForm, False)
                self.register_field(PctAtRisk, False)

                class NoInstrAttribGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(InstrAttribType, False)
                        self.register_field(InstrAttribValue, False)

                self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)

                class NoLegsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSymbol, False)
                        self.register_field(LegSymbolSfx, False)
                        self.register_field(LegSecurityID, False)
                        self.register_field(LegSecurityIDSource, False)

                        class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegSecurityAltID, False)
                                self.register_field(LegSecurityAltIDSource, False)

                        self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                        self.register_field(LegProduct, False)
                        self.register_field(LegCFICode, False)
                        self.register_field(LegSecurityType, False)
                        self.register_field(LegSecuritySubType, False)
                        self.register_field(LegMaturityMonthYear, False)
                        self.register_field(LegMaturityDate, False)
                        self.register_field(LegCouponPaymentDate, False)
                        self.register_field(LegIssueDate, False)
                        self.register_field(LegRepoCollateralSecurityType, False)
                        self.register_field(LegRepurchaseTerm, False)
                        self.register_field(LegRepurchaseRate, False)
                        self.register_field(LegFactor, False)
                        self.register_field(LegCreditRating, False)
                        self.register_field(LegInstrRegistry, False)
                        self.register_field(LegCountryOfIssue, False)
                        self.register_field(LegStateOrProvinceOfIssue, False)
                        self.register_field(LegLocaleOfIssue, False)
                        self.register_field(LegRedemptionDate, False)
                        self.register_field(LegStrikePrice, False)
                        self.register_field(LegStrikeCurrency, False)
                        self.register_field(LegOptAttribute, False)
                        self.register_field(LegContractMultiplier, False)
                        self.register_field(LegCouponRate, False)
                        self.register_field(LegSecurityExchange, False)
                        self.register_field(LegIssuer, False)
                        self.register_field(EncodedLegIssuerLen, False)
                        self.register_field(EncodedLegIssuer, False)
                        self.register_field(LegSecurityDesc, False)
                        self.register_field(EncodedLegSecurityDescLen, False)
                        self.register_field(EncodedLegSecurityDesc, False)
                        self.register_field(LegRatioQty, False)
                        self.register_field(LegSide, False)
                        self.register_field(LegCurrency, False)
                        self.register_field(LegPool, False)
                        self.register_field(LegDatedDate, False)
                        self.register_field(LegContractSettlMonth, False)
                        self.register_field(LegInterestAccrualDate, False)

                self.register_group(NoLegs, NoLegsGroup, False)
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)

        self.register_group(NoRelatedSym, NoRelatedSymGroup, False)

MESSAGE_TYPES['AA'] = DerivativeSecurityList

class NewOrderMultileg(fix_message.MessageBase):
    _msgtype = 'AB'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ClOrdID, True)
        self.register_field(SecondaryClOrdID, False)
        self.register_field(ClOrdLinkID, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(TradeOriginationDate, False)
        self.register_field(TradeDate, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(DayBookingInst, False)
        self.register_field(BookingUnit, False)
        self.register_field(PreallocMethod, False)
        self.register_field(AllocID, False)

        class NoAllocsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AllocAccount, False)
                self.register_field(AllocAcctIDSource, False)
                self.register_field(AllocSettlCurrency, False)
                self.register_field(IndividualAllocID, False)

                class NoNested3PartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(Nested3PartyID, False)
                        self.register_field(Nested3PartyIDSource, False)
                        self.register_field(Nested3PartyRole, False)

                        class NoNested3PartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(Nested3PartySubID, False)
                                self.register_field(Nested3PartySubIDType, False)

                        self.register_group(NoNested3PartySubIDs, NoNested3PartySubIDsGroup, False)

                self.register_group(NoNested3PartyIDs, NoNested3PartyIDsGroup, False)
                self.register_field(AllocQty, False)

        self.register_group(NoAllocs, NoAllocsGroup, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(CashMargin, False)
        self.register_field(ClearingFeeIndicator, False)
        self.register_field(HandlInst, False)
        self.register_field(ExecInst, False)
        self.register_field(MinQty, False)
        self.register_field(MaxFloor, False)
        self.register_field(ExDestination, False)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(ProcessCode, False)
        self.register_field(Side, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(PrevClosePx, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)
                self.register_field(LegQty, False)
                self.register_field(LegSwapType, False)

                class NoLegStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegStipulationType, False)
                        self.register_field(LegStipulationValue, False)

                self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)

                class NoLegAllocsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegAllocAccount, False)
                        self.register_field(LegIndividualAllocID, False)

                        class NoNested2PartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(Nested2PartyID, False)
                                self.register_field(Nested2PartyIDSource, False)
                                self.register_field(Nested2PartyRole, False)

                                class NoNested2PartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(Nested2PartySubID, False)
                                        self.register_field(Nested2PartySubIDType, False)

                                self.register_group(NoNested2PartySubIDs, NoNested2PartySubIDsGroup, False)

                        self.register_group(NoNested2PartyIDs, NoNested2PartyIDsGroup, False)
                        self.register_field(LegAllocQty, False)
                        self.register_field(LegAllocAcctIDSource, False)
                        self.register_field(LegSettlCurrency, False)

                self.register_group(NoLegAllocs, NoLegAllocsGroup, False)
                self.register_field(LegPositionEffect, False)
                self.register_field(LegCoveredOrUncovered, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(LegRefID, False)
                self.register_field(LegPrice, False)
                self.register_field(LegSettlType, False)
                self.register_field(LegSettlDate, False)

        self.register_group(NoLegs, NoLegsGroup, True)
        self.register_field(LocateReqd, False)
        self.register_field(TransactTime, True)
        self.register_field(QtyType, False)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(OrdType, True)
        self.register_field(PriceType, False)
        self.register_field(Price, False)
        self.register_field(StopPx, False)
        self.register_field(Currency, False)
        self.register_field(ComplianceID, False)
        self.register_field(SolicitedFlag, False)
        self.register_field(IOIID, False)
        self.register_field(QuoteID, False)
        self.register_field(TimeInForce, False)
        self.register_field(EffectiveTime, False)
        self.register_field(ExpireDate, False)
        self.register_field(ExpireTime, False)
        self.register_field(GTBookingInst, False)
        self.register_field(Commission, False)
        self.register_field(CommType, False)
        self.register_field(CommCurrency, False)
        self.register_field(FundRenewWaiv, False)
        self.register_field(OrderCapacity, False)
        self.register_field(OrderRestrictions, False)
        self.register_field(CustOrderCapacity, False)
        self.register_field(ForexReq, False)
        self.register_field(SettlCurrency, False)
        self.register_field(BookingType, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(PositionEffect, False)
        self.register_field(CoveredOrUncovered, False)
        self.register_field(MaxShow, False)
        self.register_field(PegOffsetValue, False)
        self.register_field(PegMoveType, False)
        self.register_field(PegOffsetType, False)
        self.register_field(PegLimitType, False)
        self.register_field(PegRoundDirection, False)
        self.register_field(PegScope, False)
        self.register_field(DiscretionInst, False)
        self.register_field(DiscretionOffsetValue, False)
        self.register_field(DiscretionMoveType, False)
        self.register_field(DiscretionOffsetType, False)
        self.register_field(DiscretionLimitType, False)
        self.register_field(DiscretionRoundDirection, False)
        self.register_field(DiscretionScope, False)
        self.register_field(TargetStrategy, False)
        self.register_field(TargetStrategyParameters, False)
        self.register_field(ParticipationRate, False)
        self.register_field(CancellationRights, False)
        self.register_field(MoneyLaunderingStatus, False)
        self.register_field(RegistID, False)
        self.register_field(Designation, False)
        self.register_field(MultiLegRptTypeReq, False)

MESSAGE_TYPES['AB'] = NewOrderMultileg

class MultilegOrderCancelReplace(fix_message.MessageBase):
    _msgtype = 'AC'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(OrderID, False)
        self.register_field(OrigClOrdID, True)
        self.register_field(ClOrdID, True)
        self.register_field(SecondaryClOrdID, False)
        self.register_field(ClOrdLinkID, False)
        self.register_field(OrigOrdModTime, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(TradeOriginationDate, False)
        self.register_field(TradeDate, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(DayBookingInst, False)
        self.register_field(BookingUnit, False)
        self.register_field(PreallocMethod, False)
        self.register_field(AllocID, False)

        class NoAllocsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AllocAccount, False)
                self.register_field(AllocAcctIDSource, False)
                self.register_field(AllocSettlCurrency, False)
                self.register_field(IndividualAllocID, False)

                class NoNested3PartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(Nested3PartyID, False)
                        self.register_field(Nested3PartyIDSource, False)
                        self.register_field(Nested3PartyRole, False)

                        class NoNested3PartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(Nested3PartySubID, False)
                                self.register_field(Nested3PartySubIDType, False)

                        self.register_group(NoNested3PartySubIDs, NoNested3PartySubIDsGroup, False)

                self.register_group(NoNested3PartyIDs, NoNested3PartyIDsGroup, False)
                self.register_field(AllocQty, False)

        self.register_group(NoAllocs, NoAllocsGroup, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(CashMargin, False)
        self.register_field(ClearingFeeIndicator, False)
        self.register_field(HandlInst, False)
        self.register_field(ExecInst, False)
        self.register_field(MinQty, False)
        self.register_field(MaxFloor, False)
        self.register_field(ExDestination, False)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(ProcessCode, False)
        self.register_field(Side, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(PrevClosePx, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)
                self.register_field(LegQty, False)
                self.register_field(LegSwapType, False)

                class NoLegStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegStipulationType, False)
                        self.register_field(LegStipulationValue, False)

                self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)

                class NoLegAllocsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegAllocAccount, False)
                        self.register_field(LegIndividualAllocID, False)

                        class NoNested2PartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(Nested2PartyID, False)
                                self.register_field(Nested2PartyIDSource, False)
                                self.register_field(Nested2PartyRole, False)

                                class NoNested2PartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(Nested2PartySubID, False)
                                        self.register_field(Nested2PartySubIDType, False)

                                self.register_group(NoNested2PartySubIDs, NoNested2PartySubIDsGroup, False)

                        self.register_group(NoNested2PartyIDs, NoNested2PartyIDsGroup, False)
                        self.register_field(LegAllocQty, False)
                        self.register_field(LegAllocAcctIDSource, False)
                        self.register_field(LegSettlCurrency, False)

                self.register_group(NoLegAllocs, NoLegAllocsGroup, False)
                self.register_field(LegPositionEffect, False)
                self.register_field(LegCoveredOrUncovered, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(LegRefID, False)
                self.register_field(LegPrice, False)
                self.register_field(LegSettlType, False)
                self.register_field(LegSettlDate, False)

        self.register_group(NoLegs, NoLegsGroup, True)
        self.register_field(LocateReqd, False)
        self.register_field(TransactTime, True)
        self.register_field(QtyType, False)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(OrdType, True)
        self.register_field(PriceType, False)
        self.register_field(Price, False)
        self.register_field(StopPx, False)
        self.register_field(Currency, False)
        self.register_field(ComplianceID, False)
        self.register_field(SolicitedFlag, False)
        self.register_field(IOIID, False)
        self.register_field(QuoteID, False)
        self.register_field(TimeInForce, False)
        self.register_field(EffectiveTime, False)
        self.register_field(ExpireDate, False)
        self.register_field(ExpireTime, False)
        self.register_field(GTBookingInst, False)
        self.register_field(Commission, False)
        self.register_field(CommType, False)
        self.register_field(CommCurrency, False)
        self.register_field(FundRenewWaiv, False)
        self.register_field(OrderCapacity, False)
        self.register_field(OrderRestrictions, False)
        self.register_field(CustOrderCapacity, False)
        self.register_field(ForexReq, False)
        self.register_field(SettlCurrency, False)
        self.register_field(BookingType, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(PositionEffect, False)
        self.register_field(CoveredOrUncovered, False)
        self.register_field(MaxShow, False)
        self.register_field(PegOffsetValue, False)
        self.register_field(PegMoveType, False)
        self.register_field(PegOffsetType, False)
        self.register_field(PegLimitType, False)
        self.register_field(PegRoundDirection, False)
        self.register_field(PegScope, False)
        self.register_field(DiscretionInst, False)
        self.register_field(DiscretionOffsetValue, False)
        self.register_field(DiscretionMoveType, False)
        self.register_field(DiscretionOffsetType, False)
        self.register_field(DiscretionLimitType, False)
        self.register_field(DiscretionRoundDirection, False)
        self.register_field(DiscretionScope, False)
        self.register_field(TargetStrategy, False)
        self.register_field(TargetStrategyParameters, False)
        self.register_field(ParticipationRate, False)
        self.register_field(CancellationRights, False)
        self.register_field(MoneyLaunderingStatus, False)
        self.register_field(RegistID, False)
        self.register_field(Designation, False)
        self.register_field(MultiLegRptTypeReq, False)

MESSAGE_TYPES['AC'] = MultilegOrderCancelReplace

class TradeCaptureReportRequest(fix_message.MessageBase):
    _msgtype = 'AD'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(TradeRequestID, True)
        self.register_field(TradeRequestType, True)
        self.register_field(SubscriptionRequestType, False)
        self.register_field(TradeReportID, False)
        self.register_field(SecondaryTradeReportID, False)
        self.register_field(ExecID, False)
        self.register_field(ExecType, False)
        self.register_field(OrderID, False)
        self.register_field(ClOrdID, False)
        self.register_field(MatchStatus, False)
        self.register_field(TrdType, False)
        self.register_field(TrdSubType, False)
        self.register_field(TransferReason, False)
        self.register_field(SecondaryTrdType, False)
        self.register_field(TradeLinkID, False)
        self.register_field(TrdMatchID, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(DeliveryForm, False)
        self.register_field(PctAtRisk, False)

        class NoInstrAttribGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(InstrAttribType, False)
                self.register_field(InstrAttribValue, False)

        self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoDatesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradeDate, False)
                self.register_field(TransactTime, False)

        self.register_group(NoDates, NoDatesGroup, False)
        self.register_field(ClearingBusinessDate, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(TimeBracket, False)
        self.register_field(Side, False)
        self.register_field(MultiLegReportingType, False)
        self.register_field(TradeInputSource, False)
        self.register_field(TradeInputDevice, False)
        self.register_field(ResponseTransportType, False)
        self.register_field(ResponseDestination, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AD'] = TradeCaptureReportRequest

class TradeCaptureReport(fix_message.MessageBase):
    _msgtype = 'AE'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(TradeReportID, True)
        self.register_field(TradeReportTransType, False)
        self.register_field(TradeReportType, False)
        self.register_field(TradeRequestID, False)
        self.register_field(TrdType, False)
        self.register_field(TrdSubType, False)
        self.register_field(SecondaryTrdType, False)
        self.register_field(TransferReason, False)
        self.register_field(ExecType, False)
        self.register_field(TotNumTradeReports, False)
        self.register_field(LastRptRequested, False)
        self.register_field(UnsolicitedIndicator, False)
        self.register_field(SubscriptionRequestType, False)
        self.register_field(TradeReportRefID, False)
        self.register_field(SecondaryTradeReportRefID, False)
        self.register_field(SecondaryTradeReportID, False)
        self.register_field(TradeLinkID, False)
        self.register_field(TrdMatchID, False)
        self.register_field(ExecID, False)
        self.register_field(OrdStatus, False)
        self.register_field(SecondaryExecID, False)
        self.register_field(ExecRestatementReason, False)
        self.register_field(PreviouslyReported, True)
        self.register_field(PriceType, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(QtyType, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(UnderlyingTradingSessionID, False)
        self.register_field(UnderlyingTradingSessionSubID, False)
        self.register_field(LastQty, True)
        self.register_field(LastPx, True)
        self.register_field(LastParPx, False)
        self.register_field(LastSpotRate, False)
        self.register_field(LastForwardPoints, False)
        self.register_field(LastMkt, False)
        self.register_field(TradeDate, True)
        self.register_field(ClearingBusinessDate, False)
        self.register_field(AvgPx, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(AvgPxIndicator, False)

        class NoPosAmtGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PosAmtType, False)
                self.register_field(PosAmt, False)

        self.register_group(NoPosAmt, NoPosAmtGroup, False)
        self.register_field(MultiLegReportingType, False)
        self.register_field(TradeLegRefID, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)
                self.register_field(LegQty, False)
                self.register_field(LegSwapType, False)

                class NoLegStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegStipulationType, False)
                        self.register_field(LegStipulationValue, False)

                self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)
                self.register_field(LegPositionEffect, False)
                self.register_field(LegCoveredOrUncovered, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(LegRefID, False)
                self.register_field(LegPrice, False)
                self.register_field(LegSettlType, False)
                self.register_field(LegSettlDate, False)
                self.register_field(LegLastPx, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(TransactTime, True)

        class NoTrdRegTimestampsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TrdRegTimestamp, False)
                self.register_field(TrdRegTimestampType, False)
                self.register_field(TrdRegTimestampOrigin, False)

        self.register_group(NoTrdRegTimestamps, NoTrdRegTimestampsGroup, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(MatchStatus, False)
        self.register_field(MatchType, False)

        class NoSidesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Side, True)
                self.register_field(OrderID, True)
                self.register_field(SecondaryOrderID, False)
                self.register_field(ClOrdID, False)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(ListID, False)

                class NoPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartyID, False)
                        self.register_field(PartyIDSource, False)
                        self.register_field(PartyRole, False)

                        class NoPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(PartySubID, False)
                                self.register_field(PartySubIDType, False)

                        self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

                self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
                self.register_field(Account, False)
                self.register_field(AcctIDSource, False)
                self.register_field(AccountType, False)
                self.register_field(ProcessCode, False)
                self.register_field(OddLot, False)

                class NoClearingInstructionsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(ClearingInstruction, False)

                self.register_group(NoClearingInstructions, NoClearingInstructionsGroup, False)
                self.register_field(TradeInputSource, False)
                self.register_field(TradeInputDevice, False)
                self.register_field(OrderInputDevice, False)
                self.register_field(Currency, False)
                self.register_field(ComplianceID, False)
                self.register_field(SolicitedFlag, False)
                self.register_field(OrderCapacity, False)
                self.register_field(OrderRestrictions, False)
                self.register_field(CustOrderCapacity, False)
                self.register_field(OrdType, False)
                self.register_field(ExecInst, False)
                self.register_field(TransBkdTime, False)
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)
                self.register_field(TimeBracket, False)
                self.register_field(Commission, False)
                self.register_field(CommType, False)
                self.register_field(CommCurrency, False)
                self.register_field(FundRenewWaiv, False)
                self.register_field(GrossTradeAmt, False)
                self.register_field(NumDaysInterest, False)
                self.register_field(ExDate, False)
                self.register_field(AccruedInterestRate, False)
                self.register_field(AccruedInterestAmt, False)
                self.register_field(InterestAtMaturity, False)
                self.register_field(EndAccruedInterestAmt, False)
                self.register_field(StartCash, False)
                self.register_field(EndCash, False)
                self.register_field(Concession, False)
                self.register_field(TotalTakedown, False)
                self.register_field(NetMoney, False)
                self.register_field(SettlCurrAmt, False)
                self.register_field(SettlCurrency, False)
                self.register_field(SettlCurrFxRate, False)
                self.register_field(SettlCurrFxRateCalc, False)
                self.register_field(PositionEffect, False)
                self.register_field(Text, False)
                self.register_field(EncodedTextLen, False)
                self.register_field(EncodedText, False)
                self.register_field(SideMultiLegReportingType, False)

                class NoContAmtsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(ContAmtType, False)
                        self.register_field(ContAmtValue, False)
                        self.register_field(ContAmtCurr, False)

                self.register_group(NoContAmts, NoContAmtsGroup, False)

                class NoStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(StipulationType, False)
                        self.register_field(StipulationValue, False)

                self.register_group(NoStipulations, NoStipulationsGroup, False)

                class NoMiscFeesGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(MiscFeeAmt, False)
                        self.register_field(MiscFeeCurr, False)
                        self.register_field(MiscFeeType, False)
                        self.register_field(MiscFeeBasis, False)

                self.register_group(NoMiscFees, NoMiscFeesGroup, False)
                self.register_field(ExchangeRule, False)
                self.register_field(TradeAllocIndicator, False)
                self.register_field(PreallocMethod, False)
                self.register_field(AllocID, False)

                class NoAllocsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(AllocAccount, False)
                        self.register_field(AllocAcctIDSource, False)
                        self.register_field(AllocSettlCurrency, False)
                        self.register_field(IndividualAllocID, False)

                        class NoNested2PartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(Nested2PartyID, False)
                                self.register_field(Nested2PartyIDSource, False)
                                self.register_field(Nested2PartyRole, False)

                                class NoNested2PartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(Nested2PartySubID, False)
                                        self.register_field(Nested2PartySubIDType, False)

                                self.register_group(NoNested2PartySubIDs, NoNested2PartySubIDsGroup, False)

                        self.register_group(NoNested2PartyIDs, NoNested2PartyIDsGroup, False)
                        self.register_field(AllocQty, False)

                self.register_group(NoAllocs, NoAllocsGroup, False)

        self.register_group(NoSides, NoSidesGroup, True)
        self.register_field(CopyMsgIndicator, False)
        self.register_field(PublishTrdIndicator, False)
        self.register_field(ShortSaleReason, False)

MESSAGE_TYPES['AE'] = TradeCaptureReport

class OrderMassStatusRequest(fix_message.MessageBase):
    _msgtype = 'AF'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(MassStatusReqID, True)
        self.register_field(MassStatusReqType, True)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(UnderlyingSymbol, False)
        self.register_field(UnderlyingSymbolSfx, False)
        self.register_field(UnderlyingSecurityID, False)
        self.register_field(UnderlyingSecurityIDSource, False)

        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSecurityAltID, False)
                self.register_field(UnderlyingSecurityAltIDSource, False)

        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
        self.register_field(UnderlyingProduct, False)
        self.register_field(UnderlyingCFICode, False)
        self.register_field(UnderlyingSecurityType, False)
        self.register_field(UnderlyingSecuritySubType, False)
        self.register_field(UnderlyingMaturityMonthYear, False)
        self.register_field(UnderlyingMaturityDate, False)
        self.register_field(UnderlyingPutOrCall, False)
        self.register_field(UnderlyingCouponPaymentDate, False)
        self.register_field(UnderlyingIssueDate, False)
        self.register_field(UnderlyingRepoCollateralSecurityType, False)
        self.register_field(UnderlyingRepurchaseTerm, False)
        self.register_field(UnderlyingRepurchaseRate, False)
        self.register_field(UnderlyingFactor, False)
        self.register_field(UnderlyingCreditRating, False)
        self.register_field(UnderlyingInstrRegistry, False)
        self.register_field(UnderlyingCountryOfIssue, False)
        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
        self.register_field(UnderlyingLocaleOfIssue, False)
        self.register_field(UnderlyingRedemptionDate, False)
        self.register_field(UnderlyingStrikePrice, False)
        self.register_field(UnderlyingStrikeCurrency, False)
        self.register_field(UnderlyingOptAttribute, False)
        self.register_field(UnderlyingContractMultiplier, False)
        self.register_field(UnderlyingCouponRate, False)
        self.register_field(UnderlyingSecurityExchange, False)
        self.register_field(UnderlyingIssuer, False)
        self.register_field(EncodedUnderlyingIssuerLen, False)
        self.register_field(EncodedUnderlyingIssuer, False)
        self.register_field(UnderlyingSecurityDesc, False)
        self.register_field(EncodedUnderlyingSecurityDescLen, False)
        self.register_field(EncodedUnderlyingSecurityDesc, False)
        self.register_field(UnderlyingCPProgram, False)
        self.register_field(UnderlyingCPRegType, False)
        self.register_field(UnderlyingCurrency, False)
        self.register_field(UnderlyingQty, False)
        self.register_field(UnderlyingPx, False)
        self.register_field(UnderlyingDirtyPrice, False)
        self.register_field(UnderlyingEndPrice, False)
        self.register_field(UnderlyingStartValue, False)
        self.register_field(UnderlyingCurrentValue, False)
        self.register_field(UnderlyingEndValue, False)

        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingStipType, False)
                self.register_field(UnderlyingStipValue, False)

        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
        self.register_field(Side, False)

MESSAGE_TYPES['AF'] = OrderMassStatusRequest

class QuoteRequestReject(fix_message.MessageBase):
    _msgtype = 'AG'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(QuoteReqID, True)
        self.register_field(RFQReqID, False)
        self.register_field(QuoteRequestRejectReason, True)

        class NoRelatedSymGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)
                self.register_field(AgreementDesc, False)
                self.register_field(AgreementID, False)
                self.register_field(AgreementDate, False)
                self.register_field(AgreementCurrency, False)
                self.register_field(TerminationType, False)
                self.register_field(StartDate, False)
                self.register_field(EndDate, False)
                self.register_field(DeliveryType, False)
                self.register_field(MarginRatio, False)

                class NoUnderlyingsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSymbol, False)
                        self.register_field(UnderlyingSymbolSfx, False)
                        self.register_field(UnderlyingSecurityID, False)
                        self.register_field(UnderlyingSecurityIDSource, False)

                        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingSecurityAltID, False)
                                self.register_field(UnderlyingSecurityAltIDSource, False)

                        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                        self.register_field(UnderlyingProduct, False)
                        self.register_field(UnderlyingCFICode, False)
                        self.register_field(UnderlyingSecurityType, False)
                        self.register_field(UnderlyingSecuritySubType, False)
                        self.register_field(UnderlyingMaturityMonthYear, False)
                        self.register_field(UnderlyingMaturityDate, False)
                        self.register_field(UnderlyingPutOrCall, False)
                        self.register_field(UnderlyingCouponPaymentDate, False)
                        self.register_field(UnderlyingIssueDate, False)
                        self.register_field(UnderlyingRepoCollateralSecurityType, False)
                        self.register_field(UnderlyingRepurchaseTerm, False)
                        self.register_field(UnderlyingRepurchaseRate, False)
                        self.register_field(UnderlyingFactor, False)
                        self.register_field(UnderlyingCreditRating, False)
                        self.register_field(UnderlyingInstrRegistry, False)
                        self.register_field(UnderlyingCountryOfIssue, False)
                        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                        self.register_field(UnderlyingLocaleOfIssue, False)
                        self.register_field(UnderlyingRedemptionDate, False)
                        self.register_field(UnderlyingStrikePrice, False)
                        self.register_field(UnderlyingStrikeCurrency, False)
                        self.register_field(UnderlyingOptAttribute, False)
                        self.register_field(UnderlyingContractMultiplier, False)
                        self.register_field(UnderlyingCouponRate, False)
                        self.register_field(UnderlyingSecurityExchange, False)
                        self.register_field(UnderlyingIssuer, False)
                        self.register_field(EncodedUnderlyingIssuerLen, False)
                        self.register_field(EncodedUnderlyingIssuer, False)
                        self.register_field(UnderlyingSecurityDesc, False)
                        self.register_field(EncodedUnderlyingSecurityDescLen, False)
                        self.register_field(EncodedUnderlyingSecurityDesc, False)
                        self.register_field(UnderlyingCPProgram, False)
                        self.register_field(UnderlyingCPRegType, False)
                        self.register_field(UnderlyingCurrency, False)
                        self.register_field(UnderlyingQty, False)
                        self.register_field(UnderlyingPx, False)
                        self.register_field(UnderlyingDirtyPrice, False)
                        self.register_field(UnderlyingEndPrice, False)
                        self.register_field(UnderlyingStartValue, False)
                        self.register_field(UnderlyingCurrentValue, False)
                        self.register_field(UnderlyingEndValue, False)

                        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingStipType, False)
                                self.register_field(UnderlyingStipValue, False)

                        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

                self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
                self.register_field(PrevClosePx, False)
                self.register_field(QuoteRequestType, False)
                self.register_field(QuoteType, False)
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)
                self.register_field(TradeOriginationDate, False)
                self.register_field(Side, False)
                self.register_field(QtyType, False)
                self.register_field(OrderQty, False)
                self.register_field(CashOrderQty, False)
                self.register_field(OrderPercent, False)
                self.register_field(RoundingDirection, False)
                self.register_field(RoundingModulus, False)
                self.register_field(SettlType, False)
                self.register_field(SettlDate, False)
                self.register_field(SettlDate2, False)
                self.register_field(OrderQty2, False)
                self.register_field(Currency, False)

                class NoStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(StipulationType, False)
                        self.register_field(StipulationValue, False)

                self.register_group(NoStipulations, NoStipulationsGroup, False)
                self.register_field(Account, False)
                self.register_field(AcctIDSource, False)
                self.register_field(AccountType, False)

                class NoLegsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSymbol, False)
                        self.register_field(LegSymbolSfx, False)
                        self.register_field(LegSecurityID, False)
                        self.register_field(LegSecurityIDSource, False)

                        class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegSecurityAltID, False)
                                self.register_field(LegSecurityAltIDSource, False)

                        self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                        self.register_field(LegProduct, False)
                        self.register_field(LegCFICode, False)
                        self.register_field(LegSecurityType, False)
                        self.register_field(LegSecuritySubType, False)
                        self.register_field(LegMaturityMonthYear, False)
                        self.register_field(LegMaturityDate, False)
                        self.register_field(LegCouponPaymentDate, False)
                        self.register_field(LegIssueDate, False)
                        self.register_field(LegRepoCollateralSecurityType, False)
                        self.register_field(LegRepurchaseTerm, False)
                        self.register_field(LegRepurchaseRate, False)
                        self.register_field(LegFactor, False)
                        self.register_field(LegCreditRating, False)
                        self.register_field(LegInstrRegistry, False)
                        self.register_field(LegCountryOfIssue, False)
                        self.register_field(LegStateOrProvinceOfIssue, False)
                        self.register_field(LegLocaleOfIssue, False)
                        self.register_field(LegRedemptionDate, False)
                        self.register_field(LegStrikePrice, False)
                        self.register_field(LegStrikeCurrency, False)
                        self.register_field(LegOptAttribute, False)
                        self.register_field(LegContractMultiplier, False)
                        self.register_field(LegCouponRate, False)
                        self.register_field(LegSecurityExchange, False)
                        self.register_field(LegIssuer, False)
                        self.register_field(EncodedLegIssuerLen, False)
                        self.register_field(EncodedLegIssuer, False)
                        self.register_field(LegSecurityDesc, False)
                        self.register_field(EncodedLegSecurityDescLen, False)
                        self.register_field(EncodedLegSecurityDesc, False)
                        self.register_field(LegRatioQty, False)
                        self.register_field(LegSide, False)
                        self.register_field(LegCurrency, False)
                        self.register_field(LegPool, False)
                        self.register_field(LegDatedDate, False)
                        self.register_field(LegContractSettlMonth, False)
                        self.register_field(LegInterestAccrualDate, False)
                        self.register_field(LegQty, False)
                        self.register_field(LegSwapType, False)
                        self.register_field(LegSettlType, False)
                        self.register_field(LegSettlDate, False)

                        class NoLegStipulationsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegStipulationType, False)
                                self.register_field(LegStipulationValue, False)

                        self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)

                        class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartyID, False)
                                self.register_field(NestedPartyIDSource, False)
                                self.register_field(NestedPartyRole, False)

                                class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(NestedPartySubID, False)
                                        self.register_field(NestedPartySubIDType, False)

                                self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                        self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                        self.register_field(LegBenchmarkCurveCurrency, False)
                        self.register_field(LegBenchmarkCurveName, False)
                        self.register_field(LegBenchmarkCurvePoint, False)
                        self.register_field(LegBenchmarkPrice, False)
                        self.register_field(LegBenchmarkPriceType, False)

                self.register_group(NoLegs, NoLegsGroup, False)

                class NoQuoteQualifiersGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(QuoteQualifier, False)

                self.register_group(NoQuoteQualifiers, NoQuoteQualifiersGroup, False)
                self.register_field(QuotePriceType, False)
                self.register_field(OrdType, False)
                self.register_field(ExpireTime, False)
                self.register_field(TransactTime, False)
                self.register_field(Spread, False)
                self.register_field(BenchmarkCurveCurrency, False)
                self.register_field(BenchmarkCurveName, False)
                self.register_field(BenchmarkCurvePoint, False)
                self.register_field(BenchmarkPrice, False)
                self.register_field(BenchmarkPriceType, False)
                self.register_field(BenchmarkSecurityID, False)
                self.register_field(BenchmarkSecurityIDSource, False)
                self.register_field(PriceType, False)
                self.register_field(Price, False)
                self.register_field(Price2, False)
                self.register_field(YieldType, False)
                self.register_field(Yield, False)
                self.register_field(YieldCalcDate, False)
                self.register_field(YieldRedemptionDate, False)
                self.register_field(YieldRedemptionPrice, False)
                self.register_field(YieldRedemptionPriceType, False)

                class NoPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartyID, False)
                        self.register_field(PartyIDSource, False)
                        self.register_field(PartyRole, False)

                        class NoPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(PartySubID, False)
                                self.register_field(PartySubIDType, False)

                        self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

                self.register_group(NoPartyIDs, NoPartyIDsGroup, False)

        self.register_group(NoRelatedSym, NoRelatedSymGroup, True)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AG'] = QuoteRequestReject

class RFQRequest(fix_message.MessageBase):
    _msgtype = 'AH'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(RFQReqID, True)

        class NoRelatedSymGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(SecurityIDSource, False)

                class NoSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SecurityAltID, False)
                        self.register_field(SecurityAltIDSource, False)

                self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
                self.register_field(Product, False)
                self.register_field(CFICode, False)
                self.register_field(SecurityType, False)
                self.register_field(SecuritySubType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDate, False)
                self.register_field(PutOrCall, False)
                self.register_field(CouponPaymentDate, False)
                self.register_field(IssueDate, False)
                self.register_field(RepoCollateralSecurityType, False)
                self.register_field(RepurchaseTerm, False)
                self.register_field(RepurchaseRate, False)
                self.register_field(Factor, False)
                self.register_field(CreditRating, False)
                self.register_field(InstrRegistry, False)
                self.register_field(CountryOfIssue, False)
                self.register_field(StateOrProvinceOfIssue, False)
                self.register_field(LocaleOfIssue, False)
                self.register_field(RedemptionDate, False)
                self.register_field(StrikePrice, False)
                self.register_field(StrikeCurrency, False)
                self.register_field(OptAttribute, False)
                self.register_field(ContractMultiplier, False)
                self.register_field(CouponRate, False)
                self.register_field(SecurityExchange, False)
                self.register_field(Issuer, False)
                self.register_field(EncodedIssuerLen, False)
                self.register_field(EncodedIssuer, False)
                self.register_field(SecurityDesc, False)
                self.register_field(EncodedSecurityDescLen, False)
                self.register_field(EncodedSecurityDesc, False)
                self.register_field(Pool, False)
                self.register_field(ContractSettlMonth, False)
                self.register_field(CPProgram, False)
                self.register_field(CPRegType, False)

                class NoEventsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(EventType, False)
                        self.register_field(EventDate, False)
                        self.register_field(EventPx, False)
                        self.register_field(EventText, False)

                self.register_group(NoEvents, NoEventsGroup, False)
                self.register_field(DatedDate, False)
                self.register_field(InterestAccrualDate, False)

                class NoUnderlyingsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSymbol, False)
                        self.register_field(UnderlyingSymbolSfx, False)
                        self.register_field(UnderlyingSecurityID, False)
                        self.register_field(UnderlyingSecurityIDSource, False)

                        class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingSecurityAltID, False)
                                self.register_field(UnderlyingSecurityAltIDSource, False)

                        self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                        self.register_field(UnderlyingProduct, False)
                        self.register_field(UnderlyingCFICode, False)
                        self.register_field(UnderlyingSecurityType, False)
                        self.register_field(UnderlyingSecuritySubType, False)
                        self.register_field(UnderlyingMaturityMonthYear, False)
                        self.register_field(UnderlyingMaturityDate, False)
                        self.register_field(UnderlyingPutOrCall, False)
                        self.register_field(UnderlyingCouponPaymentDate, False)
                        self.register_field(UnderlyingIssueDate, False)
                        self.register_field(UnderlyingRepoCollateralSecurityType, False)
                        self.register_field(UnderlyingRepurchaseTerm, False)
                        self.register_field(UnderlyingRepurchaseRate, False)
                        self.register_field(UnderlyingFactor, False)
                        self.register_field(UnderlyingCreditRating, False)
                        self.register_field(UnderlyingInstrRegistry, False)
                        self.register_field(UnderlyingCountryOfIssue, False)
                        self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                        self.register_field(UnderlyingLocaleOfIssue, False)
                        self.register_field(UnderlyingRedemptionDate, False)
                        self.register_field(UnderlyingStrikePrice, False)
                        self.register_field(UnderlyingStrikeCurrency, False)
                        self.register_field(UnderlyingOptAttribute, False)
                        self.register_field(UnderlyingContractMultiplier, False)
                        self.register_field(UnderlyingCouponRate, False)
                        self.register_field(UnderlyingSecurityExchange, False)
                        self.register_field(UnderlyingIssuer, False)
                        self.register_field(EncodedUnderlyingIssuerLen, False)
                        self.register_field(EncodedUnderlyingIssuer, False)
                        self.register_field(UnderlyingSecurityDesc, False)
                        self.register_field(EncodedUnderlyingSecurityDescLen, False)
                        self.register_field(EncodedUnderlyingSecurityDesc, False)
                        self.register_field(UnderlyingCPProgram, False)
                        self.register_field(UnderlyingCPRegType, False)
                        self.register_field(UnderlyingCurrency, False)
                        self.register_field(UnderlyingQty, False)
                        self.register_field(UnderlyingPx, False)
                        self.register_field(UnderlyingDirtyPrice, False)
                        self.register_field(UnderlyingEndPrice, False)
                        self.register_field(UnderlyingStartValue, False)
                        self.register_field(UnderlyingCurrentValue, False)
                        self.register_field(UnderlyingEndValue, False)

                        class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(UnderlyingStipType, False)
                                self.register_field(UnderlyingStipValue, False)

                        self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

                self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

                class NoLegsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSymbol, False)
                        self.register_field(LegSymbolSfx, False)
                        self.register_field(LegSecurityID, False)
                        self.register_field(LegSecurityIDSource, False)

                        class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(LegSecurityAltID, False)
                                self.register_field(LegSecurityAltIDSource, False)

                        self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                        self.register_field(LegProduct, False)
                        self.register_field(LegCFICode, False)
                        self.register_field(LegSecurityType, False)
                        self.register_field(LegSecuritySubType, False)
                        self.register_field(LegMaturityMonthYear, False)
                        self.register_field(LegMaturityDate, False)
                        self.register_field(LegCouponPaymentDate, False)
                        self.register_field(LegIssueDate, False)
                        self.register_field(LegRepoCollateralSecurityType, False)
                        self.register_field(LegRepurchaseTerm, False)
                        self.register_field(LegRepurchaseRate, False)
                        self.register_field(LegFactor, False)
                        self.register_field(LegCreditRating, False)
                        self.register_field(LegInstrRegistry, False)
                        self.register_field(LegCountryOfIssue, False)
                        self.register_field(LegStateOrProvinceOfIssue, False)
                        self.register_field(LegLocaleOfIssue, False)
                        self.register_field(LegRedemptionDate, False)
                        self.register_field(LegStrikePrice, False)
                        self.register_field(LegStrikeCurrency, False)
                        self.register_field(LegOptAttribute, False)
                        self.register_field(LegContractMultiplier, False)
                        self.register_field(LegCouponRate, False)
                        self.register_field(LegSecurityExchange, False)
                        self.register_field(LegIssuer, False)
                        self.register_field(EncodedLegIssuerLen, False)
                        self.register_field(EncodedLegIssuer, False)
                        self.register_field(LegSecurityDesc, False)
                        self.register_field(EncodedLegSecurityDescLen, False)
                        self.register_field(EncodedLegSecurityDesc, False)
                        self.register_field(LegRatioQty, False)
                        self.register_field(LegSide, False)
                        self.register_field(LegCurrency, False)
                        self.register_field(LegPool, False)
                        self.register_field(LegDatedDate, False)
                        self.register_field(LegContractSettlMonth, False)
                        self.register_field(LegInterestAccrualDate, False)

                self.register_group(NoLegs, NoLegsGroup, False)
                self.register_field(PrevClosePx, False)
                self.register_field(QuoteRequestType, False)
                self.register_field(QuoteType, False)
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoRelatedSym, NoRelatedSymGroup, True)
        self.register_field(SubscriptionRequestType, False)

MESSAGE_TYPES['AH'] = RFQRequest

class QuoteStatusReport(fix_message.MessageBase):
    _msgtype = 'AI'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(QuoteStatusReqID, False)
        self.register_field(QuoteReqID, False)
        self.register_field(QuoteID, True)
        self.register_field(QuoteRespID, False)
        self.register_field(QuoteType, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(Side, False)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(SettlDate2, False)
        self.register_field(OrderQty2, False)
        self.register_field(Currency, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)
                self.register_field(LegQty, False)
                self.register_field(LegSwapType, False)
                self.register_field(LegSettlType, False)
                self.register_field(LegSettlDate, False)

                class NoLegStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegStipulationType, False)
                        self.register_field(LegStipulationValue, False)

                self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoQuoteQualifiersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(QuoteQualifier, False)

        self.register_group(NoQuoteQualifiers, NoQuoteQualifiersGroup, False)
        self.register_field(ExpireTime, False)
        self.register_field(Price, False)
        self.register_field(PriceType, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)
        self.register_field(BidPx, False)
        self.register_field(OfferPx, False)
        self.register_field(MktBidPx, False)
        self.register_field(MktOfferPx, False)
        self.register_field(MinBidSize, False)
        self.register_field(BidSize, False)
        self.register_field(MinOfferSize, False)
        self.register_field(OfferSize, False)
        self.register_field(ValidUntilTime, False)
        self.register_field(BidSpotRate, False)
        self.register_field(OfferSpotRate, False)
        self.register_field(BidForwardPoints, False)
        self.register_field(OfferForwardPoints, False)
        self.register_field(MidPx, False)
        self.register_field(BidYield, False)
        self.register_field(MidYield, False)
        self.register_field(OfferYield, False)
        self.register_field(TransactTime, False)
        self.register_field(OrdType, False)
        self.register_field(BidForwardPoints2, False)
        self.register_field(OfferForwardPoints2, False)
        self.register_field(SettlCurrBidFxRate, False)
        self.register_field(SettlCurrOfferFxRate, False)
        self.register_field(SettlCurrFxRateCalc, False)
        self.register_field(CommType, False)
        self.register_field(Commission, False)
        self.register_field(CustOrderCapacity, False)
        self.register_field(ExDestination, False)
        self.register_field(QuoteStatus, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AI'] = QuoteStatusReport

class QuoteResponse(fix_message.MessageBase):
    _msgtype = 'AJ'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(QuoteRespID, True)
        self.register_field(QuoteID, False)
        self.register_field(QuoteRespType, True)
        self.register_field(ClOrdID, False)
        self.register_field(OrderCapacity, False)
        self.register_field(IOIID, False)
        self.register_field(QuoteType, False)

        class NoQuoteQualifiersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(QuoteQualifier, False)

        self.register_group(NoQuoteQualifiers, NoQuoteQualifiersGroup, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(Side, False)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrderPercent, False)
        self.register_field(RoundingDirection, False)
        self.register_field(RoundingModulus, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(SettlDate2, False)
        self.register_field(OrderQty2, False)
        self.register_field(Currency, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)
                self.register_field(LegQty, False)
                self.register_field(LegSwapType, False)
                self.register_field(LegSettlType, False)
                self.register_field(LegSettlDate, False)

                class NoLegStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegStipulationType, False)
                        self.register_field(LegStipulationValue, False)

                self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(LegPriceType, False)
                self.register_field(LegBidPx, False)
                self.register_field(LegOfferPx, False)
                self.register_field(LegBenchmarkCurveCurrency, False)
                self.register_field(LegBenchmarkCurveName, False)
                self.register_field(LegBenchmarkCurvePoint, False)
                self.register_field(LegBenchmarkPrice, False)
                self.register_field(LegBenchmarkPriceType, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(BidPx, False)
        self.register_field(OfferPx, False)
        self.register_field(MktBidPx, False)
        self.register_field(MktOfferPx, False)
        self.register_field(MinBidSize, False)
        self.register_field(BidSize, False)
        self.register_field(MinOfferSize, False)
        self.register_field(OfferSize, False)
        self.register_field(ValidUntilTime, False)
        self.register_field(BidSpotRate, False)
        self.register_field(OfferSpotRate, False)
        self.register_field(BidForwardPoints, False)
        self.register_field(OfferForwardPoints, False)
        self.register_field(MidPx, False)
        self.register_field(BidYield, False)
        self.register_field(MidYield, False)
        self.register_field(OfferYield, False)
        self.register_field(TransactTime, False)
        self.register_field(OrdType, False)
        self.register_field(BidForwardPoints2, False)
        self.register_field(OfferForwardPoints2, False)
        self.register_field(SettlCurrBidFxRate, False)
        self.register_field(SettlCurrOfferFxRate, False)
        self.register_field(SettlCurrFxRateCalc, False)
        self.register_field(Commission, False)
        self.register_field(CommType, False)
        self.register_field(CustOrderCapacity, False)
        self.register_field(ExDestination, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(Price, False)
        self.register_field(PriceType, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)

MESSAGE_TYPES['AJ'] = QuoteResponse

class Confirmation(fix_message.MessageBase):
    _msgtype = 'AK'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ConfirmID, True)
        self.register_field(ConfirmRefID, False)
        self.register_field(ConfirmReqID, False)
        self.register_field(ConfirmTransType, True)
        self.register_field(ConfirmType, True)
        self.register_field(CopyMsgIndicator, False)
        self.register_field(LegalConfirm, False)
        self.register_field(ConfirmStatus, True)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)

        class NoOrdersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ClOrdID, False)
                self.register_field(OrderID, False)
                self.register_field(SecondaryOrderID, False)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(ListID, False)

                class NoNested2PartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(Nested2PartyID, False)
                        self.register_field(Nested2PartyIDSource, False)
                        self.register_field(Nested2PartyRole, False)

                        class NoNested2PartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(Nested2PartySubID, False)
                                self.register_field(Nested2PartySubIDType, False)

                        self.register_group(NoNested2PartySubIDs, NoNested2PartySubIDsGroup, False)

                self.register_group(NoNested2PartyIDs, NoNested2PartyIDsGroup, False)
                self.register_field(OrderQty, False)
                self.register_field(OrderAvgPx, False)
                self.register_field(OrderBookingQty, False)

        self.register_group(NoOrders, NoOrdersGroup, False)
        self.register_field(AllocID, False)
        self.register_field(SecondaryAllocID, False)
        self.register_field(IndividualAllocID, False)
        self.register_field(TransactTime, True)
        self.register_field(TradeDate, True)

        class NoTrdRegTimestampsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TrdRegTimestamp, False)
                self.register_field(TrdRegTimestampType, False)
                self.register_field(TrdRegTimestampOrigin, False)

        self.register_group(NoTrdRegTimestamps, NoTrdRegTimestampsGroup, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(DeliveryForm, False)
        self.register_field(PctAtRisk, False)

        class NoInstrAttribGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(InstrAttribType, False)
                self.register_field(InstrAttribValue, False)

        self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)
        self.register_field(AllocQty, True)
        self.register_field(QtyType, False)
        self.register_field(Side, True)
        self.register_field(Currency, False)
        self.register_field(LastMkt, False)

        class NoCapacitiesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(OrderCapacity, True)
                self.register_field(OrderRestrictions, False)
                self.register_field(OrderCapacityQty, True)

        self.register_group(NoCapacities, NoCapacitiesGroup, True)
        self.register_field(AllocAccount, True)
        self.register_field(AllocAcctIDSource, False)
        self.register_field(AllocAccountType, False)
        self.register_field(AvgPx, True)
        self.register_field(AvgPxPrecision, False)
        self.register_field(PriceType, False)
        self.register_field(AvgParPx, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(ReportedPx, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(ProcessCode, False)
        self.register_field(GrossTradeAmt, True)
        self.register_field(NumDaysInterest, False)
        self.register_field(ExDate, False)
        self.register_field(AccruedInterestRate, False)
        self.register_field(AccruedInterestAmt, False)
        self.register_field(InterestAtMaturity, False)
        self.register_field(EndAccruedInterestAmt, False)
        self.register_field(StartCash, False)
        self.register_field(EndCash, False)
        self.register_field(Concession, False)
        self.register_field(TotalTakedown, False)
        self.register_field(NetMoney, True)
        self.register_field(MaturityNetMoney, False)
        self.register_field(SettlCurrAmt, False)
        self.register_field(SettlCurrency, False)
        self.register_field(SettlCurrFxRate, False)
        self.register_field(SettlCurrFxRateCalc, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(SettlDeliveryType, False)
        self.register_field(StandInstDbType, False)
        self.register_field(StandInstDbName, False)
        self.register_field(StandInstDbID, False)

        class NoDlvyInstGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SettlInstSource, False)
                self.register_field(DlvyInstType, False)

                class NoSettlPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SettlPartyID, False)
                        self.register_field(SettlPartyIDSource, False)
                        self.register_field(SettlPartyRole, False)

                        class NoSettlPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(SettlPartySubID, False)
                                self.register_field(SettlPartySubIDType, False)

                        self.register_group(NoSettlPartySubIDs, NoSettlPartySubIDsGroup, False)

                self.register_group(NoSettlPartyIDs, NoSettlPartyIDsGroup, False)

        self.register_group(NoDlvyInst, NoDlvyInstGroup, False)
        self.register_field(Commission, False)
        self.register_field(CommType, False)
        self.register_field(CommCurrency, False)
        self.register_field(FundRenewWaiv, False)
        self.register_field(SharedCommission, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)

        class NoMiscFeesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(MiscFeeAmt, False)
                self.register_field(MiscFeeCurr, False)
                self.register_field(MiscFeeType, False)
                self.register_field(MiscFeeBasis, False)

        self.register_group(NoMiscFees, NoMiscFeesGroup, False)

MESSAGE_TYPES['AK'] = Confirmation

class PositionMaintenanceRequest(fix_message.MessageBase):
    _msgtype = 'AL'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(PosReqID, True)
        self.register_field(PosTransType, True)
        self.register_field(PosMaintAction, True)
        self.register_field(OrigPosReqRefID, False)
        self.register_field(PosMaintRptRefID, False)
        self.register_field(ClearingBusinessDate, True)
        self.register_field(SettlSessID, False)
        self.register_field(SettlSessSubID, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, True)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(TransactTime, True)

        class NoPositionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PosType, False)
                self.register_field(LongQty, False)
                self.register_field(ShortQty, False)
                self.register_field(PosQtyStatus, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)

        self.register_group(NoPositions, NoPositionsGroup, False)
        self.register_field(AdjustmentType, False)
        self.register_field(ContraryInstructionIndicator, False)
        self.register_field(PriorSpreadIndicator, False)
        self.register_field(ThresholdAmount, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AL'] = PositionMaintenanceRequest

class PositionMaintenanceReport(fix_message.MessageBase):
    _msgtype = 'AM'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(PosMaintRptID, True)
        self.register_field(PosTransType, True)
        self.register_field(PosReqID, False)
        self.register_field(PosMaintAction, True)
        self.register_field(OrigPosReqRefID, True)
        self.register_field(PosMaintStatus, True)
        self.register_field(PosMaintResult, False)
        self.register_field(ClearingBusinessDate, True)
        self.register_field(SettlSessID, False)
        self.register_field(SettlSessSubID, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, True)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(TransactTime, True)

        class NoPositionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PosType, False)
                self.register_field(LongQty, False)
                self.register_field(ShortQty, False)
                self.register_field(PosQtyStatus, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)

        self.register_group(NoPositions, NoPositionsGroup, False)

        class NoPosAmtGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PosAmtType, False)
                self.register_field(PosAmt, False)

        self.register_group(NoPosAmt, NoPosAmtGroup, False)
        self.register_field(AdjustmentType, False)
        self.register_field(ThresholdAmount, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AM'] = PositionMaintenanceReport

class RequestForPositions(fix_message.MessageBase):
    _msgtype = 'AN'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(PosReqID, True)
        self.register_field(PosReqType, True)
        self.register_field(MatchStatus, False)
        self.register_field(SubscriptionRequestType, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, True)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(ClearingBusinessDate, True)
        self.register_field(SettlSessID, False)
        self.register_field(SettlSessSubID, False)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)
                self.register_field(TradingSessionSubID, False)

        self.register_group(NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(TransactTime, True)
        self.register_field(ResponseTransportType, False)
        self.register_field(ResponseDestination, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AN'] = RequestForPositions

class RequestForPositionsAck(fix_message.MessageBase):
    _msgtype = 'AO'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(PosMaintRptID, True)
        self.register_field(PosReqID, False)
        self.register_field(TotalNumPosReports, False)
        self.register_field(UnsolicitedIndicator, False)
        self.register_field(PosReqResult, True)
        self.register_field(PosReqStatus, True)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, True)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(ResponseTransportType, False)
        self.register_field(ResponseDestination, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AO'] = RequestForPositionsAck

class PositionReport(fix_message.MessageBase):
    _msgtype = 'AP'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(PosMaintRptID, True)
        self.register_field(PosReqID, False)
        self.register_field(PosReqType, False)
        self.register_field(SubscriptionRequestType, False)
        self.register_field(TotalNumPosReports, False)
        self.register_field(UnsolicitedIndicator, False)
        self.register_field(PosReqResult, True)
        self.register_field(ClearingBusinessDate, True)
        self.register_field(SettlSessID, False)
        self.register_field(SettlSessSubID, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, True)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(Currency, False)
        self.register_field(SettlPrice, True)
        self.register_field(SettlPriceType, True)
        self.register_field(PriorSettlPrice, True)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
                self.register_field(UnderlyingSettlPrice, True)
                self.register_field(UnderlyingSettlPriceType, True)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoPositionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PosType, False)
                self.register_field(LongQty, False)
                self.register_field(ShortQty, False)
                self.register_field(PosQtyStatus, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)

        self.register_group(NoPositions, NoPositionsGroup, False)

        class NoPosAmtGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PosAmtType, False)
                self.register_field(PosAmt, False)

        self.register_group(NoPosAmt, NoPosAmtGroup, False)
        self.register_field(RegistStatus, False)
        self.register_field(DeliveryDate, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AP'] = PositionReport

class TradeCaptureReportRequestAck(fix_message.MessageBase):
    _msgtype = 'AQ'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(TradeRequestID, True)
        self.register_field(TradeRequestType, True)
        self.register_field(SubscriptionRequestType, False)
        self.register_field(TotNumTradeReports, False)
        self.register_field(TradeRequestResult, True)
        self.register_field(TradeRequestStatus, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(MultiLegReportingType, False)
        self.register_field(ResponseTransportType, False)
        self.register_field(ResponseDestination, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AQ'] = TradeCaptureReportRequestAck

class TradeCaptureReportAck(fix_message.MessageBase):
    _msgtype = 'AR'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(TradeReportID, True)
        self.register_field(TradeReportTransType, False)
        self.register_field(TradeReportType, False)
        self.register_field(TrdType, False)
        self.register_field(TrdSubType, False)
        self.register_field(SecondaryTrdType, False)
        self.register_field(TransferReason, False)
        self.register_field(ExecType, True)
        self.register_field(TradeReportRefID, False)
        self.register_field(SecondaryTradeReportRefID, False)
        self.register_field(TrdRptStatus, False)
        self.register_field(TradeReportRejectReason, False)
        self.register_field(SecondaryTradeReportID, False)
        self.register_field(SubscriptionRequestType, False)
        self.register_field(TradeLinkID, False)
        self.register_field(TrdMatchID, False)
        self.register_field(ExecID, False)
        self.register_field(SecondaryExecID, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(TransactTime, False)

        class NoTrdRegTimestampsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TrdRegTimestamp, False)
                self.register_field(TrdRegTimestampType, False)
                self.register_field(TrdRegTimestampOrigin, False)

        self.register_group(NoTrdRegTimestamps, NoTrdRegTimestampsGroup, False)
        self.register_field(ResponseTransportType, False)
        self.register_field(ResponseDestination, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)
                self.register_field(LegQty, False)
                self.register_field(LegSwapType, False)

                class NoLegStipulationsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegStipulationType, False)
                        self.register_field(LegStipulationValue, False)

                self.register_group(NoLegStipulations, NoLegStipulationsGroup, False)
                self.register_field(LegPositionEffect, False)
                self.register_field(LegCoveredOrUncovered, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(LegRefID, False)
                self.register_field(LegPrice, False)
                self.register_field(LegSettlType, False)
                self.register_field(LegSettlDate, False)
                self.register_field(LegLastPx, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(ClearingFeeIndicator, False)
        self.register_field(OrderCapacity, False)
        self.register_field(OrderRestrictions, False)
        self.register_field(CustOrderCapacity, False)
        self.register_field(Account, False)
        self.register_field(AcctIDSource, False)
        self.register_field(AccountType, False)
        self.register_field(PositionEffect, False)
        self.register_field(PreallocMethod, False)

        class NoAllocsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AllocAccount, False)
                self.register_field(AllocAcctIDSource, False)
                self.register_field(AllocSettlCurrency, False)
                self.register_field(IndividualAllocID, False)

                class NoNested2PartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(Nested2PartyID, False)
                        self.register_field(Nested2PartyIDSource, False)
                        self.register_field(Nested2PartyRole, False)

                        class NoNested2PartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(Nested2PartySubID, False)
                                self.register_field(Nested2PartySubIDType, False)

                        self.register_group(NoNested2PartySubIDs, NoNested2PartySubIDsGroup, False)

                self.register_group(NoNested2PartyIDs, NoNested2PartyIDsGroup, False)
                self.register_field(AllocQty, False)

        self.register_group(NoAllocs, NoAllocsGroup, False)

MESSAGE_TYPES['AR'] = TradeCaptureReportAck

class AllocationReport(fix_message.MessageBase):
    _msgtype = 'AS'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(AllocReportID, True)
        self.register_field(AllocID, False)
        self.register_field(AllocTransType, True)
        self.register_field(AllocReportRefID, False)
        self.register_field(AllocCancReplaceReason, False)
        self.register_field(SecondaryAllocID, False)
        self.register_field(AllocReportType, True)
        self.register_field(AllocStatus, True)
        self.register_field(AllocRejCode, False)
        self.register_field(RefAllocID, False)
        self.register_field(AllocIntermedReqType, False)
        self.register_field(AllocLinkID, False)
        self.register_field(AllocLinkType, False)
        self.register_field(BookingRefID, False)
        self.register_field(AllocNoOrdersType, True)

        class NoOrdersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ClOrdID, False)
                self.register_field(OrderID, False)
                self.register_field(SecondaryOrderID, False)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(ListID, False)

                class NoNested2PartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(Nested2PartyID, False)
                        self.register_field(Nested2PartyIDSource, False)
                        self.register_field(Nested2PartyRole, False)

                        class NoNested2PartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(Nested2PartySubID, False)
                                self.register_field(Nested2PartySubIDType, False)

                        self.register_group(NoNested2PartySubIDs, NoNested2PartySubIDsGroup, False)

                self.register_group(NoNested2PartyIDs, NoNested2PartyIDsGroup, False)
                self.register_field(OrderQty, False)
                self.register_field(OrderAvgPx, False)
                self.register_field(OrderBookingQty, False)

        self.register_group(NoOrders, NoOrdersGroup, False)

        class NoExecsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LastQty, False)
                self.register_field(ExecID, False)
                self.register_field(SecondaryExecID, False)
                self.register_field(LastPx, False)
                self.register_field(LastParPx, False)
                self.register_field(LastCapacity, False)

        self.register_group(NoExecs, NoExecsGroup, False)
        self.register_field(PreviouslyReported, False)
        self.register_field(ReversalIndicator, False)
        self.register_field(MatchType, False)
        self.register_field(Side, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(DeliveryForm, False)
        self.register_field(PctAtRisk, False)

        class NoInstrAttribGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(InstrAttribType, False)
                self.register_field(InstrAttribValue, False)

        self.register_group(NoInstrAttrib, NoInstrAttribGroup, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)
        self.register_field(Quantity, True)
        self.register_field(QtyType, False)
        self.register_field(LastMkt, False)
        self.register_field(TradeOriginationDate, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(PriceType, False)
        self.register_field(AvgPx, True)
        self.register_field(AvgParPx, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)
        self.register_field(Currency, False)
        self.register_field(AvgPxPrecision, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(TradeDate, True)
        self.register_field(TransactTime, False)
        self.register_field(SettlType, False)
        self.register_field(SettlDate, False)
        self.register_field(BookingType, False)
        self.register_field(GrossTradeAmt, False)
        self.register_field(Concession, False)
        self.register_field(TotalTakedown, False)
        self.register_field(NetMoney, False)
        self.register_field(PositionEffect, False)
        self.register_field(AutoAcceptIndicator, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(NumDaysInterest, False)
        self.register_field(AccruedInterestRate, False)
        self.register_field(AccruedInterestAmt, False)
        self.register_field(TotalAccruedInterestAmt, False)
        self.register_field(InterestAtMaturity, False)
        self.register_field(EndAccruedInterestAmt, False)
        self.register_field(StartCash, False)
        self.register_field(EndCash, False)
        self.register_field(LegalConfirm, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(YieldType, False)
        self.register_field(Yield, False)
        self.register_field(YieldCalcDate, False)
        self.register_field(YieldRedemptionDate, False)
        self.register_field(YieldRedemptionPrice, False)
        self.register_field(YieldRedemptionPriceType, False)
        self.register_field(TotNoAllocs, False)
        self.register_field(LastFragment, False)

        class NoAllocsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AllocAccount, False)
                self.register_field(AllocAcctIDSource, False)
                self.register_field(MatchStatus, False)
                self.register_field(AllocPrice, False)
                self.register_field(AllocQty, False)
                self.register_field(IndividualAllocID, False)
                self.register_field(ProcessCode, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)
                self.register_field(NotifyBrokerOfCredit, False)
                self.register_field(AllocHandlInst, False)
                self.register_field(AllocText, False)
                self.register_field(EncodedAllocTextLen, False)
                self.register_field(EncodedAllocText, False)
                self.register_field(Commission, False)
                self.register_field(CommType, False)
                self.register_field(CommCurrency, False)
                self.register_field(FundRenewWaiv, False)
                self.register_field(AllocAvgPx, False)
                self.register_field(AllocNetMoney, False)
                self.register_field(SettlCurrAmt, False)
                self.register_field(AllocSettlCurrAmt, False)
                self.register_field(SettlCurrency, False)
                self.register_field(AllocSettlCurrency, False)
                self.register_field(SettlCurrFxRate, False)
                self.register_field(SettlCurrFxRateCalc, False)
                self.register_field(AllocAccruedInterestAmt, False)
                self.register_field(AllocInterestAtMaturity, False)

                class NoMiscFeesGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(MiscFeeAmt, False)
                        self.register_field(MiscFeeCurr, False)
                        self.register_field(MiscFeeType, False)
                        self.register_field(MiscFeeBasis, False)

                self.register_group(NoMiscFees, NoMiscFeesGroup, False)

                class NoClearingInstructionsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(ClearingInstruction, False)

                self.register_group(NoClearingInstructions, NoClearingInstructionsGroup, False)
                self.register_field(AllocSettlInstType, False)
                self.register_field(SettlDeliveryType, False)
                self.register_field(StandInstDbType, False)
                self.register_field(StandInstDbName, False)
                self.register_field(StandInstDbID, False)

                class NoDlvyInstGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SettlInstSource, False)
                        self.register_field(DlvyInstType, False)

                        class NoSettlPartyIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(SettlPartyID, False)
                                self.register_field(SettlPartyIDSource, False)
                                self.register_field(SettlPartyRole, False)

                                class NoSettlPartySubIDsGroup(fix_message.FIXGroup):
                                    def __init__(self):
                                        self.register_field(SettlPartySubID, False)
                                        self.register_field(SettlPartySubIDType, False)

                                self.register_group(NoSettlPartySubIDs, NoSettlPartySubIDsGroup, False)

                        self.register_group(NoSettlPartyIDs, NoSettlPartyIDsGroup, False)

                self.register_group(NoDlvyInst, NoDlvyInstGroup, False)

        self.register_group(NoAllocs, NoAllocsGroup, False)

MESSAGE_TYPES['AS'] = AllocationReport

class AllocationReportAck(fix_message.MessageBase):
    _msgtype = 'AT'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(AllocReportID, True)
        self.register_field(AllocID, True)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(SecondaryAllocID, False)
        self.register_field(TradeDate, False)
        self.register_field(TransactTime, True)
        self.register_field(AllocStatus, True)
        self.register_field(AllocRejCode, False)
        self.register_field(AllocReportType, False)
        self.register_field(AllocIntermedReqType, False)
        self.register_field(MatchStatus, False)
        self.register_field(Product, False)
        self.register_field(SecurityType, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

        class NoAllocsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AllocAccount, False)
                self.register_field(AllocAcctIDSource, False)
                self.register_field(AllocPrice, False)
                self.register_field(IndividualAllocID, False)
                self.register_field(IndividualAllocRejCode, False)
                self.register_field(AllocText, False)
                self.register_field(EncodedAllocTextLen, False)
                self.register_field(EncodedAllocText, False)

        self.register_group(NoAllocs, NoAllocsGroup, False)

MESSAGE_TYPES['AT'] = AllocationReportAck

class ConfirmationAck(fix_message.MessageBase):
    _msgtype = 'AU'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ConfirmID, True)
        self.register_field(TradeDate, True)
        self.register_field(TransactTime, True)
        self.register_field(AffirmStatus, True)
        self.register_field(ConfirmRejReason, False)
        self.register_field(MatchStatus, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AU'] = ConfirmationAck

class SettlementInstructionRequest(fix_message.MessageBase):
    _msgtype = 'AV'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(SettlInstReqID, True)
        self.register_field(TransactTime, True)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(AllocAccount, False)
        self.register_field(AllocAcctIDSource, False)
        self.register_field(Side, False)
        self.register_field(Product, False)
        self.register_field(SecurityType, False)
        self.register_field(CFICode, False)
        self.register_field(EffectiveTime, False)
        self.register_field(ExpireTime, False)
        self.register_field(LastUpdateTime, False)
        self.register_field(StandInstDbType, False)
        self.register_field(StandInstDbName, False)
        self.register_field(StandInstDbID, False)

MESSAGE_TYPES['AV'] = SettlementInstructionRequest

class AssignmentReport(fix_message.MessageBase):
    _msgtype = 'AW'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(AsgnRptID, True)
        self.register_field(TotNumAssignmentReports, False)
        self.register_field(LastRptRequested, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AccountType, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)

        class NoPositionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PosType, False)
                self.register_field(LongQty, False)
                self.register_field(ShortQty, False)
                self.register_field(PosQtyStatus, False)

                class NoNestedPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(NestedPartyID, False)
                        self.register_field(NestedPartyIDSource, False)
                        self.register_field(NestedPartyRole, False)

                        class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(NestedPartySubID, False)
                                self.register_field(NestedPartySubIDType, False)

                        self.register_group(NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

                self.register_group(NoNestedPartyIDs, NoNestedPartyIDsGroup, False)

        self.register_group(NoPositions, NoPositionsGroup, False)

        class NoPosAmtGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PosAmtType, False)
                self.register_field(PosAmt, False)

        self.register_group(NoPosAmt, NoPosAmtGroup, False)
        self.register_field(ThresholdAmount, False)
        self.register_field(SettlPrice, True)
        self.register_field(SettlPriceType, True)
        self.register_field(UnderlyingSettlPrice, True)
        self.register_field(ExpireDate, False)
        self.register_field(AssignmentMethod, True)
        self.register_field(AssignmentUnit, False)
        self.register_field(OpenInterest, True)
        self.register_field(ExerciseMethod, True)
        self.register_field(SettlSessID, True)
        self.register_field(SettlSessSubID, True)
        self.register_field(ClearingBusinessDate, True)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AW'] = AssignmentReport

class CollateralRequest(fix_message.MessageBase):
    _msgtype = 'AX'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(CollReqID, True)
        self.register_field(CollAsgnReason, True)
        self.register_field(TransactTime, True)
        self.register_field(ExpireTime, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AccountType, False)
        self.register_field(ClOrdID, False)
        self.register_field(OrderID, False)
        self.register_field(SecondaryOrderID, False)
        self.register_field(SecondaryClOrdID, False)

        class NoExecsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ExecID, False)

        self.register_group(NoExecs, NoExecsGroup, False)

        class NoTradesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradeReportID, False)
                self.register_field(SecondaryTradeReportID, False)

        self.register_group(NoTrades, NoTradesGroup, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)
        self.register_field(SettlDate, False)
        self.register_field(Quantity, False)
        self.register_field(QtyType, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
                self.register_field(CollAction, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(MarginExcess, False)
        self.register_field(TotalNetValue, False)
        self.register_field(CashOutstanding, False)

        class NoTrdRegTimestampsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TrdRegTimestamp, False)
                self.register_field(TrdRegTimestampType, False)
                self.register_field(TrdRegTimestampOrigin, False)

        self.register_group(NoTrdRegTimestamps, NoTrdRegTimestampsGroup, False)
        self.register_field(Side, False)

        class NoMiscFeesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(MiscFeeAmt, False)
                self.register_field(MiscFeeCurr, False)
                self.register_field(MiscFeeType, False)
                self.register_field(MiscFeeBasis, False)

        self.register_group(NoMiscFees, NoMiscFeesGroup, False)
        self.register_field(Price, False)
        self.register_field(PriceType, False)
        self.register_field(AccruedInterestAmt, False)
        self.register_field(EndAccruedInterestAmt, False)
        self.register_field(StartCash, False)
        self.register_field(EndCash, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(SettlSessID, False)
        self.register_field(SettlSessSubID, False)
        self.register_field(ClearingBusinessDate, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AX'] = CollateralRequest

class CollateralAssignment(fix_message.MessageBase):
    _msgtype = 'AY'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(CollAsgnID, True)
        self.register_field(CollReqID, False)
        self.register_field(CollAsgnReason, True)
        self.register_field(CollAsgnTransType, True)
        self.register_field(CollAsgnRefID, False)
        self.register_field(TransactTime, True)
        self.register_field(ExpireTime, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AccountType, False)
        self.register_field(ClOrdID, False)
        self.register_field(OrderID, False)
        self.register_field(SecondaryOrderID, False)
        self.register_field(SecondaryClOrdID, False)

        class NoExecsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ExecID, False)

        self.register_group(NoExecs, NoExecsGroup, False)

        class NoTradesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradeReportID, False)
                self.register_field(SecondaryTradeReportID, False)

        self.register_group(NoTrades, NoTradesGroup, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)
        self.register_field(SettlDate, False)
        self.register_field(Quantity, False)
        self.register_field(QtyType, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
                self.register_field(CollAction, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(MarginExcess, False)
        self.register_field(TotalNetValue, False)
        self.register_field(CashOutstanding, False)

        class NoTrdRegTimestampsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TrdRegTimestamp, False)
                self.register_field(TrdRegTimestampType, False)
                self.register_field(TrdRegTimestampOrigin, False)

        self.register_group(NoTrdRegTimestamps, NoTrdRegTimestampsGroup, False)
        self.register_field(Side, False)

        class NoMiscFeesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(MiscFeeAmt, False)
                self.register_field(MiscFeeCurr, False)
                self.register_field(MiscFeeType, False)
                self.register_field(MiscFeeBasis, False)

        self.register_group(NoMiscFees, NoMiscFeesGroup, False)
        self.register_field(Price, False)
        self.register_field(PriceType, False)
        self.register_field(AccruedInterestAmt, False)
        self.register_field(EndAccruedInterestAmt, False)
        self.register_field(StartCash, False)
        self.register_field(EndCash, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(SettlDeliveryType, False)
        self.register_field(StandInstDbType, False)
        self.register_field(StandInstDbName, False)
        self.register_field(StandInstDbID, False)

        class NoDlvyInstGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SettlInstSource, False)
                self.register_field(DlvyInstType, False)

                class NoSettlPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SettlPartyID, False)
                        self.register_field(SettlPartyIDSource, False)
                        self.register_field(SettlPartyRole, False)

                        class NoSettlPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(SettlPartySubID, False)
                                self.register_field(SettlPartySubIDType, False)

                        self.register_group(NoSettlPartySubIDs, NoSettlPartySubIDsGroup, False)

                self.register_group(NoSettlPartyIDs, NoSettlPartyIDsGroup, False)

        self.register_group(NoDlvyInst, NoDlvyInstGroup, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(SettlSessID, False)
        self.register_field(SettlSessSubID, False)
        self.register_field(ClearingBusinessDate, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AY'] = CollateralAssignment

class CollateralResponse(fix_message.MessageBase):
    _msgtype = 'AZ'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(CollRespID, True)
        self.register_field(CollAsgnID, True)
        self.register_field(CollReqID, False)
        self.register_field(CollAsgnReason, True)
        self.register_field(CollAsgnTransType, False)
        self.register_field(CollAsgnRespType, True)
        self.register_field(CollAsgnRejectReason, False)
        self.register_field(TransactTime, True)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AccountType, False)
        self.register_field(ClOrdID, False)
        self.register_field(OrderID, False)
        self.register_field(SecondaryOrderID, False)
        self.register_field(SecondaryClOrdID, False)

        class NoExecsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ExecID, False)

        self.register_group(NoExecs, NoExecsGroup, False)

        class NoTradesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradeReportID, False)
                self.register_field(SecondaryTradeReportID, False)

        self.register_group(NoTrades, NoTradesGroup, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)
        self.register_field(SettlDate, False)
        self.register_field(Quantity, False)
        self.register_field(QtyType, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)
                self.register_field(CollAction, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(MarginExcess, False)
        self.register_field(TotalNetValue, False)
        self.register_field(CashOutstanding, False)

        class NoTrdRegTimestampsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TrdRegTimestamp, False)
                self.register_field(TrdRegTimestampType, False)
                self.register_field(TrdRegTimestampOrigin, False)

        self.register_group(NoTrdRegTimestamps, NoTrdRegTimestampsGroup, False)
        self.register_field(Side, False)

        class NoMiscFeesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(MiscFeeAmt, False)
                self.register_field(MiscFeeCurr, False)
                self.register_field(MiscFeeType, False)
                self.register_field(MiscFeeBasis, False)

        self.register_group(NoMiscFees, NoMiscFeesGroup, False)
        self.register_field(Price, False)
        self.register_field(PriceType, False)
        self.register_field(AccruedInterestAmt, False)
        self.register_field(EndAccruedInterestAmt, False)
        self.register_field(StartCash, False)
        self.register_field(EndCash, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['AZ'] = CollateralResponse

class CollateralReport(fix_message.MessageBase):
    _msgtype = 'BA'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(CollRptID, True)
        self.register_field(CollInquiryID, False)
        self.register_field(CollStatus, True)
        self.register_field(TotNumReports, False)
        self.register_field(LastRptRequested, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AccountType, False)
        self.register_field(ClOrdID, False)
        self.register_field(OrderID, False)
        self.register_field(SecondaryOrderID, False)
        self.register_field(SecondaryClOrdID, False)

        class NoExecsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ExecID, False)

        self.register_group(NoExecs, NoExecsGroup, False)

        class NoTradesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradeReportID, False)
                self.register_field(SecondaryTradeReportID, False)

        self.register_group(NoTrades, NoTradesGroup, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)
        self.register_field(SettlDate, False)
        self.register_field(Quantity, False)
        self.register_field(QtyType, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(MarginExcess, False)
        self.register_field(TotalNetValue, False)
        self.register_field(CashOutstanding, False)

        class NoTrdRegTimestampsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TrdRegTimestamp, False)
                self.register_field(TrdRegTimestampType, False)
                self.register_field(TrdRegTimestampOrigin, False)

        self.register_group(NoTrdRegTimestamps, NoTrdRegTimestampsGroup, False)
        self.register_field(Side, False)

        class NoMiscFeesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(MiscFeeAmt, False)
                self.register_field(MiscFeeCurr, False)
                self.register_field(MiscFeeType, False)
                self.register_field(MiscFeeBasis, False)

        self.register_group(NoMiscFees, NoMiscFeesGroup, False)
        self.register_field(Price, False)
        self.register_field(PriceType, False)
        self.register_field(AccruedInterestAmt, False)
        self.register_field(EndAccruedInterestAmt, False)
        self.register_field(StartCash, False)
        self.register_field(EndCash, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(SettlDeliveryType, False)
        self.register_field(StandInstDbType, False)
        self.register_field(StandInstDbName, False)
        self.register_field(StandInstDbID, False)

        class NoDlvyInstGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SettlInstSource, False)
                self.register_field(DlvyInstType, False)

                class NoSettlPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SettlPartyID, False)
                        self.register_field(SettlPartyIDSource, False)
                        self.register_field(SettlPartyRole, False)

                        class NoSettlPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(SettlPartySubID, False)
                                self.register_field(SettlPartySubIDType, False)

                        self.register_group(NoSettlPartySubIDs, NoSettlPartySubIDsGroup, False)

                self.register_group(NoSettlPartyIDs, NoSettlPartyIDsGroup, False)

        self.register_group(NoDlvyInst, NoDlvyInstGroup, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(SettlSessID, False)
        self.register_field(SettlSessSubID, False)
        self.register_field(ClearingBusinessDate, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['BA'] = CollateralReport

class CollateralInquiry(fix_message.MessageBase):
    _msgtype = 'BB'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(CollInquiryID, False)

        class NoCollInquiryQualifierGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(CollInquiryQualifier, False)

        self.register_group(NoCollInquiryQualifier, NoCollInquiryQualifierGroup, False)
        self.register_field(SubscriptionRequestType, False)
        self.register_field(ResponseTransportType, False)
        self.register_field(ResponseDestination, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AccountType, False)
        self.register_field(ClOrdID, False)
        self.register_field(OrderID, False)
        self.register_field(SecondaryOrderID, False)
        self.register_field(SecondaryClOrdID, False)

        class NoExecsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ExecID, False)

        self.register_group(NoExecs, NoExecsGroup, False)

        class NoTradesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradeReportID, False)
                self.register_field(SecondaryTradeReportID, False)

        self.register_group(NoTrades, NoTradesGroup, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)
        self.register_field(SettlDate, False)
        self.register_field(Quantity, False)
        self.register_field(QtyType, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(MarginExcess, False)
        self.register_field(TotalNetValue, False)
        self.register_field(CashOutstanding, False)

        class NoTrdRegTimestampsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TrdRegTimestamp, False)
                self.register_field(TrdRegTimestampType, False)
                self.register_field(TrdRegTimestampOrigin, False)

        self.register_group(NoTrdRegTimestamps, NoTrdRegTimestampsGroup, False)
        self.register_field(Side, False)
        self.register_field(Price, False)
        self.register_field(PriceType, False)
        self.register_field(AccruedInterestAmt, False)
        self.register_field(EndAccruedInterestAmt, False)
        self.register_field(StartCash, False)
        self.register_field(EndCash, False)
        self.register_field(Spread, False)
        self.register_field(BenchmarkCurveCurrency, False)
        self.register_field(BenchmarkCurveName, False)
        self.register_field(BenchmarkCurvePoint, False)
        self.register_field(BenchmarkPrice, False)
        self.register_field(BenchmarkPriceType, False)
        self.register_field(BenchmarkSecurityID, False)
        self.register_field(BenchmarkSecurityIDSource, False)

        class NoStipulationsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(StipulationType, False)
                self.register_field(StipulationValue, False)

        self.register_group(NoStipulations, NoStipulationsGroup, False)
        self.register_field(SettlDeliveryType, False)
        self.register_field(StandInstDbType, False)
        self.register_field(StandInstDbName, False)
        self.register_field(StandInstDbID, False)

        class NoDlvyInstGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SettlInstSource, False)
                self.register_field(DlvyInstType, False)

                class NoSettlPartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(SettlPartyID, False)
                        self.register_field(SettlPartyIDSource, False)
                        self.register_field(SettlPartyRole, False)

                        class NoSettlPartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(SettlPartySubID, False)
                                self.register_field(SettlPartySubIDType, False)

                        self.register_group(NoSettlPartySubIDs, NoSettlPartySubIDsGroup, False)

                self.register_group(NoSettlPartyIDs, NoSettlPartyIDsGroup, False)

        self.register_group(NoDlvyInst, NoDlvyInstGroup, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(SettlSessID, False)
        self.register_field(SettlSessSubID, False)
        self.register_field(ClearingBusinessDate, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['BB'] = CollateralInquiry

class NetworkCounterpartySystemStatusRequest(fix_message.MessageBase):
    _msgtype = 'BC'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(NetworkRequestType, True)
        self.register_field(NetworkRequestID, True)

        class NoCompIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(RefCompID, False)
                self.register_field(RefSubID, False)
                self.register_field(LocationID, False)
                self.register_field(DeskID, False)

        self.register_group(NoCompIDs, NoCompIDsGroup, False)

MESSAGE_TYPES['BC'] = NetworkCounterpartySystemStatusRequest

class NetworkCounterpartySystemStatusResponse(fix_message.MessageBase):
    _msgtype = 'BD'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(NetworkStatusResponseType, True)
        self.register_field(NetworkRequestID, False)
        self.register_field(NetworkResponseID, True)
        self.register_field(LastNetworkResponseID, False)

        class NoCompIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(RefCompID, False)
                self.register_field(RefSubID, False)
                self.register_field(LocationID, False)
                self.register_field(DeskID, False)
                self.register_field(StatusValue, False)
                self.register_field(StatusText, False)

        self.register_group(NoCompIDs, NoCompIDsGroup, True)

MESSAGE_TYPES['BD'] = NetworkCounterpartySystemStatusResponse

class UserRequest(fix_message.MessageBase):
    _msgtype = 'BE'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(UserRequestID, True)
        self.register_field(UserRequestType, True)
        self.register_field(Username, True)
        self.register_field(Password, False)
        self.register_field(NewPassword, False)
        self.register_field(RawDataLength, False)
        self.register_field(RawData, False)

MESSAGE_TYPES['BE'] = UserRequest

class UserResponse(fix_message.MessageBase):
    _msgtype = 'BF'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(UserRequestID, True)
        self.register_field(Username, True)
        self.register_field(UserStatus, False)
        self.register_field(UserStatusText, False)

MESSAGE_TYPES['BF'] = UserResponse

class CollateralInquiryAck(fix_message.MessageBase):
    _msgtype = 'BG'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(CollInquiryID, True)
        self.register_field(CollInquiryStatus, True)
        self.register_field(CollInquiryResult, False)

        class NoCollInquiryQualifierGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(CollInquiryQualifier, False)

        self.register_group(NoCollInquiryQualifier, NoCollInquiryQualifierGroup, False)
        self.register_field(TotNumReports, False)

        class NoPartyIDsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(PartyID, False)
                self.register_field(PartyIDSource, False)
                self.register_field(PartyRole, False)

                class NoPartySubIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(PartySubID, False)
                        self.register_field(PartySubIDType, False)

                self.register_group(NoPartySubIDs, NoPartySubIDsGroup, False)

        self.register_group(NoPartyIDs, NoPartyIDsGroup, False)
        self.register_field(Account, False)
        self.register_field(AccountType, False)
        self.register_field(ClOrdID, False)
        self.register_field(OrderID, False)
        self.register_field(SecondaryOrderID, False)
        self.register_field(SecondaryClOrdID, False)

        class NoExecsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ExecID, False)

        self.register_group(NoExecs, NoExecsGroup, False)

        class NoTradesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradeReportID, False)
                self.register_field(SecondaryTradeReportID, False)

        self.register_group(NoTrades, NoTradesGroup, False)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(SecurityIDSource, False)

        class NoSecurityAltIDGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(SecurityAltID, False)
                self.register_field(SecurityAltIDSource, False)

        self.register_group(NoSecurityAltID, NoSecurityAltIDGroup, False)
        self.register_field(Product, False)
        self.register_field(CFICode, False)
        self.register_field(SecurityType, False)
        self.register_field(SecuritySubType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDate, False)
        self.register_field(PutOrCall, False)
        self.register_field(CouponPaymentDate, False)
        self.register_field(IssueDate, False)
        self.register_field(RepoCollateralSecurityType, False)
        self.register_field(RepurchaseTerm, False)
        self.register_field(RepurchaseRate, False)
        self.register_field(Factor, False)
        self.register_field(CreditRating, False)
        self.register_field(InstrRegistry, False)
        self.register_field(CountryOfIssue, False)
        self.register_field(StateOrProvinceOfIssue, False)
        self.register_field(LocaleOfIssue, False)
        self.register_field(RedemptionDate, False)
        self.register_field(StrikePrice, False)
        self.register_field(StrikeCurrency, False)
        self.register_field(OptAttribute, False)
        self.register_field(ContractMultiplier, False)
        self.register_field(CouponRate, False)
        self.register_field(SecurityExchange, False)
        self.register_field(Issuer, False)
        self.register_field(EncodedIssuerLen, False)
        self.register_field(EncodedIssuer, False)
        self.register_field(SecurityDesc, False)
        self.register_field(EncodedSecurityDescLen, False)
        self.register_field(EncodedSecurityDesc, False)
        self.register_field(Pool, False)
        self.register_field(ContractSettlMonth, False)
        self.register_field(CPProgram, False)
        self.register_field(CPRegType, False)

        class NoEventsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(EventType, False)
                self.register_field(EventDate, False)
                self.register_field(EventPx, False)
                self.register_field(EventText, False)

        self.register_group(NoEvents, NoEventsGroup, False)
        self.register_field(DatedDate, False)
        self.register_field(InterestAccrualDate, False)
        self.register_field(AgreementDesc, False)
        self.register_field(AgreementID, False)
        self.register_field(AgreementDate, False)
        self.register_field(AgreementCurrency, False)
        self.register_field(TerminationType, False)
        self.register_field(StartDate, False)
        self.register_field(EndDate, False)
        self.register_field(DeliveryType, False)
        self.register_field(MarginRatio, False)
        self.register_field(SettlDate, False)
        self.register_field(Quantity, False)
        self.register_field(QtyType, False)
        self.register_field(Currency, False)

        class NoLegsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(LegSymbol, False)
                self.register_field(LegSymbolSfx, False)
                self.register_field(LegSecurityID, False)
                self.register_field(LegSecurityIDSource, False)

                class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(LegSecurityAltID, False)
                        self.register_field(LegSecurityAltIDSource, False)

                self.register_group(NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
                self.register_field(LegProduct, False)
                self.register_field(LegCFICode, False)
                self.register_field(LegSecurityType, False)
                self.register_field(LegSecuritySubType, False)
                self.register_field(LegMaturityMonthYear, False)
                self.register_field(LegMaturityDate, False)
                self.register_field(LegCouponPaymentDate, False)
                self.register_field(LegIssueDate, False)
                self.register_field(LegRepoCollateralSecurityType, False)
                self.register_field(LegRepurchaseTerm, False)
                self.register_field(LegRepurchaseRate, False)
                self.register_field(LegFactor, False)
                self.register_field(LegCreditRating, False)
                self.register_field(LegInstrRegistry, False)
                self.register_field(LegCountryOfIssue, False)
                self.register_field(LegStateOrProvinceOfIssue, False)
                self.register_field(LegLocaleOfIssue, False)
                self.register_field(LegRedemptionDate, False)
                self.register_field(LegStrikePrice, False)
                self.register_field(LegStrikeCurrency, False)
                self.register_field(LegOptAttribute, False)
                self.register_field(LegContractMultiplier, False)
                self.register_field(LegCouponRate, False)
                self.register_field(LegSecurityExchange, False)
                self.register_field(LegIssuer, False)
                self.register_field(EncodedLegIssuerLen, False)
                self.register_field(EncodedLegIssuer, False)
                self.register_field(LegSecurityDesc, False)
                self.register_field(EncodedLegSecurityDescLen, False)
                self.register_field(EncodedLegSecurityDesc, False)
                self.register_field(LegRatioQty, False)
                self.register_field(LegSide, False)
                self.register_field(LegCurrency, False)
                self.register_field(LegPool, False)
                self.register_field(LegDatedDate, False)
                self.register_field(LegContractSettlMonth, False)
                self.register_field(LegInterestAccrualDate, False)

        self.register_group(NoLegs, NoLegsGroup, False)

        class NoUnderlyingsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(UnderlyingSymbol, False)
                self.register_field(UnderlyingSymbolSfx, False)
                self.register_field(UnderlyingSecurityID, False)
                self.register_field(UnderlyingSecurityIDSource, False)

                class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingSecurityAltID, False)
                        self.register_field(UnderlyingSecurityAltIDSource, False)

                self.register_group(NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
                self.register_field(UnderlyingProduct, False)
                self.register_field(UnderlyingCFICode, False)
                self.register_field(UnderlyingSecurityType, False)
                self.register_field(UnderlyingSecuritySubType, False)
                self.register_field(UnderlyingMaturityMonthYear, False)
                self.register_field(UnderlyingMaturityDate, False)
                self.register_field(UnderlyingPutOrCall, False)
                self.register_field(UnderlyingCouponPaymentDate, False)
                self.register_field(UnderlyingIssueDate, False)
                self.register_field(UnderlyingRepoCollateralSecurityType, False)
                self.register_field(UnderlyingRepurchaseTerm, False)
                self.register_field(UnderlyingRepurchaseRate, False)
                self.register_field(UnderlyingFactor, False)
                self.register_field(UnderlyingCreditRating, False)
                self.register_field(UnderlyingInstrRegistry, False)
                self.register_field(UnderlyingCountryOfIssue, False)
                self.register_field(UnderlyingStateOrProvinceOfIssue, False)
                self.register_field(UnderlyingLocaleOfIssue, False)
                self.register_field(UnderlyingRedemptionDate, False)
                self.register_field(UnderlyingStrikePrice, False)
                self.register_field(UnderlyingStrikeCurrency, False)
                self.register_field(UnderlyingOptAttribute, False)
                self.register_field(UnderlyingContractMultiplier, False)
                self.register_field(UnderlyingCouponRate, False)
                self.register_field(UnderlyingSecurityExchange, False)
                self.register_field(UnderlyingIssuer, False)
                self.register_field(EncodedUnderlyingIssuerLen, False)
                self.register_field(EncodedUnderlyingIssuer, False)
                self.register_field(UnderlyingSecurityDesc, False)
                self.register_field(EncodedUnderlyingSecurityDescLen, False)
                self.register_field(EncodedUnderlyingSecurityDesc, False)
                self.register_field(UnderlyingCPProgram, False)
                self.register_field(UnderlyingCPRegType, False)
                self.register_field(UnderlyingCurrency, False)
                self.register_field(UnderlyingQty, False)
                self.register_field(UnderlyingPx, False)
                self.register_field(UnderlyingDirtyPrice, False)
                self.register_field(UnderlyingEndPrice, False)
                self.register_field(UnderlyingStartValue, False)
                self.register_field(UnderlyingCurrentValue, False)
                self.register_field(UnderlyingEndValue, False)

                class NoUnderlyingStipsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(UnderlyingStipType, False)
                        self.register_field(UnderlyingStipValue, False)

                self.register_group(NoUnderlyingStips, NoUnderlyingStipsGroup, False)

        self.register_group(NoUnderlyings, NoUnderlyingsGroup, False)
        self.register_field(TradingSessionID, False)
        self.register_field(TradingSessionSubID, False)
        self.register_field(SettlSessID, False)
        self.register_field(SettlSessSubID, False)
        self.register_field(ClearingBusinessDate, False)
        self.register_field(ResponseTransportType, False)
        self.register_field(ResponseDestination, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['BG'] = CollateralInquiryAck

class ConfirmationRequest(fix_message.MessageBase):
    _msgtype = 'BH'
    _msgcat = 'app'
    def __init__(self):
        super().__init__()
        self.register_field(ConfirmReqID, True)
        self.register_field(ConfirmType, True)

        class NoOrdersGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(ClOrdID, False)
                self.register_field(OrderID, False)
                self.register_field(SecondaryOrderID, False)
                self.register_field(SecondaryClOrdID, False)
                self.register_field(ListID, False)

                class NoNested2PartyIDsGroup(fix_message.FIXGroup):
                    def __init__(self):
                        self.register_field(Nested2PartyID, False)
                        self.register_field(Nested2PartyIDSource, False)
                        self.register_field(Nested2PartyRole, False)

                        class NoNested2PartySubIDsGroup(fix_message.FIXGroup):
                            def __init__(self):
                                self.register_field(Nested2PartySubID, False)
                                self.register_field(Nested2PartySubIDType, False)

                        self.register_group(NoNested2PartySubIDs, NoNested2PartySubIDsGroup, False)

                self.register_group(NoNested2PartyIDs, NoNested2PartyIDsGroup, False)
                self.register_field(OrderQty, False)
                self.register_field(OrderAvgPx, False)
                self.register_field(OrderBookingQty, False)

        self.register_group(NoOrders, NoOrdersGroup, False)
        self.register_field(AllocID, False)
        self.register_field(SecondaryAllocID, False)
        self.register_field(IndividualAllocID, False)
        self.register_field(TransactTime, True)
        self.register_field(AllocAccount, False)
        self.register_field(AllocAcctIDSource, False)
        self.register_field(AllocAccountType, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['BH'] = ConfirmationRequest
