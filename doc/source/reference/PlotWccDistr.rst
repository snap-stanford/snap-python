PlotWccDistr
''''''''''''

.. function:: PlotWccDistr(Graph, FNmPref, DescStr)

Plots the distribution of sizes of weakly connected components of *Graph*. The function creates three new files: 1) wcc.<*FNmPref*>.plt (the plot), 2) wcc.<*FNPref*>.eps (the plotting description), and 3) wcc.<*FNmPref*>.tab (the tab separated plotting data).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *FNmPref*: string (input)
    A string representing the preferred output file name

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty

Return value:

- None
    
The following example shows how to plot the distribution of sizes of weakly connected components for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotWccDistr(Graph, "example", "Directed graph - wcc distributaion")

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotWccDistr(Graph, "example", "Undirected graph - wcc distribution")

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotWccDistr(Graph, "example", "Network - wcc distribution")
