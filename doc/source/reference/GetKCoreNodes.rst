GetKCoreNodes
'''''''''''''''

.. function:: GetKCoreNodes()

Returns the number of nodes in each core of order K (where K=0, 1, ...).

Parameters:

- None

Return value:

- int
    The number of cores.

- :class:`TIntPrV`, a vector of (int, int) pairs
    A vector of (order K, number of nodes of the given order) pairs. 

The following example shows how to get the number of nodes for a given k-core in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    kValue, CoreIDSzV = Graph.GetKCoreNodes()
    for item in CoreIDSzV:
        print("order: %d nodes: %d" % (item.GetVal1(), item.GetVal2()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    kValue, CoreIDSzV = UGraph.GetKCoreNodes()
    for item in CoreIDSzV:
        print("order: %d nodes: %d" % (item.GetVal1(), item.GetVal2()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    kValue, CoreIDSzV = Network.GetKCoreNodes()
    for item in CoreIDSzV:
        print("order: %d nodes: %d" % (item.GetVal1(), item.GetVal2()))

