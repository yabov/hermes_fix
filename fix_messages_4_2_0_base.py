import fields
import fix_message

BEGINSTRING = 'FIX.4.2'
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
    ENUM_TRADE = 'T'
    ENUM_CROSS = 'X'

class AdvTransType (fields.String) :
    _tag = '5'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'

class AvgPx (fields.Price) :
    _tag = '6'

class BeginSeqNo (fields.int) :
    _tag = '7'

class BeginString (fields.String) :
    _tag = '8'

class BodyLength (fields.int) :
    _tag = '9'

class CheckSum (fields.String) :
    _tag = '10'

class ClOrdID (fields.String) :
    _tag = '11'

class Commission (fields.Amt) :
    _tag = '12'

class CommType (fields.char) :
    _tag = '13'
    ENUM_PER_SHARE = '1'
    ENUM_PERCENTAGE = '2'
    ENUM_ABSOLUTE = '3'

class CumQty (fields.Qty) :
    _tag = '14'

class Currency (fields.Currency) :
    _tag = '15'

class EndSeqNo (fields.int) :
    _tag = '16'

class ExecID (fields.String) :
    _tag = '17'

class ExecInst (fields.MultipleValueString) :
    _tag = '18'
    ENUM_STAY_ON_OFFERSIDE = '0'
    ENUM_NOT_HELD = '1'
    ENUM_WORK = '2'
    ENUM_GO_ALONG = '3'
    ENUM_OVER_THE_DAY = '4'
    ENUM_HELD = '5'
    ENUM_PARTICIPATE_DONT_INITIATE = '6'
    ENUM_STRICT_SCALE = '7'
    ENUM_TRY_TO_SCALE = '8'
    ENUM_STAY_ON_BIDSIDE = '9'
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

class ExecRefID (fields.String) :
    _tag = '19'

class ExecTransType (fields.char) :
    _tag = '20'
    ENUM_NEW = '0'
    ENUM_CANCEL = '1'
    ENUM_CORRECT = '2'
    ENUM_STATUS = '3'

class HandlInst (fields.char) :
    _tag = '21'
    ENUM_AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION = '1'
    ENUM_AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK = '2'
    ENUM_MANUAL_ORDER_BEST_EXECUTION = '3'

class IDSource (fields.String) :
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

class IOIid (fields.String) :
    _tag = '23'

class IOIOthSvc (fields.char) :
    _tag = '24'

class IOIQltyInd (fields.char) :
    _tag = '25'
    ENUM_HIGH = 'H'
    ENUM_LOW = 'L'
    ENUM_MEDIUM = 'M'

class IOIRefID (fields.String) :
    _tag = '26'

class IOIShares (fields.String) :
    _tag = '27'
    ENUM_LARGE = 'L'
    ENUM_MEDIUM = 'M'
    ENUM_SMALL = 'S'

class IOITransType (fields.char) :
    _tag = '28'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'
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

class LastShares (fields.Qty) :
    _tag = '32'

class LinesOfText (fields.int) :
    _tag = '33'

class MsgSeqNum (fields.int) :
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
    ENUM_QUOTE_STATUS_REQUEST = 'a'
    ENUM_LOGON = 'A'
    ENUM_NEWS = 'B'
    ENUM_QUOTE_ACKNOWLEDGEMENT = 'b'
    ENUM_EMAIL = 'C'
    ENUM_SECURITY_DEFINITION_REQUEST = 'c'
    ENUM_ORDER_SINGLE = 'D'
    ENUM_SECURITY_DEFINITION = 'd'
    ENUM_ORDER_LIST = 'E'
    ENUM_SECURITY_STATUS_REQUEST = 'e'
    ENUM_SECURITY_STATUS = 'f'
    ENUM_ORDER_CANCEL_REQUEST = 'F'
    ENUM_ORDER_CANCEL_REPLACE_REQUEST = 'G'
    ENUM_TRADING_SESSION_STATUS_REQUEST = 'g'
    ENUM_ORDER_STATUS_REQUEST = 'H'
    ENUM_TRADING_SESSION_STATUS = 'h'
    ENUM_MASS_QUOTE = 'i'
    ENUM_BUSINESS_MESSAGE_REJECT = 'j'
    ENUM_ALLOCATION = 'J'
    ENUM_LIST_CANCEL_REQUEST = 'K'
    ENUM_BID_REQUEST = 'k'
    ENUM_BID_RESPONSE = 'l'
    ENUM_LIST_EXECUTE = 'L'
    ENUM_LIST_STRIKE_PRICE = 'm'
    ENUM_LIST_STATUS_REQUEST = 'M'
    ENUM_LIST_STATUS = 'N'
    ENUM_ALLOCATION_ACK = 'P'
    ENUM_DONT_KNOW_TRADE = 'Q'
    ENUM_QUOTE_REQUEST = 'R'
    ENUM_QUOTE = 'S'
    ENUM_SETTLEMENT_INSTRUCTIONS = 'T'
    ENUM_MARKET_DATA_REQUEST = 'V'
    ENUM_MARKET_DATA_SNAPSHOT_FULL_REFRESH = 'W'
    ENUM_MARKET_DATA_INCREMENTAL_REFRESH = 'X'
    ENUM_MARKET_DATA_REQUEST_REJECT = 'Y'
    ENUM_QUOTE_CANCEL = 'Z'

class NewSeqNo (fields.int) :
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

class OrdType (fields.char) :
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
    ENUM_FOREX_C = 'C'
    ENUM_PREVIOUSLY_QUOTED = 'D'
    ENUM_PREVIOUSLY_INDICATED = 'E'
    ENUM_FOREX_F = 'F'
    ENUM_FOREX_G = 'G'
    ENUM_FOREX_H = 'H'
    ENUM_FUNARI = 'I'
    ENUM_PEGGED = 'P'

class OrigClOrdID (fields.String) :
    _tag = '41'

class OrigTime (fields.UTCTimestamp) :
    _tag = '42'

class PossDupFlag (fields.Boolean) :
    _tag = '43'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class Price (fields.Price) :
    _tag = '44'

class RefSeqNum (fields.int) :
    _tag = '45'

class RelatdSym (fields.String) :
    _tag = '46'

class Rule80A (fields.char) :
    _tag = '47'
    ENUM_AGENCY_SINGLE_ORDER = 'A'
    ENUM_SHORT_EXEMPT_TRANSACTION_B = 'B'
    ENUM_PROGRAM_ORDER_NON_INDEX_ARB_FOR_MEMBER_FIRM_ORG = 'C'
    ENUM_PROGRAM_ORDER_INDEX_ARB_FOR_MEMBER_FIRM_ORG = 'D'
    ENUM_REGISTERED_EQUITY_MARKET_MAKER_TRADES = 'E'
    ENUM_SHORT_EXEMPT_TRANSACTION_F = 'F'
    ENUM_SHORT_EXEMPT_TRANSACTION_H = 'H'
    ENUM_INDIVIDUAL_INVESTOR_SINGLE_ORDER = 'I'
    ENUM_PROGRAM_ORDER_INDEX_ARB_FOR_INDIVIDUAL_CUSTOMER = 'J'
    ENUM_PROGRAM_ORDER_NON_INDEX_ARB_FOR_INDIVIDUAL_CUSTOMER = 'K'
    ENUM_SHORT_EXEMPT_TRANSACTION_FOR_MEMBER_COMPETING_MARKET_MAKER_AFFILIATED_WITH_THE_FIRM_CLEARING_THE_TRADE = 'L'
    ENUM_PROGRAM_ORDER_INDEX_ARB_FOR_OTHER_MEMBER = 'M'
    ENUM_PROGRAM_ORDER_NON_INDEX_ARB_FOR_OTHER_MEMBER = 'N'
    ENUM_COMPETING_DEALER_TRADES_O = 'O'
    ENUM_PRINCIPAL = 'P'
    ENUM_COMPETING_DEALER_TRADES_R = 'R'
    ENUM_SPECIALIST_TRADES = 'S'
    ENUM_COMPETING_DEALER_TRADES_T = 'T'
    ENUM_PROGRAM_ORDER_INDEX_ARB_FOR_OTHER_AGENCY = 'U'
    ENUM_ALL_OTHER_ORDERS_AS_AGENT_FOR_OTHER_MEMBER = 'W'
    ENUM_SHORT_EXEMPT_TRANSACTION_FOR_MEMBER_COMPETING_MARKET_MAKER_NOT_AFFILIATED_WITH_THE_FIRM_CLEARING_THE_TRADE = 'X'
    ENUM_PROGRAM_ORDER_NON_INDEX_ARB_FOR_OTHER_AGENCY = 'Y'
    ENUM_SHORT_EXEMPT_TRANSACTION_FOR_NON_MEMBER_COMPETING_MARKET_MAKER = 'Z'

class SecurityID (fields.String) :
    _tag = '48'

class SenderCompID (fields.String) :
    _tag = '49'

class SenderSubID (fields.String) :
    _tag = '50'

class SendingDate (fields.LocalMktDate) :
    _tag = '51'

class SendingTime (fields.UTCTimestamp) :
    _tag = '52'

class Shares (fields.Qty) :
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

class TransactTime (fields.UTCTimestamp) :
    _tag = '60'

class Urgency (fields.char) :
    _tag = '61'
    ENUM_NORMAL = '0'
    ENUM_FLASH = '1'
    ENUM_BACKGROUND = '2'

class ValidUntilTime (fields.UTCTimestamp) :
    _tag = '62'

class SettlmntTyp (fields.char) :
    _tag = '63'
    ENUM_REGULAR = '0'
    ENUM_CASH = '1'
    ENUM_NEXT_DAY = '2'
    ENUM_T_PLUS_2 = '3'
    ENUM_T_PLUS_3 = '4'
    ENUM_T_PLUS_4 = '5'
    ENUM_FUTURE = '6'
    ENUM_WHEN_ISSUED = '7'
    ENUM_SELLERS_OPTION = '8'
    ENUM_T_PLUS_5 = '9'

class FutSettDate (fields.LocalMktDate) :
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
    ENUM_PRELIMINARY = '3'
    ENUM_CALCULATED = '4'
    ENUM_CALCULATED_WITHOUT_PRELIMINARY = '5'

class RefAllocID (fields.String) :
    _tag = '72'

class NoOrders (fields.int) :
    _tag = '73'

class AvgPrxPrecision (fields.int) :
    _tag = '74'

class TradeDate (fields.LocalMktDate) :
    _tag = '75'

class ExecBroker (fields.String) :
    _tag = '76'

class OpenClose (fields.char) :
    _tag = '77'
    ENUM_CLOSE = 'C'
    ENUM_OPEN = 'O'

class NoAllocs (fields.int) :
    _tag = '78'

class AllocAccount (fields.String) :
    _tag = '79'

class AllocShares (fields.Qty) :
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

class NoDlvyInst (fields.int) :
    _tag = '85'

class DlvyInst (fields.String) :
    _tag = '86'

class AllocStatus (fields.int) :
    _tag = '87'
    ENUM_ACCEPTED = 0
    ENUM_REJECTED = 1
    ENUM_PARTIAL_ACCEPT = 2
    ENUM_RECEIVED = 3

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

class Signature (fields.data) :
    _tag = '89'

class SecureDataLen (fields.Length) :
    _tag = '90'

class SecureData (fields.data) :
    _tag = '91'

class BrokerOfCredit (fields.String) :
    _tag = '92'

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
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

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
    ENUM_BROKER_OPTION = 2
    ENUM_ORDER_ALREADY_IN_PENDING_CANCEL_OR_PENDING_REPLACE_STATUS = 3

class OrdRejReason (fields.int) :
    _tag = '103'
    ENUM_BROKER_OPTION = 0
    ENUM_UNKNOWN_SYMBOL = 1
    ENUM_EXCHANGE_CLOSED = 2
    ENUM_ORDER_EXCEEDS_LIMIT = 3
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_UNKNOWN_ORDER = 5
    ENUM_DUPLICATE_ORDER = 6
    ENUM_DUPLICATE_OF_A_VERBALLY_COMMUNICATED_ORDER = 7
    ENUM_STALE_ORDER = 8

class IOIQualifier (fields.char) :
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
    ENUM_PORTFOLIO_SHOW_N = 'S'
    ENUM_THROUGH_THE_DAY = 'T'
    ENUM_VERSUS = 'V'
    ENUM_INDICATION = 'W'
    ENUM_CROSSING_OPPORTUNITY = 'X'
    ENUM_AT_THE_MIDPOINT = 'Y'
    ENUM_PRE_OPEN = 'Z'

class WaveNo (fields.String) :
    _tag = '105'

class Issuer (fields.String) :
    _tag = '106'

class SecurityDesc (fields.String) :
    _tag = '107'

class HeartBtInt (fields.int) :
    _tag = '108'

class ClientID (fields.String) :
    _tag = '109'

class MinQty (fields.Qty) :
    _tag = '110'

class MaxFloor (fields.Qty) :
    _tag = '111'

class TestReqID (fields.String) :
    _tag = '112'

class ReportToExch (fields.Boolean) :
    _tag = '113'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class LocateReqd (fields.Boolean) :
    _tag = '114'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

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
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class OrigSendingTime (fields.UTCTimestamp) :
    _tag = '122'

class GapFillFlag (fields.Boolean) :
    _tag = '123'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class NoExecs (fields.int) :
    _tag = '124'

class CxlType (fields.char) :
    _tag = '125'

class ExpireTime (fields.UTCTimestamp) :
    _tag = '126'

class DKReason (fields.char) :
    _tag = '127'
    ENUM_UNKNOWN_SYMBOL = 'A'
    ENUM_WRONG_SIDE = 'B'
    ENUM_QUANTITY_EXCEEDS_ORDER = 'C'
    ENUM_NO_MATCHING_ORDER = 'D'
    ENUM_PRICE_EXCEEDS_LIMIT = 'E'
    ENUM_OTHER = 'Z'

class DeliverToCompID (fields.String) :
    _tag = '128'

class DeliverToSubID (fields.String) :
    _tag = '129'

class IOINaturalFlag (fields.Boolean) :
    _tag = '130'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

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

class NoMiscFees (fields.int) :
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

class PrevClosePx (fields.Price) :
    _tag = '140'

class ResetSeqNumFlag (fields.Boolean) :
    _tag = '141'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class SenderLocationID (fields.String) :
    _tag = '142'

class TargetLocationID (fields.String) :
    _tag = '143'

class OnBehalfOfLocationID (fields.String) :
    _tag = '144'

class DeliverToLocationID (fields.String) :
    _tag = '145'

class NoRelatedSym (fields.int) :
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
    ENUM_PARTIAL_FILL = '1'
    ENUM_FILL = '2'
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

class AccruedInterestRate (fields.float) :
    _tag = '158'

class AccruedInterestAmt (fields.Amt) :
    _tag = '159'

class SettlInstMode (fields.char) :
    _tag = '160'
    ENUM_DEFAULT = '0'
    ENUM_STANDING_INSTRUCTIONS_PROVIDED = '1'
    ENUM_SPECIFIC_ALLOCATION_ACCOUNT_OVERRIDING = '2'
    ENUM_SPECIFIC_ALLOCATION_ACCOUNT_STANDING = '3'

class AllocText (fields.String) :
    _tag = '161'

class SettlInstID (fields.String) :
    _tag = '162'

class SettlInstTransType (fields.char) :
    _tag = '163'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'

class EmailThreadID (fields.String) :
    _tag = '164'

class SettlInstSource (fields.char) :
    _tag = '165'
    ENUM_BROKERS_INSTRUCTIONS = '1'
    ENUM_INSTITUTIONS_INSTRUCTIONS = '2'

class SettlLocation (fields.String) :
    _tag = '166'
    ENUM_CEDEL = 'CED'
    ENUM_DEPOSITORY_TRUST_COMPANY = 'DTC'
    ENUM_EUROCLEAR = 'EUR'
    ENUM_FEDERAL_BOOK_ENTRY = 'FED'
    ENUM_LOCAL_MARKET_SETTLE_LOCATION = 'ISO Country Code'
    ENUM_PHYSICAL = 'PNY'
    ENUM_PARTICIPANT_TRUST_COMPANY = 'PTC'

class SecurityType (fields.String) :
    _tag = '167'
    ENUM_WILDCARD_ENTRY = '?'
    ENUM_BANKERS_ACCEPTANCE = 'BA'
    ENUM_CONVERTIBLE_BOND = 'CB'
    ENUM_CERTIFICATE_OF_DEPOSIT = 'CD'
    ENUM_COLLATERALIZE_MORTGAGE_OBLIGATION = 'CMO'
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
    ENUM_TREASURIES_PLUS_AGENCY_DEBENTURE = 'GOVT'
    ENUM_MORTGAGE_IOETTE = 'IET'
    ENUM_MUTUAL_FUND = 'MF'
    ENUM_MORTGAGE_INTEREST_ONLY = 'MIO'
    ENUM_MORTGAGE_PRINCIPAL_ONLY = 'MPO'
    ENUM_MORTGAGE_PRIVATE_PLACEMENT = 'MPP'
    ENUM_MISCELLANEOUS_PASS_THRU = 'MPT'
    ENUM_MUNICIPAL_BOND = 'MUNI'
    ENUM_NO_ISITC_SECURITY_TYPE = 'NONE'
    ENUM_OPTION = 'OPT'
    ENUM_PREFERRED_STOCK = 'PS'
    ENUM_REPURCHASE_AGREEMENT = 'RP'
    ENUM_REVERSE_REPURCHASE_AGREEMENT = 'RVRP'
    ENUM_STUDENT_LOAN_MARKETING_ASSOCIATION = 'SL'
    ENUM_TIME_DEPOSIT = 'TD'
    ENUM_US_TREASURY_BILL = 'USTB'
    ENUM_WARRANT = 'WAR'
    ENUM_CATS_TIGERS_LIONS = 'ZOO'

class EffectiveTime (fields.UTCTimestamp) :
    _tag = '168'

class StandInstDbType (fields.int) :
    _tag = '169'
    ENUM_OTHER = 0
    ENUM_DTC_SID = 1
    ENUM_THOMSON_ALERT = 2
    ENUM_A_GLOBAL_CUSTODIAN = 3

class StandInstDbName (fields.String) :
    _tag = '170'

class StandInstDbID (fields.String) :
    _tag = '171'

class SettlDeliveryType (fields.int) :
    _tag = '172'

class SettlDepositoryCode (fields.String) :
    _tag = '173'

class SettlBrkrCode (fields.String) :
    _tag = '174'

class SettlInstCode (fields.String) :
    _tag = '175'

class SecuritySettlAgentName (fields.String) :
    _tag = '176'

class SecuritySettlAgentCode (fields.String) :
    _tag = '177'

class SecuritySettlAgentAcctNum (fields.String) :
    _tag = '178'

class SecuritySettlAgentAcctName (fields.String) :
    _tag = '179'

class SecuritySettlAgentContactName (fields.String) :
    _tag = '180'

class SecuritySettlAgentContactPhone (fields.String) :
    _tag = '181'

class CashSettlAgentName (fields.String) :
    _tag = '182'

class CashSettlAgentCode (fields.String) :
    _tag = '183'

class CashSettlAgentAcctNum (fields.String) :
    _tag = '184'

class CashSettlAgentAcctName (fields.String) :
    _tag = '185'

class CashSettlAgentContactName (fields.String) :
    _tag = '186'

class CashSettlAgentContactPhone (fields.String) :
    _tag = '187'

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

class FutSettDate2 (fields.LocalMktDate) :
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

class NoIOIQualifiers (fields.int) :
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

class CustomerOrFirm (fields.int) :
    _tag = '204'
    ENUM_CUSTOMER = 0
    ENUM_FIRM = 1

class MaturityDay (fields.DayOfMonth) :
    _tag = '205'

class OptAttribute (fields.char) :
    _tag = '206'

class SecurityExchange (fields.Exchange) :
    _tag = '207'

class NotifyBrokerOfCredit (fields.Boolean) :
    _tag = '208'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class AllocHandlInst (fields.int) :
    _tag = '209'
    ENUM_MATCH = 1
    ENUM_FORWARD = 2
    ENUM_FORWARD_AND_MATCH = 3

class MaxShow (fields.Qty) :
    _tag = '210'

class PegDifference (fields.PriceOffset) :
    _tag = '211'

class XmlDataLen (fields.Length) :
    _tag = '212'

class XmlData (fields.data) :
    _tag = '213'

class SettlInstRefID (fields.String) :
    _tag = '214'

class NoRoutingIDs (fields.int) :
    _tag = '215'

class RoutingType (fields.int) :
    _tag = '216'
    ENUM_TARGET_FIRM = 1
    ENUM_TARGET_LIST = 2
    ENUM_BLOCK_FIRM = 3
    ENUM_BLOCK_LIST = 4

class RoutingID (fields.String) :
    _tag = '217'

class SpreadToBenchmark (fields.PriceOffset) :
    _tag = '218'

class Benchmark (fields.char) :
    _tag = '219'
    ENUM_CURVE = '1'
    ENUM_5_YR = '2'
    ENUM_OLD_5 = '3'
    ENUM_10_YR = '4'
    ENUM_OLD_10 = '5'
    ENUM_30_YR = '6'
    ENUM_OLD_30 = '7'
    ENUM_3_MO_LIBOR = '8'
    ENUM_6_MO_LIBOR = '9'

class CouponRate (fields.float) :
    _tag = '223'

class ContractMultiplier (fields.float) :
    _tag = '231'

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
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class NoMDEntryTypes (fields.int) :
    _tag = '267'

class NoMDEntries (fields.int) :
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

class MDEntryPx (fields.Price) :
    _tag = '270'

class MDEntrySize (fields.Qty) :
    _tag = '271'

class MDEntryDate (fields.UTCDate) :
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

class OpenCloseSettleFlag (fields.char) :
    _tag = '286'
    ENUM_DAILY_OPEN = '0'
    ENUM_SESSION_OPEN = '1'
    ENUM_DELIVERY_SETTLEMENT_PRICE = '2'

class SellerDays (fields.int) :
    _tag = '287'

class MDEntryBuyer (fields.String) :
    _tag = '288'

class MDEntrySeller (fields.String) :
    _tag = '289'

class MDEntryPositionNo (fields.int) :
    _tag = '290'

class FinancialStatus (fields.char) :
    _tag = '291'
    ENUM_BANKRUPT = '1'

class CorporateAction (fields.char) :
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

class NoQuoteEntries (fields.int) :
    _tag = '295'

class NoQuoteSets (fields.int) :
    _tag = '296'

class QuoteAckStatus (fields.int) :
    _tag = '297'
    ENUM_ACCEPTED = 0
    ENUM_CANCELED_FOR_SYMBOL = 1
    ENUM_CANCELED_FOR_SECURITY_TYPE = 2
    ENUM_CANCELED_FOR_UNDERLYING = 3
    ENUM_CANCELED_ALL = 4
    ENUM_REJECTED = 5

class QuoteCancelType (fields.int) :
    _tag = '298'
    ENUM_CANCEL_FOR_SYMBOL = 1
    ENUM_CANCEL_FOR_SECURITY_TYPE = 2
    ENUM_CANCEL_FOR_UNDERLYING_SYMBOL = 3
    ENUM_CANCEL_FOR_ALL_QUOTES = 4

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

class TotQuoteEntries (fields.int) :
    _tag = '304'

class UnderlyingIDSource (fields.String) :
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

class UnderlyingMaturityDay (fields.DayOfMonth) :
    _tag = '314'

class UnderlyingPutOrCall (fields.int) :
    _tag = '315'

class UnderlyingStrikePrice (fields.Price) :
    _tag = '316'

class UnderlyingOptAttribute (fields.char) :
    _tag = '317'

class UnderlyingCurrency (fields.Currency) :
    _tag = '318'

class RatioQty (fields.Qty) :
    _tag = '319'

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
    ENUM_LIST_OF_SECURITY_TYPES_RETURNED_PER_REQUEST = 3
    ENUM_LIST_OF_SECURITIES_RETURNED_PER_REQUEST = 4
    ENUM_REJECT_SECURITY_PROPOSAL = 5
    ENUM_CAN_NOT_MATCH_SELECTION_CRITERIA = 6

class SecurityStatusReqID (fields.String) :
    _tag = '324'

class UnsolicitedIndicator (fields.Boolean) :
    _tag = '325'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class SecurityTradingStatus (fields.int) :
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
    ENUM_NO_OPEN_NO_RESUME = 4
    ENUM_PRICE_INDICATION = 5
    ENUM_TRADING_RANGE_INDICATION = 6
    ENUM_MARKET_IMBALANCE_BUY = 7
    ENUM_MARKET_IMBALANCE_SELL = 8
    ENUM_MARKET_ON_CLOSE_IMBALANCE_BUY = 9

class HaltReasonChar (fields.char) :
    _tag = '327'
    ENUM_NEWS_DISSEMINATION = 'D'
    ENUM_ORDER_INFLUX = 'E'
    ENUM_ORDER_IMBALANCE = 'I'
    ENUM_ADDITIONAL_INFORMATION = 'M'
    ENUM_NEWS_PENDING = 'P'
    ENUM_EQUIPMENT_CHANGEOVER = 'X'

class InViewOfCommon (fields.Boolean) :
    _tag = '328'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class DueToRelated (fields.Boolean) :
    _tag = '329'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

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
    ENUM_HALTED = 1
    ENUM_OPEN = 2
    ENUM_CLOSED = 3
    ENUM_PRE_OPEN = 4
    ENUM_PRE_CLOSE = 5

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
    ENUM_EUC_JP = 'EUC-JP'
    ENUM_ISO_2022_JP = 'ISO-2022-JP'
    ENUM_SHIFT_JIS = 'SHIFT_JIS'
    ENUM_UTF_8 = 'UTF-8'

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
    ENUM_UNKNOWN_SYMBOL = 1
    ENUM_EXCHANGE = 2
    ENUM_QUOTE_EXCEEDS_LIMIT = 3
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_UNKNOWN_QUOTE = 5
    ENUM_DUPLICATE_QUOTE = 6
    ENUM_INVALID_BID_ASK_SPREAD = 7
    ENUM_INVALID_PRICE = 8
    ENUM_NOT_AUTHORIZED_TO_QUOTE_SECURITY = 9

class LastMsgSeqNumProcessed (fields.int) :
    _tag = '369'

class OnBehalfOfSendingTime (fields.UTCTimestamp) :
    _tag = '370'

class RefTagID (fields.int) :
    _tag = '371'

class RefMsgType (fields.String) :
    _tag = '372'

class SessionRejectReason (fields.int) :
    _tag = '373'
    ENUM_INVALID_TAG_NUMBER = 0
    ENUM_REQUIRED_TAG_MISSING = 1
    ENUM_SENDINGTIME_ACCURACY_PROBLEM = 10
    ENUM_INVALID_MSGTYPE = 11
    ENUM_TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE = 2
    ENUM_UNDEFINED_TAG = 3
    ENUM_TAG_SPECIFIED_WITHOUT_A_VALUE = 4
    ENUM_VALUE_IS_INCORRECT = 5
    ENUM_INCORRECT_DATA_FORMAT_FOR_VALUE = 6
    ENUM_DECRYPTION_PROBLEM = 7
    ENUM_SIGNATURE_PROBLEM = 8
    ENUM_COMPID_PROBLEM = 9

class BidRequestTransType (fields.char) :
    _tag = '374'
    ENUM_CANCEL = 'C'
    ENUM_NO = 'N'

class ContraBroker (fields.String) :
    _tag = '375'

class ComplianceID (fields.String) :
    _tag = '376'

class SolicitedFlag (fields.Boolean) :
    _tag = '377'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class ExecRestatementReason (fields.int) :
    _tag = '378'
    ENUM_GT_CORPORATE_ACTION = 0
    ENUM_GT_RENEWAL = 1
    ENUM_VERBAL_CHANGE = 2
    ENUM_REPRICING_OF_ORDER = 3
    ENUM_BROKER_OPTION = 4
    ENUM_PARTIAL_DECLINE_OF_ORDERQTY = 5

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

class GrossTradeAmt (fields.Amt) :
    _tag = '381'

class NoContraBrokers (fields.int) :
    _tag = '382'

class MaxMessageSize (fields.int) :
    _tag = '383'

class NoMsgTypes (fields.int) :
    _tag = '384'

class MsgDirection (fields.char) :
    _tag = '385'
    ENUM_RECEIVE = 'R'
    ENUM_SEND = 'S'

class NoTradingSessions (fields.int) :
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

class DiscretionOffset (fields.PriceOffset) :
    _tag = '389'

class BidID (fields.String) :
    _tag = '390'

class ClientBidID (fields.String) :
    _tag = '391'

class ListName (fields.String) :
    _tag = '392'

class TotalNumSecurities (fields.int) :
    _tag = '393'

class BidType (fields.int) :
    _tag = '394'

class NumTickets (fields.int) :
    _tag = '395'

class SideValue1 (fields.Amt) :
    _tag = '396'

class SideValue2 (fields.Amt) :
    _tag = '397'

class NoBidDescriptors (fields.int) :
    _tag = '398'

class BidDescriptorType (fields.int) :
    _tag = '399'

class BidDescriptor (fields.String) :
    _tag = '400'

class SideValueInd (fields.int) :
    _tag = '401'

class LiquidityPctLow (fields.float) :
    _tag = '402'

class LiquidityPctHigh (fields.float) :
    _tag = '403'

class LiquidityValue (fields.Amt) :
    _tag = '404'

class EFPTrackingError (fields.float) :
    _tag = '405'

class FairValue (fields.Amt) :
    _tag = '406'

class OutsideIndexPct (fields.float) :
    _tag = '407'

class ValueOfFutures (fields.Amt) :
    _tag = '408'

class LiquidityIndType (fields.int) :
    _tag = '409'
    ENUM_5_DAY_MOVING_AVERAGE = 1
    ENUM_20_DAY_MOVING_AVERAGE = 2
    ENUM_NORMAL_MARKET_SIZE = 3
    ENUM_OTHER = 4

class WtAverageLiquidity (fields.float) :
    _tag = '410'

class ExchangeForPhysical (fields.Boolean) :
    _tag = '411'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class OutMainCntryUIndex (fields.Amt) :
    _tag = '412'

class CrossPercent (fields.float) :
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

class TradeType (fields.char) :
    _tag = '418'
    ENUM_AGENCY = 'A'
    ENUM_VWAP_GUARANTEE = 'G'
    ENUM_GUARANTEED_CLOSE = 'J'
    ENUM_RISK_TRADE = 'R'

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

class NoBidComponents (fields.int) :
    _tag = '420'

class Country (fields.String) :
    _tag = '421'

class TotNoStrikes (fields.int) :
    _tag = '422'

class PriceType (fields.int) :
    _tag = '423'
    ENUM_PERCENTAGE = 1
    ENUM_PER_SHARE = 2
    ENUM_FIXED_AMOUNT = 3

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

class NoStrikes (fields.int) :
    _tag = '428'

class ListStatusType (fields.int) :
    _tag = '429'

class NetGrossInd (fields.int) :
    _tag = '430'
    ENUM_NET = 1
    ENUM_GROSS = 2

class ListOrderStatus (fields.int) :
    _tag = '431'

class ExpireDate (fields.LocalMktDate) :
    _tag = '432'

class ListExecInstType (fields.char) :
    _tag = '433'
    ENUM_IMMEDIATE = '1'
    ENUM_WAIT_FOR_EXECUTE_INSTRUCTION = '2'

class CxlRejResponseTo (fields.char) :
    _tag = '434'
    ENUM_ORDER_CANCEL_REQUEST = '1'
    ENUM_ORDER_CANCEL_REPLACE_REQUEST = '2'

class UnderlyingCouponRate (fields.float) :
    _tag = '435'

class UnderlyingContractMultiplier (fields.float) :
    _tag = '436'

class ContraTradeQty (fields.Qty) :
    _tag = '437'

class ContraTradeTime (fields.UTCTimestamp) :
    _tag = '438'

class ClearingFirm (fields.String) :
    _tag = '439'

class ClearingAccount (fields.String) :
    _tag = '440'

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
        self.register_field(OnBehalfOfSendingTime, False)

class Heartbeat(fix_message.MessageBase):
    _msgtype = '0'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(TestReqID, False)

MESSAGE_TYPES['0'] = Heartbeat

class TestRequest(fix_message.MessageBase):
    _msgtype = '1'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(TestReqID, True)

MESSAGE_TYPES['1'] = TestRequest

class ResendRequest(fix_message.MessageBase):
    _msgtype = '2'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(BeginSeqNo, True)
        self.register_field(EndSeqNo, True)

MESSAGE_TYPES['2'] = ResendRequest

class Reject(fix_message.MessageBase):
    _msgtype = '3'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
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
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(GapFillFlag, False)
        self.register_field(NewSeqNo, True)

MESSAGE_TYPES['4'] = SequenceReset

class Logout(fix_message.MessageBase):
    _msgtype = '5'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['5'] = Logout

class IOI(fix_message.MessageBase):
    _msgtype = '6'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(IOIid, True)
        self.register_field(IOITransType, True)
        self.register_field(IOIRefID, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Side, True)
        self.register_field(IOIShares, True)
        self.register_field(Price, False)
        self.register_field(Currency, False)
        self.register_field(ValidUntilTime, False)
        self.register_field(IOIQltyInd, False)
        self.register_field(IOINaturalFlag, False)

        self.register_group(NoIOIQualifiers, IOI.NoIOIQualifiersGroup, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(TransactTime, False)
        self.register_field(URLLink, False)

        self.register_group(NoRoutingIDs, IOI.NoRoutingIDsGroup, False)
        self.register_field(SpreadToBenchmark, False)
        self.register_field(Benchmark, False)

    class NoIOIQualifiersGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(IOIQualifier, False)

    class NoRoutingIDsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(RoutingType, False)
            self.register_field(RoutingID, False)

MESSAGE_TYPES['6'] = IOI

class Advertisement(fix_message.MessageBase):
    _msgtype = '7'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(AdvId, True)
        self.register_field(AdvTransType, True)
        self.register_field(AdvRefID, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(AdvSide, True)
        self.register_field(Shares, True)
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

MESSAGE_TYPES['7'] = Advertisement

class ExecutionReport(fix_message.MessageBase):
    _msgtype = '8'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(OrderID, True)
        self.register_field(SecondaryOrderID, False)
        self.register_field(ClOrdID, False)
        self.register_field(OrigClOrdID, False)
        self.register_field(ClientID, False)
        self.register_field(ExecBroker, False)

        self.register_group(NoContraBrokers, ExecutionReport.NoContraBrokersGroup, False)
        self.register_field(ListID, False)
        self.register_field(ExecID, True)
        self.register_field(ExecTransType, True)
        self.register_field(ExecRefID, False)
        self.register_field(ExecType, True)
        self.register_field(OrdStatus, True)
        self.register_field(OrdRejReason, False)
        self.register_field(ExecRestatementReason, False)
        self.register_field(Account, False)
        self.register_field(SettlmntTyp, False)
        self.register_field(FutSettDate, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Side, True)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrdType, False)
        self.register_field(Price, False)
        self.register_field(StopPx, False)
        self.register_field(PegDifference, False)
        self.register_field(DiscretionInst, False)
        self.register_field(DiscretionOffset, False)
        self.register_field(Currency, False)
        self.register_field(ComplianceID, False)
        self.register_field(SolicitedFlag, False)
        self.register_field(TimeInForce, False)
        self.register_field(EffectiveTime, False)
        self.register_field(ExpireDate, False)
        self.register_field(ExpireTime, False)
        self.register_field(ExecInst, False)
        self.register_field(Rule80A, False)
        self.register_field(LastShares, False)
        self.register_field(LastPx, False)
        self.register_field(LastSpotRate, False)
        self.register_field(LastForwardPoints, False)
        self.register_field(LastMkt, False)
        self.register_field(TradingSessionID, False)
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
        self.register_field(GrossTradeAmt, False)
        self.register_field(SettlCurrAmt, False)
        self.register_field(SettlCurrency, False)
        self.register_field(SettlCurrFxRate, False)
        self.register_field(SettlCurrFxRateCalc, False)
        self.register_field(HandlInst, False)
        self.register_field(MinQty, False)
        self.register_field(MaxFloor, False)
        self.register_field(OpenClose, False)
        self.register_field(MaxShow, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(FutSettDate2, False)
        self.register_field(OrderQty2, False)
        self.register_field(ClearingFirm, False)
        self.register_field(ClearingAccount, False)
        self.register_field(MultiLegReportingType, False)

    class NoContraBrokersGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(ContraBroker, False)
            self.register_field(ContraTrader, False)
            self.register_field(ContraTradeQty, False)
            self.register_field(ContraTradeTime, False)

MESSAGE_TYPES['8'] = ExecutionReport

class OrderCancelReject(fix_message.MessageBase):
    _msgtype = '9'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(OrderID, True)
        self.register_field(SecondaryOrderID, False)
        self.register_field(ClOrdID, True)
        self.register_field(OrigClOrdID, True)
        self.register_field(OrdStatus, True)
        self.register_field(ClientID, False)
        self.register_field(ExecBroker, False)
        self.register_field(ListID, False)
        self.register_field(Account, False)
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
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(EncryptMethod, True)
        self.register_field(HeartBtInt, True)
        self.register_field(RawDataLength, False)
        self.register_field(RawData, False)
        self.register_field(ResetSeqNumFlag, False)
        self.register_field(MaxMessageSize, False)

        self.register_group(NoMsgTypes, Logon.NoMsgTypesGroup, False)

    class NoMsgTypesGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(RefMsgType, False)
            self.register_field(MsgDirection, False)

MESSAGE_TYPES['A'] = Logon

class News(fix_message.MessageBase):
    _msgtype = 'B'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(OrigTime, False)
        self.register_field(Urgency, False)
        self.register_field(Headline, True)
        self.register_field(EncodedHeadlineLen, False)
        self.register_field(EncodedHeadline, False)

        self.register_group(NoRoutingIDs, News.NoRoutingIDsGroup, False)

        self.register_group(NoRelatedSym, News.NoRelatedSymGroup, False)

        self.register_group(LinesOfText, News.LinesOfTextGroup, True)
        self.register_field(URLLink, False)
        self.register_field(RawDataLength, False)
        self.register_field(RawData, False)

    class NoRoutingIDsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(RoutingType, False)
            self.register_field(RoutingID, False)

    class NoRelatedSymGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(RelatdSym, False)
            self.register_field(SymbolSfx, False)
            self.register_field(SecurityID, False)
            self.register_field(IDSource, False)
            self.register_field(SecurityType, False)
            self.register_field(MaturityMonthYear, False)
            self.register_field(MaturityDay, False)
            self.register_field(PutOrCall, False)
            self.register_field(StrikePrice, False)
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

    class LinesOfTextGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(Text, True)
            self.register_field(EncodedTextLen, False)
            self.register_field(EncodedText, False)

MESSAGE_TYPES['B'] = News

class Email(fix_message.MessageBase):
    _msgtype = 'C'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(EmailThreadID, True)
        self.register_field(EmailType, True)
        self.register_field(OrigTime, False)
        self.register_field(Subject, True)
        self.register_field(EncodedSubjectLen, False)
        self.register_field(EncodedSubject, False)

        self.register_group(NoRoutingIDs, Email.NoRoutingIDsGroup, False)

        self.register_group(NoRelatedSym, Email.NoRelatedSymGroup, False)
        self.register_field(OrderID, False)
        self.register_field(ClOrdID, False)

        self.register_group(LinesOfText, Email.LinesOfTextGroup, True)
        self.register_field(RawDataLength, False)
        self.register_field(RawData, False)

    class NoRoutingIDsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(RoutingType, False)
            self.register_field(RoutingID, False)

    class NoRelatedSymGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(RelatdSym, False)
            self.register_field(SymbolSfx, False)
            self.register_field(SecurityID, False)
            self.register_field(IDSource, False)
            self.register_field(SecurityType, False)
            self.register_field(MaturityMonthYear, False)
            self.register_field(MaturityDay, False)
            self.register_field(PutOrCall, False)
            self.register_field(StrikePrice, False)
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

    class LinesOfTextGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(Text, True)
            self.register_field(EncodedTextLen, False)
            self.register_field(EncodedText, False)

MESSAGE_TYPES['C'] = Email

class NewOrderSingle(fix_message.MessageBase):
    _msgtype = 'D'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(ClOrdID, True)
        self.register_field(ClientID, False)
        self.register_field(ExecBroker, False)
        self.register_field(Account, False)

        self.register_group(NoAllocs, NewOrderSingle.NoAllocsGroup, False)
        self.register_field(SettlmntTyp, False)
        self.register_field(FutSettDate, False)
        self.register_field(HandlInst, True)
        self.register_field(ExecInst, False)
        self.register_field(MinQty, False)
        self.register_field(MaxFloor, False)
        self.register_field(ExDestination, False)

        self.register_group(NoTradingSessions, NewOrderSingle.NoTradingSessionsGroup, False)
        self.register_field(ProcessCode, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(PrevClosePx, False)
        self.register_field(Side, True)
        self.register_field(LocateReqd, False)
        self.register_field(TransactTime, True)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrdType, True)
        self.register_field(Price, False)
        self.register_field(StopPx, False)
        self.register_field(Currency, False)
        self.register_field(ComplianceID, False)
        self.register_field(SolicitedFlag, False)
        self.register_field(IOIid, False)
        self.register_field(QuoteID, False)
        self.register_field(TimeInForce, False)
        self.register_field(EffectiveTime, False)
        self.register_field(ExpireDate, False)
        self.register_field(ExpireTime, False)
        self.register_field(GTBookingInst, False)
        self.register_field(Commission, False)
        self.register_field(CommType, False)
        self.register_field(Rule80A, False)
        self.register_field(ForexReq, False)
        self.register_field(SettlCurrency, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(FutSettDate2, False)
        self.register_field(OrderQty2, False)
        self.register_field(OpenClose, False)
        self.register_field(CoveredOrUncovered, False)
        self.register_field(CustomerOrFirm, False)
        self.register_field(MaxShow, False)
        self.register_field(PegDifference, False)
        self.register_field(DiscretionInst, False)
        self.register_field(DiscretionOffset, False)
        self.register_field(ClearingFirm, False)
        self.register_field(ClearingAccount, False)

    class NoAllocsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(AllocAccount, False)
            self.register_field(AllocShares, False)

    class NoTradingSessionsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(TradingSessionID, False)

MESSAGE_TYPES['D'] = NewOrderSingle

class NewOrderList(fix_message.MessageBase):
    _msgtype = 'E'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(ListID, True)
        self.register_field(BidID, False)
        self.register_field(ClientBidID, False)
        self.register_field(ProgRptReqs, False)
        self.register_field(BidType, True)
        self.register_field(ProgPeriodInterval, False)
        self.register_field(ListExecInstType, False)
        self.register_field(ListExecInst, False)
        self.register_field(EncodedListExecInstLen, False)
        self.register_field(EncodedListExecInst, False)
        self.register_field(TotNoOrders, True)

        self.register_group(NoOrders, NewOrderList.NoOrdersGroup, True)

    class NoOrdersGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(ClOrdID, True)
            self.register_field(ListSeqNo, True)
            self.register_field(SettlInstMode, False)
            self.register_field(ClientID, False)
            self.register_field(ExecBroker, False)
            self.register_field(Account, False)

            self.register_group(NoAllocs, NewOrderList.NoOrdersGroup.NoAllocsGroup, False)
            self.register_field(SettlmntTyp, False)
            self.register_field(FutSettDate, False)
            self.register_field(HandlInst, False)
            self.register_field(ExecInst, False)
            self.register_field(MinQty, False)
            self.register_field(MaxFloor, False)
            self.register_field(ExDestination, False)

            self.register_group(NoTradingSessions, NewOrderList.NoOrdersGroup.NoTradingSessionsGroup, False)
            self.register_field(ProcessCode, False)
            self.register_field(Symbol, True)
            self.register_field(SymbolSfx, False)
            self.register_field(SecurityID, False)
            self.register_field(IDSource, False)
            self.register_field(SecurityType, False)
            self.register_field(MaturityMonthYear, False)
            self.register_field(MaturityDay, False)
            self.register_field(PutOrCall, False)
            self.register_field(StrikePrice, False)
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
            self.register_field(PrevClosePx, False)
            self.register_field(Side, True)
            self.register_field(SideValueInd, False)
            self.register_field(LocateReqd, False)
            self.register_field(TransactTime, False)
            self.register_field(OrderQty, False)
            self.register_field(CashOrderQty, False)
            self.register_field(OrdType, False)
            self.register_field(Price, False)
            self.register_field(StopPx, False)
            self.register_field(Currency, False)
            self.register_field(ComplianceID, False)
            self.register_field(SolicitedFlag, False)
            self.register_field(IOIid, False)
            self.register_field(QuoteID, False)
            self.register_field(TimeInForce, False)
            self.register_field(EffectiveTime, False)
            self.register_field(ExpireDate, False)
            self.register_field(ExpireTime, False)
            self.register_field(GTBookingInst, False)
            self.register_field(Commission, False)
            self.register_field(CommType, False)
            self.register_field(Rule80A, False)
            self.register_field(ForexReq, False)
            self.register_field(SettlCurrency, False)
            self.register_field(Text, False)
            self.register_field(EncodedTextLen, False)
            self.register_field(EncodedText, False)
            self.register_field(FutSettDate2, False)
            self.register_field(OrderQty2, False)
            self.register_field(OpenClose, False)
            self.register_field(CoveredOrUncovered, False)
            self.register_field(CustomerOrFirm, False)
            self.register_field(MaxShow, False)
            self.register_field(PegDifference, False)
            self.register_field(DiscretionInst, False)
            self.register_field(DiscretionOffset, False)
            self.register_field(ClearingFirm, False)
            self.register_field(ClearingAccount, False)

        class NoAllocsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(AllocAccount, False)
                self.register_field(AllocShares, False)

        class NoTradingSessionsGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(TradingSessionID, False)

MESSAGE_TYPES['E'] = NewOrderList

class OrderCancelRequest(fix_message.MessageBase):
    _msgtype = 'F'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(OrigClOrdID, True)
        self.register_field(OrderID, False)
        self.register_field(ClOrdID, True)
        self.register_field(ListID, False)
        self.register_field(Account, False)
        self.register_field(ClientID, False)
        self.register_field(ExecBroker, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Side, True)
        self.register_field(TransactTime, True)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(ComplianceID, False)
        self.register_field(SolicitedFlag, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['F'] = OrderCancelRequest

class OrderCancelReplaceRequest(fix_message.MessageBase):
    _msgtype = 'G'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(OrderID, False)
        self.register_field(ClientID, False)
        self.register_field(ExecBroker, False)
        self.register_field(OrigClOrdID, True)
        self.register_field(ClOrdID, True)
        self.register_field(ListID, False)
        self.register_field(Account, False)

        self.register_group(NoAllocs, OrderCancelReplaceRequest.NoAllocsGroup, False)
        self.register_field(SettlmntTyp, False)
        self.register_field(FutSettDate, False)
        self.register_field(HandlInst, True)
        self.register_field(ExecInst, False)
        self.register_field(MinQty, False)
        self.register_field(MaxFloor, False)
        self.register_field(ExDestination, False)

        self.register_group(NoTradingSessions, OrderCancelReplaceRequest.NoTradingSessionsGroup, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Side, True)
        self.register_field(TransactTime, True)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(OrdType, True)
        self.register_field(Price, False)
        self.register_field(StopPx, False)
        self.register_field(PegDifference, False)
        self.register_field(DiscretionInst, False)
        self.register_field(DiscretionOffset, False)
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
        self.register_field(Rule80A, False)
        self.register_field(ForexReq, False)
        self.register_field(SettlCurrency, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(FutSettDate2, False)
        self.register_field(OrderQty2, False)
        self.register_field(OpenClose, False)
        self.register_field(CoveredOrUncovered, False)
        self.register_field(CustomerOrFirm, False)
        self.register_field(MaxShow, False)
        self.register_field(LocateReqd, False)
        self.register_field(ClearingFirm, False)
        self.register_field(ClearingAccount, False)

    class NoAllocsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(AllocAccount, False)
            self.register_field(AllocShares, False)

    class NoTradingSessionsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(TradingSessionID, False)

MESSAGE_TYPES['G'] = OrderCancelReplaceRequest

class OrderStatusRequest(fix_message.MessageBase):
    _msgtype = 'H'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(OrderID, False)
        self.register_field(ClOrdID, True)
        self.register_field(ClientID, False)
        self.register_field(Account, False)
        self.register_field(ExecBroker, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Side, True)

MESSAGE_TYPES['H'] = OrderStatusRequest

class Allocation(fix_message.MessageBase):
    _msgtype = 'J'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(AllocID, True)
        self.register_field(AllocTransType, True)
        self.register_field(RefAllocID, False)
        self.register_field(AllocLinkID, False)
        self.register_field(AllocLinkType, False)

        self.register_group(NoOrders, Allocation.NoOrdersGroup, False)

        self.register_group(NoExecs, Allocation.NoExecsGroup, False)
        self.register_field(Side, True)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Shares, True)
        self.register_field(LastMkt, False)
        self.register_field(TradingSessionID, False)
        self.register_field(AvgPx, True)
        self.register_field(Currency, False)
        self.register_field(AvgPrxPrecision, False)
        self.register_field(TradeDate, True)
        self.register_field(TransactTime, False)
        self.register_field(SettlmntTyp, False)
        self.register_field(FutSettDate, False)
        self.register_field(GrossTradeAmt, False)
        self.register_field(NetMoney, False)
        self.register_field(OpenClose, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(NumDaysInterest, False)
        self.register_field(AccruedInterestRate, False)

        self.register_group(NoAllocs, Allocation.NoAllocsGroup, False)

    class NoOrdersGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(ClOrdID, False)
            self.register_field(OrderID, False)
            self.register_field(SecondaryOrderID, False)
            self.register_field(ListID, False)
            self.register_field(WaveNo, False)

    class NoExecsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(LastShares, False)
            self.register_field(ExecID, False)
            self.register_field(LastPx, False)
            self.register_field(LastCapacity, False)

    class NoAllocsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(AllocAccount, False)
            self.register_field(AllocPrice, False)
            self.register_field(AllocShares, True)
            self.register_field(ProcessCode, False)
            self.register_field(BrokerOfCredit, False)
            self.register_field(NotifyBrokerOfCredit, False)
            self.register_field(AllocHandlInst, False)
            self.register_field(AllocText, False)
            self.register_field(EncodedAllocTextLen, False)
            self.register_field(EncodedAllocText, False)
            self.register_field(ExecBroker, False)
            self.register_field(ClientID, False)
            self.register_field(Commission, False)
            self.register_field(CommType, False)
            self.register_field(AllocAvgPx, False)
            self.register_field(AllocNetMoney, False)
            self.register_field(SettlCurrAmt, False)
            self.register_field(SettlCurrency, False)
            self.register_field(SettlCurrFxRate, False)
            self.register_field(SettlCurrFxRateCalc, False)
            self.register_field(AccruedInterestAmt, False)
            self.register_field(SettlInstMode, False)

            self.register_group(NoMiscFees, Allocation.NoAllocsGroup.NoMiscFeesGroup, False)

        class NoMiscFeesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(MiscFeeAmt, False)
                self.register_field(MiscFeeCurr, False)
                self.register_field(MiscFeeType, False)

MESSAGE_TYPES['J'] = Allocation

class ListCancelRequest(fix_message.MessageBase):
    _msgtype = 'K'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(ListID, True)
        self.register_field(TransactTime, True)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['K'] = ListCancelRequest

class ListExecute(fix_message.MessageBase):
    _msgtype = 'L'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
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
        self.Header = Header()
        self.Trailer = Trailer()
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
        self.Header = Header()
        self.Trailer = Trailer()
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

        self.register_group(NoOrders, ListStatus.NoOrdersGroup, True)

    class NoOrdersGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(ClOrdID, True)
            self.register_field(CumQty, True)
            self.register_field(OrdStatus, True)
            self.register_field(LeavesQty, True)
            self.register_field(CxlQty, True)
            self.register_field(AvgPx, True)
            self.register_field(OrdRejReason, False)
            self.register_field(Text, False)
            self.register_field(EncodedTextLen, False)
            self.register_field(EncodedText, False)

MESSAGE_TYPES['N'] = ListStatus

class AllocationInstructionAck(fix_message.MessageBase):
    _msgtype = 'P'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(ClientID, False)
        self.register_field(ExecBroker, False)
        self.register_field(AllocID, True)
        self.register_field(TradeDate, True)
        self.register_field(TransactTime, False)
        self.register_field(AllocStatus, True)
        self.register_field(AllocRejCode, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['P'] = AllocationInstructionAck

class DontKnowTrade(fix_message.MessageBase):
    _msgtype = 'Q'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(OrderID, True)
        self.register_field(ExecID, True)
        self.register_field(DKReason, True)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Side, True)
        self.register_field(OrderQty, False)
        self.register_field(CashOrderQty, False)
        self.register_field(LastShares, False)
        self.register_field(LastPx, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['Q'] = DontKnowTrade

class QuoteRequest(fix_message.MessageBase):
    _msgtype = 'R'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(QuoteReqID, True)

        self.register_group(NoRelatedSym, QuoteRequest.NoRelatedSymGroup, True)

    class NoRelatedSymGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(Symbol, True)
            self.register_field(SymbolSfx, False)
            self.register_field(SecurityID, False)
            self.register_field(IDSource, False)
            self.register_field(SecurityType, False)
            self.register_field(MaturityMonthYear, False)
            self.register_field(MaturityDay, False)
            self.register_field(PutOrCall, False)
            self.register_field(StrikePrice, False)
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
            self.register_field(PrevClosePx, False)
            self.register_field(QuoteRequestType, False)
            self.register_field(TradingSessionID, False)
            self.register_field(Side, False)
            self.register_field(OrderQty, False)
            self.register_field(FutSettDate, False)
            self.register_field(OrdType, False)
            self.register_field(FutSettDate2, False)
            self.register_field(OrderQty2, False)
            self.register_field(ExpireTime, False)
            self.register_field(TransactTime, False)
            self.register_field(Currency, False)

MESSAGE_TYPES['R'] = QuoteRequest

class Quote(fix_message.MessageBase):
    _msgtype = 'S'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(QuoteReqID, False)
        self.register_field(QuoteID, True)
        self.register_field(QuoteResponseLevel, False)
        self.register_field(TradingSessionID, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(BidPx, False)
        self.register_field(OfferPx, False)
        self.register_field(BidSize, False)
        self.register_field(OfferSize, False)
        self.register_field(ValidUntilTime, False)
        self.register_field(BidSpotRate, False)
        self.register_field(OfferSpotRate, False)
        self.register_field(BidForwardPoints, False)
        self.register_field(OfferForwardPoints, False)
        self.register_field(TransactTime, False)
        self.register_field(FutSettDate, False)
        self.register_field(OrdType, False)
        self.register_field(FutSettDate2, False)
        self.register_field(OrderQty2, False)
        self.register_field(Currency, False)

MESSAGE_TYPES['S'] = Quote

class SettlementInstructions(fix_message.MessageBase):
    _msgtype = 'T'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(SettlInstID, True)
        self.register_field(SettlInstTransType, True)
        self.register_field(SettlInstRefID, True)
        self.register_field(SettlInstMode, True)
        self.register_field(SettlInstSource, True)
        self.register_field(AllocAccount, True)
        self.register_field(SettlLocation, False)
        self.register_field(TradeDate, False)
        self.register_field(AllocID, False)
        self.register_field(LastMkt, False)
        self.register_field(TradingSessionID, False)
        self.register_field(Side, False)
        self.register_field(SecurityType, False)
        self.register_field(EffectiveTime, False)
        self.register_field(TransactTime, True)
        self.register_field(ClientID, False)
        self.register_field(ExecBroker, False)
        self.register_field(StandInstDbType, False)
        self.register_field(StandInstDbName, False)
        self.register_field(StandInstDbID, False)
        self.register_field(SettlDeliveryType, False)
        self.register_field(SettlDepositoryCode, False)
        self.register_field(SettlBrkrCode, False)
        self.register_field(SettlInstCode, False)
        self.register_field(SecuritySettlAgentName, False)
        self.register_field(SecuritySettlAgentCode, False)
        self.register_field(SecuritySettlAgentAcctNum, False)
        self.register_field(SecuritySettlAgentAcctName, False)
        self.register_field(SecuritySettlAgentContactName, False)
        self.register_field(SecuritySettlAgentContactPhone, False)
        self.register_field(CashSettlAgentName, False)
        self.register_field(CashSettlAgentCode, False)
        self.register_field(CashSettlAgentAcctNum, False)
        self.register_field(CashSettlAgentAcctName, False)
        self.register_field(CashSettlAgentContactName, False)
        self.register_field(CashSettlAgentContactPhone, False)

MESSAGE_TYPES['T'] = SettlementInstructions

class MarketDataRequest(fix_message.MessageBase):
    _msgtype = 'V'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(MDReqID, True)
        self.register_field(SubscriptionRequestType, True)
        self.register_field(MarketDepth, True)
        self.register_field(MDUpdateType, False)
        self.register_field(AggregatedBook, False)

        self.register_group(NoMDEntryTypes, MarketDataRequest.NoMDEntryTypesGroup, True)

        self.register_group(NoRelatedSym, MarketDataRequest.NoRelatedSymGroup, True)

    class NoMDEntryTypesGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(MDEntryType, True)

    class NoRelatedSymGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(Symbol, True)
            self.register_field(SymbolSfx, False)
            self.register_field(SecurityID, False)
            self.register_field(IDSource, False)
            self.register_field(SecurityType, False)
            self.register_field(MaturityMonthYear, False)
            self.register_field(MaturityDay, False)
            self.register_field(PutOrCall, False)
            self.register_field(StrikePrice, False)
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
            self.register_field(TradingSessionID, False)

MESSAGE_TYPES['V'] = MarketDataRequest

class MarketDataSnapshotFullRefresh(fix_message.MessageBase):
    _msgtype = 'W'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(MDReqID, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(FinancialStatus, False)
        self.register_field(CorporateAction, False)
        self.register_field(TotalVolumeTraded, False)

        self.register_group(NoMDEntries, MarketDataSnapshotFullRefresh.NoMDEntriesGroup, True)

    class NoMDEntriesGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(MDEntryType, True)
            self.register_field(MDEntryPx, True)
            self.register_field(Currency, False)
            self.register_field(MDEntrySize, False)
            self.register_field(MDEntryDate, False)
            self.register_field(MDEntryTime, False)
            self.register_field(TickDirection, False)
            self.register_field(MDMkt, False)
            self.register_field(TradingSessionID, False)
            self.register_field(QuoteCondition, False)
            self.register_field(TradeCondition, False)
            self.register_field(MDEntryOriginator, False)
            self.register_field(LocationID, False)
            self.register_field(DeskID, False)
            self.register_field(OpenCloseSettleFlag, False)
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
            self.register_field(Text, False)
            self.register_field(EncodedTextLen, False)
            self.register_field(EncodedText, False)

MESSAGE_TYPES['W'] = MarketDataSnapshotFullRefresh

class MarketDataIncrementalRefresh(fix_message.MessageBase):
    _msgtype = 'X'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(MDReqID, False)

        self.register_group(NoMDEntries, MarketDataIncrementalRefresh.NoMDEntriesGroup, True)

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
            self.register_field(IDSource, False)
            self.register_field(SecurityType, False)
            self.register_field(MaturityMonthYear, False)
            self.register_field(MaturityDay, False)
            self.register_field(PutOrCall, False)
            self.register_field(StrikePrice, False)
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
            self.register_field(QuoteCondition, False)
            self.register_field(TradeCondition, False)
            self.register_field(MDEntryOriginator, False)
            self.register_field(LocationID, False)
            self.register_field(DeskID, False)
            self.register_field(OpenCloseSettleFlag, False)
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
            self.register_field(TotalVolumeTraded, False)
            self.register_field(Text, False)
            self.register_field(EncodedTextLen, False)
            self.register_field(EncodedText, False)

MESSAGE_TYPES['X'] = MarketDataIncrementalRefresh

class MarketDataRequestReject(fix_message.MessageBase):
    _msgtype = 'Y'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(MDReqID, True)
        self.register_field(MDReqRejReason, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

MESSAGE_TYPES['Y'] = MarketDataRequestReject

class QuoteCancel(fix_message.MessageBase):
    _msgtype = 'Z'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(QuoteReqID, False)
        self.register_field(QuoteID, True)
        self.register_field(QuoteCancelType, True)
        self.register_field(QuoteResponseLevel, False)
        self.register_field(TradingSessionID, False)

        self.register_group(NoQuoteEntries, QuoteCancel.NoQuoteEntriesGroup, True)

    class NoQuoteEntriesGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(Symbol, True)
            self.register_field(SymbolSfx, False)
            self.register_field(SecurityID, False)
            self.register_field(IDSource, False)
            self.register_field(SecurityType, False)
            self.register_field(MaturityMonthYear, False)
            self.register_field(MaturityDay, False)
            self.register_field(PutOrCall, False)
            self.register_field(StrikePrice, False)
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
            self.register_field(UnderlyingSymbol, False)

MESSAGE_TYPES['Z'] = QuoteCancel

class QuoteStatusRequest(fix_message.MessageBase):
    _msgtype = 'a'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(QuoteID, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Side, False)
        self.register_field(TradingSessionID, False)

MESSAGE_TYPES['a'] = QuoteStatusRequest

class QuoteAcknowledgement(fix_message.MessageBase):
    _msgtype = 'b'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(QuoteReqID, False)
        self.register_field(QuoteID, False)
        self.register_field(QuoteAckStatus, True)
        self.register_field(QuoteRejectReason, False)
        self.register_field(QuoteResponseLevel, False)
        self.register_field(TradingSessionID, False)
        self.register_field(Text, False)

        self.register_group(NoQuoteSets, QuoteAcknowledgement.NoQuoteSetsGroup, False)

    class NoQuoteSetsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(QuoteSetID, False)
            self.register_field(UnderlyingSymbol, False)
            self.register_field(UnderlyingSymbolSfx, False)
            self.register_field(UnderlyingSecurityID, False)
            self.register_field(UnderlyingIDSource, False)
            self.register_field(UnderlyingSecurityType, False)
            self.register_field(UnderlyingMaturityMonthYear, False)
            self.register_field(UnderlyingMaturityDay, False)
            self.register_field(UnderlyingPutOrCall, False)
            self.register_field(UnderlyingStrikePrice, False)
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
            self.register_field(TotQuoteEntries, False)

            self.register_group(NoQuoteEntries, QuoteAcknowledgement.NoQuoteSetsGroup.NoQuoteEntriesGroup, False)

        class NoQuoteEntriesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(QuoteEntryID, False)
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(IDSource, False)
                self.register_field(SecurityType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDay, False)
                self.register_field(PutOrCall, False)
                self.register_field(StrikePrice, False)
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
                self.register_field(QuoteEntryRejectReason, False)

MESSAGE_TYPES['b'] = QuoteAcknowledgement

class SecurityDefinitionRequest(fix_message.MessageBase):
    _msgtype = 'c'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(SecurityReqID, True)
        self.register_field(SecurityRequestType, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Currency, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)
        self.register_field(TradingSessionID, False)

        self.register_group(NoRelatedSym, SecurityDefinitionRequest.NoRelatedSymGroup, False)

    class NoRelatedSymGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(UnderlyingSymbol, False)
            self.register_field(UnderlyingSymbolSfx, False)
            self.register_field(UnderlyingSecurityID, False)
            self.register_field(UnderlyingIDSource, False)
            self.register_field(UnderlyingSecurityType, False)
            self.register_field(UnderlyingMaturityMonthYear, False)
            self.register_field(UnderlyingMaturityDay, False)
            self.register_field(UnderlyingPutOrCall, False)
            self.register_field(UnderlyingStrikePrice, False)
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
            self.register_field(RatioQty, False)
            self.register_field(Side, False)
            self.register_field(UnderlyingCurrency, False)

MESSAGE_TYPES['c'] = SecurityDefinitionRequest

class SecurityDefinition(fix_message.MessageBase):
    _msgtype = 'd'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(SecurityReqID, True)
        self.register_field(SecurityResponseID, True)
        self.register_field(SecurityResponseType, False)
        self.register_field(TotalNumSecurities, True)
        self.register_field(Symbol, False)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Currency, False)
        self.register_field(TradingSessionID, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

        self.register_group(NoRelatedSym, SecurityDefinition.NoRelatedSymGroup, False)

    class NoRelatedSymGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(UnderlyingSymbol, False)
            self.register_field(UnderlyingSymbolSfx, False)
            self.register_field(UnderlyingSecurityID, False)
            self.register_field(UnderlyingIDSource, False)
            self.register_field(UnderlyingSecurityType, False)
            self.register_field(UnderlyingMaturityMonthYear, False)
            self.register_field(UnderlyingMaturityDay, False)
            self.register_field(UnderlyingPutOrCall, False)
            self.register_field(UnderlyingStrikePrice, False)
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
            self.register_field(RatioQty, False)
            self.register_field(Side, False)
            self.register_field(UnderlyingCurrency, False)

MESSAGE_TYPES['d'] = SecurityDefinition

class SecurityStatusRequest(fix_message.MessageBase):
    _msgtype = 'e'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(SecurityStatusReqID, True)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Currency, False)
        self.register_field(SubscriptionRequestType, True)
        self.register_field(TradingSessionID, False)

MESSAGE_TYPES['e'] = SecurityStatusRequest

class SecurityStatus(fix_message.MessageBase):
    _msgtype = 'f'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(SecurityStatusReqID, False)
        self.register_field(Symbol, True)
        self.register_field(SymbolSfx, False)
        self.register_field(SecurityID, False)
        self.register_field(IDSource, False)
        self.register_field(SecurityType, False)
        self.register_field(MaturityMonthYear, False)
        self.register_field(MaturityDay, False)
        self.register_field(PutOrCall, False)
        self.register_field(StrikePrice, False)
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
        self.register_field(Currency, False)
        self.register_field(TradingSessionID, False)
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

MESSAGE_TYPES['f'] = SecurityStatus

class TradingSessionStatusRequest(fix_message.MessageBase):
    _msgtype = 'g'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(TradSesReqID, True)
        self.register_field(TradingSessionID, False)
        self.register_field(TradSesMethod, False)
        self.register_field(TradSesMode, False)
        self.register_field(SubscriptionRequestType, True)

MESSAGE_TYPES['g'] = TradingSessionStatusRequest

class TradingSessionStatus(fix_message.MessageBase):
    _msgtype = 'h'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(TradSesReqID, False)
        self.register_field(TradingSessionID, True)
        self.register_field(TradSesMethod, False)
        self.register_field(TradSesMode, False)
        self.register_field(UnsolicitedIndicator, False)
        self.register_field(TradSesStatus, True)
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
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(QuoteReqID, False)
        self.register_field(QuoteID, True)
        self.register_field(QuoteResponseLevel, False)
        self.register_field(DefBidSize, False)
        self.register_field(DefOfferSize, False)

        self.register_group(NoQuoteSets, MassQuote.NoQuoteSetsGroup, True)

    class NoQuoteSetsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(QuoteSetID, True)
            self.register_field(UnderlyingSymbol, True)
            self.register_field(UnderlyingSymbolSfx, False)
            self.register_field(UnderlyingSecurityID, False)
            self.register_field(UnderlyingIDSource, False)
            self.register_field(UnderlyingSecurityType, False)
            self.register_field(UnderlyingMaturityMonthYear, False)
            self.register_field(UnderlyingMaturityDay, False)
            self.register_field(UnderlyingPutOrCall, False)
            self.register_field(UnderlyingStrikePrice, False)
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
            self.register_field(QuoteSetValidUntilTime, False)
            self.register_field(TotQuoteEntries, True)

            self.register_group(NoQuoteEntries, MassQuote.NoQuoteSetsGroup.NoQuoteEntriesGroup, True)

        class NoQuoteEntriesGroup(fix_message.FIXGroup):
            def __init__(self):
                self.register_field(QuoteEntryID, True)
                self.register_field(Symbol, False)
                self.register_field(SymbolSfx, False)
                self.register_field(SecurityID, False)
                self.register_field(IDSource, False)
                self.register_field(SecurityType, False)
                self.register_field(MaturityMonthYear, False)
                self.register_field(MaturityDay, False)
                self.register_field(PutOrCall, False)
                self.register_field(StrikePrice, False)
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
                self.register_field(BidPx, False)
                self.register_field(OfferPx, False)
                self.register_field(BidSize, False)
                self.register_field(OfferSize, False)
                self.register_field(ValidUntilTime, False)
                self.register_field(BidSpotRate, False)
                self.register_field(OfferSpotRate, False)
                self.register_field(BidForwardPoints, False)
                self.register_field(OfferForwardPoints, False)
                self.register_field(TransactTime, False)
                self.register_field(TradingSessionID, False)
                self.register_field(FutSettDate, False)
                self.register_field(OrdType, False)
                self.register_field(FutSettDate2, False)
                self.register_field(OrderQty2, False)
                self.register_field(Currency, False)

MESSAGE_TYPES['i'] = MassQuote

class BusinessMessageReject(fix_message.MessageBase):
    _msgtype = 'j'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
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
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(BidID, False)
        self.register_field(ClientBidID, True)
        self.register_field(BidRequestTransType, True)
        self.register_field(ListName, False)
        self.register_field(TotalNumSecurities, True)
        self.register_field(BidType, True)
        self.register_field(NumTickets, False)
        self.register_field(Currency, False)
        self.register_field(SideValue1, False)
        self.register_field(SideValue2, False)

        self.register_group(NoBidDescriptors, BidRequest.NoBidDescriptorsGroup, False)

        self.register_group(NoBidComponents, BidRequest.NoBidComponentsGroup, False)
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
        self.register_field(TradeType, True)
        self.register_field(BasisPxType, True)
        self.register_field(StrikeTime, False)
        self.register_field(Text, False)
        self.register_field(EncodedTextLen, False)
        self.register_field(EncodedText, False)

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

    class NoBidComponentsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(ListID, False)
            self.register_field(Side, False)
            self.register_field(TradingSessionID, False)
            self.register_field(NetGrossInd, False)
            self.register_field(SettlmntTyp, False)
            self.register_field(FutSettDate, False)
            self.register_field(Account, False)

MESSAGE_TYPES['k'] = BidRequest

class BidResponse(fix_message.MessageBase):
    _msgtype = 'l'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(BidID, False)
        self.register_field(ClientBidID, False)

        self.register_group(NoBidComponents, BidResponse.NoBidComponentsGroup, True)

    class NoBidComponentsGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(Commission, True)
            self.register_field(CommType, True)
            self.register_field(ListID, False)
            self.register_field(Country, False)
            self.register_field(Side, False)
            self.register_field(Price, False)
            self.register_field(PriceType, False)
            self.register_field(FairValue, False)
            self.register_field(NetGrossInd, False)
            self.register_field(SettlmntTyp, False)
            self.register_field(FutSettDate, False)
            self.register_field(TradingSessionID, False)
            self.register_field(Text, False)
            self.register_field(EncodedTextLen, False)
            self.register_field(EncodedText, False)

MESSAGE_TYPES['l'] = BidResponse

class ListStrikePrice(fix_message.MessageBase):
    _msgtype = 'm'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(ListID, True)
        self.register_field(TotNoStrikes, True)

        self.register_group(NoStrikes, ListStrikePrice.NoStrikesGroup, True)

    class NoStrikesGroup(fix_message.FIXGroup):
        def __init__(self):
            self.register_field(Symbol, True)
            self.register_field(SymbolSfx, False)
            self.register_field(SecurityID, False)
            self.register_field(IDSource, False)
            self.register_field(SecurityType, False)
            self.register_field(MaturityMonthYear, False)
            self.register_field(MaturityDay, False)
            self.register_field(PutOrCall, False)
            self.register_field(StrikePrice, False)
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
            self.register_field(PrevClosePx, False)
            self.register_field(ClOrdID, False)
            self.register_field(Side, False)
            self.register_field(Price, True)
            self.register_field(Currency, False)
            self.register_field(Text, False)
            self.register_field(EncodedTextLen, False)
            self.register_field(EncodedText, False)

MESSAGE_TYPES['m'] = ListStrikePrice

class Trailer(fix_message.MessageBase):
    def __init__(self):
        super().__init__()
        self.register_field(SignatureLength, False)
        self.register_field(Signature, False)
        self.register_field(CheckSum, True)
