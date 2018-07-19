GetEdgesInOut
'''''''''''''

.. function:: GetEdgesInOut (Graph, NIdV)

Returns the number of reciprocal edges between the nodes in *NIdV* and the number of edges between the nodes in *NIdV* and the rest of the graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NIdV*: :class:`TIntV`, a vector of ints (input)
    A vector of node IDs.

Return value:

- list: [ int, int ]
    The list contains two elements: the first element gives the number of reciprocal edges between the nodes in *NIdV*, and the second element gives the number of edges between the nodes in *NIdV* and the rest of the graph.

The following example shows how to use :func:`GetEdgesInOut` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Nodes = snap.TIntV()
    for nodeId in range(10):
        Nodes.Add(nodeId)

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    results = snap.GetEdgesInOut(Graph, Nodes)
    print "EdgesIn: %s EdgesOut: %s" % (results[0], results[1])

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    results = snap.GetEdgesInOut(UGraph, Nodes)
    print "EdgesIn: %s EdgesOut: %s" % (results[0], results[1])

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    results = snap.GetEdgesInOut(Network, Nodes)
    print "EdgesIn: %s EdgesOut: %s" % (results[0], results[1])

