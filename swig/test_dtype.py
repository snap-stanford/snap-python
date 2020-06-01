import snap

G = snap.TUNGraph.New()
for i in range(10):
    G.AddNode(i)
G.AddEdge(1,2)
G.AddEdge(1,3)
G.AddEdge(2,3)
NodeId = 1

#Old
NodeSet = snap.TIntSet()
NodeSet.AddKey(2)
NodeSet.AddKey(3)
print(snap.CntEdgesToSet(G, NodeId, NodeSet))

#New
print(snap.CntEdgesToSet(G, NodeId, {'2',3}))
print(G.CntEdgesToSet(NodeId, {2,3}))
