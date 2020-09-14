GetBfsEffDiam
'''''''''''''

.. function:: GetBfsEffDiam(Graph, NTestNodes, SubGraphNIdV, IsDir)

Uses the entire graph (all edges) to measure the shortest path lengths but reports only the path lengths between nodes in SubGraphNIdV.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NTestNodes*: int (input)
    Number of starting nodes for calculating path lengths.

- *SubGraphNIdV*: TIntV - vector of ints (input)
    List of nodes in the subgraph for which the path lengths will be reported.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

Return value:

- list: [float, float, int]
    The list contains three elements: the first and the second element are
    the 90th-percentile approximation for the average shortest path length
    among the nodes in SubGraphNIdV, the third element is the diameter.

Notes:

- There are three other versions of GetBfsEffDiam with different parameters. 


The following example shows how to calculate the average shortest path length
for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Num = 50
    List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
    Result = snap.GetBfsEffDiam(Graph, Num, List, True)
    print(Result)

    Graph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Num = 75
    List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
    Result = snap.GetBfsEffDiam(Graph, Num, List, False)
    print(Result)

    Graph = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Num = 33
    List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
    Result = snap.GetBfsEffDiam(Graph, Num, List, True)
    print(Result)

