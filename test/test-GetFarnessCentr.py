import snap

Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
for NI in Graph.Nodes():
    FarCentr = snap.GetFarnessCentr(Graph, NI.GetId())
    print "node: %d centrality: %f" % (NI.GetId(), FarCentr)

UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
for NI in UGraph.Nodes():
    FarCentr = snap.GetFarnessCentr(UGraph, NI.GetId())
    print "node: %d centrality: %f" % (NI.GetId(), FarCentr)

Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
for NI in Network.Nodes():
    FarCentr = snap.GetFarnessCentr(Network, NI.GetId())
    print "node: %d centrality: %f" % (NI.GetId(), FarCentr)

