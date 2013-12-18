import snap

print "version", snap.Version
g = snap.TNEANet.New()
print "nodes", g.GetNodes(), "edges", g.GetEdges()

g.AddNode(1)
print "nodes", g.GetNodes(), "edges", g.GetEdges()

g.AddNode(2)
print "nodes", g.GetNodes(), "edges", g.GetEdges()

g.AddEdge(1,2)
print "nodes", g.GetNodes(), "edges", g.GetEdges()

g.AddIntAttrDatN(1,1,'node_attr')
g.AddIntAttrDatE(0,2,'edge_attr')

g.DelNode(1)
print "nodes", g.GetNodes(), "edges", g.GetEdges()

print "-------------------"

g = snap.TNEANet.New()
g.AddNode(0)
g.AddNode(2)
g.AddNode(1)
g.AddNode(3)
g.AddNode(4)
g.AddNode(5)

e = g.AddEdge(1,2)
print e
e = g.AddEdge(2,3)
print e
e = g.AddEdge(3,4)
print e
e = g.AddEdge(4,5)
print e
e = g.AddEdge(2,5)
print e

#g.AddIntAttrDatN(1, 1, 'weight')
g.AddIntAttrDatE(0, 2, 'edge_weight')
g.AddIntAttrDatE(1, 5, 'edge_weight')
g.AddIntAttrDatE(2, 9, 'edge_weight')
g.AddIntAttrDatE(3, 12, 'edge_weight')
g.AddIntAttrDatE(4, 232, 'edge_weight')
#print g.GetNodes()
g.DelNode(1)
g.DelNode(3)
#print g.GetNodes()

for edge in g.Edges():
    print edge.GetSrcNId(), edge.GetDstNId(), g.GetIntAttrDatE(edge.GetId(), 'edge_weight')         

