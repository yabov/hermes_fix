class EnumType(type):       
    def __new__(metacls, cls, bases, classdict):
        cls =  super().__new__(metacls, cls, bases, classdict)
        cls.base_type = bases[0]
        cls._member_map_ = {}
        for key, value in classdict.items():
            if key.startswith('ENUM'):
                cls._member_map_[value] = key
        return cls
        
    def __contains__(cls, member):
        return  member in cls._member_map_

    def __call__(cls, value):
        value = cls.base_type(value)
        if value not in cls._member_map_:
            raise ValueError("%r is not a valid %s" % (value, cls.__qualname__))
        return cls.__new__(cls, value)