GetBfsEffDiam
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetBfsEffDiam(Graph, NTestNodes, IsDir, EffDiam, FullDiam)

.. note::

    This function is not yet supported.

Returns the (approximation of the) Effective Diameter and the Diameter of Graph by performing BFS from NTestNodes starting nodes.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NTestNodes*: int (input)
    The number of random start nodes to use in the BFS used to calculate the graph diameter and effective diameter.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

- *EffDiam: float* (output)
    The computed effective diameter will be stored in EffDiam.

- FullDiam: float (output)
    The computed full diameter will be stored in FullDiam.

Return value:

- float
    The effective diameter of the graph (same value as EffDiam)

The following example shows how to fetch the in-degrees for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NTestNodes = 1
    IsDir = True
    EffDiam = 0
    FullDiam = 0
    snap.GetBfsEffDiam(Graph, NTestNodes, IsDir, EffDiam, FullDiam)
    print("Effective Diameter = %f" % EffDiam)
    print("Full Diameter = %f" % FullDiam)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NTestNodes = 1
    IsDir = False
    EffDiam = 0
    FullDiam = 0
    snap.GetBfsEffDiam(Graph, NTestNodes, IsDir, EffDiam, FullDiam)
    print("Effective Diameter = %f" % EffDiam)
    print("Full Diameter = %f" % FullDiam)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NTestNodes = 1
    IsDir = False
    EffDiam = 0
    FullDiam = 0
    snap.GetBfsEffDiam(Graph, NTestNodes, IsDir, EffDiam, FullDiam)
    print("Effective Diameter = %f" % EffDiam)
    print("Full Diameter = %f" % FullDiam)
