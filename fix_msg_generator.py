import sys
import xml.etree.ElementTree as ET

import fields
import inspect

FILE_HEADER = """import fields
import fix_message

BEGINSTRING = '{begin_string}'
MESSAGE_TYPES = {{}}
"""

FIELD_CLASS_FORMATTER = """
class {name} (fields.{type}) :
    _tag = '{number}'
"""

ENUM_FORMATTER = """    ENUM_{description} = {value}
"""

HEADER_CLASS_FORMATTER  = """
class Header(fix_message.MessageBase):
    def __init__(self):
        super().__init__()
"""

TRAILER_CLASS_FORMATTER  = """
class Trailer(fix_message.MessageBase):
    def __init__(self):
        super().__init__()
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

FIELD_FORMATTER = """{indent}self.register_field({field}, {required})
"""

GROUP_FORMATTER = """
{indent}class {group}Group(fix_message.FIXGroup):
{indent}    def __init__(self):
"""

GROUP_FORMATTER_TRAILER = """
{indent}self.register_group({group}, {full_name}Group, {required})
"""

FIELD_CLASSES = { name.upper(): obj for name, obj in inspect.getmembers(fields) if inspect.isclass(obj)}        
COMPONENTS = {}

def generate_fix_classes(file_name, begin_string):
    tree = ET.parse(file_name)
    root = tree.getroot()
    major, minor, sp = get_fix_version(root)
    with open("fix_messages_%s_%s_%s.py"%(major, minor, sp), 'w') as message_writer:
        message_writer.write(FILE_HEADER.format(begin_string = begin_string))
        build_components(root)
        generate_fields(root, message_writer)
        generate_header(root, message_writer)
        generate_messages(root, message_writer)
        generate_trailer(root, message_writer)

def build_components(root):
    for component in root.find('components'):
        COMPONENTS[component.get('name')] = component

"""<fix type='FIX' major='4' minor='4' servicepack='0'>"""
def get_fix_version(root):
    #fix = root.get('FIX')
    major = root.get('major')
    minor = root.get('minor')
    sp = root.get('servicepack')

    return (major, minor, sp)

def get_field_type(type_name):
    return FIELD_CLASSES[type_name]

def generate_fields(root, writer):
    for child in root.find('fields'):
        name = child.get('name')
        type = get_field_type(child.get('type')) 
        number = child.get('number')

        writer.write(
            FIELD_CLASS_FORMATTER.format(name = name, type = type.__name__, number = number)
        )
        """<value enum='1' description='NOT_HELD' />"""
        for enum in child.findall('value'):
            str_formatter = "'{value}'" if issubclass(type, str) or issubclass(type, bytes) else "{value}"
            writer.write(ENUM_FORMATTER.format(description = enum.get('description'), value = str_formatter.format(value = enum.get('enum'))  ))

def generate_recursive(root, writer, indent = ' '*8, parents = ""):
    delay_group_write = []
    for child in root:
        if child.tag == 'field':
            generate_field(child, writer, indent)
        elif child.tag == 'group':
            generate_group(child, writer, indent, parents)
            delay_group_write += [child]
        elif child.tag == 'component':
            generate_recursive(COMPONENTS[child.get('name')], writer, indent, "%s.%s"%(parents, child.get('name')))

    for child in delay_group_write:
        generate_group_delayed(child, writer, indent[:-4], parents)

def generate_group(group_root, writer, indent = ' '*4, parents= ""):
    name = group_root.get('name')
    required = group_root.get('required')
    #generate_field(group_root, writer, indent)
    full_name = "%s.%s"%(parents, name)
    writer.write(GROUP_FORMATTER_TRAILER.format(group = name, full_name = full_name, indent = indent, required = required == 'Y'))

def generate_group_delayed(group_root, writer, indent = ' '*4, parents = ""):
    name = group_root.get('name')
    required = group_root.get('required')
    #generate_field(group_root, writer, indent)
    writer.write(GROUP_FORMATTER.format(group = name, indent = indent))
    generate_recursive(group_root, writer,indent + ' '*8, "%s.%sGroup"%(parents, name))

def generate_field(field_root, writer, indent = ' '*4):
    name = field_root.get('name')
    required = field_root.get('required')
    writer.write(FIELD_FORMATTER.format(field = name, indent = indent, required = required == 'Y'))

"""<field name='BeginString' required='Y' />"""
def generate_header(root, writer):
    writer.write(HEADER_CLASS_FORMATTER)
    generate_recursive(root.find('header'), writer, parents = "Header")

def generate_trailer(root, writer):
    writer.write(TRAILER_CLASS_FORMATTER)
    generate_recursive(root.find('trailer'), writer, parents = "Trailer")

def generate_messages(root, writer):
    for child in root.find('messages'):
        writer.write(MESSAGE_CLASS_FORMATTER.format(name = child.get('name'), msgtype = child.get('msgtype'), msgcat = child.get('msgcat')))
        generate_recursive(child, writer, parents = child.get('name'))
        writer.write(MESSAGE_CLASS_TRAILER.format(name = child.get('name'), msgtype = child.get('msgtype')))

        

if __name__ == '__main__':
    file_name = sys.argv[1]
    generate_fix_classes(file_name, 'FIX.4.4')