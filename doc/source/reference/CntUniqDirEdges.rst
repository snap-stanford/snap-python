CntUniqDirEdges
'''''''''''

.. function:: CntUniqDirEdges(Graph)

Returns the number of unique directed edges in the graph *Graph*. Nodes (u,v), where u != v, are connected via a directed edge if there exists a directed edge from node u to node v. If there are multiple directed edges from u to v, the connection will be counted only once.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- Number of unique directed edges in Graph (int)

The following example shows how to calculate the number of unique directed edges for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    n1 = snap.CntUniqDirEdges(Graph)
    print n1

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    n2 = snap.CntUniqDirEdges(Graph)
    print n2

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    n3 = snap.CntUniqDirEdges(Graph)
    print n3
