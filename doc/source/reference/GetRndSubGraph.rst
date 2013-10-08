GetRndSubGraph
''''''''''''''

.. function:: GetRndSubGraph(Graph, numNodes)

Randomly selects numNodes nodes from the input graph and returns an induced graph on those nodes.
Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *numNodes*: int (input)
    Number of nodes desired in the output graph

Return value:

- *Graph*: the induced sub-graph

The following example shows how to get a random subgraph of size 10 in a graph of type
:class:`TNGraph`, :class:`TUNGraph`, or :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    subGraph = snap.GetRndSubGraph(Graph,10)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    subGraph = snap.GetRndSubGraph(Graph,10)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    subGraph = snap.GetRndSubGraph(Graph,10)

