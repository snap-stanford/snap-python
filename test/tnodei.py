import snap

G2 = snap.GenRndGnm(snap.PNGraph, 100, 1000)
count = 0
for NI in G2.Nodes():
    count += 1
    print "%2d: node %d, out-degree %d, in-degree %d" % ( count, NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
    print "GetId() %d" % (NI.GetId())
    print "GetOutDeg() %d" % (NI.GetOutDeg())
    print "GetInDeg() %d" % (NI.GetInDeg())
    print "GetOutNId(0) %d" % (NI.GetOutNId(0))
    print "GetOutNId(1) %d" % (NI.GetOutNId(1))
    print "GetInNId(0) %d" % (NI.GetInNId(0))
    print "GetInNId(1) %d" % (NI.GetInNId(1))
    e1 = NI.GetOutNId(3)
    print "IsOutNId(%d): %d" % (e1, NI.IsOutNId(e1))
    print "IsOutNId(101): %d" % (NI.IsOutNId(101))
    e2 = NI.GetInNId(2)
    print "IsInNId(%d): %d" % (e2, NI.IsInNId(e2))
    print "IsInNId(101): %d" % (NI.IsInNId(101))
    print "IsNbhNId(%d): %d" % (e1, NI.IsNbrNId(e1))
    print "IsNbhNId(%d): %d" % (e2, NI.IsNbrNId(e2))
    print "IsNbrNId(101): %d" % (NI.IsNbrNId(101))

