PlotSccDistr
''''''''''''

.. function:: PlotSccDistr(Graph, FNmPref, DescStr)

Plots the distribution of sizes of strongly connected components of *Graph*. The function creates three new files: 1) scc.<*FNmPref*>.plt (the commands used to create the plot), 2) scc.<*FNPref*>.png (the plot), and 3) scc.<*FNmPref*>.tab (the plotting data).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *FNmPref*: string (input)
    A string representing the preferred output file name.

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.

Return value:

- None
  
  
The following example shows how to plot the distribution of sizes of strongly connected components for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotSccDistr(Graph, "example", "Directed graph - scc distributaion")

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotSccDistr(UGraph, "example", "Undirected graph - scc distribution")

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotSccDistr(Network, "example", "Network - scc distribution")

