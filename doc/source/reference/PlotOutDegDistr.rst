PlotOutDegDistr
'''''''''''''''

.. function:: PlotOutDegDistr(FNmPref, DescStr, PlotCCdf=False, PowerFit=False)

A graph method that plots the out-degree distribution of a graph. The function creates three new files: 1) outDeg.<*FNmPref*>.plt (the plot), 2) outDeg.<*FNPref*>.png (the plotting description), and 3) outDeg.<*FNmPref*>.tab (the tab separated plotting data).


Parameters:

- *FNmPref*: string
    A string representing the preferred output file name.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

- *PlotCCdf*: bool
    Plots the distribution as a Complementary Cummulative distribution function.

- *PowerFit*: bool
    Fits a Power-Law to the distribution.

Return value:

- None


The following example shows how generate a plot of the out-degree distribution for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.PlotOutDegDistr("example", "Directed graph - out-degree Distribution")

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    UGraph.PlotOutDegDistr("example", "Undirected graph - out-degree Distribution")

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Network.PlotOutDegDistr("example", "Network - out-degree Distribution")
