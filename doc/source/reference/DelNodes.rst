DelNodes
''''''''

.. function:: DelNodes(Graph, NIdV)

Removes all the nodes contained in the vector *NIdV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NIdV*: TIntV, vector of ints (input)
    Node Id's to be deleted from the Graph


Return value:

- None

The following example shows how to delete nodes in
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
    
    v = snap.TIntV()
    v.Add(2)
    snap.DelNodes(G1,v)
    for NI in G1.Nodes():
    	print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
    
    G2 = snap.TUNGraph.New()
    G2.AddNode(1)
    G2.AddNode(3)
    G2.AddNode(5)
    G2.AddNode(32)
    G2.AddNode(2)
    
    G2.AddEdge(1,5)
    G2.AddEdge(5,32)
    G2.AddEdge(3,5)
    G2.AddEdge(3,2)
    
    v = snap.TIntV()
    v.Add(2)
    snap.DelNodes(G2,v)
    for NI in G2.Nodes():
    	print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
    	
    G3 = snap.TNEANet.New()
    G3.AddNode(1)
    G3.AddNode(3)
    G3.AddNode(5)
    G3.AddNode(32)
    G3.AddNode(2)
    
    G3.AddEdge(1,5)
    G3.AddEdge(5,1)
    G3.AddEdge(5,32)
    G3.AddEdge(3,5)
    G3.AddEdge(32,5)
    G3.AddEdge(3,2)
    
    v = snap.TIntV()
    v.Add(2)
    snap.DelNodes(G3,v)
    for NI in G3.Nodes():
	print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
