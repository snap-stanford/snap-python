DelZeroDegNodes 
'''''''''''''''

.. function:: DelZeroDegNodes()

A graph method that removes all the zero-degree nodes from a graph.

Parameters:

- None

Return value:

- None


The following example shows how to delete all zero-degree nodes from 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 0)
    print("Number of nodes in directed graph: %d" % Graph.GetNodes())
    Graph.DelZeroDegNodes()
    print("Number of nodes in directed graph after delete: %d" % Graph.GetNodes())

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 0)
    print("Number of nodes in undirected graph: %d" % UGraph.GetNodes())
    UGraph.DelZeroDegNodes()
    print("Number of nodes in undirected graph after delete: %d" % UGraph.GetNodes())

    Network = snap.GenRndGnm(snap.TNEANet, 100, 0)
    print("Number of nodes in network: %d" % Network.GetNodes())
    Network.DelZeroDegNodes()
    print("Number of nodes in network after delete: %d" % Network.GetNodes())
