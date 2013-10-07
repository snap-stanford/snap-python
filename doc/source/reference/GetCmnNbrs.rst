GetCmnNbrs
'''''''''''

.. function:: GetCmnNbrs(Graph, NId1, NId2)

Returns a number of shared neighbors between a pair of nodes *NId1* and *NId2*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NId1*: int (input)
    Id of the first node

- *NId2*: int (input)
    Id of the second node

Return value:

- int

The following example shows how to calculate number of neighbors for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.GetCmnNbrs(1,10)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.GetCmnNbrs(1,10)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.GetCmnNbrs(1,10)