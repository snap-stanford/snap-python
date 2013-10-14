GenRndGnm
'''''''''
.. note::

    This page is a draft and under revision.


.. function:: GenRndGnm(GraphType, Nodes, Edges, IsDir=True, Rnd=TInt.Rnd)

Generates an Erdos-Renyi random graph of the specified *GraphType*, Computes the degree sequence vector for nodes in *Graph*. The degree sequence vector is stored in *DegV*.

Parameters:

- *GraphType*: class of graph
    The class of Snap.py graph produced

- *Nodes*: an integer
    Number of nodes in the generated graph.

- *Edges*: an integer
    Number of edges in the genereated graph.

- *IsDir*: a boolean
    Whether the graph is directed.

- *Rnd*: a random generator instance
    The random generator instance used

Return value:

- A Snap.py graph of the relevant type.

The following example shows how to generate random graphs of types
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph1 = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph2 = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Graph3 = snap.GenRndGnm(snap.PNEANet, 100, 1000)
