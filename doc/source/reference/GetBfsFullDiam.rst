GetBfsFullDiam
''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetBfsFullDiam (Graph, NTestNodes, IsDir=false)

Computes the diameter, or 'longest shortest path', of a *Graph* by performing a breadth first search over the *Graph*. This diameter is approximate, as it is calculated with an *NTestNodes* number of random starting nodes.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NTestNodes*: int (input)
    Number of starting test nodes

- *IsDir*: bool (input)
    Set to false if edges are to be treated as undirected

Return value:

- *Diameter*: int (output)
    Approximate diameter of the graph

For more info see: http://mathworld.wolfram.com/GraphDiameter.html

The following example shows how to calculate diameters for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    G = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    diam = snap.GetBfsFullDiam(G, 100, False)
    print diam

    G = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    diam = snap.GetBfsFullDiam(G, 100, True)
    print diam

    G = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    diam = snap.GetBfsFullDiam(G, 100, False)
    print diam

    G = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    diam = snap.GetBfsFullDiam(G, 100, True)
    print diam

    G = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    diam = snap.GetBfsFullDiam(G, 100, False)
    print diam

    G = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    diam = snap.GetBfsFullDiam(G, 100, True)
    print diam
