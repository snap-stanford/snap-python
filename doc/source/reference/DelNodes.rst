DelNodes
''''''''

.. function:: DelNodes(NIdV)

A graph method that removes the nodes contained in the vector *NIdV* from a graph.

Parameters:

- *NIdV*: Python list or :class:`TIntV`, vector of ints
    A vector of node ids to be deleted.

Return value:

- None


The following example shows how to delete nodes from
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    V = []
    for i in range(10):
        V.append(i)

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Network.DelNodes(V)
    for NI in V:
        if Graph.IsNode(NI):
            print("Node %d found in graph." % NI)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    UGraph.DelNodes(V)
    for NI in V:
        if UGraph.IsNode(NI):
            print("Node %d found in graph." % NI)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Network.DelNodes(V)
    for NI in V:
        if Network.IsNode(NI):
            print("Node %d found in graph." % NI)
