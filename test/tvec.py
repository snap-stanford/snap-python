from snap import *

v = TIntV.GetV(TInt(11),TInt(12),TInt(13),TInt(14),TInt(15))

print "--------- 1"
for item in v:
    print item.Val

print "--------- 2"
for i in range(0, v.Len()):
    print v[i].Val

print "--------- 3"
for i in range(0, v.Len()):
    print v.GetVal(i).Val

