GetClosenessCentr
'''''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetClosenessCentr(Graph, NId)

.. note::

    This function is not yet supported.


Returns Closeness centrality of a given node specified by NId parameter. Closeness centrality of a node is defined as 1/FarnessCentrality.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NId*: int (input)
    Valid Node ID in Graph

Return value:

- Closeness centrality as a float value

For more info about Farness Centrality see :func:'GetFarnessCentr'

The following example shows how to get the Closeness Centrality for a node in
:class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    ctr = snap.GetClosenessCentr(Graph, 5)
    print ctr
