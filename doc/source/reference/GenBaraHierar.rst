GenBaraHierar
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GenBaraHierar(Levels, IsDir)

Generates a Ravasz-Barabasi deterministic scale-free graph.

Corners of the graph are recursively expanded with miniature copies of the base graph (below). The graph has power-law degree distribution with the exponent 1+ln(5)/ln(4) and clustering coefficient with power-law decay exponent -1. Base graph::

  *   o---o
  *   |\ /|
  *   | o |
  *   |/ \|
  *   o---o
  * 

Parameters:

- *Levels*: int (input)
    The number of expansions of the base graph. 

- *IsDir*: bool (input)
    if false: ignore edge directions and consider edges/paths as undirected.

Return value:

- *GraphPt*: PGraph 
    A newly created Ravasz-Barabasi Snap.py graph with the expansion level equal to *Levels*

For more information see: Hierarchical organization in complex networks. Ravasz and Barabasi. http://arxiv.org/abs/cond-mat/0206130

The following example shows how to generate a Ravasz-Barabasi deterministic scale-free graph (in this case of level 100) using the GenBaraHierar function::

    
    import snap

    G1 = snap.GenBaraHierar(100, False)

    for NI in G1.Nodes():
        for Id in NI.GetOutEdges():
            print "edge (%d %d)" % (NI.GetId(), Id)
