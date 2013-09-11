import snap

#G6 = snap.GenForestFire(100000, 0.25, 0.25)
G6 = snap.GenRndGnm(snap.PNGraph, 10000, 5000)
print "type(G6) %s" % (type(G6))
print "G6 nodes %d, edges %d" % (G6.GetNodes(), G6.GetEdges())

l = []
for EI in G6.Edges():
    src = EI.GetSrcNId()
    dst = EI.GetDstNId()
    if EI.GetSrcNId() > EI.GetDstNId():
        dst = EI.GetSrcNId()
        src = EI.GetDstNId()

    l.append((src,dst))

l.sort()
#for item in l:
#    print "G6\t%d\t%d" % (item[0], item[1])


G7 = snap.ConvertGraph(snap.PUNGraph, G6)
print "type(G7) %s" % (type(G7))
print "G7 nodes %d, edges %d" % (G7.GetNodes(), G7.GetEdges())

l = []
for EI in G7.Edges():
    src = EI.GetSrcNId()
    dst = EI.GetDstNId()
    if EI.GetSrcNId() > EI.GetDstNId():
        dst = EI.GetSrcNId()
        src = EI.GetDstNId()

    l.append((src,dst))

l.sort()
#for item in l:
#    print "G7\t%d\t%d" % (item[0], item[1])

WccG6 = snap.GetMxWcc(G6)
print "type(WccG6) %s" % (type(WccG6))
print "WccG6 nodes %d, edges %d" % (WccG6.GetNodes(), WccG6.GetEdges())

WccG7 = snap.GetMxWcc(G7)
print "type(WccG7) %s" % (type(WccG7))
print "WccG7 nodes %d, edges %d" % (WccG7.GetNodes(), WccG7.GetEdges())

SccG6 = snap.GetMxScc(G6)
print "type(SccG6) %s" % (type(SccG6))
print "SccG6 nodes %d, edges %d" % (SccG6.GetNodes(), SccG6.GetEdges())

SccG7 = snap.GetMxScc(G7)
print "type(SccG7) %s" % (type(SccG7))
print "SccG7 nodes %d, edges %d" % (SccG7.GetNodes(), SccG7.GetEdges())

SubG6 = snap.GetSubGraph(G6, snap.TIntV.GetV(0,1,2,3,4))
print "type(SubG6) %s" % (type(SubG6))
print "SubG6 nodes %d, edges %d" % (SubG6.GetNodes(), SubG6.GetEdges())
for EI in SubG6.Edges():
    print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

Core3G6 = snap.GetKCore(G6, 3)
print "type(Core3G6) %s" % (type(Core3G6))
print "CoreG6 nodes %d, edges %d" % (Core3G6.GetNodes(), Core3G6.GetEdges())

G8 = snap.GenRndGnm(snap.PNGraph, 1000, 100000)
print "type(G8) %s" % (type(G8))
print "G8 nodes %d, edges %d" % (G8.GetNodes(), G8.GetEdges())

WccG8 = snap.GetMxWcc(G8)
print "type(WccG8) %s" % (type(WccG8))
print "WccG8 nodes %d, edges %d" % (WccG8.GetNodes(), WccG8.GetEdges())

WccG7 = snap.GetMxWcc(G7)
print "type(WccG7) %s" % (type(WccG7))
print "WccG7 nodes %d, edges %d" % (WccG7.GetNodes(), WccG7.GetEdges())

SccG8 = snap.GetMxScc(G8)
print "type(SccG8) %s" % (type(SccG8))
print "SccG8 nodes %d, edges %d" % (SccG8.GetNodes(), SccG8.GetEdges())

SccG7 = snap.GetMxScc(G7)
print "type(SccG7) %s" % (type(SccG7))
print "SccG7 nodes %d, edges %d" % (SccG7.GetNodes(), SccG7.GetEdges())

SubG8 = snap.GetSubGraph(G8, snap.TIntV.GetV(0,1,2,3,4))
print "type(SubG8) %s" % (type(SubG8))
print "SubG8 nodes %d, edges %d" % (SubG8.GetNodes(), SubG8.GetEdges())
for EI in SubG8.Edges():
    print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

Core3G8 = snap.GetKCore(G8, 3)
print "type(Core3G8) %s" % (type(Core3G8))
print "CoreG8 nodes %d, edges %d" % (Core3G8.GetNodes(), Core3G8.GetEdges())



