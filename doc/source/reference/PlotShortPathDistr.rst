PlotShortPathDistr
''''''''''''''''''

.. function:: PlotShortPathDistr(Graph, FNmPref, DescStr = TStr(), int TestNodes = TInt.Mx)

Plots the distribution of the shortest path lengths in *Graph*.  The implementation is based on BFS.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *FNmPref*: TStr (input)
    File name prefix.  The file name will be "diam.FNmPref.*".

- *DescStr*: TStr (input)
    Description string. This will be the first part of the title of the graph.  If *DescStr* is an empty TStr (the default option), then *FNmPref* will be used instead.

- *TestNodes*: int (input)
    Number of nodes from which to start BFS to count shortest path lengths.  If TestNodes is less than the total number of graph nodes, then the plot may only be an approximation of the distribution of the shortest path lengths.

Return value:

- None

The following example shows how to generate plots of the distribution of shortest path lengths for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotShortPathDistr(Graph, "Directed_Random_100-1000")
    
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotShortPathDistr(Graph, "urand", "Undirected_Random_100-1000")
    
    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotShortPathDistr(Graph, "net", "Network_100-1000", 50)
    
