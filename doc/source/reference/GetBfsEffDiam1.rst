GetBfsEffDiam
'''''''''''''

.. function:: GetBfsEffDiam(NTestNodes, SubGraphNIdV, IsDir)
   :noindex:

A graph method that uses the entire graph (all edges) to measure the shortest path lengths but reports only the path lengths between nodes in *SubGraphNIdV*.

Parameters:

- *NTestNodes*: int
    Number of starting nodes for calculating path lengths.

- *SubGraphNIdV*: Python list or TIntV - vector of ints
    List of nodes in the subgraph for which the path lengths will be reported.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

Return value:

- list: [float, float, int]
    The list contains three elements: the first and the second element are
    the 90th-percentile approximation for the average shortest path length
    among the nodes in SubGraphNIdV, the third element is the diameter.

Notes:

- There is another version of GetBfsEffDiam with different parameters. 


The following example shows how to calculate the average shortest path length
for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Num = 50
    Nodes = [ 1, 4, 9, 16, 25, 36 ]
    Result = Graph.GetBfsEffDiam(Num, Nodes, True)
    print(Result)

    Graph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Num = 75
    Nodes = [ 1, 4, 9, 16, 25, 36 ]
    Result = Graph.GetBfsEffDiam(Num, Nodes, False)
    print(Result)

    Graph = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Num = 33
    Nodes = [ 1, 4, 9, 16, 25, 36 ]
    Result = Graph.GetBfsEffDiam(Num, Nodes, True)
    print(Result)

