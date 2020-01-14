"""
Everything needed to build HTML elements


"""

class Element:
    """
    Basic HTML/XML element
    
    This base class should contain everything to building the HTML tags 
    --implicit terminating tag (<img>, <br>)
    --explicit terminating tags (<html></html>, <body>,</body>)
    --explicit terminating tags with text (<a href="url.com"> text goes here </a>)
    """
    __slots__ = ['element', 'has_attributes', 'attributes', 'tag_text', 'begin_element', 'attribute_string', 'end_element', 'k', 'v'
    ]
    def __init__(self, element, has_attributes, attribdict):
        self.element = element
        self.has_attributes = has_attributes
        self.attributes = attribdict 
        if self.has_attributes == True:       #Does it have attributes?
            self.attribute_string = ''
            for self.k in self.attributes:    #Begin going over the attributes dictionary
                if self.k == 'TAG_TEXT':    #if this exists, we need to determine if it is None or has a string
                    if self.attributes[self.k] == None:
                        pass
                    elif self.attributes[self.k] != None:
                        self.tag_text = self.attributes[self.k]
                elif self.k != 'TAG_TEXT':     #Everything else gets concatinated into 
                    self.v = self.attributes[self.k]
                    self.attribute_string = self.attribute_string + '{}="{}" '.format(self.k, self.v)
            self.begin_element = '<{} {}>'.format(self.element, self.attribute_string)
        elif has_attributes == False:
            self.begin_element = '<{}>'.format(self.element)
        self.end_element = '</{}>'.format(self.element)
        

class SingleTag(Element):
    """
    Single Tag Class 
    """
    def __init__(self, element, has_attributes, attribdict):
        super().__init__(element, has_attributes, attribdict)

    def return_tag(self):
        return '{}'.format(self.begin_element)

 
class FullTag(Element):
    """
    The Anchor Element
    """
    def __init__(self, element, has_attributes, attribdict):
        super().__init__(element, has_attributes, attribdict)

    def return_tag(self):
        return '{}{}'.format(self.begin_element, self.end_element)


class FullTextTag(Element):
    """
    Elements that have text between beginning and ending tags
    """
    def __init__(self, element, has_attributes, attribdict):
        super().__init__(element, has_attributes, attribdict)

    def return_tag(self):
        return '{}{}{}'.format(self.begin_element, self.tag_text, self.end_element)


