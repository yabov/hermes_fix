SEP = '\x01'
EQU = '='
b_SEP = SEP.encode()
b_EQU = EQU.encode()

B_TABLE = bytes.maketrans(b'\x01', b'|')
