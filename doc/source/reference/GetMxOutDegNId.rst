GetMxOutDegNId
''''''''''''''

.. function:: GetMxOutDegNId(Graph)

Returns the NId of the node in *Graph* with the maximum out-degree. If multiple nodes have the maximum out-degree, GetMxOutDegNId will return the node that was added to the graph first. Treats all graphs as undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- *NId*: int
	The NId of the node with the maximum out-degree in *Graph*. If there are multiple nodes with the max out-degree, NId will be the NId of the node that was added to the graph first.

The following example shows how to extract the NId of (one of) the node(s) with maximum out-degree for graphs in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NodeMaxDeg = snap.GetMxOutDegNId(Graph)
    print NodeMaxDeg

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NodeMaxDeg = snap.GetMxOutDegNId(Graph)
    print NodeMaxDeg

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NodeMaxDeg = snap.GetMxOutDegNId(Graph)
    print NodeMaxDeg
