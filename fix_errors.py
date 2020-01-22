class FIXEngineError(Exception): pass
class FIXEngineWarning(Exception) : pass

class FIXValueError(FIXEngineError): 
    def __init__(self, Text, tag = None):
        super().__init__(Text)
        self.tag = tag

class FIXEnumValueError(FIXEngineError): 
    def __init__(self, Text, tag = None):
        super().__init__(Text)
        self.tag = tag
class FIXTagEmptyError(FIXEngineError) : 
    def __init__(self, Text, tag):
        super().__init__(Text)
        self.tag = tag

class FIXDropMessageError(FIXEngineError) : pass
class FIXRejectError(FIXEngineError) : 
    def __init__(self, RefSeqNum, RefMsgType, RefTagID, Text, SessionRejectReason):
        super().__init__(Text)
        self.RefSeqNum = RefSeqNum
        self.RefMsgType = RefMsgType
        self.RefTagID = RefTagID
        self.Text = Text
        self.SessionRejectReason = SessionRejectReason

class FIXRejectAndLogoutError(FIXEngineError):
    def __init__(self, RefSeqNum, RefMsgType, RefTagID, Text, SessionRejectReason, wait_interval = 2, send_test_msg = False):
        super().__init__(Text)
        self.RefSeqNum = RefSeqNum
        self.RefMsgType = RefMsgType
        self.RefTagID = RefTagID
        self.Text = Text
        self.SessionRejectReason = SessionRejectReason
        self.wait_interval = wait_interval
        self.send_test_msg = send_test_msg

class FIXLogoutError(FIXEngineError) :
    def __init__(self, Text, wait_interval = 2, send_test_msg = False):
        super().__init__(Text)
        self.Text = Text
        self.wait_interval = wait_interval
        self.send_test_msg = send_test_msg

class FIXHardKillError(FIXEngineError) : pass

class FieldNotFoundError(FIXEngineError) : pass

class RequiredTagMissingError(FIXRejectError) : pass
class FIXBadCompIDError(FIXRejectAndLogoutError) : pass

class FIXGarbledMessageError(FIXDropMessageError) : pass
class FIXCheckSumError(FIXGarbledMessageError): pass

class FIXSequenceTooLowError(FIXLogoutError) : pass
class FIXResetSequenceToLowerError(FIXRejectError) : pass

class FIXEngineResendRequest(FIXDropMessageError) : pass
class FIXDupeMessageRecv(FIXDropMessageError) : pass
class FIXSendTimeAccuracyError(FIXRejectAndLogoutError) : pass

class FIXInvalidMessageError(FIXLogoutError) : pass
class FIXInvalidFirstMessage(FIXHardKillError) : pass


class FIXSessionExistsError(FIXHardKillError): pass
class FIXSessionNotFound(FIXHardKillError):pass

class FIXSessionLogoutTimeoutWarning(FIXEngineWarning) : pass

class FIXInvalidMessageTypeError(FIXRejectError) : pass
class FIXInvalidMessageFieldError(FIXRejectError) : pass
class FIXUnsupportedMessageTypeError(FIXRejectError) : pass
class FIXIncorrectNumInGroup(FIXRejectError) : pass 

class FIXRepeatingFieldError(FIXRejectError) : pass 



