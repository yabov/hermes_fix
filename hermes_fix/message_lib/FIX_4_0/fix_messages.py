
from ... import fix_message
from . import fields
from . import field_types

BEGINSTRING = 'FIX.4.0'
MESSAGE_TYPES = {}


class Header(fix_message.MessageBase):
    def __init__(self):
        super().__init__()
        register_StandardHeader_component(self)
        
class Trailer(fix_message.MessageBase): 
    def __init__(self):
        super().__init__()
        register_StandardTrailer_component(self)
##############Begin Repeating Groups###############
class NoMiscFeesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.MiscFeeAmt, False)
        self.register_field(fields.MiscFeeCurr, False)
        self.register_field(fields.MiscFeeType, False)

class NoOrdersGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.ListID, False)
        self.register_field(fields.WaveNo, False)

class NoExecsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ExecID, False)
        self.register_field(fields.LastShares, False)
        self.register_field(fields.LastPx, False)
        self.register_field(fields.LastMkt, False)

class NoAllocsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.AllocAccount, True)
        self.register_field(fields.AllocShares, True)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.ExecBroker, False)
        self.register_field(fields.ClientID, False)
        self.register_field(fields.Commission, False)
        self.register_field(fields.CommType, False)
        self.register_field(fields.NoDlvyInst, False)
        self.register_field(fields.BrokerOfCredit, False)
        self.register_field(fields.DlvyInst, False)

##############End Repeating Groups###############
##############Begin Componenets###############
def register_StandardHeader_component(self):
    self.register_field(fields.BeginString, True)
    self.register_field(fields.BodyLength, True)
    self.register_field(fields.MsgType, True)
    self.register_field(fields.SenderCompID, True)
    self.register_field(fields.TargetCompID, True)
    self.register_field(fields.OnBehalfOfCompID, False)
    self.register_field(fields.DeliverToCompID, False)
    self.register_field(fields.SecureDataLen, False)
    self.register_field(fields.SecureData, False)
    self.register_field(fields.MsgSeqNum, True)
    self.register_field(fields.SenderSubID, False)
    self.register_field(fields.TargetSubID, False)
    self.register_field(fields.OnBehalfOfSubID, False)
    self.register_field(fields.DeliverToSubID, False)
    self.register_field(fields.PossDupFlag, False)
    self.register_field(fields.PossResend, False)
    self.register_field(fields.SendingTime, True)
    self.register_field(fields.OrigSendingTime, False)

def register_StandardTrailer_component(self):
    self.register_field(fields.SignatureLength, False)
    self.register_field(fields.Signature, False)
    self.register_field(fields.CheckSum, True)

##############End Componenets###############

class Heartbeat(fix_message.MessageBase):
    _msgtype = '0'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TestReqID, False)


MESSAGE_TYPES['0'] = Heartbeat

class TestRequest(fix_message.MessageBase):
    _msgtype = '1'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TestReqID, True)


MESSAGE_TYPES['1'] = TestRequest

class ResendRequest(fix_message.MessageBase):
    _msgtype = '2'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.BeginSeqNo, True)
        self.register_field(fields.EndSeqNo, True)


MESSAGE_TYPES['2'] = ResendRequest

class Reject(fix_message.MessageBase):
    _msgtype = '3'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.RefSeqNum, True)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['3'] = Reject

class SequenceReset(fix_message.MessageBase):
    _msgtype = '4'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.GapFillFlag, False)
        self.register_field(fields.NewSeqNo, True)


MESSAGE_TYPES['4'] = SequenceReset

class Logout(fix_message.MessageBase):
    _msgtype = '5'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.Text, False)


MESSAGE_TYPES['5'] = Logout

class IOI(fix_message.MessageBase):
    _msgtype = '6'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.IOIid, True)
        self.register_field(fields.IOITransType, True)
        self.register_field(fields.IOIRefID, False)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.SecurityID, False)
        self.register_field(fields.IDSource, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.IOIShares, True)
        self.register_field(fields.Price, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ValidUntilTime, False)
        self.register_field(fields.IOIQltyInd, False)
        self.register_field(fields.IOIOthSvc, False)
        self.register_field(fields.IOINaturalFlag, False)
        self.register_field(fields.IOIQualifier, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['6'] = IOI

class Advertisement(fix_message.MessageBase):
    _msgtype = '7'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.AdvId, True)
        self.register_field(fields.AdvTransType, True)
        self.register_field(fields.AdvRefID, False)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.SecurityID, False)
        self.register_field(fields.IDSource, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.AdvSide, True)
        self.register_field(fields.Shares, True)
        self.register_field(fields.Price, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['7'] = Advertisement

class ExecutionReport(fix_message.MessageBase):
    _msgtype = '8'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, True)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.ClientID, False)
        self.register_field(fields.ExecBroker, False)
        self.register_field(fields.ListID, False)
        self.register_field(fields.ExecID, True)
        self.register_field(fields.ExecTransType, True)
        self.register_field(fields.ExecRefID, False)
        self.register_field(fields.OrdStatus, True)
        self.register_field(fields.OrdRejReason, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.SecurityID, False)
        self.register_field(fields.IDSource, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.OrderQty, True)
        self.register_field(fields.OrdType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.Rule80A, False)
        self.register_field(fields.LastShares, True)
        self.register_field(fields.LastPx, True)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.LastCapacity, False)
        self.register_field(fields.CumQty, True)
        self.register_field(fields.AvgPx, True)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.ReportToExch, False)
        self.register_field(fields.Commission, False)
        self.register_field(fields.CommType, False)
        self.register_group(fields.NoMiscFees, NoMiscFeesGroup, False)
        self.register_field(fields.NetMoney, False)
        self.register_field(fields.SettlCurrAmt, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['8'] = ExecutionReport

class OrderCancelReject(fix_message.MessageBase):
    _msgtype = '9'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, True)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.ClientID, False)
        self.register_field(fields.ExecBroker, False)
        self.register_field(fields.ListID, False)
        self.register_field(fields.CxlRejReason, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['9'] = OrderCancelReject

class Logon(fix_message.MessageBase):
    _msgtype = 'A'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.EncryptMethod, True)
        self.register_field(fields.HeartBtInt, True)
        self.register_field(fields.RawDataLength, False)
        self.register_field(fields.RawData, False)


MESSAGE_TYPES['A'] = Logon

class News(fix_message.MessageBase):
    _msgtype = 'B'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrigTime, False)
        self.register_field(fields.Urgency, False)
        self.register_field(fields.RelatdSym, False)
        self.register_field(fields.LinesOfText, True)
        self.register_field(fields.Text, True)
        self.register_field(fields.RawDataLength, False)
        self.register_field(fields.RawData, False)


MESSAGE_TYPES['B'] = News

class Email(fix_message.MessageBase):
    _msgtype = 'C'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.EmailType, True)
        self.register_field(fields.OrigTime, False)
        self.register_field(fields.RelatdSym, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.LinesOfText, True)
        self.register_field(fields.Text, True)
        self.register_field(fields.RawDataLength, False)
        self.register_field(fields.RawData, False)


MESSAGE_TYPES['C'] = Email

class OrderSingle(fix_message.MessageBase):
    _msgtype = 'D'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.ClientID, False)
        self.register_field(fields.ExecBroker, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.HandlInst, True)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.SecurityID, False)
        self.register_field(fields.IDSource, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.OrderQty, True)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.IOIid, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.Commission, False)
        self.register_field(fields.CommType, False)
        self.register_field(fields.Rule80A, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['D'] = OrderSingle

class OrderList(fix_message.MessageBase):
    _msgtype = 'E'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.WaveNo, False)
        self.register_field(fields.ListSeqNo, True)
        self.register_field(fields.ListNoOrds, True)
        self.register_field(fields.ListExecInst, False)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.ClientID, False)
        self.register_field(fields.ExecBroker, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.HandlInst, True)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.SecurityID, False)
        self.register_field(fields.IDSource, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.OrderQty, True)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.Commission, False)
        self.register_field(fields.CommType, False)
        self.register_field(fields.Rule80A, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['E'] = OrderList

class OrderCancelRequest(fix_message.MessageBase):
    _msgtype = 'F'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrigClOrdID, True)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.ListID, False)
        self.register_field(fields.CxlType, True)
        self.register_field(fields.ClientID, False)
        self.register_field(fields.ExecBroker, False)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.SecurityID, False)
        self.register_field(fields.IDSource, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.OrderQty, True)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['F'] = OrderCancelRequest

class OrderCancelReplaceRequest(fix_message.MessageBase):
    _msgtype = 'G'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, False)
        self.register_field(fields.ClientID, False)
        self.register_field(fields.ExecBroker, False)
        self.register_field(fields.OrigClOrdID, True)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.ListID, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.HandlInst, True)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.SecurityID, False)
        self.register_field(fields.IDSource, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.OrderQty, True)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.Commission, False)
        self.register_field(fields.CommType, False)
        self.register_field(fields.Rule80A, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['G'] = OrderCancelReplaceRequest

class OrderStatusRequest(fix_message.MessageBase):
    _msgtype = 'H'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, False)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.ClientID, False)
        self.register_field(fields.ExecBroker, False)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.Side, True)


MESSAGE_TYPES['H'] = OrderStatusRequest

class Allocation(fix_message.MessageBase):
    _msgtype = 'J'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.AllocID, True)
        self.register_field(fields.AllocTransType, True)
        self.register_field(fields.RefAllocID, False)
        self.register_group(fields.NoOrders, NoOrdersGroup, True)
        self.register_group(fields.NoExecs, NoExecsGroup, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.SecurityID, False)
        self.register_field(fields.IDSource, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.Shares, True)
        self.register_field(fields.AvgPx, True)
        self.register_field(fields.Currency, False)
        self.register_field(fields.AvgPrxPrecision, False)
        self.register_field(fields.TradeDate, True)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.NetMoney, False)
        self.register_group(fields.NoMiscFees, NoMiscFeesGroup, False)
        self.register_field(fields.SettlCurrAmt, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.OpenClose, False)
        self.register_field(fields.Text, False)
        self.register_group(fields.NoAllocs, NoAllocsGroup, True)


MESSAGE_TYPES['J'] = Allocation

class ListCancelRequest(fix_message.MessageBase):
    _msgtype = 'K'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.WaveNo, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['K'] = ListCancelRequest

class ListExecute(fix_message.MessageBase):
    _msgtype = 'L'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.WaveNo, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['L'] = ListExecute

class ListStatusRequest(fix_message.MessageBase):
    _msgtype = 'M'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.WaveNo, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['M'] = ListStatusRequest

class ListStatus(fix_message.MessageBase):
    _msgtype = 'N'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.WaveNo, False)
        self.register_field(fields.NoRpts, True)
        self.register_field(fields.RptSeq, True)
        self.register_group(fields.NoOrders, NoOrdersGroup, True)


MESSAGE_TYPES['N'] = ListStatus

class AllocationInstructionAck(fix_message.MessageBase):
    _msgtype = 'P'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ClientID, False)
        self.register_field(fields.ExecBroker, False)
        self.register_field(fields.AllocID, True)
        self.register_field(fields.TradeDate, True)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.AllocStatus, True)
        self.register_field(fields.AllocRejCode, False)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['P'] = AllocationInstructionAck

class DontKnowTrade(fix_message.MessageBase):
    _msgtype = 'Q'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, False)
        self.register_field(fields.ExecID, False)
        self.register_field(fields.DKReason, True)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.Side, True)
        self.register_field(fields.OrderQty, True)
        self.register_field(fields.LastShares, True)
        self.register_field(fields.LastPx, True)
        self.register_field(fields.Text, False)


MESSAGE_TYPES['Q'] = DontKnowTrade

class QuoteRequest(fix_message.MessageBase):
    _msgtype = 'R'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.QuoteReqID, True)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.SecurityID, False)
        self.register_field(fields.IDSource, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.Side, False)
        self.register_field(fields.OrderQty, False)


MESSAGE_TYPES['R'] = QuoteRequest

class Quote(fix_message.MessageBase):
    _msgtype = 'S'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.QuoteReqID, False)
        self.register_field(fields.QuoteID, True)
        self.register_field(fields.Symbol, True)
        self.register_field(fields.SymbolSfx, False)
        self.register_field(fields.SecurityID, False)
        self.register_field(fields.IDSource, False)
        self.register_field(fields.Issuer, False)
        self.register_field(fields.SecurityDesc, False)
        self.register_field(fields.BidPx, True)
        self.register_field(fields.OfferPx, False)
        self.register_field(fields.BidSize, False)
        self.register_field(fields.OfferSize, False)
        self.register_field(fields.ValidUntilTime, False)


MESSAGE_TYPES['S'] = Quote
