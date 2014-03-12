GenBaraHierar
'''''''''''''

.. function:: GenBaraHierar(GraphType, Levels, IsDir=True)

Generates a Ravasz-Barabasi deterministic scale-free graph.

Corners of the graph are recursively expanded with miniature copies of the base graph (below). The graph has power-law degree distribution with the exponent 1+ln(5)/ln(4) and clustering coefficient with power-law decay exponent -1. Base graph::

  o---o
  |\ /|
  | o |
  |/ \|
  o---o

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *Levels*: int (input)
    The number of expansions of the base graph. 

- *IsDir*: boolean (input)
    Indicates whether the edges should be directed or undirected. Defaults to directed. 

Return value:

- graph
    A Snap.py graph of the specified type.

For more information see: Hierarchical organization in complex networks. Ravasz and Barabasi. http://arxiv.org/abs/cond-mat/0206130


The following example shows how to generate a Ravasz-Barabasi deterministic scale-free graph (in this case of level 100) using the :func:`GenBaraHierar` for classes :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::
    
    import snap

    Graph = snap.GenBaraHierar(snap.PNGraph, 3, True)
    for EI in Graph.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
    
    UGraph = snap.GenBaraHierar(snap.PUNGraph, 3, True)
    for EI in UGraph.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())


    Network = snap.GenBaraHierar(snap.PNEANet, 3, True)
    for EI in Network.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
