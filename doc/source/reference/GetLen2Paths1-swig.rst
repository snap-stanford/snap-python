GetLen2Paths (SWIG)
'''''''''''''''''''''

.. function:: GetLen2Paths (Graph, NId1, NId2, NbrV)
   :noindex:

Returns the number of length 2 paths between a pair of nodes *NId1*, *NId2* (*NId1* --> U --> *NId2*).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NId1*: int (input)
    ID of the source node

- *NId2*: int (input)
    ID of the destination node

- *NbrV*: TIntV (output)
    A vector of nodes on each path between node *NId1* and node *NId2*. The vector is filled by the function.

Return value:

- int: the number of length 2 paths between a pair of nodes.

The following example shows how to use GetLen2Paths in :class:`PUNGraph`, :class:`PNGraph`, and :class:`PNEANet`::

    import snap

    g = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NbrV = snap.TIntV()
    Num = snap.GetLen2Paths(g, 0, 1, NbrV)
    print("The number of paths between nodes %d and %d is %d" % (0, 1, Num))
    for Nbr in NbrV:
        print("Path: %d %d %d" % (0, Nbr, 1))

    g = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NbrV = snap.TIntV()
    Num = snap.GetLen2Paths(g, 0, 1, NbrV)
    print("The number of paths between nodes %d and %d is %d" % (0, 1, Num))
    for Nbr in NbrV:
        print("Path: %d %d %d" % (0, Nbr, 1))

    g = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NbrV = snap.TIntV()
    Num = snap.GetLen2Paths(g, 0, 1, NbrV)
    print("The number of paths between nodes %d and %d is %d" % (0, 1, Num))
    for Nbr in NbrV:
        print("Path: %d %d %d" % (0, Nbr, 1))

