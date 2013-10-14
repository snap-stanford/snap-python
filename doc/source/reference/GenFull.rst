GenFull
'''''''
.. note::

    This page is a draft and under revision.


.. function:: GenFull(tspec, Nodes)

Generates a complete graph on Nodes nodes. Graph has no self-loops.

Parameters:

- *tspec*: type (input)
    The type of graph you want to generate, e.g. 
    :class:`PNGraph`, :class:`PUNGraph`, and :class:`PNEANet`

- *Nodes*: int (input)
    The number of nodes used to generate the graph

Return value:

- *Graph*

The following example shows how to generate different types of fully connected graphs::


    import snap

    # Generate a complete directed graph with 5 nodes
    G1 = snap.GenFull(snap.PNGraph, 5)

    # Generate a complete undirected graph with 5 nodes
    G2 = snap.GenFull(snap.PUNGraph, 5)

    # Generate a complete directed network with 5 nodes
    N1 = snap.GenFull(snap.PNEANet, 5)
