GetNodeClustCf
''''''''''''''

.. function:: GetNodeClustCf(NId) 

Returns clustering coefficient of a particular node. Considers the graph as undirected.

Parameters:

- *NId*: int
    A node id in the *Graph*.

Return value:

- float
    Clustering coefficient of a particular node.


The following example shows how to calculate clustering coefficient of a particular node in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.GetNodeClustCf(50)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    UGraph.GetNodeClustCf(50)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Network.GetNodeClustCf(50)
