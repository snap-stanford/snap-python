PlotHops
''''''''

.. function:: PlotHops(Graph, FNmPref, DescStr, IsDir=False, NApprox=32)

Plots the cumulative distribution of the shortest path lengths of *Graph*. The implementation is based on ANF (Approximate Neighborhood Function). The function creates three new files: 1) hop.<*FNmPref*>.plt (the commands used to create the plot), 2) hop.<*FNPref*>.png (the plot), and 3) hop.<*FNmPref*>.tab (the plotting data).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *FNmPref*: string (input)
    A string representing the preferred output file name.

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.

- *IsDir*: bool (input)
    Whether the input graph is directed or not.

- *NApprox*: int (input)
    Number of ANF approximations, must be a multiple of eight. The larger this value is, the more accurate the distribution is.

Return value:

- None


The following example shows how to plot the cumulative distribution of shortest path lengths for graphs of types :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotHops(Graph, "example", "Directed graph - hops", True, 1024)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotHops(UGraph, "example", "Undirected graph - hops", False, 1024)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotHops(Network, "example", "Network - hops", True, 1024)