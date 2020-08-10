ConvertGraph
''''''''''''

.. function:: ConvertGraph(GraphType, RenumberNodes=False)

A graph method that converts a graph to a graph of type *GraphType* with an optional node renumbering. The resulting graph will have type *GraphType*. Any node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *GraphType*: graph class
    Class of output graph -- one of PNGraph, PUNGraph or PNEANet.

- (optional) *RenumberNodes*: bool
    Determines whether the node ids are preserved or not. If False, then nodes in the resulting graph have the same node ids as nodes in the original graph. If True, then nodes in the resulting graph are renumbered sequentially from 0 to N-1, where N is the number of nodes. By default, the nodes are not renumbered.

Return value:

- graph
    A graph of type *GraphType* converted from the original graph.


The following example shows how to convert between :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` types of graphs::

    import snap

    GIn = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    # convert directed graph to undirected
    GOut = GIn.ConvertGraph(snap.PUNGraph)

    GIn = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    # convert undirected graph to directed
    GOut = GIn.ConvertGraph(snap.PNGraph)

    GIn = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    # convert directed graph to a network
    GOut = GIn.ConvertGraph(snap.PNEANet)
