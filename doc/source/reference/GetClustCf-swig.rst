GetClustCf (SWIG)
'''''''''''''''''

.. function:: GetClustCf (Graph, SampleNodes=-1) 

Computes the average clustering coefficient as defined in Watts and Strogatz, Collective dynamics of 'small-world' networks

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *SampleNodes*: int (input)
    If !=-1 then compute clustering coefficient only for a random sample of SampleNodes nodes. Useful for approximate but quick computations.

Return value: 

- float
    The clustering coefficient for *Graph*.

For more info see: http://en.wikipedia.org/wiki/Clustering_coefficient

The following example shows how to calculate the average clustering coefficient in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    GraphClustCoeff = snap.GetClustCf (Graph, -1)
    print("Clustering coefficient: %f" % GraphClustCoeff)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    GraphClustCoeff = snap.GetClustCf (UGraph, -1)
    print("Clustering coefficient: %f" % GraphClustCoeff)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    GraphClustCoeff = snap.GetClustCf (Network, -1)
    print("Clustering coefficient: %f" % GraphClustCoeff)


