import sys
import xml.etree.ElementTree as ET
import re
import os

FILE_HEADER = """
from ... import fix_message
from . import fields
from . import field_types

BEGINSTRING = '{fix_version}'
MESSAGE_TYPES = {{}}


class Header(fix_message.MessageBase):
    def __init__(self):
        super().__init__()
        register_StandardHeader_component(self)
        
class Trailer(fix_message.MessageBase): 
    def __init__(self):
        super().__init__()
        register_StandardTrailer_component(self)
"""
FIELD_HEADER ="""from . import field_types
from ... import fix_enum_type
"""

FIELD_BASE_TYPE_FORMATTER = """
class {name}({subclass}):
    def __bytes__(self):
        return str(self).encode()
"""

FIELD_TYPE_FORMATTER = """
class {name}({subclass}): pass
"""

FIELD_TYPE_HEADER = """ """

BASE_TYPE_MAP = {'String' : 'str', 'char' : 'str', 'Pattern' : 'str', 'data' : 'str', 'date' : 'str', 'time' : 'str'}

FIELD_CLASS_FORMATTER = """
class {name} (field_types.{type}_Type{enum}) :
    _tag = '{number}'
"""

ENUM_FORMATTER = """    ENUM_{description} = {value}
"""

COMPONENT_HEADER = """def register_{component}_component(self):
"""

COMPONENT_FORMATTER = """{indent}register_{component}_component({instance})
"""

FIELD_FORMATTER = """{indent}self.register_field(fields.{field}, {required})
"""

GROUP_FORMATTER = """{indent}class {group}Group(fix_message.FIXGroup):
{indent}    def __init__(self, value = None):
{indent}        super().__init__(value)
"""

GROUP_FORMATTER_TRAILER = """{indent}self.register_group(fields.{group_no_name}, {group}Group, {required})
"""


MESSAGE_CLASS_FORMATTER  = """
class {name}(fix_message.MessageBase):
    _msgtype = '{msgtype}'
    _msgcat = '{msgcat}'
    def __init__(self):
        self.Header = Header()
        self.Trailer = Trailer()
        super().__init__()
"""


MESSAGE_CLASS_TRAILER = """
MESSAGE_TYPES['{msgtype}'] = {name}
"""

LENGTH_TYPE_FORMATTER = """
class Length_Type(int_Type): pass
"""

MVS_TYPE_FORMATTER = """
class MultipleValueString_Type(str): pass
"""

BOOLEAN_TYPE_FORMATTER ="""
class Boolean_Type(str): pass
"""

TAG_NAME_MAP = {}
FIELD_TYPE_MAP = {}

def camel_to_snake(name):
  name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).upper()

def generate_fix_classes(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    
    
    os.makedirs('message_lib', exist_ok=True)
    
    fix_root = root.findall('fix')
    header_writer =  open(os.path.join('message_lib', '__init__.py'), 'w')

    for fix in fix_root:
        global TAG_NAME_MAP, FIELD_TYPE_MAP
        TAG_NAME_MAP = {}
        FIELD_TYPE_MAP = {}
        fix_version = fix.get('version')
        if fix_version == 'FIXT.1.1': continue 
        
        header_writer.write(f"from . import {fix_version.replace('.','_')}\n")

        path = os.path.join('message_lib', fix_version.replace('.','_'))
        os.makedirs(path, exist_ok=True)

        with open(os.path.join(path, '__init__.py'), 'w') as message_writer:
            message_writer.write('from . import field_types\n')
            message_writer.write('from . import fields\n')
            message_writer.write('from . import fix_messages\n')
            
        with open(os.path.join(path, 'field_types.py'), 'w') as message_writer:
            generate_fields_types(fix, fix_version, message_writer)

        with open(os.path.join(path, 'fields.py'), 'w') as message_writer:
            generate_fields(fix, fix_version, message_writer)
            
        with open(os.path.join(path, "fix_messages.py"), 'w') as message_writer:
            message_writer.write(FILE_HEADER.format(fix_version = fix_version))
            generate_repeating_groups(fix, fix_version, {}, message_writer)
            generate_components(fix, fix_version, message_writer)
            generate_messages(fix, fix_version, message_writer)

    header_writer.close()

def generate_fields_types(root, fix_version, writer):
    writer.write(FIELD_TYPE_HEADER)
    for child in root.find('datatypes'):
        name = child.get('name')
        type = child.get('baseType', name)
        
        FIELD_TYPE_MAP[name] = BASE_TYPE_MAP.get(type)

        if type == name:
            writer.write(
                FIELD_BASE_TYPE_FORMATTER.format(name = name + '_Type', subclass = BASE_TYPE_MAP.get(type, type))
            )
        else:
            writer.write(
                FIELD_TYPE_FORMATTER.format(name = name+ '_Type', subclass = type+ '_Type')
            )
    
    if 'Length' not in FIELD_TYPE_MAP:
        writer.write(LENGTH_TYPE_FORMATTER)
        
    if 'MultipleValueString' not in FIELD_TYPE_MAP:
        writer.write(MVS_TYPE_FORMATTER)
        
    if 'Boolean' not in FIELD_TYPE_MAP:
        writer.write(BOOLEAN_TYPE_FORMATTER)


def generate_fields(root, fix_version, writer):
    writer.write(FIELD_HEADER)
    for child in root.find('fields'):
        name = child.get('name')
        type = child.get('type')
        number = child.get('id')
        

        TAG_NAME_MAP[number] = name

        enums = child.findall('enum')
        enum = ""
        if len(enums) > 0: 
            enum = ', field_types.' + type+'_Type.mro()[-2], metaclass = fix_enum_type.EnumType'
        writer.write(FIELD_CLASS_FORMATTER.format(name = name, type = type, number = number, enum = enum))
        
        for enum in child.findall('enum'):
            description = camel_to_snake( enum.get('symbolicName'))
            str_formatter = ""
            if FIELD_TYPE_MAP.get(child.get('type'), 'str') == 'str':
                str_formatter = "'{value}'" 
            else:
                try:
                    float(enum.get('value'))
                    str_formatter = "{value}"
                except: 
                    continue
                
            writer.write(ENUM_FORMATTER.format(description = description, value = str_formatter.format(value = enum.get('value'))  ))

def find_rec(node, element, level = 0):
    for item in node.iter():
        for group in item.findall(element):
            yield group
    find_rec(item, element, level+1)


def generate_repeating_groups(fix, fix_version, repeating_groups_map, writer ):
    writer.write('##############Begin Repeating Groups###############\n')
    indent = ''
    for child in find_rec(fix, 'repeatingGroup'):
        if child.get('id') in repeating_groups_map: continue
        repeating_groups_map[child.get('id')] = 1
        writer.write(GROUP_FORMATTER.format(indent = indent, group = TAG_NAME_MAP[child.get('id')]))
        generate_body(child,fix_version, writer, indent + ' '*8)
    writer.write('##############End Repeating Groups###############\n')
    

        
def generate_components(root, fix_version, writer, indent = '    '):
    writer.write('##############Begin Componenets###############\n')
    for component in root.find('components'):
        writer.write(COMPONENT_HEADER.format(component = component.get('name')))
        generate_body(component, fix_version, writer, indent)
    writer.write('##############End Componenets###############\n')

def generate_body(component, fix_version, writer, indent = '    '):
    for child in component:
        if child.tag == 'fieldRef':
            writer.write(FIELD_FORMATTER.format(indent = indent, field = child.get('name'), required = 'True' if child.get('required') == '1' else 'False'))
        elif child.tag == 'componentRef' and child.get('name') not in ['StandardHeader', 'StandardTrailer']:
            writer.write(COMPONENT_FORMATTER.format(indent = indent, component = child.get('name'), instance = 'self'))
        elif child.tag == 'repeatingGroup':
            #writer.write(GROUP_FORMATTER.format(indent = indent, group = TAG_NAME_MAP[child.get('id')]))
            #generate_body(child,fix_version, writer, indent + ' '*8)
            writer.write(GROUP_FORMATTER_TRAILER.format(indent = indent, group_no_name = TAG_NAME_MAP[child.get('id')], group = TAG_NAME_MAP[child.get('id')], required = 'True' if child.get('required') == '1' else 'False'))

    writer.write('\n')

def generate_messages(root, fix_version, writer, indent = '    '):
    for msg in root.find('messages'):
        writer.write(MESSAGE_CLASS_FORMATTER.format(name = msg.get('name'), msgtype = msg.get('msgType'), msgcat = 'admin' if msg.get('category') == 'Session' else 'app' ))
        generate_body(msg, fix_version, writer, indent + ' '*4)
        writer.write(MESSAGE_CLASS_TRAILER.format(name = msg.get('name'), msgtype = msg.get('msgType')))



if __name__ == '__main__':
    file_name = sys.argv[1]
    generate_fix_classes(file_name, *sys.argv[2:])