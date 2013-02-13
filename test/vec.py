import sys
import time

sys.path.append("../swig")
import snap as Snap

numnodes = 100
numtask = 50

#print "dir(Snap.TIntV)", dir(Snap.TIntV)
Vec1 = Snap.TIntV(numnodes)
#print "dir(Vec1)", dir(Vec1)
print "Len Vec1", Vec1.Len()

#print "dir(Snap.TIntIntVV)", dir(Snap.TIntIntVV)
Vec2 = Snap.TIntIntVV(numtask)
#print "dir(Vec2)", dir(Vec2)
print "Len Vec2", Vec2.Len()

print "Vec1", type(Vec1)

Snap.GetDegrees(Vec1, 10.0, 1.5)

for i in range(0,Vec1.Len()):
    print "Vec1", i, Vec1.GetVal(i).Val

Snap.AssignRndTask(Vec1, Vec2)

for i in range(0,Vec2.Len()):
    Vec3 = Vec2.GetVal(i)
    print "Vec3", i, Vec3.Len()

    for j in range(0,Vec3.Len()):
        print "Vec4", i, j, Vec3.GetVal(j).Val

