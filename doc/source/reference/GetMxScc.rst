GetMxSccs
'''''''''

.. function:: GetMxSccs (Graph)

Returns a graph representing the largest strongly connected component in ＊Graph＊.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- graph
    A Snap.py graph or a network representing the largest strongly connected component in ＊Graph＊.


The following example shows how to get the largest strongly connected component in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap


    # Directed Graph
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 500)
    PGraph = snap.GetMxScc(Graph)
    for edge in PGraph.Edges():
      print "(%d, %d)" % (edge.GetSrcNId(), edge.GetDstNId())
    

    # Undirected Graph
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 500)
    PGraph = snap.GetMxScc(Graph)
    for edge in PGraph.Edges():
      print "(%d, %d)" % (edge.GetSrcNId(), edge.GetDstNId())


    # Network
    Graph = snap.GenRndGnm(snap.PNEANet, 100, 500)
    PGraph = snap.GetMxScc(Graph)
    for edge in PGraph.Edges():
      print "(%d, %d)" % (edge.GetSrcNId(), edge.GetDstNId())

