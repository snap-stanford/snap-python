LoadConnListStr
'''''''''''''''

.. function:: LoadConnListStr(GraphType, InFNm, StrToNIdH)

Loads a (directed, undirected, or multi) graph from a text file, *InFNm*, with 1 node and all its edges in a single line.

*InFNm* is a whitespace separated file of several columns: <source node name> <destination node name 1> <destination node name 2> ...
First column of each line contains a source node name followed by ids of the destination nodes.
For example, 'A B C' encodes edges A-->B and A-->C.
Note that this format allows for saving isolated nodes.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *InFNm*: string (input)
    Filename with the description of the graph nodes and edges.

- *StrToNIdH*: :class:`TStrIntH`, a hash table of string keys and int values (output)
    Stores the mapping from node names to node ids.

Return value:

- graph
    A Snap.py graph of the specified type *GraphType*.


The following example shows how to load each of the graph types from a file named "test.dat"::

    import snap

    H = snap.TStrIntH()
    snap.LoadConnListStr(snap.PNGraph, "test.dat", H)

    H = snap.TStrIntH()
    snap.LoadConnListStr(snap.PNEANet, "test.dat", H)

    H = snap.TStrIntH()
    snap.LoadConnListStr(snap.PUNGraph, "test.dat", H)
