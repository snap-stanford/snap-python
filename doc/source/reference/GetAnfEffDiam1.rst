GetAnfEffDiam
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetAnfEffDiam(Graph, NRuns = 1, NApprox = -1)

.. note::

    This function is not yet supported.

Returns a 90-th percentile of the shortest path length distribution of a Graph (based on a NRuns runs of Approximate Neighborhood Function of approximation quality NApprox). 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NRuns*: int (input)
    Number of runs of the Approximate Neighborhood Function (ANF). Default value is 1.

- *NApprox*: int (input)
    Number of approximations. Default value is -1.

Return value:

- Double

For more info see: http://www.cs.cmu.edu/~christos/PUBLICATIONS/kdd02-anf.pdf

The following example shows how to calculate the ANF Effective Diameter for a graph
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print "Directed Graph: ANF Effective Diameter is %.2f" % (snap.GetAnfEffDiam(Graph))

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print "Undirected Graph: ANF Effective Diameter is %.2f" % (snap.GetAnfEffDiam(Graph))

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print "Network Graph: ANF Effective Diameter is %.2f" % (snap.GetAnfEffDiam(Graph))
