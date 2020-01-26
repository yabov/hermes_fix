import logging
from collections import OrderedDict
import io
from collections.abc import MutableSequence

from . import fix_errors
from .utils.constants import SEP, EQU, b_SEP, b_EQU 

from .utils.log import logger

def calc_checksum(buffer):
    checksum =  '%03d' % (sum(c for c in buffer.getbuffer()) % 256) 
    return checksum

class Content:
    def __init__(self, field_type, group_content, required, value = None, is_group= False):
        self.field_type = field_type
        self.group_content = group_content
        self.required = required
        self.value = value
        self.is_group = is_group

class Tags:
    def __init__(self, content_name_map):
        self._content_name_map = content_name_map
    def __getattr__(self, name):
        return self._content_name_map[name].field_type._tag

class MessageBase(object):
    def __init__(self):
        super().__init__()

        self._content_tag_map = OrderedDict()
        self._content_name_map = OrderedDict()
        self.tags = Tags(self._content_name_map)
        self.initialized = True

    def register_field(self, field_type, required):
        c = Content(field_type, None, required)
        self._content_tag_map[field_type._tag] = c
        self._content_name_map[field_type.__name__] = c

    def register_group(self, group_num_field, group_type, required):
        group_content = Content(group_type, None, required, value = group_type(), is_group=True)
        c = Content(group_num_field, group_content, required)
        self._content_tag_map[group_num_field._tag] = c
        self._content_name_map[group_num_field.__name__] = c
        self._content_name_map[group_type.__name__] = group_content

    def build_from_list(self, field_list, stop_if_field_not_defined, ignore_invalid_field_vals = False, in_group = False):
        missed_fields = []
        while field_list:
            field = field_list[0]
            tag, value = field.split(EQU,1)
            content = self._content_tag_map.get(tag)
            if not content:
                if stop_if_field_not_defined: 
                    return missed_fields
                else:
                    missed_fields.append(field_list.pop(0))

                    continue
            
            if content.value is not None:
                #we already set this field which likely means we're in a repeating group and in the next group item
                if in_group:
                    return missed_fields
                else:
                    raise fix_errors.FIXRepeatingFieldError(None, None, tag, "Tag appears more than once", None)

            try:
                setattr(self, content.field_type.__name__, value)
            except fix_errors.FIXEnumValueError as e:
                if ignore_invalid_field_vals:
                    field_list.pop(0)
                    continue
                else:
                    e.tag = tag
                    raise e
            except fix_errors.FIXTagEmptyError as e:
                if ignore_invalid_field_vals:
                    field_list.pop(0)
                    continue
                else:
                    raise
            except ValueError as e:
                if ignore_invalid_field_vals:
                    field_list.pop(0)
                    continue
                else:
                    raise fix_errors.FIXValueError(e, tag)

            field_list.pop(0)
            if content.group_content: #value should be number of repeating groups
                for i in range(content.value):
                    group_item = content.group_content.field_type()
                    #if this is the last group item we should retun to processing the main message.
                    #if this is not the last group item we should discard fields until we get back to one that we know.
                    missed_fields += group_item.build_from_list(field_list, i == content.value -1, ignore_invalid_field_vals, in_group = True)

                    if len(field_list) == 0: #we discarded all the fields because we're expecting more items in group
                        raise fix_errors.FIXIncorrectNumInGroup(None, None, tag, "Incorrect NumInGroup count for repeating group", None)
                    content.group_content.value.append(group_item)

        return missed_fields


    def __bytes__(self):
        return self.serialize().getvalue()

    def serialize(self):
        buffer = io.BytesIO()
   
        tmp_buffer = io.BytesIO()
        tmp_buffer_len = self.Header.serialize_msg(tmp_buffer)
        tmp_buffer_len += self.serialize_msg(tmp_buffer)
        tmp_buffer_len += self.Trailer.serialize_msg(tmp_buffer)

        buffer.write(self.Header.BeginString._tag.encode())
        buffer.write(b_EQU)
        buffer.write(self.Header.BeginString.encode())
        buffer.write(b_SEP)

        self.Header.BodyLength = self.Header.BodyLength or tmp_buffer_len
        buffer.write(self.Header.BodyLength._tag.encode())
        buffer.write(b_EQU)
        buffer.write(str(self.Header.BodyLength).encode())
        buffer.write(b_SEP)

        buffer.write(tmp_buffer.getbuffer())

        checksum = calc_checksum(buffer)

        self.Trailer.CheckSum = self.Trailer.CheckSum or checksum
        buffer.write(self.Trailer.CheckSum._tag.encode())
        buffer.write(b_EQU)
        buffer.write(self.Trailer.CheckSum.encode())
        buffer.write(b_SEP)

        return buffer

    def serialize_msg(self, buffer):
        buffer_len = 0
        for tag, content in self._content_tag_map.items():
            if content.field_type.__name__ in ('BeginString', 'BodyLength', 'CheckSum')  : continue #ignore BeginString
            if content.value is None: continue              
            buffer_len += buffer.write(tag.encode())
            buffer_len += buffer.write(b_EQU)
            buffer_len += buffer.write(bytes(content.value))
            buffer_len += buffer.write(b_SEP)
            if content.group_content:
                for value in content.group_content.value:
                    buffer_len += value.serialize_msg(buffer)
        return buffer_len

    def __getattr__(self, name):
        return self._content_name_map.get(name).value

    def __setattr__(self, name, value):
        if 'initialized' not in self.__dict__ or  name in self.__dict__: 
            return super().__setattr__(name, value)

        content = self._content_name_map.get(name)
        if value == "": 
            raise fix_errors.FIXTagEmptyError("Value is empty", content.field_type._tag)
        if content:
            if isinstance(value, content.field_type):
                content.value = value
            else:
                content.value = content.field_type(value)
        else:
            raise fix_errors.FieldNotFoundError(f"Field {name} does not exist in message")

    def get_first_unset_required_field(self):
        for content in self._content_name_map.values():
            if content.is_group: continue #access group through GroupNo field
            if content.required and content.value is None:
                return content.field_type._tag
            if content.group_content and content.value:
                for group in content.group_content.value:
                    tag = group.get_first_unset_required_field()
                    if tag is not None:
                        return tag
        return None

class FIXGroup(MessageBase, MutableSequence):
    def __init__(self, value):
        self._items = []
        if value:
            for item in value:
                if not isinstance(item, type(self)):
                    raise ValueError(f"Invalid type {type(item)} expecting instance of {type(self)}")
            self._items = value 
        super().__init__()

    def __len__ (self):
        return len(self._items)
        
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]

    def insert(self, index, value):
        self._items.insert(index, value)
