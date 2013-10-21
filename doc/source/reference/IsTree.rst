IsTree (Graph)
''''''''''''''''''''''''''''''''''''''''''


.. function:: IsTree(Graph, RootNId)

Determines if *Graph* is a connected tree with *RootNID* as the root.  As a special case, if a graph has one node and no edges, it is a tree.  If there are any orphaned nodes, the graph is not a tree. The function returns a boolean indicating whether *Graph* is a tree.

Parameters:

- *Graph*: (input) 
    A Snap.py graph or a network

- *RootNId*: (input)
    The node id of the root

Return value: 

- bool: 
    true if *Graph* represents a tree with root *RootNId* and false otherwise

The following example shows how to detect trees in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenTree(snap.PNGraph, 3, 3)
    firstnode = 0
    IsTree(Graph, firstnode)

    Graph = snap.GenTree(snap.PUNGraph, 3, 3)
    firstnode = 0
    IsTree(Graph, firstnode)

    Graph = snap.GenTree(snap.PNEANraph, 3, 3)
    firstnode = 0
    IsTree(Graph, firstnode)

