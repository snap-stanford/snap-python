GetKCoreEdges
'''''''''''''

.. function:: GetKCoreEdges(Graph, CoreIDSzV)

Returns the number of edges in each core of order K (where K=0, 1, ...).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *CoreIDSzV*: a vector of int pairs (output)
    The first number of every pair is the order K. The second number of every pair is the number of edges for the given order K.

Return value:

- Returns the current value of K. (This value increases by 1 for every valid call to GetNextCore(). After the highest valid value, resets to 0.)

For more info see: http://en.wikipedia.org/wiki/Degeneracy_(graph_theory)#k-Cores

The following example shows how to get the number of edges for a given k-core in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    CoreIDSzV = snap.TIntPrV()
    kValue = snap.GetKCoreEdges(Graph, CoreIDSzV)
    for item in CoreIDSzV:
        print item.GetVal1(), item.GetVal2()

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    CoreIDSzV = snap.TIntPrV()
    kValue = snap.GetKCoreEdges(Graph, CoreIDSzV)
    for item in CoreIDSzV:
        print item.GetVal1(), item.GetVal2()

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    CoreIDSzV = snap.TIntPrV()
    kValue = snap.GetKCoreEdges(Graph, CoreIDSzV)
    for item in CoreIDSzV:
        print item.GetVal1(), item.GetVal2()
