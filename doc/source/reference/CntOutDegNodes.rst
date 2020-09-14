CntOutDegNodes
'''''''''''''''''''

.. function:: CntOutDegNodes(NodeOutDeg)

A graph method that returns the number of nodes in a graph with out-degree *NodeOutDeg*.

Parameters:

- *NodeOutDeg*: int
    The out-degree of the nodes to be counted.

Return value:

- int
    The number of nodes in a graph with out-degree *NodeOutDeg*.


The following example shows how to get the number of nodes with out-degrees 10, 20 and 5 in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::
    
    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Count = Graph.CntOutDegNodes(10)
    print("Directed Graph: Count of nodes with out-degree 10 is %d" % Count)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Count = UGraph.CntOutDegNodes(20)
    print("Undirected Graph: Count of nodes with out-degree 20 is %d" % Count)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Count = Network.CntOutDegNodes(5)
    print("Network Graph: Count of nodes with out-degree 5 is %d" % Count)
