import snap

Graph = snap.TNEANet.New()
Graph.AddFltAttrN("Test 1")
for i in range(5):
  Graph.AddNode()

Graph.AddFltAttrDatN(3, 103.0, "Test 1")
Graph.GetFltAttrDatN(3, "Test 1") # Returns 103.0
Graph.DelNode(0)
Graph.GetFltAttrDatN(3, "Test 1") # Returns 103.0
Graph.AddNode()
Graph.GetFltAttrDatN(3, "Test 1") # Returns -1.7976931348623157e+308
Graph.GetFltAttrDatN(4, "Test 1") # Returns 103.0