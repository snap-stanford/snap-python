#
#   generate dispatch tables for instantiated polymorphic SNAP templates
#       input file format: <func> <type>
#

import os
import sys

f_header = "def %s(gtype, *args):" 
f_body   = "    if gtype == %-8s: return %s_%s(*args)"
f_end    = "    return None" 

def gendispatch(item, df):
    flist = df[item]

    print f_header % (item)
    for ftype in flist:
        print f_body % (ftype, item, ftype)
    print f_end

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " <file>"
        sys.exit(1)

    fname = sys.argv[1]

    df = {}

    f = open(fname, "r")
    for nline in f:
        line = nline.split("\n")[0]
        w = line.split("\t")

        # skip empty lines, comments, malformed lines
        if len(w) < 2  or  len(w[0]) <= 0  or  w[0] == "#":
            continue

        ftype  = w[0]
        func   = w[1]

        if not df.has_key(func):
            df[func] = []

        df[func].append(ftype)

    f.close()

    for item in df:
        #print item, df[item]
        gendispatch(item,df)

