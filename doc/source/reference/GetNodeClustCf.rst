GetNodeClustCf
''''''''''''''

.. function:: GetNodeClustCf(NId) 

A graph method that returns clustering coefficient of a particular node. Considers the graph as undirected.

Parameters:

- *NId*: int
    A node id in the *Graph*.

Return value:

- float
    Clustering coefficient of a particular node.


The following example shows how to calculate clustering coefficient of a particular node in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Graph.GetNodeClustCf(50)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    UGraph.GetNodeClustCf(50)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Network.GetNodeClustCf(50)
