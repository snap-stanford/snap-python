import os
import sys
import time

sys.path.append("/home/rok/git/rok/snapworld")
import snap as Snap

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " <file>")
        sys.exit(1)

    fname = sys.argv[1]

    FIn = Snap.TFIn(Snap.TStr(fname))
    Vec = Snap.TIntV(FIn)
    print("len", Vec.Len())

    Vec.Sort()

    for i in range(0,Vec.Len()):
        print("Vec", i, Vec.GetVal(i).Val)

