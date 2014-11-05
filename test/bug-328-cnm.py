import snap

g = snap.LoadEdgeList(snap.PUNGraph, 'data/final_sorted_edges.txt', 0, 1)
CmtyV = snap.TCnComV()

modularity = snap.CommunityCNM(g, CmtyV)
print modularity
