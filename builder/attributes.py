from dataclasses import dataclass

@dataclass
class HTMLAttributes:
    """
    Base Class for HTML Attributes
    Data Class
    name = str
    tags = list
    description = str

    global attributes = ALL
    Depricated attributes = None
    """
    __slots__ = ['name', 'tags', 'description']
    name : str
    tags : list
    description : str

class blank(HTMLAttributes):
    super().__init__('blank', ['tags that use this attribute'], 'description here')


class Accept(HTMLAttributes):
    super().__init__('accept', ['input'], 'Specifies the types of files that the server accepts (only for type="file")')


class AcceptCharset(HTMLAttributes):
    super().__init__('accept-charset', ['form'], 'Specifies the character encodings that are to be used for the form submission')


class Accesskey(HTMLAttributes):
    super().__init__('accesskey', ['ALL'], 'Specifies a shortcut key to activate/focus an element')


class blank(HTMLAttributes):
    super().__init__('blank', ['tags that use this attribute'], 'description here')





