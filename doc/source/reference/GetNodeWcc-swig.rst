GetNodeWcc (SWIG)
'''''''''''''''''

.. function:: GetNodeWcc(Graph, NId, CnCom)

Returns (via output parameter *CnCom*) all nodes that are in the same connected component as node *NId*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NId*: int (input)
    A node id in *Graph*.

- *CnCom*: :class:`TIntV`, a vector of ints (output)
    All nodes that are in the same weakly connected component as *NId*.

Return value:

- None


The following example shows how to get the nodes in the same connected component as node 0 in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    CnCom = snap.TIntV()
    snap.GetNodeWcc(Graph, 0, CnCom)
    print("Nodes in the same connected component as node 0:")
    for node in CnCom:
        print(node)


    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    CnCom = snap.TIntV()
    snap.GetNodeWcc(UGraph, 0, CnCom)
    print("Nodes in the same connected component as node 0:")
    for node in CnCom:
        print(node)


    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    CnCom = snap.TIntV()
    snap.GetNodeWcc(Network, 0, CnCom)
    print("Nodes in the same connected component as node 0:")
    for node in CnCom:
        print(node)
