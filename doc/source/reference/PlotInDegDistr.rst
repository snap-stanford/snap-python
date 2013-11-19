PlotInDegDistr
''''''''''''''

.. function:: PlotInDegDistr(Graph, FNmPref, DescStr, PlotCCdf=False, PowerFit=False)

Plots the in-degree distribution of *Graph*. The function creates three new files: 1) inDeg.<*FNmPref*>.plt (the plot), 2) inDeg.<*FNPref*>.png (the plotting description), and 3) inDeg.<*FNmPref*>.tab (the tab separated plotting data).


Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *FNmPref*: string (input)
    A string representing the preferred output file name

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty

- *PlotCCdf*: bool (input)
    Plots the distribution as a Complementary Cummulative distribution function

- *PowerFit*: bool (input)
    Fits a Power-Law to the distribution

Return value:

- None

The following example shows how generate a plot of the in-degree distribution for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotInDegDistr(Graph, "example", "Directed graph - in-degree Distribution")

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotInDegDistr(Graph, "example", "Undirected graph - in-degree Distribution")

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotInDegDistr(Graph, "example", "Network - in-degree Distribution")
