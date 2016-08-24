import snap

frac = 1.0
dir = True

UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(UGraph, Nodes, Edges, frac, dir)

for node in Nodes:
    print "node: %d centrality: %f" % (node, Nodes[node])

for edge in Edges:
    print "edge: (%d, %d) centrality: %f" % (
            edge.GetVal1(), edge.GetVal2(), Edges[edge])

DGraph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(DGraph, Nodes, Edges, frac, dir)

for node in Nodes:
    print "node: %d centrality: %f" % (node, Nodes[node])

for edge in Edges:
    print "edge: (%d, %d) centrality: %f" % (
            edge.GetVal1(), edge.GetVal2(), Edges[edge])

Net = snap.GenRndGnm(snap.PNEANet, 100, 1000)
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(Net, Nodes, Edges, frac, dir)

for node in Nodes:
    print "node: %d centrality: %f" % (node, Nodes[node])

for edge in Edges:
    print "edge: (%d, %d) centrality: %f" % (
            edge.GetVal1(), edge.GetVal2(), Edges[edge])

