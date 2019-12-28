class int (int):
    def __bytes__(self):
        return ("%s"%self).encode()
class String (str): 
    def __bytes__(self):
        return ("%s"%self).encode()
class float (float): 
    def __bytes__(self):
        return ("%s"%self).encode()

class Length (int): pass
class TagNum (int): pass
class SeqNum (int): pass
class NumInGroup (int): pass
class DayOfMonth (int): pass
class Qty (float): pass
class Price (float): pass
class PriceOffset (float): pass
class Amt (float): pass
class Percentage (float): pass
class char (String): pass
class Boolean (String): pass
class MultipleCharValue (String): pass
class MultipleStringValue (String): pass
class MultipleValueString (String): pass #not sure which one is correct
class Country (String): pass
class Currency (String): pass
class Exchange (String): pass
class MonthYear (String): pass
class UTCTimestamp (String): pass
class UTCTimeOnly (String): pass
class UTCDateOnly (String): pass
class UTCDate(String): pass
class LocalMktDate (String): pass
class TZTimeOnly (String): pass
class TZTimestamp (String): pass
class data (bytes): pass
class Pattern (String): pass
class Tenor (String): pass
class Reserved100Plus (String): pass
class Reserved1000Plus (String): pass
class Reserved4000Plus (String): pass