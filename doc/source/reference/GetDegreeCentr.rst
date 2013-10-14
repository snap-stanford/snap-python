GetDegreeCentr
''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetDegreeCentr(Graph, NId)

Returns Degree centrality of a given node NId. Degree centrality of a node is defined as its degree/(N-1), where N is the number of nodes in the network.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NId*: int (input)
    Id of the node whose degree centrality is to be returned

Return value:

- float

The following example shows how to calculate Degree Centrality for nodes in :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for node in Graph.Nodes():
        print snap.GetDegreeCentr(Graph,node.GetId())
