GetClustCfAll (SWIG)
''''''''''''''''''''

.. function:: GetClustCfAll (Graph, DegToCCfV, SampleNodes=-1)
   :noindex:

Computes the average clustering coefficient, as well as the number of open and closed triads in the graph, as defined in Watts and Strogatz, Collective dynamics of 'small-world' networks. 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCCfV*: a vector of pairs of floats (output)
    The vector of pairs (degree, avg. clustering coefficient of nodes of that degree)

- *SampleNodes*: int (input)
    If !=-1 then compute clustering coefficient only for a random sample of SampleNodes nodes

Return value:

- list: [float, int, int]
    The list contains three elements: the average clustering coefficient,
    the number of closed triads, and the number of open triads in the graph.

For more info see: http://en.wikipedia.org/wiki/Watts_and_Strogatz_model

The following example shows how to compute the in degree for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DegToCCfV = snap.TFltPrV()
    result = snap.GetClustCfAll(Graph, DegToCCfV)
    for item in DegToCCfV:
        print("degree: %d, clustering coefficient: %f" % (item.GetVal1(), item.GetVal2()))
    print("average clustering coefficient", result[0])
    print("closed triads", result[1])
    print("open triads", result[2])

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DegToCCfV = snap.TFltPrV()
    result = snap.GetClustCfAll(Graph, DegToCCfV)
    for item in DegToCCfV:
        print("degree: %d, clustering coefficient: %f" % (item.GetVal1(), item.GetVal2()))
    print("average clustering coefficient", result[0])
    print("closed triads", result[1])
    print("open triads", result[2])

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DegToCCfV = snap.TFltPrV()
    result = snap.GetClustCfAll(Graph, DegToCCfV)
    for item in DegToCCfV:
        print("degree: %d, clustering coefficient: %f" % (item.GetVal1(), item.GetVal2()))
    print("average clustering coefficient", result[0])
    print("closed triads", result[1])
    print("open triads", result[2])

