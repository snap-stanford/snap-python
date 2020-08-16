PlotSngVec
''''''''''

.. function:: PlotSngVec(FNmPref, DescStr)

A graph method for directed graphs that ranks the values of the leading left singular vector of the adjacency matrix and then plots the first *SngVals* on a log-log chart. The function creates three new files: 1) sngVecL.<*FNmPref*>.plt (the plot), 2) sngVecL.<*FNPref*>.eps (the plotting description), and 3) sngVecL.<*FNmPref*>.tab (the tab separated plotting data).

Parameters:

- *FNmPref*: string
    A string representing the preferred output file name.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to use :func:`PlotSngVec` for :class:`TNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.PlotSngVec("my_filename", "my_chart_title")
