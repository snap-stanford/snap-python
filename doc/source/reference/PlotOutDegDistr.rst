PlotOutDegDistr
'''''''''''''''

.. function:: PlotOutDegDistr(Graph, FNmPref, DescStr, PlotCCdf=False, PowerFit=False)

Plots the out-degree distribution of *Graph*. The function creates three new files: 1) outDeg.<*FNmPref*>.plt (the plot), 2) outDeg.<*FNPref*>.png (the plotting description), and 3) outDeg.<*FNmPref*>.tab (the tab separated plotting data).


Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *FNmPref*: string (input)
    A string representing the preferred output file name.

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.

- *PlotCCdf*: bool (input)
    Plots the distribution as a Complementary Cummulative distribution function.

- *PowerFit*: bool (input)
    Fits a Power-Law to the distribution.

Return value:

- None


The following example shows how generate a plot of the out-degree distribution for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotOutDegDistr(Graph, "example", "Directed graph - out-degree Distribution")

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotOutDegDistr(UGraph, "example", "Undirected graph - out-degree Distribution")

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotOutDegDistr(Network, "example", "Network - out-degree Distribution")
