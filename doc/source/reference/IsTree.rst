IsTree
''''''


.. function:: IsTree(Graph)

Determines if *Graph* is a connected tree. The function returns a (boolean, int) pair, where the boolean indicates whether *Graph* is a tree and the int is the node id for the root of the tree.

Parameters:

- *Graph*: directed graph (input) 
    A Snap.py directed graph or a network


Return value: 

- bool: 
    Indicates whether *Graph* is a tree

- int:
    The node id for the root of the tree


The following example shows how to detect trees in 
:class:`TNGraph` and :class:`TNEANet`::

    import snap

    # Directed Graph
    Graph = snap.GenTree(snap.PNGraph, 3, 3)
    (is_tree, root_id) = snap.IsTree(Graph)
    print "The graph is a tree: %s " % is_tree
    print "The graph has a root id: %d" % root_id

    # Network
    Graph = snap.GenTree(snap.PNEANet, 3, 3)
    (is_tree, root_id) = snap.IsTree(Graph)
    print "The graph is a tree: %s " % is_tree
    print "The graph has a root id: %d" % root_id
