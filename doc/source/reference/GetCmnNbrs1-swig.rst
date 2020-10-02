GetCmnNbrs (SWIG)
'''''''''''''''''

.. function:: GetCmnNbrs(Graph, NId1, NId2, NbrV)
   :noindex:

Computes the number of shared neighbors between a pair of nodes *NId1* and *NId2*. The node ids of the neighbors are stored in *NbrV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NId1*: int (input)
    Node id of the first node.

- *NId2*: int (input)
    Node id of the second node.

- *NbrV*: TIntV, vector of int (output)
    Shared neighbors between the two nodes. Neighbors are node IDs.

Return value:

- int
    The number of common neighbors between the pair of nodes.

The following example shows how to find the shared neighbors of two nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Nbrs = snap.TIntV()
    snap.GetCmnNbrs(Graph, 1, 10, Nbrs)
    for NId in Nbrs:
        print("node: %d" % NId)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Nbrs = snap.TIntV()
    snap.GetCmnNbrs(UGraph, 1, 10, Nbrs)
    for NId in Nbrs:
        print("node: %d" % NId)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Nbrs = snap.TIntV()
    snap.GetCmnNbrs(Network, 1, 10, Nbrs)
    for NId in Nbrs:
        print("node: %d" % NId)
