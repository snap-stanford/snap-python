import snap

G = snap.TUNGraph.New()
for i in range(10):
    G.AddNode(i)
G.AddEdge(1,2)
G.AddEdge(1,3)
G.AddEdge(2,3)

print(snap.CntEdgesToSet(G,1,{2,3}))
