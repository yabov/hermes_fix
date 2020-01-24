
from ... import fix_message
from . import fields
from . import field_types

BEGINSTRING = 'FIX.5.0'
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
class NoLegStipulationsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.LegStipulationType, False)
        self.register_field(fields.LegStipulationValue, False)

class NoNestedPartyIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.NestedPartyID, False)
        self.register_field(fields.NestedPartyIDSource, False)
        self.register_field(fields.NestedPartyRole, False)
        register_NstdPtysSubGrp_component(self)

class NoPartyIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.PartyID, False)
        self.register_field(fields.PartyIDSource, False)
        self.register_field(fields.PartyRole, False)
        register_PtysSubGrp_component(self)

class NoPosAmtGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.PosAmtType, False)
        self.register_field(fields.PosAmt, False)
        self.register_field(fields.PositionCurrency, False)

class NoPositionsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.PosType, False)
        self.register_field(fields.LongQty, False)
        self.register_field(fields.ShortQty, False)
        self.register_field(fields.PosQtyStatus, False)
        self.register_field(fields.QuantityDate, False)
        register_NestedParties_component(self)

class NoSettlPartyIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.SettlPartyID, False)
        self.register_field(fields.SettlPartyIDSource, False)
        self.register_field(fields.SettlPartyRole, False)
        register_SettlPtysSubGrp_component(self)

class NoStipulationsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.StipulationType, False)
        self.register_field(fields.StipulationValue, False)

class NoTrdRegTimestampsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.TrdRegTimestamp, False)
        self.register_field(fields.TrdRegTimestampType, False)
        self.register_field(fields.TrdRegTimestampOrigin, False)
        self.register_field(fields.DeskType, False)
        self.register_field(fields.DeskTypeSource, False)
        self.register_field(fields.DeskOrderHandlingInst, False)

class NoUnderlyingStipsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.UnderlyingStipType, False)
        self.register_field(fields.UnderlyingStipValue, False)

class NoNested2PartyIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.Nested2PartyID, False)
        self.register_field(fields.Nested2PartyIDSource, False)
        self.register_field(fields.Nested2PartyRole, False)
        register_NstdPtys2SubGrp_component(self)

class NoNested3PartyIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.Nested3PartyID, False)
        self.register_field(fields.Nested3PartyIDSource, False)
        self.register_field(fields.Nested3PartyRole, False)
        register_NstdPtys3SubGrp_component(self)

class NoAffectedOrdersGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.OrigClOrdID, False)
        self.register_field(fields.AffectedOrderID, False)
        self.register_field(fields.AffectedSecondaryOrderID, False)

class NoAllocsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.AllocAccount, False)
        self.register_field(fields.AllocAcctIDSource, False)
        self.register_field(fields.AllocPrice, False)
        self.register_field(fields.AllocPositionEffect, False)
        self.register_field(fields.IndividualAllocID, False)
        self.register_field(fields.IndividualAllocRejCode, False)
        register_NestedParties_component(self)
        self.register_field(fields.AllocText, False)
        self.register_field(fields.EncodedAllocTextLen, False)
        self.register_field(fields.EncodedAllocText, False)
        self.register_field(fields.SecondaryIndividualAllocID, False)
        self.register_field(fields.AllocCustomerCapacity, False)
        self.register_field(fields.IndividualAllocType, False)
        self.register_field(fields.AllocQty, False)

class NoBidComponentsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ListID, False)
        self.register_field(fields.Side, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.NetGrossInd, False)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)

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

class NoClearingInstructionsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ClearingInstruction, False)

class NoCollInquiryQualifierGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.CollInquiryQualifier, False)

class NoCompIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.RefCompID, False)
        self.register_field(fields.RefSubID, False)
        self.register_field(fields.LocationID, False)
        self.register_field(fields.DeskID, False)

class NoContAmtsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ContAmtType, False)
        self.register_field(fields.ContAmtValue, False)
        self.register_field(fields.ContAmtCurr, False)

class NoContraBrokersGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ContraBroker, False)
        self.register_field(fields.ContraTrader, False)
        self.register_field(fields.ContraTradeQty, False)
        self.register_field(fields.ContraTradeTime, False)
        self.register_field(fields.ContraLegRefID, False)

class NoCapacitiesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.OrderCapacity, True)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.OrderCapacityQty, True)

class NoExecsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.LastQty, False)
        self.register_field(fields.ExecID, False)
        self.register_field(fields.SecondaryExecID, False)
        self.register_field(fields.LastPx, False)
        self.register_field(fields.LastParPx, False)
        self.register_field(fields.LastCapacity, False)
        self.register_field(fields.TradeID, False)
        self.register_field(fields.FirmTradeID, False)

class NoRelatedSymGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        register_Instrument_component(self)

class NoLegsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        register_InstrumentLeg_component(self)
        self.register_field(fields.LegQty, False)
        self.register_field(fields.LegOrderQty, False)
        self.register_field(fields.LegSwapType, False)
        register_LegStipulations_component(self)
        self.register_field(fields.LegPositionEffect, False)
        self.register_field(fields.LegCoveredOrUncovered, False)
        register_NestedParties_component(self)
        self.register_field(fields.LegRefID, False)
        self.register_field(fields.LegPrice, False)
        self.register_field(fields.LegSettlType, False)
        self.register_field(fields.LegSettlDate, False)
        self.register_field(fields.LegLastPx, False)
        self.register_field(fields.LegSettlCurrency, False)
        self.register_field(fields.LegLastForwardPoints, False)
        self.register_field(fields.LegCalculatedCcyLastQty, False)
        self.register_field(fields.LegGrossTradeAmt, False)

class NoStrikesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        register_Instrument_component(self)

class NoIOIQualifiersGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.IOIQualifier, False)

class NoLegAllocsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.LegAllocAccount, False)
        self.register_field(fields.LegIndividualAllocID, False)
        register_NestedParties2_component(self)
        self.register_field(fields.LegAllocQty, False)
        self.register_field(fields.LegAllocAcctIDSource, False)
        self.register_field(fields.LegSettlCurrency, False)

class NoLinesOfTextGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.Text, True)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)

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
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.AllocID, False)
        self.register_field(fields.PreallocMethod, False)
        register_PreAllocGrp_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.HandlInst, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MatchIncrement, False)
        self.register_field(fields.MaxPriceLevels, False)
        register_DisplayInstruction_component(self)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ExDestinationIDSource, False)
        register_TrdgSesGrp_component(self)
        self.register_field(fields.ProcessCode, False)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.SideValueInd, False)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, False)
        register_Stipulations_component(self)
        self.register_field(fields.QtyType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceProtectionScope, False)
        self.register_field(fields.StopPx, False)
        register_TriggeringInstruction_component(self)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.IOIID, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.RefOrderID, False)
        self.register_field(fields.RefOrderIDSource, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        register_CommissionData_component(self)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.PreTradeAnonymity, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.BookingType, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.SettlDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.Price2, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.CoveredOrUncovered, False)
        self.register_field(fields.MaxShow, False)
        register_PegInstructions_component(self)
        register_DiscretionInstructions_component(self)
        self.register_field(fields.TargetStrategy, False)
        register_StrategyParametersGrp_component(self)
        self.register_field(fields.TargetStrategyParameters, False)
        self.register_field(fields.ParticipationRate, False)
        self.register_field(fields.Designation, False)

class NoMDEntriesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.MDEntryType, True)
        self.register_field(fields.MDEntryID, False)
        self.register_field(fields.MDEntryPx, False)
        self.register_field(fields.OrdType, False)
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
        self.register_field(fields.OpenCloseSettlFlag, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.SellerDays, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.QuoteEntryID, False)
        self.register_field(fields.MDEntryBuyer, False)
        self.register_field(fields.MDEntrySeller, False)
        self.register_field(fields.NumberOfOrders, False)
        self.register_field(fields.MDEntryPositionNo, False)
        self.register_field(fields.Scope, False)
        self.register_field(fields.PriceDelta, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.MDPriceLevel, False)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.MDOriginType, False)
        self.register_field(fields.HighPx, False)
        self.register_field(fields.LowPx, False)
        self.register_field(fields.TradeVolume, False)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.MDQuoteType, False)
        self.register_field(fields.RptSeq, False)
        self.register_field(fields.DealingCapacity, False)
        self.register_field(fields.MDEntrySpotRate, False)
        self.register_field(fields.MDEntryForwardPoints, False)
        register_Parties_component(self)

class NoMDEntryTypesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.MDEntryType, True)

class NoAltMDSourceGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.AltMDSourceID, False)

class NoMiscFeesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.MiscFeeAmt, False)
        self.register_field(fields.MiscFeeCurr, False)
        self.register_field(fields.MiscFeeType, False)
        self.register_field(fields.MiscFeeBasis, False)

class NoUnderlyingsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        register_UnderlyingInstrument_component(self)
        self.register_field(fields.UnderlyingSettlPrice, False)
        self.register_field(fields.UnderlyingSettlPriceType, False)
        self.register_field(fields.UnderlyingDeliveryAmount, False)
        register_UnderlyingAmount_component(self)

class NoQuoteEntriesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)

class NoQuoteQualifiersGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.QuoteQualifier, False)

class NoQuoteSetsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.QuoteSetID, False)
        register_UnderlyingInstrument_component(self)
        self.register_field(fields.TotNoQuoteEntries, False)
        self.register_field(fields.LastFragment, False)
        register_QuotEntryAckGrp_component(self)

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
        self.register_field(fields.CashDistribAgentAcctName, False)

class NoRegistDtlsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.RegistDtls, False)
        self.register_field(fields.RegistEmail, False)
        self.register_field(fields.MailingDtls, False)
        self.register_field(fields.MailingInst, False)
        register_NestedParties_component(self)
        self.register_field(fields.OwnerType, False)
        self.register_field(fields.DateOfBirth, False)
        self.register_field(fields.InvestorCountryOfResidence, False)

class NoRoutingIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.RoutingType, False)
        self.register_field(fields.RoutingID, False)

class NoSecurityTypesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.SecurityType, False)
        self.register_field(fields.SecuritySubType, False)
        self.register_field(fields.Product, False)
        self.register_field(fields.CFICode, False)

class NoSettlInstGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.SettlInstID, False)
        self.register_field(fields.SettlInstTransType, False)
        self.register_field(fields.SettlInstRefID, False)
        register_Parties_component(self)
        self.register_field(fields.Side, False)
        self.register_field(fields.Product, False)
        self.register_field(fields.SecurityType, False)
        self.register_field(fields.CFICode, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.LastUpdateTime, False)
        register_SettlInstructionsData_component(self)
        self.register_field(fields.PaymentMethod, False)
        self.register_field(fields.PaymentRef, False)
        self.register_field(fields.CardHolderName, False)
        self.register_field(fields.CardNumber, False)
        self.register_field(fields.CardStartDate, False)
        self.register_field(fields.CardExpDate, False)
        self.register_field(fields.CardIssNum, False)
        self.register_field(fields.PaymentDate, False)
        self.register_field(fields.PaymentRemitterID, False)

class NoSidesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.Side, True)
        self.register_field(fields.OrigClOrdID, True)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ClOrdLinkID, False)
        self.register_field(fields.OrigOrdModTime, False)
        register_Parties_component(self)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.TradeDate, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)

class NoTradesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.TradeReportID, False)
        self.register_field(fields.SecondaryTradeReportID, False)

class NoTradingSessionsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)

class NoDatesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.LastUpdateTime, False)
        self.register_field(fields.TransactTime, False)

class NoEventsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.EventType, False)
        self.register_field(fields.EventDate, False)
        self.register_field(fields.EventPx, False)
        self.register_field(fields.EventText, False)

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

class NoUnderlyingSecurityAltIDGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.UnderlyingSecurityAltID, False)
        self.register_field(fields.UnderlyingSecurityAltIDSource, False)

class NoInstrAttribGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.InstrAttribType, False)
        self.register_field(fields.InstrAttribValue, False)

class NoDlvyInstGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.SettlInstSource, False)
        self.register_field(fields.DlvyInstType, False)
        register_SettlParties_component(self)

class NoSettlPartySubIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.SettlPartySubID, False)
        self.register_field(fields.SettlPartySubIDType, False)

class NoPartySubIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.PartySubID, False)
        self.register_field(fields.PartySubIDType, False)

class NoNestedPartySubIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.NestedPartySubID, False)
        self.register_field(fields.NestedPartySubIDType, False)

class NoHopsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.HopCompID, False)
        self.register_field(fields.HopSendingTime, False)
        self.register_field(fields.HopRefID, False)

class NoNested2PartySubIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.Nested2PartySubID, False)
        self.register_field(fields.Nested2PartySubIDType, False)

class NoNested3PartySubIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.Nested3PartySubID, False)
        self.register_field(fields.Nested3PartySubIDType, False)

class NoStrategyParametersGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.StrategyParameterName, False)
        self.register_field(fields.StrategyParameterType, False)
        self.register_field(fields.StrategyParameterValue, False)

class NoUnderlyingAmountsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.UnderlyingPayAmount, False)
        self.register_field(fields.UnderlyingCollectAmount, False)
        self.register_field(fields.UnderlyingSettlementDate, False)
        self.register_field(fields.UnderlyingSettlementStatus, False)

class NoExpirationGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.ExpType, False)
        self.register_field(fields.ExpQty, False)

class NoInstrumentPartiesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.InstrumentPartyID, False)
        self.register_field(fields.InstrumentPartyIDSource, False)
        self.register_field(fields.InstrumentPartyRole, False)
        register_InstrumentPtysSubGrp_component(self)

class NoInstrumentPartySubIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.InstrumentPartySubID, False)
        self.register_field(fields.InstrumentPartySubIDType, False)

class NoSideTrdRegTSGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.SideTrdRegTimestamp, False)
        self.register_field(fields.SideTrdRegTimestampType, False)
        self.register_field(fields.SideTrdRegTimestampSrc, False)

class NoUndlyInstrumentPartiesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.UndlyInstrumentPartyID, False)
        self.register_field(fields.UndlyInstrumentPartyIDSource, False)
        self.register_field(fields.UndlyInstrumentPartyRole, False)
        register_UndlyInstrumentPtysSubGrp_component(self)

class NoUndlyInstrumentPartySubIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.UndlyInstrumentPartySubID, False)
        self.register_field(fields.UndlyInstrumentPartySubIDType, False)

class NoRootPartyIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.RootPartyID, False)
        self.register_field(fields.RootPartyIDSource, False)
        self.register_field(fields.RootPartyRole, False)
        register_RootSubParties_component(self)

class NoRootPartySubIDsGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.RootPartySubID, False)
        self.register_field(fields.RootPartySubIDType, False)

class NoMsgTypesGroup(fix_message.FIXGroup):
    def __init__(self, value = None):
        super().__init__(value)
        self.register_field(fields.RefMsgType, False)
        self.register_field(fields.MsgDirection, False)
        self.register_field(fields.RefApplVerID, False)
        self.register_field(fields.RefCstmApplVerID, False)

##############End Repeating Groups###############
##############Begin Componenets###############
def register_CommissionData_component(self):
    self.register_field(fields.Commission, False)
    self.register_field(fields.CommType, False)
    self.register_field(fields.CommCurrency, False)
    self.register_field(fields.FundRenewWaiv, False)

def register_DiscretionInstructions_component(self):
    self.register_field(fields.DiscretionInst, False)
    self.register_field(fields.DiscretionOffsetValue, False)
    self.register_field(fields.DiscretionMoveType, False)
    self.register_field(fields.DiscretionOffsetType, False)
    self.register_field(fields.DiscretionLimitType, False)
    self.register_field(fields.DiscretionRoundDirection, False)
    self.register_field(fields.DiscretionScope, False)

def register_FinancingDetails_component(self):
    self.register_field(fields.AgreementDesc, False)
    self.register_field(fields.AgreementID, False)
    self.register_field(fields.AgreementDate, False)
    self.register_field(fields.AgreementCurrency, False)
    self.register_field(fields.TerminationType, False)
    self.register_field(fields.StartDate, False)
    self.register_field(fields.EndDate, False)
    self.register_field(fields.DeliveryType, False)
    self.register_field(fields.MarginRatio, False)

def register_Instrument_component(self):
    self.register_field(fields.Symbol, False)
    self.register_field(fields.SymbolSfx, False)
    self.register_field(fields.SecurityID, False)
    self.register_field(fields.SecurityIDSource, False)
    register_SecAltIDGrp_component(self)
    self.register_field(fields.Product, False)
    self.register_field(fields.CFICode, False)
    self.register_field(fields.SecurityType, False)
    self.register_field(fields.SecuritySubType, False)
    self.register_field(fields.MaturityMonthYear, False)
    self.register_field(fields.MaturityDate, False)
    self.register_field(fields.MaturityTime, False)
    self.register_field(fields.PutOrCall, False)
    self.register_field(fields.SettleOnOpenFlag, False)
    self.register_field(fields.InstrmtAssignmentMethod, False)
    self.register_field(fields.SecurityStatus, False)
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
    self.register_field(fields.StrikeCurrency, False)
    self.register_field(fields.StrikeMultiplier, False)
    self.register_field(fields.StrikeValue, False)
    self.register_field(fields.OptAttribute, False)
    self.register_field(fields.ContractMultiplier, False)
    self.register_field(fields.MinPriceIncrement, False)
    self.register_field(fields.UnitofMeasure, False)
    self.register_field(fields.TimeUnit, False)
    self.register_field(fields.CouponRate, False)
    self.register_field(fields.SecurityExchange, False)
    self.register_field(fields.PositionLimit, False)
    self.register_field(fields.NTPositionLimit, False)
    self.register_field(fields.Issuer, False)
    self.register_field(fields.EncodedIssuerLen, False)
    self.register_field(fields.EncodedIssuer, False)
    self.register_field(fields.SecurityDesc, False)
    self.register_field(fields.EncodedSecurityDescLen, False)
    self.register_field(fields.EncodedSecurityDesc, False)
    self.register_field(fields.Pool, False)
    self.register_field(fields.ContractSettlMonth, False)
    self.register_field(fields.CPProgram, False)
    self.register_field(fields.CPRegType, False)
    register_EvntGrp_component(self)
    self.register_field(fields.DatedDate, False)
    self.register_field(fields.InterestAccrualDate, False)
    register_InstrumentParties_component(self)

def register_InstrumentExtension_component(self):
    self.register_field(fields.DeliveryForm, False)
    self.register_field(fields.PctAtRisk, False)
    register_AttrbGrp_component(self)

def register_InstrumentLeg_component(self):
    self.register_field(fields.LegSymbol, False)
    self.register_field(fields.LegSymbolSfx, False)
    self.register_field(fields.LegSecurityID, False)
    self.register_field(fields.LegSecurityIDSource, False)
    register_LegSecAltIDGrp_component(self)
    self.register_field(fields.LegProduct, False)
    self.register_field(fields.LegCFICode, False)
    self.register_field(fields.LegSecurityType, False)
    self.register_field(fields.LegSecuritySubType, False)
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
    self.register_field(fields.LegStrikeCurrency, False)
    self.register_field(fields.LegOptAttribute, False)
    self.register_field(fields.LegContractMultiplier, False)
    self.register_field(fields.LegUnitofMeasure, False)
    self.register_field(fields.LegTimeUnit, False)
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
    self.register_field(fields.LegCurrency, False)
    self.register_field(fields.LegPool, False)
    self.register_field(fields.LegDatedDate, False)
    self.register_field(fields.LegContractSettlMonth, False)
    self.register_field(fields.LegInterestAccrualDate, False)
    self.register_field(fields.LegOptionRatio, False)
    self.register_field(fields.LegPrice, False)

def register_LegBenchmarkCurveData_component(self):
    self.register_field(fields.LegBenchmarkCurveCurrency, False)
    self.register_field(fields.LegBenchmarkCurveName, False)
    self.register_field(fields.LegBenchmarkCurvePoint, False)
    self.register_field(fields.LegBenchmarkPrice, False)
    self.register_field(fields.LegBenchmarkPriceType, False)

def register_LegStipulations_component(self):
    self.register_group(fields.NoLegStipulations, NoLegStipulationsGroup, False)

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

def register_PegInstructions_component(self):
    self.register_field(fields.PegOffsetValue, False)
    self.register_field(fields.PegPriceType, False)
    self.register_field(fields.PegMoveType, False)
    self.register_field(fields.PegOffsetType, False)
    self.register_field(fields.PegLimitType, False)
    self.register_field(fields.PegRoundDirection, False)
    self.register_field(fields.PegScope, False)
    self.register_field(fields.PegSecurityIDSource, False)
    self.register_field(fields.PegSecurityID, False)
    self.register_field(fields.PegSymbol, False)
    self.register_field(fields.PegSecurityDesc, False)

def register_PositionAmountData_component(self):
    self.register_group(fields.NoPosAmt, NoPosAmtGroup, False)

def register_PositionQty_component(self):
    self.register_group(fields.NoPositions, NoPositionsGroup, False)

def register_SettlInstructionsData_component(self):
    self.register_field(fields.SettlDeliveryType, False)
    self.register_field(fields.StandInstDbType, False)
    self.register_field(fields.StandInstDbName, False)
    self.register_field(fields.StandInstDbID, False)
    register_DlvyInstGrp_component(self)

def register_SettlParties_component(self):
    self.register_group(fields.NoSettlPartyIDs, NoSettlPartyIDsGroup, False)

def register_SpreadOrBenchmarkCurveData_component(self):
    self.register_field(fields.Spread, False)
    self.register_field(fields.BenchmarkCurveCurrency, False)
    self.register_field(fields.BenchmarkCurveName, False)
    self.register_field(fields.BenchmarkCurvePoint, False)
    self.register_field(fields.BenchmarkPrice, False)
    self.register_field(fields.BenchmarkPriceType, False)
    self.register_field(fields.BenchmarkSecurityID, False)
    self.register_field(fields.BenchmarkSecurityIDSource, False)

def register_Stipulations_component(self):
    self.register_group(fields.NoStipulations, NoStipulationsGroup, False)

def register_TrdRegTimestamps_component(self):
    self.register_group(fields.NoTrdRegTimestamps, NoTrdRegTimestampsGroup, False)

def register_UnderlyingInstrument_component(self):
    self.register_field(fields.UnderlyingSymbol, False)
    self.register_field(fields.UnderlyingSymbolSfx, False)
    self.register_field(fields.UnderlyingSecurityID, False)
    self.register_field(fields.UnderlyingSecurityIDSource, False)
    register_UndSecAltIDGrp_component(self)
    self.register_field(fields.UnderlyingProduct, False)
    self.register_field(fields.UnderlyingCFICode, False)
    self.register_field(fields.UnderlyingSecurityType, False)
    self.register_field(fields.UnderlyingSecuritySubType, False)
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
    self.register_field(fields.UnderlyingStrikeCurrency, False)
    self.register_field(fields.UnderlyingOptAttribute, False)
    self.register_field(fields.UnderlyingContractMultiplier, False)
    self.register_field(fields.UnderlyingUnitofMeasure, False)
    self.register_field(fields.UnderlyingTimeUnit, False)
    self.register_field(fields.UnderlyingCouponRate, False)
    self.register_field(fields.UnderlyingSecurityExchange, False)
    self.register_field(fields.UnderlyingIssuer, False)
    self.register_field(fields.EncodedUnderlyingIssuerLen, False)
    self.register_field(fields.EncodedUnderlyingIssuer, False)
    self.register_field(fields.UnderlyingSecurityDesc, False)
    self.register_field(fields.EncodedUnderlyingSecurityDescLen, False)
    self.register_field(fields.EncodedUnderlyingSecurityDesc, False)
    self.register_field(fields.UnderlyingCPProgram, False)
    self.register_field(fields.UnderlyingCPRegType, False)
    self.register_field(fields.UnderlyingAllocationPercent, False)
    self.register_field(fields.UnderlyingCurrency, False)
    self.register_field(fields.UnderlyingQty, False)
    self.register_field(fields.UnderlyingSettlementType, False)
    self.register_field(fields.UnderlyingCashAmount, False)
    self.register_field(fields.UnderlyingCashType, False)
    self.register_field(fields.UnderlyingPx, False)
    self.register_field(fields.UnderlyingDirtyPrice, False)
    self.register_field(fields.UnderlyingEndPrice, False)
    self.register_field(fields.UnderlyingStartValue, False)
    self.register_field(fields.UnderlyingCurrentValue, False)
    self.register_field(fields.UnderlyingEndValue, False)
    register_UnderlyingStipulations_component(self)
    self.register_field(fields.UnderlyingAdjustedQuantity, False)
    self.register_field(fields.UnderlyingFXRate, False)
    self.register_field(fields.UnderlyingFXRateCalc, False)
    self.register_field(fields.UnderlyingCapValue, False)
    register_UndlyInstrumentParties_component(self)
    self.register_field(fields.UnderlyingSettlMethod, False)

def register_YieldData_component(self):
    self.register_field(fields.YieldType, False)
    self.register_field(fields.Yield, False)
    self.register_field(fields.YieldCalcDate, False)
    self.register_field(fields.YieldRedemptionDate, False)
    self.register_field(fields.YieldRedemptionPrice, False)
    self.register_field(fields.YieldRedemptionPriceType, False)

def register_UnderlyingStipulations_component(self):
    self.register_group(fields.NoUnderlyingStips, NoUnderlyingStipsGroup, False)

def register_StandardHeader_component(self):
    self.register_field(fields.BeginString, True)
    self.register_field(fields.BodyLength, True)
    self.register_field(fields.MsgType, True)
    self.register_field(fields.ApplVerID, False)
    self.register_field(fields.CstmApplVerID, False)
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
    register_HopGrp_component(self)

def register_StandardTrailer_component(self):
    self.register_field(fields.SignatureLength, False)
    self.register_field(fields.Signature, False)
    self.register_field(fields.CheckSum, True)

def register_NestedParties2_component(self):
    self.register_group(fields.NoNested2PartyIDs, NoNested2PartyIDsGroup, False)

def register_NestedParties3_component(self):
    self.register_group(fields.NoNested3PartyIDs, NoNested3PartyIDsGroup, False)

def register_AffectedOrdGrp_component(self):
    self.register_group(fields.NoAffectedOrders, NoAffectedOrdersGroup, False)

def register_AllocAckGrp_component(self):
    self.register_group(fields.NoAllocs, NoAllocsGroup, False)

def register_AllocGrp_component(self):
    self.register_group(fields.NoAllocs, NoAllocsGroup, False)

def register_BidCompReqGrp_component(self):
    self.register_group(fields.NoBidComponents, NoBidComponentsGroup, False)

def register_BidCompRspGrp_component(self):
    self.register_group(fields.NoBidComponents, NoBidComponentsGroup, True)

def register_BidDescReqGrp_component(self):
    self.register_group(fields.NoBidDescriptors, NoBidDescriptorsGroup, False)

def register_ClrInstGrp_component(self):
    self.register_group(fields.NoClearingInstructions, NoClearingInstructionsGroup, False)

def register_CollInqQualGrp_component(self):
    self.register_group(fields.NoCollInquiryQualifier, NoCollInquiryQualifierGroup, False)

def register_CompIDReqGrp_component(self):
    self.register_group(fields.NoCompIDs, NoCompIDsGroup, False)

def register_CompIDStatGrp_component(self):
    self.register_group(fields.NoCompIDs, NoCompIDsGroup, True)

def register_ContAmtGrp_component(self):
    self.register_group(fields.NoContAmts, NoContAmtsGroup, False)

def register_ContraGrp_component(self):
    self.register_group(fields.NoContraBrokers, NoContraBrokersGroup, False)

def register_CpctyConfGrp_component(self):
    self.register_group(fields.NoCapacities, NoCapacitiesGroup, True)

def register_ExecAllocGrp_component(self):
    self.register_group(fields.NoExecs, NoExecsGroup, False)

def register_ExecCollGrp_component(self):
    self.register_group(fields.NoExecs, NoExecsGroup, False)

def register_ExecsGrp_component(self):
    self.register_group(fields.NoExecs, NoExecsGroup, False)

def register_InstrmtGrp_component(self):
    self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, False)

def register_InstrmtLegExecGrp_component(self):
    self.register_group(fields.NoLegs, NoLegsGroup, False)

def register_InstrmtLegGrp_component(self):
    self.register_group(fields.NoLegs, NoLegsGroup, False)

def register_InstrmtLegIOIGrp_component(self):
    self.register_group(fields.NoLegs, NoLegsGroup, False)

def register_InstrmtLegSecListGrp_component(self):
    self.register_group(fields.NoLegs, NoLegsGroup, False)

def register_InstrmtMDReqGrp_component(self):
    self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, True)

def register_InstrmtStrkPxGrp_component(self):
    self.register_group(fields.NoStrikes, NoStrikesGroup, True)

def register_IOIQualGrp_component(self):
    self.register_group(fields.NoIOIQualifiers, NoIOIQualifiersGroup, False)

def register_LegOrdGrp_component(self):
    self.register_group(fields.NoLegs, NoLegsGroup, True)

def register_LegPreAllocGrp_component(self):
    self.register_group(fields.NoLegAllocs, NoLegAllocsGroup, False)

def register_LegQuotGrp_component(self):
    self.register_group(fields.NoLegs, NoLegsGroup, False)

def register_LegQuotStatGrp_component(self):
    self.register_group(fields.NoLegs, NoLegsGroup, False)

def register_LinesOfTextGrp_component(self):
    self.register_group(fields.NoLinesOfText, NoLinesOfTextGroup, True)

def register_ListOrdGrp_component(self):
    self.register_group(fields.NoOrders, NoOrdersGroup, True)

def register_MDFullGrp_component(self):
    self.register_group(fields.NoMDEntries, NoMDEntriesGroup, True)

def register_MDIncGrp_component(self):
    self.register_group(fields.NoMDEntries, NoMDEntriesGroup, True)

def register_MDReqGrp_component(self):
    self.register_group(fields.NoMDEntryTypes, NoMDEntryTypesGroup, True)

def register_MDRjctGrp_component(self):
    self.register_group(fields.NoAltMDSource, NoAltMDSourceGroup, False)

def register_MiscFeesGrp_component(self):
    self.register_group(fields.NoMiscFees, NoMiscFeesGroup, False)

def register_OrdAllocGrp_component(self):
    self.register_group(fields.NoOrders, NoOrdersGroup, False)

def register_OrdListStatGrp_component(self):
    self.register_group(fields.NoOrders, NoOrdersGroup, True)

def register_PosUndInstrmtGrp_component(self):
    self.register_group(fields.NoUnderlyings, NoUnderlyingsGroup, False)

def register_PreAllocGrp_component(self):
    self.register_group(fields.NoAllocs, NoAllocsGroup, False)

def register_PreAllocMlegGrp_component(self):
    self.register_group(fields.NoAllocs, NoAllocsGroup, False)

def register_QuotCxlEntriesGrp_component(self):
    self.register_group(fields.NoQuoteEntries, NoQuoteEntriesGroup, False)

def register_QuotEntryAckGrp_component(self):
    self.register_group(fields.NoQuoteEntries, NoQuoteEntriesGroup, False)

def register_QuotEntryGrp_component(self):
    self.register_group(fields.NoQuoteEntries, NoQuoteEntriesGroup, True)

def register_QuotQualGrp_component(self):
    self.register_group(fields.NoQuoteQualifiers, NoQuoteQualifiersGroup, False)

def register_QuotReqGrp_component(self):
    self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, True)

def register_QuotReqLegsGrp_component(self):
    self.register_group(fields.NoLegs, NoLegsGroup, False)

def register_QuotReqRjctGrp_component(self):
    self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, True)

def register_QuotSetAckGrp_component(self):
    self.register_group(fields.NoQuoteSets, NoQuoteSetsGroup, False)

def register_QuotSetGrp_component(self):
    self.register_group(fields.NoQuoteSets, NoQuoteSetsGroup, True)

def register_RelSymDerivSecGrp_component(self):
    self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, False)

def register_RFQReqGrp_component(self):
    self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, True)

def register_RgstDistInstGrp_component(self):
    self.register_group(fields.NoDistribInsts, NoDistribInstsGroup, False)

def register_RgstDtlsGrp_component(self):
    self.register_group(fields.NoRegistDtls, NoRegistDtlsGroup, False)

def register_RoutingGrp_component(self):
    self.register_group(fields.NoRoutingIDs, NoRoutingIDsGroup, False)

def register_SecListGrp_component(self):
    self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, False)

def register_SecTypesGrp_component(self):
    self.register_group(fields.NoSecurityTypes, NoSecurityTypesGroup, False)

def register_SettlInstGrp_component(self):
    self.register_group(fields.NoSettlInst, NoSettlInstGroup, False)

def register_SideCrossOrdCxlGrp_component(self):
    self.register_group(fields.NoSides, NoSidesGroup, True)

def register_SideCrossOrdModGrp_component(self):
    self.register_group(fields.NoSides, NoSidesGroup, True)

def register_TrdAllocGrp_component(self):
    self.register_group(fields.NoAllocs, NoAllocsGroup, False)

def register_TrdCapRptSideGrp_component(self):
    self.register_group(fields.NoSides, NoSidesGroup, True)

def register_TrdCollGrp_component(self):
    self.register_group(fields.NoTrades, NoTradesGroup, False)

def register_TrdInstrmtLegGrp_component(self):
    self.register_group(fields.NoLegs, NoLegsGroup, False)

def register_TrdgSesGrp_component(self):
    self.register_group(fields.NoTradingSessions, NoTradingSessionsGroup, False)

def register_UndInstrmtCollGrp_component(self):
    self.register_group(fields.NoUnderlyings, NoUnderlyingsGroup, False)

def register_UndInstrmtGrp_component(self):
    self.register_group(fields.NoUnderlyings, NoUnderlyingsGroup, False)

def register_UndInstrmtStrkPxGrp_component(self):
    self.register_group(fields.NoUnderlyings, NoUnderlyingsGroup, False)

def register_TrdCapDtGrp_component(self):
    self.register_group(fields.NoDates, NoDatesGroup, False)

def register_EvntGrp_component(self):
    self.register_group(fields.NoEvents, NoEventsGroup, False)

def register_SecAltIDGrp_component(self):
    self.register_group(fields.NoSecurityAltID, NoSecurityAltIDGroup, False)

def register_LegSecAltIDGrp_component(self):
    self.register_group(fields.NoLegSecurityAltID, NoLegSecurityAltIDGroup, False)

def register_UndSecAltIDGrp_component(self):
    self.register_group(fields.NoUnderlyingSecurityAltID, NoUnderlyingSecurityAltIDGroup, False)

def register_AttrbGrp_component(self):
    self.register_group(fields.NoInstrAttrib, NoInstrAttribGroup, False)

def register_DlvyInstGrp_component(self):
    self.register_group(fields.NoDlvyInst, NoDlvyInstGroup, False)

def register_SettlPtysSubGrp_component(self):
    self.register_group(fields.NoSettlPartySubIDs, NoSettlPartySubIDsGroup, False)

def register_PtysSubGrp_component(self):
    self.register_group(fields.NoPartySubIDs, NoPartySubIDsGroup, False)

def register_NstdPtysSubGrp_component(self):
    self.register_group(fields.NoNestedPartySubIDs, NoNestedPartySubIDsGroup, False)

def register_HopGrp_component(self):
    self.register_group(fields.NoHops, NoHopsGroup, False)

def register_NstdPtys2SubGrp_component(self):
    self.register_group(fields.NoNested2PartySubIDs, NoNested2PartySubIDsGroup, False)

def register_NstdPtys3SubGrp_component(self):
    self.register_group(fields.NoNested3PartySubIDs, NoNested3PartySubIDsGroup, False)

def register_StrategyParametersGrp_component(self):
    self.register_group(fields.NoStrategyParameters, NoStrategyParametersGroup, False)

def register_SecLstUpdRelSymGrp_component(self):
    self.register_group(fields.NoRelatedSym, NoRelatedSymGroup, False)

def register_SecLstUpdRelSymsLegGrp_component(self):
    self.register_group(fields.NoLegs, NoLegsGroup, False)

def register_UnderlyingAmount_component(self):
    self.register_group(fields.NoUnderlyingAmounts, NoUnderlyingAmountsGroup, False)

def register_ExpirationQty_component(self):
    self.register_group(fields.NoExpiration, NoExpirationGroup, False)

def register_InstrumentParties_component(self):
    self.register_group(fields.NoInstrumentParties, NoInstrumentPartiesGroup, False)

def register_InstrumentPtysSubGrp_component(self):
    self.register_group(fields.NoInstrumentPartySubIDs, NoInstrumentPartySubIDsGroup, False)

def register_SideTrdRegTS_component(self):
    self.register_group(fields.NoSideTrdRegTS, NoSideTrdRegTSGroup, False)

def register_TrdCapRptAckSideGrp_component(self):
    self.register_group(fields.NoSides, NoSidesGroup, True)

def register_UndlyInstrumentParties_component(self):
    self.register_group(fields.NoUndlyInstrumentParties, NoUndlyInstrumentPartiesGroup, False)

def register_UndlyInstrumentPtysSubGrp_component(self):
    self.register_group(fields.NoUndlyInstrumentPartySubIDs, NoUndlyInstrumentPartySubIDsGroup, False)

def register_DisplayInstruction_component(self):
    self.register_field(fields.DisplayQty, False)
    self.register_field(fields.SecondaryDisplayQty, False)
    self.register_field(fields.DisplayWhen, False)
    self.register_field(fields.DisplayMethod, False)
    self.register_field(fields.DisplayLowQty, False)
    self.register_field(fields.DisplayHighQty, False)
    self.register_field(fields.DisplayMinIncr, False)
    self.register_field(fields.RefreshQty, False)

def register_TriggeringInstruction_component(self):
    self.register_field(fields.TriggerType, False)
    self.register_field(fields.TriggerAction, False)
    self.register_field(fields.TriggerPrice, False)
    self.register_field(fields.TriggerSymbol, False)
    self.register_field(fields.TriggerSecurityID, False)
    self.register_field(fields.TriggerSecurityIDSource, False)
    self.register_field(fields.TriggerSecurityDesc, False)
    self.register_field(fields.TriggerPriceType, False)
    self.register_field(fields.TriggerPriceTypeScope, False)
    self.register_field(fields.TriggerPriceDirection, False)
    self.register_field(fields.TriggerNewPrice, False)
    self.register_field(fields.TriggerOrderType, False)
    self.register_field(fields.TriggerNewQty, False)
    self.register_field(fields.TriggerTradingSessionID, False)
    self.register_field(fields.TriggerTradingSessionSubID, False)

def register_RootParties_component(self):
    self.register_group(fields.NoRootPartyIDs, NoRootPartyIDsGroup, False)

def register_RootSubParties_component(self):
    self.register_group(fields.NoRootPartySubIDs, NoRootPartySubIDsGroup, False)

def register_TrdSessLstGrp_component(self):
    self.register_group(fields.NoTradingSessions, NoTradingSessionsGroup, True)

def register_MsgTypeGrp_component(self):
    self.register_group(fields.NoMsgTypes, NoMsgTypesGroup, False)

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
        self.register_field(fields.IOIID, True)
        self.register_field(fields.IOITransType, True)
        self.register_field(fields.IOIRefID, False)
        register_Instrument_component(self)
        register_Parties_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.Side, True)
        self.register_field(fields.QtyType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.IOIQty, True)
        self.register_field(fields.Currency, False)
        register_Stipulations_component(self)
        register_InstrmtLegIOIGrp_component(self)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.ValidUntilTime, False)
        self.register_field(fields.IOIQltyInd, False)
        self.register_field(fields.IOINaturalFlag, False)
        register_IOIQualGrp_component(self)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.URLLink, False)
        register_RoutingGrp_component(self)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)


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
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.AdvSide, True)
        self.register_field(fields.Quantity, True)
        self.register_field(fields.QtyType, False)
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
        self.register_field(fields.QuoteRespID, False)
        self.register_field(fields.OrdStatusReqID, False)
        self.register_field(fields.MassStatusReqID, False)
        self.register_field(fields.HostCrossID, False)
        self.register_field(fields.TotNumReports, False)
        self.register_field(fields.LastRptRequested, False)
        register_Parties_component(self)
        self.register_field(fields.TradeOriginationDate, False)
        register_ContraGrp_component(self)
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
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.MatchType, False)
        self.register_field(fields.OrderCategory, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.Side, True)
        register_Stipulations_component(self)
        self.register_field(fields.QtyType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.LotType, False)
        self.register_field(fields.OrdType, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceProtectionScope, False)
        self.register_field(fields.StopPx, False)
        register_TriggeringInstruction_component(self)
        register_PegInstructions_component(self)
        register_DiscretionInstructions_component(self)
        self.register_field(fields.PeggedPrice, False)
        self.register_field(fields.PeggedRefPrice, False)
        self.register_field(fields.DiscretionPrice, False)
        self.register_field(fields.TargetStrategy, False)
        register_StrategyParametersGrp_component(self)
        self.register_field(fields.TargetStrategyParameters, False)
        self.register_field(fields.ParticipationRate, False)
        self.register_field(fields.TargetStrategyPerformance, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.AggressorIndicator, False)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.PreTradeAnonymity, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.LastQty, False)
        self.register_field(fields.CalculatedCcyLastQty, False)
        self.register_field(fields.LastSwapPoints, False)
        self.register_field(fields.UnderlyingLastQty, False)
        self.register_field(fields.LastPx, False)
        self.register_field(fields.UnderlyingLastPx, False)
        self.register_field(fields.LastParPx, False)
        self.register_field(fields.LastSpotRate, False)
        self.register_field(fields.LastForwardPoints, False)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.TimeBracket, False)
        self.register_field(fields.LastCapacity, False)
        self.register_field(fields.LeavesQty, True)
        self.register_field(fields.CumQty, True)
        self.register_field(fields.AvgPx, False)
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
        self.register_field(fields.InterestAtMaturity, False)
        self.register_field(fields.EndAccruedInterestAmt, False)
        self.register_field(fields.StartCash, False)
        self.register_field(fields.EndCash, False)
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
        self.register_field(fields.MatchIncrement, False)
        self.register_field(fields.MaxPriceLevels, False)
        register_DisplayInstruction_component(self)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.MaxShow, False)
        self.register_field(fields.BookingType, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.SettlDate2, False)
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
        self.register_field(fields.LastLiquidityInd, False)
        register_ContAmtGrp_component(self)
        register_InstrmtLegExecGrp_component(self)
        self.register_field(fields.CopyMsgIndicator, False)
        register_MiscFeesGrp_component(self)
        self.register_field(fields.ManualOrderIndicator, False)
        self.register_field(fields.CustDirectedOrder, False)
        self.register_field(fields.ReceivedDeptID, False)
        self.register_field(fields.CustOrderHandlingInst, False)
        self.register_field(fields.OrderHandlingInstSource, False)
        register_TrdRegTimestamps_component(self)


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
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.TradeDate, False)
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
        self.register_field(fields.NextExpectedMsgSeqNum, False)
        self.register_field(fields.MaxMessageSize, False)
        register_MsgTypeGrp_component(self)
        self.register_field(fields.TestMessageIndicator, False)
        self.register_field(fields.Username, False)
        self.register_field(fields.Password, False)
        self.register_field(fields.DefaultApplVerID, True)


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
        register_RoutingGrp_component(self)
        register_InstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtGrp_component(self)
        register_LinesOfTextGrp_component(self)
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
        register_RoutingGrp_component(self)
        register_InstrmtGrp_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.ClOrdID, False)
        register_LinesOfTextGrp_component(self)
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
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_field(fields.AllocID, False)
        register_PreAllocGrp_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.HandlInst, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MatchIncrement, False)
        self.register_field(fields.MaxPriceLevels, False)
        register_DisplayInstruction_component(self)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ExDestinationIDSource, False)
        register_TrdgSesGrp_component(self)
        self.register_field(fields.ProcessCode, False)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, True)
        register_Stipulations_component(self)
        self.register_field(fields.QtyType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceProtectionScope, False)
        self.register_field(fields.StopPx, False)
        register_TriggeringInstruction_component(self)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.IOIID, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        register_CommissionData_component(self)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.PreTradeAnonymity, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.BookingType, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.SettlDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.Price2, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.CoveredOrUncovered, False)
        self.register_field(fields.MaxShow, False)
        register_PegInstructions_component(self)
        register_DiscretionInstructions_component(self)
        self.register_field(fields.TargetStrategy, False)
        register_StrategyParametersGrp_component(self)
        self.register_field(fields.TargetStrategyParameters, False)
        self.register_field(fields.ParticipationRate, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.ManualOrderIndicator, False)
        self.register_field(fields.CustDirectedOrder, False)
        self.register_field(fields.ReceivedDeptID, False)
        self.register_field(fields.CustOrderHandlingInst, False)
        self.register_field(fields.OrderHandlingInstSource, False)
        register_TrdRegTimestamps_component(self)
        self.register_field(fields.RefOrderID, False)
        self.register_field(fields.RefOrderIDSource, False)


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
        self.register_field(fields.AllowableOneSidednessPct, False)
        self.register_field(fields.AllowableOneSidednessValue, False)
        self.register_field(fields.AllowableOneSidednessCurr, False)
        self.register_field(fields.TotNoOrders, True)
        self.register_field(fields.LastFragment, False)
        register_RootParties_component(self)
        register_ListOrdGrp_component(self)


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
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        register_Parties_component(self)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
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
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.OrigClOrdID, True)
        self.register_field(fields.ClOrdID, True)
        self.register_field(fields.SecondaryClOrdID, False)
        self.register_field(fields.ClOrdLinkID, False)
        self.register_field(fields.ListID, False)
        self.register_field(fields.OrigOrdModTime, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_field(fields.AllocID, False)
        register_PreAllocGrp_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.HandlInst, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MatchIncrement, False)
        self.register_field(fields.MaxPriceLevels, False)
        register_DisplayInstruction_component(self)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ExDestinationIDSource, False)
        register_TrdgSesGrp_component(self)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.Side, True)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.QtyType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceProtectionScope, False)
        self.register_field(fields.StopPx, False)
        register_TriggeringInstruction_component(self)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        register_PegInstructions_component(self)
        register_DiscretionInstructions_component(self)
        self.register_field(fields.TargetStrategy, False)
        register_StrategyParametersGrp_component(self)
        self.register_field(fields.TargetStrategyParameters, False)
        self.register_field(fields.ParticipationRate, False)
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
        self.register_field(fields.PreTradeAnonymity, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.BookingType, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.SettlDate2, False)
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
        self.register_field(fields.ManualOrderIndicator, False)
        self.register_field(fields.CustDirectedOrder, False)
        self.register_field(fields.ReceivedDeptID, False)
        self.register_field(fields.CustOrderHandlingInst, False)
        self.register_field(fields.OrderHandlingInstSource, False)
        register_TrdRegTimestamps_component(self)


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
        self.register_field(fields.OrdStatusReqID, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.Side, True)


MESSAGE_TYPES['H'] = OrderStatusRequest

class AllocationInstruction(fix_message.MessageBase):
    _msgtype = 'J'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.AllocID, True)
        self.register_field(fields.AllocTransType, True)
        self.register_field(fields.AllocType, True)
        self.register_field(fields.SecondaryAllocID, False)
        self.register_field(fields.RefAllocID, False)
        self.register_field(fields.AllocCancReplaceReason, False)
        self.register_field(fields.AllocIntermedReqType, False)
        self.register_field(fields.AllocLinkID, False)
        self.register_field(fields.AllocLinkType, False)
        self.register_field(fields.BookingRefID, False)
        self.register_field(fields.AllocNoOrdersType, False)
        register_OrdAllocGrp_component(self)
        register_ExecAllocGrp_component(self)
        self.register_field(fields.PreviouslyReported, False)
        self.register_field(fields.ReversalIndicator, False)
        self.register_field(fields.MatchType, False)
        self.register_field(fields.Side, True)
        register_Instrument_component(self)
        register_InstrumentExtension_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.Quantity, True)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.AvgPx, False)
        self.register_field(fields.AvgParPx, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.AvgPxPrecision, False)
        register_Parties_component(self)
        self.register_field(fields.TradeDate, True)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.BookingType, False)
        self.register_field(fields.GrossTradeAmt, False)
        self.register_field(fields.Concession, False)
        self.register_field(fields.TotalTakedown, False)
        self.register_field(fields.NetMoney, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.AutoAcceptIndicator, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.NumDaysInterest, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.TotalAccruedInterestAmt, False)
        self.register_field(fields.InterestAtMaturity, False)
        self.register_field(fields.EndAccruedInterestAmt, False)
        self.register_field(fields.StartCash, False)
        self.register_field(fields.EndCash, False)
        self.register_field(fields.LegalConfirm, False)
        register_Stipulations_component(self)
        register_YieldData_component(self)
        register_PositionAmountData_component(self)
        self.register_field(fields.TotNoAllocs, False)
        self.register_field(fields.LastFragment, False)
        register_AllocGrp_component(self)
        self.register_field(fields.AvgPxIndicator, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.TrdType, False)
        self.register_field(fields.TrdSubType, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.TradeInputSource, False)
        self.register_field(fields.MultiLegReportingType, False)
        self.register_field(fields.MessageEventSource, False)
        self.register_field(fields.RndPx, False)


MESSAGE_TYPES['J'] = AllocationInstruction

class ListCancelRequest(fix_message.MessageBase):
    _msgtype = 'K'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ListID, True)
        register_Parties_component(self)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.TradeDate, False)
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
        self.register_field(fields.LastFragment, False)
        register_OrdListStatGrp_component(self)


MESSAGE_TYPES['N'] = ListStatus

class AllocationInstructionAck(fix_message.MessageBase):
    _msgtype = 'P'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.AllocID, True)
        register_Parties_component(self)
        self.register_field(fields.SecondaryAllocID, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.AllocStatus, True)
        self.register_field(fields.AllocRejCode, False)
        self.register_field(fields.AllocType, False)
        self.register_field(fields.AllocIntermedReqType, False)
        self.register_field(fields.MatchStatus, False)
        self.register_field(fields.Product, False)
        self.register_field(fields.SecurityType, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        register_AllocAckGrp_component(self)


MESSAGE_TYPES['P'] = AllocationInstructionAck

class DontKnowTrade(fix_message.MessageBase):
    _msgtype = 'Q'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, True)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.ExecID, True)
        self.register_field(fields.DKReason, True)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
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
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.OrderCapacity, False)
        register_QuotReqGrp_component(self)
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
        self.register_field(fields.QuoteRespID, False)
        self.register_field(fields.QuoteType, False)
        register_QuotQualGrp_component(self)
        self.register_field(fields.QuoteResponseLevel, False)
        register_Parties_component(self)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.Side, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.SettlDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.Currency, False)
        register_Stipulations_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        register_LegQuotGrp_component(self)
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
        self.register_field(fields.BidSwapPoints, False)
        self.register_field(fields.OfferSwapPoints, False)
        self.register_field(fields.MidPx, False)
        self.register_field(fields.BidYield, False)
        self.register_field(fields.MidYield, False)
        self.register_field(fields.OfferYield, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.OrdType, False)
        self.register_field(fields.BidForwardPoints2, False)
        self.register_field(fields.OfferForwardPoints2, False)
        self.register_field(fields.SettlCurrBidFxRate, False)
        self.register_field(fields.SettlCurrOfferFxRate, False)
        self.register_field(fields.SettlCurrFxRateCalc, False)
        self.register_field(fields.CommType, False)
        self.register_field(fields.Commission, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ExDestinationIDSource, False)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.PriceType, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
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
        self.register_field(fields.SettlInstMsgID, True)
        self.register_field(fields.SettlInstReqID, False)
        self.register_field(fields.SettlInstMode, True)
        self.register_field(fields.SettlInstReqRejCode, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.TransactTime, True)
        register_SettlInstGrp_component(self)


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
        self.register_field(fields.OpenCloseSettlFlag, False)
        self.register_field(fields.Scope, False)
        self.register_field(fields.MDImplicitDelete, False)
        register_MDReqGrp_component(self)
        register_InstrmtMDReqGrp_component(self)
        register_TrdgSesGrp_component(self)
        self.register_field(fields.ApplQueueAction, False)
        self.register_field(fields.ApplQueueMax, False)
        self.register_field(fields.MDQuoteType, False)


MESSAGE_TYPES['V'] = MarketDataRequest

class MarketDataSnapshotFullRefresh(fix_message.MessageBase):
    _msgtype = 'W'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.MDReportID, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.MDBookType, False)
        self.register_field(fields.MDFeedType, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.MDReqID, False)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.FinancialStatus, False)
        self.register_field(fields.CorporateAction, False)
        self.register_field(fields.NetChgPrevDay, False)
        register_MDFullGrp_component(self)
        self.register_field(fields.ApplQueueDepth, False)
        self.register_field(fields.ApplQueueResolution, False)
        register_RoutingGrp_component(self)


MESSAGE_TYPES['W'] = MarketDataSnapshotFullRefresh

class MarketDataIncrementalRefresh(fix_message.MessageBase):
    _msgtype = 'X'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.MDBookType, False)
        self.register_field(fields.MDFeedType, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.MDReqID, False)
        register_MDIncGrp_component(self)
        self.register_field(fields.ApplQueueDepth, False)
        self.register_field(fields.ApplQueueResolution, False)
        register_RoutingGrp_component(self)


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
        register_MDRjctGrp_component(self)
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
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.QuoteCancelType, True)
        self.register_field(fields.QuoteResponseLevel, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_QuotCxlEntriesGrp_component(self)


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
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
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
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        register_QuotSetAckGrp_component(self)


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
        register_InstrumentExtension_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.ExpirationCycle, False)
        self.register_field(fields.SubscriptionRequestType, False)


MESSAGE_TYPES['c'] = SecurityDefinitionRequest

class SecurityDefinition(fix_message.MessageBase):
    _msgtype = 'd'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReportID, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.SecurityReqID, False)
        self.register_field(fields.SecurityResponseID, False)
        self.register_field(fields.SecurityResponseType, False)
        register_Instrument_component(self)
        register_InstrumentExtension_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.ExpirationCycle, False)
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
        register_InstrumentExtension_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
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
        register_InstrumentExtension_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
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
        self.register_field(fields.FirstPx, False)
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
        self.register_field(fields.SecurityExchange, False)


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
        register_Instrument_component(self)


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
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DefBidSize, False)
        self.register_field(fields.DefOfferSize, False)
        register_QuotSetGrp_component(self)


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
        self.register_field(fields.TotNoRelatedSym, True)
        self.register_field(fields.BidType, True)
        self.register_field(fields.NumTickets, False)
        self.register_field(fields.Currency, False)
        self.register_field(fields.SideValue1, False)
        self.register_field(fields.SideValue2, False)
        register_BidDescReqGrp_component(self)
        register_BidCompReqGrp_component(self)
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
        self.register_field(fields.BidTradeType, True)
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
        register_BidCompRspGrp_component(self)


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
        self.register_field(fields.LastFragment, False)
        register_InstrmtStrkPxGrp_component(self)
        register_UndInstrmtStrkPxGrp_component(self)


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
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.RegistAcctType, False)
        self.register_field(fields.TaxAdvantageType, False)
        self.register_field(fields.OwnershipType, False)
        register_RgstDtlsGrp_component(self)
        register_RgstDistInstGrp_component(self)


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
        self.register_field(fields.AcctIDSource, False)
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
        register_Parties_component(self)
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
        register_AffectedOrdGrp_component(self)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_Parties_component(self)
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
        register_RootParties_component(self)
        register_SideCrossOrdModGrp_component(self)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.HandlInst, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MatchIncrement, False)
        self.register_field(fields.MaxPriceLevels, False)
        register_DisplayInstruction_component(self)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ExDestinationIDSource, False)
        register_TrdgSesGrp_component(self)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.TransBkdTime, False)
        register_Stipulations_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceProtectionScope, False)
        self.register_field(fields.StopPx, False)
        register_TriggeringInstruction_component(self)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.IOIID, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        self.register_field(fields.MaxShow, False)
        register_PegInstructions_component(self)
        register_DiscretionInstructions_component(self)
        self.register_field(fields.TargetStrategy, False)
        register_StrategyParametersGrp_component(self)
        self.register_field(fields.TargetStrategyParameters, False)
        self.register_field(fields.ParticipationRate, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)


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
        self.register_field(fields.HostCrossID, False)
        self.register_field(fields.CrossType, True)
        self.register_field(fields.CrossPrioritization, True)
        register_RootParties_component(self)
        register_SideCrossOrdModGrp_component(self)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.HandlInst, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MatchIncrement, False)
        self.register_field(fields.MaxPriceLevels, False)
        register_DisplayInstruction_component(self)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ExDestinationIDSource, False)
        register_TrdgSesGrp_component(self)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.TransBkdTime, False)
        register_Stipulations_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceProtectionScope, False)
        self.register_field(fields.StopPx, False)
        register_TriggeringInstruction_component(self)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.IOIID, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        self.register_field(fields.MaxShow, False)
        register_PegInstructions_component(self)
        register_DiscretionInstructions_component(self)
        self.register_field(fields.TargetStrategy, False)
        register_StrategyParametersGrp_component(self)
        self.register_field(fields.TargetStrategyParameters, False)
        self.register_field(fields.ParticipationRate, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)


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
        self.register_field(fields.HostCrossID, False)
        self.register_field(fields.CrossType, True)
        self.register_field(fields.CrossPrioritization, True)
        register_RootParties_component(self)
        register_SideCrossOrdCxlGrp_component(self)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
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
        self.register_field(fields.Product, False)
        self.register_field(fields.SecurityType, False)
        self.register_field(fields.SecuritySubType, False)


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
        self.register_field(fields.TotNoSecurityTypes, False)
        self.register_field(fields.LastFragment, False)
        register_SecTypesGrp_component(self)
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
        register_InstrumentExtension_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
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
        self.register_field(fields.SecurityReportID, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.SecurityReqID, False)
        self.register_field(fields.SecurityResponseID, False)
        self.register_field(fields.SecurityRequestResult, False)
        self.register_field(fields.TotNoRelatedSym, False)
        self.register_field(fields.LastFragment, False)
        register_SecListGrp_component(self)


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
        self.register_field(fields.SecuritySubType, False)
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
        self.register_field(fields.TotNoRelatedSym, False)
        self.register_field(fields.LastFragment, False)
        register_RelSymDerivSecGrp_component(self)


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
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_field(fields.AllocID, False)
        register_PreAllocMlegGrp_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.HandlInst, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MatchIncrement, False)
        self.register_field(fields.MaxPriceLevels, False)
        register_DisplayInstruction_component(self)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ExDestinationIDSource, False)
        register_TrdgSesGrp_component(self)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.Side, True)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.SwapPoints, False)
        register_LegOrdGrp_component(self)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.QtyType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceProtectionScope, False)
        self.register_field(fields.StopPx, False)
        register_TriggeringInstruction_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.IOIID, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.RefOrderID, False)
        self.register_field(fields.RefOrderIDSource, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        register_CommissionData_component(self)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.PreTradeAnonymity, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.BookingType, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.CoveredOrUncovered, False)
        self.register_field(fields.MaxShow, False)
        register_PegInstructions_component(self)
        register_DiscretionInstructions_component(self)
        self.register_field(fields.TargetStrategy, False)
        register_StrategyParametersGrp_component(self)
        self.register_field(fields.TargetStrategyParameters, False)
        self.register_field(fields.ParticipationRate, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.MultiLegRptTypeReq, False)


MESSAGE_TYPES['AB'] = NewOrderMultileg

class MultilegOrderCancelReplace(fix_message.MessageBase):
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
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.DayBookingInst, False)
        self.register_field(fields.BookingUnit, False)
        self.register_field(fields.PreallocMethod, False)
        self.register_field(fields.AllocID, False)
        register_PreAllocMlegGrp_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.CashMargin, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        self.register_field(fields.HandlInst, False)
        self.register_field(fields.ExecInst, False)
        self.register_field(fields.MinQty, False)
        self.register_field(fields.MatchIncrement, False)
        self.register_field(fields.MaxPriceLevels, False)
        register_DisplayInstruction_component(self)
        self.register_field(fields.MaxFloor, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ExDestinationIDSource, False)
        register_TrdgSesGrp_component(self)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.Side, True)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.PrevClosePx, False)
        self.register_field(fields.SwapPoints, False)
        register_LegOrdGrp_component(self)
        self.register_field(fields.LocateReqd, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.QtyType, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.OrdType, True)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceProtectionScope, False)
        self.register_field(fields.StopPx, False)
        register_TriggeringInstruction_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.ComplianceID, False)
        self.register_field(fields.SolicitedFlag, False)
        self.register_field(fields.IOIID, False)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.TimeInForce, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.GTBookingInst, False)
        register_CommissionData_component(self)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.OrderRestrictions, False)
        self.register_field(fields.PreTradeAnonymity, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ForexReq, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.BookingType, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.CoveredOrUncovered, False)
        self.register_field(fields.MaxShow, False)
        register_PegInstructions_component(self)
        register_DiscretionInstructions_component(self)
        self.register_field(fields.TargetStrategy, False)
        register_StrategyParametersGrp_component(self)
        self.register_field(fields.TargetStrategyParameters, False)
        self.register_field(fields.ParticipationRate, False)
        self.register_field(fields.CancellationRights, False)
        self.register_field(fields.MoneyLaunderingStatus, False)
        self.register_field(fields.RegistID, False)
        self.register_field(fields.Designation, False)
        self.register_field(fields.MultiLegRptTypeReq, False)


MESSAGE_TYPES['AC'] = MultilegOrderCancelReplace

class TradeCaptureReportRequest(fix_message.MessageBase):
    _msgtype = 'AD'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TradeRequestID, True)
        self.register_field(fields.TradeID, False)
        self.register_field(fields.SecondaryTradeID, False)
        self.register_field(fields.FirmTradeID, False)
        self.register_field(fields.SecondaryFirmTradeID, False)
        self.register_field(fields.TradeRequestType, True)
        self.register_field(fields.SubscriptionRequestType, False)
        self.register_field(fields.TradeReportID, False)
        self.register_field(fields.SecondaryTradeReportID, False)
        self.register_field(fields.ExecID, False)
        self.register_field(fields.ExecType, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.MatchStatus, False)
        self.register_field(fields.TrdType, False)
        self.register_field(fields.TrdSubType, False)
        self.register_field(fields.TradeHandlingInstr, False)
        self.register_field(fields.TransferReason, False)
        self.register_field(fields.SecondaryTrdType, False)
        self.register_field(fields.TradeLinkID, False)
        self.register_field(fields.TrdMatchID, False)
        register_Parties_component(self)
        register_Instrument_component(self)
        register_InstrumentExtension_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        register_TrdCapDtGrp_component(self)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.TimeBracket, False)
        self.register_field(fields.Side, False)
        self.register_field(fields.MultiLegReportingType, False)
        self.register_field(fields.TradeInputSource, False)
        self.register_field(fields.TradeInputDevice, False)
        self.register_field(fields.ResponseTransportType, False)
        self.register_field(fields.ResponseDestination, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.MessageEventSource, False)


MESSAGE_TYPES['AD'] = TradeCaptureReportRequest

class TradeCaptureReport(fix_message.MessageBase):
    _msgtype = 'AE'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TradeReportID, False)
        self.register_field(fields.TradeID, False)
        self.register_field(fields.SecondaryTradeID, False)
        self.register_field(fields.FirmTradeID, False)
        self.register_field(fields.SecondaryFirmTradeID, False)
        self.register_field(fields.TradeReportTransType, False)
        self.register_field(fields.TradeReportType, False)
        self.register_field(fields.TrdRptStatus, False)
        self.register_field(fields.TradeRequestID, False)
        self.register_field(fields.TrdType, False)
        self.register_field(fields.TrdSubType, False)
        self.register_field(fields.SecondaryTrdType, False)
        self.register_field(fields.TradeHandlingInstr, False)
        self.register_field(fields.OrigTradeHandlingInstr, False)
        self.register_field(fields.OrigTradeDate, False)
        self.register_field(fields.OrigTradeID, False)
        self.register_field(fields.OrigSecondaryTradeID, False)
        self.register_field(fields.TransferReason, False)
        self.register_field(fields.ExecType, False)
        self.register_field(fields.TotNumTradeReports, False)
        self.register_field(fields.LastRptRequested, False)
        self.register_field(fields.UnsolicitedIndicator, False)
        self.register_field(fields.SubscriptionRequestType, False)
        self.register_field(fields.TradeReportRefID, False)
        self.register_field(fields.SecondaryTradeReportRefID, False)
        self.register_field(fields.SecondaryTradeReportID, False)
        self.register_field(fields.TradeLinkID, False)
        self.register_field(fields.TrdMatchID, False)
        self.register_field(fields.ExecID, False)
        self.register_field(fields.OrdStatus, False)
        self.register_field(fields.SecondaryExecID, False)
        self.register_field(fields.ExecRestatementReason, False)
        self.register_field(fields.PreviouslyReported, False)
        self.register_field(fields.PriceType, False)
        register_RootParties_component(self)
        self.register_field(fields.AsOfIndicator, False)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        register_OrderQtyData_component(self)
        self.register_field(fields.QtyType, False)
        register_YieldData_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.UnderlyingTradingSessionID, False)
        self.register_field(fields.UnderlyingTradingSessionSubID, False)
        self.register_field(fields.LastQty, True)
        self.register_field(fields.LastPx, True)
        self.register_field(fields.CalculatedCcyLastQty, False)
        self.register_field(fields.LastParPx, False)
        self.register_field(fields.LastSpotRate, False)
        self.register_field(fields.LastForwardPoints, False)
        self.register_field(fields.LastSwapPoints, False)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradeDate, True)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.AvgPx, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        self.register_field(fields.AvgPxIndicator, False)
        register_PositionAmountData_component(self)
        self.register_field(fields.MultiLegReportingType, False)
        self.register_field(fields.TradeLegRefID, False)
        register_TrdInstrmtLegGrp_component(self)
        self.register_field(fields.TransactTime, False)
        register_TrdRegTimestamps_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.UnderlyingSettlementDate, False)
        self.register_field(fields.MatchStatus, False)
        self.register_field(fields.MatchType, False)
        self.register_field(fields.OrderCategory, False)
        register_TrdCapRptSideGrp_component(self)
        self.register_field(fields.CopyMsgIndicator, False)
        self.register_field(fields.PublishTrdIndicator, False)
        self.register_field(fields.ShortSaleReason, False)
        self.register_field(fields.TierCode, False)
        self.register_field(fields.MessageEventSource, False)
        self.register_field(fields.LastUpdateTime, False)
        self.register_field(fields.RndPx, False)
        self.register_field(fields.TZTransactTime, False)
        self.register_field(fields.ReportedPxDiff, False)
        self.register_field(fields.GrossTradeAmt, False)


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
        self.register_field(fields.AcctIDSource, False)
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
        register_QuotReqRjctGrp_component(self)
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
        register_RFQReqGrp_component(self)
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
        self.register_field(fields.QuoteRespID, False)
        self.register_field(fields.QuoteType, False)
        register_Parties_component(self)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.Side, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.SettlDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.Currency, False)
        register_Stipulations_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        register_LegQuotStatGrp_component(self)
        register_QuotQualGrp_component(self)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceType, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)
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
        self.register_field(fields.OrdType, False)
        self.register_field(fields.BidForwardPoints2, False)
        self.register_field(fields.OfferForwardPoints2, False)
        self.register_field(fields.SettlCurrBidFxRate, False)
        self.register_field(fields.SettlCurrOfferFxRate, False)
        self.register_field(fields.SettlCurrFxRateCalc, False)
        self.register_field(fields.CommType, False)
        self.register_field(fields.Commission, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ExDestinationIDSource, False)
        self.register_field(fields.QuoteStatus, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AI'] = QuoteStatusReport

class QuoteResponse(fix_message.MessageBase):
    _msgtype = 'AJ'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.QuoteRespID, True)
        self.register_field(fields.QuoteID, False)
        self.register_field(fields.QuoteRespType, True)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.OrderCapacity, False)
        self.register_field(fields.IOIID, False)
        self.register_field(fields.QuoteType, False)
        register_QuotQualGrp_component(self)
        register_Parties_component(self)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.Side, False)
        register_OrderQtyData_component(self)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.SettlDate2, False)
        self.register_field(fields.OrderQty2, False)
        self.register_field(fields.Currency, False)
        register_Stipulations_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        register_LegQuotGrp_component(self)
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
        self.register_field(fields.OrdType, False)
        self.register_field(fields.BidForwardPoints2, False)
        self.register_field(fields.OfferForwardPoints2, False)
        self.register_field(fields.SettlCurrBidFxRate, False)
        self.register_field(fields.SettlCurrOfferFxRate, False)
        self.register_field(fields.SettlCurrFxRateCalc, False)
        self.register_field(fields.Commission, False)
        self.register_field(fields.CommType, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.ExDestination, False)
        self.register_field(fields.ExDestinationIDSource, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceType, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_YieldData_component(self)


MESSAGE_TYPES['AJ'] = QuoteResponse

class Confirmation(fix_message.MessageBase):
    _msgtype = 'AK'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ConfirmID, True)
        self.register_field(fields.ConfirmRefID, False)
        self.register_field(fields.ConfirmReqID, False)
        self.register_field(fields.ConfirmTransType, True)
        self.register_field(fields.ConfirmType, True)
        self.register_field(fields.CopyMsgIndicator, False)
        self.register_field(fields.LegalConfirm, False)
        self.register_field(fields.ConfirmStatus, True)
        register_Parties_component(self)
        register_OrdAllocGrp_component(self)
        self.register_field(fields.AllocID, False)
        self.register_field(fields.SecondaryAllocID, False)
        self.register_field(fields.IndividualAllocID, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.TradeDate, True)
        register_TrdRegTimestamps_component(self)
        register_Instrument_component(self)
        register_InstrumentExtension_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        register_YieldData_component(self)
        self.register_field(fields.AllocQty, True)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.Side, True)
        self.register_field(fields.Currency, False)
        self.register_field(fields.LastMkt, False)
        register_CpctyConfGrp_component(self)
        self.register_field(fields.AllocAccount, True)
        self.register_field(fields.AllocAcctIDSource, False)
        self.register_field(fields.AllocAccountType, False)
        self.register_field(fields.AvgPx, True)
        self.register_field(fields.AvgPxPrecision, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.AvgParPx, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        self.register_field(fields.ReportedPx, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.ProcessCode, False)
        self.register_field(fields.GrossTradeAmt, True)
        self.register_field(fields.NumDaysInterest, False)
        self.register_field(fields.ExDate, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.InterestAtMaturity, False)
        self.register_field(fields.EndAccruedInterestAmt, False)
        self.register_field(fields.StartCash, False)
        self.register_field(fields.EndCash, False)
        self.register_field(fields.Concession, False)
        self.register_field(fields.TotalTakedown, False)
        self.register_field(fields.NetMoney, True)
        self.register_field(fields.MaturityNetMoney, False)
        self.register_field(fields.SettlCurrAmt, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.SettlCurrFxRate, False)
        self.register_field(fields.SettlCurrFxRateCalc, False)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        register_SettlInstructionsData_component(self)
        register_CommissionData_component(self)
        self.register_field(fields.SharedCommission, False)
        register_Stipulations_component(self)
        register_MiscFeesGrp_component(self)


MESSAGE_TYPES['AK'] = Confirmation

class PositionMaintenanceRequest(fix_message.MessageBase):
    _msgtype = 'AL'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.PosReqID, False)
        self.register_field(fields.PosTransType, True)
        self.register_field(fields.PosMaintAction, True)
        self.register_field(fields.OrigPosReqRefID, False)
        self.register_field(fields.PosMaintRptRefID, False)
        self.register_field(fields.ClearingBusinessDate, True)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtGrp_component(self)
        register_TrdgSesGrp_component(self)
        self.register_field(fields.TransactTime, False)
        register_PositionQty_component(self)
        register_PositionAmountData_component(self)
        self.register_field(fields.AdjustmentType, False)
        self.register_field(fields.ContraryInstructionIndicator, False)
        self.register_field(fields.PriorSpreadIndicator, False)
        self.register_field(fields.ThresholdAmount, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.SettlCurrency, False)


MESSAGE_TYPES['AL'] = PositionMaintenanceRequest

class PositionMaintenanceReport(fix_message.MessageBase):
    _msgtype = 'AM'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.PosMaintRptID, True)
        self.register_field(fields.PosTransType, True)
        self.register_field(fields.PosReqID, False)
        self.register_field(fields.PosMaintAction, True)
        self.register_field(fields.OrigPosReqRefID, False)
        self.register_field(fields.PosMaintStatus, True)
        self.register_field(fields.PosMaintResult, False)
        self.register_field(fields.ClearingBusinessDate, True)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.PosMaintRptRefID, False)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.ContraryInstructionIndicator, False)
        self.register_field(fields.PriorSpreadIndicator, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtGrp_component(self)
        register_TrdgSesGrp_component(self)
        self.register_field(fields.TransactTime, False)
        register_PositionQty_component(self)
        register_PositionAmountData_component(self)
        self.register_field(fields.AdjustmentType, False)
        self.register_field(fields.ThresholdAmount, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AM'] = PositionMaintenanceReport

class RequestForPositions(fix_message.MessageBase):
    _msgtype = 'AN'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.PosReqID, True)
        self.register_field(fields.PosReqType, True)
        self.register_field(fields.MatchStatus, False)
        self.register_field(fields.SubscriptionRequestType, False)
        self.register_field(fields.SettlCurrency, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.ClearingBusinessDate, True)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        register_TrdgSesGrp_component(self)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.ResponseTransportType, False)
        self.register_field(fields.ResponseDestination, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AN'] = RequestForPositions

class RequestForPositionsAck(fix_message.MessageBase):
    _msgtype = 'AO'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.PosMaintRptID, True)
        self.register_field(fields.PosReqID, False)
        self.register_field(fields.TotalNumPosReports, False)
        self.register_field(fields.UnsolicitedIndicator, False)
        self.register_field(fields.PosReqResult, True)
        self.register_field(fields.PosReqStatus, True)
        self.register_field(fields.PosReqType, False)
        self.register_field(fields.MatchStatus, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.SubscriptionRequestType, False)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        self.register_field(fields.SettlCurrency, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.ResponseTransportType, False)
        self.register_field(fields.ResponseDestination, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AO'] = RequestForPositionsAck

class PositionReport(fix_message.MessageBase):
    _msgtype = 'AP'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.PosMaintRptID, True)
        self.register_field(fields.PosReqID, False)
        self.register_field(fields.PosReqType, False)
        self.register_field(fields.SubscriptionRequestType, False)
        self.register_field(fields.TotalNumPosReports, False)
        self.register_field(fields.PosReqResult, False)
        self.register_field(fields.UnsolicitedIndicator, False)
        self.register_field(fields.ClearingBusinessDate, True)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.MessageEventSource, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AcctIDSource, False)
        self.register_field(fields.AccountType, False)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.SettlPrice, False)
        self.register_field(fields.SettlPriceType, False)
        self.register_field(fields.PriorSettlPrice, False)
        self.register_field(fields.MatchStatus, False)
        register_InstrmtLegGrp_component(self)
        register_PosUndInstrmtGrp_component(self)
        register_PositionQty_component(self)
        register_PositionAmountData_component(self)
        self.register_field(fields.RegistStatus, False)
        self.register_field(fields.DeliveryDate, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AP'] = PositionReport

class TradeCaptureReportRequestAck(fix_message.MessageBase):
    _msgtype = 'AQ'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TradeRequestID, True)
        self.register_field(fields.TradeID, False)
        self.register_field(fields.SecondaryTradeID, False)
        self.register_field(fields.FirmTradeID, False)
        self.register_field(fields.SecondaryFirmTradeID, False)
        self.register_field(fields.TradeRequestType, True)
        self.register_field(fields.SubscriptionRequestType, False)
        self.register_field(fields.TotNumTradeReports, False)
        self.register_field(fields.TradeRequestResult, True)
        self.register_field(fields.TradeRequestStatus, True)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.MultiLegReportingType, False)
        self.register_field(fields.ResponseTransportType, False)
        self.register_field(fields.ResponseDestination, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.MessageEventSource, False)


MESSAGE_TYPES['AQ'] = TradeCaptureReportRequestAck

class TradeCaptureReportAck(fix_message.MessageBase):
    _msgtype = 'AR'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TradeReportID, False)
        self.register_field(fields.TradeID, False)
        self.register_field(fields.SecondaryTradeID, False)
        self.register_field(fields.FirmTradeID, False)
        self.register_field(fields.SecondaryFirmTradeID, False)
        self.register_field(fields.TradeReportTransType, False)
        self.register_field(fields.TradeReportType, False)
        self.register_field(fields.TrdType, False)
        self.register_field(fields.TrdSubType, False)
        self.register_field(fields.SecondaryTrdType, False)
        self.register_field(fields.TradeHandlingInstr, False)
        self.register_field(fields.OrigTradeHandlingInstr, False)
        self.register_field(fields.OrigTradeDate, False)
        self.register_field(fields.OrigTradeID, False)
        self.register_field(fields.OrigSecondaryTradeID, False)
        self.register_field(fields.TransferReason, False)
        register_RootParties_component(self)
        self.register_field(fields.ExecType, False)
        self.register_field(fields.TradeReportRefID, False)
        self.register_field(fields.SecondaryTradeReportRefID, False)
        self.register_field(fields.TrdRptStatus, False)
        self.register_field(fields.TradeReportRejectReason, False)
        self.register_field(fields.SecondaryTradeReportID, False)
        self.register_field(fields.SubscriptionRequestType, False)
        self.register_field(fields.TradeLinkID, False)
        self.register_field(fields.TrdMatchID, False)
        self.register_field(fields.ExecID, False)
        self.register_field(fields.SecondaryExecID, False)
        self.register_field(fields.OrdStatus, False)
        self.register_field(fields.ExecRestatementReason, False)
        self.register_field(fields.PreviouslyReported, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.UnderlyingTradingSessionID, False)
        self.register_field(fields.UnderlyingTradingSessionSubID, False)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.LastQty, False)
        self.register_field(fields.LastPx, False)
        register_Instrument_component(self)
        self.register_field(fields.LastParPx, False)
        self.register_field(fields.CalculatedCcyLastQty, False)
        self.register_field(fields.LastSwapPoints, False)
        self.register_field(fields.LastSpotRate, False)
        self.register_field(fields.LastForwardPoints, False)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.AvgPx, False)
        self.register_field(fields.AvgPxIndicator, False)
        self.register_field(fields.MultiLegReportingType, False)
        self.register_field(fields.TradeLegRefID, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.SettlType, False)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.MatchStatus, False)
        self.register_field(fields.MatchType, False)
        self.register_field(fields.CopyMsgIndicator, False)
        self.register_field(fields.PublishTrdIndicator, False)
        self.register_field(fields.ShortSaleReason, False)
        register_TrdInstrmtLegGrp_component(self)
        register_TrdRegTimestamps_component(self)
        self.register_field(fields.ResponseTransportType, False)
        self.register_field(fields.ResponseDestination, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.AsOfIndicator, False)
        self.register_field(fields.ClearingFeeIndicator, False)
        register_PositionAmountData_component(self)
        self.register_field(fields.TierCode, False)
        self.register_field(fields.MessageEventSource, False)
        self.register_field(fields.LastUpdateTime, False)
        self.register_field(fields.RndPx, False)
        register_TrdCapRptAckSideGrp_component(self)
        self.register_field(fields.RptSys, False)
        self.register_field(fields.GrossTradeAmt, False)
        self.register_field(fields.SettlDate, False)


MESSAGE_TYPES['AR'] = TradeCaptureReportAck

class AllocationReport(fix_message.MessageBase):
    _msgtype = 'AS'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.AllocReportID, True)
        self.register_field(fields.AllocID, False)
        self.register_field(fields.AllocTransType, True)
        self.register_field(fields.AllocReportRefID, False)
        self.register_field(fields.AllocCancReplaceReason, False)
        self.register_field(fields.SecondaryAllocID, False)
        self.register_field(fields.AllocReportType, True)
        self.register_field(fields.AllocStatus, True)
        self.register_field(fields.AllocRejCode, False)
        self.register_field(fields.RefAllocID, False)
        self.register_field(fields.AllocIntermedReqType, False)
        self.register_field(fields.AllocLinkID, False)
        self.register_field(fields.AllocLinkType, False)
        self.register_field(fields.BookingRefID, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.TrdType, False)
        self.register_field(fields.TrdSubType, False)
        self.register_field(fields.MultiLegReportingType, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.TradeInputSource, False)
        self.register_field(fields.RndPx, False)
        self.register_field(fields.MessageEventSource, False)
        self.register_field(fields.TradeInputDevice, False)
        self.register_field(fields.AvgPxIndicator, False)
        self.register_field(fields.AllocNoOrdersType, False)
        register_OrdAllocGrp_component(self)
        register_ExecAllocGrp_component(self)
        self.register_field(fields.PreviouslyReported, False)
        self.register_field(fields.ReversalIndicator, False)
        self.register_field(fields.MatchType, False)
        self.register_field(fields.Side, True)
        register_Instrument_component(self)
        register_InstrumentExtension_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.Quantity, True)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.AvgPx, True)
        self.register_field(fields.AvgParPx, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.AvgPxPrecision, False)
        register_Parties_component(self)
        self.register_field(fields.TradeDate, True)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.BookingType, False)
        self.register_field(fields.GrossTradeAmt, False)
        self.register_field(fields.Concession, False)
        self.register_field(fields.TotalTakedown, False)
        self.register_field(fields.NetMoney, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.AutoAcceptIndicator, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.NumDaysInterest, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.TotalAccruedInterestAmt, False)
        self.register_field(fields.InterestAtMaturity, False)
        self.register_field(fields.EndAccruedInterestAmt, False)
        self.register_field(fields.StartCash, False)
        self.register_field(fields.EndCash, False)
        self.register_field(fields.LegalConfirm, False)
        register_Stipulations_component(self)
        register_YieldData_component(self)
        register_PositionAmountData_component(self)
        self.register_field(fields.TotNoAllocs, False)
        self.register_field(fields.LastFragment, False)
        register_AllocGrp_component(self)


MESSAGE_TYPES['AS'] = AllocationReport

class AllocationReportAck(fix_message.MessageBase):
    _msgtype = 'AT'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.AllocReportID, True)
        self.register_field(fields.AllocID, True)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.AvgPxIndicator, False)
        self.register_field(fields.Quantity, False)
        self.register_field(fields.AllocTransType, False)
        register_Parties_component(self)
        self.register_field(fields.SecondaryAllocID, False)
        self.register_field(fields.TradeDate, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.AllocStatus, False)
        self.register_field(fields.AllocRejCode, False)
        self.register_field(fields.AllocReportType, False)
        self.register_field(fields.AllocIntermedReqType, False)
        self.register_field(fields.MatchStatus, False)
        self.register_field(fields.Product, False)
        self.register_field(fields.SecurityType, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        register_AllocAckGrp_component(self)


MESSAGE_TYPES['AT'] = AllocationReportAck

class ConfirmationAck(fix_message.MessageBase):
    _msgtype = 'AU'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ConfirmID, True)
        self.register_field(fields.TradeDate, True)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.AffirmStatus, True)
        self.register_field(fields.ConfirmRejReason, False)
        self.register_field(fields.MatchStatus, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AU'] = ConfirmationAck

class SettlementInstructionRequest(fix_message.MessageBase):
    _msgtype = 'AV'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SettlInstReqID, True)
        self.register_field(fields.TransactTime, True)
        register_Parties_component(self)
        self.register_field(fields.AllocAccount, False)
        self.register_field(fields.AllocAcctIDSource, False)
        self.register_field(fields.Side, False)
        self.register_field(fields.Product, False)
        self.register_field(fields.SecurityType, False)
        self.register_field(fields.CFICode, False)
        self.register_field(fields.SettlCurrency, False)
        self.register_field(fields.EffectiveTime, False)
        self.register_field(fields.ExpireTime, False)
        self.register_field(fields.LastUpdateTime, False)
        self.register_field(fields.StandInstDbType, False)
        self.register_field(fields.StandInstDbName, False)
        self.register_field(fields.StandInstDbID, False)


MESSAGE_TYPES['AV'] = SettlementInstructionRequest

class AssignmentReport(fix_message.MessageBase):
    _msgtype = 'AW'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.AsgnRptID, True)
        self.register_field(fields.TotNumAssignmentReports, False)
        self.register_field(fields.LastRptRequested, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        register_Instrument_component(self)
        self.register_field(fields.Currency, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtGrp_component(self)
        register_PositionQty_component(self)
        register_PositionAmountData_component(self)
        self.register_field(fields.ThresholdAmount, False)
        self.register_field(fields.SettlPrice, False)
        self.register_field(fields.SettlPriceType, False)
        self.register_field(fields.UnderlyingSettlPrice, False)
        self.register_field(fields.PriorSettlPrice, False)
        self.register_field(fields.ExpireDate, False)
        self.register_field(fields.AssignmentMethod, False)
        self.register_field(fields.AssignmentUnit, False)
        self.register_field(fields.OpenInterest, False)
        self.register_field(fields.ExerciseMethod, False)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        self.register_field(fields.ClearingBusinessDate, True)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AW'] = AssignmentReport

class CollateralRequest(fix_message.MessageBase):
    _msgtype = 'AX'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.CollReqID, True)
        self.register_field(fields.CollAsgnReason, True)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.ExpireTime, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.SecondaryClOrdID, False)
        register_ExecCollGrp_component(self)
        register_TrdCollGrp_component(self)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.Quantity, False)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.Currency, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtCollGrp_component(self)
        self.register_field(fields.MarginExcess, False)
        self.register_field(fields.TotalNetValue, False)
        self.register_field(fields.CashOutstanding, False)
        register_TrdRegTimestamps_component(self)
        self.register_field(fields.Side, False)
        register_MiscFeesGrp_component(self)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.EndAccruedInterestAmt, False)
        self.register_field(fields.StartCash, False)
        self.register_field(fields.EndCash, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_Stipulations_component(self)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AX'] = CollateralRequest

class CollateralAssignment(fix_message.MessageBase):
    _msgtype = 'AY'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.CollAsgnID, True)
        self.register_field(fields.CollReqID, False)
        self.register_field(fields.CollAsgnReason, True)
        self.register_field(fields.CollAsgnTransType, True)
        self.register_field(fields.CollAsgnRefID, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.ExpireTime, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.SecondaryClOrdID, False)
        register_ExecCollGrp_component(self)
        register_TrdCollGrp_component(self)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.Quantity, False)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.Currency, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtCollGrp_component(self)
        self.register_field(fields.MarginExcess, False)
        self.register_field(fields.TotalNetValue, False)
        self.register_field(fields.CashOutstanding, False)
        register_TrdRegTimestamps_component(self)
        self.register_field(fields.Side, False)
        register_MiscFeesGrp_component(self)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.EndAccruedInterestAmt, False)
        self.register_field(fields.StartCash, False)
        self.register_field(fields.EndCash, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_Stipulations_component(self)
        register_SettlInstructionsData_component(self)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AY'] = CollateralAssignment

class CollateralResponse(fix_message.MessageBase):
    _msgtype = 'AZ'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.CollRespID, True)
        self.register_field(fields.CollAsgnID, False)
        self.register_field(fields.CollReqID, False)
        self.register_field(fields.CollAsgnReason, False)
        self.register_field(fields.CollAsgnTransType, False)
        self.register_field(fields.CollAsgnRespType, True)
        self.register_field(fields.CollAsgnRejectReason, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.CollApplType, False)
        self.register_field(fields.FinancialStatus, False)
        self.register_field(fields.ClearingBusinessDate, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.SecondaryClOrdID, False)
        register_ExecCollGrp_component(self)
        register_TrdCollGrp_component(self)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.Quantity, False)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.Currency, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtCollGrp_component(self)
        self.register_field(fields.MarginExcess, False)
        self.register_field(fields.TotalNetValue, False)
        self.register_field(fields.CashOutstanding, False)
        register_TrdRegTimestamps_component(self)
        self.register_field(fields.Side, False)
        register_MiscFeesGrp_component(self)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.EndAccruedInterestAmt, False)
        self.register_field(fields.StartCash, False)
        self.register_field(fields.EndCash, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_Stipulations_component(self)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['AZ'] = CollateralResponse

class CollateralReport(fix_message.MessageBase):
    _msgtype = 'BA'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.CollRptID, True)
        self.register_field(fields.CollInquiryID, False)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.CollApplType, False)
        self.register_field(fields.FinancialStatus, False)
        self.register_field(fields.CollStatus, True)
        self.register_field(fields.TotNumReports, False)
        self.register_field(fields.LastRptRequested, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.SecondaryClOrdID, False)
        register_ExecCollGrp_component(self)
        register_TrdCollGrp_component(self)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.Quantity, False)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.Currency, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.MarginExcess, False)
        self.register_field(fields.TotalNetValue, False)
        self.register_field(fields.CashOutstanding, False)
        register_TrdRegTimestamps_component(self)
        self.register_field(fields.Side, False)
        register_MiscFeesGrp_component(self)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.EndAccruedInterestAmt, False)
        self.register_field(fields.StartCash, False)
        self.register_field(fields.EndCash, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_Stipulations_component(self)
        register_SettlInstructionsData_component(self)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['BA'] = CollateralReport

class CollateralInquiry(fix_message.MessageBase):
    _msgtype = 'BB'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.CollInquiryID, False)
        register_CollInqQualGrp_component(self)
        self.register_field(fields.SubscriptionRequestType, False)
        self.register_field(fields.ResponseTransportType, False)
        self.register_field(fields.ResponseDestination, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.SecondaryClOrdID, False)
        register_ExecCollGrp_component(self)
        register_TrdCollGrp_component(self)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.Quantity, False)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.Currency, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.MarginExcess, False)
        self.register_field(fields.TotalNetValue, False)
        self.register_field(fields.CashOutstanding, False)
        register_TrdRegTimestamps_component(self)
        self.register_field(fields.Side, False)
        self.register_field(fields.Price, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.EndAccruedInterestAmt, False)
        self.register_field(fields.StartCash, False)
        self.register_field(fields.EndCash, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        register_Stipulations_component(self)
        register_SettlInstructionsData_component(self)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['BB'] = CollateralInquiry

class NetworkCounterpartySystemStatusRequest(fix_message.MessageBase):
    _msgtype = 'BC'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.NetworkRequestType, True)
        self.register_field(fields.NetworkRequestID, True)
        register_CompIDReqGrp_component(self)


MESSAGE_TYPES['BC'] = NetworkCounterpartySystemStatusRequest

class NetworkCounterpartySystemStatusResponse(fix_message.MessageBase):
    _msgtype = 'BD'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.NetworkStatusResponseType, True)
        self.register_field(fields.NetworkRequestID, False)
        self.register_field(fields.NetworkResponseID, True)
        self.register_field(fields.LastNetworkResponseID, False)
        register_CompIDStatGrp_component(self)


MESSAGE_TYPES['BD'] = NetworkCounterpartySystemStatusResponse

class UserRequest(fix_message.MessageBase):
    _msgtype = 'BE'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.UserRequestID, True)
        self.register_field(fields.UserRequestType, True)
        self.register_field(fields.Username, True)
        self.register_field(fields.Password, False)
        self.register_field(fields.NewPassword, False)
        self.register_field(fields.RawDataLength, False)
        self.register_field(fields.RawData, False)


MESSAGE_TYPES['BE'] = UserRequest

class UserResponse(fix_message.MessageBase):
    _msgtype = 'BF'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.UserRequestID, True)
        self.register_field(fields.Username, True)
        self.register_field(fields.UserStatus, False)
        self.register_field(fields.UserStatusText, False)


MESSAGE_TYPES['BF'] = UserResponse

class CollateralInquiryAck(fix_message.MessageBase):
    _msgtype = 'BG'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.CollInquiryID, True)
        self.register_field(fields.CollInquiryStatus, True)
        self.register_field(fields.CollInquiryResult, False)
        register_CollInqQualGrp_component(self)
        self.register_field(fields.TotNumReports, False)
        register_Parties_component(self)
        self.register_field(fields.Account, False)
        self.register_field(fields.AccountType, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.OrderID, False)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.SecondaryClOrdID, False)
        register_ExecCollGrp_component(self)
        register_TrdCollGrp_component(self)
        register_Instrument_component(self)
        register_FinancingDetails_component(self)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.Quantity, False)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.Currency, False)
        register_InstrmtLegGrp_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.SettlSessSubID, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.ResponseTransportType, False)
        self.register_field(fields.ResponseDestination, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['BG'] = CollateralInquiryAck

class ConfirmationRequest(fix_message.MessageBase):
    _msgtype = 'BH'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ConfirmReqID, True)
        self.register_field(fields.ConfirmType, True)
        register_OrdAllocGrp_component(self)
        self.register_field(fields.AllocID, False)
        self.register_field(fields.SecondaryAllocID, False)
        self.register_field(fields.IndividualAllocID, False)
        self.register_field(fields.TransactTime, True)
        self.register_field(fields.AllocAccount, False)
        self.register_field(fields.AllocAcctIDSource, False)
        self.register_field(fields.AllocAccountType, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['BH'] = ConfirmationRequest

class ContraryIntentionReport(fix_message.MessageBase):
    _msgtype = 'BO'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.ContIntRptID, True)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.LateIndicator, False)
        self.register_field(fields.InputSource, False)
        self.register_field(fields.ClearingBusinessDate, True)
        register_Parties_component(self)
        register_ExpirationQty_component(self)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['BO'] = ContraryIntentionReport

class SecurityDefinitionUpdateReport(fix_message.MessageBase):
    _msgtype = 'BP'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReportID, False)
        self.register_field(fields.SecurityReqID, False)
        self.register_field(fields.SecurityResponseID, False)
        self.register_field(fields.SecurityResponseType, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.SecurityUpdateAction, False)
        self.register_field(fields.CorporateAction, False)
        register_Instrument_component(self)
        register_UnderlyingInstrument_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.ExpirationCycle, False)
        self.register_field(fields.RoundLot, False)
        self.register_field(fields.MinTradeVol, False)


MESSAGE_TYPES['BP'] = SecurityDefinitionUpdateReport

class SecurityListUpdateReport(fix_message.MessageBase):
    _msgtype = 'BK'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.SecurityReportID, False)
        self.register_field(fields.SecurityReqID, False)
        self.register_field(fields.SecurityResponseID, False)
        self.register_field(fields.SecurityRequestResult, False)
        self.register_field(fields.TotNoRelatedSym, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.SecurityUpdateAction, False)
        self.register_field(fields.CorporateAction, False)
        self.register_field(fields.LastFragment, False)
        register_SecLstUpdRelSymGrp_component(self)


MESSAGE_TYPES['BK'] = SecurityListUpdateReport

class AdjustedPositionReport(fix_message.MessageBase):
    _msgtype = 'BL'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.PosMaintRptID, True)
        self.register_field(fields.PosReqType, False)
        self.register_field(fields.ClearingBusinessDate, True)
        self.register_field(fields.SettlSessID, False)
        self.register_field(fields.PosMaintRptRefID, False)
        register_Parties_component(self)
        register_PositionQty_component(self)
        register_Instrument_component(self)
        self.register_field(fields.SettlPrice, False)
        self.register_field(fields.PriorSettlPrice, False)


MESSAGE_TYPES['BL'] = AdjustedPositionReport

class AllocationInstructionAlert(fix_message.MessageBase):
    _msgtype = 'BM'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.AllocID, True)
        self.register_field(fields.AllocTransType, True)
        self.register_field(fields.AllocType, True)
        self.register_field(fields.SecondaryAllocID, False)
        self.register_field(fields.RefAllocID, False)
        self.register_field(fields.AllocCancReplaceReason, False)
        self.register_field(fields.AllocIntermedReqType, False)
        self.register_field(fields.AllocLinkID, False)
        self.register_field(fields.AllocLinkType, False)
        self.register_field(fields.BookingRefID, False)
        self.register_field(fields.AllocNoOrdersType, False)
        register_OrdAllocGrp_component(self)
        register_ExecAllocGrp_component(self)
        self.register_field(fields.PreviouslyReported, False)
        self.register_field(fields.ReversalIndicator, False)
        self.register_field(fields.MatchType, False)
        self.register_field(fields.Side, True)
        register_Instrument_component(self)
        register_InstrumentExtension_component(self)
        register_FinancingDetails_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.Quantity, True)
        self.register_field(fields.QtyType, False)
        self.register_field(fields.LastMkt, False)
        self.register_field(fields.TradeOriginationDate, False)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.AvgPx, False)
        self.register_field(fields.AvgParPx, False)
        register_SpreadOrBenchmarkCurveData_component(self)
        self.register_field(fields.Currency, False)
        self.register_field(fields.AvgPxPrecision, False)
        register_Parties_component(self)
        self.register_field(fields.TradeDate, True)
        self.register_field(fields.TransactTime, False)
        self.register_field(fields.SettlType, False)
        self.register_field(fields.SettlDate, False)
        self.register_field(fields.BookingType, False)
        self.register_field(fields.GrossTradeAmt, False)
        self.register_field(fields.Concession, False)
        self.register_field(fields.TotalTakedown, False)
        self.register_field(fields.NetMoney, False)
        self.register_field(fields.PositionEffect, False)
        self.register_field(fields.AutoAcceptIndicator, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)
        self.register_field(fields.NumDaysInterest, False)
        self.register_field(fields.AccruedInterestRate, False)
        self.register_field(fields.AccruedInterestAmt, False)
        self.register_field(fields.TotalAccruedInterestAmt, False)
        self.register_field(fields.InterestAtMaturity, False)
        self.register_field(fields.EndAccruedInterestAmt, False)
        self.register_field(fields.StartCash, False)
        self.register_field(fields.EndCash, False)
        self.register_field(fields.LegalConfirm, False)
        register_Stipulations_component(self)
        register_YieldData_component(self)
        register_PositionAmountData_component(self)
        self.register_field(fields.TotNoAllocs, False)
        self.register_field(fields.LastFragment, False)
        register_AllocGrp_component(self)
        self.register_field(fields.AvgPxIndicator, False)
        self.register_field(fields.ClearingBusinessDate, False)
        self.register_field(fields.TrdType, False)
        self.register_field(fields.TrdSubType, False)
        self.register_field(fields.CustOrderCapacity, False)
        self.register_field(fields.TradeInputSource, False)
        self.register_field(fields.MultiLegReportingType, False)
        self.register_field(fields.MessageEventSource, False)
        self.register_field(fields.RndPx, False)


MESSAGE_TYPES['BM'] = AllocationInstructionAlert

class ExecutionAcknowledgement(fix_message.MessageBase):
    _msgtype = 'BN'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.OrderID, True)
        self.register_field(fields.SecondaryOrderID, False)
        self.register_field(fields.ClOrdID, False)
        self.register_field(fields.ExecAckStatus, True)
        self.register_field(fields.ExecID, True)
        self.register_field(fields.DKReason, False)
        register_Instrument_component(self)
        register_UndInstrmtGrp_component(self)
        register_InstrmtLegGrp_component(self)
        self.register_field(fields.Side, True)
        register_OrderQtyData_component(self)
        self.register_field(fields.LastQty, False)
        self.register_field(fields.LastPx, False)
        self.register_field(fields.PriceType, False)
        self.register_field(fields.LastParPx, False)
        self.register_field(fields.CumQty, False)
        self.register_field(fields.AvgPx, False)
        self.register_field(fields.Text, False)
        self.register_field(fields.EncodedTextLen, False)
        self.register_field(fields.EncodedText, False)


MESSAGE_TYPES['BN'] = ExecutionAcknowledgement

class TradingSessionList(fix_message.MessageBase):
    _msgtype = 'BJ'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TradSesReqID, False)
        register_TrdSessLstGrp_component(self)


MESSAGE_TYPES['BJ'] = TradingSessionList

class TradingSessionListRequest(fix_message.MessageBase):
    _msgtype = 'BI'
    _msgcat = 'app'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
        self.register_field(fields.TradSesReqID, True)
        self.register_field(fields.TradingSessionID, False)
        self.register_field(fields.TradingSessionSubID, False)
        self.register_field(fields.SecurityExchange, False)
        self.register_field(fields.TradSesMethod, False)
        self.register_field(fields.TradSesMode, False)
        self.register_field(fields.SubscriptionRequestType, True)


MESSAGE_TYPES['BI'] = TradingSessionListRequest
