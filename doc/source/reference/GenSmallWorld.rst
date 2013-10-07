GenSmallWorld
'''''''''''''

.. function:: PUNGraph GenSmallWorld(Nodes, NodeOutDeg, RewireProb, Rnd=TInt::Rnd)

Generates and returns a random small-world graph using the Watts-Strogatz model.

Generates a small-world graph using the Watts-Strogatz model. We assume a circle where each node creates links to NodeOutDeg other nodes. See: Collective dynamics of 'small-world' networks. Watts and Strogatz. URL: http://research.yahoo.com/files/w_s_NATURE_0.pdf

Parameters:

- *Nodes*: int (input)
    Represents the desired number of nodes in the output graph

- *NodeOutDeg*: int (input)
	Indicates the average out-degree of a node prior to the Watts-Strogatz rewiring procedure

- *RewireProb*: double (input)
	Represents the probability that an edge will be rewired

- *Rnd*: TRnd (input)
	A TRnd instance that defaults to TInt.Rnd (Rnd)

Return value:

- :class:`PUNGraph` (output)
    A Snap.py undirected graph

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
	