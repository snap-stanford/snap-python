IsWeaklyConn
''''''''''''

.. function:: IsWeaklyConn()

A graph method that tests whether a graph is weakly connected.

Parameters:

- None

Return value:

- bool
    Returns True if the graph is weakly connected, False otherwise.


The following example shows how to use :func:`IsWeaklyConn` for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    print(Graph.IsWeaklyConn())

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    print(UGraph.IsWeaklyConn())

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    print(Network.IsWeaklyConn())
