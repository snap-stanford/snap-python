GetClustCfAll
'''''''''''''

.. function:: GetClustCfAll (SampleNodes=-1)

A graph method that computes the average clustering coefficient, as well as the number of open and closed triads in the graph, as defined in Watts and Strogatz, Collective dynamics of 'small-world' networks. 

Parameters:

- (optional) *SampleNodes*: int
    If *SampleNodes* is -1 (default value), then compute the clustering coefficient over all the nodes. Otherwise, compute the clustering coefficient using only a random sample of *SampleNodes* nodes.

Return value:

- list: [float, int, int]
    The list contains three elements: the average clustering coefficient,
    the number of closed triads, and the number of open triads in the graph.

- :class:`TFltPrV`
    The vector of pairs (degree, avg. clustering coefficient of nodes of that degree)

For more info see: http://en.wikipedia.org/wiki/Watts_and_Strogatz_model

The following example shows how to compute the in degree for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    result, DegToCCfV = Graph.GetClustCfAll()
    for item in DegToCCfV:
        print("degree: %d, clustering coefficient: %f" % (item.GetVal1(), item.GetVal2()))
    print("average clustering coefficient", result[0])
    print("closed triads", result[1])
    print("open triads", result[2])

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    result, DegToCCfV = Graph.GetClustCfAll()
    for item in DegToCCfV:
        print("degree: %d, clustering coefficient: %f" % (item.GetVal1(), item.GetVal2()))
    print("average clustering coefficient", result[0])
    print("closed triads", result[1])
    print("open triads", result[2])

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    result, DegToCCfV = Graph.GetClustCfAll()
    for item in DegToCCfV:
        print("degree: %d, clustering coefficient: %f" % (item.GetVal1(), item.GetVal2()))
    print("average clustering coefficient", result[0])
    print("closed triads", result[1])
    print("open triads", result[2])

