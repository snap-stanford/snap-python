import snap

Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
PRankH = snap.TIntFltH()
snap.GetPageRank(Graph, PRankH)

snap.GetPageRank(Graph, PRankH, C=0.85)

