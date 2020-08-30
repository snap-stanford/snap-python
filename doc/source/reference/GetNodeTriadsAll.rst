GetNodeTriadsAll
''''''''''''''''

.. function:: GetNodeTriadsAll(NId)

A graph method that returns the number of closed and open triads that a node *NId* participates in.

Considers the graph as undirected.

Parameters:

- *NId*: int
	The id of the node of interest.

Return value:

- list: [int, int, int]
    The list contains three elements: the first two elements are the number of closed triads and the third element is the number of open triads in the graph.

The following example shows how to compute the number of closed and open triads that a node *NId* participates in for the :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` classes::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    result = Graph.GetNodeTriadsAll(2)
    print("closed triads", result[0])
    print("open triads", result[2])

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    result = UGraph.GetNodeTriadsAll(5)
    print("closed triads", result[0])
    print("open triads", result[2])

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    result = Network.GetNodeTriadsAll(6)
    print("closed triads", result[0])
    print("open triads", result[2])

