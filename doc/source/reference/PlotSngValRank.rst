PlotSngValRank
''''''''''''''

.. function:: PlotSngValRank(SngVals, FNmPref, DescStr)

A graph method for directed graphs that plots the rank distribution of singular values of the adjacency matrix. Plots first *SngVals* values. The function creates three new files: 1) sngVal.<*FNmPref*>.plt (the commands used to create the plot), 2) sngVal.<*FNPref*>.png (the plot), and 3) sngVal.<*FNmPref*>.tab (the plotting data).

Parameters:

- *SngVals*: int
    Number of largest singular values to plot.

- *FNmPref*: string
    File name preference for the plotted graph.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to plot the rank distribution of singular values of the Graph adjacency matrix for :class:`TNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.PlotSngValRank(100, "filename", "Singular Value Distribution")
