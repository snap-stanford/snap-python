GetCmnNbrs (SWIG)
''''''''''''''''''

.. function:: GetCmnNbrs(Graph, NId1, NId2)
   :noindex:

Computes the number of shared neighbors between a pair of nodes *NId1* and *NId2*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NId1*: int (input)
    Node id of the first node.

- *NId2*: int (input)
    Node id of the second node.

Return value:

- int
    The number of common neighbors between the pair of nodes.


The following example shows how to calculate number of neighbors for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.GetCmnNbrs(Graph, 1, 10)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.GetCmnNbrs(UGraph, 1, 10)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.GetCmnNbrs(Network, 1, 10)
