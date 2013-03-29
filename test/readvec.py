import os
import sys
import time

sys.path.append("/home/rok/git/rok/snapworld")
import snap as Snap

fname = "/home/rok/git/rok/snapworld/work-nbr/swout-GetNbr-0-GetDist-0.txt"

FIn = Snap.TFIn(Snap.TStr(fname))
Vec = Snap.TIntV(FIn)
print "len", Vec.Len()

for i in range(0,Vec.Len()):
    print "Vec", i, Vec.GetVal(i).Val

