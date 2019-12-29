import fields
import fix_message

class BeginString (fields.String) :
    _tag = '8'

class BodyLength (fields.Length) :
    _tag = '9'

class MsgType (fields.String) :
    _tag = '35'

class CheckSum (fields.String) :
    _tag = '10'


