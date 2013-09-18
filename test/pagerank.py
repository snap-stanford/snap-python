import snap

Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
PRankH = snap.TIntFltH()
snap.GetPageRank(Graph, PRankH)
for item in PRankH:
    print item.GetKey(), item.GetDat()

Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
PRankH = snap.TIntFltH()
snap.GetPageRank(Graph, PRankH)
for item in PRankH:
    print item.GetKey(), item.GetDat()

Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
PRankH = snap.TIntFltH()
snap.GetPageRank(Graph, PRankH)
for item in PRankH:
    print item.GetKey(), item.GetDat()

