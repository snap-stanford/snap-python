ConvertGraph
''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: PNGraph ConvertGraph(toutspec, tinspec, InGraph, RenumberNodes=False)

Performs conversion of graph, *InGraph*, with an optional node renumbering.

Takes an input graph *InGraph* and returns an output graph.
Input and output graphs can have different types.
Node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *toutspec*: graph class (input)
    Class of output graph -- one of `PNGraph`, `PNEANet`, or `PUNGraph`

- *tinspec*: graph class (input)
    Class of input graph -- one of `PNGraph`, `PNEANet`, or `PUNGraph`

- *InGraph*: graph (input)
    A Snap.py graph or a network

- *RenumberNodes*: boolean (input)
    Indicates whether the node IDs are preserved or not.
    If RenumberNodes is false, then nodes in the resulting graph have the same node IDs as nodes in InGraph.
    If RenumberNodes is true, then nodes in the resulting graph are renumbered sequentially from 0 to N-1.
    By default, the nodes are not renumbered.

Return value:

- The converted version of the input graph.

The following example shows how to convert between different types of graphs::

    import snap

    GIn = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    # convert directed graph to undirected
    GOut = snap.ConvertGraph(snap.PUNGraph, GIn)

    GIn = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    # convert undirected graph to directed
    GOut = snap.ConvertGraph(snap.PNGraph, GIn)
