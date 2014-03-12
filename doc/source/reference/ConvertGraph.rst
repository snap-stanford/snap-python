ConvertGraph
''''''''''''

.. function:: ConvertGraph(GraphType, InGraph, RenumberNodes=false)

Converts *InGraph* to a graph of type *GraphType* with an optional node renumbering. The resulting graph will have type *GraphType*. Node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *InGraph*: graph (input)
    A Snap.py graph or network.

- *RenumberNodes*: boolean (input)
    Determines whether the node IDs are preserved or not. If False, then nodes in the resulting graph have the same node IDs as nodes in *InGraph*. If True, then nodes in the resulting graph are renumbered sequentially from 0 to N-1, where N is the number of nodes. By default, the nodes are not renumbered.

Return value:

- graph
    A snap.py graph of type *GraphType* converted from the original graph *InGraph*.


The following example shows how to convert between different types of graphs::

    import snap

    GIn = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    # convert directed graph to undirected
    GOut = snap.ConvertGraph(snap.PUNGraph, GIn)

    GIn = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    # convert undirected graph to directed
    GOut = snap.ConvertGraph(snap.PNGraph, GIn)

    GIn = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    # convert directed graph to a network
    GOut = snap.ConvertGraph(snap.PNEANet, GIn)
