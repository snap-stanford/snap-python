GetESubGraph
''''''''''''

.. function:: GetESubGraph(EIdV)

A graph method for that returns a subgraph of the original graph, which contains all the edges from the original graph with edge ids in *EIdV* and all the nodes that are connected by at least one edge in *EIdV*. Nodes and edges in the resulting subgraph have the same ids as in the original graph. This method is only implemented for :class:`TNEANet`.

Parameters:

- *EIdV*: Python list or :class:`TIntV`, a vector of ints (input)
    A vector of edge ids in graph.

Return value:

- network
    A network, which is a subgraph of the original graph with *EIdV* edges.


The following example shows how to use :func:`GetESubGraph` with
:class:`TNEANet`::

    import snap

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    EIdV = []
    for EI in Network.Edges():
        EIdV.append(EI.GetId())
    ESubGraph = Network.GetESubGraph(EIdV)
