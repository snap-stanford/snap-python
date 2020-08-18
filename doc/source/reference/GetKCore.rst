GetKCore
'''''''''''''''

.. function:: GetKCore(K)

Returns the K-core of the graph *Graph*. If the core of order *K* does not exist, the function returns an empty graph.

Parameters

- *K*: int
    Minimum degree needed for a subgraph to be in the core.

Return value:

- graph
    A Snap.py graph or network where all nodes have degree >= *K*. The graph is empty if no such graph exists.


The following example shows how to check if a K-Core subgraph exists
for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    K = 5
    KCore = Graph.GetKCore(K)
    if KCore.Empty():
        print('No Core exists for K=%d' % K)
    else:
        print('Core exists for K=%d' % K)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    K = 10
    KCore = UGraph.GetKCore(K)
    if KCore.Empty():
        print('No Core exists for K=%d' % K)
    else:
        print('Core exists for K=%d' % K)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    K = 15
    KCore = Network.GetKCore(K)
    if KCore.Empty():
        print('No Core exists for K=%d' % K)
    else:
        print('Core exists for K=%d' % K)
