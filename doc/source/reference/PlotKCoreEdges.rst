PlotKCoreEdges
''''''''''''''

.. function:: PlotKCoreEdges(FNmPref, DescStr)

A graph method that plots the k-core edge-size distribution: core k vs. number of edges in k-core. The function creates three new files: 1) coreEdges.<*FNmPref*>.plt (the commands used to create the plot), 2) coreEdges.<*FNPref*>.png (the plot), and 3) coreEdges.<*FNmPref*>.tab (the plotting data).

Parameters:

- *FNmPref*: string
    A string representing the preferred output file name.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to plot the k-core edge-size distribution for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.PlotKCoreEdges("example", "Directed graph - k-core edges")
    
    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    UGraph.PlotKCoreEdgees("example", "Undirected graph - k-core edges")

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Network.PlotKCoreEdges("example", "Network - k-core edges")


