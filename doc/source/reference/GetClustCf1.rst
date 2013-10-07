GetClustCf
'''''''''''

.. function:: AvgClustCf = GetClustCf(Graph, DegToCCfV, SampleNodes = -1)

Computes the distribution of average clustering coefficient.

Considers the graph as undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCCfV*: Vector of pairs (int,float) (output)
    Degree, avg. clustering coefficient of nodes of that degree.

- *SampleNodes*: int (input)
    If !=-1 then compute clustering coefficient only for a random sample of SampleNodes nodes. 
    Useful for approximate but quick computations.

Return value:

- *AvgClustCf*: float (output)
    Average clustering coefficient over all node degrees

The following example shows how to compute the clustering coefficient distribution in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    CfVec = snap.TFltPrV()
    Cf = GetClustCf(Graph, CfVec, -1)
    print "Average Clustering Coefficient: %f" % (Cf)
    print "Coefficients by degree:\n"
    for pair in CfVec:
        print "degree: %d, clustering coefficient: %f" % (pair.GetVal1(), pair.GetVal2())
    
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    CfVec = snap.TFltPrV()
    Cf = GetClustCf(Graph, CfVec, -1)
    print "Average Clustering Coefficient: %f" % (Cf)
    print "Coefficients by degree:\n"
    for pair in CfVec:
        print "degree: %d, clustering coefficient: %f" % (pair.GetVal1(), pair.GetVal2())
    
    Graph = snap.GenRndGnm(snap.PNEANetGraph, 100, 1000)
    CfVec = snap.TFltPrV()
    Cf = GetClustCf(Graph, CfVec, -1)
    print "Average Clustering Coefficient: %f" % (Cf)
    print "Coefficients by degree:\n"
    for pair in CfVec:
        print "degree: %d, clustering coefficient: %f" % (pair.GetVal1(), pair.GetVal2())