from . import field_types

class Account (field_types.char_Type) :
    _tag = '1'

class AdvId (field_types.char_Type) :
    _tag = '2'

class AdvRefID (field_types.char_Type) :
    _tag = '3'

class AdvSide (field_types.char_Type) :
    _tag = '4'
    ENUM_BUY = 'B'
    ENUM_SELL = 'S'
    ENUM_TRADE = 'T'
    ENUM_CROSS = 'X'

class AdvTransType (field_types.char_Type) :
    _tag = '5'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'

class AvgPx (field_types.float_Type) :
    _tag = '6'

class BeginSeqNo (field_types.int_Type) :
    _tag = '7'

class BeginString (field_types.char_Type) :
    _tag = '8'

class BodyLength (field_types.int_Type) :
    _tag = '9'

class CheckSum (field_types.char_Type) :
    _tag = '10'

class ClOrdID (field_types.char_Type) :
    _tag = '11'

class Commission (field_types.float_Type) :
    _tag = '12'

class CommType (field_types.char_Type) :
    _tag = '13'
    ENUM_PER_UNIT = '1'
    ENUM_PERCENT = '2'
    ENUM_ABSOLUTE = '3'

class CumQty (field_types.int_Type) :
    _tag = '14'

class Currency (field_types.char_Type) :
    _tag = '15'

class EndSeqNo (field_types.int_Type) :
    _tag = '16'

class ExecID (field_types.char_Type) :
    _tag = '17'

class ExecInst (field_types.char_Type) :
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
    ENUM_CUSTOMER_DISPLAY_INSTRUCTION = 'U'
    ENUM_NETTING = 'V'

class ExecRefID (field_types.char_Type) :
    _tag = '19'

class ExecTransType (field_types.char_Type) :
    _tag = '20'
    ENUM_NEW = '0'
    ENUM_CANCEL = '1'
    ENUM_CORRECT = '2'
    ENUM_STATUS = '3'

class HandlInst (field_types.char_Type) :
    _tag = '21'
    ENUM_AUTOMATED_EXECUTION_NO_INTERVENTION = '1'
    ENUM_AUTOMATED_EXECUTION_INTERVENTION_OK = '2'
    ENUM_MANUAL_ORDER = '3'

class IDSource (field_types.char_Type) :
    _tag = '22'
    ENUM_CUSIP = '1'
    ENUM_SEDOL = '2'
    ENUM_QUIK = '3'
    ENUM_ISIN_NUMBER = '4'
    ENUM_RIC_CODE = '5'
    ENUM_ISO_CURRENCY_CODE = '6'
    ENUM_ISO_COUNTRY_CODE = '7'

class IOIid (field_types.char_Type) :
    _tag = '23'

class IOIOthSvc (field_types.char_Type) :
    _tag = '24'
    ENUM_AUTEX = 'A'
    ENUM_BRIDGE = 'B'

class IOIQltyInd (field_types.char_Type) :
    _tag = '25'
    ENUM_HIGH = 'H'
    ENUM_LOW = 'L'
    ENUM_MEDIUM = 'M'

class IOIRefID (field_types.char_Type) :
    _tag = '26'

class IOIShares (field_types.char_Type) :
    _tag = '27'

class IOITransType (field_types.char_Type) :
    _tag = '28'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'

class LastCapacity (field_types.char_Type) :
    _tag = '29'
    ENUM_AGENT = '1'
    ENUM_CROSS_AS_AGENT = '2'
    ENUM_CROSS_AS_PRINCIPAL = '3'
    ENUM_PRINCIPAL = '4'

class LastMkt (field_types.char_Type) :
    _tag = '30'

class LastPx (field_types.float_Type) :
    _tag = '31'

class LastShares (field_types.int_Type) :
    _tag = '32'

class LinesOfText (field_types.int_Type) :
    _tag = '33'

class MsgSeqNum (field_types.int_Type) :
    _tag = '34'

class MsgType (field_types.char_Type) :
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

class NewSeqNo (field_types.int_Type) :
    _tag = '36'

class OrderID (field_types.char_Type) :
    _tag = '37'

class OrderQty (field_types.int_Type) :
    _tag = '38'

class OrdStatus (field_types.char_Type) :
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

class OrdType (field_types.char_Type) :
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
    ENUM_PEGGED = 'P'

class OrigClOrdID (field_types.char_Type) :
    _tag = '41'

class OrigTime (field_types.time_Type) :
    _tag = '42'

class PossDupFlag (field_types.char_Type) :
    _tag = '43'
    ENUM_ORIGINAL_TRANSMISSION = 'N'
    ENUM_POSSIBLE_DUPLICATE = 'Y'

class Price (field_types.float_Type) :
    _tag = '44'

class RefSeqNum (field_types.int_Type) :
    _tag = '45'

class RelatdSym (field_types.char_Type) :
    _tag = '46'

class Rule80A (field_types.char_Type) :
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

class SecurityID (field_types.char_Type) :
    _tag = '48'

class SenderCompID (field_types.char_Type) :
    _tag = '49'

class SenderSubID (field_types.char_Type) :
    _tag = '50'

class SendingTime (field_types.time_Type) :
    _tag = '52'

class Shares (field_types.int_Type) :
    _tag = '53'

class Side (field_types.char_Type) :
    _tag = '54'
    ENUM_BUY = '1'
    ENUM_SELL = '2'
    ENUM_BUY_MINUS = '3'
    ENUM_SELL_PLUS = '4'
    ENUM_SELL_SHORT = '5'
    ENUM_SELL_SHORT_EXEMPT = '6'
    ENUM_UNDISCLOSED = '7'
    ENUM_CROSS = '8'

class Symbol (field_types.char_Type) :
    _tag = '55'

class TargetCompID (field_types.char_Type) :
    _tag = '56'

class TargetSubID (field_types.char_Type) :
    _tag = '57'

class Text (field_types.char_Type) :
    _tag = '58'

class TimeInForce (field_types.char_Type) :
    _tag = '59'
    ENUM_DAY = '0'
    ENUM_GOOD_TILL_CANCEL = '1'
    ENUM_AT_THE_OPENING = '2'
    ENUM_IMMEDIATE_OR_CANCEL = '3'
    ENUM_FILL_OR_KILL = '4'
    ENUM_GOOD_TILL_CROSSING = '5'
    ENUM_GOOD_TILL_DATE = '6'

class TransactTime (field_types.time_Type) :
    _tag = '60'

class Urgency (field_types.char_Type) :
    _tag = '61'
    ENUM_NORMAL = '0'
    ENUM_FLASH = '1'
    ENUM_BACKGROUND = '2'

class ValidUntilTime (field_types.time_Type) :
    _tag = '62'

class SettlmntTyp (field_types.char_Type) :
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

class FutSettDate (field_types.date_Type) :
    _tag = '64'

class SymbolSfx (field_types.char_Type) :
    _tag = '65'

class ListID (field_types.char_Type) :
    _tag = '66'

class ListSeqNo (field_types.int_Type) :
    _tag = '67'

class ListNoOrds (field_types.int_Type) :
    _tag = '68'

class ListExecInst (field_types.char_Type) :
    _tag = '69'

class AllocID (field_types.char_Type) :
    _tag = '70'

class AllocTransType (field_types.char_Type) :
    _tag = '71'
    ENUM_NEW = '0'
    ENUM_REPLACE = '1'
    ENUM_CANCEL = '2'
    ENUM_PRELIMINARY = '3'
    ENUM_CALCULATED = '4'

class RefAllocID (field_types.char_Type) :
    _tag = '72'

class NoOrders (field_types.int_Type) :
    _tag = '73'

class AvgPrxPrecision (field_types.int_Type) :
    _tag = '74'

class TradeDate (field_types.date_Type) :
    _tag = '75'

class ExecBroker (field_types.char_Type) :
    _tag = '76'

class OpenClose (field_types.char_Type) :
    _tag = '77'
    ENUM_CLOSE = 'C'
    ENUM_OPEN = 'O'

class NoAllocs (field_types.int_Type) :
    _tag = '78'

class AllocAccount (field_types.char_Type) :
    _tag = '79'

class AllocShares (field_types.int_Type) :
    _tag = '80'

class ProcessCode (field_types.char_Type) :
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

class CxlQty (field_types.int_Type) :
    _tag = '84'

class AllocStatus (field_types.int_Type) :
    _tag = '87'
    ENUM_ACCEPTED = 0
    ENUM_BLOCK_LEVEL_REJECT = 1
    ENUM_ACCOUNT_LEVEL_REJECT = 2
    ENUM_RECEIVED = 3

class AllocRejCode (field_types.int_Type) :
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

class BrokerOfCredit (field_types.char_Type) :
    _tag = '92'

class SignatureLength (field_types.Length_Type) :
    _tag = '93'

class EmailType (field_types.char_Type) :
    _tag = '94'
    ENUM_NEW = '0'
    ENUM_REPLY = '1'
    ENUM_ADMIN_REPLY = '2'

class RawDataLength (field_types.Length_Type) :
    _tag = '95'

class RawData (field_types.data_Type) :
    _tag = '96'

class PossResend (field_types.char_Type) :
    _tag = '97'
    ENUM_ORIGINAL_TRANSMISSION = 'N'
    ENUM_POSSIBLE_RESEND = 'Y'

class EncryptMethod (field_types.int_Type) :
    _tag = '98'
    ENUM_NONE = 0
    ENUM_PKCS = 1
    ENUM_DES = 2
    ENUM_PKCSDES = 3
    ENUM_PGPDES = 4
    ENUM_PGPDESMD5 = 5
    ENUM_PEM = 6

class StopPx (field_types.float_Type) :
    _tag = '99'

class ExDestination (field_types.char_Type) :
    _tag = '100'

class CxlRejReason (field_types.int_Type) :
    _tag = '102'
    ENUM_TOO_LATE_TO_CANCEL = 0
    ENUM_UNKNOWN_ORDER = 1

class OrdRejReason (field_types.int_Type) :
    _tag = '103'
    ENUM_BROKER_CREDIT = 0
    ENUM_UNKNOWN_SYMBOL = 1
    ENUM_EXCHANGE_CLOSED = 2
    ENUM_ORDER_EXCEEDS_LIMIT = 3
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_UNKNOWN_ORDER = 5
    ENUM_DUPLICATE_ORDER = 6

class IOIQualifier (field_types.char_Type) :
    _tag = '104'
    ENUM_ALL_OR_NONE = 'A'
    ENUM_AT_THE_CLOSE = 'C'
    ENUM_IN_TOUCH_WITH = 'I'
    ENUM_LIMIT = 'L'
    ENUM_MORE_BEHIND = 'M'
    ENUM_AT_THE_OPEN = 'O'
    ENUM_TAKING_A_POSITION = 'P'
    ENUM_AT_THE_MARKET = 'Q'
    ENUM_PORTFOLIO_SHOWN = 'S'
    ENUM_THROUGH_THE_DAY = 'T'
    ENUM_VERSUS = 'V'
    ENUM_INDICATION = 'W'
    ENUM_CROSSING_OPPORTUNITY = 'X'
    ENUM_AT_THE_MIDPOINT = 'Y'
    ENUM_PRE_OPEN = 'Z'

class WaveNo (field_types.char_Type) :
    _tag = '105'

class Issuer (field_types.char_Type) :
    _tag = '106'

class SecurityDesc (field_types.char_Type) :
    _tag = '107'

class HeartBtInt (field_types.int_Type) :
    _tag = '108'

class ClientID (field_types.char_Type) :
    _tag = '109'

class MinQty (field_types.int_Type) :
    _tag = '110'

class MaxFloor (field_types.int_Type) :
    _tag = '111'

class TestReqID (field_types.char_Type) :
    _tag = '112'

class ReportToExch (field_types.char_Type) :
    _tag = '113'
    ENUM_SENDER_REPORTS = 'N'
    ENUM_RECEIVER_REPORTS = 'Y'

class LocateReqd (field_types.char_Type) :
    _tag = '114'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class OnBehalfOfCompID (field_types.char_Type) :
    _tag = '115'

class OnBehalfOfSubID (field_types.char_Type) :
    _tag = '116'

class QuoteID (field_types.char_Type) :
    _tag = '117'

class NetMoney (field_types.float_Type) :
    _tag = '118'

class SettlCurrAmt (field_types.float_Type) :
    _tag = '119'

class SettlCurrency (field_types.char_Type) :
    _tag = '120'

class ForexReq (field_types.char_Type) :
    _tag = '121'
    ENUM_DO_NOT_EXECUTE_FOREX_AFTER_SECURITY_TRADE = 'N'
    ENUM_EXECUTE_FOREX_AFTER_SECURITY_TRADE = 'Y'

class OrigSendingTime (field_types.time_Type) :
    _tag = '122'

class GapFillFlag (field_types.char_Type) :
    _tag = '123'
    ENUM_SEQUENCE_RESET = 'N'
    ENUM_GAP_FILL_MESSAGE = 'Y'

class NoExecs (field_types.int_Type) :
    _tag = '124'

class ExpireTime (field_types.time_Type) :
    _tag = '126'

class DKReason (field_types.char_Type) :
    _tag = '127'
    ENUM_UNKNOWN_SYMBOL = 'A'
    ENUM_WRONG_SIDE = 'B'
    ENUM_QUANTITY_EXCEEDS_ORDER = 'C'
    ENUM_NO_MATCHING_ORDER = 'D'
    ENUM_PRICE_EXCEEDS_LIMIT = 'E'
    ENUM_OTHER = 'Z'

class DeliverToCompID (field_types.char_Type) :
    _tag = '128'

class DeliverToSubID (field_types.char_Type) :
    _tag = '129'

class IOINaturalFlag (field_types.char_Type) :
    _tag = '130'
    ENUM_NOT_NATURAL = 'N'
    ENUM_NATURAL = 'Y'

class QuoteReqID (field_types.char_Type) :
    _tag = '131'

class BidPx (field_types.float_Type) :
    _tag = '132'

class OfferPx (field_types.float_Type) :
    _tag = '133'

class BidSize (field_types.int_Type) :
    _tag = '134'

class OfferSize (field_types.int_Type) :
    _tag = '135'

class NoMiscFees (field_types.int_Type) :
    _tag = '136'

class MiscFeeAmt (field_types.float_Type) :
    _tag = '137'

class MiscFeeCurr (field_types.char_Type) :
    _tag = '138'

class MiscFeeType (field_types.char_Type) :
    _tag = '139'
    ENUM_REGULATORY = '1'
    ENUM_TAX = '2'
    ENUM_LOCAL_COMMISSION = '3'
    ENUM_EXCHANGE_FEES = '4'
    ENUM_STAMP = '5'
    ENUM_LEVY = '6'
    ENUM_OTHER = '7'
    ENUM_MARKUP = '8'

class PrevClosePx (field_types.float_Type) :
    _tag = '140'

class ResetSeqNumFlag (field_types.char_Type) :
    _tag = '141'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class SenderLocationID (field_types.char_Type) :
    _tag = '142'

class TargetLocationID (field_types.char_Type) :
    _tag = '143'

class OnBehalfOfLocationID (field_types.char_Type) :
    _tag = '144'

class DeliverToLocationID (field_types.char_Type) :
    _tag = '145'

class NoRelatedSym (field_types.int_Type) :
    _tag = '146'

class Subject (field_types.char_Type) :
    _tag = '147'

class Headline (field_types.char_Type) :
    _tag = '148'

class URLLink (field_types.char_Type) :
    _tag = '149'

class ExecType (field_types.char_Type) :
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

class LeavesQty (field_types.int_Type) :
    _tag = '151'

class CashOrderQty (field_types.float_Type) :
    _tag = '152'

class AllocAvgPx (field_types.float_Type) :
    _tag = '153'

class AllocNetMoney (field_types.float_Type) :
    _tag = '154'

class SettlCurrFxRate (field_types.float_Type) :
    _tag = '155'

class SettlCurrFxRateCalc (field_types.char_Type) :
    _tag = '156'

class NumDaysInterest (field_types.int_Type) :
    _tag = '157'

class AccruedInterestRate (field_types.float_Type) :
    _tag = '158'

class AccruedInterestAmt (field_types.float_Type) :
    _tag = '159'

class SettlInstMode (field_types.char_Type) :
    _tag = '160'
    ENUM_DEFAULT = '0'
    ENUM_STANDING_INSTRUCTIONS_PROVIDED = '1'
    ENUM_SPECIFIC_ALLOCATION_ACCOUNT_OVERRIDING = '2'
    ENUM_SPECIFIC_ALLOCATION_ACCOUNT_STANDING = '3'

class AllocText (field_types.char_Type) :
    _tag = '161'

class SettlInstID (field_types.char_Type) :
    _tag = '162'

class SettlInstTransType (field_types.char_Type) :
    _tag = '163'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'

class EmailThreadID (field_types.char_Type) :
    _tag = '164'

class SettlInstSource (field_types.char_Type) :
    _tag = '165'
    ENUM_BROKER_CREDIT = '1'
    ENUM_INSTITUTION = '2'

class SettlLocation (field_types.char_Type) :
    _tag = '166'
    ENUM_CEDEL = 'CED'
    ENUM_DEPOSITORY_TRUST_COMPANY = 'DTC'
    ENUM_EURO_CLEAR = 'EUR'
    ENUM_FEDERAL_BOOK_ENTRY = 'FED'
    ENUM_LOCAL_MARKET_SETTLE_LOCATION = 'ISO Country Code'
    ENUM_PHYSICAL = 'PNY'
    ENUM_PARTICIPANT_TRUST_COMPANY = 'PTC'

class SecurityType (field_types.char_Type) :
    _tag = '167'
    ENUM_BANKERS_ACCEPTANCE = 'BA'
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

class EffectiveTime (field_types.time_Type) :
    _tag = '168'

class StandInstDbType (field_types.int_Type) :
    _tag = '169'
    ENUM_OTHER = 0
    ENUM_DTCSID = 1
    ENUM_THOMSON_ALERT = 2
    ENUM_A_GLOBAL_CUSTODIAN = 3

class StandInstDbName (field_types.char_Type) :
    _tag = '170'

class StandInstDbID (field_types.char_Type) :
    _tag = '171'

class SettlDeliveryType (field_types.int_Type) :
    _tag = '172'

class SettlDepositoryCode (field_types.char_Type) :
    _tag = '173'

class SettlBrkrCode (field_types.char_Type) :
    _tag = '174'

class SettlInstCode (field_types.char_Type) :
    _tag = '175'

class SecuritySettlAgentName (field_types.char_Type) :
    _tag = '176'

class SecuritySettlAgentCode (field_types.char_Type) :
    _tag = '177'

class SecuritySettlAgentAcctNum (field_types.char_Type) :
    _tag = '178'

class SecuritySettlAgentAcctName (field_types.char_Type) :
    _tag = '179'

class SecuritySettlAgentContactName (field_types.char_Type) :
    _tag = '180'

class SecuritySettlAgentContactPhone (field_types.char_Type) :
    _tag = '181'

class CashSettlAgentName (field_types.char_Type) :
    _tag = '182'

class CashSettlAgentCode (field_types.char_Type) :
    _tag = '183'

class CashSettlAgentAcctNum (field_types.char_Type) :
    _tag = '184'

class CashSettlAgentAcctName (field_types.char_Type) :
    _tag = '185'

class CashSettlAgentContactName (field_types.char_Type) :
    _tag = '186'

class CashSettlAgentContactPhone (field_types.char_Type) :
    _tag = '187'

class BidSpotRate (field_types.float_Type) :
    _tag = '188'

class BidForwardPoints (field_types.float_Type) :
    _tag = '189'

class OfferSpotRate (field_types.float_Type) :
    _tag = '190'

class OfferForwardPoints (field_types.float_Type) :
    _tag = '191'

class OrderQty2 (field_types.float_Type) :
    _tag = '192'

class FutSettDate2 (field_types.date_Type) :
    _tag = '193'

class LastSpotRate (field_types.float_Type) :
    _tag = '194'

class LastForwardPoints (field_types.float_Type) :
    _tag = '195'

class AllocLinkID (field_types.char_Type) :
    _tag = '196'

class AllocLinkType (field_types.int_Type) :
    _tag = '197'
    ENUM_FX_NETTING = 0
    ENUM_FX_SWAP = 1

class SecondaryOrderID (field_types.char_Type) :
    _tag = '198'

class NoIOIQualifiers (field_types.int_Type) :
    _tag = '199'

class MaturityMonthYear (field_types.MonthYear_Type) :
    _tag = '200'

class PutOrCall (field_types.int_Type) :
    _tag = '201'
    ENUM_PUT = 0
    ENUM_CALL = 1

class StrikePrice (field_types.float_Type) :
    _tag = '202'

class CoveredOrUncovered (field_types.int_Type) :
    _tag = '203'
    ENUM_COVERED = 0
    ENUM_UNCOVERED = 1

class CustomerOrFirm (field_types.int_Type) :
    _tag = '204'
    ENUM_CUSTOMER = 0
    ENUM_FIRM = 1

class MaturityDay (field_types.DayOfMonth_Type) :
    _tag = '205'

class OptAttribute (field_types.char_Type) :
    _tag = '206'

class SecurityExchange (field_types.char_Type) :
    _tag = '207'

class NotifyBrokerOfCredit (field_types.char_Type) :
    _tag = '208'
    ENUM_DETAILS_SHOULD_NOT_BE_COMMUNICATED = 'N'
    ENUM_DETAILS_SHOULD_BE_COMMUNICATED = 'Y'

class AllocHandlInst (field_types.int_Type) :
    _tag = '209'
    ENUM_MATCH = 1
    ENUM_FORWARD = 2
    ENUM_FORWARD_AND_MATCH = 3

class MaxShow (field_types.int_Type) :
    _tag = '210'

class PegDifference (field_types.float_Type) :
    _tag = '211'
