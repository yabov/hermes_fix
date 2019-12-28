class FIXEngineError(Exception): pass
class FIXEngineWarning(Exception) : pass


class FIXDropMessageError(FIXEngineError) : pass
class FIXRejectError(FIXDropMessageError) : pass

class FIXLogoutError(FIXEngineError) : pass
class FIXHardKillError(FIXEngineError) : pass

class FieldNotFoundError(FIXEngineError) : pass

class RequiredTagMissingError(FIXRejectError) : pass

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