import snap

net = snap.TNEANet.New()
net.AddNode(0)
net.AddNode(1)
net.AddEdge(0,1)

net.AddStrAttrE('name')
#for edge in net.Edges():
#    net.AddStrAttrDatE(edge.GetId(),'01','name')

net.DelEdge(0,1)

