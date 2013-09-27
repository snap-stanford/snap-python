import snap

G = snap.TNGraph.New()
G.AddNode(1)
G.AddNode(2)
G.AddNode(3)
G.AddNode(4)
G.AddEdge(1,2)
G.AddEdge(2,3)
G.AddEdge(1,3)
G.AddEdge(2,4)
G.AddEdge(3,4)

S = snap.TIntStrH()
S.AddDat(1,"David")
S.AddDat(2,"Emma")
S.AddDat(3,"Jim")
S.AddDat(4,"Sam")

snap.DrawGViz(G, snap.gvlDot, "gviz.png", "Graph", S)

