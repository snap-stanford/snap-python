GetDegCnt
'''''''''''''''


.. function:: GetDegCnt(Graph, DegToCntV)

Computes a degree histogram: a vector of pairs (degree, number of nodes of such degree). The results are stored in *DegToCntV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCntV*: TFltPrV, a vector of (float, float) pairs (output)
    A vector of (degree, number of nodes of such degree) pairs.

Return Value:

- None

For more info see http://en.wikipedia.org/wiki/Degree_distribution

The following examples shows how to obtain the degree histogram for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    result = snap.TFltPrV()
    snap.GetDegCnt(Graph, result)
    for x in result:
      print "There are %s nodes with degree %s" % (x.GetVal2(), x.GetVal1())

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    result = snap.TFltPrV()
    snap.GetDegCnt(Graph, result)
    for x in result:
      print "There are %s nodes with degree %s" % (x.GetVal2(), x.GetVal1())

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    result = snap.TFltPrV()
    snap.GetDegCnt(Graph, result)
    for x in result:
      print "There are %s nodes with degree %s" % (x.GetVal2(), x.GetVal1())