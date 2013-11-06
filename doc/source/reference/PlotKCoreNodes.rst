PlotKCoreNodes
''''''''''''''

.. function:: PlotKCoreNodes(Graph, FNmPref, DescStr)

Plots the k-core node-size distribution: core k vs. number of nodes in k-core. The function creates three new files: 1) coreNodes.<*FNmPref*>.plt (the plot), 2) coreNodes.<*FNPref*>.eps (the plotting description), and 3) coreNodes.<*FNmPref*>.tab (the tab separated plotting data).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *FNmPref*: string (input)
    A string representing the preferred output file name

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty

Return value:

- None

The following example shows how to plot the k-core node-size distribution for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotKCoreNodes(Graph, "example", "Directed graph - k-core nodes")
    
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotKCoreNodes(Graph, "example", "Undirected graph - k-core nodes")

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotKCoreNodes(Graph, "example", "Network - k-core nodes")