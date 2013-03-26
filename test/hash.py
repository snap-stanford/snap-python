import random
import os
import sys
import time

sys.path.append("../swig")
import snap as Snap

numnodes = 100
valrange = numnodes / 5

Edges = Snap.TIntV()

for i in range(0,numnodes):
    Edges.Add(int(random.random() * valrange))

d = {}
for i in range(0,numnodes,2):
    print "Edges", i/2, Edges.GetVal(i).Val, Edges.GetVal(i+1).Val
    d[(Edges.GetVal(i).Val,Edges.GetVal(i+1).Val)] = 1

Hash = Snap.TIntH()
#Snap.Edge2Hash(Edges,Hash)

Hash.AddDat(3,5)
Hash.AddDat(4,6)

print "type", type(Edges), type(Hash)

#for i in range(0,valrange):
#    Vec2 = Hash.GetDat(i)
#    print i, Vec2.Val

print "len", Hash.Len()
Iter = Hash.BegI()
Key = Iter.GetKey()
Value = Iter.GetDat()
print "iter", Key, Value

print "Iter < Hash.EndI", Iter < Hash.EndI()
while Iter < Hash.EndI():
    Key = Iter.GetKey()
    Value = Iter.GetDat()
    print Key, Value

    Iter.Next()

sys.exit(0)

AdjLists = Snap.TIntIntVH()
print "type", type(Edges), type(AdjLists)
Snap.GetAdjLists(Edges, AdjLists)

size = 0
for i in range(0,valrange):
    Vec2 = AdjLists.GetDat(i)
    size += Vec2.Len()

    for j in range(0,Vec2.Len()):
        print i, Vec2.GetVal(j).Val

print "done", Edges.Len(), AdjLists.Len(), size, len(d)

sys.exit(0)

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

sys.exit(0)

for i in range(0,Vec2.Len()):
    Vec3 = Vec2.GetVal(i)
    print "Vec3", i, Vec3.Len()

    h = httplib.HTTPConnection("rokl1.stanford.edu",8100)
    #h.request("POST","/msg/GenStubs-0/GenTasks-2","12345",{"User-agent": "007"})
    h.connect()
    url = "/msg/GenStubs-0/GenTasks-%d" % (i)
    h.putrequest("POST",url)
    h.putheader("User-Agent", "007")
    #h.putheader("Content-Length", "9")
    h.putheader("Content-Length", str(Vec3.GetMemSize()))
    h.endheaders()

    fileno = h.sock.fileno()
    print "fileno", fileno

    n = Vec3.Send(fileno)
    #n = os.write(fileno,"123abcdef")
    print n

    #h.send("abc123")

    res = h.getresponse()
    print res.status, res.reason
    data = res.read()
    print len(data)
    print data


