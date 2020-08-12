IsConnected
'''''''''''

.. function:: IsConnected()

A graph method that tests whether a graph is connected.

Parameters:

- None

Return value:

- bool
    Returns True if the graph is connected, False otherwise.

The following example shows how to use :func:`IsConnected` for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print(Graph.IsConnected())

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print(UGraph.IsConnected())

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print(Network.IsConnected())
