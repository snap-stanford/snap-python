DelNodes
''''''''

.. function:: DelNodes(Graph, NIdV)

Removes the nodes contained in the vector *NIdV* from *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NIdV*: TIntV, vector of ints (input)
    A vector of node ids to be deleted from *Graph*.

Return value:

- None


The following example shows how to delete nodes from
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    V = snap.TIntV()
    for i in range(10):
        Vec.Add(i)

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.DelNodes(Graph, V)
    for NI in V:
        if Graph.IsNode(NI):
            print "Node %d found in graph." % NI

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.DelNodes(UGraph, V)
    for NI in V:
        if UGraph.IsNode(NI):
            print "Node %d found in graph." % NI

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.DelNodes(Network, V)
    for NI in V:
        if Network.IsNode(NI):
            print "Node %d found in graph." % NI
