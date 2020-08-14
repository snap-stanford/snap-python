GetBfsFullDiam
''''''''''''''

.. function:: GetBfsFullDiam (NTestNodes, IsDir=false)

A graph method that computes the diameter, or 'longest shortest path', of a graph by performing a breadth first search. This diameter is approximate, as it is calculated with an *NTestNodes* number of random starting nodes.

Parameters:

- *NTestNodes*: int
    Number of starting test nodes.

- *IsDir*: bool
    Indicates whether the edges should be considered directed or undirected.

Return value:

- int
    Approximate diameter of the graph.

For more info see: http://mathworld.wolfram.com/GraphDiameter.html


The following example shows how to calculate diameters for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    diam = Graph.GetBfsFullDiam(100, False)
    print(diam)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    diam = UGraph.GetBfsFullDiam(100, False)
    print(diam)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    diam = Network.GetBfsFullDiam(100, False)
    print(diam)
