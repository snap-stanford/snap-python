MakeUnDir
'''''''''
.. note::

    This page is a draft and under revision.


.. function:: MakeUnDir(Graph)

Makes the graph undirected.
For every edge (u,v) an edge (v,u) is added (if it does not yet exist).

Parameters:

- *Graph*: graph (input)
    A directed Snap.py graph or network
    (i.e. :class:`TNGraph` or :class:`TNEANet`)

Return value:

- None

The following example shows correct usage with 
:class:`TNGraph` and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print Graph.GetEdges() # Outputs 1000
    snap.MakeUnDir(Graph)
    print Graph.GetEdges() # Outputs something like 1900 as edges added

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print Graph.GetEdges() # Outputs 1000
    snap.MakeUnDir(Graph)
    print Graph.GetEdges() # Outputs something like 1900 as edges added

The following example shows how using :py:func:`MakeUnDir` incorrectly with
:class:`TUNGraph` results in no change to the graph::

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print Graph.GetEdges() # Outputs 1000
    snap.MakeUnDir(Graph)
    print Graph.GetEdges() # Outputs 1000