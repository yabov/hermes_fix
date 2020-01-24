# Hermes FIX

A fully native python FIX engine implementation

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
Standard Python .ini file syntax

|  Setting Name | Description  |  Valid Values | Default|
|---|---|---|---|
| TimeFormat  | Syntax for format sent over FIX  | '%Y%m%d-%H:%M:%S.%f'<br>'%Y%m%d-%H:%M:%S' | '%Y%m%d-%H:%M:%S.%f'|
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