GetBfsEffDiam
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetBfsEffDiam(Graph, NTestNodes, SubGraphNIdV, IsDir, EffDiam, FullDiam)

.. note::

    This function is not yet supported.

Uses the entire graph (all edges) to measure the shortest path lengths but reports only the path lengths between nodes in SubGraphNIdV.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NTestNodes*: int (input)
    Number of starting nodes for calculating path lengths

- *SubGraphNIdV*: TIntV - vector of ints (input)
    List of nodes in the subgraph for which the path lengths will be reported

- *IsDir*: boolean (input)
    If false, ignores edge directions and considers edges to be undirected

- *EffDiam*: double (output)
    90-th percentile approximation of the diameter of SubGraphNIdV, equal to the average shortest path length

- *FullDiam*: int (output)
    The maximal shortest path found from the sampled nodes, used to approximate the full diameter of the graph

Return value:

- 90th-percentile approximation for the average shortest path length among the nodes in SubGraphNIdV (float)

Notes:

- This function is also known as GetBfsEffDiam4. There are three other versions of GetBfsEffDiam with different parameters. 


The following example shows how to calculate the average shortest path length for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Num = 50
    List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
    Dist = snap.GetBfsEffDiam(Graph, Num, List, True,0,0)
    print Dist

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Num = 75
    List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
    Dist = snap.GetBfsEffDiam(Graph, Num, List, False,0,0)
    print Dist

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Num = 33
    List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
    Dist = snap.GetBfsEffDiam(Graph, Num, List, True,0,0)
    print Dist
