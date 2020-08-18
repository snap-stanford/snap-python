GetClustCf
''''''''''

.. function:: GetClustCf (CCfByDeg=False, SampleNodes=-1)

Computes the average clustering coefficient as defined in Watts and Strogatz, Collective dynamics of 'small-world' networks

Parameters:

- (optional) *CCfByDeg*: bool
    If *CCfByDeg* is true, then return a vector of (degree, avg. clustering coefficient of nodes of that degree) pairs in addition to the clustering coefficient.

- (optional) *SampleNodes*: int
    If !=-1 then compute clustering coefficient only for a random sample of SampleNodes nodes. Useful for approximate but quick computations.

Return value: 

- float
    The clustering coefficient for *Graph*.

- (optional) :class:`TFltPrV`
    A vector of (degree, avg. clustering coefficient of nodes of that degree) pairs.

For more info see: http://en.wikipedia.org/wiki/Clustering_coefficient

The following example shows how to calculate the average clustering coefficient in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    GraphClustCoeff = Graph.GetClustCf (-1)
    print("Clustering coefficient: %f" % GraphClustCoeff)
    Cf, CfVec = Graph.GetClustCf(True, -1)
    print("Average Clustering Coefficient: %f" % (Cf))
    print("Coefficients by degree:\n")
    for pair in CfVec:
        print("degree: %d, clustering coefficient: %f" % (pair.GetVal1(), pair.GetVal2()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    GraphClustCoeff = UGraph.GetClustCf (-1)
    print("Clustering coefficient: %f" % GraphClustCoeff)
    Cf, CfVec = UGraph.GetClustCf(True, -1)
    print("Average Clustering Coefficient: %f" % (Cf))
    print("Coefficients by degree:\n")
    for pair in CfVec:
        print("degree: %d, clustering coefficient: %f" % (pair.GetVal1(), pair.GetVal2()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    GraphClustCoeff = Network.GetClustCf (-1)
    print("Clustering coefficient: %f" % GraphClustCoeff)
    Cf, CfVec = Network.GetClustCf(True, -1)
    print("Average Clustering Coefficient: %f" % (Cf))
    print("Coefficients by degree:\n")
    for pair in CfVec:
        print("degree: %d, clustering coefficient: %f" % (pair.GetVal1(), pair.GetVal2()))