
import fix_message
from . import fields
from . import field_types

BEGINSTRING = 'FIX.4.3'
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
class NoSecurityAltIDGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.SecurityAltID, False)
        self.register_field(fields.SecurityAltIDSource, False)

class NoLegSecurityAltIDGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.LegSecurityAltID, False)
        self.register_field(fields.LegSecurityAltIDSource, False)

class NoNestedPartyIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.NestedPartyID, False)
        self.register_field(fields.NestedPartyIDSource, False)
        self.register_field(fields.NestedPartyRole, False)
        self.register_field(fields.NestedPartySubID, False)

class NoPartyIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.PartyID, False)
        self.register_field(fields.PartyIDSource, False)
        self.register_field(fields.PartyRole, False)
        self.register_field(fields.PartySubID, False)

class NoStipulationsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.StipulationType, False)
        self.register_field(fields.StipulationValue, False)

class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.UnderlyingSecurityAltID, False)
        self.register_field(fields.UnderlyingSecurityAltIDSource, False)

class NoHopsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.HopCompID, False)
        self.register_field(fields.HopSendingTime, False)
        self.register_field(fields.HopRefID, False)

class NoIOIQualifiersGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.IOIQualifier, False)

class NoRoutingIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.RoutingType, False)
        self.register_field(fields.RoutingID, False)

class NoContraBrokersGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ContraBroker, False)
        self.register_field(fields.ContraTrader, False)
        self.register_field(fields.ContraTradeQty, False)
        self.register_field(fields.ContraTradeTime, False)
        self.register_field(fields.ContraLegRefID, False)

class NoContAmtsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ContAmtType, False)
        self.register_field(fields.ContAmtValue, False)
        self.register_field(fields.ContAmtCurr, False)

class NoLegsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        register_InstrumentLeg_component(self)
        self.register_field(fields.LegPositionEffect, False)
        self.register_field(fields.LegCoveredOrUncovered, False)
        register_NestedParties_component(self)
        self.register_field(fields.LegRefID, False)
        self.register_field(fields.LegPrice, False)
        self.register_field(fields.LegSettlmntTyp, False)
        self.register_field(fields.LegFutSettDate, False)
        self.register_field(fields.LegLastPx, False)

class NoMsgTypesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.RefMsgType, False)
        self.register_field(fields.MsgDirection, False)

class NoRelatedSymGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        register_Instrument_component(self)

class LinesOfTextGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.Text, True)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)

class NoAllocsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.AllocAccount, False)
        self.register_field(fields.IndividualAllocID, False)
        register_NestedParties_component(self)
        self.register_field(fields.AllocQty, False)

class NoTradingSessionsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)

class NoOrdersGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ListSeqNo, True)
        self.register_field(fields.ClOrdLinkID, False)
        self.register_field(fields.SettlInstMode, False)
        register_Parties_component(self)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_group(fields.NoAllocs, NoAllocsGroup, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.HandlInst, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_group(fields.NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(fields.ProcessCode, False)
        register_Instrument_component(self)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.SideValueInd, False)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, False)
        register_Stipulations_component(self)
        self.register_field(fields.QuantityType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.IOIid, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        register_CommissionData_component(self)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.Rule80A, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.FutSettDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.Price2, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.CoveredOrUncovered, False)
        self.register_field(fields.MaxShow, False)
        self.register_field(fields.PegDifference, False)
        self.register_field(fields.DiscretionInst, False)
        self.register_field(fields.DiscretionOffset, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.NetMoney, False)

class NoExecsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.LastQty, False)
        self.register_field(fields.ExecID, False)
        self.register_field(fields.SecondaryExecID, False)
        self.register_field(fields.LastPx, False)
        self.register_field(fields.LastCapacity, False)

class NoMiscFeesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.MiscFeeAmt, False)
        self.register_field(fields.MiscFeeCurr, False)
        self.register_field(fields.MiscFeeType, False)

class NoMDEntryTypesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.MDEntryType, True)

class NoMDEntriesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.MDEntryType, True)
        self.register_field(fields.MDEntryPx, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.MDEntrySize, False)
        self.register_field(fields.MDEntryDate, False)
        self.register_field(fields.MDEntryTime, False)
        self.register_field(fields.TickDirection, False)
        self.register_field(fields.MDMkt, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.QuoteCondition, False)
        self.register_field(fields.TradeCondition, False)
        self.register_field(fields.MDEntryOriginator, False)
        self.register_field(fields.LocationID, False)
        self.register_field(fields.DeskID, False)
        self.register_field(fields.OpenCloseSettleFlag, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.SellerDays, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.QuoteEntryID, False)
        self.register_field(fields.MDEntryBuyer, False)
        self.register_field(fields.MDEntrySeller, False)
        self.register_field(fields.NumberOfOrders, False)
        self.register_field(fields.MDEntryPositionNo, False)
        self.register_field(fields.Scope, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)

class NoQuoteEntriesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        register_Instrument_component(self)

class NoQuoteSetsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.QuoteSetID, False)
        register_UnderlyingInstrument_component(self)
        self.register_field(fields.TotQuoteEntries, False)
        self.register_group(fields.NoQuoteEntries, NoQuoteEntriesGroup, False)

class NoBidDescriptorsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.BidDescriptorType, False)
        self.register_field(fields.BidDescriptor, False)
        self.register_field(fields.SideValueInd, False)
        self.register_field(fields.LiquidityValue, False)
        self.register_field(fields.LiquidityNumSecurities, False)
        self.register_field(fields.LiquidityPctLow, False)
        self.register_field(fields.LiquidityPctHigh, False)
        self.register_field(fields.EFPTrackingError, False)
        self.register_field(fields.FairValue, False)
        self.register_field(fields.OutsideIndexPct, False)
        self.register_field(fields.ValueOfFutures, False)

class NoBidComponentsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ListID, False)
        self.register_field(fields.Side, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.NetGrossInd, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.Account, False)

class NoStrikesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        register_Instrument_component(self)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.Side, False)
        self.register_field(fields.Price, True)
        self.register_field(fields.Currency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)

class NoRegistDtlsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.RegistDetls, False)
        self.register_field(fields.RegistEmail, False)
        self.register_field(fields.MailingDtls, False)
        self.register_field(fields.MailingInst, False)
        register_NestedParties_component(self)
        self.register_field(fields.OwnerType, False)
        self.register_field(fields.DateOfBirth, False)
        self.register_field(fields.InvestorCountryOfResidence, False)

class NoDistribInstsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.DistribPaymentMethod, False)
        self.register_field(fields.DistribPercentage, False)
        self.register_field(fields.CashDistribCurr, False)
        self.register_field(fields.CashDistribAgentName, False)
        self.register_field(fields.CashDistribAgentCode, False)
        self.register_field(fields.CashDistribAgentAcctNumber, False)
        self.register_field(fields.CashDistribPayRef, False)

class NoAffectedOrdersGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.OrigClOrdID, False)
        self.register_field(fields.AffectedOrderID, False)
        self.register_field(fields.AffectedSecondaryOrderID, False)

class NoSidesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.Side, True)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ClOrdLinkID, False)
        register_Parties_component(self)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_group(fields.NoAllocs, NoAllocsGroup, False)
        self.register_field(fields.QuantityType, False)
        register_OrderQtyData_component(self)
        register_CommissionData_component(self)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.CoveredOrUncovered, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.SideComplianceID, False)

class NoSecurityTypesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.SecurityType, False)
        self.register_field(fields.Product, False)
        self.register_field(fields.CFICode, False)

class NoDatesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.TransactTime, False)

class NoClearingInstructionsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ClearingInstruction, False)

##############End Repeating Groups###############
##############Begin Componenets###############
def register_CommissionData_component(self):
    self.register_field(fields.Commission, False)
    self.register_field(fields.CommType, False)
    self.register_field(fields.CommCurrency, False)
    self.register_field(fields.FundRenewWaiv, False)

def register_Instrument_component(self):
    self.register_field(fields.Symbol, False)
    self.register_field(fields.SymbolSfx, False)
    self.register_field(fields.SecurityID, False)
    self.register_field(fields.SecurityIDSource, False)
    self.register_group(fields.NoSecurityAltID, NoSecurityAltIDGroup, False)
    self.register_field(fields.Product, False)
    self.register_field(fields.CFICode, False)
    self.register_field(fields.SecurityType, False)
    self.register_field(fields.MaturityMonthYear, False)
    self.register_field(fields.MaturityDate, False)
    self.register_field(fields.CouponPaymentDate, False)
    self.register_field(fields.IssueDate, False)
    self.register_field(fields.RepoCollateralSecurityType, False)
    self.register_field(fields.RepurchaseTerm, False)
    self.register_field(fields.RepurchaseRate, False)
    self.register_field(fields.Factor, False)
    self.register_field(fields.CreditRating, False)
    self.register_field(fields.InstrRegistry, False)
    self.register_field(fields.CountryOfIssue, False)
    self.register_field(fields.StateOrProvinceOfIssue, False)
    self.register_field(fields.LocaleOfIssue, False)
    self.register_field(fields.RedemptionDate, False)
    self.register_field(fields.StrikePrice, False)
    self.register_field(fields.OptAttribute, False)
    self.register_field(fields.ContractMultiplier, False)
    self.register_field(fields.CouponRate, False)
    self.register_field(fields.SecurityExchange, False)
    self.register_field(fields.Issuer, False)
    self.register_field(fields.EncodedIssuerLen, False)
    self.register_field(fields.EncodedIssuer, False)
    self.register_field(fields.SecurityDesc, False)
    self.register_field(fields.EncodedSecurityDescLen, False)
    self.register_field(fields.EncodedSecurityDesc, False)

def register_InstrumentLeg_component(self):
    self.register_field(fields.LegSymbol, False)
    self.register_field(fields.LegSymbolSfx, False)
    self.register_field(fields.LegSecurityID, False)
    self.register_field(fields.LegSecurityIDSource, False)
    self.register_group(fields.NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)
    self.register_field(fields.LegProduct, False)
    self.register_field(fields.LegCFICode, False)
    self.register_field(fields.LegSecurityType, False)
    self.register_field(fields.LegMaturityMonthYear, False)
    self.register_field(fields.LegMaturityDate, False)
    self.register_field(fields.LegCouponPaymentDate, False)
    self.register_field(fields.LegIssueDate, False)
    self.register_field(fields.LegRepoCollateralSecurityType, False)
    self.register_field(fields.LegRepurchaseTerm, False)
    self.register_field(fields.LegRepurchaseRate, False)
    self.register_field(fields.LegFactor, False)
    self.register_field(fields.LegCreditRating, False)
    self.register_field(fields.LegInstrRegistry, False)
    self.register_field(fields.LegCountryOfIssue, False)
    self.register_field(fields.LegStateOrProvinceOfIssue, False)
    self.register_field(fields.LegLocaleOfIssue, False)
    self.register_field(fields.LegRedemptionDate, False)
    self.register_field(fields.LegStrikePrice, False)
    self.register_field(fields.LegOptAttribute, False)
    self.register_field(fields.LegContractMultiplier, False)
    self.register_field(fields.LegCouponRate, False)
    self.register_field(fields.LegSecurityExchange, False)
    self.register_field(fields.LegIssuer, False)
    self.register_field(fields.EncodedLegIssuerLen, False)
    self.register_field(fields.EncodedLegIssuer, False)
    self.register_field(fields.LegSecurityDesc, False)
    self.register_field(fields.EncodedLegSecurityDescLen, False)
    self.register_field(fields.EncodedLegSecurityDesc, False)
    self.register_field(fields.LegRatioQty, False)
    self.register_field(fields.LegSide, False)

def register_NestedParties_component(self):
    self.register_group(fields.NoNestedPartyIDs, NoNestedPartyIDsGroup, False)

def register_OrderQtyData_component(self):
    self.register_field(fields.OrderQty, False)
    self.register_field(fields.CashOrderQty, False)
    self.register_field(fields.OrderPercent, False)
    self.register_field(fields.RoundingDirection, False)
    self.register_field(fields.RoundingModulus, False)

def register_Parties_component(self):
    self.register_group(fields.NoPartyIDs, NoPartyIDsGroup, False)

def register_SpreadOrBenchmarkCurveData_component(self):
    self.register_field(fields.Spread, False)
    self.register_field(fields.BenchmarkCurveCurrency, False)
    self.register_field(fields.BenchmarkCurveName, False)
    self.register_field(fields.BenchmarkCurvePoint, False)

def register_Stipulations_component(self):
    self.register_group(fields.NoStipulations, NoStipulationsGroup, False)

def register_UnderlyingInstrument_component(self):
    self.register_field(fields.UnderlyingSymbol, False)
    self.register_field(fields.UnderlyingSymbolSfx, False)
    self.register_field(fields.UnderlyingSecurityID, False)
    self.register_field(fields.UnderlyingSecurityIDSource, False)
    self.register_group(fields.NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)
    self.register_field(fields.UnderlyingProduct, False)
    self.register_field(fields.UnderlyingCFICode, False)
    self.register_field(fields.UnderlyingSecurityType, False)
    self.register_field(fields.UnderlyingMaturityMonthYear, False)
    self.register_field(fields.UnderlyingMaturityDate, False)
    self.register_field(fields.UnderlyingPutOrCall, False)
    self.register_field(fields.UnderlyingCouponPaymentDate, False)
    self.register_field(fields.UnderlyingIssueDate, False)
    self.register_field(fields.UnderlyingRepoCollateralSecurityType, False)
    self.register_field(fields.UnderlyingRepurchaseTerm, False)
    self.register_field(fields.UnderlyingRepurchaseRate, False)
    self.register_field(fields.UnderlyingFactor, False)
    self.register_field(fields.UnderlyingCreditRating, False)
    self.register_field(fields.UnderlyingInstrRegistry, False)
    self.register_field(fields.UnderlyingCountryOfIssue, False)
    self.register_field(fields.UnderlyingStateOrProvinceOfIssue, False)
    self.register_field(fields.UnderlyingLocaleOfIssue, False)
    self.register_field(fields.UnderlyingRedemptionDate, False)
    self.register_field(fields.UnderlyingStrikePrice, False)
    self.register_field(fields.UnderlyingOptAttribute, False)
    self.register_field(fields.UnderlyingContractMultiplier, False)
    self.register_field(fields.UnderlyingCouponRate, False)
    self.register_field(fields.UnderlyingSecurityExchange, False)
    self.register_field(fields.UnderlyingIssuer, False)
    self.register_field(fields.EncodedUnderlyingIssuerLen, False)
    self.register_field(fields.EncodedUnderlyingIssuer, False)
    self.register_field(fields.UnderlyingSecurityDesc, False)
    self.register_field(fields.EncodedUnderlyingSecurityDescLen, False)
    self.register_field(fields.EncodedUnderlyingSecurityDesc, False)

def register_YieldData_component(self):
    self.register_field(fields.YieldType, False)
    self.register_field(fields.Yield, False)

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
    self.register_field(fields.SenderLocationID, False)
    self.register_field(fields.TargetSubID, False)
    self.register_field(fields.TargetLocationID, False)
    self.register_field(fields.OnBehalfOfSubID, False)
    self.register_field(fields.OnBehalfOfLocationID, False)
    self.register_field(fields.DeliverToSubID, False)
    self.register_field(fields.DeliverToLocationID, False)
    self.register_field(fields.PossDupFlag, False)
    self.register_field(fields.PossResend, False)
    self.register_field(fields.SendingTime, True)
    self.register_field(fields.OrigSendingTime, False)
    self.register_field(fields.XmlDataLen, False)
    self.register_field(fields.XmlData, False)
    self.register_field(fields.MessageEncoding, False)
    self.register_field(fields.LastMsgSeqNumProcessed, False)
    self.register_field(fields.OnBehalfOfSendingTime, False)
    self.register_group(fields.NoHops, NoHopsGroup, False)

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
        self.register_field(fields.RefTagID, False)
        self.register_field(fields.RefMsgType, False)
        self.register_field(fields.SessionRejectReason, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


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
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


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
        register_Instrument_component(self)
        self.register_field(fields.Side, True)
        self.register_field(fields.QuantityType, False)
        self.register_field(fields.IOIQty, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ValidUntilTime, False)
        self.register_field(fields.IOIQltyInd, False)
        self.register_field(fields.IOINaturalFlag, False)
        self.register_group(fields.NoIOIQualifiers, NoIOIQualifiersGroup, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.URLLink, False)
        self.register_group(fields.NoRoutingIDs, NoRoutingIDsGroup, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        self.register_field(fields.Benchmark, False)


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
        register_Instrument_component(self)
        self.register_field(fields.AdvSide, True)
        self.register_field(fields.Quantity, True)
        self.register_field(fields.Price, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.URLLink, False)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)


MESSAGE_TYPES['7'] = Advertisement

class ExecutionReport(fix_message.MessageBase):
    _msgtype = '8'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, True)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.SecondaryExecID, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.OrigClOrdID, False)
        self.register_field(fields.ClOrdLinkID, False)
        register_Parties_component(self)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_group(fields.NoContraBrokers, NoContraBrokersGroup, False)
        self.register_field(fields.ListID, False)
        self.register_field(fields.CrossID, False)
        self.register_field(fields.OrigCrossID, False)
        self.register_field(fields.CrossType, False)
        self.register_field(fields.ExecID, True)
        self.register_field(fields.ExecRefID, False)
        self.register_field(fields.ExecType, True)
        self.register_field(fields.OrdStatus, True)
        self.register_field(fields.WorkingIndicator, False)
        self.register_field(fields.OrdRejReason, False)
        self.register_field(fields.ExecRestatementReason, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        register_Instrument_component(self)
        self.register_field(fields.Side, True)
        register_Stipulations_component(self)
        self.register_field(fields.QuantityType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        self.register_field(fields.PegDifference, False)
        self.register_field(fields.DiscretionInst, False)
        self.register_field(fields.DiscretionOffset, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.Rule80A, False)
        self.register_field(fields.LastQty, False)
        self.register_field(fields.UnderlyingLastQty, False)
        self.register_field(fields.LastPx, False)
        self.register_field(fields.UnderlyingLastPx, False)
        self.register_field(fields.LastSpotRate, False)
        self.register_field(fields.LastForwardPoints, False)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.LastCapacity, False)
        self.register_field(fields.LeavesQty, True)
        self.register_field(fields.CumQty, True)
        self.register_field(fields.AvgPx, True)
        self.register_field(fields.DayOrderQty, False)
        self.register_field(fields.DayCumQty, False)
        self.register_field(fields.DayAvgPx, False)
        self.register_field(fields.GTBookingInst, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.ReportToExch, False)
        register_CommissionData_component(self)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        self.register_field(fields.GrossTradeAmt, False)
        self.register_field(fields.NumDaysInterest, False)
        self.register_field(fields.ExDate, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.TradedFlatSwitch, False)
        self.register_field(fields.BasisFeatureDate, False)
        self.register_field(fields.BasisFeaturePrice, False)
        self.register_field(fields.Concession, False)
        self.register_field(fields.TotalTakedown, False)
        self.register_field(fields.NetMoney, False)
        self.register_field(fields.SettlCurrAmt, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.SettlCurrFxRate, False)
        self.register_field(fields.SettlCurrFxRateCalc, False)
        self.register_field(fields.HandlInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.MaxShow, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.FutSettDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.LastForwardPoints2, False)
        self.register_field(fields.MultiLegReportingType, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.TransBkdTime, False)
        self.register_field(fields.ExecValuationPoint, False)
        self.register_field(fields.ExecPriceType, False)
        self.register_field(fields.ExecPriceAdjustment, False)
        self.register_field(fields.PriorityIndicator, False)
        self.register_field(fields.PriceImprovement, False)
        self.register_group(fields.NoContAmts, NoContAmtsGroup, False)
        self.register_group(fields.NoLegs, NoLegsGroup, False)


MESSAGE_TYPES['8'] = ExecutionReport

class OrderCancelReject(fix_message.MessageBase):
    _msgtype = '9'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, True)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.ClOrdLinkID, False)
        self.register_field(fields.OrigClOrdID, True)
        self.register_field(fields.OrdStatus, True)
        self.register_field(fields.WorkingIndicator, False)
        self.register_field(fields.OrigOrdModTime, False)
        self.register_field(fields.ListID, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.CxlRejResponseTo, True)
        self.register_field(fields.CxlRejReason, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


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
        self.register_field(fields.ResetSeqNumFlag, False)
        self.register_field(fields.MaxMessageSize, False)
        self.register_group(fields.NoMsgTypes, NoMsgTypesGroup, False)
        self.register_field(fields.TestMessageIndicator, False)
        self.register_field(fields.Username, False)
        self.register_field(fields.Password, False)


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
        self.register_field(fields.Headline, True)
        self.register_field(fields.EncodedHeadlineLen, False)
        self.register_field(fields.EncodedHeadline, False)
        self.register_group(fields.NoRoutingIDs, NoRoutingIDsGroup, False)
        self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, False)
        self.register_group(fields.LinesOfText, LinesOfTextGroup, True)
        self.register_field(fields.URLLink, False)
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
        self.register_field(fields.EmailThreadID, True)
        self.register_field(fields.EmailType, True)
        self.register_field(fields.OrigTime, False)
        self.register_field(fields.Subject, True)
        self.register_field(fields.EncodedSubjectLen, False)
        self.register_field(fields.EncodedSubject, False)
        self.register_group(fields.NoRoutingIDs, NoRoutingIDsGroup, False)
        self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.ClOrdID, False)
        self.register_group(fields.LinesOfText, LinesOfTextGroup, True)
        self.register_field(fields.RawDataLength, False)
        self.register_field(fields.RawData, False)


MESSAGE_TYPES['C'] = Email

class NewOrderSingle(fix_message.MessageBase):
    _msgtype = 'D'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ClOrdLinkID, False)
        register_Parties_component(self)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_group(fields.NoAllocs, NoAllocsGroup, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.HandlInst, True)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_group(fields.NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(fields.ProcessCode, False)
        register_Instrument_component(self)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, True)
        register_Stipulations_component(self)
        self.register_field(fields.QuantityType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.IOIid, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        register_CommissionData_component(self)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.Rule80A, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.FutSettDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.Price2, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.CoveredOrUncovered, False)
        self.register_field(fields.MaxShow, False)
        self.register_field(fields.PegDifference, False)
        self.register_field(fields.DiscretionInst, False)
        self.register_field(fields.DiscretionOffset, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.NetMoney, False)


MESSAGE_TYPES['D'] = NewOrderSingle

class NewOrderList(fix_message.MessageBase):
    _msgtype = 'E'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.BidID, False)
        self.register_field(fields.ClientBidID, False)
        self.register_field(fields.ProgRptReqs, False)
        self.register_field(fields.BidType, True)
        self.register_field(fields.ProgPeriodInterval, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.ListExecInstType, False)
        self.register_field(fields.ListExecInst, False)
        self.register_field(fields.EncodedListExecInstLen, False)
        self.register_field(fields.EncodedListExecInst, False)
        self.register_field(fields.TotNoOrders, True)
        self.register_group(fields.NoOrders, NoOrdersGroup, True)


MESSAGE_TYPES['E'] = NewOrderList

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
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ClOrdLinkID, False)
        self.register_field(fields.ListID, False)
        self.register_field(fields.OrigOrdModTime, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        register_Parties_component(self)
        register_Instrument_component(self)
        self.register_field(fields.Side, True)
        self.register_field(fields.TransactTime, True)
        register_OrderQtyData_component(self)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['F'] = OrderCancelRequest

class OrderCancelReplaceRequest(fix_message.MessageBase):
    _msgtype = 'G'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, False)
        register_Parties_component(self)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.OrigClOrdID, True)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ClOrdLinkID, False)
        self.register_field(fields.ListID, False)
        self.register_field(fields.OrigOrdModTime, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_group(fields.NoAllocs, NoAllocsGroup, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.HandlInst, True)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_group(fields.NoTradingSessions, NoTradingSessionsGroup, False)
        register_Instrument_component(self)
        self.register_field(fields.Side, True)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.QuantityType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        self.register_field(fields.PegDifference, False)
        self.register_field(fields.DiscretionInst, False)
        self.register_field(fields.DiscretionOffset, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        register_CommissionData_component(self)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.Rule80A, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.FutSettDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.Price2, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.CoveredOrUncovered, False)
        self.register_field(fields.MaxShow, False)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.NetMoney, False)


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
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ClOrdLinkID, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        register_Instrument_component(self)
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
        self.register_field(fields.AllocType, True)
        self.register_field(fields.RefAllocID, False)
        self.register_field(fields.AllocLinkID, False)
        self.register_field(fields.AllocLinkType, False)
        self.register_field(fields.BookingRefID, False)
        self.register_group(fields.NoOrders, NoOrdersGroup, False)
        self.register_group(fields.NoExecs, NoExecsGroup, False)
        self.register_field(fields.Side, True)
        register_Instrument_component(self)
        self.register_field(fields.Quantity, True)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.AvgPx, True)
        self.register_field(fields.Currency, False)
        self.register_field(fields.AvgPrxPrecision, False)
        register_Parties_component(self)
        self.register_field(fields.TradeDate, True)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.GrossTradeAmt, False)
        self.register_field(fields.Concession, False)
        self.register_field(fields.TotalTakedown, False)
        self.register_field(fields.NetMoney, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.NumDaysInterest, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.TotalAccruedInterestAmt, False)
        self.register_field(fields.LegalConfirm, False)
        self.register_group(fields.NoAllocs, NoAllocsGroup, False)


MESSAGE_TYPES['J'] = Allocation

class ListCancelRequest(fix_message.MessageBase):
    _msgtype = 'K'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['K'] = ListCancelRequest

class ListExecute(fix_message.MessageBase):
    _msgtype = 'L'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.ClientBidID, False)
        self.register_field(fields.BidID, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['L'] = ListExecute

class ListStatusRequest(fix_message.MessageBase):
    _msgtype = 'M'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['M'] = ListStatusRequest

class ListStatus(fix_message.MessageBase):
    _msgtype = 'N'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.ListStatusType, True)
        self.register_field(fields.NoRpts, True)
        self.register_field(fields.ListOrderStatus, True)
        self.register_field(fields.RptSeq, True)
        self.register_field(fields.ListStatusText, False)
        self.register_field(fields.EncodedListStatusTextLen, False)
        self.register_field(fields.EncodedListStatusText, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.TotNoOrders, True)
        self.register_group(fields.NoOrders, NoOrdersGroup, True)


MESSAGE_TYPES['N'] = ListStatus

class AllocationAck(fix_message.MessageBase):
    _msgtype = 'P'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        register_Parties_component(self)
        self.register_field(fields.AllocID, True)
        self.register_field(fields.TradeDate, True)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.AllocStatus, True)
        self.register_field(fields.AllocRejCode, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.LegalConfirm, False)


MESSAGE_TYPES['P'] = AllocationAck

class DontKnowTrade(fix_message.MessageBase):
    _msgtype = 'Q'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, True)
        self.register_field(fields.ExecID, True)
        self.register_field(fields.DKReason, True)
        register_Instrument_component(self)
        self.register_field(fields.Side, True)
        register_OrderQtyData_component(self)
        self.register_field(fields.LastQty, False)
        self.register_field(fields.LastPx, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['Q'] = DontKnowTrade

class QuoteRequest(fix_message.MessageBase):
    _msgtype = 'R'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.QuoteReqID, True)
        self.register_field(fields.RFQReqID, False)
        self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, True)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


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
        self.register_field(fields.QuoteType, False)
        self.register_field(fields.QuoteResponseLevel, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_Instrument_component(self)
        self.register_field(fields.BidPx, False)
        self.register_field(fields.OfferPx, False)
        self.register_field(fields.MktBidPx, False)
        self.register_field(fields.MktOfferPx, False)
        self.register_field(fields.MinBidSize, False)
        self.register_field(fields.BidSize, False)
        self.register_field(fields.MinOfferSize, False)
        self.register_field(fields.OfferSize, False)
        self.register_field(fields.ValidUntilTime, False)
        self.register_field(fields.BidSpotRate, False)
        self.register_field(fields.OfferSpotRate, False)
        self.register_field(fields.BidForwardPoints, False)
        self.register_field(fields.OfferForwardPoints, False)
        self.register_field(fields.MidPx, False)
        self.register_field(fields.BidYield, False)
        self.register_field(fields.MidYield, False)
        self.register_field(fields.OfferYield, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.OrdType, False)
        self.register_field(fields.FutSettDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.BidForwardPoints2, False)
        self.register_field(fields.OfferForwardPoints2, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.SettlCurrBidFxRate, False)
        self.register_field(fields.SettlCurrOfferFxRate, False)
        self.register_field(fields.SettlCurrFxRateCalc, False)
        self.register_field(fields.Commission, False)
        self.register_field(fields.CommType, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['S'] = Quote

class SettlementInstructions(fix_message.MessageBase):
    _msgtype = 'T'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SettlInstID, True)
        self.register_field(fields.SettlInstTransType, True)
        self.register_field(fields.SettlInstRefID, True)
        self.register_field(fields.SettlInstMode, True)
        self.register_field(fields.SettlInstSource, True)
        self.register_field(fields.AllocAccount, True)
        self.register_field(fields.IndividualAllocID, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.AllocID, False)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.Side, False)
        self.register_field(fields.SecurityType, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.TransactTime, True)
        register_Parties_component(self)
        self.register_field(fields.StandInstDbType, False)
        self.register_field(fields.StandInstDbName, False)
        self.register_field(fields.StandInstDbID, False)
        self.register_field(fields.SettlDeliveryType, False)
        self.register_field(fields.SettlDepositoryCode, False)
        self.register_field(fields.SettlBrkrCode, False)
        self.register_field(fields.SettlInstCode, False)
        self.register_field(fields.SecuritySettlAgentName, False)
        self.register_field(fields.SecuritySettlAgentCode, False)
        self.register_field(fields.SecuritySettlAgentAcctNum, False)
        self.register_field(fields.SecuritySettlAgentAcctName, False)
        self.register_field(fields.SecuritySettlAgentContactName, False)
        self.register_field(fields.SecuritySettlAgentContactPhone, False)
        self.register_field(fields.CashSettlAgentName, False)
        self.register_field(fields.CashSettlAgentCode, False)
        self.register_field(fields.CashSettlAgentAcctNum, False)
        self.register_field(fields.CashSettlAgentAcctName, False)
        self.register_field(fields.CashSettlAgentContactName, False)
        self.register_field(fields.CashSettlAgentContactPhone, False)
        self.register_field(fields.PaymentMethod, False)
        self.register_field(fields.PaymentRef, False)
        self.register_field(fields.CardHolderName, False)
        self.register_field(fields.CardNumber, False)
        self.register_field(fields.CardStartDate, False)
        self.register_field(fields.CardExpDate, False)
        self.register_field(fields.CardIssNo, False)
        self.register_field(fields.PaymentDate, False)
        self.register_field(fields.PaymentRemitterID, False)


MESSAGE_TYPES['T'] = SettlementInstructions

class MarketDataRequest(fix_message.MessageBase):
    _msgtype = 'V'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.MDReqID, True)
        self.register_field(fields.SubscriptionRequestType, True)
        self.register_field(fields.MarketDepth, True)
        self.register_field(fields.MDUpdateType, False)
        self.register_field(fields.AggregatedBook, False)
        self.register_field(fields.OpenCloseSettleFlag, False)
        self.register_field(fields.Scope, False)
        self.register_field(fields.MDImplicitDelete, False)
        self.register_group(fields.NoMDEntryTypes, NoMDEntryTypesGroup, True)
        self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, True)
        self.register_group(fields.NoTradingSessions, NoTradingSessionsGroup, False)


MESSAGE_TYPES['V'] = MarketDataRequest

class MarketDataSnapshotFullRefresh(fix_message.MessageBase):
    _msgtype = 'W'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.MDReqID, False)
        register_Instrument_component(self)
        self.register_field(fields.FinancialStatus, False)
        self.register_field(fields.CorporateAction, False)
        self.register_field(fields.TotalVolumeTraded, False)
        self.register_field(fields.TotalVolumeTradedDate, False)
        self.register_field(fields.TotalVolumeTradedTime, False)
        self.register_field(fields.NetChgPrevDay, False)
        self.register_group(fields.NoMDEntries, NoMDEntriesGroup, True)


MESSAGE_TYPES['W'] = MarketDataSnapshotFullRefresh

class MarketDataIncrementalRefresh(fix_message.MessageBase):
    _msgtype = 'X'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.MDReqID, False)
        self.register_group(fields.NoMDEntries, NoMDEntriesGroup, True)


MESSAGE_TYPES['X'] = MarketDataIncrementalRefresh

class MarketDataRequestReject(fix_message.MessageBase):
    _msgtype = 'Y'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.MDReqID, True)
        self.register_field(fields.MDReqRejReason, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['Y'] = MarketDataRequestReject

class QuoteCancel(fix_message.MessageBase):
    _msgtype = 'Z'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.QuoteReqID, False)
        self.register_field(fields.QuoteID, True)
        self.register_field(fields.QuoteCancelType, True)
        self.register_field(fields.QuoteResponseLevel, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_group(fields.NoQuoteEntries, NoQuoteEntriesGroup, False)


MESSAGE_TYPES['Z'] = QuoteCancel

class QuoteStatusRequest(fix_message.MessageBase):
    _msgtype = 'a'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.QuoteStatusReqID, False)
        self.register_field(fields.QuoteID, False)
        register_Instrument_component(self)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.SubscriptionRequestType, False)


MESSAGE_TYPES['a'] = QuoteStatusRequest

class MassQuoteAcknowledgement(fix_message.MessageBase):
    _msgtype = 'b'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.QuoteReqID, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.QuoteStatus, True)
        self.register_field(fields.QuoteRejectReason, False)
        self.register_field(fields.QuoteResponseLevel, False)
        self.register_field(fields.QuoteType, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.Text, False)
        self.register_group(fields.NoQuoteSets, NoQuoteSetsGroup, False)


MESSAGE_TYPES['b'] = MassQuoteAcknowledgement

class SecurityDefinitionRequest(fix_message.MessageBase):
    _msgtype = 'c'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReqID, True)
        self.register_field(fields.SecurityRequestType, True)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_group(fields.NoLegs, NoLegsGroup, False)
        self.register_field(fields.SubscriptionRequestType, False)


MESSAGE_TYPES['c'] = SecurityDefinitionRequest

class SecurityDefinition(fix_message.MessageBase):
    _msgtype = 'd'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReqID, True)
        self.register_field(fields.SecurityResponseID, True)
        self.register_field(fields.SecurityResponseType, True)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_group(fields.NoLegs, NoLegsGroup, False)
        self.register_field(fields.RoundLot, False)
        self.register_field(fields.MinTradeVol, False)


MESSAGE_TYPES['d'] = SecurityDefinition

class SecurityStatusRequest(fix_message.MessageBase):
    _msgtype = 'e'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityStatusReqID, True)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.SubscriptionRequestType, True)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)


MESSAGE_TYPES['e'] = SecurityStatusRequest

class SecurityStatus(fix_message.MessageBase):
    _msgtype = 'f'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityStatusReqID, False)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.UnsolicitedIndicator, False)
        self.register_field(fields.SecurityTradingStatus, False)
        self.register_field(fields.FinancialStatus, False)
        self.register_field(fields.CorporateAction, False)
        self.register_field(fields.HaltReason, False)
        self.register_field(fields.InViewOfCommon, False)
        self.register_field(fields.DueToRelated, False)
        self.register_field(fields.BuyVolume, False)
        self.register_field(fields.SellVolume, False)
        self.register_field(fields.HighPx, False)
        self.register_field(fields.LowPx, False)
        self.register_field(fields.LastPx, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.Adjustment, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['f'] = SecurityStatus

class TradingSessionStatusRequest(fix_message.MessageBase):
    _msgtype = 'g'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TradSesReqID, True)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.TradSesMethod, False)
        self.register_field(fields.TradSesMode, False)
        self.register_field(fields.SubscriptionRequestType, True)


MESSAGE_TYPES['g'] = TradingSessionStatusRequest

class TradingSessionStatus(fix_message.MessageBase):
    _msgtype = 'h'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TradSesReqID, False)
        self.register_field(fields.TradingSessionID, True)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.TradSesMethod, False)
        self.register_field(fields.TradSesMode, False)
        self.register_field(fields.UnsolicitedIndicator, False)
        self.register_field(fields.TradSesStatus, True)
        self.register_field(fields.TradSesStatusRejReason, False)
        self.register_field(fields.TradSesStartTime, False)
        self.register_field(fields.TradSesOpenTime, False)
        self.register_field(fields.TradSesPreCloseTime, False)
        self.register_field(fields.TradSesCloseTime, False)
        self.register_field(fields.TradSesEndTime, False)
        self.register_field(fields.TotalVolumeTraded, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['h'] = TradingSessionStatus

class MassQuote(fix_message.MessageBase):
    _msgtype = 'i'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.QuoteReqID, False)
        self.register_field(fields.QuoteID, True)
        self.register_field(fields.QuoteType, False)
        self.register_field(fields.QuoteResponseLevel, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DefBidSize, False)
        self.register_field(fields.DefOfferSize, False)
        self.register_group(fields.NoQuoteSets, NoQuoteSetsGroup, True)


MESSAGE_TYPES['i'] = MassQuote

class BusinessMessageReject(fix_message.MessageBase):
    _msgtype = 'j'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.RefSeqNum, False)
        self.register_field(fields.RefMsgType, True)
        self.register_field(fields.BusinessRejectRefID, False)
        self.register_field(fields.BusinessRejectReason, True)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['j'] = BusinessMessageReject

class BidRequest(fix_message.MessageBase):
    _msgtype = 'k'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.BidID, False)
        self.register_field(fields.ClientBidID, True)
        self.register_field(fields.BidRequestTransType, True)
        self.register_field(fields.ListName, False)
        self.register_field(fields.TotalNumSecurities, True)
        self.register_field(fields.BidType, True)
        self.register_field(fields.NumTickets, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.SideValue1, False)
        self.register_field(fields.SideValue2, False)
        self.register_group(fields.NoBidDescriptors, NoBidDescriptorsGroup, False)
        self.register_group(fields.NoBidComponents, NoBidComponentsGroup, False)
        self.register_field(fields.LiquidityIndType, False)
        self.register_field(fields.WtAverageLiquidity, False)
        self.register_field(fields.ExchangeForPhysical, False)
        self.register_field(fields.OutMainCntryUIndex, False)
        self.register_field(fields.CrossPercent, False)
        self.register_field(fields.ProgRptReqs, False)
        self.register_field(fields.ProgPeriodInterval, False)
        self.register_field(fields.IncTaxInd, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.NumBidders, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.TradeType, True)
        self.register_field(fields.BasisPxType, True)
        self.register_field(fields.StrikeTime, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['k'] = BidRequest

class BidResponse(fix_message.MessageBase):
    _msgtype = 'l'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.BidID, False)
        self.register_field(fields.ClientBidID, False)
        self.register_group(fields.NoBidComponents, NoBidComponentsGroup, True)


MESSAGE_TYPES['l'] = BidResponse

class ListStrikePrice(fix_message.MessageBase):
    _msgtype = 'm'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        self.register_field(fields.TotNoStrikes, True)
        self.register_group(fields.NoStrikes, NoStrikesGroup, True)


MESSAGE_TYPES['m'] = ListStrikePrice

class XMLnonFIX(fix_message.MessageBase):
    _msgtype = 'n'
    _msgcat = 'admin'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()


MESSAGE_TYPES['n'] = XMLnonFIX

class RegistrationInstructions(fix_message.MessageBase):
    _msgtype = 'o'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.RegistID, True)
        self.register_field(fields.RegistTransType, True)
        self.register_field(fields.RegistRefID, True)
        self.register_field(fields.ClOrdID, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.RegistAcctType, False)
        self.register_field(fields.TaxAdvantageType, False)
        self.register_field(fields.OwnershipType, False)
        self.register_group(fields.NoRegistDtls, NoRegistDtlsGroup, False)
        self.register_group(fields.NoDistribInsts, NoDistribInstsGroup, False)
        self.register_field(fields.OwnershipType, False)


MESSAGE_TYPES['o'] = RegistrationInstructions

class RegistrationInstructionsResponse(fix_message.MessageBase):
    _msgtype = 'p'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.RegistID, True)
        self.register_field(fields.RegistTransType, True)
        self.register_field(fields.RegistRefID, True)
        self.register_field(fields.ClOrdID, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.RegistStatus, True)
        self.register_field(fields.RegistRejReasonCode, False)
        self.register_field(fields.RegistRejReasonText, False)


MESSAGE_TYPES['p'] = RegistrationInstructionsResponse

class OrderMassCancelRequest(fix_message.MessageBase):
    _msgtype = 'q'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.MassCancelRequestType, True)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_Instrument_component(self)
        register_UnderlyingInstrument_component(self)
        self.register_field(fields.Side, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['q'] = OrderMassCancelRequest

class OrderMassCancelReport(fix_message.MessageBase):
    _msgtype = 'r'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.OrderID, True)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.MassCancelRequestType, True)
        self.register_field(fields.MassCancelResponse, True)
        self.register_field(fields.MassCancelRejectReason, False)
        self.register_field(fields.TotalAffectedOrders, False)
        self.register_group(fields.NoAffectedOrders, NoAffectedOrdersGroup, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_Instrument_component(self)
        register_UnderlyingInstrument_component(self)
        self.register_field(fields.Side, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['r'] = OrderMassCancelReport

class NewOrderCross(fix_message.MessageBase):
    _msgtype = 's'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.CrossID, True)
        self.register_field(fields.CrossType, True)
        self.register_field(fields.CrossPrioritization, True)
        self.register_group(fields.NoSides, NoSidesGroup, True)
        register_Instrument_component(self)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.HandlInst, True)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_group(fields.NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, True)
        register_Stipulations_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.IOIid, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        self.register_field(fields.MaxShow, False)
        self.register_field(fields.PegDifference, False)
        self.register_field(fields.DiscretionInst, False)
        self.register_field(fields.DiscretionOffset, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.NetMoney, False)


MESSAGE_TYPES['s'] = NewOrderCross

class CrossOrderCancelReplaceRequest(fix_message.MessageBase):
    _msgtype = 't'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, False)
        self.register_field(fields.CrossID, True)
        self.register_field(fields.OrigCrossID, True)
        self.register_field(fields.CrossType, True)
        self.register_field(fields.CrossPrioritization, True)
        self.register_group(fields.NoSides, NoSidesGroup, True)
        register_Instrument_component(self)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.HandlInst, True)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_group(fields.NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, True)
        register_Stipulations_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.IOIid, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        self.register_field(fields.MaxShow, False)
        self.register_field(fields.PegDifference, False)
        self.register_field(fields.DiscretionInst, False)
        self.register_field(fields.DiscretionOffset, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.NetMoney, False)


MESSAGE_TYPES['t'] = CrossOrderCancelReplaceRequest

class CrossOrderCancelRequest(fix_message.MessageBase):
    _msgtype = 'u'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, False)
        self.register_field(fields.CrossID, True)
        self.register_field(fields.OrigCrossID, True)
        self.register_field(fields.CrossType, True)
        self.register_field(fields.CrossPrioritization, True)
        self.register_group(fields.NoSides, NoSidesGroup, True)
        register_Instrument_component(self)
        self.register_field(fields.TransactTime, True)


MESSAGE_TYPES['u'] = CrossOrderCancelRequest

class SecurityTypeRequest(fix_message.MessageBase):
    _msgtype = 'v'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReqID, True)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)


MESSAGE_TYPES['v'] = SecurityTypeRequest

class SecurityTypes(fix_message.MessageBase):
    _msgtype = 'w'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReqID, True)
        self.register_field(fields.SecurityResponseID, True)
        self.register_field(fields.SecurityResponseType, True)
        self.register_field(fields.TotalNumSecurityTypes, False)
        self.register_group(fields.NoSecurityTypes, NoSecurityTypesGroup, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.SubscriptionRequestType, False)


MESSAGE_TYPES['w'] = SecurityTypes

class SecurityListRequest(fix_message.MessageBase):
    _msgtype = 'x'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReqID, True)
        self.register_field(fields.SecurityListRequestType, True)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.SubscriptionRequestType, False)


MESSAGE_TYPES['x'] = SecurityListRequest

class SecurityList(fix_message.MessageBase):
    _msgtype = 'y'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReqID, True)
        self.register_field(fields.SecurityResponseID, True)
        self.register_field(fields.SecurityRequestResult, True)
        self.register_field(fields.TotalNumSecurities, False)
        self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, False)


MESSAGE_TYPES['y'] = SecurityList

class DerivativeSecurityListRequest(fix_message.MessageBase):
    _msgtype = 'z'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReqID, True)
        self.register_field(fields.SecurityListRequestType, True)
        register_UnderlyingInstrument_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.SubscriptionRequestType, False)


MESSAGE_TYPES['z'] = DerivativeSecurityListRequest

class DerivativeSecurityList(fix_message.MessageBase):
    _msgtype = 'AA'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReqID, True)
        self.register_field(fields.SecurityResponseID, True)
        self.register_field(fields.SecurityRequestResult, True)
        register_UnderlyingInstrument_component(self)
        self.register_field(fields.TotalNumSecurities, False)
        self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, False)


MESSAGE_TYPES['AA'] = DerivativeSecurityList

class NewOrderMultileg(fix_message.MessageBase):
    _msgtype = 'AB'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ClOrdLinkID, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_group(fields.NoAllocs, NoAllocsGroup, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.HandlInst, True)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_group(fields.NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.Side, True)
        register_Instrument_component(self)
        self.register_field(fields.PrevClosePx, False)
        self.register_group(fields.NoLegs, NoLegsGroup, True)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.QuantityType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.IOIid, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        register_CommissionData_component(self)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.CoveredOrUncovered, False)
        self.register_field(fields.MaxShow, False)
        self.register_field(fields.PegDifference, False)
        self.register_field(fields.DiscretionInst, False)
        self.register_field(fields.DiscretionOffset, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.MultiLegRptTypeReq, False)
        self.register_field(fields.NetMoney, False)


MESSAGE_TYPES['AB'] = NewOrderMultileg

class MultilegOrderCancelReplaceRequest(fix_message.MessageBase):
    _msgtype = 'AC'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, False)
        self.register_field(fields.OrigClOrdID, True)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ClOrdLinkID, False)
        self.register_field(fields.OrigOrdModTime, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_group(fields.NoAllocs, NoAllocsGroup, False)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.HandlInst, True)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_group(fields.NoTradingSessions, NoTradingSessionsGroup, False)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.Side, True)
        register_Instrument_component(self)
        self.register_field(fields.PrevClosePx, False)
        self.register_group(fields.NoLegs, NoLegsGroup, True)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.QuantityType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.StopPx, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.IOIid, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        register_CommissionData_component(self)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.CoveredOrUncovered, False)
        self.register_field(fields.MaxShow, False)
        self.register_field(fields.PegDifference, False)
        self.register_field(fields.DiscretionInst, False)
        self.register_field(fields.DiscretionOffset, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.MultiLegRptTypeReq, False)
        self.register_field(fields.NetMoney, False)


MESSAGE_TYPES['AC'] = MultilegOrderCancelReplaceRequest

class TradeCaptureReportRequest(fix_message.MessageBase):
    _msgtype = 'AD'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TradeRequestID, True)
        self.register_field(fields.TradeRequestType, True)
        self.register_field(fields.SubscriptionRequestType, False)
        self.register_field(fields.ExecID, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.MatchStatus, False)
        register_Parties_component(self)
        register_Instrument_component(self)
        self.register_group(fields.NoDates, NoDatesGroup, False)
        self.register_field(fields.Side, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.TradeInputSource, False)
        self.register_field(fields.TradeInputDevice, False)


MESSAGE_TYPES['AD'] = TradeCaptureReportRequest

class TradeCaptureReport(fix_message.MessageBase):
    _msgtype = 'AE'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TradeReportID, True)
        self.register_field(fields.TradeReportTransType, False)
        self.register_field(fields.TradeRequestID, False)
        self.register_field(fields.ExecType, True)
        self.register_field(fields.TradeReportRefID, False)
        self.register_field(fields.ExecID, False)
        self.register_field(fields.SecondaryExecID, False)
        self.register_field(fields.ExecRestatementReason, False)
        self.register_field(fields.PreviouslyReported, True)
        register_Instrument_component(self)
        register_OrderQtyData_component(self)
        self.register_field(fields.LastQty, True)
        self.register_field(fields.LastPx, True)
        self.register_field(fields.LastSpotRate, False)
        self.register_field(fields.LastForwardPoints, False)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradeDate, True)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.SettlmntTyp, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.MatchStatus, False)
        self.register_field(fields.MatchType, False)
        self.register_group(fields.NoSides, NoSidesGroup, True)


MESSAGE_TYPES['AE'] = TradeCaptureReport

class OrderMassStatusRequest(fix_message.MessageBase):
    _msgtype = 'AF'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.MassStatusReqID, True)
        self.register_field(fields.MassStatusReqType, True)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_Instrument_component(self)
        register_UnderlyingInstrument_component(self)
        self.register_field(fields.Side, False)


MESSAGE_TYPES['AF'] = OrderMassStatusRequest

class QuoteRequestReject(fix_message.MessageBase):
    _msgtype = 'AG'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.QuoteReqID, True)
        self.register_field(fields.RFQReqID, False)
        self.register_field(fields.QuoteRequestRejectReason, True)
        self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, True)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AG'] = QuoteRequestReject

class RFQRequest(fix_message.MessageBase):
    _msgtype = 'AH'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.RFQReqID, True)
        self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, True)
        self.register_field(fields.SubscriptionRequestType, False)


MESSAGE_TYPES['AH'] = RFQRequest

class QuoteStatusReport(fix_message.MessageBase):
    _msgtype = 'AI'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.QuoteStatusReqID, False)
        self.register_field(fields.QuoteReqID, False)
        self.register_field(fields.QuoteID, True)
        self.register_field(fields.QuoteType, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_Instrument_component(self)
        self.register_field(fields.BidPx, False)
        self.register_field(fields.OfferPx, False)
        self.register_field(fields.MktBidPx, False)
        self.register_field(fields.MktOfferPx, False)
        self.register_field(fields.MinBidSize, False)
        self.register_field(fields.BidSize, False)
        self.register_field(fields.MinOfferSize, False)
        self.register_field(fields.OfferSize, False)
        self.register_field(fields.ValidUntilTime, False)
        self.register_field(fields.BidSpotRate, False)
        self.register_field(fields.OfferSpotRate, False)
        self.register_field(fields.BidForwardPoints, False)
        self.register_field(fields.OfferForwardPoints, False)
        self.register_field(fields.MidPx, False)
        self.register_field(fields.BidYield, False)
        self.register_field(fields.MidYield, False)
        self.register_field(fields.OfferYield, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.FutSettDate, False)
        self.register_field(fields.OrdType, False)
        self.register_field(fields.FutSettDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.BidForwardPoints2, False)
        self.register_field(fields.OfferForwardPoints2, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.SettlCurrBidFxRate, False)
        self.register_field(fields.SettlCurrOfferFxRate, False)
        self.register_field(fields.SettlCurrFxRateCalc, False)
        self.register_field(fields.Commission, False)
        self.register_field(fields.CommType, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.QuoteStatus, False)


MESSAGE_TYPES['AI'] = QuoteStatusReport
