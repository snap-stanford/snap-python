import random
import os
import sys
import time

from snap import *

Hash = TIntH()

Hash.AddDat(5,4)
Hash.AddDat(1,2)
Hash.AddDat(4,8)
#Hash.AddDat(TInt(3),TInt(5))
#Hash.AddDat(TInt(4),TInt(6))
#Hash.AddDat(TInt(1),TInt(8))
#Hash.AddDat(TInt(6),TInt(2))

print "len", Hash.Len()

Iter = Hash.BegI()
Key = Iter.GetKey().Val
Value = Iter.GetDat().Val
print "iter", Key, Value

print "Iter < Hash.EndI", Iter < Hash.EndI()
#while Iter < Hash.EndI():
while not Iter.IsEnd():
    Key = Iter.GetKey().Val
    Value = Iter.GetDat().Val
    print Key, Value

    Iter.Next()

for item in Hash:
    print item.GetKey().Val, item.GetDat().Val

