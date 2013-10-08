GetClustCf
'''''''''''

.. function:: GetClustCf (Graph, DegToCCfV, ClosedTriads, OpenTriads, SampleNodes=-1)

.. note::

    This functions is not yet supported.

Computes the average clustering coefficient, as well as the number of open and closed triads in the graph, as defined in Watts and Strogatz, Collective dynamics of 'small-world' networks. 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCCfV*: a vector of pairs of floats (output)
    The vector of pairs (degree, avg. clustering coefficient of nodes of that degree)

- *ClosedTriads*: int (64-bit) (output)
    The closed triads in the graph

- *OpenTriads*: int (64-bit) (output)
    The open triads in the graph

- *SampleNodes*: int (input)
    If !=-1 then compute clustering coefficient only for a random sample of SampleNodes nodes

Return value: (float)

- The average clustering coefficient

For more info see: http://en.wikipedia.org/wiki/Watts_and_Strogatz_model

The following example shows how to compute the in degree for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DegToCCfV = snap.TFltPrV()
    # There is no SNAP type for 64-bit ints, so use two argument version of function instead
    #ClosedTriads = snap.TInt()
    #OpenTriads = snap.TInt()
    #print snap.GetClustCf(Graph, DegToCCfV, ClosedTriads, OpenTriads)
    print snap.GetClustCf(Graph, DegToCCfV)
    for item in DegToCCfV:
      print item.GetVal1(), item.GetVal2()
    #print ClosedTriads
    #print OpenTriads

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DegToCCfV = snap.TFltPrV()
    # There is no SNAP type for 64-bit ints, so use two argument version of function instead
    #ClosedTriads = snap.TInt()
    #OpenTriads = snap.TInt()
    #print snap.GetClustCf(Graph, DegToCCfV, ClosedTriads, OpenTriads)
    print snap.GetClustCf(Graph, DegToCCfV)
    for item in DegToCCfV:
      print item.GetVal1(), item.GetVal2()
    #print ClosedTriads
    #print OpenTriads

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DegToCCfV = snap.TFltPrV()
    # There is no SNAP type for 64-bit ints, so use two argument version of function instead
    #ClosedTriads = snap.TInt()
    #OpenTriads = snap.TInt()
    #print snap.GetClustCf(Graph, DegToCCfV, ClosedTriads, OpenTriads)
    print snap.GetClustCf(Graph, DegToCCfV)
    for item in DegToCCfV:
      print item.GetVal1(), item.GetVal2()
    #print ClosedTriads
    #print OpenTriads
