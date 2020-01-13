"""Everything needed to build HTML elements"""

class Element:
    """ Basic HTML/XML element"""
    def __init__(self, element, has_attributes, attribdict):
        self.element = element
        self.has_attributes = has_attributes
        self.attributes = attribdict
        if self.has_attributes == True:
            self.attribute_string = ''
            for self.k in self.attributes:
                self.v = self.attributes[self.k]
                self.attribute_string = self.attribute_string + '{}="{}" '.format(self.k, self.v)
            self.begin_element = '<{} {}>'.format(self.element, self.attribute_string)
        elif has_attributes == False:
            self.begin_element = '<{}>'.format(self.element)
        self.end_element = '</{}>'.format(self.element)

class Image:
    """ Image Element """
    def __init__(self, attribdict):
        self.attributes = attribdict
        self.element = 'img'
        self.has_attributes = True
        self.image = Element(self.element, self.has_attributes, self.attributes)

    def return_tag(self):
        return self.image.begin_element

class Anchor:
    """The Anchor Element"""
    def __init__(self, link_element, attribdict):
        self.link_element = link_element
        self.attributes = attribdict
        self.element = 'a'
        self.has_attributes = True
        self.anchor = Element(self.element, self.has_attributes, self.attributes)

    def return_tag(self):
        return self.anchor.begin_element + self.link_element + self.anchor.end_element