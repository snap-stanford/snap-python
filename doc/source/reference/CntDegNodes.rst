CntDegNodes
'''''''''''

.. function:: CntDegNodes(NodeDeg)

A graph method that returns the number of nodes in a graph with degree *NodeDeg*.

Parameters:

- *NodeDeg*: int
    The degree of the nodes to be counted.

Return value:

- int
    The number of nodes in a graph with degree *NodeDeg*.


The following example shows how to get the number of nodes with degree 20 in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Count = Graph.CntDegNodes(10)
    print("Directed Graph: Count of nodes with degree 10 is %d" % Count)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Count = UGraph.CntDegNodes(20)
    print("Undirected Graph: Count of nodes with degree 20 is %d" % Count)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Count = Network.CntDegNodes(5)
    print("Network Graph: Count of nodes with degree 5 is %d" % Count)
