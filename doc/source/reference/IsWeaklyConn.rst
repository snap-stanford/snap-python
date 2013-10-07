IsWeaklyConn
'''''''''''

.. function:: IsWeaklyConn(Graph)

Tests whether *Graph* is weakly connected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or network

Return value:

- Boolean indicating whether the graph is weakly connected.

The following example shows how to use this function for 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    if snap.IsWeaklyConn(Graph): print "Graph is weakly connected"

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    if snap.IsWeaklyConn(Graph): print "Graph is weakly connected"

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    if snap.IsWeaklyConn(Graph): print "Graph is weakly connected"