CntUniqUndirEdges (SWIG)
''''''''''''''''''''''''

.. function:: CntUniqUndirEdges(Graph)
   :noindex:

Returns the number of unique undirected edges in the graph *Graph*. 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

Return value:

- int
    The number of unique undirected edges in *Graph*.


The following example shows how to calculate the number of unique undirected edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Count = snap.CntUniqUndirEdges(Graph)
    print("Directed Graph: Count of unique undirected edges is %d" % Count)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Count = snap.CntUniqUndirEdges(UGraph)
    print("Undirected Graph: Count of unique undirected edges is %d" % Count)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Count = snap.CntUniqUndirEdges(Network)
    print("Network Graph: Count of unique undirected edges is %d" % Count)
