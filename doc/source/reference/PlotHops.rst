PlotHops
''''''''

.. function:: PlotHops(FNmPref, DescStr, IsDir=False, NApprox=32)

A graph method that plots the cumulative distribution of the shortest path lengths of a graph. The implementation is based on ANF (Approximate Neighborhood Function). The function creates three new files: 1) hop.<*FNmPref*>.plt (the commands used to create the plot), 2) hop.<*FNPref*>.png (the plot), and 3) hop.<*FNmPref*>.tab (the plotting data).

Parameters:

- *FNmPref*: string
    A string representing the preferred output file name.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

- *IsDir*: bool
    Whether the input graph is directed or not.

- *NApprox*: int
    Number of ANF approximations, must be a multiple of eight. The larger this value is, the more accurate the distribution is.

Return value:

- None


The following example shows how to plot the cumulative distribution of shortest path lengths for graphs of types :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.PlotHops("example", "Directed graph - hops", True, 1024)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    UGraph.PlotHops("example", "Undirected graph - hops", False, 1024)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Network.PlotHops("example", "Network - hops", True, 1024)
