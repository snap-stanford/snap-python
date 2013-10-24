IsTree (Graph)
''''''''''''''''''''''''''''''''''''''''''


.. function:: IsTree(Graph)

Determines if *Graph* is a connected tree.  As a special case, if a graph has one node and no edges, it is a tree. The function returns a (boolean, int) pair, where the boolean indicates whether *Graph* is a tree and the int is the node id for the root of the tree.

Parameters:

- *Graph*: (input) 
    A Snap.py graph or a network


Return value: 

- bool: 
    True if *Graph* represents a tree with root *RootNId* and false otherwise

- int:
    The node id for the root of the tree


The following example shows how to detect trees in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenTree(snap.PNGraph, 3, 3)
    IsTree(Graph)
    

    Graph = snap.GenTree(snap.PUNGraph, 3, 3)
    IsTree(Graph)

    Graph = snap.GenTree(snap.PNEANraph, 3, 3)
    IsTree(Graph)

