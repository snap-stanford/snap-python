CntUniqUndirEdges
'''''''''''''''''

.. function:: CntUniqUndirEdges()

A graph method that returns the number of unique undirected edges in a graph. 

Parameters:

- None

Return value:

- int
    The number of unique undirected edges in a graph.


The following example shows how to calculate the number of unique undirected edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Count = Graph.CntUniqUndirEdges()
    print("Directed Graph: Count of unique undirected edges is %d" % Count)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Count = UGraph.CntUniqUndirEdges()
    print("Undirected Graph: Count of unique undirected edges is %d" % Count)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Count = Network.CntUniqUndirEdges()
    print("Network Graph: Count of unique undirected edges is %d" % Count)
