GetMxInDegNId
'''''''''''''

.. function:: int  GetMxInDegNId(Graph)

Returns a randomly chosen node from all the nodes in *Graph* with the maximum in-degree.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- A randomly chosen node from all the nodes in *Graph* with the maximum in-degree

The following example shows how to use :func:`GetMxInDegNId` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.GetMxInDegNId(Graph)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.GetMxInDegNId(Graph)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.GetMxInDegNId(Graph)
