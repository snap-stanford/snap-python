GetNodeWcc
''''''''''

.. function:: GetNodeWcc(NId)

A graph method that returns all nodes that are in the same connected component as node *NId*.

Parameters:

- *NId*: int
    A node id in the graph.

Return value:

- *CnCom*: :class:`TIntV`, a vector of ints
    All nodes that are in the same weakly connected component as *NId*.

The following example shows how to get the nodes in the same connected component as node 0 in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    CnCom = Graph.GetNodeWcc(0)
    print("Nodes in the same connected component as node 0:")
    for node in CnCom:
        print(node)


    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    CnCom = UGraph.GetNodeWcc(0)
    print("Nodes in the same connected component as node 0:")
    for node in CnCom:
        print(node)


    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    CnCom = Network.GetNodeWcc(0)
    print("Nodes in the same connected component as node 0:")
    for node in CnCom:
        print(node)
