# Hermes FIX

A fully native python FIX engine implementation inspired by QuickFIX.

## Getting Started
see *samples/* folder for additional examples
```python
import hermes_fix as fix

class FIXApp(fix.Application): pass

settings  = fix.SessionSettings('config.ini')
client_app = FIXApp()
store = fix.FileStoreFactory()
client = fix.SocketConnection(client_app, store, settings)
client.start()
```

### Configuration Settings
Standard Python .ini file syntax example:

```ini
[DEFAULT]
BeginString=FIX.4.2
ConnectionStartTime=08:00:00
ConnectionEndTime=07:55:00
LogonTime=08:01:00
LogoutTime=07:54:00

[MY_HOST]
ConnectionType=acceptor
SenderCompID=HOST
TargetCompID=CLIENT
FileStorePath=store


[Session_Name2]
ConnectionType=initiator
SenderCompID=CLIENT
TargetCompID=HOST
FileStorePath=store
```

|  Setting Name | Description  |  Valid Values | Default|
|---|---|---|---|
|SenderCompID| Your identifier when sending messages| String| |
|TargetCompID| Their identifier when sending messages| String| |
|ConnectionType| Identifies the session as acceptor or initiator| acceptor <br> initiator| |
|SocketAcceptHost|For acceptor the machine name to listen for connections| ip address<br>machine name| localhost|
|SocketAcceptPort|Port to listen for connections| integer||
|SocketConnectHost|For initiator the machine to connect to| ip address<br>machine name| |
|SocketConnectPort|Port to connect to| integer||
| TimeFormat  | Syntax for format sent over FIX  | '%Y%m%d-%H:%M:%S.%f'<br><br>'%Y%m%d-%H:%M:%S' | '%Y%m%d-%H:%M:%S.%f'|
| HeartBeatInt  |  Initiator's Heartbeat Interval in seconds |  Positive float | 30 |
| AcceptUnknownFields  | Accept and ignore FIX fields not defined in dictionary  | True<br> False  | False|
|  SendingTimeTolerance | Grace Period in checking Sending Time<52> in minutes. <br>Reject if outside sending window. Setting SendingTimeTolerance=0 will never reject| Positive float | 2|
|  ValidateCompIDs | Checks for Target and Sender CompIDs to be defined correct on each message  | True<br>False   | True|
| ValidateRequiredFields  | Send Reject if a Required field is not sent  | True<br>False    || True
|  MessageReadTimeout |  Timeout in seconds to wait for a complete FIX message to be sent from first byte received | Positive float  | 2 |
| IgnoreChecksum  | skip checksum calculation |  True<br>False  | False |
| IgnoreInvalidFieldValues  | Drop fields that are incorrect type or invalid Enum or tag=\<SOH\>|  True<br>False  | False |




### Whats left
* connection start and end time for initiator