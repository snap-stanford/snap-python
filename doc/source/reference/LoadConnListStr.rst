LoadConnListStr
'''''''''''''''

.. function:: LoadConnListStr(GraphType, InFNm)

Loads a (directed, undirected, or multi) graph from a text file, *InFNm*, with 1 node and all its edges in a single line.

*InFNm* is a whitespace separated file of several columns: <source node name> <destination node name 1> <destination node name 2> ...
First column of each line contains a source node name followed by ids of the destination nodes.
For example, 'A B C' encodes edges A => B and A => C.
Note that this format allows for saving isolated nodes.

Parameters:

- *GraphType*: graph class
    Class of output graph -- one of :class:`TNGraph`, :class:`TNEANet`, or :class:`TUNGraph`.

- *InFNm*: string
    Filename with the description of the graph nodes and edges.

Return value:

- graph
    A Snap.py graph of the specified type *GraphType*.

- *StrToNIdH*: :class:`TStrIntSH`, a hash table of string keys and int values
    Stores the mapping from node names to node ids.
    Note that this is a special hash table for holding strings and its interface differs from the standard SNAP hash table. Use *GetKeyId(name)* to obtain a mapping from a node name to its node id.


The following example shows how to load each of the graph types from a file named *test.dat*::

    import snap

    (Graph, H) = snap.LoadConnListStr(snap.TNGraph, "test.dat")

    (UGraph, H) = snap.LoadConnListStr(snap.TUNGraph, "test.dat")

    (Network, H) = snap.LoadConnListStr(snap.TNEANet, "test.dat")

    # convert input string to node id
    NodeId = H.GetKeyId("A")
    # convert node id to input string
    NodeName = H.GetKey(NodeId)
    print("name", NodeName)
    print("id  ", NodeId)

A sample of *test.dat* is::

    A B C
    B C D
