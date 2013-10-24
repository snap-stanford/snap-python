MakeUnDir
'''''''''

.. function:: MakeUnDir(Graph)

Makes the graph undirected.
For every edge (u,v) an edge (v,u) is added (if it does not yet exist).
The function has no effect on undirected graphs.

Parameters:

- *Graph*: graph (input)
    A directed Snap.py graph or network
    (i.e. :class:`TNGraph` or :class:`TNEANet`)

Return value:

- None

The following example shows usage with directed graph types 
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

The following example shows how using :py:func:`MakeUnDir` with
an undirected graph of type :class:`TUNGraph` results in no change to the graph::

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print Graph.GetEdges() # Outputs 1000
    snap.MakeUnDir(Graph)
    print Graph.GetEdges() # Outputs 1000
