import snap

Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(Graph, Nodes, Edges, 1.0)
for node in Nodes:
    print("node: %d centrality: %f" % (node, Nodes[node]))
for edge in Edges:
    print("edge: (%d, %d) centrality: %f" % (edge.GetVal1(), edge.GetVal2(), Edges[edge]))

UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(UGraph, Nodes, Edges, 1.0)
for node in Nodes:
    print("node: %d centrality: %f" % (node, Nodes[node]))
for edge in Edges:
    print("edge: (%d, %d) centrality: %f" % (edge.GetVal1(), edge.GetVal2(), Edges[edge]))

Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(Network, Nodes, Edges, 1.0)
for node in Nodes:
    print("node: %d centrality: %f" % (node, Nodes[node]))
for edge in Edges:
    print("edge: (%d, %d) centrality: %f" % (edge.GetVal1(), edge.GetVal2(), Edges[edge]))


