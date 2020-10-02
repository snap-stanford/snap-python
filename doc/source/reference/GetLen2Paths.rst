GetLen2Paths
''''''''''''

.. function:: GetLen2Paths (NId1, NId2, ReturnPaths=False)

A graph method that returns the number of length 2 directed paths between a pair of nodes *NId1*, *NId2* (*NId1* --> U --> *NId2*).

Parameters:

- *NId1*: int
    ID of first node.

- *NId2*: int
    ID of second node.

- (optional) *ReturnPaths*: bool
    Specifies whether to return *NbrV*

Return value:

- int: the number of length 2 paths between *NId1* and *NId2*.

- (optional) *NbrV*: :class:`TIntV`
    A vector of nodes on each path between node *NId1* and node *NId2*. It is returned, if *ReturnPaths* is True.

The following example shows how to calculate the number of length 2 directed paths between nodes within a :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    NumLen2Paths = Graph.GetLen2Paths(0, 1)
    NumLen2Paths, NbrV = Graph.GetLen2Paths(0, 1, True)
    print("The number of paths between nodes %d and %d is %d" % (0, 1, NumLen2Paths))
    for Nbr in NbrV:
        print("Path: %d %d %d" % (0, Nbr, 1))

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    NumLen2Paths = UGraph.GetLen2Paths(0, 1)
    NumLen2Paths, NbrV = UGraph.GetLen2Paths(0, 1, True)
    print("The number of paths between nodes %d and %d is %d" % (0, 1, NumLen2Paths))
    for Nbr in NbrV:
        print("Path: %d %d %d" % (0, Nbr, 1))

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    NumLen2Paths = Network.GetLen2Paths(0, 1)
    NumLen2Paths, NbrV = Network.GetLen2Paths(0, 1, True)
    print("The number of paths between nodes %d and %d is %d" % (0, 1, NumLen2Paths))
    for Nbr in NbrV:
        print("Path: %d %d %d" % (0, Nbr, 1))
