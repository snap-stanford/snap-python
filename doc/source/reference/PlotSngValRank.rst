PlotSngValRank
''''''''''''''

.. function:: PlotSngValRank(Graph, SngVals, FNmPref, DescStr)

Plots the rank distribution of singular values of the Graph adjacency matrix. Plots first *SngVals* values. The function creates three new files: 1) sngVal.<*FNmPref*>.plt (the plot), 2) sngVal.<*FNPref*>.eps (the plotting description), and 3) sngVal.<*FNmPref*>.tab (the tab separated plotting data).

Parameters:

- *Graph*: directed graph (input)
    A Snap.py directed graph

- *SngVals*: int (input)
    Number of largest singular values to plot

- *FNmPref*: string (input)
    File name preference for the plotted graph

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.

Return value:

- None

The following example shows how to plot the rank distribution of singular values of the Graph adjacency matrix in :class:`TNGraph`::

    import snap

    graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotSngValRank(graph, 100, "filename", "Singular Value Distribution")
