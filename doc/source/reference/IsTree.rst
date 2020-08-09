IsTree
''''''

.. function:: IsTree()

A graph method that determines if a graph is a connected tree. The function returns a list of [bool, int], where the bool indicates whether the graph is a tree and the int is the node id for the root of the tree. The method works with :class:`TNGraph` and :class:`TNEANet`.

Parameters:

- none

Return value: 

- list: [bool, int]
    The list consists of two elements: a bool that indicates whether the graph is a tree, and an int giving the node id for the root of the tree.


The following example shows how to detect trees in 
:class:`TNGraph` and :class:`TNEANet`::

    import snap

    Graph = snap.GenTree(snap.PNGraph, 3, 3)
    [is_tree, root_id] = Graph.IsTree()
    print("The graph is a tree: %s " % is_tree)
    print("The graph has a root id: %d" % root_id)

    Network = snap.GenTree(snap.PNEANet, 3, 3)
    [is_tree, root_id] = Network.IsTree()
    print("The graph is a tree: %s " % is_tree)
    print("The graph has a root id: %d" % root_id)
