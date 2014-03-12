PlotClustCf
'''''''''''

.. function:: PlotClustCf(Graph, FNmPref, DescStr)

Plots the distribution of clustering coefficient of *Graph*. The function creates three new files: 1) ccf.<*FNmPref*>.plt (the commands used to create the plot), 2) ccf.<*FNPref*>.png (the plot), and 3) ccf.<*FNmPref*>.tab (the plotting data).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *FNmPref*: string (input)
    A string representing the preferred output file name.

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to plot the distribution of clustering coefficients
for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotClustCf(Graph, "example", "Directed graph - clustering coefficient")

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotClustCf(UGraph, "example", "Directed graph - clustering coefficient")

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotClustCf(Network, "example", "Directed graph - clustering coefficient")

