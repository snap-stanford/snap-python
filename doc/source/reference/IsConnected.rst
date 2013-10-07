IsConnected
'''''''''''

.. function:: IsConnected(Graph)

Tests whether the *Graph* is (weakly) connected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- True: If the *Graph* is (weakly) connected
- False: If the *Graph* is not connected

The following example shows how to use IsConnected for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print snap.IsConnected(Graph)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print snap.IsConnected(Graph)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print snap.IsConnected(Graph)
