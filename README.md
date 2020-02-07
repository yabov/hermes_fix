# Hermes FIX

A fully native python FIX engine implementation inspired by QuickFIX.

![Python package](https://github.com/yabov/hermes_fix/workflows/Python%20package/badge.svg)
[![codecov](https://codecov.io/gh/yabov/hermes_fix/branch/master/graph/badge.svg?token=sGgRmhpHud)](https://codecov.io/gh/yabov/hermes_fix)


## Getting Started
see *examples/* folder for additional examples
```python
import hermes_fix as fix
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s-%(asctime)s-%(thread)d-%(filename)s:%(lineno)d - %(message)s')

class FIXApp(fix.Application):
    pass

def main():
    settings = fix.SessionSettings('config.ini')
    client_app = FIXApp()
    store = fix.FileStoreFactory()
    client = fix.SocketConnection(client_app, store, settings)
    task = client.start()

    while not task.done():
        print(task.result())
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
StorageConnectionString=sqlite:///:memory:?check_same_thread=False
SocketAcceptPort=5001
SocketAcceptHost=localhost


[Session_Name2]
ConnectionType=initiator
SenderCompID=CLIENT
TargetCompID=HOST
StorageConnectionString=sqlite:///:memory:?check_same_thread=False
SocketConnectPort=5001
SocketConnectHost=localhost
```

|  Setting Name | Description|  Valid Values | Default|
|---|---|---|---|
|SenderCompID| Your identifier when sending messages| String| |
|TargetCompID| Their identifier when sending messages| String| |
|ConnectionType| Identifies the session as acceptor or initiator| acceptor <br> initiator| |
|StorageConnectionString| sqlalchemy style connect string to database| ex: sqlite:///:memory:?check_same_thread=False <br> for sqlite must use check_same_thread=False| |
|LogonTime| Time at which session logs on and performs a sequence reset| 'Monday 08:00:00am' for weekly <br> '6:00:00' for daily <br>|
|LogoutTime| Time at which session sends a logoff| same format as LogonTime, can be before LogonTime for inverted times |
|SessionTimeZone| Standard Time Zone format | ex: America/New_York | UTC |
|ConnectionStartTime| Time when initiator opens the socket to the server||
|ConnectionStartTime| Time when initiator closes connection to the server, will not close before LogoutTime||
|SocketAcceptHost|For acceptor the machine name to listen for connections| ip address<br>machine name| localhost|
|SocketAcceptPort|Port to listen for connections| integer||
|SocketConnectHost|For initiator the machine to connect to| ip address<br>machine name| |
|SocketConnectPort|Port to connect to| integer||
|TimeFormat| Syntax for format sent over FIX| '%Y%m%d-%H:%M:%S.%f'<br><br>'%Y%m%d-%H:%M:%S' | '%Y%m%d-%H:%M:%S.%f'|
|HeartBeatInt|  Initiator's Heartbeat Interval in seconds |  Positive float | 30 |
|AcceptUnknownFields| Accept and ignore FIX fields not defined in dictionary| True<br> False| False|
|SendingTimeTolerance | Grace Period in checking Sending Time<52> in minutes.<br>Reject if outside sending window. <br> Setting SendingTimeTolerance=0 will never reject| Positive float | 2|
|ValidateCompIDs | Checks for Target and Sender CompIDs to be defined correct on each message| True<br>False | True|
|ValidateRequiredFields| Send Reject if a Required field is not sent| True<br>False  || True
|MessageReadTimeout |  Timeout in seconds to wait for a complete FIX message to be sent from first byte received | Positive float| 2 |
|IgnoreChecksum| skip checksum calculation |  True<br>False| False |
|IgnoreInvalidFieldValues| Drop fields that are incorrect type or invalid Enum or tag=\<SOH\>|  True<br>False| False |
||
|SSL Options|
|SSLProtocol| SSL Protocol version as specified in https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS | ssl.PROTOCOL_* | |
|SSLOptions | SSL Options as specified by https://docs.python.org/3/library/ssl.html#ssl.OP_ALL <br> Options are comma separated and bit-or'd together| ssl.OP_* | |
||||
|SSLCertFile| Server side - Certificate path https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain |||
|SSLCertKeyFile| Optional Certificate key file path|||
|SSLCertPassword| Optional Password for certificate key file|||
||||
|SSLCAFile| Client side - Certificate path https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations |||
|SSLCAPath| Optional path to multiple ca certificates|||
|SSLCAData| Optional ascii encode certificate|||
||||
|SSLCheckHostName| https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname |True <br> False| True|
|SSLVerifyMode| https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode | | |
|SSLCiphers| https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ciphers | | |

### What's missing
* dynamic message generation from config file
