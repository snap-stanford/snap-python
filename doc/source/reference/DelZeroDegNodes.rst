DelZeroDegNodes 
'''''''''''''''

.. function:: DelZeroDegNodes(Graph)

Removes all the zero-degree nodes from *Graph*.

Parameters:

- *Graph*: graph (input and output)
    A Snap.py graph or a network.

Return value:

- None


The following example shows how to delete all zero-degree nodes from 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 0)
    print "Number of nodes in directed graph: %d" % Graph.GetNodes()
    snap.DelZeroDegNodes(Graph)
    print "Number of nodes in directed graph after delete: %d" % Graph.GetNodes()

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 0)
    print "Number of nodes in undirected graph: %d" % UGraph.GetNodes()
    snap.DelZeroDegNodes(UGraph)
    print "Number of nodes in undirected graph after delete: %d" % UGraph.GetNodes()

    Network = snap.GenRndGnm(snap.PNEANet, 100, 0)
    print "Number of nodes in network: %d" % Network.GetNodes()
    snap.DelZeroDegNodes(Network)
    print "Number of nodes in network after delete: %d" % Network.GetNodes()