import snap

#G6 = snap.GenForestFire(100000, 0.25, 0.25)
G6 = snap.GenRndGnm(snap.PNGraph, 10000, 5000)
print "type(G6) %s" % (type(G6))
print "G6 nodes %d, edges %d" % (G6.GetNodes(), G6.GetEdges())

G7 = snap.ConvertGraph(snap.PUNGraph, G6)
print "type(G7) %s" % (type(G7))
print "G7 nodes %d, edges %d" % (G7.GetNodes(), G7.GetEdges())

WccG6 = snap.GetMxWcc(G6)
print "type(WccG6) %s" % (type(WccG6))
print "WccG6 nodes %d, edges %d" % (WccG6.GetNodes(), WccG6.GetEdges())

G8 = snap.GenForestFire(1000, 0.35, 0.35)
print "type(G8) %s" % (type(G8))
print "G8 nodes %d, edges %d" % (G8.GetNodes(), G8.GetEdges())

SubG8 = snap.GetSubGraph(G8, snap.TIntV.GetV(0,1,2,3,4))
print "type(SubG8) %s" % (type(SubG8))
print "SubG8 nodes %d, edges %d" % (SubG8.GetNodes(), SubG8.GetEdges())

Core3G8 = snap.GetKCore(G8, 3)
print "type(Core3G8) %s" % (type(Core3G8))
print "CoreG8 nodes %d, edges %d" % (Core3G8.GetNodes(), Core3G8.GetEdges())

snap.DelDegKNodes(G8, 3, 2)
print "type(G8) %s" % (type(G8))
print "G8 nodes %d, edges %d" % (G8.GetNodes(), G8.GetEdges())

