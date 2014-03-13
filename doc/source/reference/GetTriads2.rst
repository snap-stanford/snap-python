GetTriads
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetTriads (Graph, ClosedTriadsX, OpenTriadsX, SampleNodes)

.. note::

    This function is not yet supported.

Computes the number of open and closed triads for every node in *Graph*. Considers the graph as undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *ClosedTriadsX*: int (output)
    The number of closed triads.

- *OpenTriadsX*: int (output)
    The number of open triads.

- *SampleNodes*: integer (input)
    If !=-1 then compute triads only for a random sample of SampleNodes nodes. Useful for approximate but quick computations.

Return value:

- None

The following example shows how to compute the number of open and closed triads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.GetTriads(Graph)