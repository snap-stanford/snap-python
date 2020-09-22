PlotWccDistr
''''''''''''

.. function:: PlotWccDistr(FNmPref, DescStr)

A graph method that plots the distribution of sizes of weakly connected components of a graph. The function creates three new files: 1) wcc.<*FNmPref*>.plt (the plot), 2) wcc.<*FNPref*>.png (the plotting description), and 3) wcc.<*FNmPref*>.tab (the tab separated plotting data).

Parameters:

- *FNmPref*: string
    A string representing the preferred output file name.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

Return value:

- None
  
    
The following example shows how to plot the distribution of sizes of weakly connected components for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Graph.PlotWccDistr("example", "Directed graph - wcc distributaion")

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    UGraph.PlotWccDistr("example", "Undirected graph - wcc distribution")

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Network.PlotWccDistr("example", "Network - wcc distribution")
