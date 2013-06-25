import os
import sys
import time

sys.path.append("/home/rok/git/rok/snapworld")
import snap

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "Usage: " + sys.argv[0] + " <file>"
        sys.exit(1)

    fname = sys.argv[1]

    FIn = snap.TFIn(snap.TStr(fname))
    Vec = snap.TIntV(FIn)
    print "len", Vec.Len()

    Vec.Sort()

    for i in range(0,Vec.Len()):
        print "Vec", i, Vec.GetVal(i).Val

