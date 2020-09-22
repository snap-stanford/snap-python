GetRndESubGraph
'''''''''''''''

.. function:: GetRndESubGraph(numEdges)

A graph method that randomly selects *numEdges* edges from the original graph and returns a subgraph on those edges.

Parameters:

- *numEdges*: int
    Number of edges desired in the output graph.

Return value:

- graph
    The induced sub-graph.


The following example shows how to get a random subgraph with 10 edges from a graph of type
:class:`TNGraph`, :class:`TUNGraph`, or :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    SubGraph = Graph.GetRndESubGraph(10)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    SubUGraph = UGraph.GetRndESubGraph(10)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    SubNetwork = Network.GetRndESubGraph(10)
