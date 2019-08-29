IsConnected
'''''''''''

.. function:: IsConnected(Graph)

Tests whether *Graph* is (weakly) connected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

Return value:

- bool
    Returns True if the *Graph* is (weakly) connected, False otherwise.

The following example shows how to use :func:`IsConnected` for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print(snap.IsConnected(Graph))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print(snap.IsConnected(UGraph))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print(snap.IsConnected(Network))
