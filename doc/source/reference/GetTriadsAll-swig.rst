GetTriadsAll (SWIG)
'''''''''''''''''''

.. function:: GetTriadsAll (Graph, SampleNodes=-1)

Computes the number of closed and open triads for every node in *Graph*. Considers the graph as undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *SampleNodes*: integer (input)
    If equal to -1, then compute triads over all the nodes. Otherwise,
    compute triads only for a random sample of *SampleNodes* nodes, which is
    useful for approximate but quick computations.

Return value:

- list: [int, int, int]
    The list contains three elements: the first two elements are the number of closed triads and the third element is the number of open triads in the graph.

The following example shows how to compute the number of open and closed triads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    result = snap.GetTriadsAll(Graph)
    print("closed triads", result[0])
    print("open triads", result[2])

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    result = snap.GetTriadsAll(Graph)
    print("closed triads", result[0])
    print("open triads", result[2])

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    result = snap.GetTriadsAll(Graph)
    print("closed triads", result[0])
    print("open triads", result[2])

