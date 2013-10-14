GetTreeRootNId
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetTreeRootNId(Graph)

Returns root id of tree in graph, -1 if There is no root node.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or directed graph

Return value:

- int: Returns root id of tree in graph, -1 if There is no root node.

The following example shows how to use GetKCoreNodes for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    G = snap.LoadEdgeList(snap.PNGraph, "example.txt",0,1)
    rootNodeId = snap.GetTreeRootNId(G)
    