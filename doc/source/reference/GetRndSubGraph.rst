GetRndSubGraph
''''''''''''''

.. function:: GetRndSubGraph(Graph, numNodes)

Randomly selects *numNodes* nodes from the input graph and returns an induced graph on those nodes.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *numNodes*: int (input)
    Number of nodes desired in the output graph.

Return value:

- graph
    The induced sub-graph.


The following example shows how to get a random subgraph of size 10 from a graph of type
:class:`TNGraph`, :class:`TUNGraph`, or :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    SubGraph = snap.GetRndSubGraph(Graph,10)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    SubUGraph = snap.GetRndSubGraph(UGraph,10)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    SubNetwork = snap.GetRndSubGraph(Network,10)

