LoadConnListStr
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: PGraph LoadConnListStr(tspec, InFNm, StrToNIdH)

.. note::

    This function is not yet supported.

TODO: Unsure how to create a TStrHash<TInt>, so the demonstration is not functional.

Loads a (directed, undirected, or multi) graph from a text file, *InFNm*, with 1 node and all its edges in a single line.

Whitespace separated file of several columns: <source node name> <destination node name 1> <destination node name 2> ...
First column of each line contains a source node name followed by ids of the destination nodes.
For example, 'A B C' encodes edges A-->B and A-->C.
Note that this format allows for saving isolated nodes.

Parameters:

- *tspec*: graph class (input)
    Class of graph to load -- one of `PNGraph`, `PNEANet`, or `PUNGraph`.

- *InFNm*: string (input)
    Name of the text file to load

- *StrToNIdH*: a hash of string keys and int values (output)
    Stores the mapping from node names to node ids

Return value:

-  The loaded graph


The following example shows how to load each of the following graph types:
:class:`PNGraph`, :class:`PNEANet`, and :class:`PUNGraph`::

    # TODO write example that actually works
    h = snap.TStrIntH()
    snap.LoadConnListStr(snap.PNGraph, "test.dat", h)

    h = snap.TStrIntH()
    snap.LoadConnListStr(snap.PNEANet, "test.dat", h)

    h = snap.TStrIntH()
    snap.LoadConnListStr(snap.PUNGraph, "test.dat", h)
