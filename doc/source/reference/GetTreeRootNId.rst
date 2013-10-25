GetTreeRootNId
'''''''''''''''


.. function:: GetTreeRootNId(Graph)

If *Graph* is a tree, the function returns the root id of the tree. Otherwise, it returns -1.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network


Return value:

- int: 
    If *Graph* is a tree, the node id of the root. Otherwise, -1 is returned.


The following example shows how to get the root node id in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap


    # Directed Graph
    Graph = snap.GenTree(snap.PNGraph, 3, 3)
    root_id = snap.GetTreeRootNId(Graph)
    print "The graph has a root id: %d" % root_id


    # Undirected Graph
    Graph = snap.GenTree(snap.PUNGraph, 3, 3)
    root_id = snap.GetTreeRootNId(Graph)
    print "The graph has a root id: %d" % root_id


    # Network
    Graph = snap.GenTree(snap.PNEANet, 3, 3)
    root_id = snap.GetTreeRootNId(Graph)
    print "The graph has a root id: %d" % root_id
    