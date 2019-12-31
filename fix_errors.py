class FIXEngineError(Exception): pass
class FIXEngineWarning(Exception) : pass


class FIXDropMessageError(FIXEngineError) : pass
class FIXRejectError(FIXEngineError) : 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.RefSeqNum = None
        self.RefMsgType = None
        self.RefTagID = None
        self.Text = None
        self.SessionRejectReason = None

class FIXLogoutError(FIXEngineError) : pass
class FIXHardKillError(FIXEngineError) : pass

class FieldNotFoundError(FIXEngineError) : pass

class RequiredTagMissingError(FIXRejectError) : pass
class FIXBadCompIDError(FIXLogoutError) : pass

class FIXGarbledMessageError(FIXDropMessageError) : pass
class FIXCheckSumError(FIXGarbledMessageError): pass

class FIXSequenceTooLowError(FIXLogoutError) : pass
class FIXEngineResendRequest(FIXDropMessageError) : pass
class FIXDupeMessageRecv(FIXDropMessageError) : pass
class FIXSendTimeAccuracyError(FIXLogoutError) : pass

class FIXInvalidMessageError(FIXLogoutError) : pass
class FIXInvalidFirstMessage(FIXHardKillError) : pass


class FIXSessionExistsError(FIXHardKillError): pass
class FIXSessionNotFound(FIXHardKillError):pass

class FIXSessionLogoutTimeoutWarning(FIXEngineWarning) : pass

class FIXInvalidMessageTypeError(FIXRejectError) : pass
