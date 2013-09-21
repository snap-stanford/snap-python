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
    print item.GetKey(), item.GetDat()

print "---------- 2 ---------"

h = snap.TIntStrH()

h.AddDat(5,"five")
h.AddDat(3,"three")
h.AddDat(9,"nine")
h.AddDat(6,"six")
h.AddDat(1,"one")

print h.Len()

print "h[3] =", h.GetDat(3)

h.AddDat(3,"four")
print "h[3] =", h.GetDat(3)

for item in h:
    print item.GetKey(), item.GetDat()

