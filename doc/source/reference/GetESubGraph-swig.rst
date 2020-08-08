GetESubGraph (SWIG)
'''''''''''''''''''

.. function:: GetESubGraph(Graph, EIdV)

Returns a subgraph of graph *Graph*. The resulting subgraph contains all the edges from *Graph* with edge IDs in *EIdV* and all the nodes that are connected by at least one edge in *EIdV*. Nodes and edges in the resulting subgraph have the same IDs as in *Graph*.

Parameters:

- *Graph*: network (input)
    A Snap.py network.

- *EIdV*: :class:`TIntV`, a vector of ints (input)
    A vector of edge IDs in graph.

Return value:

- network
    A Snap.py network, which is a subgraph of *Graph* with *EIdV* edges.


The following example shows how to use :func:`GetESubGraph` with
:class:`TNEANet`::

    import snap

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    EIdV = snap.TIntV()
    for EI in Network.Edges():
        EIdV.Add(EI.GetId())
    ESubGraph = snap.GetESubGraph(Network, EIdV)
