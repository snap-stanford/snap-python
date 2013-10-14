ConvertGraph
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: ConvertGraph(GraphType, InGraph, RenumberNodes = false)

Performs conversion of :class:`PGraph` InGraph to a graph of type GraphType with an optional node renumbering, and returns the new graph. 

Input graph and output graph may have different types. Node and edge data is not copied, but it is shared by input and output graphs.


Parameters:

- *GraphType*: a subclass of :class:`PGraph`
	The desired type of the output graph

- *InGraph*: :class:`PGraph`
    A Snap.py graph or a network

- *RenumberNodes*: Boolean
	If true, nodes in the output graph are renumbered sequentially from 0 to N-1. By default, this is false, and nodes retain the same node IDs as the nodes in InGraph. 


Return value:

- output graph (output)
	The InGraph converted to type GraphType


The following example shows how to use ConvertGraph::

    import snap

    graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    new_graph = snap.ConvertGraph(snap.PUNGraph, graph)

    graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    new_graph = snap.ConvertGraph(snap.PNGraph, graph, true)

    graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    new_graph = snap.ConvertGraph(snap.PNEANet, graph, true)