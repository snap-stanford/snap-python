PlotSngValRank
''''''''''''''

.. function:: PlotSngValRank(Graph, SngVals, FNmPref, DescStr="")

Plots the rank distribution of singular values of the Graph adjacency matrix. Plots first SngVals values.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *SngVals*: int (input)
    Number of largest singular values to plot

- *FNmPref*: String (input)
    File name preference for the plotted graph

- *DescStr*: String (input)
    Description of the graph. Default to file name preference.

Return value:

- None

The following example shows how to plot the rank distribution of singular values of the Graph adjacency matrix in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    neighbors = snap.TIntV()

    graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotSngValRank(graph, 100, "filename", "nice graph!")

    graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotSngValRank(graph, 100, "filename", "nice graph!")
