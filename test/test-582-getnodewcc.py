import snap

Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
CnCom = snap.TIntV()
snap.GetNodeWcc(Graph, 0, CnCom)
print("Nodes in the same connected component as node 0:")
for node in CnCom:
    print(node)

