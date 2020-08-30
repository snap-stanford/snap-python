GetCmnNbrs
'''''''''''

.. function:: GetCmnNbrs(NId1, NId2, NbrList = False)

A graph method that computes the number of shared neighbors between a pair of nodes *NId1* and *NId2*.

Parameters:

- *NId1*: int
    Node id of the first node.

- *NId2*: int
    Node id of the second node.

- (optional) *NbrList*: bool
    Specifies whether to return the list of shared neighbors *NbrV*. 

Return value:

- int
    The number of common neighbors between the pair of nodes.

- (optional) *NbrV*: :class:`TIntV`, a string hash table with string keys and int values
    It provides shared neighbors between the two nodes and is returned if *NbrList* is True. Neighbors are given by their node ids.


The following example shows how to calculate number of neighbors for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.GetCmnNbrs(1, 10)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    UGraph.GetCmnNbrs(1, 10)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Network.GetCmnNbrs(1, 10)

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    numNbrs, Nbrs = Graph.GetCmnNbrs(1, 10, True)
    for NId in Nbrs:
        print("node: %d" % NId)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    numNbrs, Nbrs = UGraph.GetCmnNbrs(1, 10, True)
    for NId in Nbrs:
        print("node: %d" % NId)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    numNbrs, Nbrs = Network.GetCmnNbrs(1, 10, True)
    for NId in Nbrs:
        print("node: %d" % NId)
