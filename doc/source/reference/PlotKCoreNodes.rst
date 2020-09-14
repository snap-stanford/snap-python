PlotKCoreNodes
''''''''''''''

.. function:: PlotKCoreNodes(FNmPref, DescStr)

A graph method that plots the k-core node-size distribution: core k vs. number of nodes in k-core. The function creates three new files: 1) coreNodes.<*FNmPref*>.plt (the commands used to create the plot), 2) coreNodes.<*FNPref*>.png (the plot), and 3) coreNodes.<*FNmPref*>.tab (the plotting data).

Parameters:

- *FNmPref*: string
    A string representing the preferred output file name.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to plot the k-core node-size distribution for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Graph.PlotKCoreNodes("example", "Directed graph - k-core nodes")
    
    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    UGraph.PlotKCoreNodes("example", "Undirected graph - k-core nodes")

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Graph.PlotKCoreNodes("example", "Network - k-core nodes")
