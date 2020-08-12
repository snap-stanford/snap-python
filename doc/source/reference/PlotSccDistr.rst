PlotSccDistr
''''''''''''

.. function:: PlotSccDistr(FNmPref, DescStr)

A graph method that plots the distribution of sizes of strongly connected components of a graph. The function creates three new files: 1) scc.<*FNmPref*>.plt (the commands used to create the plot), 2) scc.<*FNPref*>.png (the plot), and 3) scc.<*FNmPref*>.tab (the plotting data).

Parameters:

- *FNmPref*: string
    A string representing the preferred output file name.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

Return value:

- None
  
  
The following example shows how to plot the distribution of sizes of strongly connected components for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.PlotSccDistr("example", "Directed graph - scc distribution")

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    UGraph.PlotSccDistr("example", "Undirected graph - scc distribution")

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Network.PlotSccDistr("example", "Network - scc distribution")

