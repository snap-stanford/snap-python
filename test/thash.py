import random
import os
import sys
import time

import snap

print "---------- 1 ---------"

Hash = snap.TIntIntH()

Hash.AddDat(5,4)
Hash.AddDat(1,2)
Hash.AddDat(4,8)

Hash[17] = 15
Hash[11] = 14
Hash[15] = 18
#Hash.AddDat(TInt(3),TInt(5))
#Hash.AddDat(TInt(4),TInt(6))
#Hash.AddDat(TInt(1),TInt(8))
#Hash.AddDat(TInt(6),TInt(2))

print "len", Hash.Len()

Iter = Hash.BegI()
Key = Iter.GetKey()
Value = Iter.GetDat()
print "iter", Key, Value

print "Iter < Hash.EndI", Iter < Hash.EndI()
#while Iter < Hash.EndI():
while not Iter.IsEnd():
    Key = Iter.GetKey()
    Value = Iter.GetDat()
    print Key, Value

    Iter.Next()

for item in Hash:
    print item, Hash[item]

print "---------- 2 ---------"

h = snap.TIntStrH()

h[5] = "five"
h[3] = "thre"
h[9] = "nine"
h[6] = "six"
h[1] = "one"

print h.Len()

print "h[3] =", h[3]

h[3] = "three"

print "h[3] =", h[3]

for item in h:
    print item, h[item]

