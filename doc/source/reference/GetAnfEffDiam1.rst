GetAnfEffDiam
'''''''''''''

.. function:: GetAnfEffDiam(NRuns=1, NApprox=-1)
   :noindex:

A graph method that returns a 90th percentile of the shortest path length distribution of a Graph (based on a NRuns runs of Approximate Neighborhood Function of approximation quality NApprox). 

Parameters:

- (Optional) *NRuns*: int
    Number of runs of the Approximate Neighborhood Function (ANF). Default value is 1.

- (Optional) *NApprox*: int
    Number of approximations. Default value is -1.

Return value:

- float
    the given 90th of the shortest path length distribution.

For more info see: http://www.cs.cmu.edu/~christos/PUBLICATIONS/kdd02-anf.pdf

The following example shows how to calculate the ANF Effective Diameter for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    print(Graph.GetAnfEffDiam())

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    print(UGraph.GetAnfEffDiam())

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    print(Network.GetAnfEffDiam())
