GetDegCnt
'''''''''''''''

.. function:: GetDegCnt(Graph, DegToCntV)

Returns a degree histogram: a set of pairs *(degree, number of nodes of such degree)*

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCntV*: TFltPrV (output)
    The degree histogram as a vector of float pairs

Return Value:

- None

For more info see http://en.wikipedia.org/wiki/Degree_distribution

The following examples shows how to obtain the degree histogram for networks of class :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

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