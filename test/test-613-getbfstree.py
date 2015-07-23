import snap

G = snap.TNGraph.New()
for i in range(4):
    xxx = G.AddNode(i)

xxx = G.AddEdge(0,1); xxx = G.AddEdge(0,2)
xxx = G.AddEdge(1,3); xxx = G.AddEdge(2,3)


T = snap.GetBfsTree(G, 0, True, True)

#T = snap.GetBfsTree(G, 0, True, False) # same result

#T = snap.GetBfsTree(G, 0, False, True) # node 0 only, no edges

#T = snap.GetBfsTree(G, 0, False, False) # node 0 only, no edges

for e in T.Edges():
    print e.GetSrcNId(), e.GetDstNId()

