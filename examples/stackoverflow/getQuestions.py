
#
#   parse a StackOverflow posts file and print out questions in a TSV format,
#   one question per line.
#   Output fields:
#       post id
#       owner
#       accepted answer
#

import sys
import xml.sax

questionId = "1"

class StackContentHandler(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
 
    def startElement(self, name, attrs):
        '''
        finds posts that are questions, then prints id, owner and accepted answer
        '''
        
        # only 'row' elements are relevant, skip elements that are not rows
        if name != "row":
            return

        # get post type
        ptype = "__none__"
        if attrs.has_key("PostTypeId"):
            ptype = attrs.getValue("PostTypeId")

        # only questions are relevant, skip elements with PostTypeId != questionId
        if ptype != questionId:
            return

        # extract post id, owner, and accepted answer
        id = "__none__"
        if attrs.has_key("Id"):
            id = attrs.getValue("Id")
        owner = "__none__"
        if attrs.has_key("OwnerUserId"):
            owner = attrs.getValue("OwnerUserId")
        accepted = "__none__"
        if attrs.has_key("AcceptedAnswerId"):
            accepted = attrs.getValue("AcceptedAnswerId")
    
        line = []
        line.append(id)
        line.append(owner)
        line.append(accepted)
        print "\t".join(line)
 
if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " <file>"
        sys.exit(1)

    fname = sys.argv[1]
    #print fname

    f = open(fname)
    xml.sax.parse(f, StackContentHandler())

