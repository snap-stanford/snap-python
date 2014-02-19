GenPrefAttach
'''''''''''''

.. function:: GenPrefAttach(Nodes, NodesOutDeg, Rnd=TRnd)

Generates an undirected graph with a power-law degree distribution using Barabasi-Albert model of scale-free graphs.

Parameters: 

- *Nodes*: int (input)
	The number of nodes desired

- *NodeOutDeg*: int (input)
	The out degree of each node desired

- *Rnd*: TRnd (input)
	Random number generator 

Return Value: 
	
- :class:`PUNGraph`
	An undirected graph representing the power-law degree distribution. 

The function implements a Barabasi-Albert model of scale-free graphs and generates graphs with a power-law degree distribution. See: Emergence of scaling in random networks by Barabasi and Albert. URL: http://arxiv.org/abs/cond-mat/9910332

The following example shows how to use :func:`GenPrefAttach`::
	
    import snap 

    Rnd = snap.TRnd()
    Graph = snap.GenPrefAttach(100, 10, Rnd)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())
