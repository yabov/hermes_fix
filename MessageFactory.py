import xml.etree.ElementTree as ET

SEP = b'\x01'
EQU = b'='

class MessageFactory:
    def __init__(self): pass

    async def initialize(self, reader, settings_map):
        beginString = await reader.readuntil(SEP)
        bodyLength = await reader.readuntil(SEP)
        msgType = await reader.readuntil(SEP)
        senderCompID = await reader.readuntil(SEP)
        targetCompID = await reader.readuntil(SEP)

        beginStringTag, beginStringValue = beginString[:-len(SEP)].split(EQU, 1)
        bodyLengthTag, bodyLengthValue = bodyLength[:-len(SEP)].split(EQU, 1)
        senderCompIDTag, senderCompIDValue = senderCompID[:-len(SEP)].split(EQU, 1)
        targetCompIDTag, targetCompIDValue = targetCompID[:-len(SEP)].split(EQU, 1)

        data = await reader.readexactly(int(bodyLengthValue) - len(msgType) - len(senderCompID) - len(targetCompID))

        #logger.info("Received [%s]", message)

        checkSum = await reader.readuntil(SEP)
        checkSumTag, checkSumValue = checkSum[:-len(SEP)].split(EQU)

        #TODO check:  (checkSumValue == calc_checkSum(beginString + bodyLength + msgType + data))

        dictionary_path = settings_map[(senderCompIDValue, targetCompIDValue)]['DataDictionary']
        tree = ET.parse(dictionary_path)
        root = tree.getroot()
        print (root)

        

