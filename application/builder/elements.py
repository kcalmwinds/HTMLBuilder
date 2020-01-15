from dataclasses import dataclass
"""
Everything needed to build HTML elements


"""
@dataclass
class Element:
    """
    Basic HTML element
    """
    element : str
    attributes : list

class ElementBuilder:
    def __init__(self):
        self.attribute_list = []
        self.tag_list = []
        self.element_list = []

    def load_attributes(self):
        '''
        tab delimited - 
        attribute
        list of tags
        description
        '''
        with open('builder\\attributes.txt', 'r' ) as self.x:
            for self.line in self.x:
                self.line = self.line.split('\t')
                self.line[1] = self.line[1].split(',')
                for self.tag in range(len(self.line[1])):
                    self.line[1][self.tag - 1] = self.line[1][self.tag - 1].strip()
                self.attribute_list.append(self.line)



    def load_tags(self):
        with open('builder\\tags.txt', 'r') as self.x:
            for self.line in self.x:
                self.tag_list.append(self.line.split('\t'))

    def build_element(self):
        self.load_tags()
        self.load_attributes()
        for self.tag in self.tag_list:
            self.attrib_list = []
            for self.attrib in self.attribute_list:
                if self.tag[0] in self.attrib[1]:
                    self.attrib_list.append(self.attrib[0])
                elif self.attrib[1][0] == 'GLOBAL':
                    self.attrib_list.append(self.attrib[0])
            self.element_list.append(Element(self.tag[0], self.attrib_list))


    def list_elements(self):
        for self.x in self.element_list:
            print('''
            TAG : {}
            Attributes : {} \t
            '''.format(self.x.element, '    '.join(self.x.attributes)))
        print('DONE!')

    

