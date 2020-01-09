
class int_Type(int):
    def __bytes__(self):
        return str(self).encode()

class float_Type(float):
    def __bytes__(self):
        return str(self).encode()

class char_Type(str):
    def __bytes__(self):
        return str(self).encode()

class time_Type(str):
    def __bytes__(self):
        return str(self).encode()

class date_Type(str):
    def __bytes__(self):
        return str(self).encode()

class data_Type(str):
    def __bytes__(self):
        return str(self).encode()

class MonthYear_Type(char_Type): pass

class DayOfMonth_Type(int_Type): pass

class Length_Type(int_Type): pass

class MultipleValueString_Type(str): pass

class Boolean_Type(str): pass
