CntUniqBiDirEdges
'''''''''''''''''

.. function:: CntUniqBiDirEdges()

A function that returns the number of unique bidirectional edges in a graph.

Parameters:

- None

Return value:

- int
    The number of unique bidirectional edges in a graph.


The following example shows how to calculate the number of unique bidirectional edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Count = Graph.CntUniqBiDirEdges()
    print("Directed Graph: Count of unique bidirectional edges is %d" % Count)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Count = UGraph.CntUniqBiDirEdges()
    print("Undirected Graph: Count of unique bidirectional edges is %d" % Count)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Count = Network.CntUniqBiDirEdges()
    print("Network Graph: Count of unique bidirectional edges is %d" % Count)
