GetNodeTriadsSet
''''''''''''''''

.. function:: GetNodeTriadsSet(NId, GroupSet)

A graph method that returns the number of closed triads between a node *NId* and a subset of its neighbors in *GroupSet* as well as the number of triads for cases where neighbors are not in *GroupSet*.
Considers the graph to be undirected.

Parameters:

- *NId*: int
    NId of the node of interest

- *GroupSet*: Python set or :class:`TIntSet`
    Set of NIds representing a subset of the neighbors of the node of interest


Return value:

- list: [int, int, int, int]
    The list contains four elements: the first two elements are the number of closed triads between *NId* and nodes in *GroupSet*, the third element is the number of triads between *NId* and a node in *GroupSet* and another node not in *GroupSet*, the fourth element is the number of triads between *NId* and two nodes not in *GroupSet*.

The following example shows how to calculate the number of triads a node participates in for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenFull(snap.TNGraph, 100)
    NId = Graph.GetRndNId()
    NI = Graph.GetNI(NId)
    GroupSet = snap.TIntSet()
    for NbrIdx in range(4):
        GroupSet.AddKey(NI.GetOutNId(NbrIdx))
    result = Graph.GetNodeTriadsSet(NId, GroupSet)
    print("number of triads between", NId, " and two set members", result[0])
    print("number of triads between", NId, " and a set member and a set non-member", result[2])
    print("number of triads between", NId, " and two set non-members", result[3])

    UGraph = snap.GenFull(snap.TUNGraph, 100)
    NId = UGraph.GetRndNId()
    NI = UGraph.GetNI(NId)
    GroupSet = snap.TIntSet()
    for NbrIdx in range(4):
        GroupSet.AddKey(NI.GetOutNId(NbrIdx))
    result = UGraph.GetNodeTriadsSet(NId, GroupSet)
    print("number of triads between", NId, " and two set members", result[0])
    print("number of triads between", NId, " and a set member and a set non-member", result[2])
    print("number of triads between", NId, " and two set non-members", result[3])

    Network = snap.GenFull(snap.TNEANet, 100)
    NId = Network.GetRndNId()
    NI = Network.GetNI(NId)
    GroupSet = snap.TIntSet()
    for NbrIdx in range(4):
        GroupSet.AddKey(NI.GetOutNId(NbrIdx))
    result = Network.GetNodeTriadsSet(NId, GroupSet)
    print("number of triads between", NId, " and two set members", result[0])
    print("number of triads between", NId, " and a set member and a set non-member", result[2])
    print("number of triads between", NId, " and two set non-members", result[3])

