GetRndSubGraph
''''''''''''''

.. function:: GetRndSubGraph(numNodes)

A graph method that randomly selects *numNodes* nodes from the input graph and returns an induced graph on those nodes.

Parameters:

- *numNodes*: int
    Number of nodes desired in the output graph.

Return value:

- graph
    The induced sub-graph.


The following example shows how to get a random subgraph of size 10 from a graph of type
:class:`TNGraph`, :class:`TUNGraph`, or :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    SubGraph = Graph.GetRndSubGraph(10)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    SubUGraph = UGraph.GetRndSubGraph(10)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    SubNetwork = Network.GetRndSubGraph(10)

