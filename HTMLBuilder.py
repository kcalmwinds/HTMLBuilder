import builder.elements

def main():
    testarguments = {'src' : 'localhost', 'alt' : 'sometext', 'bob' : 'charlie'}
    picture = builder.elements.Image(testarguments)
    print(picture.return_tag())
    testarguments = { 'href' :  'http://omgwtf.com'}
    anchor = builder.elements.Anchor('a brisk walk', testarguments)
    print(anchor.return_tag())

if __name__ == '__main__':
    main()
