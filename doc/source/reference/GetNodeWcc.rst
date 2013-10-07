GetNodeWcc
''''''''''

.. function:: GetNodeWcc(Graph, NId, CnCom)

Returns (via output parameter CnCom) all nodes that are in the same connected component as node NId.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NId*: int (input)
    Node Id.

- *CnCom*: a vector of int values (output)
    Values of the vectors are connected component node IDs

Return value:

- None

The following example shows how to get  connected component of nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    G1 = snap.TNGraph.New()
    G1.AddNode(1)
    G1.AddNode(3)
    G1.AddNode(5)
    G1.AddNode(32)
    G1.AddNode(2)
    
    G1.AddEdge(1,5)
    G1.AddEdge(5,1)
    G1.AddEdge(5,32)
    G1.AddEdge(3,5)
    G1.AddEdge(32,5)
    G1.AddEdge(3,2)
    
    for NI in G1.Nodes():
    	print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
    	tv = snap.TIntV()
    	snap.GetNodeWcc(G1,NI.GetId(),tv)
    	for item in tv:
    		print tv[item]
    
    G1 = snap.TUNGraph.New()
    G1.AddNode(1)
    G1.AddNode(3)
    G1.AddNode(5)
    G1.AddNode(32)
    G1.AddNode(2)
    
    G1.AddEdge(1,5)
    G1.AddEdge(5,1)
    G1.AddEdge(5,32)
    G1.AddEdge(3,5)
    G1.AddEdge(32,5)
    G1.AddEdge(3,2)
    
    for NI in G1.Nodes():
    	print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
    	tv = snap.TIntV()
    	snap.GetNodeWcc(G1,NI.GetId(),tv)
    	for item in tv:
    		print tv[item]
    
    G1 = snap.TNEANet.New()
    G1.AddNode(1)
    G1.AddNode(3)
    G1.AddNode(5)
    G1.AddNode(32)
    G1.AddNode(2)
    
    G1.AddEdge(1,5)
    G1.AddEdge(5,1)
    G1.AddEdge(5,32)
    G1.AddEdge(3,5)
    G1.AddEdge(32,5)
    G1.AddEdge(3,2)
    
    for NI in G1.Nodes():
    	print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
    	tv = snap.TIntV()
    	snap.GetNodeWcc(G1,NI.GetId(),tv)
    	for item in tv:
		print tv[item]
