from . import field_types

class Account (field_types.String_Type) :
    _tag = '1'

class AdvId (field_types.String_Type) :
    _tag = '2'

class AdvRefID (field_types.String_Type) :
    _tag = '3'

class AdvSide (field_types.char_Type) :
    _tag = '4'
    ENUM_BUY = 'B'
    ENUM_SELL = 'S'
    ENUM_TRADE = 'T'
    ENUM_CROSS = 'X'

class AdvTransType (field_types.String_Type) :
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

class CommType (field_types.char_Type) :
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

class ExecInst (field_types.MultipleCharValue_Type) :
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
    ENUM_FIXED_PEG_TO_LOCAL_BEST_BID_OR_OFFER_AT_TIME_OF_ORDER = 'T'
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
    ENUM_INTERMARKET_SWEEP = 'f'
    ENUM_EXTERNAL_ROUTING_ALLOWED = 'g'
    ENUM_EXTERNAL_ROUTING_NOT_ALLOWED = 'h'
    ENUM_IMBALANCE_ONLY = 'i'
    ENUM_SINGLE_EXECUTION_REQUESTED_FOR_BLOCK_TRADE = 'j'
    ENUM_BEST_EXECUTION = 'k'
    ENUM_SUSPEND_ON_SYSTEM_FAILURE = 'l'
    ENUM_SUSPEND_ON_TRADING_HALT = 'm'
    ENUM_REINSTATE_ON_CONNECTION_LOSS = 'n'
    ENUM_CANCEL_ON_CONNECTION_LOSS = 'o'
    ENUM_SUSPEND_ON_CONNECTION_LOSS = 'p'
    ENUM_RELEASE_FROM_SUSPENSION = 'q'
    ENUM_EXECUTE_AS_DELTA_NEUTRAL = 'r'
    ENUM_EXECUTE_AS_DURATION_NEUTRAL = 's'
    ENUM_EXECUTE_AS_FX_NEUTRAL = 't'

class ExecRefID (field_types.String_Type) :
    _tag = '19'

class HandlInst (field_types.char_Type) :
    _tag = '21'
    ENUM_AUTOMATED_EXECUTION_NO_INTERVENTION = '1'
    ENUM_AUTOMATED_EXECUTION_INTERVENTION_OK = '2'
    ENUM_MANUAL_ORDER = '3'

class SecurityIDSource (field_types.String_Type) :
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
    ENUM_ISDA_FP_MLURL = 'K'
    ENUM_LETTER_OF_CREDIT = 'L'
    ENUM_MARKETPLACE_ASSIGNED_IDENTIFIER = 'M'

class IOIID (field_types.String_Type) :
    _tag = '23'

class IOIQltyInd (field_types.char_Type) :
    _tag = '25'
    ENUM_HIGH = 'H'
    ENUM_LOW = 'L'
    ENUM_MEDIUM = 'M'

class IOIRefID (field_types.String_Type) :
    _tag = '26'

class IOIQty (field_types.String_Type) :
    _tag = '27'
    ENUM_SMALL = 'S'
    ENUM_MEDIUM = 'M'
    ENUM_LARGE = 'L'
    ENUM_UNDISCLOSED_QUANTITY = 'U'

class IOITransType (field_types.char_Type) :
    _tag = '28'
    ENUM_NEW = 'N'
    ENUM_CANCEL = 'C'
    ENUM_REPLACE = 'R'

class LastCapacity (field_types.char_Type) :
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

class MsgType (field_types.String_Type) :
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
    ENUM_NEWS = 'B'
    ENUM_COLLATERAL_REPORT = 'BA'
    ENUM_COLLATERAL_INQUIRY = 'BB'
    ENUM_NETWORK_COUNTERPARTY_SYSTEM_STATUS_REQUEST = 'BC'
    ENUM_NETWORK_COUNTERPARTY_SYSTEM_STATUS_RESPONSE = 'BD'
    ENUM_USER_REQUEST = 'BE'
    ENUM_USER_RESPONSE = 'BF'
    ENUM_COLLATERAL_INQUIRY_ACK = 'BG'
    ENUM_CONFIRMATION_REQUEST = 'BH'
    ENUM_TRADING_SESSION_LIST_REQUEST = 'BI'
    ENUM_TRADING_SESSION_LIST = 'BJ'
    ENUM_SECURITY_LIST_UPDATE_REPORT = 'BK'
    ENUM_ADJUSTED_POSITION_REPORT = 'BL'
    ENUM_ALLOCATION_INSTRUCTION_ALERT = 'BM'
    ENUM_EXECUTION_ACKNOWLEDGEMENT = 'BN'
    ENUM_CONTRARY_INTENTION_REPORT = 'BO'
    ENUM_SECURITY_DEFINITION_UPDATE_REPORT = 'BP'
    ENUM_SETTLEMENT_OBLIGATION_REPORT = 'BQ'
    ENUM_DERIVATIVE_SECURITY_LIST_UPDATE_REPORT = 'BR'
    ENUM_TRADING_SESSION_LIST_UPDATE_REPORT = 'BS'
    ENUM_MARKET_DEFINITION_REQUEST = 'BT'
    ENUM_MARKET_DEFINITION = 'BU'
    ENUM_MARKET_DEFINITION_UPDATE_REPORT = 'BV'
    ENUM_APPLICATION_MESSAGE_REQUEST = 'BW'
    ENUM_APPLICATION_MESSAGE_REQUEST_ACK = 'BX'
    ENUM_APPLICATION_MESSAGE_REPORT = 'BY'
    ENUM_ORDER_MASS_ACTION_REPORT = 'BZ'
    ENUM_EMAIL = 'C'
    ENUM_ORDER_MASS_ACTION_REQUEST = 'CA'
    ENUM_USER_NOTIFICATION = 'CB'
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
    ENUM_XM_LNON_FIX = 'n'
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

class NewSeqNo (field_types.SeqNum_Type) :
    _tag = '36'

class OrderID (field_types.String_Type) :
    _tag = '37'

class OrderQty (field_types.Qty_Type) :
    _tag = '38'

class OrdStatus (field_types.char_Type) :
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
    ENUM_FUNARI = 'I'
    ENUM_MARKET_IF_TOUCHED = 'J'
    ENUM_MARKET_WITH_LEFT_OVER_AS_LIMIT = 'K'
    ENUM_PREVIOUS_FUND_VALUATION_POINT = 'L'
    ENUM_NEXT_FUND_VALUATION_POINT = 'M'
    ENUM_PEGGED = 'P'
    ENUM_COUNTER_ORDER_SELECTION = 'Q'

class OrigClOrdID (field_types.String_Type) :
    _tag = '41'

class OrigTime (field_types.UTCTimestamp_Type) :
    _tag = '42'

class PossDupFlag (field_types.Boolean_Type) :
    _tag = '43'
    ENUM_ORIGINAL_TRANSMISSION = 'N'
    ENUM_POSSIBLE_DUPLICATE = 'Y'

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

class TimeInForce (field_types.char_Type) :
    _tag = '59'
    ENUM_DAY = '0'
    ENUM_GOOD_TILL_CANCEL = '1'
    ENUM_AT_THE_OPENING = '2'
    ENUM_IMMEDIATE_OR_CANCEL = '3'
    ENUM_FILL_OR_KILL = '4'
    ENUM_GOOD_TILL_CROSSING = '5'
    ENUM_GOOD_TILL_DATE = '6'
    ENUM_AT_THE_CLOSE = '7'
    ENUM_GOOD_THROUGH_CROSSING = '8'
    ENUM_AT_CROSSING = '9'

class TransactTime (field_types.UTCTimestamp_Type) :
    _tag = '60'

class Urgency (field_types.char_Type) :
    _tag = '61'
    ENUM_NORMAL = '0'
    ENUM_FLASH = '1'
    ENUM_BACKGROUND = '2'

class ValidUntilTime (field_types.UTCTimestamp_Type) :
    _tag = '62'

class SettlType (field_types.String_Type) :
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
    ENUM_BROKEN_DATE = 'B'
    ENUM_FX_SPOT_NEXT_SETTLEMENT = 'C'

class SettlDate (field_types.LocalMktDate_Type) :
    _tag = '64'

class SymbolSfx (field_types.String_Type) :
    _tag = '65'
    ENUM_EUCP_WITH_LUMP_SUM_INTEREST = 'CD'
    ENUM_WHEN_ISSUED = 'WI'

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

class AllocTransType (field_types.char_Type) :
    _tag = '71'
    ENUM_NEW = '0'
    ENUM_REPLACE = '1'
    ENUM_CANCEL = '2'
    ENUM_PRELIMINARY = '3'
    ENUM_CALCULATED = '4'
    ENUM_CALCULATED_WITHOUT_PRELIMINARY = '5'
    ENUM_REVERSAL = '6'

class RefAllocID (field_types.String_Type) :
    _tag = '72'

class NoOrders (field_types.NumInGroup_Type) :
    _tag = '73'

class AvgPxPrecision (field_types.int_Type) :
    _tag = '74'

class TradeDate (field_types.LocalMktDate_Type) :
    _tag = '75'

class PositionEffect (field_types.char_Type) :
    _tag = '77'
    ENUM_CLOSE = 'C'
    ENUM_FIFO = 'F'
    ENUM_OPEN = 'O'
    ENUM_ROLLED = 'R'
    ENUM_CLOSE_BUT_NOTIFY_ON_OPEN = 'N'
    ENUM_DEFAULT = 'D'

class NoAllocs (field_types.NumInGroup_Type) :
    _tag = '78'

class AllocAccount (field_types.String_Type) :
    _tag = '79'

class AllocQty (field_types.Qty_Type) :
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

class CxlQty (field_types.Qty_Type) :
    _tag = '84'

class NoDlvyInst (field_types.NumInGroup_Type) :
    _tag = '85'

class AllocStatus (field_types.int_Type) :
    _tag = '87'
    ENUM_ACCEPTED = 0
    ENUM_BLOCK_LEVEL_REJECT = 1
    ENUM_ACCOUNT_LEVEL_REJECT = 2
    ENUM_RECEIVED = 3
    ENUM_INCOMPLETE = 4
    ENUM_REJECTED_BY_INTERMEDIARY = 5
    ENUM_ALLOCATION_PENDING = 6
    ENUM_REVERSED = 7

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

class EmailType (field_types.char_Type) :
    _tag = '94'
    ENUM_NEW = '0'
    ENUM_REPLY = '1'
    ENUM_ADMIN_REPLY = '2'

class RawDataLength (field_types.Length_Type) :
    _tag = '95'

class RawData (field_types.data_Type) :
    _tag = '96'

class PossResend (field_types.Boolean_Type) :
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

class StopPx (field_types.Price_Type) :
    _tag = '99'

class ExDestination (field_types.Exchange_Type) :
    _tag = '100'

class CxlRejReason (field_types.int_Type) :
    _tag = '102'
    ENUM_TOO_LATE_TO_CANCEL = 0
    ENUM_UNKNOWN_ORDER = 1
    ENUM_BROKER_CREDIT = 2
    ENUM_ORDER_ALREADY_IN_PENDING_STATUS = 3
    ENUM_UNABLE_TO_PROCESS_ORDER_MASS_CANCEL_REQUEST = 4
    ENUM_ORIG_ORD_MOD_TIME = 5
    ENUM_DUPLICATE_CL_ORD_ID = 6
    ENUM_PRICE_EXCEEDS_CURRENT_PRICE = 7
    ENUM_PRICE_EXCEEDS_CURRENT_PRICE_BAND = 8
    ENUM_INVALID_PRICE_INCREMENT = 18
    ENUM_OTHER = 99

class OrdRejReason (field_types.int_Type) :
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
    ENUM_SURVEILLENCE_OPTION = 12
    ENUM_INCORRECT_QUANTITY = 13
    ENUM_INCORRECT_ALLOCATED_QUANTITY = 14
    ENUM_UNKNOWN_ACCOUNT = 15
    ENUM_PRICE_EXCEEDS_CURRENT_PRICE_BAND = 16
    ENUM_INVALID_PRICE_INCREMENT = 18
    ENUM_OTHER = 99

class IOIQualifier (field_types.char_Type) :
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

class ReportToExch (field_types.Boolean_Type) :
    _tag = '113'
    ENUM_SENDER_REPORTS = 'N'
    ENUM_RECEIVER_REPORTS = 'Y'

class LocateReqd (field_types.Boolean_Type) :
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

class ForexReq (field_types.Boolean_Type) :
    _tag = '121'
    ENUM_DO_NOT_EXECUTE_FOREX_AFTER_SECURITY_TRADE = 'N'
    ENUM_EXECUTE_FOREX_AFTER_SECURITY_TRADE = 'Y'

class OrigSendingTime (field_types.UTCTimestamp_Type) :
    _tag = '122'

class GapFillFlag (field_types.Boolean_Type) :
    _tag = '123'
    ENUM_SEQUENCE_RESET = 'N'
    ENUM_GAP_FILL_MESSAGE = 'Y'

class NoExecs (field_types.NumInGroup_Type) :
    _tag = '124'

class ExpireTime (field_types.UTCTimestamp_Type) :
    _tag = '126'

class DKReason (field_types.char_Type) :
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

class IOINaturalFlag (field_types.Boolean_Type) :
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

class NoMiscFees (field_types.NumInGroup_Type) :
    _tag = '136'

class MiscFeeAmt (field_types.Amt_Type) :
    _tag = '137'

class MiscFeeCurr (field_types.Currency_Type) :
    _tag = '138'

class MiscFeeType (field_types.String_Type) :
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
    ENUM_TRANSFER_FEE = '13'
    ENUM_SECURITY_LENDING = '14'

class PrevClosePx (field_types.Price_Type) :
    _tag = '140'

class ResetSeqNumFlag (field_types.Boolean_Type) :
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

class NoRelatedSym (field_types.NumInGroup_Type) :
    _tag = '146'

class Subject (field_types.String_Type) :
    _tag = '147'

class Headline (field_types.String_Type) :
    _tag = '148'

class URLLink (field_types.String_Type) :
    _tag = '149'

class ExecType (field_types.char_Type) :
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
    ENUM_TRADE_IN_A_CLEARING_HOLD = 'J'
    ENUM_TRADE_HAS_BEEN_RELEASED_TO_CLEARING = 'K'
    ENUM_TRIGGERED_OR_ACTIVATED_BY_SYSTEM = 'L'

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
    ENUM_MULTIPLY = 'M'
    ENUM_DIVIDE = 'D'

class NumDaysInterest (field_types.int_Type) :
    _tag = '157'

class AccruedInterestRate (field_types.Percentage_Type) :
    _tag = '158'

class AccruedInterestAmt (field_types.Amt_Type) :
    _tag = '159'

class SettlInstMode (field_types.char_Type) :
    _tag = '160'
    ENUM_DEFAULT = '0'
    ENUM_STANDING_INSTRUCTIONS_PROVIDED = '1'
    ENUM_SPECIFIC_ALLOCATION_ACCOUNT_OVERRIDING = '2'
    ENUM_SPECIFIC_ALLOCATION_ACCOUNT_STANDING = '3'
    ENUM_SPECIFIC_ORDER_FOR_A_SINGLE_ACCOUNT = '4'
    ENUM_REQUEST_REJECT = '5'

class AllocText (field_types.String_Type) :
    _tag = '161'

class SettlInstID (field_types.String_Type) :
    _tag = '162'

class SettlInstTransType (field_types.char_Type) :
    _tag = '163'
    ENUM_NEW = 'N'
    ENUM_CANCEL = 'C'
    ENUM_REPLACE = 'R'
    ENUM_RESTATE = 'T'

class EmailThreadID (field_types.String_Type) :
    _tag = '164'

class SettlInstSource (field_types.char_Type) :
    _tag = '165'
    ENUM_BROKER_CREDIT = '1'
    ENUM_INSTITUTION = '2'
    ENUM_INVESTOR = '3'

class SecurityType (field_types.String_Type) :
    _tag = '167'
    ENUM_US_TREASURY_NOTE_OLD = 'UST'
    ENUM_US_TREASURY_BILL_OLD = 'USTB'
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
    ENUM_EURO_CORPORATE_FLOATING_RATE_NOTES = 'EUFRN'
    ENUM_US_CORPORATE_FLOATING_RATE_NOTES = 'FRN'
    ENUM_INDEXED_LINKED = 'XLINKD'
    ENUM_STRUCTURED_NOTES = 'STRUCT'
    ENUM_YANKEE_CORPORATE_BOND = 'YANK'
    ENUM_FOREIGN_EXCHANGE_CONTRACT = 'FOR'
    ENUM_CREDIT_DEFAULT_SWAP = 'CDS'
    ENUM_FUTURE = 'FUT'
    ENUM_OPTION = 'OPT'
    ENUM_OPTIONS_ON_FUTURES = 'OOF'
    ENUM_OPTIONS_ON_PHYSICAL = 'OOP'
    ENUM_INTEREST_RATE_SWAP = 'IRS'
    ENUM_OPTIONS_ON_COMBO = 'OOC'
    ENUM_COMMON_STOCK = 'CS'
    ENUM_PREFERRED_STOCK = 'PS'
    ENUM_REPURCHASE = 'REPO'
    ENUM_FORWARD = 'FORWARD'
    ENUM_BUY_SELLBACK = 'BUYSELL'
    ENUM_SECURITIES_LOAN = 'SECLOAN'
    ENUM_SECURITIES_PLEDGE = 'SECPLEDGE'
    ENUM_BRADY_BOND = 'BRADY'
    ENUM_CANADIAN_TREASURY_NOTES = 'CAN'
    ENUM_CANADIAN_TREASURY_BILLS = 'CTB'
    ENUM_EURO_SOVEREIGNS = 'EUSOV'
    ENUM_CANADIAN_PROVINCIAL_BONDS = 'PROV'
    ENUM_TREASURY_BILL = 'TB'
    ENUM_US_TREASURY_BOND = 'TBOND'
    ENUM_INTEREST_STRIP_FROM_ANY_BOND_OR_NOTE = 'TINT'
    ENUM_US_TREASURY_BILL = 'TBILL'
    ENUM_TREASURY_INFLATION_PROTECTED_SECURITIES = 'TIPS'
    ENUM_PRINCIPAL_STRIP_OF_A_CALLABLE_BOND_OR_NOTE = 'TCAL'
    ENUM_PRINCIPAL_STRIP_FROM_A_NON_CALLABLE_BOND_OR_NOTE = 'TPRN'
    ENUM_US_TREASURY_NOTE = 'TNOTE'
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
    ENUM_BANK_DEPOSITORY_NOTE = 'BDN'
    ENUM_BANK_NOTES = 'BN'
    ENUM_BILL_OF_EXCHANGES = 'BOX'
    ENUM_CANADIAN_MONEY_MARKETS = 'CAMM'
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
    ENUM_SHORT_TERM_LOAN_NOTE = 'STN'
    ENUM_PLAZOS_FIJOS = 'PZFJ'
    ENUM_SECURED_LIQUIDITY_NOTE = 'SLQN'
    ENUM_TIME_DEPOSIT = 'TD'
    ENUM_TERM_LIQUIDITY_NOTE = 'TLQN'
    ENUM_EXTENDED_COMM_NOTE = 'XCN'
    ENUM_YANKEE_CERTIFICATE_OF_DEPOSIT = 'YCD'
    ENUM_ASSET_BACKED_SECURITIES = 'ABS'
    ENUM_CANADIAN_MORTGAGE_BONDS = 'CMB'
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
    ENUM_TAXABLE_MUNICIPAL_CP = 'TMCP'
    ENUM_TAX_REVENUE_ANTICIPATION_NOTE = 'TRAN'
    ENUM_VARIABLE_RATE_DEMAND_NOTE = 'VRDN'
    ENUM_WARRANT = 'WAR'
    ENUM_MUTUAL_FUND = 'MF'
    ENUM_MULTILEG_INSTRUMENT = 'MLEG'
    ENUM_NO_SECURITY_TYPE = 'NONE'
    ENUM_WILDCARD = '?'
    ENUM_CASH = 'CASH'

class EffectiveTime (field_types.UTCTimestamp_Type) :
    _tag = '168'

class StandInstDbType (field_types.int_Type) :
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

class SettlDeliveryType (field_types.int_Type) :
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

class AllocLinkType (field_types.int_Type) :
    _tag = '197'
    ENUM_FX_NETTING = 0
    ENUM_FX_SWAP = 1

class SecondaryOrderID (field_types.String_Type) :
    _tag = '198'

class NoIOIQualifiers (field_types.NumInGroup_Type) :
    _tag = '199'

class MaturityMonthYear (field_types.MonthYear_Type) :
    _tag = '200'

class PutOrCall (field_types.int_Type) :
    _tag = '201'
    ENUM_PUT = 0
    ENUM_CALL = 1

class StrikePrice (field_types.Price_Type) :
    _tag = '202'

class CoveredOrUncovered (field_types.int_Type) :
    _tag = '203'
    ENUM_COVERED = 0
    ENUM_UNCOVERED = 1

class OptAttribute (field_types.char_Type) :
    _tag = '206'

class SecurityExchange (field_types.Exchange_Type) :
    _tag = '207'

class NotifyBrokerOfCredit (field_types.Boolean_Type) :
    _tag = '208'
    ENUM_DETAILS_SHOULD_NOT_BE_COMMUNICATED = 'N'
    ENUM_DETAILS_SHOULD_BE_COMMUNICATED = 'Y'

class AllocHandlInst (field_types.int_Type) :
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

class RoutingType (field_types.int_Type) :
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
    ENUM_EONIA = 'EONIA'
    ENUM_EUREPO = 'EUREPO'
    ENUM_EURIBOR = 'Euribor'
    ENUM_FUTURE_SWAP = 'FutureSWAP'
    ENUM_LIBID = 'LIBID'
    ENUM_LIBOR = 'LIBOR'
    ENUM_MUNI_AAA = 'MuniAAA'
    ENUM_OTHER = 'OTHER'
    ENUM_PFANDBRIEFE = 'Pfandbriefe'
    ENUM_SONIA = 'SONIA'
    ENUM_SWAP = 'SWAP'
    ENUM_TREASURY = 'Treasury'

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

class StipulationType (field_types.String_Type) :
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
    ENUM_MINIMUM_DENOMINATION = 'MINDNOM'
    ENUM_MINIMUM_INCREMENT = 'MININCR'
    ENUM_MINIMUM_QUANTITY = 'MINQTY'
    ENUM_PAYMENT_FREQUENCY = 'PAYFREQ'
    ENUM_NUMBER_OF_PIECES = 'PIECES'
    ENUM_POOLS_MAXIMUM = 'PMAX'
    ENUM_POOLS_PER_LOT = 'PPL'
    ENUM_POOLS_PER_MILLION = 'PPM'
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
    ENUM_AVERAGE_FICO_SCORE = 'AVFICO'
    ENUM_AVERAGE_LOAN_SIZE = 'AVSIZE'
    ENUM_MAXIMUM_LOAN_BALANCE = 'MAXBAL'
    ENUM_POOL_IDENTIFIER = 'POOL'
    ENUM_TYPE_OF_ROLL_TRADE = 'ROLLTYPE'
    ENUM_REFERENCE_TO_ROLLING_OR_CLOSING_TRADE = 'REFTRADE'
    ENUM_PRINCIPAL_OF_ROLLING_OR_CLOSING_TRADE = 'REFPRIN'
    ENUM_INTEREST_OF_ROLLING_OR_CLOSING_TRADE = 'REFINT'
    ENUM_AVAILABLE_OFFER_QUANTITY_TO_BE_SHOWN_TO_THE_STREET = 'AVAILQTY'
    ENUM_BROKER_CREDIT = 'BROKERCREDIT'
    ENUM_OFFER_PRICE_TO_BE_SHOWN_TO_INTERNAL_BROKERS = 'INTERNALPX'
    ENUM_OFFER_QUANTITY_TO_BE_SHOWN_TO_INTERNAL_BROKERS = 'INTERNALQTY'
    ENUM_THE_MINIMUM_RESIDUAL_OFFER_QUANTITY = 'LEAVEQTY'
    ENUM_MAXIMUM_ORDER_SIZE = 'MAXORDQTY'
    ENUM_ORDER_QUANTITY_INCREMENT = 'ORDRINCR'
    ENUM_PRIMARY_OR_SECONDARY_MARKET_INDICATOR = 'PRIMARY'
    ENUM_BROKER_SALES_CREDIT_OVERRIDE = 'SALESCREDITOVR'
    ENUM_TRADER_CREDIT = 'TRADERCREDIT'
    ENUM_DISCOUNT_RATE = 'DISCOUNT'
    ENUM_YIELD_TO_MATURITY = 'YTM'
    ENUM_ABSOLUTE_PREPAYMENT_SPEED = 'ABS'
    ENUM_CONSTANT_PREPAYMENT_PENALTY = 'CPP'
    ENUM_CONSTANT_PREPAYMENT_RATE = 'CPR'
    ENUM_CONSTANT_PREPAYMENT_YIELD = 'CPY'
    ENUM_FINAL_CPR_OF_HOME_EQUITY_PREPAYMENT_CURVE = 'HEP'
    ENUM_PERCENT_OF_MANUFACTURED_HOUSING_PREPAYMENT_CURVE = 'MHP'
    ENUM_MONTHLY_PREPAYMENT_RATE = 'MPR'
    ENUM_PERCENT_OF_PROSPECTUS_PREPAYMENT_CURVE = 'PPC'
    ENUM_PERCENT_OF_BMA_PREPAYMENT_CURVE = 'PSA'
    ENUM_SINGLE_MONTHLY_MORTALITY = 'SMM'

class StipulationValue (field_types.String_Type) :
    _tag = '234'

class YieldType (field_types.String_Type) :
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
    ENUM_GVNT_EQUIVALENT_YIELD = 'GOVTEQUIV'
    ENUM_TRUE_GROSS_YIELD = 'GROSS'
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
    ENUM_PREVIOUS_CLOSE_YIELD = 'PREVCLOSE'
    ENUM_PROCEEDS_YIELD = 'PROCEEDS'
    ENUM_YIELD_TO_NEXT_PUT = 'PUT'
    ENUM_SEMI_ANNUAL_YIELD = 'SEMIANNUAL'
    ENUM_YIELD_TO_SHORTEST_AVERAGE_LIFE = 'SHORTAVGLIFE'
    ENUM_SIMPLE_YIELD = 'SIMPLE'
    ENUM_TAX_EQUIVALENT_YIELD = 'TAXEQUIV'
    ENUM_YIELD_TO_TENDER_DATE = 'TENDER'
    ENUM_TRUE_YIELD = 'TRUE'
    ENUM_YIELD_VALUE_OF32NDS = 'VALUE1_32'
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

class TradedFlatSwitch (field_types.Boolean_Type) :
    _tag = '258'
    ENUM_NOT_TRADED_FLAT = 'N'
    ENUM_TRADED_FLAT = 'Y'

class BasisFeatureDate (field_types.LocalMktDate_Type) :
    _tag = '259'

class BasisFeaturePrice (field_types.Price_Type) :
    _tag = '260'

class MDReqID (field_types.String_Type) :
    _tag = '262'

class SubscriptionRequestType (field_types.char_Type) :
    _tag = '263'
    ENUM_SNAPSHOT = '0'
    ENUM_SNAPSHOT_AND_UPDATES = '1'
    ENUM_DISABLE_PREVIOUS_SNAPSHOT = '2'

class MarketDepth (field_types.int_Type) :
    _tag = '264'

class MDUpdateType (field_types.int_Type) :
    _tag = '265'
    ENUM_FULL_REFRESH = 0
    ENUM_INCREMENTAL_REFRESH = 1

class AggregatedBook (field_types.Boolean_Type) :
    _tag = '266'
    ENUM_BOOK_ENTRIES_TO_BE_AGGREGATED = 'Y'
    ENUM_BOOK_ENTRIES_SHOULD_NOT_BE_AGGREGATED = 'N'

class NoMDEntryTypes (field_types.NumInGroup_Type) :
    _tag = '267'

class NoMDEntries (field_types.NumInGroup_Type) :
    _tag = '268'

class MDEntryType (field_types.char_Type) :
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
    ENUM_COMPOSITE_UNDERLYING_PRICE = 'D'
    ENUM_SIMULATED_SELL_PRICE = 'E'
    ENUM_SIMULATED_BUY_PRICE = 'F'
    ENUM_MARGIN_RATE = 'G'
    ENUM_MID_PRICE = 'H'
    ENUM_EMPTY_BOOK = 'J'
    ENUM_SETTLE_HIGH_PRICE = 'K'
    ENUM_SETTLE_LOW_PRICE = 'L'
    ENUM_PRIOR_SETTLE_PRICE = 'M'
    ENUM_SESSION_HIGH_BID = 'N'
    ENUM_SESSION_LOW_OFFER = 'O'
    ENUM_EARLY_PRICES = 'P'
    ENUM_AUCTION_CLEARING_PRICE = 'Q'
    ENUM_SWAP_VALUE_FACTOR = 'S'
    ENUM_DAILY_VALUE_ADJUSTMENT_FOR_LONG_POSITIONS = 'R'
    ENUM_CUMULATIVE_VALUE_ADJUSTMENT_FOR_LONG_POSITIONS = 'T'
    ENUM_DAILY_VALUE_ADJUSTMENT_FOR_SHORT_POSITIONS = 'U'
    ENUM_CUMULATIVE_VALUE_ADJUSTMENT_FOR_SHORT_POSITIONS = 'V'

class MDEntryPx (field_types.Price_Type) :
    _tag = '270'

class MDEntrySize (field_types.Qty_Type) :
    _tag = '271'

class MDEntryDate (field_types.UTCDateOnly_Type) :
    _tag = '272'

class MDEntryTime (field_types.UTCTimeOnly_Type) :
    _tag = '273'

class TickDirection (field_types.char_Type) :
    _tag = '274'
    ENUM_PLUS_TICK = '0'
    ENUM_ZERO_PLUS_TICK = '1'
    ENUM_MINUS_TICK = '2'
    ENUM_ZERO_MINUS_TICK = '3'

class MDMkt (field_types.Exchange_Type) :
    _tag = '275'

class QuoteCondition (field_types.MultipleStringValue_Type) :
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
    ENUM_MANUAL = 'L'
    ENUM_OUTRIGHT_PRICE = 'J'
    ENUM_IMPLIED_PRICE = 'K'
    ENUM_DEPTH_ON_OFFER = 'M'
    ENUM_DEPTH_ON_BID = 'N'
    ENUM_CLOSING = 'O'
    ENUM_NEWS_DISSEMINATION = 'P'
    ENUM_TRADING_RANGE = 'Q'
    ENUM_ORDER_INFLUX = 'R'
    ENUM_DUE_TO_RELATED = 'S'
    ENUM_NEWS_PENDING = 'T'
    ENUM_ADDITIONAL_INFO = 'U'
    ENUM_ADDITIONAL_INFO_DUE_TO_RELATED = 'V'
    ENUM_RESUME = 'W'
    ENUM_VIEW_OF_COMMON = 'X'
    ENUM_VOLUME_ALERT = 'Y'
    ENUM_ORDER_IMBALANCE = 'Z'
    ENUM_EQUIPMENT_CHANGEOVER = 'a'
    ENUM_NO_OPEN = 'b'
    ENUM_REGULAR_ETH = 'c'
    ENUM_AUTOMATIC_EXECUTION = 'd'
    ENUM_AUTOMATIC_EXECUTION_ETH = 'e'
    ENUM_FAST_MARKET_ETH = 'f '
    ENUM_INACTIVE_ETH = 'g'
    ENUM_ROTATION = 'h'
    ENUM_ROTATION_ETH = 'i'
    ENUM_HALT = 'j'
    ENUM_HALT_ETH = 'k'
    ENUM_DUE_TO_NEWS_DISSEMINATION = 'l'
    ENUM_DUE_TO_NEWS_PENDING = 'm'
    ENUM_TRADING_RESUME = 'n'
    ENUM_OUT_OF_SEQUENCE = 'o'
    ENUM_BID_SPECIALIST = 'p'
    ENUM_OFFER_SPECIALIST = 'q'
    ENUM_BID_OFFER_SPECIALIST = 'r'
    ENUM_END_OF_DAY_SAM = 's'
    ENUM_FORBIDDEN_SAM = 't'
    ENUM_FROZEN_SAM = 'u'
    ENUM_PRE_OPENING_SAM = 'v'
    ENUM_OPENING_SAM = 'w'
    ENUM_OPEN_SAM = 'x'
    ENUM_SURVEILLANCE_SAM = 'y'
    ENUM_SUSPENDED_SAM = 'z'
    ENUM_RESERVED_SAM = '0'
    ENUM_NO_ACTIVE_SAM = '1'
    ENUM_RESTRICTED = '2'
    ENUM_REST_OF_BOOK_VWAP = '3'
    ENUM_BETTER_PRICES_IN_CONDITIONAL_ORDERS = '4'
    ENUM_MEDIAN_PRICE = '5'

class TradeCondition (field_types.MultipleStringValue_Type) :
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
    ENUM_BARGAIN_CONDITION = 'S'
    ENUM_CONVERTED_PRICE_INDICATOR = 'T'
    ENUM_EXCHANGE_LAST = 'U'
    ENUM_FINAL_PRICE_OF_SESSION = 'V'
    ENUM_EX_PIT = 'W'
    ENUM_CROSSED = 'X'
    ENUM_TRADES_RESULTING_FROM_MANUAL = 'Y'
    ENUM_TRADES_RESULTING_FROM_INTERMARKET_SWEEP = 'Z'
    ENUM_VOLUME_ONLY = 'a'
    ENUM_DIRECT_PLUS = 'b'
    ENUM_ACQUISITION = 'c'
    ENUM_BUNCHED = 'd'
    ENUM_DISTRIBUTION = 'e'
    ENUM_BUNCHED_SALE = 'f'
    ENUM_SPLIT_TRADE = 'g'
    ENUM_CANCEL_STOPPED = 'h'
    ENUM_CANCEL_ETH = 'i'
    ENUM_CANCEL_STOPPED_ETH = 'j'
    ENUM_OUT_OF_SEQUENCE_ETH = 'k'
    ENUM_CANCEL_LAST_ETH = 'l'
    ENUM_SOLD_LAST_SALE_ETH = 'm'
    ENUM_CANCEL_LAST = 'n'
    ENUM_SOLD_LAST_SALE = 'o'
    ENUM_CANCEL_OPEN = 'p'
    ENUM_CANCEL_OPEN_ETH = 'q'
    ENUM_OPENED_SALE_ETH = 'r'
    ENUM_CANCEL_ONLY = 's'
    ENUM_CANCEL_ONLY_ETH = 't'
    ENUM_LATE_OPEN_ETH = 'u'
    ENUM_AUTO_EXECUTION_ETH = 'v'
    ENUM_REOPEN = 'w'
    ENUM_REOPEN_ETH = 'x'
    ENUM_ADJUSTED = 'y'
    ENUM_ADJUSTED_ETH = 'z'
    ENUM_SPREAD = 'AA'
    ENUM_SPREAD_ETH = 'AB'
    ENUM_STRADDLE = 'AC'
    ENUM_STRADDLE_ETH = 'AD'
    ENUM_STOPPED = 'AE'
    ENUM_STOPPED_ETH = 'AF'
    ENUM_REGULAR_ETH = 'AG'
    ENUM_COMBO = 'AH'
    ENUM_COMBO_ETH = 'AI'
    ENUM_OFFICIAL_CLOSING_PRICE = 'AJ'
    ENUM_PRIOR_REFERENCE_PRICE = 'AK'
    ENUM_CANCEL = '0'
    ENUM_STOPPED_SOLD_LAST = 'AL'
    ENUM_STOPPED_OUT_OF_SEQUENCE = 'AM'
    ENUM_OFFICAL_CLOSING_PRICE = 'AN'
    ENUM_CROSSED_OLD = 'AO'
    ENUM_FAST_MARKET = 'AP'
    ENUM_AUTOMATIC_EXECUTION = 'AQ'
    ENUM_FORM_T = 'AR'
    ENUM_BASKET_INDEX = 'AS'
    ENUM_BURST_BASKET = 'AT'
    ENUM_OUTSIDE_SPREAD = 'AV'
    ENUM_IMPLIED_TRADE = '1'
    ENUM_MARKETPLACE_ENTERED_TRADE = '2'
    ENUM_MULT_ASSET_CLASS_MULTILEG_TRADE = '3'
    ENUM_MULTILEG_TO_MULTILEG_TRADE = '4'

class MDEntryID (field_types.String_Type) :
    _tag = '278'

class MDUpdateAction (field_types.char_Type) :
    _tag = '279'
    ENUM_NEW = '0'
    ENUM_CHANGE = '1'
    ENUM_DELETE = '2'
    ENUM_DELETE_THRU = '3'
    ENUM_DELETE_FROM = '4'
    ENUM_OVERLAY = '5'

class MDEntryRefID (field_types.String_Type) :
    _tag = '280'

class MDReqRejReason (field_types.char_Type) :
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
    ENUM_INSUFFICIENT_CREDIT = 'D'

class MDEntryOriginator (field_types.String_Type) :
    _tag = '282'

class LocationID (field_types.String_Type) :
    _tag = '283'

class DeskID (field_types.String_Type) :
    _tag = '284'

class DeleteReason (field_types.char_Type) :
    _tag = '285'
    ENUM_CANCELLATION = '0'
    ENUM_ERROR = '1'

class OpenCloseSettlFlag (field_types.MultipleCharValue_Type) :
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

class FinancialStatus (field_types.MultipleCharValue_Type) :
    _tag = '291'
    ENUM_BANKRUPT = '1'
    ENUM_PENDING_DELISTING = '2'
    ENUM_RESTRICTED = '3'

class CorporateAction (field_types.MultipleCharValue_Type) :
    _tag = '292'
    ENUM_EX_DIVIDEND = 'A'
    ENUM_EX_DISTRIBUTION = 'B'
    ENUM_EX_RIGHTS = 'C'
    ENUM_NEW = 'D'
    ENUM_EX_INTEREST = 'E'
    ENUM_CASH_DIVIDEND = 'F'
    ENUM_STOCK_DIVIDEND = 'G'
    ENUM_NON_INTEGER_STOCK_SPLIT = 'H'
    ENUM_REVERSE_STOCK_SPLIT = 'I'
    ENUM_STANDARD_INTEGER_STOCK_SPLIT = 'J'
    ENUM_POSITION_CONSOLIDATION = 'K'
    ENUM_LIQUIDATION_REORGANIZATION = 'L'
    ENUM_MERGER_REORGANIZATION = 'M'
    ENUM_RIGHTS_OFFERING = 'N'
    ENUM_SHAREHOLDER_MEETING = 'O'
    ENUM_SPINOFF = 'P'
    ENUM_TENDER_OFFER = 'Q'
    ENUM_WARRANT = 'R'
    ENUM_SPECIAL_ACTION = 'S'
    ENUM_SYMBOL_CONVERSION = 'T'
    ENUM_CUSIP = 'U'
    ENUM_LEAP_ROLLOVER = 'V'
    ENUM_SUCCESSION_EVENT = 'W'

class DefBidSize (field_types.Qty_Type) :
    _tag = '293'

class DefOfferSize (field_types.Qty_Type) :
    _tag = '294'

class NoQuoteEntries (field_types.NumInGroup_Type) :
    _tag = '295'

class NoQuoteSets (field_types.NumInGroup_Type) :
    _tag = '296'

class QuoteStatus (field_types.int_Type) :
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
    ENUM_ACTIVE = 16
    ENUM_CANCELED = 17
    ENUM_UNSOLICITED_QUOTE_REPLENISHMENT = 18
    ENUM_PENDING_END_TRADE = 19
    ENUM_TOO_LATE_TO_END = 20

class QuoteCancelType (field_types.int_Type) :
    _tag = '298'
    ENUM_CANCEL_FOR_ONE_OR_MORE_SECURITIES = 1
    ENUM_CANCEL_FOR_SECURITY_TYPE = 2
    ENUM_CANCEL_FOR_UNDERLYING_SECURITY = 3
    ENUM_CANCEL_ALL_QUOTES = 4
    ENUM_CANCEL_QUOTE_SPECIFIED_IN_QUOTE_ID = 5

class QuoteEntryID (field_types.String_Type) :
    _tag = '299'

class QuoteRejectReason (field_types.int_Type) :
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
    ENUM_PRICE_EXCEEDS_CURRENT_PRICE_BAND = 10
    ENUM_QUOTE_LOCKED = 11
    ENUM_OTHER = 99

class QuoteResponseLevel (field_types.int_Type) :
    _tag = '301'
    ENUM_NO_ACKNOWLEDGEMENT = 0
    ENUM_ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES = 1
    ENUM_ACKNOWLEDGE_EACH_QUOTE_MESSAGE = 2
    ENUM_SUMMARY_ACKNOWLEDGEMENT = 3

class QuoteSetID (field_types.String_Type) :
    _tag = '302'

class QuoteRequestType (field_types.int_Type) :
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

class SecurityRequestType (field_types.int_Type) :
    _tag = '321'
    ENUM_REQUEST_SECURITY_IDENTITY_AND_SPECIFICATIONS = 0
    ENUM_REQUEST_SECURITY_IDENTITY_FOR_SPECIFICATIONS = 1
    ENUM_REQUEST_LIST_SECURITY_TYPES = 2
    ENUM_REQUEST_LIST_SECURITIES = 3
    ENUM_SYMBOL = 4
    ENUM_SECURITY_TYPE_AND_OR_CFI_CODE = 5
    ENUM_PRODUCT = 6
    ENUM_TRADING_SESSION_ID = 7
    ENUM_ALL_SECURITIES = 8
    ENUM_MARKET_ID_OR_MARKET_ID = 9

class SecurityResponseID (field_types.String_Type) :
    _tag = '322'

class SecurityResponseType (field_types.int_Type) :
    _tag = '323'
    ENUM_ACCEPT_AS_IS = 1
    ENUM_ACCEPT_WITH_REVISIONS = 2
    ENUM_LIST_OF_SECURITY_TYPES_RETURNED_PER_REQUEST = 3
    ENUM_LIST_OF_SECURITIES_RETURNED_PER_REQUEST = 4
    ENUM_REJECT_SECURITY_PROPOSAL = 5
    ENUM_CANNOT_MATCH_SELECTION_CRITERIA = 6

class SecurityStatusReqID (field_types.String_Type) :
    _tag = '324'

class UnsolicitedIndicator (field_types.Boolean_Type) :
    _tag = '325'
    ENUM_MESSAGE_IS_BEING_SENT_AS_A_RESULT_OF_A_PRIOR_REQUEST = 'N'
    ENUM_MESSAGE_IS_BEING_SENT_UNSOLICITED = 'Y'

class SecurityTradingStatus (field_types.int_Type) :
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
    ENUM_PRE_CROSS = 24
    ENUM_CROSS = 25

class HaltReason (field_types.char_Type) :
    _tag = '327'
    ENUM_NEWS_DISSEMINATION = 'D'
    ENUM_ORDER_INFLUX = 'E'
    ENUM_ORDER_IMBALANCE = 'I'
    ENUM_ADDITIONAL_INFORMATION = 'M'
    ENUM_NEW_PENDING = 'P'
    ENUM_EQUIPMENT_CHANGEOVER = 'X'

class InViewOfCommon (field_types.Boolean_Type) :
    _tag = '328'
    ENUM_HALT_WAS_NOT_RELATED_TO_A_HALT_OF_THE_COMMON_STOCK = 'N'
    ENUM_HALT_WAS_DUE_TO_COMMON_STOCK_BEING_HALTED = 'Y'

class DueToRelated (field_types.Boolean_Type) :
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

class Adjustment (field_types.int_Type) :
    _tag = '334'
    ENUM_CANCEL = 1
    ENUM_ERROR = 2
    ENUM_CORRECTION = 3

class TradSesReqID (field_types.String_Type) :
    _tag = '335'

class TradingSessionID (field_types.String_Type) :
    _tag = '336'
    ENUM_DAY = '1'
    ENUM_HALF_DAY = '2'
    ENUM_MORNING = '3'
    ENUM_AFTERNOON = '4'
    ENUM_EVENING = '5'
    ENUM_AFTER_HOURS = '6'

class ContraTrader (field_types.String_Type) :
    _tag = '337'

class TradSesMethod (field_types.int_Type) :
    _tag = '338'
    ENUM_ELECTRONIC = 1
    ENUM_OPEN_OUTCRY = 2
    ENUM_TWO_PARTY = 3

class TradSesMode (field_types.int_Type) :
    _tag = '339'
    ENUM_TESTING = 1
    ENUM_SIMULATED = 2
    ENUM_PRODUCTION = 3

class TradSesStatus (field_types.int_Type) :
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

class MessageEncoding (field_types.String_Type) :
    _tag = '347'

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

class SessionRejectReason (field_types.int_Type) :
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
    ENUM_INVALID = 18
    ENUM_OTHER = 99

class BidRequestTransType (field_types.char_Type) :
    _tag = '374'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'

class ContraBroker (field_types.String_Type) :
    _tag = '375'

class ComplianceID (field_types.String_Type) :
    _tag = '376'

class SolicitedFlag (field_types.Boolean_Type) :
    _tag = '377'
    ENUM_WAS_NOT_SOLICITED = 'N'
    ENUM_WAS_SOLICITED = 'Y'

class ExecRestatementReason (field_types.int_Type) :
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
    ENUM_PEG_REFRESH = 11
    ENUM_OTHER = 99

class BusinessRejectRefID (field_types.String_Type) :
    _tag = '379'

class BusinessRejectReason (field_types.int_Type) :
    _tag = '380'
    ENUM_OTHER = 0
    ENUM_UNKNOWN_ID = 1
    ENUM_UNKNOWN_SECURITY = 2
    ENUM_UNSUPPORTED_MESSAGE_TYPE = 3
    ENUM_APPLICATION_NOT_AVAILABLE = 4
    ENUM_CONDITIONALLY_REQUIRED_FIELD_MISSING = 5
    ENUM_NOT_AUTHORIZED = 6
    ENUM_DELIVER_TO_FIRM_NOT_AVAILABLE_AT_THIS_TIME = 7
    ENUM_INVALID_PRICE_INCREMENT = 18

class GrossTradeAmt (field_types.Amt_Type) :
    _tag = '381'

class NoContraBrokers (field_types.NumInGroup_Type) :
    _tag = '382'

class MaxMessageSize (field_types.Length_Type) :
    _tag = '383'

class NoMsgTypes (field_types.NumInGroup_Type) :
    _tag = '384'

class MsgDirection (field_types.char_Type) :
    _tag = '385'
    ENUM_RECEIVE = 'R'
    ENUM_SEND = 'S'

class NoTradingSessions (field_types.NumInGroup_Type) :
    _tag = '386'

class TotalVolumeTraded (field_types.Qty_Type) :
    _tag = '387'

class DiscretionInst (field_types.char_Type) :
    _tag = '388'
    ENUM_RELATED_TO_DISPLAYED_PRICE = '0'
    ENUM_RELATED_TO_MARKET_PRICE = '1'
    ENUM_RELATED_TO_PRIMARY_PRICE = '2'
    ENUM_RELATED_TO_LOCAL_PRIMARY_PRICE = '3'
    ENUM_RELATED_TO_MIDPOINT_PRICE = '4'
    ENUM_RELATED_TO_LAST_TRADE_PRICE = '5'
    ENUM_RELATED_TO_VWAP = '6'
    ENUM_AVERAGE_PRICE_GUARANTEE = '7'

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

class BidType (field_types.int_Type) :
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

class BidDescriptorType (field_types.int_Type) :
    _tag = '399'
    ENUM_SECTOR = 1
    ENUM_COUNTRY = 2
    ENUM_INDEX = 3

class BidDescriptor (field_types.String_Type) :
    _tag = '400'

class SideValueInd (field_types.int_Type) :
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

class LiquidityIndType (field_types.int_Type) :
    _tag = '409'
    ENUM_FIVE_DAY_MOVING_AVERAGE = 1
    ENUM_TWENTY_DAY_MOVING_AVERAGE = 2
    ENUM_NORMAL_MARKET_SIZE = 3
    ENUM_OTHER = 4

class WtAverageLiquidity (field_types.Percentage_Type) :
    _tag = '410'

class ExchangeForPhysical (field_types.Boolean_Type) :
    _tag = '411'
    ENUM_FALSE = 'N'
    ENUM_TRUE = 'Y'

class OutMainCntryUIndex (field_types.Amt_Type) :
    _tag = '412'

class CrossPercent (field_types.Percentage_Type) :
    _tag = '413'

class ProgRptReqs (field_types.int_Type) :
    _tag = '414'
    ENUM_BUY_SIDE_REQUESTS = 1
    ENUM_SELL_SIDE_SENDS = 2
    ENUM_REAL_TIME_EXECUTION_REPORTS = 3

class ProgPeriodInterval (field_types.int_Type) :
    _tag = '415'

class IncTaxInd (field_types.int_Type) :
    _tag = '416'
    ENUM_NET = 1
    ENUM_GROSS = 2

class NumBidders (field_types.int_Type) :
    _tag = '417'

class BidTradeType (field_types.char_Type) :
    _tag = '418'
    ENUM_AGENCY = 'A'
    ENUM_VWAP_GUARANTEE = 'G'
    ENUM_GUARANTEED_CLOSE = 'J'
    ENUM_RISK_TRADE = 'R'

class BasisPxType (field_types.char_Type) :
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

class PriceType (field_types.int_Type) :
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
    ENUM_PRODUCT_TICKS_IN_HALFS = 13
    ENUM_PRODUCT_TICKS_IN_FOURTHS = 14
    ENUM_PRODUCT_TICKS_IN_EIGHTS = 15
    ENUM_PRODUCT_TICKS_IN_SIXTEENTHS = 16
    ENUM_PRODUCT_TICKS_IN_THIRTY_SECONDS = 17
    ENUM_PRODUCT_TICKS_IN_SIXTY_FORTHS = 18
    ENUM_PRODUCT_TICKS_IN_ONE_TWENTY_EIGHTS = 19

class DayOrderQty (field_types.Qty_Type) :
    _tag = '424'

class DayCumQty (field_types.Qty_Type) :
    _tag = '425'

class DayAvgPx (field_types.Price_Type) :
    _tag = '426'

class GTBookingInst (field_types.int_Type) :
    _tag = '427'
    ENUM_BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION = 0
    ENUM_ACCUMULATE_UNTIL_FILLED_OR_EXPIRED = 1
    ENUM_ACCUMULATE_UNTIL_VERBALLY_NOTIFIED_OTHERWISE = 2

class NoStrikes (field_types.NumInGroup_Type) :
    _tag = '428'

class ListStatusType (field_types.int_Type) :
    _tag = '429'
    ENUM_ACK = 1
    ENUM_RESPONSE = 2
    ENUM_TIMED = 3
    ENUM_EXEC_STARTED = 4
    ENUM_ALL_DONE = 5
    ENUM_ALERT = 6

class NetGrossInd (field_types.int_Type) :
    _tag = '430'
    ENUM_NET = 1
    ENUM_GROSS = 2

class ListOrderStatus (field_types.int_Type) :
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

class ListExecInstType (field_types.char_Type) :
    _tag = '433'
    ENUM_IMMEDIATE = '1'
    ENUM_WAIT_FOR_INSTRUCTION = '2'
    ENUM_SELL_DRIVEN = '3'
    ENUM_BUY_DRIVEN_CASH_TOP_UP = '4'
    ENUM_BUY_DRIVEN_CASH_WITHDRAW = '5'

class CxlRejResponseTo (field_types.char_Type) :
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

class MultiLegReportingType (field_types.char_Type) :
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

class PartyIDSource (field_types.char_Type) :
    _tag = '447'
    ENUM_UK_NATIONAL_INSURANCE_OR_PENSION_NUMBER = '6'
    ENUM_US_SOCIAL_SECURITY_NUMBER = '7'
    ENUM_US_EMPLOYER_OR_TAX_ID_NUMBER = '8'
    ENUM_AUSTRALIAN_BUSINESS_NUMBER = '9'
    ENUM_AUSTRALIAN_TAX_FILE_NUMBER = 'A'
    ENUM_KOREAN_INVESTOR_ID = '1'
    ENUM_TAIWANESE_FOREIGN_INVESTOR_ID = '2'
    ENUM_TAIWANESE_TRADING_ACCT = '3'
    ENUM_MALAYSIAN_CENTRAL_DEPOSITORY = '4'
    ENUM_CHINESE_INVESTOR_ID = '5'
    ENUM_ISITC_ACRONYM = 'I'
    ENUM_BIC = 'B'
    ENUM_GENERAL_IDENTIFIER = 'C'
    ENUM_PROPRIETARY = 'D'
    ENUM_ISO_COUNTRY_CODE = 'E'
    ENUM_SETTLEMENT_ENTITY_LOCATION = 'F'
    ENUM_MIC = 'G'
    ENUM_CSD_PARTICIPANT = 'H'

class PartyID (field_types.String_Type) :
    _tag = '448'

class NetChgPrevDay (field_types.PriceOffset_Type) :
    _tag = '451'

class PartyRole (field_types.int_Type) :
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
    ENUM_CONTRA_INVESTOR_ID = 39
    ENUM_TRANSFER_TO_FIRM = 40
    ENUM_CONTRA_POSITION_ACCOUNT = 41
    ENUM_CONTRA_EXCHANGE = 42
    ENUM_INTERNAL_CARRY_ACCOUNT = 43
    ENUM_ORDER_ENTRY_OPERATOR_ID = 44
    ENUM_SECONDARY_ACCOUNT_NUMBER = 45
    ENUM_FOREIGN_FIRM = 46
    ENUM_THIRD_PARTY_ALLOCATION_FIRM = 47
    ENUM_CLAIMING_ACCOUNT = 48
    ENUM_ASSET_MANAGER = 49
    ENUM_PLEDGOR_ACCOUNT = 50
    ENUM_PLEDGEE_ACCOUNT = 51
    ENUM_LARGE_TRADER_REPORTABLE_ACCOUNT = 52
    ENUM_TRADER_MNEMONIC = 53
    ENUM_SENDER_LOCATION = 54
    ENUM_SESSION_ID = 55
    ENUM_ACCEPTABLE_COUNTERPARTY = 56
    ENUM_UNACCEPTABLE_COUNTERPARTY = 57
    ENUM_ENTERING_UNIT = 58
    ENUM_EXECUTING_UNIT = 59
    ENUM_INTRODUCING_BROKER = 60
    ENUM_QUOTE_ORIGINATOR = 61
    ENUM_REPORT_ORIGINATOR = 62
    ENUM_SYSTEMATIC_INTERNALISER = 63
    ENUM_MULTILATERAL_TRADING_FACILITY = 64
    ENUM_REGULATED_MARKET = 65
    ENUM_MARKET_MAKER = 66
    ENUM_INVESTMENT_FIRM = 67
    ENUM_HOST_COMPETENT_AUTHORITY = 68
    ENUM_HOME_COMPETENT_AUTHORITY = 69
    ENUM_COMPETENT_AUTHORITY_LIQUIDITY = 70
    ENUM_COMPETENT_AUTHORITY_TRANSACTION_VENUE = 71
    ENUM_REPORTING_INTERMEDIARY = 72
    ENUM_EXECUTION_VENUE = 73
    ENUM_MARKET_DATA_ENTRY_ORIGINATOR = 74
    ENUM_LOCATION_ID = 75
    ENUM_DESK_ID = 76
    ENUM_MARKET_DATA_MARKET = 77
    ENUM_ALLOCATION_ENTITY = 78
    ENUM_PRIME_BROKER = 79
    ENUM_STEP_OUT_FIRM = 80
    ENUM_BROKER_CLEARING_ID = 81

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

class Product (field_types.int_Type) :
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

class TestMessageIndicator (field_types.Boolean_Type) :
    _tag = '464'
    ENUM_FALES = 'N'
    ENUM_TRUE = 'Y'

class BookingRefID (field_types.String_Type) :
    _tag = '466'

class IndividualAllocID (field_types.String_Type) :
    _tag = '467'

class RoundingDirection (field_types.char_Type) :
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

class CancellationRights (field_types.char_Type) :
    _tag = '480'
    ENUM_YES = 'Y'
    ENUM_NO_EXECUTION_ONLY = 'N'
    ENUM_NO_WAIVER_AGREEMENT = 'M'
    ENUM_NO_INSTITUTIONAL = 'O'

class MoneyLaunderingStatus (field_types.char_Type) :
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

class ExecPriceType (field_types.char_Type) :
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
    ENUM_NEW = 0
    ENUM_CANCEL = 1
    ENUM_REPLACE = 2
    ENUM_RELEASE = 3
    ENUM_REVERSE = 4
    ENUM_CANCEL_DUE_TO_BACK_OUT_OF_TRADE = 5

class CardHolderName (field_types.String_Type) :
    _tag = '488'

class CardNumber (field_types.String_Type) :
    _tag = '489'

class CardExpDate (field_types.LocalMktDate_Type) :
    _tag = '490'

class CardIssNum (field_types.String_Type) :
    _tag = '491'

class PaymentMethod (field_types.int_Type) :
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

class TaxAdvantageType (field_types.int_Type) :
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
    ENUM_OTHER = 999

class RegistRejReasonText (field_types.String_Type) :
    _tag = '496'

class FundRenewWaiv (field_types.char_Type) :
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

class CashDistribAgentAcctName (field_types.String_Type) :
    _tag = '502'

class CardStartDate (field_types.LocalMktDate_Type) :
    _tag = '503'

class PaymentDate (field_types.LocalMktDate_Type) :
    _tag = '504'

class PaymentRemitterID (field_types.String_Type) :
    _tag = '505'

class RegistStatus (field_types.char_Type) :
    _tag = '506'
    ENUM_ACCEPTED = 'A'
    ENUM_REJECTED = 'R'
    ENUM_HELD = 'H'
    ENUM_REMINDER = 'N'

class RegistRejReasonCode (field_types.int_Type) :
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

class RegistTransType (field_types.char_Type) :
    _tag = '514'
    ENUM_NEW = '0'
    ENUM_CANCEL = '2'
    ENUM_REPLACE = '1'

class ExecValuationPoint (field_types.UTCTimestamp_Type) :
    _tag = '515'

class OrderPercent (field_types.Percentage_Type) :
    _tag = '516'

class OwnershipType (field_types.char_Type) :
    _tag = '517'
    ENUM_JOINT_INVESTORS = 'J'
    ENUM_TENANTS_IN_COMMON = 'T'
    ENUM_JOINT_TRUSTEES = '2'

class NoContAmts (field_types.NumInGroup_Type) :
    _tag = '518'

class ContAmtType (field_types.int_Type) :
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

class OwnerType (field_types.int_Type) :
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

class OrderCapacity (field_types.char_Type) :
    _tag = '528'
    ENUM_AGENCY = 'A'
    ENUM_PROPRIETARY = 'G'
    ENUM_INDIVIDUAL = 'I'
    ENUM_PRINCIPAL = 'P'
    ENUM_RISKLESS_PRINCIPAL = 'R'
    ENUM_AGENT_FOR_OTHER_MEMBER = 'W'

class OrderRestrictions (field_types.MultipleCharValue_Type) :
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
    ENUM_ISSUER_HOLDING = 'B'
    ENUM_ISSUE_PRICE_STABILIZATION = 'C'
    ENUM_NON_ALGORITHMIC = 'D'
    ENUM_ALGORITHMIC = 'E'

class MassCancelRequestType (field_types.char_Type) :
    _tag = '530'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY = '1'
    ENUM_CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    ENUM_CANCEL_ORDERS_FOR_A_PRODUCT = '3'
    ENUM_CANCEL_ORDERS_FOR_ACFI_CODE = '4'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY_TYPE = '5'
    ENUM_CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    ENUM_CANCEL_ALL_ORDERS = '7'
    ENUM_CANCEL_ORDERS_FOR_A_MARKET = '8'
    ENUM_CANCEL_ORDERS_FOR_A_MARKET_SEGMENT = '9'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY_GROUP = 'A'

class MassCancelResponse (field_types.char_Type) :
    _tag = '531'
    ENUM_CANCEL_REQUEST_REJECTED = '0'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY = '1'
    ENUM_CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    ENUM_CANCEL_ORDERS_FOR_A_PRODUCT = '3'
    ENUM_CANCEL_ORDERS_FOR_ACFI_CODE = '4'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY_TYPE = '5'
    ENUM_CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    ENUM_CANCEL_ALL_ORDERS = '7'
    ENUM_CANCEL_ORDERS_FOR_A_MARKET = '8'
    ENUM_CANCEL_ORDERS_FOR_A_MARKET_SEGMENT = '9'
    ENUM_CANCEL_ORDERS_FOR_A_SECURITY_GROUP = 'A'

class MassCancelRejectReason (field_types.int_Type) :
    _tag = '532'
    ENUM_MASS_CANCEL_NOT_SUPPORTED = 0
    ENUM_INVALID_OR_UNKNOWN_SECURITY = 1
    ENUM_INVALID_OR_UNKOWN_UNDERLYING_SECURITY = 2
    ENUM_INVALID_OR_UNKNOWN_PRODUCT = 3
    ENUM_INVALID_OR_UNKNOWN_CFI_CODE = 4
    ENUM_INVALID_OR_UNKNOWN_SECURITY_TYPE = 5
    ENUM_INVALID_OR_UNKNOWN_TRADING_SESSION = 6
    ENUM_INVALID_OR_UNKNOWN_MARKET = 7
    ENUM_INVALID_OR_UNKOWN_MARKET_SEGMENT = 8
    ENUM_INVALID_OR_UNKNOWN_SECURITY_GROUP = 9
    ENUM_OTHER = 99

class TotalAffectedOrders (field_types.int_Type) :
    _tag = '533'

class NoAffectedOrders (field_types.NumInGroup_Type) :
    _tag = '534'

class AffectedOrderID (field_types.String_Type) :
    _tag = '535'

class AffectedSecondaryOrderID (field_types.String_Type) :
    _tag = '536'

class QuoteType (field_types.int_Type) :
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

class CashMargin (field_types.char_Type) :
    _tag = '544'
    ENUM_CASH = '1'
    ENUM_MARGIN_OPEN = '2'
    ENUM_MARGIN_CLOSE = '3'

class NestedPartySubID (field_types.String_Type) :
    _tag = '545'

class Scope (field_types.MultipleCharValue_Type) :
    _tag = '546'
    ENUM_LOCAL_MARKET = '1'
    ENUM_NATIONAL = '2'
    ENUM_GLOBAL = '3'

class MDImplicitDelete (field_types.Boolean_Type) :
    _tag = '547'
    ENUM_NO = 'N'
    ENUM_YES = 'Y'

class CrossID (field_types.String_Type) :
    _tag = '548'

class CrossType (field_types.int_Type) :
    _tag = '549'
    ENUM_CROSS_AON = 1
    ENUM_CROSS_IOC = 2
    ENUM_CROSS_ONE_SIDE = 3
    ENUM_CROSS_SAME_PRICE = 4

class CrossPrioritization (field_types.int_Type) :
    _tag = '550'
    ENUM_NONE = 0
    ENUM_BUY_SIDE_IS_PRIORITIZED = 1
    ENUM_SELL_SIDE_IS_PRIORITIZED = 2

class OrigCrossID (field_types.String_Type) :
    _tag = '551'

class NoSides (field_types.NumInGroup_Type) :
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

class SecurityListRequestType (field_types.int_Type) :
    _tag = '559'
    ENUM_SYMBOL = 0
    ENUM_SECURITY_TYPE_AND = 1
    ENUM_PRODUCT = 2
    ENUM_TRADING_SESSION_ID = 3
    ENUM_ALL_SECURITIES = 4
    ENUM_MARKET_ID_OR_MARKET_ID = 5

class SecurityRequestResult (field_types.int_Type) :
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

class MultiLegRptTypeReq (field_types.int_Type) :
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

class TradSesStatusRejReason (field_types.int_Type) :
    _tag = '567'
    ENUM_UNKNOWN_OR_INVALID_TRADING_SESSION_ID = 1
    ENUM_OTHER = 99

class TradeRequestID (field_types.String_Type) :
    _tag = '568'

class TradeRequestType (field_types.int_Type) :
    _tag = '569'
    ENUM_ALL_TRADES = 0
    ENUM_MATCHED_TRADES_MATCHING_CRITERIA = 1
    ENUM_UNMATCHED_TRADES_THAT_MATCH_CRITERIA = 2
    ENUM_UNREPORTED_TRADES_THAT_MATCH_CRITERIA = 3
    ENUM_ADVISORIES_THAT_MATCH_CRITERIA = 4

class PreviouslyReported (field_types.Boolean_Type) :
    _tag = '570'
    ENUM_NOT_REPORTED_TO_COUNTERPARTY = 'N'
    ENUM_PERVIOUSLY_REPORTED_TO_COUNTERPARTY = 'Y'

class TradeReportID (field_types.String_Type) :
    _tag = '571'

class TradeReportRefID (field_types.String_Type) :
    _tag = '572'

class MatchStatus (field_types.char_Type) :
    _tag = '573'
    ENUM_COMPARED = '0'
    ENUM_UNCOMPARED = '1'
    ENUM_ADVISORY_OR_ALERT = '2'

class MatchType (field_types.String_Type) :
    _tag = '574'
    ENUM_ONE_PARTY_TRADE_REPORT = '1'
    ENUM_TWO_PARTY_TRADE_REPORT = '2'
    ENUM_CONFIRMED_TRADE_REPORT = '3'
    ENUM_AUTO_MATCH = '4'
    ENUM_CROSS_AUCTION = '5'
    ENUM_COUNTER_ORDER_SELECTION = '6'
    ENUM_CALL_AUCTION = '7'
    ENUM_ISSUING = '8'
    ENUM_ACT_ACCEPTED_TRADE = 'M3'
    ENUM_ACT_DEFAULT_TRADE = 'M4'
    ENUM_ACT_DEFAULT_AFTER_M2 = 'M5'
    ENUM_ACTM6_MATCH = 'M6'
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

class OddLot (field_types.Boolean_Type) :
    _tag = '575'
    ENUM_TREAT_AS_ROUND_LOT = 'N'
    ENUM_TREAT_AS_ODD_LOT = 'Y'

class NoClearingInstructions (field_types.NumInGroup_Type) :
    _tag = '576'

class ClearingInstruction (field_types.int_Type) :
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

class AccountType (field_types.int_Type) :
    _tag = '581'
    ENUM_CARRIED_CUSTOMER_SIDE = 1
    ENUM_CARRIED_NON_CUSTOMER_SIDE = 2
    ENUM_HOUSE_TRADER = 3
    ENUM_FLOOR_TRADER = 4
    ENUM_CARRIED_NON_CUSTOMER_SIDE_CROSS_MARGINED = 6
    ENUM_HOUSE_TRADER_CROSS_MARGINED = 7
    ENUM_JOINT_BACK_OFFICE_ACCOUNT = 8

class CustOrderCapacity (field_types.int_Type) :
    _tag = '582'
    ENUM_MEMBER_TRADING_FOR_THEIR_OWN_ACCOUNT = 1
    ENUM_CLEARING_FIRM_TRADING_FOR_ITS_PROPRIETARY_ACCOUNT = 2
    ENUM_MEMBER_TRADING_FOR_ANOTHER_MEMBER = 3
    ENUM_ALL_OTHER = 4

class ClOrdLinkID (field_types.String_Type) :
    _tag = '583'

class MassStatusReqID (field_types.String_Type) :
    _tag = '584'

class MassStatusReqType (field_types.int_Type) :
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

class DayBookingInst (field_types.char_Type) :
    _tag = '589'
    ENUM_AUTO = '0'
    ENUM_SPEAK_WITH_ORDER_INITIATOR_BEFORE_BOOKING = '1'
    ENUM_ACCUMULATE = '2'

class BookingUnit (field_types.char_Type) :
    _tag = '590'
    ENUM_EACH_PARTIAL_EXECUTION_IS_A_BOOKABLE_UNIT = '0'
    ENUM_AGGREGATE_PARTIAL_EXECUTIONS_ON_THIS_ORDER = '1'
    ENUM_AGGREGATE_EXECUTIONS_FOR_THIS_SYMBOL = '2'

class PreallocMethod (field_types.char_Type) :
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
    ENUM_PRE_TRADING = '1'
    ENUM_OPENING_OR_OPENING_AUCTION = '2'
    ENUM_CONTINUOUS = '3'
    ENUM_CLOSING_OR_CLOSING_AUCTION = '4'
    ENUM_POST_TRADING = '5'
    ENUM_INTRADAY_AUCTION = '6'
    ENUM_QUIESCENT = '7'

class AllocType (field_types.int_Type) :
    _tag = '626'
    ENUM_CALCULATED = 1
    ENUM_PRELIMINARY = 2
    ENUM_SELLSIDE_CALCULATED_USING_PRELIMINARY = 3
    ENUM_SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY = 4
    ENUM_READY_TO_BOOK = 5
    ENUM_BUYSIDE_READY_TO_BOOK = 6
    ENUM_WAREHOUSE_INSTRUCTION = 7
    ENUM_REQUEST_TO_INTERMEDIARY = 8
    ENUM_ACCEPT = 9
    ENUM_REJECT = 10
    ENUM_ACCEPT_PENDING = 11
    ENUM_INCOMPLETE_GROUP = 12
    ENUM_COMPLETE_GROUP = 13
    ENUM_REVERSAL_PENDING = 14

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

class ClearingFeeIndicator (field_types.String_Type) :
    _tag = '635'
    ENUM_FIRST_YEAR_DELEGATE = '1'
    ENUM_SECOND_YEAR_DELEGATE = '2'
    ENUM_THIRD_YEAR_DELEGATE = '3'
    ENUM_FOURTH_YEAR_DELEGATE = '4'
    ENUM_FIFTH_YEAR_DELEGATE = '5'
    ENUM_SIXTH_YEAR_DELEGATE = '9'
    ENUM_CBOE_MEMBER = 'B'
    ENUM_NON_MEMBER_AND_CUSTOMER = 'C'
    ENUM_EQUITY_MEMBER_AND_CLEARING_MEMBER = 'E'
    ENUM_FULL_AND_ASSOCIATE_MEMBER = 'F'
    ENUM_FIRMS106_H_AND106_J = 'H'
    ENUM_GIM = 'I'
    ENUM_LESSEE106_F_EMPLOYEES = 'L'
    ENUM_ALL_OTHER_OWNERSHIP_TYPES = 'M'

class WorkingIndicator (field_types.Boolean_Type) :
    _tag = '636'
    ENUM_NOT_WORKING = 'N'
    ENUM_WORKING = 'Y'

class LegLastPx (field_types.Price_Type) :
    _tag = '637'

class PriorityIndicator (field_types.int_Type) :
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

class LegalConfirm (field_types.Boolean_Type) :
    _tag = '650'
    ENUM_DOES_NOT_CONSITUTE_A_LEGAL_CONFIRM = 'N'
    ENUM_LEGAL_CONFIRM = 'Y'

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

class QuoteRequestRejectReason (field_types.int_Type) :
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
    ENUM_INSUFFICIENT_CREDIT = 11
    ENUM_OTHER = 99

class SideComplianceID (field_types.String_Type) :
    _tag = '659'

class AcctIDSource (field_types.int_Type) :
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

class ConfirmStatus (field_types.int_Type) :
    _tag = '665'
    ENUM_RECEIVED = 1
    ENUM_MISMATCHED_ACCOUNT = 2
    ENUM_MISSING_SETTLEMENT_INSTRUCTIONS = 3
    ENUM_CONFIRMED = 4
    ENUM_REQUEST_REJECTED = 5

class ConfirmTransType (field_types.int_Type) :
    _tag = '666'
    ENUM_NEW = 0
    ENUM_REPLACE = 1
    ENUM_CANCEL = 2

class ContractSettlMonth (field_types.MonthYear_Type) :
    _tag = '667'

class DeliveryForm (field_types.int_Type) :
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

class LegOrderQty (field_types.Qty_Type) :
    _tag = '685'

class LegPriceType (field_types.int_Type) :
    _tag = '686'

class LegQty (field_types.Qty_Type) :
    _tag = '687'

class LegStipulationType (field_types.String_Type) :
    _tag = '688'

class LegStipulationValue (field_types.String_Type) :
    _tag = '689'

class LegSwapType (field_types.int_Type) :
    _tag = '690'
    ENUM_PAR_FOR_PAR = 1
    ENUM_MODIFIED_DURATION = 2
    ENUM_RISK = 4
    ENUM_PROCEEDS = 5

class Pool (field_types.String_Type) :
    _tag = '691'

class QuotePriceType (field_types.int_Type) :
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

class QuoteRespType (field_types.int_Type) :
    _tag = '694'
    ENUM_HIT = 1
    ENUM_COUNTER = 2
    ENUM_EXPIRED = 3
    ENUM_COVER = 4
    ENUM_DONE_AWAY = 5
    ENUM_PASS = 6
    ENUM_END_TRADE = 7
    ENUM_TIMED_OUT = 8

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

class PosType (field_types.String_Type) :
    _tag = '703'
    ENUM_ALLOCATION_TRADE_QTY = 'ALC'
    ENUM_OPTION_ASSIGNMENT = 'AS'
    ENUM_AS_OF_TRADE_QTY = 'ASF'
    ENUM_DELIVERY_QTY = 'DLV'
    ENUM_ELECTRONIC_TRADE_QTY = 'ETR'
    ENUM_OPTION_EXERCISE_QTY = 'EX'
    ENUM_END_OF_DAY_QTY = 'FIN'
    ENUM_INTRA_SPREAD_QTY = 'IAS'
    ENUM_INTER_SPREAD_QTY = 'IES'
    ENUM_ADJUSTMENT_QTY = 'PA'
    ENUM_PIT_TRADE_QTY = 'PIT'
    ENUM_START_OF_DAY_QTY = 'SOD'
    ENUM_INTEGRAL_SPLIT = 'SPL'
    ENUM_TRANSACTION_FROM_ASSIGNMENT = 'TA'
    ENUM_TOTAL_TRANSACTION_QTY = 'TOT'
    ENUM_TRANSACTION_QUANTITY = 'TQ'
    ENUM_TRANSFER_TRADE_QTY = 'TRF'
    ENUM_TRANSACTION_FROM_EXERCISE = 'TX'
    ENUM_CROSS_MARGIN_QTY = 'XM'
    ENUM_RECEIVE_QUANTITY = 'RCV'
    ENUM_CORPORATE_ACTION_ADJUSTMENT = 'CAA'
    ENUM_DELIVERY_NOTICE_QTY = 'DN'
    ENUM_EXCHANGE_FOR_PHYSICAL_QTY = 'EP'
    ENUM_PRIVATELY_NEGOTIATED_TRADE_QTY = 'PNTN'

class LongQty (field_types.Qty_Type) :
    _tag = '704'

class ShortQty (field_types.Qty_Type) :
    _tag = '705'

class PosQtyStatus (field_types.int_Type) :
    _tag = '706'
    ENUM_SUBMITTED = 0
    ENUM_ACCEPTED = 1
    ENUM_REJECTED = 2

class PosAmtType (field_types.String_Type) :
    _tag = '707'
    ENUM_CASH_AMOUNT = 'CASH'
    ENUM_CASH_RESIDUAL_AMOUNT = 'CRES'
    ENUM_FINAL_MARK_TO_MARKET_AMOUNT = 'FMTM'
    ENUM_INCREMENTAL_MARK_TO_MARKET_AMOUNT = 'IMTM'
    ENUM_PREMIUM_AMOUNT = 'PREM'
    ENUM_START_OF_DAY_MARK_TO_MARKET_AMOUNT = 'SMTM'
    ENUM_TRADE_VARIATION_AMOUNT = 'TVAR'
    ENUM_VALUE_ADJUSTED_AMOUNT = 'VADJ'
    ENUM_SETTLEMENT_VALUE = 'SETL'

class PosAmt (field_types.Amt_Type) :
    _tag = '708'

class PosTransType (field_types.int_Type) :
    _tag = '709'
    ENUM_EXERCISE = 1
    ENUM_DO_NOT_EXERCISE = 2
    ENUM_POSITION_ADJUSTMENT = 3
    ENUM_POSITION_CHANGE_SUBMISSION = 4
    ENUM_PLEDGE = 5
    ENUM_LARGE_TRADER_SUBMISSION = 6

class PosReqID (field_types.String_Type) :
    _tag = '710'

class NoUnderlyings (field_types.NumInGroup_Type) :
    _tag = '711'

class PosMaintAction (field_types.int_Type) :
    _tag = '712'
    ENUM_NEW = 1
    ENUM_REPLACE = 2
    ENUM_CANCEL = 3
    ENUM_REVERSE = 4

class OrigPosReqRefID (field_types.String_Type) :
    _tag = '713'

class PosMaintRptRefID (field_types.String_Type) :
    _tag = '714'

class ClearingBusinessDate (field_types.LocalMktDate_Type) :
    _tag = '715'

class SettlSessID (field_types.String_Type) :
    _tag = '716'
    ENUM_INTRADAY = 'ITD'
    ENUM_REGULAR_TRADING_HOURS = 'RTH'
    ENUM_ELECTRONIC_TRADING_HOURS = 'ETH'
    ENUM_END_OF_DAY = 'EOD'

class SettlSessSubID (field_types.String_Type) :
    _tag = '717'

class AdjustmentType (field_types.int_Type) :
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

class PosMaintStatus (field_types.int_Type) :
    _tag = '722'
    ENUM_ACCEPTED = 0
    ENUM_ACCEPTED_WITH_WARNINGS = 1
    ENUM_REJECTED = 2
    ENUM_COMPLETED = 3
    ENUM_COMPLETED_WITH_WARNINGS = 4

class PosMaintResult (field_types.int_Type) :
    _tag = '723'
    ENUM_SUCCESSFUL_COMPLETION = 0
    ENUM_REJECTED = 1
    ENUM_OTHER = 99

class PosReqType (field_types.int_Type) :
    _tag = '724'
    ENUM_POSITIONS = 0
    ENUM_TRADES = 1
    ENUM_EXERCISES = 2
    ENUM_ASSIGNMENTS = 3
    ENUM_SETTLEMENT_ACTIVITY = 4
    ENUM_BACKOUT_MESSAGE = 5

class ResponseTransportType (field_types.int_Type) :
    _tag = '725'
    ENUM_INBAND = 0
    ENUM_OUT_OF_BAND = 1

class ResponseDestination (field_types.String_Type) :
    _tag = '726'

class TotalNumPosReports (field_types.int_Type) :
    _tag = '727'

class PosReqResult (field_types.int_Type) :
    _tag = '728'
    ENUM_VALID_REQUEST = 0
    ENUM_INVALID_OR_UNSUPPORTED_REQUEST = 1
    ENUM_NO_POSITIONS_FOUND_THAT_MATCH_CRITERIA = 2
    ENUM_NOT_AUTHORIZED_TO_REQUEST_POSITIONS = 3
    ENUM_REQUEST_FOR_POSITION_NOT_SUPPORTED = 4
    ENUM_OTHER = 99

class PosReqStatus (field_types.int_Type) :
    _tag = '729'
    ENUM_COMPLETED = 0
    ENUM_COMPLETED_WITH_WARNINGS = 1
    ENUM_REJECTED = 2

class SettlPrice (field_types.Price_Type) :
    _tag = '730'

class SettlPriceType (field_types.int_Type) :
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

class AssignmentMethod (field_types.char_Type) :
    _tag = '744'
    ENUM_PRO_RATA = 'P'
    ENUM_RANDOM = 'R'

class AssignmentUnit (field_types.Qty_Type) :
    _tag = '745'

class OpenInterest (field_types.Amt_Type) :
    _tag = '746'

class ExerciseMethod (field_types.char_Type) :
    _tag = '747'
    ENUM_AUTOMATIC = 'A'
    ENUM_MANUAL = 'M'

class TotNumTradeReports (field_types.int_Type) :
    _tag = '748'

class TradeRequestResult (field_types.int_Type) :
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

class TradeRequestStatus (field_types.int_Type) :
    _tag = '750'
    ENUM_ACCEPTED = 0
    ENUM_COMPLETED = 1
    ENUM_REJECTED = 2

class TradeReportRejectReason (field_types.int_Type) :
    _tag = '751'
    ENUM_SUCCESSFUL = 0
    ENUM_INVALID_PARTY_ONFORMATION = 1
    ENUM_UNKNOWN_INSTRUMENT = 2
    ENUM_UNAUTHORIZED_TO_REPORT_TRADES = 3
    ENUM_INVALID_TRADE_TYPE = 4
    ENUM_OTHER = 99

class SideMultiLegReportingType (field_types.int_Type) :
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

class TrdRegTimestampType (field_types.int_Type) :
    _tag = '770'
    ENUM_EXECUTION_TIME = 1
    ENUM_TIME_IN = 2
    ENUM_TIME_OUT = 3
    ENUM_BROKER_RECEIPT = 4
    ENUM_BROKER_EXECUTION = 5
    ENUM_DESK_RECEIPT = 6

class TrdRegTimestampOrigin (field_types.String_Type) :
    _tag = '771'

class ConfirmRefID (field_types.String_Type) :
    _tag = '772'

class ConfirmType (field_types.int_Type) :
    _tag = '773'
    ENUM_STATUS = 1
    ENUM_CONFIRMATION = 2
    ENUM_CONFIRMATION_REQUEST_REJECTED = 3

class ConfirmRejReason (field_types.int_Type) :
    _tag = '774'
    ENUM_MISMATCHED_ACCOUNT = 1
    ENUM_MISSING_SETTLEMENT_INSTRUCTIONS = 2
    ENUM_OTHER = 99

class BookingType (field_types.int_Type) :
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

class AllocSettlInstType (field_types.int_Type) :
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

class DlvyInstType (field_types.char_Type) :
    _tag = '787'
    ENUM_CASH = 'C'
    ENUM_SECURITIES = 'S'

class TerminationType (field_types.int_Type) :
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

class SettlInstReqRejCode (field_types.int_Type) :
    _tag = '792'
    ENUM_UNABLE_TO_PROCESS_REQUEST = 0
    ENUM_UNKNOWN_ACCOUNT = 1
    ENUM_NO_MATCHING_SETTLEMENT_INSTRUCTIONS_FOUND = 2
    ENUM_OTHER = 99

class SecondaryAllocID (field_types.String_Type) :
    _tag = '793'

class AllocReportType (field_types.int_Type) :
    _tag = '794'
    ENUM_PRELIMINARY_REQUEST_TO_INTERMEDIARY = 2
    ENUM_SELLSIDE_CALCULATED_USING_PRELIMINARY = 3
    ENUM_SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY = 4
    ENUM_WAREHOUSE_RECAP = 5
    ENUM_REQUEST_TO_INTERMEDIARY = 8
    ENUM_ACCEPT = 9
    ENUM_REJECT = 10
    ENUM_ACCEPT_PENDING = 11
    ENUM_COMPLETE = 12
    ENUM_REVERSE_PENDING = 14

class AllocReportRefID (field_types.String_Type) :
    _tag = '795'

class AllocCancReplaceReason (field_types.int_Type) :
    _tag = '796'
    ENUM_ORIGINAL_DETAILS_INCOMPLETE = 1
    ENUM_CHANGE_IN_UNDERLYING_ORDER_DETAILS = 2
    ENUM_OTHER = 99

class CopyMsgIndicator (field_types.Boolean_Type) :
    _tag = '797'

class AllocAccountType (field_types.int_Type) :
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

class PartySubIDType (field_types.int_Type) :
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
    ENUM_SECURITY_LOCATE_ID = 27
    ENUM_MARKET_MAKER = 28
    ENUM_ELIGIBLE_COUNTERPARTY = 29
    ENUM_PROFESSIONAL_CLIENT = 30
    ENUM_LOCATION = 31
    ENUM_EXECUTION_VENUE = 32
    ENUM_CURRENCY_DELIVERY_IDENTIFIER = 33

class NoNestedPartySubIDs (field_types.NumInGroup_Type) :
    _tag = '804'

class NestedPartySubIDType (field_types.int_Type) :
    _tag = '805'

class NoNested2PartySubIDs (field_types.NumInGroup_Type) :
    _tag = '806'

class Nested2PartySubIDType (field_types.int_Type) :
    _tag = '807'

class AllocIntermedReqType (field_types.int_Type) :
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

class ApplQueueResolution (field_types.int_Type) :
    _tag = '814'
    ENUM_NO_ACTION_TAKEN = 0
    ENUM_QUEUE_FLUSHED = 1
    ENUM_OVERLAY_LAST = 2
    ENUM_END_SESSION = 3

class ApplQueueAction (field_types.int_Type) :
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

class AvgPxIndicator (field_types.int_Type) :
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

class TradeAllocIndicator (field_types.int_Type) :
    _tag = '826'
    ENUM_ALLOCATION_NOT_REQUIRED = 0
    ENUM_ALLOCATION_REQUIRED = 1
    ENUM_USE_ALLOCATION_PROVIDED_WITH_THE_TRADE = 2
    ENUM_ALLOCATION_GIVE_UP_EXECUTOR = 3
    ENUM_ALLOCATION_FROM_EXECUTOR = 4
    ENUM_ALLOCATION_TO_CLAIM_ACCOUNT = 5

class ExpirationCycle (field_types.int_Type) :
    _tag = '827'
    ENUM_EXPIRE_ON_TRADING_SESSION_CLOSE = 0
    ENUM_EXPIRE_ON_TRADING_SESSION_OPEN = 1
    ENUM_SPECIFIED_EXPIRATION = 2

class TrdType (field_types.int_Type) :
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
    ENUM_EXCHANGE_FOR_RISK = 11
    ENUM_EXCHANGE_FOR_SWAP = 12
    ENUM_EXCHANGE_OF_FUTURES_FOR = 13
    ENUM_EXCHANGE_OF_OPTIONS_FOR_OPTIONS = 14
    ENUM_TRADING_AT_SETTLEMENT = 15
    ENUM_ALL_OR_NONE = 16
    ENUM_FUTURES_LARGE_ORDER_EXECUTION = 17
    ENUM_EXCHANGE_OF_FUTURES_FOR_FUTURES = 18
    ENUM_OPTION_INTERIM_TRADE = 19
    ENUM_OPTION_CABINET_TRADE = 20
    ENUM_PRIVATELY_NEGOTIATED_TRADES = 22
    ENUM_SUBSTITUTION_OF_FUTURES_FOR_FORWARDS = 23
    ENUM_NON_STANDARD_SETTLEMENT = 48
    ENUM_DERIVATIVE_RELATED_TRANSACTION = 49
    ENUM_PORTFOLIO_TRADE = 50
    ENUM_VOLUME_WEIGHTED_AVERAGE_TRADE = 51
    ENUM_EXCHANGE_GRANTED_TRADE = 52
    ENUM_REPURCHASE_AGREEMENT = 53
    ENUM_OTC = 54
    ENUM_EXCHANGE_BASIS_FACILITY = 55
    ENUM_ERROR_TRADE = 24
    ENUM_SPECIAL_CUM_DIVIDEND = 25
    ENUM_SPECIAL_EX_DIVIDEND = 26
    ENUM_SPECIAL_CUM_COUPON = 27
    ENUM_SPECIAL_EX_COUPON = 28
    ENUM_CASH_SETTLEMENT = 29
    ENUM_SPECIAL_PRICE = 30
    ENUM_GUARANTEED_DELIVERY = 31
    ENUM_SPECIAL_CUM_RIGHTS = 32
    ENUM_SPECIAL_EX_RIGHTS = 33
    ENUM_SPECIAL_CUM_CAPITAL_REPAYMENTS = 34
    ENUM_SPECIAL_EX_CAPITAL_REPAYMENTS = 35
    ENUM_SPECIAL_CUM_BONUS = 36
    ENUM_SPECIAL_EX_BONUS = 37
    ENUM_LARGE_TRADE = 38
    ENUM_WORKED_PRINCIPAL_TRADE = 39
    ENUM_BLOCK_TRADES = 40
    ENUM_NAME_CHANGE = 41
    ENUM_PORTFOLIO_TRANSFER = 42
    ENUM_PROROGATION_BUY = 43
    ENUM_PROROGATION_SELL = 44
    ENUM_OPTION_EXERCISE = 45
    ENUM_DELTA_NEUTRAL_TRANSACTION = 46
    ENUM_FINANCING_TRANSACTION = 47

class TrdSubType (field_types.int_Type) :
    _tag = '829'
    ENUM_CMTA = 0
    ENUM_INTERNAL_TRANSFER_OR_ADJUSTMENT = 1
    ENUM_EXTERNAL_TRANSFER_OR_TRANSFER_OF_ACCOUNT = 2
    ENUM_REJECT_FOR_SUBMITTING_SIDE = 3
    ENUM_ADVISORY_FOR_CONTRA_SIDE = 4
    ENUM_OFFSET_DUE_TO_AN_ALLOCATION = 5
    ENUM_ONSET_DUE_TO_AN_ALLOCATION = 6
    ENUM_DIFFERENTIAL_SPREAD = 7
    ENUM_IMPLIED_SPREAD_LEG_EXECUTED_AGAINST_AN_OUTRIGHT = 8
    ENUM_TRANSACTION_FROM_EXERCISE = 9
    ENUM_TRANSACTION_FROM_ASSIGNMENT = 10
    ENUM_ACATS = 11
    ENUM_OFF_HOURS_TRADE = 33
    ENUM_ON_HOURS_TRADE = 34
    ENUM_OTC_QUOTE = 35
    ENUM_CONVERTED_SWAP = 36
    ENUM_AI = 14
    ENUM_B = 15
    ENUM_K = 16
    ENUM_LC = 17
    ENUM_M = 18
    ENUM_N = 19
    ENUM_NM = 20
    ENUM_NR = 21
    ENUM_P = 22
    ENUM_PA = 23
    ENUM_PC = 24
    ENUM_PN = 25
    ENUM_R = 26
    ENUM_RO = 27
    ENUM_RT = 28
    ENUM_SW = 29
    ENUM_T = 30
    ENUM_WN = 31
    ENUM_WT = 32
    ENUM_CROSSED_TRADE = 37
    ENUM_INTERIM_PROTECTED_TRADE = 38
    ENUM_LARGE_IN_SCALE = 39

class TransferReason (field_types.String_Type) :
    _tag = '830'

class TotNumAssignmentReports (field_types.int_Type) :
    _tag = '832'

class AsgnRptID (field_types.String_Type) :
    _tag = '833'

class ThresholdAmount (field_types.PriceOffset_Type) :
    _tag = '834'

class PegMoveType (field_types.int_Type) :
    _tag = '835'
    ENUM_FLOATING = 0
    ENUM_FIXED = 1

class PegOffsetType (field_types.int_Type) :
    _tag = '836'
    ENUM_PRICE = 0
    ENUM_BASIS_POINTS = 1
    ENUM_TICKS = 2
    ENUM_PRICE_TIER = 3

class PegLimitType (field_types.int_Type) :
    _tag = '837'
    ENUM_OR_BETTER = 0
    ENUM_STRICT = 1
    ENUM_OR_WORSE = 2

class PegRoundDirection (field_types.int_Type) :
    _tag = '838'
    ENUM_MORE_AGGRESSIVE = 1
    ENUM_MORE_PASSIVE = 2

class PeggedPrice (field_types.Price_Type) :
    _tag = '839'

class PegScope (field_types.int_Type) :
    _tag = '840'
    ENUM_LOCAL = 1
    ENUM_NATIONAL = 2
    ENUM_GLOBAL = 3
    ENUM_NATIONAL_EXCLUDING_LOCAL = 4

class DiscretionMoveType (field_types.int_Type) :
    _tag = '841'
    ENUM_FLOATING = 0
    ENUM_FIXED = 1

class DiscretionOffsetType (field_types.int_Type) :
    _tag = '842'
    ENUM_PRICE = 0
    ENUM_BASIS_POINTS = 1
    ENUM_TICKS = 2
    ENUM_PRICE_TIER = 3

class DiscretionLimitType (field_types.int_Type) :
    _tag = '843'
    ENUM_OR_BETTER = 0
    ENUM_STRICT = 1
    ENUM_OR_WORSE = 2

class DiscretionRoundDirection (field_types.int_Type) :
    _tag = '844'
    ENUM_MORE_AGGRESSIVE = 1
    ENUM_MORE_PASSIVE = 2

class DiscretionPrice (field_types.Price_Type) :
    _tag = '845'

class DiscretionScope (field_types.int_Type) :
    _tag = '846'
    ENUM_LOCAL = 1
    ENUM_NATIONAL = 2
    ENUM_GLOBAL = 3
    ENUM_NATIONAL_EXCLUDING_LOCAL = 4

class TargetStrategy (field_types.int_Type) :
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

class LastLiquidityInd (field_types.int_Type) :
    _tag = '851'
    ENUM_ADDED_LIQUIDITY = 1
    ENUM_REMOVED_LIQUIDITY = 2
    ENUM_LIQUIDITY_ROUTED_OUT = 3
    ENUM_AUCTION = 4

class PublishTrdIndicator (field_types.Boolean_Type) :
    _tag = '852'
    ENUM_DO_NOT_REPORT_TRADE = 'N'
    ENUM_REPORT_TRADE = 'Y'

class ShortSaleReason (field_types.int_Type) :
    _tag = '853'
    ENUM_DEALER_SOLD_SHORT = 0
    ENUM_DEALER_SOLD_SHORT_EXEMPT = 1
    ENUM_SELLING_CUSTOMER_SOLD_SHORT = 2
    ENUM_SELLING_CUSTOMER_SOLD_SHORT_EXEMPT = 3
    ENUM_QUALIFIED_SERVICE_REPRESENTATIVE = 4
    ENUM_QSR_OR_AGU_CONTRA_SIDE_SOLD_SHORT_EXEMPT = 5

class QtyType (field_types.int_Type) :
    _tag = '854'
    ENUM_UNITS = 0
    ENUM_CONTRACTS = 1
    ENUM_UNITS_OF_MEASURE_PER_TIME_UNIT = 2

class SecondaryTrdType (field_types.int_Type) :
    _tag = '855'

class TradeReportType (field_types.int_Type) :
    _tag = '856'
    ENUM_SUBMIT = 0
    ENUM_ALLEGED = 1
    ENUM_ACCEPT = 2
    ENUM_DECLINE = 3
    ENUM_ADDENDUM = 4
    ENUM_NO = 5
    ENUM_TRADE_REPORT_CANCEL = 6
    ENUM_LOCKED_IN = 7
    ENUM_DEFAULTED = 8
    ENUM_INVALID_CMTA = 9
    ENUM_PENDED = 10
    ENUM_ALLEGED_NEW = 11
    ENUM_ALLEGED_ADDENDUM = 12
    ENUM_ALLEGED_NO = 13
    ENUM_ALLEGED_TRADE_REPORT_CANCEL = 14
    ENUM_ALLEGED_TRADE_BREAK = 15

class AllocNoOrdersType (field_types.int_Type) :
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

class EventType (field_types.int_Type) :
    _tag = '865'
    ENUM_PUT = 1
    ENUM_CALL = 2
    ENUM_TENDER = 3
    ENUM_SINKING_FUND_CALL = 4
    ENUM_ACTIVATION = 5
    ENUM_INACTIVIATION = 6
    ENUM_LAST_ELIGIBLE_TRADE_DATE = 7
    ENUM_SWAP_START_DATE = 8
    ENUM_SWAP_END_DATE = 9
    ENUM_SWAP_ROLL_DATE = 10
    ENUM_SWAP_NEXT_START_DATE = 11
    ENUM_SWAP_NEXT_ROLL_DATE = 12
    ENUM_FIRST_DELIVERY_DATE = 13
    ENUM_LAST_DELIVERY_DATE = 14
    ENUM_INITIAL_INVENTORY_DUE_DATE = 15
    ENUM_FINAL_INVENTORY_DUE_DATE = 16
    ENUM_FIRST_INTENT_DATE = 17
    ENUM_LAST_INTENT_DATE = 18
    ENUM_POSITION_REMOVAL_DATE = 19
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

class InstrAttribType (field_types.int_Type) :
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
    ENUM_PRICE_TICK_RULES_FOR_SECURITY = 23
    ENUM_TRADE_TYPE_ELIGIBILITY_DETAILS_FOR_SECURITY = 24
    ENUM_INSTRUMENT_DENOMINATOR = 25
    ENUM_INSTRUMENT_NUMERATOR = 26
    ENUM_INSTRUMENT_PRICE_PRECISION = 27
    ENUM_INSTRUMENT_STRIKE_PRICE = 28
    ENUM_TRADEABLE_INDICATOR = 29
    ENUM_TEXT = 99

class InstrAttribValue (field_types.String_Type) :
    _tag = '872'

class DatedDate (field_types.LocalMktDate_Type) :
    _tag = '873'

class InterestAccrualDate (field_types.LocalMktDate_Type) :
    _tag = '874'

class CPProgram (field_types.int_Type) :
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

class MiscFeeBasis (field_types.int_Type) :
    _tag = '891'
    ENUM_ABSOLUTE = 0
    ENUM_PER_UNIT = 1
    ENUM_PERCENTAGE = 2

class TotNoAllocs (field_types.int_Type) :
    _tag = '892'

class LastFragment (field_types.Boolean_Type) :
    _tag = '893'
    ENUM_NOT_LAST_MESSAGE = 'N'
    ENUM_LAST_MESSAGE = 'Y'

class CollReqID (field_types.String_Type) :
    _tag = '894'

class CollAsgnReason (field_types.int_Type) :
    _tag = '895'
    ENUM_INITIAL = 0
    ENUM_SCHEDULED = 1
    ENUM_TIME_WARNING = 2
    ENUM_MARGIN_DEFICIENCY = 3
    ENUM_MARGIN_EXCESS = 4
    ENUM_FORWARD_COLLATERAL_DEMAND = 5
    ENUM_EVENT_OF_DEFAULT = 6
    ENUM_ADVERSE_TAX_EVENT = 7

class CollInquiryQualifier (field_types.int_Type) :
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

class CollAsgnTransType (field_types.int_Type) :
    _tag = '903'
    ENUM_NEW = 0
    ENUM_REPLACE = 1
    ENUM_CANCEL = 2
    ENUM_RELEASE = 3
    ENUM_REVERSE = 4

class CollRespID (field_types.String_Type) :
    _tag = '904'

class CollAsgnRespType (field_types.int_Type) :
    _tag = '905'
    ENUM_RECEIVED = 0
    ENUM_ACCEPTED = 1
    ENUM_DECLINED = 2
    ENUM_REJECTED = 3

class CollAsgnRejectReason (field_types.int_Type) :
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

class CollStatus (field_types.int_Type) :
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
    ENUM_NOT_LAST_MESSAGE = 'N'
    ENUM_LAST_MESSAGE = 'Y'

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

class DeliveryType (field_types.int_Type) :
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

class UserRequestType (field_types.int_Type) :
    _tag = '924'
    ENUM_LOG_ON_USER = 1
    ENUM_LOG_OFF_USER = 2
    ENUM_CHANGE_PASSWORD_FOR_USER = 3
    ENUM_REQUEST_INDIVIDUAL_USER_STATUS = 4

class NewPassword (field_types.String_Type) :
    _tag = '925'

class UserStatus (field_types.int_Type) :
    _tag = '926'
    ENUM_LOGGED_IN = 1
    ENUM_NOT_LOGGED_IN = 2
    ENUM_USER_NOT_RECOGNISED = 3
    ENUM_PASSWORD_INCORRECT = 4
    ENUM_PASSWORD_CHANGED = 5
    ENUM_OTHER = 6
    ENUM_FORCED_USER_LOGOUT_BY_EXCHANGE = 7
    ENUM_SESSION_SHUTDOWN_WARNING = 8

class UserStatusText (field_types.String_Type) :
    _tag = '927'

class StatusValue (field_types.int_Type) :
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

class NetworkRequestType (field_types.int_Type) :
    _tag = '935'
    ENUM_SNAPSHOT = 1
    ENUM_SUBSCRIBE = 2
    ENUM_STOP_SUBSCRIBING = 4
    ENUM_LEVEL_OF_DETAIL = 8

class NoCompIDs (field_types.NumInGroup_Type) :
    _tag = '936'

class NetworkStatusResponseType (field_types.int_Type) :
    _tag = '937'
    ENUM_FULL = 1
    ENUM_INCREMENTAL_UPDATE = 2

class NoCollInquiryQualifier (field_types.NumInGroup_Type) :
    _tag = '938'

class TrdRptStatus (field_types.int_Type) :
    _tag = '939'
    ENUM_ACCEPTED = 0
    ENUM_REJECTED = 1
    ENUM_ACCEPTED_WITH_ERRORS = 3

class AffirmStatus (field_types.int_Type) :
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

class CollAction (field_types.int_Type) :
    _tag = '944'
    ENUM_RETAIN = 0
    ENUM_ADD = 1
    ENUM_REMOVE = 2

class CollInquiryStatus (field_types.int_Type) :
    _tag = '945'
    ENUM_ACCEPTED = 0
    ENUM_ACCEPTED_WITH_WARNINGS = 1
    ENUM_COMPLETED = 2
    ENUM_COMPLETED_WITH_WARNINGS = 3
    ENUM_REJECTED = 4

class CollInquiryResult (field_types.int_Type) :
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

class NoStrategyParameters (field_types.NumInGroup_Type) :
    _tag = '957'

class StrategyParameterName (field_types.String_Type) :
    _tag = '958'

class StrategyParameterType (field_types.int_Type) :
    _tag = '959'
    ENUM_INT = 1
    ENUM_LENGTH = 2
    ENUM_NUM_IN_GROUP = 3
    ENUM_SEQ_NUM = 4
    ENUM_TAG_NUM = 5
    ENUM_FLOAT = 6
    ENUM_QTY = 7
    ENUM_PRICE = 8
    ENUM_PRICE_OFFSET = 9
    ENUM_AMT = 10
    ENUM_PERCENTAGE = 11
    ENUM_CHAR = 12
    ENUM_BOOLEAN = 13
    ENUM_STRING = 14
    ENUM_MULTIPLE_CHAR_VALUE = 15
    ENUM_CURRENCY = 16
    ENUM_EXCHANGE = 17
    ENUM_MONTH_YEAR = 18
    ENUM_UTC_TIMESTAMP = 19
    ENUM_UTC_TIME_ONLY = 20
    ENUM_LOCAL_MKT_DATE = 21
    ENUM_UTC_DATE_ONLY = 22
    ENUM_DATA = 23
    ENUM_MULTIPLE_STRING_VALUE = 24

class StrategyParameterValue (field_types.String_Type) :
    _tag = '960'

class HostCrossID (field_types.String_Type) :
    _tag = '961'

class SideTimeInForce (field_types.UTCTimestamp_Type) :
    _tag = '962'

class MDReportID (field_types.int_Type) :
    _tag = '963'

class SecurityReportID (field_types.int_Type) :
    _tag = '964'

class SecurityStatus (field_types.String_Type) :
    _tag = '965'
    ENUM_ACTIVE = '1'
    ENUM_INACTIVE = '2'

class SettleOnOpenFlag (field_types.String_Type) :
    _tag = '966'

class StrikeMultiplier (field_types.float_Type) :
    _tag = '967'

class StrikeValue (field_types.float_Type) :
    _tag = '968'

class MinPriceIncrement (field_types.float_Type) :
    _tag = '969'

class PositionLimit (field_types.int_Type) :
    _tag = '970'

class NTPositionLimit (field_types.int_Type) :
    _tag = '971'

class UnderlyingAllocationPercent (field_types.Percentage_Type) :
    _tag = '972'

class UnderlyingCashAmount (field_types.Amt_Type) :
    _tag = '973'

class UnderlyingCashType (field_types.String_Type) :
    _tag = '974'
    ENUM_FIXED = 'FIXED'
    ENUM_DIFF = 'DIFF'

class UnderlyingSettlementType (field_types.int_Type) :
    _tag = '975'
    ENUM_T_PLUS1 = 2
    ENUM_T_PLUS3 = 4
    ENUM_T_PLUS4 = 5

class QuantityDate (field_types.LocalMktDate_Type) :
    _tag = '976'

class ContIntRptID (field_types.String_Type) :
    _tag = '977'

class LateIndicator (field_types.Boolean_Type) :
    _tag = '978'

class InputSource (field_types.String_Type) :
    _tag = '979'

class SecurityUpdateAction (field_types.char_Type) :
    _tag = '980'
    ENUM_ADD = 'A'
    ENUM_DELETE = 'D'
    ENUM_MODIFY = 'M'

class NoExpiration (field_types.NumInGroup_Type) :
    _tag = '981'

class ExpirationQtyType (field_types.int_Type) :
    _tag = '982'
    ENUM_AUTO_EXERCISE = 1
    ENUM_NON_AUTO_EXERCISE = 2
    ENUM_FINAL_WILL_BE_EXERCISED = 3
    ENUM_CONTRARY_INTENTION = 4
    ENUM_DIFFERENCE = 5

class ExpQty (field_types.Qty_Type) :
    _tag = '983'

class NoUnderlyingAmounts (field_types.NumInGroup_Type) :
    _tag = '984'

class UnderlyingPayAmount (field_types.Amt_Type) :
    _tag = '985'

class UnderlyingCollectAmount (field_types.Amt_Type) :
    _tag = '986'

class UnderlyingSettlementDate (field_types.LocalMktDate_Type) :
    _tag = '987'

class UnderlyingSettlementStatus (field_types.String_Type) :
    _tag = '988'

class SecondaryIndividualAllocID (field_types.String_Type) :
    _tag = '989'

class LegReportID (field_types.String_Type) :
    _tag = '990'

class RndPx (field_types.Price_Type) :
    _tag = '991'

class IndividualAllocType (field_types.int_Type) :
    _tag = '992'
    ENUM_SUB_ALLOCATE = 1
    ENUM_THIRD_PARTY_ALLOCATION = 2

class AllocCustomerCapacity (field_types.String_Type) :
    _tag = '993'

class TierCode (field_types.String_Type) :
    _tag = '994'

class UnitOfMeasure (field_types.String_Type) :
    _tag = '996'
    ENUM_BILLION_CUBIC_FEET = 'Bcf'
    ENUM_MILLION_BARRELS = 'MMbbl'
    ENUM_ONE_MILLION_BTU = 'MMBtu'
    ENUM_MEGAWATT_HOURS = 'MWh'
    ENUM_BARRELS = 'Bbl'
    ENUM_BUSHELS = 'Bu'
    ENUM_POUNDS = 'lbs'
    ENUM_GALLONS = 'Gal'
    ENUM_TROY_OUNCES = 'oz_tr'
    ENUM_METRIC_TONS = 't'
    ENUM_TONS = 'tn'
    ENUM_US_DOLLARS = 'USD'

class TimeUnit (field_types.String_Type) :
    _tag = '997'
    ENUM_HOUR = 'H'
    ENUM_MINUTE = 'Min'
    ENUM_SECOND = 'S'
    ENUM_DAY = 'D'
    ENUM_WEEK = 'Wk'
    ENUM_MONTH = 'Mo'
    ENUM_YEAR = 'Yr'

class UnderlyingUnitOfMeasure (field_types.String_Type) :
    _tag = '998'

class LegUnitOfMeasure (field_types.String_Type) :
    _tag = '999'

class UnderlyingTimeUnit (field_types.String_Type) :
    _tag = '1000'

class LegTimeUnit (field_types.String_Type) :
    _tag = '1001'

class AllocMethod (field_types.int_Type) :
    _tag = '1002'
    ENUM_AUTOMATIC = 1
    ENUM_GUARANTOR = 2
    ENUM_MANUAL = 3

class TradeID (field_types.String_Type) :
    _tag = '1003'

class SideTradeReportID (field_types.String_Type) :
    _tag = '1005'

class SideFillStationCd (field_types.String_Type) :
    _tag = '1006'

class SideReasonCd (field_types.String_Type) :
    _tag = '1007'

class SideTrdSubTyp (field_types.int_Type) :
    _tag = '1008'

class SideQty (field_types.int_Type) :
    _tag = '1009'

class MessageEventSource (field_types.String_Type) :
    _tag = '1011'

class SideTrdRegTimestamp (field_types.UTCTimestamp_Type) :
    _tag = '1012'

class SideTrdRegTimestampType (field_types.int_Type) :
    _tag = '1013'

class SideTrdRegTimestampSrc (field_types.String_Type) :
    _tag = '1014'

class AsOfIndicator (field_types.char_Type) :
    _tag = '1015'
    ENUM_FALSE = '0'
    ENUM_TRUE = '1'

class NoSideTrdRegTS (field_types.NumInGroup_Type) :
    _tag = '1016'

class LegOptionRatio (field_types.float_Type) :
    _tag = '1017'

class NoInstrumentParties (field_types.NumInGroup_Type) :
    _tag = '1018'

class InstrumentPartyID (field_types.String_Type) :
    _tag = '1019'

class TradeVolume (field_types.Qty_Type) :
    _tag = '1020'

class MDBookType (field_types.int_Type) :
    _tag = '1021'
    ENUM_TOP_OF_BOOK = 1
    ENUM_PRICE_DEPTH = 2
    ENUM_ORDER_DEPTH = 3

class MDFeedType (field_types.String_Type) :
    _tag = '1022'

class MDPriceLevel (field_types.int_Type) :
    _tag = '1023'

class MDOriginType (field_types.int_Type) :
    _tag = '1024'
    ENUM_BOOK = 0
    ENUM_OFF_BOOK = 1
    ENUM_CROSS = 2

class FirstPx (field_types.Price_Type) :
    _tag = '1025'

class MDEntrySpotRate (field_types.float_Type) :
    _tag = '1026'

class MDEntryForwardPoints (field_types.PriceOffset_Type) :
    _tag = '1027'

class ManualOrderIndicator (field_types.Boolean_Type) :
    _tag = '1028'

class CustDirectedOrder (field_types.Boolean_Type) :
    _tag = '1029'

class ReceivedDeptID (field_types.String_Type) :
    _tag = '1030'

class CustOrderHandlingInst (field_types.MultipleStringValue_Type) :
    _tag = '1031'
    ENUM_ADD_ON_ORDER = 'ADD'
    ENUM_ALL_OR_NONE = 'AON'
    ENUM_CASH_NOT_HELD = 'CNH'
    ENUM_DIRECTED_ORDER = 'DIR'
    ENUM_EXCHANGE_FOR_PHYSICAL_TRANSACTION = 'E.W'
    ENUM_FILL_OR_KILL = 'FOK'
    ENUM_IMBALANCE_ONLY = 'IO'
    ENUM_IMMEDIATE_OR_CANCEL = 'IOC'
    ENUM_LIMIT_ON_OPEN = 'LOO'
    ENUM_LIMIT_ON_CLOSE = 'LOC'
    ENUM_MARKET_AT_OPEN = 'MAO'
    ENUM_MARKET_AT_CLOSE = 'MAC'
    ENUM_MARKET_ON_OPEN = 'MOO'
    ENUM_MARKET_ON_CLOSE = 'MOC'
    ENUM_MINIMUM_QUANTITY = 'MQT'
    ENUM_NOT_HELD = 'NH'
    ENUM_OVER_THE_DAY = 'OVD'
    ENUM_PEGGED = 'PEG'
    ENUM_RESERVE_SIZE_ORDER = 'RSV'
    ENUM_STOP_STOCK_TRANSACTION = 'S.W'
    ENUM_SCALE = 'SCL'
    ENUM_TIME_ORDER = 'TMO'
    ENUM_TRAILING_STOP = 'TS'
    ENUM_WORK = 'WRK'

class OrderHandlingInstSource (field_types.int_Type) :
    _tag = '1032'
    ENUM_NASDOATS = 1

class DeskType (field_types.String_Type) :
    _tag = '1033'
    ENUM_AGENCY = 'A'
    ENUM_ARBITRAGE = 'AR'
    ENUM_DERIVATIVES = 'D'
    ENUM_INTERNATIONAL = 'IN'
    ENUM_INSTITUTIONAL = 'IS'
    ENUM_OTHER = 'O'
    ENUM_PREFERRED_TRADING = 'PF'
    ENUM_PROPRIETARY = 'PR'
    ENUM_PROGRAM_TRADING = 'PT'
    ENUM_SALES = 'S'
    ENUM_TRADING = 'T'

class DeskTypeSource (field_types.int_Type) :
    _tag = '1034'
    ENUM_NASDOATS = 1

class DeskOrderHandlingInst (field_types.MultipleStringValue_Type) :
    _tag = '1035'
    ENUM_ADD_ON_ORDER = 'ADD'
    ENUM_ALL_OR_NONE = 'AON'
    ENUM_CASH_NOT_HELD = 'CNH'
    ENUM_DIRECTED_ORDER = 'DIR'
    ENUM_EXCHANGE_FOR_PHYSICAL_TRANSACTION = 'E.W'
    ENUM_FILL_OR_KILL = 'FOK'
    ENUM_IMBALANCE_ONLY = 'IO'
    ENUM_IMMEDIATE_OR_CANCEL = 'IOC'
    ENUM_LIMIT_ON_OPEN = 'LOO'
    ENUM_LIMIT_ON_CLOSE = 'LOC'
    ENUM_MARKET_AT_OPEN = 'MAO'
    ENUM_MARKET_AT_CLOSE = 'MAC'
    ENUM_MARKET_ON_OPEN = 'MOO'
    ENUM_MARKET_ON_CLOSE = 'MOC'
    ENUM_MINIMUM_QUANTITY = 'MQT'
    ENUM_NOT_HELD = 'NH'
    ENUM_OVER_THE_DAY = 'OVD'
    ENUM_PEGGED = 'PEG'
    ENUM_RESERVE_SIZE_ORDER = 'RSV'
    ENUM_STOP_STOCK_TRANSACTION = 'S.W'
    ENUM_SCALE = 'SCL'
    ENUM_TIME_ORDER = 'TMO'
    ENUM_TRAILING_STOP = 'TS'
    ENUM_WORK = 'WRK'

class ExecAckStatus (field_types.char_Type) :
    _tag = '1036'
    ENUM_RECEIVED = '0'
    ENUM_ACCEPTED = '1'
    ENUM_DON = '2'

class UnderlyingDeliveryAmount (field_types.Amt_Type) :
    _tag = '1037'

class UnderlyingCapValue (field_types.Amt_Type) :
    _tag = '1038'

class UnderlyingSettlMethod (field_types.String_Type) :
    _tag = '1039'

class SecondaryTradeID (field_types.String_Type) :
    _tag = '1040'

class FirmTradeID (field_types.String_Type) :
    _tag = '1041'

class SecondaryFirmTradeID (field_types.String_Type) :
    _tag = '1042'

class CollApplType (field_types.int_Type) :
    _tag = '1043'
    ENUM_SPECIFIC_DEPOSIT = 0
    ENUM_GENERAL = 1

class UnderlyingAdjustedQuantity (field_types.Qty_Type) :
    _tag = '1044'

class UnderlyingFXRate (field_types.float_Type) :
    _tag = '1045'

class UnderlyingFXRateCalc (field_types.char_Type) :
    _tag = '1046'
    ENUM_DIVIDE = 'D'
    ENUM_MULTIPLY = 'M'

class AllocPositionEffect (field_types.char_Type) :
    _tag = '1047'
    ENUM_OPEN = 'O'
    ENUM_CLOSE = 'C'
    ENUM_ROLLED = 'R'
    ENUM_FIFO = 'F'

class DealingCapacity (field_types.PriceOffset_Type) :
    _tag = '1048'

class InstrmtAssignmentMethod (field_types.char_Type) :
    _tag = '1049'
    ENUM_RANDOM = 'R'
    ENUM_PRO_RATA = 'P'

class InstrumentPartyIDSource (field_types.char_Type) :
    _tag = '1050'

class InstrumentPartyRole (field_types.int_Type) :
    _tag = '1051'

class NoInstrumentPartySubIDs (field_types.NumInGroup_Type) :
    _tag = '1052'

class InstrumentPartySubID (field_types.String_Type) :
    _tag = '1053'

class InstrumentPartySubIDType (field_types.int_Type) :
    _tag = '1054'

class PositionCurrency (field_types.String_Type) :
    _tag = '1055'

class CalculatedCcyLastQty (field_types.Qty_Type) :
    _tag = '1056'

class AggressorIndicator (field_types.Boolean_Type) :
    _tag = '1057'
    ENUM_ORDER_INITIATOR_IS_AGGRESSOR = 'Y'
    ENUM_ORDER_INITIATOR_IS_PASSIVE = 'N'

class NoUndlyInstrumentParties (field_types.NumInGroup_Type) :
    _tag = '1058'

class UndlyInstrumentPartyID (field_types.String_Type) :
    _tag = '1059'

class UndlyInstrumentPartyIDSource (field_types.char_Type) :
    _tag = '1060'

class UndlyInstrumentPartyRole (field_types.int_Type) :
    _tag = '1061'

class NoUndlyInstrumentPartySubIDs (field_types.NumInGroup_Type) :
    _tag = '1062'

class UndlyInstrumentPartySubID (field_types.String_Type) :
    _tag = '1063'

class UndlyInstrumentPartySubIDType (field_types.int_Type) :
    _tag = '1064'

class BidSwapPoints (field_types.PriceOffset_Type) :
    _tag = '1065'

class OfferSwapPoints (field_types.PriceOffset_Type) :
    _tag = '1066'

class LegBidForwardPoints (field_types.PriceOffset_Type) :
    _tag = '1067'

class LegOfferForwardPoints (field_types.PriceOffset_Type) :
    _tag = '1068'

class SwapPoints (field_types.PriceOffset_Type) :
    _tag = '1069'

class MDQuoteType (field_types.int_Type) :
    _tag = '1070'
    ENUM_INDICATIVE = 0
    ENUM_TRADEABLE = 1
    ENUM_RESTRICTED_TRADEABLE = 2
    ENUM_COUNTER = 3
    ENUM_INDICATIVE_AND_TRADEABLE = 4

class LastSwapPoints (field_types.PriceOffset_Type) :
    _tag = '1071'

class SideGrossTradeAmt (field_types.Amt_Type) :
    _tag = '1072'

class LegLastForwardPoints (field_types.PriceOffset_Type) :
    _tag = '1073'

class LegCalculatedCcyLastQty (field_types.Qty_Type) :
    _tag = '1074'

class LegGrossTradeAmt (field_types.Amt_Type) :
    _tag = '1075'

class MaturityTime (field_types.TZTimeOnly_Type) :
    _tag = '1079'

class RefOrderID (field_types.String_Type) :
    _tag = '1080'

class RefOrderIDSource (field_types.char_Type) :
    _tag = '1081'
    ENUM_SECONDARY_ORDER_ID = '0'
    ENUM_ORDER_ID = '1'
    ENUM_MD_ENTRY_ID = '2'
    ENUM_QUOTE_ENTRY_ID = '3'

class SecondaryDisplayQty (field_types.Qty_Type) :
    _tag = '1082'

class DisplayWhen (field_types.char_Type) :
    _tag = '1083'
    ENUM_IMMEDIATE = '1'
    ENUM_EXHAUST = '2'

class DisplayMethod (field_types.char_Type) :
    _tag = '1084'
    ENUM_INITIAL = '1'
    ENUM_NEW = '2'
    ENUM_RANDOM = '3'

class DisplayLowQty (field_types.Qty_Type) :
    _tag = '1085'

class DisplayHighQty (field_types.Qty_Type) :
    _tag = '1086'

class DisplayMinIncr (field_types.Qty_Type) :
    _tag = '1087'

class RefreshQty (field_types.Qty_Type) :
    _tag = '1088'

class MatchIncrement (field_types.Qty_Type) :
    _tag = '1089'

class MaxPriceLevels (field_types.int_Type) :
    _tag = '1090'

class PreTradeAnonymity (field_types.Boolean_Type) :
    _tag = '1091'

class PriceProtectionScope (field_types.char_Type) :
    _tag = '1092'
    ENUM_NONE = '0'
    ENUM_LOCAL = '1'
    ENUM_NATIONAL = '2'
    ENUM_GLOBAL = '3'

class LotType (field_types.char_Type) :
    _tag = '1093'
    ENUM_ODD_LOT = '1'
    ENUM_ROUND_LOT = '2'
    ENUM_BLOCK_LOT = '3'

class PegPriceType (field_types.int_Type) :
    _tag = '1094'
    ENUM_LAST_PEG = 1
    ENUM_MID_PRICE_PEG = 2
    ENUM_OPENING_PEG = 3
    ENUM_MARKET_PEG = 4
    ENUM_PRIMARY_PEG = 5
    ENUM_PEG_TO_VWAP = 7
    ENUM_TRAILING_STOP_PEG = 8
    ENUM_PEG_TO_LIMIT_PRICE = 9

class PeggedRefPrice (field_types.Price_Type) :
    _tag = '1095'

class PegSecurityIDSource (field_types.String_Type) :
    _tag = '1096'

class PegSecurityID (field_types.String_Type) :
    _tag = '1097'

class PegSymbol (field_types.String_Type) :
    _tag = '1098'

class PegSecurityDesc (field_types.String_Type) :
    _tag = '1099'

class TriggerType (field_types.char_Type) :
    _tag = '1100'
    ENUM_PARTIAL_EXECUTION = '1'
    ENUM_SPECIFIED_TRADING_SESSION = '2'
    ENUM_NEXT_AUCTION = '3'
    ENUM_PRICE_MOVEMENT = '4'

class TriggerAction (field_types.char_Type) :
    _tag = '1101'
    ENUM_ACTIVATE = '1'
    ENUM_MODIFY = '2'
    ENUM_CANCEL = '3'

class TriggerPrice (field_types.Price_Type) :
    _tag = '1102'

class TriggerSymbol (field_types.String_Type) :
    _tag = '1103'

class TriggerSecurityID (field_types.String_Type) :
    _tag = '1104'

class TriggerSecurityIDSource (field_types.String_Type) :
    _tag = '1105'

class TriggerSecurityDesc (field_types.String_Type) :
    _tag = '1106'

class TriggerPriceType (field_types.char_Type) :
    _tag = '1107'
    ENUM_BEST_OFFER = '1'
    ENUM_LAST_TRADE = '2'
    ENUM_BEST_BID = '3'
    ENUM_BEST_BID_OR_LAST_TRADE = '4'
    ENUM_BEST_OFFER_OR_LAST_TRADE = '5'
    ENUM_BEST_MID = '6'

class TriggerPriceTypeScope (field_types.char_Type) :
    _tag = '1108'
    ENUM_NONE = '0'
    ENUM_LOCAL = '1'
    ENUM_NATIONAL = '2'
    ENUM_GLOBAL = '3'

class TriggerPriceDirection (field_types.char_Type) :
    _tag = '1109'
    ENUM_UP = 'U'
    ENUM_DOWN = 'D'

class TriggerNewPrice (field_types.Price_Type) :
    _tag = '1110'

class TriggerOrderType (field_types.char_Type) :
    _tag = '1111'
    ENUM_MARKET = '1'
    ENUM_LIMIT = '2'

class TriggerNewQty (field_types.Qty_Type) :
    _tag = '1112'

class TriggerTradingSessionID (field_types.String_Type) :
    _tag = '1113'

class TriggerTradingSessionSubID (field_types.String_Type) :
    _tag = '1114'

class OrderCategory (field_types.char_Type) :
    _tag = '1115'
    ENUM_ORDER = '1'
    ENUM_QUOTE = '2'
    ENUM_PRIVATELY_NEGOTIATED_TRADE = '3'
    ENUM_MULTILEG_ORDER = '4'
    ENUM_LINKED_ORDER = '5'
    ENUM_QUOTE_REQUEST = '6'
    ENUM_IMPLIED_ORDER = '7'
    ENUM_CROSS_ORDER = '8'
    ENUM_STREAMING_PRICE = '9'

class NoRootPartyIDs (field_types.NumInGroup_Type) :
    _tag = '1116'

class RootPartyID (field_types.String_Type) :
    _tag = '1117'

class RootPartyIDSource (field_types.char_Type) :
    _tag = '1118'

class RootPartyRole (field_types.int_Type) :
    _tag = '1119'

class NoRootPartySubIDs (field_types.NumInGroup_Type) :
    _tag = '1120'

class RootPartySubID (field_types.String_Type) :
    _tag = '1121'

class RootPartySubIDType (field_types.int_Type) :
    _tag = '1122'

class TradeHandlingInstr (field_types.char_Type) :
    _tag = '1123'
    ENUM_TRADE_CONFIRMATION = '0'
    ENUM_TWO_PARTY_REPORT = '1'
    ENUM_ONE_PARTY_REPORT_FOR_MATCHING = '2'
    ENUM_ONE_PARTY_REPORT_FOR_PASS_THROUGH = '3'
    ENUM_AUTOMATED_FLOOR_ORDER_ROUTING = '4'
    ENUM_TWO_PARTY_REPORT_FOR_CLAIM = '5'

class OrigTradeHandlingInstr (field_types.char_Type) :
    _tag = '1124'

class OrigTradeDate (field_types.LocalMktDate_Type) :
    _tag = '1125'

class OrigTradeID (field_types.String_Type) :
    _tag = '1126'

class OrigSecondaryTradeID (field_types.String_Type) :
    _tag = '1127'

class ApplVerID (field_types.String_Type) :
    _tag = '1128'
    ENUM_FIX27 = '0'
    ENUM_FIX30 = '1'
    ENUM_FIX40 = '2'
    ENUM_FIX41 = '3'
    ENUM_FIX42 = '4'
    ENUM_FIX43 = '5'
    ENUM_FIX44 = '6'
    ENUM_FIX50 = '7'
    ENUM_FIX50_SP1 = '8'

class CstmApplVerID (field_types.String_Type) :
    _tag = '1129'

class RefApplVerID (field_types.String_Type) :
    _tag = '1130'

class RefCstmApplVerID (field_types.String_Type) :
    _tag = '1131'

class TZTransactTime (field_types.TZTimestamp_Type) :
    _tag = '1132'

class ExDestinationIDSource (field_types.char_Type) :
    _tag = '1133'
    ENUM_BIC = 'B'
    ENUM_GENERAL_IDENTIFIER = 'C'
    ENUM_PROPRIETARY = 'D'
    ENUM_ISO_COUNTRY_CODE = 'E'
    ENUM_MIC = 'G'

class ReportedPxDiff (field_types.Boolean_Type) :
    _tag = '1134'

class RptSys (field_types.String_Type) :
    _tag = '1135'

class AllocClearingFeeIndicator (field_types.String_Type) :
    _tag = '1136'

class DefaultApplVerID (field_types.String_Type) :
    _tag = '1137'

class DisplayQty (field_types.Qty_Type) :
    _tag = '1138'

class ExchangeSpecialInstructions (field_types.String_Type) :
    _tag = '1139'

class UnderlyingMaturityTime (field_types.TZTimeOnly_Type) :
    _tag = '1213'

class LegMaturityTime (field_types.TZTimeOnly_Type) :
    _tag = '1212'

class MaxTradeVol (field_types.Qty_Type) :
    _tag = '1140'

class NoMDFeedTypes (field_types.NumInGroup_Type) :
    _tag = '1141'

class MatchAlgorithm (field_types.String_Type) :
    _tag = '1142'

class MaxPriceVariation (field_types.float_Type) :
    _tag = '1143'

class ImpliedMarketIndicator (field_types.int_Type) :
    _tag = '1144'
    ENUM_NOT_IMPLIED = 0
    ENUM_IMPLIED_IN = 1
    ENUM_IMPLIED_OUT = 2
    ENUM_BOTH_IMPLIED_IN_AND_IMPLIED_OUT = 3

class EventTime (field_types.UTCTimestamp_Type) :
    _tag = '1145'

class MinPriceIncrementAmount (field_types.Amt_Type) :
    _tag = '1146'

class UnitOfMeasureQty (field_types.Qty_Type) :
    _tag = '1147'

class LowLimitPrice (field_types.Price_Type) :
    _tag = '1148'

class HighLimitPrice (field_types.Price_Type) :
    _tag = '1149'

class TradingReferencePrice (field_types.Price_Type) :
    _tag = '1150'

class SecurityGroup (field_types.String_Type) :
    _tag = '1151'

class LegNumber (field_types.int_Type) :
    _tag = '1152'

class SettlementCycleNo (field_types.int_Type) :
    _tag = '1153'

class SideCurrency (field_types.Currency_Type) :
    _tag = '1154'

class SideSettlCurrency (field_types.Currency_Type) :
    _tag = '1155'

class CcyAmt (field_types.Amt_Type) :
    _tag = '1157'

class NoSettlDetails (field_types.NumInGroup_Type) :
    _tag = '1158'

class SettlObligMode (field_types.int_Type) :
    _tag = '1159'
    ENUM_PRELIMINARY = 1
    ENUM_FINAL = 2

class SettlObligMsgID (field_types.String_Type) :
    _tag = '1160'

class SettlObligID (field_types.String_Type) :
    _tag = '1161'

class SettlObligTransType (field_types.char_Type) :
    _tag = '1162'
    ENUM_CANCEL = 'C'
    ENUM_NEW = 'N'
    ENUM_REPLACE = 'R'
    ENUM_RESTATE = 'T'

class SettlObligRefID (field_types.String_Type) :
    _tag = '1163'

class SettlObligSource (field_types.char_Type) :
    _tag = '1164'
    ENUM_INSTRUCTIONS_OF_BROKER = '1'
    ENUM_INSTRUCTIONS_FOR_INSTITUTION = '2'
    ENUM_INVESTOR = '3'

class NoSettlOblig (field_types.NumInGroup_Type) :
    _tag = '1165'

class QuoteMsgID (field_types.String_Type) :
    _tag = '1166'

class QuoteEntryStatus (field_types.int_Type) :
    _tag = '1167'
    ENUM_ACCEPTED = 0
    ENUM_REJECTED = 5
    ENUM_REMOVED_FROM_MARKET = 6
    ENUM_EXPIRED = 7
    ENUM_LOCKED_MARKET_WARNING = 12
    ENUM_CROSS_MARKET_WARNING = 13
    ENUM_CANCELED_DUE_TO_LOCK_MARKET = 14
    ENUM_CANCELED_DUE_TO_CROSS_MARKET = 15
    ENUM_ACTIVE = 16

class TotNoCxldQuotes (field_types.int_Type) :
    _tag = '1168'

class TotNoAccQuotes (field_types.int_Type) :
    _tag = '1169'

class TotNoRejQuotes (field_types.int_Type) :
    _tag = '1170'

class PrivateQuote (field_types.Boolean_Type) :
    _tag = '1171'
    ENUM_PRIVATE_QUOTE = 'Y'
    ENUM_PUBLIC_QUOTE = 'N'

class RespondentType (field_types.int_Type) :
    _tag = '1172'
    ENUM_ALL_MARKET_PARTICIPANTS = 1
    ENUM_SPECIFIED_MARKET_PARTICIPANTS = 2
    ENUM_ALL_MARKET_MAKERS = 3
    ENUM_PRIMARY_MARKET_MAKER = 4

class MDSubBookType (field_types.int_Type) :
    _tag = '1173'

class SecurityTradingEvent (field_types.int_Type) :
    _tag = '1174'
    ENUM_ORDER_IMBALANCE = 1
    ENUM_TRADING_RESUMES = 2
    ENUM_PRICE_VOLATILITY_INTERRUPTION = 3
    ENUM_CHANGE_OF_TRADING_SESSION = 4
    ENUM_CHANGE_OF_TRADING_SUBSESSION = 5
    ENUM_CHANGE_OF_SECURITY_TRADING_STATUS = 6
    ENUM_CHANGE_OF_BOOK_TYPE = 7
    ENUM_CHANGE_OF_MARKET_DEPTH = 8

class NoStatsIndicators (field_types.NumInGroup_Type) :
    _tag = '1175'

class StatsType (field_types.int_Type) :
    _tag = '1176'
    ENUM_EXCHANGE_LAST = 1
    ENUM_HIGH = 2
    ENUM_AVERAGE_PRICE = 3
    ENUM_TURNOVER = 4

class NoOfSecSizes (field_types.NumInGroup_Type) :
    _tag = '1177'

class MDSecSizeType (field_types.int_Type) :
    _tag = '1178'
    ENUM_CUSTOMER = 1

class MDSecSize (field_types.Qty_Type) :
    _tag = '1179'

class ApplID (field_types.String_Type) :
    _tag = '1180'

class ApplSeqNum (field_types.SeqNum_Type) :
    _tag = '1181'

class ApplBegSeqNum (field_types.SeqNum_Type) :
    _tag = '1182'

class ApplEndSeqNum (field_types.SeqNum_Type) :
    _tag = '1183'

class SecurityXMLLen (field_types.Length_Type) :
    _tag = '1184'

class SecurityXML (field_types.XMLData_Type) :
    _tag = '1185'

class SecurityXMLSchema (field_types.String_Type) :
    _tag = '1186'

class RefreshIndicator (field_types.Boolean_Type) :
    _tag = '1187'

class Volatility (field_types.float_Type) :
    _tag = '1188'

class TimeToExpiration (field_types.float_Type) :
    _tag = '1189'

class RiskFreeRate (field_types.float_Type) :
    _tag = '1190'

class PriceUnitOfMeasure (field_types.String_Type) :
    _tag = '1191'

class PriceUnitOfMeasureQty (field_types.Qty_Type) :
    _tag = '1192'

class SettlMethod (field_types.char_Type) :
    _tag = '1193'
    ENUM_CASH_SETTLEMENT_REQUIRED = 'C'
    ENUM_PHYSICAL_SETTLEMENT_REQUIRED = 'P'

class ExerciseStyle (field_types.int_Type) :
    _tag = '1194'
    ENUM_EUROPEAN = 0
    ENUM_AMERICAN = 1
    ENUM_BERMUDA = 2

class UnderlyingExerciseStyle (field_types.int_Type) :
    _tag = '1419'

class LegExerciseStyle (field_types.int_Type) :
    _tag = '1420'

class OptPayAmount (field_types.Amt_Type) :
    _tag = '1195'

class PriceQuoteMethod (field_types.String_Type) :
    _tag = '1196'
    ENUM_STANDARD = 'STD'
    ENUM_INDEX = 'INX'
    ENUM_INTEREST_RATE_INDEX = 'INT'

class FuturesValuationMethod (field_types.String_Type) :
    _tag = '1197'
    ENUM_PREMIUM_STYLE = 'EQTY'
    ENUM_FUTURES_STYLE_MARK_TO_MARKET = 'FUT'
    ENUM_FUTURES_STYLE_WITH_AN_ATTACHED_CASH_ADJUSTMENT = 'FUTDA'

class ListMethod (field_types.int_Type) :
    _tag = '1198'
    ENUM_PRE_LISTED_ONLY = 0
    ENUM_USER_REQUESTED = 1

class CapPrice (field_types.Price_Type) :
    _tag = '1199'

class FloorPrice (field_types.Price_Type) :
    _tag = '1200'

class NoStrikeRules (field_types.NumInGroup_Type) :
    _tag = '1201'

class StartStrikePxRange (field_types.Price_Type) :
    _tag = '1202'

class EndStrikePxRange (field_types.Price_Type) :
    _tag = '1203'

class StrikeIncrement (field_types.float_Type) :
    _tag = '1204'

class NoTickRules (field_types.NumInGroup_Type) :
    _tag = '1205'

class StartTickPriceRange (field_types.Price_Type) :
    _tag = '1206'

class EndTickPriceRange (field_types.Price_Type) :
    _tag = '1207'

class TickIncrement (field_types.Price_Type) :
    _tag = '1208'

class TickRuleType (field_types.int_Type) :
    _tag = '1209'
    ENUM_REGULAR = 0
    ENUM_VARIABLE = 1
    ENUM_FIXED = 2
    ENUM_TRADED_AS_A_SPREAD_LEG = 3
    ENUM_SETTLED_AS_A_SPREAD_LEG = 4

class NestedInstrAttribType (field_types.int_Type) :
    _tag = '1210'

class NestedInstrAttribValue (field_types.String_Type) :
    _tag = '1211'

class DerivativeSymbol (field_types.String_Type) :
    _tag = '1214'

class DerivativeSymbolSfx (field_types.String_Type) :
    _tag = '1215'

class DerivativeSecurityID (field_types.String_Type) :
    _tag = '1216'

class DerivativeSecurityIDSource (field_types.String_Type) :
    _tag = '1217'

class NoDerivativeSecurityAltID (field_types.NumInGroup_Type) :
    _tag = '1218'

class DerivativeSecurityAltID (field_types.String_Type) :
    _tag = '1219'

class DerivativeSecurityAltIDSource (field_types.String_Type) :
    _tag = '1220'

class SecondaryLowLimitPrice (field_types.Price_Type) :
    _tag = '1221'

class SecondaryHighLimitPrice (field_types.Price_Type) :
    _tag = '1230'

class MaturityRuleID (field_types.String_Type) :
    _tag = '1222'

class StrikeRuleID (field_types.String_Type) :
    _tag = '1223'

class DerivativeOptPayAmount (field_types.Amt_Type) :
    _tag = '1225'

class EndMaturityMonthYear (field_types.MonthYear_Type) :
    _tag = '1226'

class ProductComplex (field_types.String_Type) :
    _tag = '1227'

class DerivativeProductComplex (field_types.String_Type) :
    _tag = '1228'

class MaturityMonthYearIncrement (field_types.int_Type) :
    _tag = '1229'

class MinLotSize (field_types.Qty_Type) :
    _tag = '1231'

class NoExecInstRules (field_types.NumInGroup_Type) :
    _tag = '1232'

class NoLotTypeRules (field_types.NumInGroup_Type) :
    _tag = '1234'

class NoMatchRules (field_types.NumInGroup_Type) :
    _tag = '1235'

class NoMaturityRules (field_types.NumInGroup_Type) :
    _tag = '1236'

class NoOrdTypeRules (field_types.NumInGroup_Type) :
    _tag = '1237'

class NoTimeInForceRules (field_types.NumInGroup_Type) :
    _tag = '1239'

class SecondaryTradingReferencePrice (field_types.Price_Type) :
    _tag = '1240'

class StartMaturityMonthYear (field_types.MonthYear_Type) :
    _tag = '1241'

class FlexProductEligibilityIndicator (field_types.Boolean_Type) :
    _tag = '1242'

class DerivFlexProductEligibilityIndicator (field_types.Boolean_Type) :
    _tag = '1243'

class FlexibleIndicator (field_types.Boolean_Type) :
    _tag = '1244'

class TradingCurrency (field_types.Currency_Type) :
    _tag = '1245'

class DerivativeProduct (field_types.int_Type) :
    _tag = '1246'

class DerivativeSecurityGroup (field_types.String_Type) :
    _tag = '1247'

class DerivativeCFICode (field_types.String_Type) :
    _tag = '1248'

class DerivativeSecurityType (field_types.String_Type) :
    _tag = '1249'

class DerivativeSecuritySubType (field_types.String_Type) :
    _tag = '1250'

class DerivativeMaturityMonthYear (field_types.MonthYear_Type) :
    _tag = '1251'

class DerivativeMaturityDate (field_types.LocalMktDate_Type) :
    _tag = '1252'

class DerivativeMaturityTime (field_types.TZTimeOnly_Type) :
    _tag = '1253'

class DerivativeSettleOnOpenFlag (field_types.String_Type) :
    _tag = '1254'

class DerivativeInstrmtAssignmentMethod (field_types.char_Type) :
    _tag = '1255'

class DerivativeSecurityStatus (field_types.String_Type) :
    _tag = '1256'

class DerivativeInstrRegistry (field_types.String_Type) :
    _tag = '1257'

class DerivativeCountryOfIssue (field_types.Country_Type) :
    _tag = '1258'

class DerivativeStateOrProvinceOfIssue (field_types.String_Type) :
    _tag = '1259'

class DerivativeLocaleOfIssue (field_types.String_Type) :
    _tag = '1260'

class DerivativeStrikePrice (field_types.Price_Type) :
    _tag = '1261'

class DerivativeStrikeCurrency (field_types.Currency_Type) :
    _tag = '1262'

class DerivativeStrikeMultiplier (field_types.float_Type) :
    _tag = '1263'

class DerivativeStrikeValue (field_types.float_Type) :
    _tag = '1264'

class DerivativeOptAttribute (field_types.char_Type) :
    _tag = '1265'

class DerivativeContractMultiplier (field_types.float_Type) :
    _tag = '1266'

class DerivativeMinPriceIncrement (field_types.float_Type) :
    _tag = '1267'

class DerivativeMinPriceIncrementAmount (field_types.Amt_Type) :
    _tag = '1268'

class DerivativeUnitOfMeasure (field_types.String_Type) :
    _tag = '1269'

class DerivativeUnitOfMeasureQty (field_types.Qty_Type) :
    _tag = '1270'

class DerivativeTimeUnit (field_types.String_Type) :
    _tag = '1271'

class DerivativeSecurityExchange (field_types.Exchange_Type) :
    _tag = '1272'

class DerivativePositionLimit (field_types.int_Type) :
    _tag = '1273'

class DerivativeNTPositionLimit (field_types.int_Type) :
    _tag = '1274'

class DerivativeIssuer (field_types.String_Type) :
    _tag = '1275'

class DerivativeIssueDate (field_types.LocalMktDate_Type) :
    _tag = '1276'

class DerivativeEncodedIssuerLen (field_types.Length_Type) :
    _tag = '1277'

class DerivativeEncodedIssuer (field_types.data_Type) :
    _tag = '1278'

class DerivativeSecurityDesc (field_types.String_Type) :
    _tag = '1279'

class DerivativeEncodedSecurityDescLen (field_types.Length_Type) :
    _tag = '1280'

class DerivativeEncodedSecurityDesc (field_types.data_Type) :
    _tag = '1281'

class DerivativeSecurityXMLLen (field_types.Length_Type) :
    _tag = '1282'

class DerivativeSecurityXML (field_types.data_Type) :
    _tag = '1283'

class DerivativeSecurityXMLSchema (field_types.String_Type) :
    _tag = '1284'

class DerivativeContractSettlMonth (field_types.MonthYear_Type) :
    _tag = '1285'

class NoDerivativeEvents (field_types.NumInGroup_Type) :
    _tag = '1286'

class DerivativeEventType (field_types.int_Type) :
    _tag = '1287'

class DerivativeEventDate (field_types.LocalMktDate_Type) :
    _tag = '1288'

class DerivativeEventTime (field_types.UTCTimestamp_Type) :
    _tag = '1289'

class DerivativeEventPx (field_types.Price_Type) :
    _tag = '1290'

class DerivativeEventText (field_types.String_Type) :
    _tag = '1291'

class NoDerivativeInstrumentParties (field_types.NumInGroup_Type) :
    _tag = '1292'

class DerivativeInstrumentPartyID (field_types.String_Type) :
    _tag = '1293'

class DerivativeInstrumentPartyIDSource (field_types.String_Type) :
    _tag = '1294'

class DerivativeInstrumentPartyRole (field_types.int_Type) :
    _tag = '1295'

class NoDerivativeInstrumentPartySubIDs (field_types.NumInGroup_Type) :
    _tag = '1296'

class DerivativeInstrumentPartySubID (field_types.String_Type) :
    _tag = '1297'

class DerivativeInstrumentPartySubIDType (field_types.int_Type) :
    _tag = '1298'

class DerivativeExerciseStyle (field_types.char_Type) :
    _tag = '1299'

class MarketSegmentID (field_types.String_Type) :
    _tag = '1300'

class MarketID (field_types.Exchange_Type) :
    _tag = '1301'

class MaturityMonthYearIncrementUnits (field_types.int_Type) :
    _tag = '1302'
    ENUM_MONTHS = 0
    ENUM_DAYS = 1
    ENUM_WEEKS = 2
    ENUM_YEARS = 3

class MaturityMonthYearFormat (field_types.int_Type) :
    _tag = '1303'
    ENUM_YEAR_MONTH_ONLY = 0
    ENUM_YEAR_MONTH_DAY = 1
    ENUM_YEAR_MONTH_WEEK = 2

class StrikeExerciseStyle (field_types.int_Type) :
    _tag = '1304'

class SecondaryPriceLimitType (field_types.int_Type) :
    _tag = '1305'

class PriceLimitType (field_types.int_Type) :
    _tag = '1306'
    ENUM_PRICE = 0
    ENUM_TICKS = 1
    ENUM_PERCENTAGE = 2

class ExecInstValue (field_types.char_Type) :
    _tag = '1308'

class NoTradingSessionRules (field_types.NumInGroup_Type) :
    _tag = '1309'

class NoMarketSegments (field_types.NumInGroup_Type) :
    _tag = '1310'

class NoDerivativeInstrAttrib (field_types.NumInGroup_Type) :
    _tag = '1311'

class NoNestedInstrAttrib (field_types.NumInGroup_Type) :
    _tag = '1312'

class DerivativeInstrAttribType (field_types.int_Type) :
    _tag = '1313'

class DerivativeInstrAttribValue (field_types.String_Type) :
    _tag = '1314'

class DerivativePriceUnitOfMeasure (field_types.String_Type) :
    _tag = '1315'

class DerivativePriceUnitOfMeasureQty (field_types.Qty_Type) :
    _tag = '1316'

class DerivativeSettlMethod (field_types.char_Type) :
    _tag = '1317'

class DerivativePriceQuoteMethod (field_types.String_Type) :
    _tag = '1318'

class DerivativeFuturesValuationMethod (field_types.String_Type) :
    _tag = '1319'

class DerivativeListMethod (field_types.int_Type) :
    _tag = '1320'

class DerivativeCapPrice (field_types.Price_Type) :
    _tag = '1321'

class DerivativeFloorPrice (field_types.Price_Type) :
    _tag = '1322'

class DerivativePutOrCall (field_types.int_Type) :
    _tag = '1323'

class ListUpdateAction (field_types.char_Type) :
    _tag = '1324'

class LegPutOrCall (field_types.int_Type) :
    _tag = '1358'

class LegUnitOfMeasureQty (field_types.Qty_Type) :
    _tag = '1224'

class LegPriceUnitOfMeasure (field_types.String_Type) :
    _tag = '1421'

class LegPriceUnitOfMeasureQty (field_types.Qty_Type) :
    _tag = '1422'

class UnderlyingUnitOfMeasureQty (field_types.Qty_Type) :
    _tag = '1423'

class UnderlyingPriceUnitOfMeasure (field_types.String_Type) :
    _tag = '1424'

class UnderlyingPriceUnitOfMeasureQty (field_types.Qty_Type) :
    _tag = '1425'

class MarketReqID (field_types.String_Type) :
    _tag = '1393'

class MarketReportID (field_types.String_Type) :
    _tag = '1394'

class MarketUpdateAction (field_types.char_Type) :
    _tag = '1395'
    ENUM_ADD = 'A'
    ENUM_DELETE = 'D'
    ENUM_MODIFY = 'M'

class MarketSegmentDesc (field_types.String_Type) :
    _tag = '1396'

class EncodedMktSegmDescLen (field_types.Length_Type) :
    _tag = '1397'

class EncodedMktSegmDesc (field_types.data_Type) :
    _tag = '1398'

class ParentMktSegmID (field_types.String_Type) :
    _tag = '1325'

class TradingSessionDesc (field_types.String_Type) :
    _tag = '1326'

class TradSesUpdateAction (field_types.char_Type) :
    _tag = '1327'

class RejectText (field_types.String_Type) :
    _tag = '1328'

class FeeMultiplier (field_types.float_Type) :
    _tag = '1329'

class UnderlyingLegSymbol (field_types.String_Type) :
    _tag = '1330'

class UnderlyingLegSymbolSfx (field_types.String_Type) :
    _tag = '1331'

class UnderlyingLegSecurityID (field_types.String_Type) :
    _tag = '1332'

class UnderlyingLegSecurityIDSource (field_types.String_Type) :
    _tag = '1333'

class NoUnderlyingLegSecurityAltID (field_types.NumInGroup_Type) :
    _tag = '1334'

class UnderlyingLegSecurityAltID (field_types.String_Type) :
    _tag = '1335'

class UnderlyingLegSecurityAltIDSource (field_types.String_Type) :
    _tag = '1336'

class UnderlyingLegSecurityType (field_types.String_Type) :
    _tag = '1337'

class UnderlyingLegSecuritySubType (field_types.String_Type) :
    _tag = '1338'

class UnderlyingLegMaturityMonthYear (field_types.MonthYear_Type) :
    _tag = '1339'

class UnderlyingLegPutOrCall (field_types.int_Type) :
    _tag = '1343'

class UnderlyingLegStrikePrice (field_types.Price_Type) :
    _tag = '1340'

class UnderlyingLegSecurityExchange (field_types.String_Type) :
    _tag = '1341'

class NoOfLegUnderlyings (field_types.NumInGroup_Type) :
    _tag = '1342'

class UnderlyingLegCFICode (field_types.String_Type) :
    _tag = '1344'

class UnderlyingLegMaturityDate (field_types.LocalMktDate_Type) :
    _tag = '1345'

class UnderlyingLegMaturityTime (field_types.TZTimeOnly_Type) :
    _tag = '1405'

class UnderlyingLegOptAttribute (field_types.char_Type) :
    _tag = '1391'

class UnderlyingLegSecurityDesc (field_types.String_Type) :
    _tag = '1392'

class EncryptedPasswordMethod (field_types.int_Type) :
    _tag = '1400'

class EncryptedPasswordLen (field_types.Length_Type) :
    _tag = '1401'

class EncryptedPassword (field_types.data_Type) :
    _tag = '1402'

class EncryptedNewPasswordLen (field_types.Length_Type) :
    _tag = '1403'

class EncryptedNewPassword (field_types.data_Type) :
    _tag = '1404'

class ApplExtID (field_types.int_Type) :
    _tag = '1156'

class RefApplExtID (field_types.int_Type) :
    _tag = '1406'

class DefaultApplExtID (field_types.int_Type) :
    _tag = '1407'

class DefaultCstmApplVerID (field_types.String_Type) :
    _tag = '1408'

class SessionStatus (field_types.int_Type) :
    _tag = '1409'
    ENUM_SESSION_ACTIVE = 0
    ENUM_SESSION_PASSWORD_CHANGED = 1
    ENUM_SESSION_PASSWORD_DUE_TO_EXPIRE = 2
    ENUM_NEW_SESSION_PASSWORD_DOES_NOT_COMPLY_WITH_POLICY = 3
    ENUM_SESSION_LOGOUT_COMPLETE = 4
    ENUM_INVALID_USERNAME_OR_PASSWORD = 5
    ENUM_ACCOUNT_LOCKED = 6
    ENUM_LOGONS_ARE_NOT_ALLOWED_AT_THIS_TIME = 7
    ENUM_PASSWORD_EXPIRED = 8

class DefaultVerIndicator (field_types.Boolean_Type) :
    _tag = '1410'

class NoUsernames (field_types.NumInGroup_Type) :
    _tag = '809'

class LegAllocSettlCurrency (field_types.Currency_Type) :
    _tag = '1367'

class TotNoFills (field_types.int_Type) :
    _tag = '1361'

class NoFills (field_types.NumInGroup_Type) :
    _tag = '1362'

class FillExecID (field_types.String_Type) :
    _tag = '1363'

class FillPx (field_types.Price_Type) :
    _tag = '1364'

class FillQty (field_types.Qty_Type) :
    _tag = '1365'

class LegAllocID (field_types.String_Type) :
    _tag = '1366'

class TradSesEvent (field_types.int_Type) :
    _tag = '1368'
    ENUM_TRADING_RESUMES = 0
    ENUM_CHANGE_OF_TRADING_SESSION = 1
    ENUM_CHANGE_OF_TRADING_SUBSESSION = 2
    ENUM_CHANGE_OF_TRADING_STATUS = 3

class MassActionReportID (field_types.String_Type) :
    _tag = '1369'

class NoNotAffectedOrders (field_types.NumInGroup_Type) :
    _tag = '1370'

class NotAffectedOrderID (field_types.String_Type) :
    _tag = '1371'

class NotAffOrigClOrdID (field_types.String_Type) :
    _tag = '1372'

class MassActionType (field_types.int_Type) :
    _tag = '1373'
    ENUM_SUSPEND_ORDERS = 1
    ENUM_RELEASE_ORDERS_FROM_SUSPENSION = 2
    ENUM_CANCEL_ORDERS = 3

class MassActionScope (field_types.int_Type) :
    _tag = '1374'
    ENUM_ALL_ORDERS_FOR_A_SECURITY = 1
    ENUM_ALL_ORDERS_FOR_AN_UNDERLYING_SECURITY = 2
    ENUM_ALL_ORDERS_FOR_A_PRODUCT = 3
    ENUM_ALL_ORDERS_FOR_ACFI_CODE = 4
    ENUM_ALL_ORDERS_FOR_A_SECURITY_TYPE = 5
    ENUM_ALL_ORDERS_FOR_A_TRADING_SESSION = 6
    ENUM_ALL_ORDERS = 7
    ENUM_ALL_ORDERS_FOR_A_MARKET = 8
    ENUM_ALL_ORDERS_FOR_A_MARKET_SEGMENT = 9
    ENUM_ALL_ORDERS_FOR_A_SECURITY_GROUP = 10

class MassActionResponse (field_types.int_Type) :
    _tag = '1375'
    ENUM_REJECTED = 0
    ENUM_ACCEPTED = 1

class MassActionRejectReason (field_types.int_Type) :
    _tag = '1376'
    ENUM_MASS_ACTION_NOT_SUPPORTED = 0
    ENUM_INVALID_OR_UNKNOWN_SECURITY = 1
    ENUM_INVALID_OR_UNKNOWN_UNDERLYING_SECURITY = 2
    ENUM_INVALID_OR_UNKNOWN_PRODUCT = 3
    ENUM_INVALID_OR_UNKNOWN_CFI_CODE = 4
    ENUM_INVALID_OR_UNKNOWN_SECURITY_TYPE = 5
    ENUM_INVALID_OR_UNKNOWN_TRADING_SESSION = 6
    ENUM_INVALID_OR_UNKNOWN_MARKET = 7
    ENUM_INVALID_OR_UNKNOWN_MARKET_SEGMENT = 8
    ENUM_INVALID_OR_UNKNOWN_SECURITY_GROUP = 9
    ENUM_OTHER = 99

class MultilegModel (field_types.int_Type) :
    _tag = '1377'
    ENUM_PREDEFINED_MULTILEG_SECURITY = 0
    ENUM_USER_DEFINED_MULTILEG_SECURITY = 1
    ENUM_USER_DEFINED = 2

class MultilegPriceMethod (field_types.int_Type) :
    _tag = '1378'
    ENUM_NET_PRICE = 0
    ENUM_REVERSED_NET_PRICE = 1
    ENUM_YIELD_DIFFERENCE = 2
    ENUM_INDIVIDUAL = 3
    ENUM_CONTRACT_WEIGHTED_AVERAGE_PRICE = 4
    ENUM_MULTIPLIED_PRICE = 5

class LegVolatility (field_types.float_Type) :
    _tag = '1379'

class DividendYield (field_types.Percentage_Type) :
    _tag = '1380'

class LegDividendYield (field_types.Percentage_Type) :
    _tag = '1381'

class CurrencyRatio (field_types.float_Type) :
    _tag = '1382'

class LegCurrencyRatio (field_types.float_Type) :
    _tag = '1383'

class LegExecInst (field_types.MultipleCharValue_Type) :
    _tag = '1384'

class ContingencyType (field_types.int_Type) :
    _tag = '1385'
    ENUM_ONE_CANCELS_THE_OTHER = 1
    ENUM_ONE_TRIGGERS_THE_OTHER = 2
    ENUM_ONE_UPDATES_THE_OTHER_ABSOLUTE = 3
    ENUM_ONE_UPDATES_THE_OTHER_PROPORTIONAL = 4

class ListRejectReason (field_types.int_Type) :
    _tag = '1386'
    ENUM_BROKER_CREDIT = 0
    ENUM_EXCHANGE_CLOSED = 2
    ENUM_TOO_LATE_TO_ENTER = 4
    ENUM_UNKNOWN_ORDER = 5
    ENUM_DUPLICATE_ORDER = 6
    ENUM_UNSUPPORTED_ORDER_CHARACTERISTIC = 11
    ENUM_OTHER = 99

class NoTrdRepIndicators (field_types.NumInGroup_Type) :
    _tag = '1387'

class TrdRepPartyRole (field_types.int_Type) :
    _tag = '1388'

class TrdRepIndicator (field_types.Boolean_Type) :
    _tag = '1389'

class TradePublishIndicator (field_types.int_Type) :
    _tag = '1390'
    ENUM_DO_NOT_PUBLISH_TRADE = 0
    ENUM_PUBLISH_TRADE = 1
    ENUM_DEFERRED_PUBLICATION = 2

class ApplReqID (field_types.String_Type) :
    _tag = '1346'

class ApplReqType (field_types.int_Type) :
    _tag = '1347'
    ENUM_RETRANSMISSION = 0
    ENUM_SUBSCRIPTION = 1
    ENUM_REQUEST_LAST_SEQ_NUM = 2
    ENUM_REQUEST_APPLICATIONS = 3
    ENUM_UNSUBSCRIBE = 4

class ApplResponseType (field_types.int_Type) :
    _tag = '1348'
    ENUM_REQUEST_SUCCESSFULLY_PROCESSED = 0
    ENUM_APPLICATION_DOES_NOT_EXIST = 1
    ENUM_MESSAGES_NOT_AVAILABLE = 2

class ApplTotalMessageCount (field_types.int_Type) :
    _tag = '1349'

class ApplLastSeqNum (field_types.SeqNum_Type) :
    _tag = '1350'

class NoApplIDs (field_types.NumInGroup_Type) :
    _tag = '1351'

class ApplResendFlag (field_types.Boolean_Type) :
    _tag = '1352'

class ApplResponseID (field_types.String_Type) :
    _tag = '1353'

class ApplResponseError (field_types.int_Type) :
    _tag = '1354'
    ENUM_APPLICATION_DOES_NOT_EXIST = 0
    ENUM_MESSAGES_REQUESTED_ARE_NOT_AVAILABLE = 1
    ENUM_USER_NOT_AUTHORIZED_FOR_APPLICATION = 2

class RefApplID (field_types.String_Type) :
    _tag = '1355'

class ApplReportID (field_types.String_Type) :
    _tag = '1356'

class RefApplLastSeqNum (field_types.SeqNum_Type) :
    _tag = '1357'

class ApplNewSeqNum (field_types.SeqNum_Type) :
    _tag = '1399'

class Nested4PartySubIDType (field_types.int_Type) :
    _tag = '1411'

class Nested4PartySubID (field_types.String_Type) :
    _tag = '1412'

class NoNested4PartySubIDs (field_types.NumInGroup_Type) :
    _tag = '1413'

class NoNested4PartyIDs (field_types.NumInGroup_Type) :
    _tag = '1414'

class Nested4PartyID (field_types.String_Type) :
    _tag = '1415'

class Nested4PartyIDSource (field_types.char_Type) :
    _tag = '1416'

class Nested4PartyRole (field_types.int_Type) :
    _tag = '1417'

class LegLastQty (field_types.Qty_Type) :
    _tag = '1418'
