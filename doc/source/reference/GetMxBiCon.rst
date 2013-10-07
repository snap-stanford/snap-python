GetMxBiCon
'''''''''''

.. function:: GetMxBiCon(Graph)

Returns a graph representing the largest bi-connected component on an input Graph.
An undirected graph is bi-connected if by removing any single node does not disconnect the graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- *Graph*: graph (input)
    A Snap.py graph or a network


For more info see: http://en.wikipedia.org/wiki/Biconnected_component

The following example shows how to calculate PageRank scores for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    MxBiConGraph = snap.GetMxBiCon(Graph)


    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    MxBiConGraph = snap.GetMxBiCon(Graph)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    MxBiConGraph = snap.GetMxBiCon(Graph)
