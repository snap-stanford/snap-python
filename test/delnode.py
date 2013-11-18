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

