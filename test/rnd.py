import snap

Graph = snap.GenFull(snap.PNEANet, 100)

for i in xrange(0,10):
    print "node id ", Graph.GetRndNId()

#for i in xrange(0,10):
#    print "node ni", Graph.GetRndNI().GetId()

for i in xrange(0,10):
    print "edge id ", Graph.GetRndEId()

#for i in xrange(0,10):
#    print "edge ni", Graph.GetRndEI().GetId()

