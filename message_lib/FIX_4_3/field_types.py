
class int_Type(int):
    def __bytes__(self):
        return str(self).encode()

class Length_Type(int_Type): pass

class NumInGroup_Type(int_Type): pass

class TagNum_Type(int_Type): pass

class SeqNum_Type(int_Type): pass

class float_Type(float):
    def __bytes__(self):
        return str(self).encode()

class Qty_Type(float_Type): pass

class Price_Type(float_Type): pass

class PriceOffset_Type(float_Type): pass

class Amt_Type(float_Type): pass

class Percentage_Type(float_Type): pass

class char_Type(str):
    def __bytes__(self):
        return str(self).encode()

class String_Type(str):
    def __bytes__(self):
        return str(self).encode()

class MultipleStringValue_Type(String_Type): pass

class Country_Type(String_Type): pass

class Currency_Type(String_Type): pass

class Exchange_Type(String_Type): pass

class MonthYear_Type(String_Type): pass

class UTCTimestamp_Type(String_Type): pass

class UTCTimeOnly_Type(String_Type): pass

class LocalMktDate_Type(String_Type): pass

class UTCDate_Type(String_Type): pass

class data_Type(String_Type): pass

class MultipleValueString_Type(str): pass

class Boolean_Type(str): pass
