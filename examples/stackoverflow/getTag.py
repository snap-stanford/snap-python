
#
#   parse a StackOverflow posts file and print out answers in a TSV format,
#   one answer per line.
#   Output fields:
#       post id
#       owner
#

import sys
import xml.sax

questionId = "1"

class StackContentHandler(xml.sax.ContentHandler):

    def __init__(self, tag):
        xml.sax.ContentHandler.__init__(self)
        self.tag = "<" + tag + ">"
 
    def startElement(self, name, attrs):
        '''
        finds posts that are answers, then prints id and owner
        '''
        
        # only 'row' elements are relevant, skip elements that are not rows
        if name != "row":
            return

        # get post type
        ptype = "__none__"
        if attrs.has_key("PostTypeId"):
            ptype = attrs.getValue("PostTypeId")

        # only answers are relevant, skip elements with PostTypeId != answerId
        if ptype != questionId:
            return

        # extract post id and tags
        id = "__none__"
        if attrs.has_key("Id"):
            id = attrs.getValue("Id")
        tags = "__none__"
        if attrs.has_key("Tags"):
            tags = attrs.getValue("Tags")

        #print "__tags__", tags

        # skip posts without a matching tag
        if not self.tag in tags:
            return
    
        line = []
        line.append(id)
        print "\t".join(line)
 
if __name__ == '__main__':

    if len(sys.argv) < 3:
        print "Usage: " + sys.argv[0] + " <file> <tag>"
        sys.exit(1)

    fname = sys.argv[1]
    tag = sys.argv[2]
    #print fname

    f = open(fname)
    xml.sax.parse(f, StackContentHandler(tag))

