GenCircle
'''''''''

.. function:: GenCircle(Type, NumNodes, OutDegree, IsDirected = true)

Generate a circular graph with *NumNodes* nodes.  The generated graph will have an edge from each node to
the subsequent *OutDegree* nodes.

If Type is `snap.PUNGraph`, the *IsDirected* parameter is ignored.  If Type is `snap.PNGraph`
or `snap.PNEANet`, the *IsDirected* parameter controls whether a reciprocal edge is
created.  If *IsDirected* is `False`, then a reciprocal edge will be created for every edge added to the graph.
If *IsDirected* is `True`, then the graph will only contain edges from each node to the subsequent
*OutDegree* nodes.

Parameters:

- *Type*: snap.PGraph (input)
    The type of the graph to be generated

- *NumNodes*: int (input)
    The number of nodes to be created in the graph

- *OutDegree*: int (input)
    The number of edges to be added to each node.  This number does not include reciprocal edges.

- *IsDirected*: boolean (input)
    Whether the generated graph should be directed. (Optional)

Return value:

- `snap.TGraph`: the generated graph

The following example shows how to generate a circular graph::

    import snap

    # Create a new directed graph
    g = snap.GenCircle(snap.PNGraph, 100, 10)

    # Create a new undirected graph
    u = snap.GenCircle(snap.PUNGraph, 100, 10)

    # Create a new directed network
    n = snap.GenCircle(snap.PNEANet, 100, 10)

Notes:

There is an off-by-one bug in the C++ code that causes the reciprocal edges to point to the wrong nodes.
For example:

>>> g = snap.GenCircle(snap.PNGraph, 3, 1, False)
>>> for n in g.Nodes():
...   for e in n.GetOutEdges():
...     print "%d -> %d" % (n.GetId(), e)
... 
0 -> 0
0 -> 1
1 -> 1
1 -> 2
2 -> 0
2 -> 2

The self edges in this graph should instead be reciprocal edges to the previous node in the circle.
