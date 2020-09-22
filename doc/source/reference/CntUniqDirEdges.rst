CntUniqDirEdges
'''''''''''''''

.. function:: CntUniqDirEdges()

A graph method that returns the number of unique directed edges in a graph.

Parameters:

- None

Return value:

- int
    The number of unique directed edges in a graph.


The following example shows how to calculate the number of unique directed edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Count = Graph.CntUniqDirEdges()
    print("Directed Graph: Count of unique directed edges is %d" % Count)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Count = UGraph.CntUniqDirEdges()
    print("Undirected Graph: Count of unique Directed edges is %d" % Count)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Count = Network.CntUniqDirEdges()
    print("Network Graph: Count of unique Directed edges is  %d" % Count)
