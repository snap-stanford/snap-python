CntSelfEdges
''''''''''''

.. function:: CntSelfEdges ()

A graph method that returns the number of self edges in a graph. 

Parameters:

- None

Return value:

- int
    The number of self edges in a graph.


The following example shows how to calculate the number of self edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Count = Graph.CntSelfEdges()
    print("Directed Graph: Count of self edges is %d" % Count)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Count = UGraph.CntSelfEdges()
    print("Undirected Graph: Count of self edges is %d" % Count)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Count = Network.CntSelfEdges()
    print("Network Graph: Count of self edges is %d" % Count)
