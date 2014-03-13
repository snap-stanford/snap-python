GenSmallWorld
'''''''''''''

.. function:: GenSmallWorld(Nodes, NodeOutDeg, RewireProb, Rnd=TRnd)

Generates and returns a random small-world graph using the Watts-Strogatz model. We assume a circle where each node creates links to *NodeOutDeg* other nodes.

Parameters:

- *Nodes*: int (input)
    The number of nodes desired.

- *NodeOutDeg*: int (input)
    The out degree of each node desired. Since the generated graph is undirected, the out degree for each node, on average, will be twice this value.

- *RewireProb*: float (input)
	Represents the probability that an edge will be rewired.

- *Rnd*: TRnd (input)
    Random number generator.

Return value:

- undirected graph
    A Snap.py undirected graph generated with the Watts-Strogatz model.

See: Collective dynamics of 'small-world' networks. Watts and Strogatz. URL: http://research.yahoo.com/files/w_s_NATURE_0.pdf


The following example shows how to generate a small-world graph for various values of *RewireProb*::

    import snap

    Rnd = snap.TRnd(1,0)
    UGraph1 = snap.GenSmallWorld(10, 3, 0, Rnd)
    for EI in UGraph1.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    UGraph2 = snap.GenSmallWorld(10, 3, 0.7, Rnd)
    for EI in UGraph2.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
	