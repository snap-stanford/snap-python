GetCmnNbrs
''''''''''

.. function:: GetCmnNbrs(Graph, NId1, NId2, NbrV)

Computes the number of shared neighbors between a pair of nodes NId1 and NId2. The node ID of the neighbors are stored in *NbrV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NId1*: int (input)
    Node ID of first node

- *NId2*: int (input)
    Node ID of second node

- *NbrV*: vector of int (output)
    Shared neighbors between the two nodes. Neighbors are node IDs.

Return value:

- int
    Number of shared neighbors between the two nodes.

The following example shows how to find the shared neighbors of two nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    neighbors = snap.TIntV()
    numNbr = snap.GetCmnNbrs(graph, 0, 1, neighbors)
    print numNbr
    print [neighbor for neighbor in neighbors]

    graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    neighbors = snap.TIntV()
    numNbr = snap.GetCmnNbrs(graph, 0, 1, neighbors)
    print numNbr
    print [neighbor for neighbor in neighbors]

    graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    neighbors = snap.TIntV()
    numNbr = snap.GetCmnNbrs(graph, 0, 1, neighbors)
    print numNbr
    print [neighbor for neighbor in neighbors]
