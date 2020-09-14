PlotClustCf
'''''''''''

.. function:: PlotClustCf(FNmPref, DescStr)

A graph method that plots the distribution of clustering coefficient of a graph. The function creates three new files: 1) ccf.<*FNmPref*>.plt (the commands used to create the plot), 2) ccf.<*FNPref*>.png (the plot), and 3) ccf.<*FNmPref*>.tab (the plotting data).

Parameters:

- *FNmPref*: string
    A string representing the preferred output file name.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to plot the distribution of clustering coefficients
for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Graph.PlotClustCf("example", "Directed graph - clustering coefficient")

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    UGraph.PlotClustCf("example", "Directed graph - clustering coefficient")

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Network.PlotClustCf("example", "Directed graph - clustering coefficient")

