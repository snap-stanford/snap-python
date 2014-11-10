import snap

Graph = snap.GenFull(snap.PNEANet, 10)

NIdV = snap.TIntV()
Graph.GetNIdV(NIdV)
for i in NIdV:
    print "node", i

EIdV = snap.TIntV()
Graph.GetEIdV(EIdV)
for i in EIdV:
    print "edge", i

