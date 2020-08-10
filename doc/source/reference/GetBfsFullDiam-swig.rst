GetBfsFullDiam (SWIG)
'''''''''''''''''''''

.. function:: GetBfsFullDiam (Graph, NTestNodes, IsDir=false)

Computes the diameter, or 'longest shortest path', of a *Graph* by performing a breadth first search over the *Graph*. This diameter is approximate, as it is calculated with an *NTestNodes* number of random starting nodes.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NTestNodes*: int (input)
    Number of starting test nodes.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

Return value:

- int
    Approximate diameter of the graph.

For more info see: http://mathworld.wolfram.com/GraphDiameter.html


The following example shows how to calculate diameters for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    diam = snap.GetBfsFullDiam(Graph, 100, False)
    print(diam)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    diam = snap.GetBfsFullDiam(UGraph, 100, False)
    print(diam)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    diam = snap.GetBfsFullDiam(Network, 100, False)
    print(diam)
