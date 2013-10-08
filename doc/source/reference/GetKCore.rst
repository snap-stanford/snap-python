GetKCore
'''''''''''''''
.. note::

    This page is a draft and under revision.



.. function:: PGraph GetKCore (Graph, K)

Returns the K-core of a graph. If the core of order K does not exist the function returns an empty graph.



Parameters

- *Graph*: graph (input)
    A Snap.py graph or a network    

- *K*: int (input)
    Minimum degree needed for a subgraph to be in the core

Return value:

- *PGraph*: graph
    A Snap.py graph or network where all nodes have degree > K. The graph is empty if no such graph exists.


For more info see: http://en.wikipedia.org/wiki/K-cores#k-Cores


The following example shows how to check if a K-Core subgraph exists
for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    K = 5
    KCore = snap.GetKCore(Graph, K)
    if KCore.Empty():
        print 'No Core exists for K=%d' % K
    else:
	print 'Core exists for K=%d!' % K

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    K = 10
    KCore = snap.GetKCore(Graph, K)
    if KCore.Empty():
        print 'No Core exists for K=%d' % K
    else:
	print 'Core exists for K=%d!' % K

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    K = 15
    KCore = snap.GetKCore(Graph, K)
    if KCore.Empty():
        print 'No Core exists for K=%d' % K
    else:
	print 'Core exists for K=%d!' % K
