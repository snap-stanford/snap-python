GetRndESubGraph
'''''''''''''''

.. function:: GetRndESubGraph(Graph, numEdges)

Randomly selects *numEdges* nodes from the input graph and returns an induced graph on those nodes.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *numEdges*: int (input)
    Number of edges desired in the output graph

Return value:

- graph
    The induced sub-graph

The following example shows how to get a random subgraph with 10 edges from a graph of type
:class:`TNGraph`, :class:`TUNGraph`, or :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    subGraph = snap.GetRndESubGraph(Graph, 10)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    subGraph = snap.GetRndESubGraph(Graph, 10)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    subGraph = snap.GetRndESubGraph(Graph, 10)
