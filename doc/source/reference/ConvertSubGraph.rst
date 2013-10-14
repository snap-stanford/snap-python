ConvertSubGraph
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: ConvertSubGraph(Graph, NIdV, RenumberNodes = False)

Returns an induced subgraph of graph InGraph with NIdV nodes with an optional node renumbering.

Creates a subgraph of the input graph InGraph on NIdV nodes and returns an output graph. Input and output graphs can have different types. Node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NIdV*: int (input)
    Number of nodes to return

- *RenumberNodes*: Boolean (input)
    Determines whether the node IDs are preserved or not. If RenumberNodes is false, then nodes in the resulting graph have the same node IDs as nodes in InGraph. If RenumberNodes is true, then nodes in the resulting graph are renumbered sequentially from 0 to N-1. By default, the nodes are not renumbered.

Return value:

- *Graph*: graph (input)
    A Snap.py graph or a network
    
The following example shows how to convert a SubGraph in
:class:`TNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    G1 = snap.ConvertSubGraph(Graph,10)
  
