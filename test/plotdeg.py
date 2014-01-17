import snap

G1 = snap.GenRndGnm(snap.PNGraph, 100, 1000)
snap.PlotInDegDistr(G1, 'test_directed', 'test for directed gragh', 0, 0)

G2 = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
snap.PlotInDegDistr(G2, 'test_undirected', 'test for undirected gragh', 0, 0)

G3 = snap.GenRndGnm(snap.PNEANet, 100, 1000)
snap.PlotInDegDistr(G3, 'test_neanet', 'test for neanet', 0, 0)

