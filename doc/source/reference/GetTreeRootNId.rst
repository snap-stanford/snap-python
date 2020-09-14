GetTreeRootNId
'''''''''''''''

.. function:: GetTreeRootNId()

A graph method for directed graphs that returns the root id of the tree, if a graph is a tree. Otherwise, it returns -1.

Parameters:

- None

Return value:

- int 
    If the graph is a tree, the node id of the root. Otherwise, -1 is returned.


The following example shows how to get the root node id in
:class:`TNGraph` and :class:`TNEANet`::

    import snap

    Graph = snap.GenTree(snap.TNGraph, 3, 3)
    root_id = Graph.GetTreeRootNId()
    print("The graph has a root id: %d" % root_id)

    Network = snap.GenTree(snap.TNEANet, 3, 3)
    root_id = Network.GetTreeRootNId()
    print("The graph has a root id: %d" % root_id)
