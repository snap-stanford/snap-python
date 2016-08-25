import snap

Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
for NI in Graph.Nodes():
    CloseCentr = snap.GetClosenessCentr(Graph, NI.GetId())
    print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)

UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
for NI in UGraph.Nodes():
    CloseCentr = snap.GetClosenessCentr(UGraph, NI.GetId())
    print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)

Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
for NI in Network.Nodes():
    CloseCentr = snap.GetClosenessCentr(Network, NI.GetId())
    print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)

