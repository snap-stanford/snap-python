GetNodeTriadsAll (SWIG)
'''''''''''''''''''''''

.. function:: GetNodeTriadsAll(Graph, NId)

Returns the number of closed and open triads that a node *NId* participates in.

Considers the *Graph* as undirected.

Parameters:

- *Graph*: PGraph (input)
    A Snap.py PGraph (considered as undirected)

- *NId*: int (input)
	The Id of the node of interest in *Graph*

- *ClosedTriads*: int (input)
	Number of closed triads

- *OpenTriads*: int (input)
	Number of open triads

Return value:

- list: [int, int, int]
    The list contains three elements: the first two elements are the number of closed triads and the third element is the number of open triads in the graph.

The following example shows how to compute the number of closed and open triads that a node *NId* participates in for the :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` classes::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    result = snap.GetNodeTriadsAll(Graph, 2)
    print("closed triads", result[0])
    print("open triads", result[2])

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    result = snap.GetNodeTriadsAll(Graph, 5)
    print("closed triads", result[0])
    print("open triads", result[2])

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    result = snap.GetNodeTriadsAll(Graph, 6)
    print("closed triads", result[0])
    print("open triads", result[2])

