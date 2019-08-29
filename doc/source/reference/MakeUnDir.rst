MakeUnDir
'''''''''

.. function:: MakeUnDir(Graph)

Makes the graph undirected. For every edge (u,v) an edge (v,u) is added (if it does not yet exist). The function has no effect on undirected graphs.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

Return value:

- None


The following example shows usage with graph types 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print(Graph.GetEdges())
    snap.MakeUnDir(Graph)
    print(Graph.GetEdges())

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print(UGraph.GetEdges())
    snap.MakeUnDir(UGraph)
    print(UGraph.GetEdges())

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print(Network.GetEdges())
    snap.MakeUnDir(Network)
    print(Network.GetEdges())
