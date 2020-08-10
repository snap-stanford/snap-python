MakeUnDir
'''''''''

.. function:: MakeUnDir()

A graph method that makes the graph undirected. For every edge (u,v) an edge (v,u) is added (if it does not yet exist). The function has no effect on undirected graphs.

Parameters:

- None

Return value:

- None


The following example shows usage with graph types 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print(Graph.GetEdges())
    Graph.MakeUnDir()
    print(Graph.GetEdges())

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print(UGraph.GetEdges())
    UGraph.MakeUnDir()
    print(UGraph.GetEdges())

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print(Network.GetEdges())
    Network.MakeUnDir()
    print(Network.GetEdges())
