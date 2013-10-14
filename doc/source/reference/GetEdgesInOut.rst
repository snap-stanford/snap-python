GetEdgesInOut
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetEdgesInOut (Graph, NIdV, EdgesIn, EdgesOut)

.. note::

    This function is not yet supported.

Returns the number of edges between the nodes NIdV and the edges pointing outside the set NIdV.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NIdV*: a vector of node Ids (input)
    A vector of node IDs

- *EdgesIn*: int (output)
    Number of edges between the nodes NIdV

- *EdgesOut*: int (output)
    Number of edges between the nodes in NIdV and the rest of the graph

Return value:

- None

The following example shows how to calculate PageRank scores for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    G1 = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	NIdV = snap.TIntV()
	NIdV.Add(5)
    NIdV.Add(8)
    NIdV.Add(11)
    edges_in = snap.TInt(0)
    edges_out = snap.TInt(0)
    snap.GetEdgesInOut(G1, NIdV, edges_in, edges_out)
    print "EdgesIn: %s EdgesOut: %s" % (edges_in, edges_out)


    G2 = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NIdV = snap.TIntV()
    NIdV.Add(5)
    NIdV.Add(8)
    NIdV.Add(11)
    snap.GetEdgesInOut(G2, NIdV, edges_in, edges_out)
    print "EdgesIn: %s EdgesOut: %s" % (edges_in, edges_out)


    G3 = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NIdV = snap.TIntV()
    NIdV.Add(5)
    NIdV.Add(8)
    NIdV.Add(11)
    snap.GetEdgesInOut(G3, NIdV, edges_in, edges_out)
    print "EdgesIn: %s EdgesOut: %s" % (edges_in, edges_out)
