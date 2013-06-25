import random
import os
import sys
import time

sys.path.append("../swig")
import snap

numnodes = 100
valrange = numnodes / 5

Edges = snap.TIntV()

for i in range(0,numnodes):
    Edges.Add(int(random.random() * valrange))

d = {}
for i in range(0,numnodes,2):
    #print "Edges", i/2, Edges.GetVal(i).Val, Edges.GetVal(i+1).Val
    d[(Edges.GetVal(i).Val,Edges.GetVal(i+1).Val)] = 1

Hash = snap.TIntH()
#snap.Edge2Hash(Edges,Hash)

Hash.AddDat(3,5)
Hash.AddDat(4,6)
Hash.AddDat(1,8)
Hash.AddDat(6,2)

print "type", type(Edges), type(Hash)

#for i in range(0,valrange):
#    Vec2 = Hash.GetDat(i)
#    print i, Vec2.Val

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

sys.exit(0)

AdjLists = snap.TIntIntVH()
print "type", type(Edges), type(AdjLists)
snap.GetAdjLists(Edges, AdjLists)

size = 0
for i in range(0,valrange):
    Vec2 = AdjLists.GetDat(i)
    size += Vec2.Len()

    for j in range(0,Vec2.Len()):
        print i, Vec2.GetVal(j).Val

print "done", Edges.Len(), AdjLists.Len(), size, len(d)

sys.exit(0)

#print "dir(snap.TIntV)", dir(snap.TIntV)
Vec1 = snap.TIntV(numnodes)
#print "dir(Vec1)", dir(Vec1)
print "Len Vec1", Vec1.Len()

#print "dir(snap.TIntIntVV)", dir(snap.TIntIntVV)
Vec2 = snap.TIntIntVV(numtask)
#print "dir(Vec2)", dir(Vec2)
print "Len Vec2", Vec2.Len()

print "Vec1", type(Vec1)

snap.GetDegrees(Vec1, 10.0, 1.5)

for i in range(0,Vec1.Len()):
    print "Vec1", i, Vec1.GetVal(i).Val

snap.AssignRndTask(Vec1, Vec2)

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


