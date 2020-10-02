GetLen2Path (SWIG)
''''''''''''''''''

.. function:: GetLen2Paths (Graph, NId1, NId2)
   :noindex:

Returns the number of length 2 directed paths between a pair of nodes *NId1*, *NId2* (*NId1* --> U --> *NId2*).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NId1*: int (input)
    ID of first node.

- *NId1*: int (input)
    ID of second node.

Return value:

- int: the number of length 2 paths between *NId1* and *NId2*.

The following example shows how to calculate the number of length 2 directed paths between nodes within a :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 3000)
    NumLen2Paths = snap.GetLen2Paths(Graph, 0, 1)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 3000)
    NumLen2Paths = snap.GetLen2Paths(Graph, 0, 1)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 3000)
    NumLen2Paths = snap.GetLen2Paths(Graph, 0, 1)

