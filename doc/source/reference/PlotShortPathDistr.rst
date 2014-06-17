PlotShortPathDistr
''''''''''''''''''

.. function:: PlotShortPathDistr(Graph, FNmPref, DescStr, TestNodes=TInt.Mx)

Plots the distribution of the shortest path lengths in *Graph*. The implementation is based on BFS. The function creates three new files: 1) diam.<*FNmPref*>.plt (the commands used to create the plot), 2) diam.<*FNPref*>.png (the plot), and 3) diam.<*FNmPref*>.tab (the plotting data).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *FNmPref*: string (input)
    A string representing the preferred output file name.

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.

- *TestNodes*: int (input)
    Number of nodes from which to start BFS to count shortest path lengths.  If TestNodes is less than the total number of graph nodes, then the plot may only be an approximation of the distribution of the shortest path lengths.

Return value:

- None


The following example shows how to generate plots of the distribution of shortest path lengths for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotShortPathDistr(Graph, "example", "Directed graph - shortest path")
    
    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotShortPathDistr(UGraph, "example", "Undirected graph - shortest path")
    
    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotShortPathDistr(Network, "example", "Network - shortest path")
    
