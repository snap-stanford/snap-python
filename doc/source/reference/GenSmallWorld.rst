GenSmallWorld
'''''''''''''

.. function:: GenSmallWorld(Nodes, NodeOutDeg, RewireProb, Rnd=TRnd)

Generates and returns a random small-world graph using the Watts-Strogatz model. We assume a circle where each node creates links to *NodeOutDeg* other nodes.

Parameters:

- *Nodes*: int (input)
    The number of nodes desired

- *NodeOutDeg*: int (input)
    The out degree of each node desired. Since the generated graph is undirected, the out degree for each node, on average, will be twice this value.

- *RewireProb*: float (input)
	Represents the probability that an edge will be rewired

- *Rnd*: TRnd (input)
	A TRnd instance that defaults to TInt.Rnd (Rnd)

Return value:

- :class:`PUNGraph`
    A Snap.py undirected graph

See: Collective dynamics of 'small-world' networks. Watts and Strogatz. URL: http://research.yahoo.com/files/w_s_NATURE_0.pdf

The following example shows how to generate a small-world graph for various values of *RewireProb*::

    import snap

    Rnd = snap.TRnd(1,0)
    Graph = snap.GenSmallWorld(10, 3, 0, Rnd)
    print Graph.GetEdges()
    for E in Graph.Edges():
        print E.GetSrcNId(), E.GetDstNId()

    Graph = snap.GenSmallWorld(10, 3, 0.7, Rnd)
    print Graph.GetEdges()
    for E in Graph.Edges():
        print E.GetSrcNId(), E.GetDstNId()
	