IsWeaklyConn
''''''''''''

.. function:: IsWeaklyConn(Graph)

Tests whether *Graph* is weakly connected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- boolean:
    Returns True if the *Graph* is weakly connected, False otherwise

The following example shows how to use :func:`IsWeaklyConn` for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print snap.IsWeaklyConn(Graph)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print snap.IsWeaklyConn(Graph)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print snap.IsWeaklyConn(Graph)
