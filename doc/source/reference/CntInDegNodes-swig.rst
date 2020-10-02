CntInDegNodes (SWIG)
''''''''''''''''''''''''''

.. function:: CntInDegNodes(Graph, NodeInDeg)
   :noindex:

Returns the number of nodes in *Graph* with in-degree *NodeInDeg*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NodeInDeg*: int (input)
    The in-degree of the nodes to be counted.

Return value:

- int
    The number of nodes in *Graph* with in-degree *NodeInDeg*.


The following example shows how to get the number of nodes with in-degrees 10, 20 and 5 in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::
    
    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Count = snap.CntInDegNodes(Graph, 10)
    print("Directed Graph: Count of nodes with in-degree 10 is %d" % Count)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Count = snap.CntInDegNodes(UGraph, 20)
    print("Undirected Graph: Count of nodes with in-degree 20 is %d" % Count)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Count = snap.CntInDegNodes(Network, 5)
    print("Network Graph: Count of nodes with in-degree 5 is %d" % Count)
