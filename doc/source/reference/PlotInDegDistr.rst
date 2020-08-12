PlotInDegDistr
''''''''''''''

.. function:: PlotInDegDistr(FNmPref, DescStr, PlotCCdf=False, PowerFit=False)

A graph method that plots the in-degree distribution of a graph. The function creates three new files: 1) inDeg.<*FNmPref*>.plt (the plot), 2) inDeg.<*FNPref*>.png (the plotting description), and 3) inDeg.<*FNmPref*>.tab (the tab separated plotting data).


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


The following example shows how generate a plot of the in-degree distribution for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.PlotInDegDistr("example", "Directed graph - in-degree Distribution")

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    UGraph.PlotInDegDistr("example", "Undirected graph - in-degree Distribution")

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Network.PlotInDegDistr("example", "Network - in-degree Distribution")
