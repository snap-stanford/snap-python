import httplib
import os
import sys
import time

sys.path.append("../swig")
import snap

numnodes = 100
numtask = 10

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

#sys.exit(0)

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


