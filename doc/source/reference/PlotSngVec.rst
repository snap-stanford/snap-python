PlotSngVec
''''''''''

.. function:: PlotSngVec(Graph, FNmPref, DescStr=snap.TStr())

Ranks the values of the leading left singular vector of the graph adjacency matrix plots the first SngVals on a log-log chart. The function creates three new files: 1) sngVecL.*FNmPref*.plt (the plot), 2) sngVecL.*FNPref*.eps (the plotting description), and 3) sngVecL.*FNmPref*.tab (the tab separated plotting data).

Parameters:

- *Graph*: directed graph (input)
    A Snap.py directed graph

- *FNmPref*: string (input)
    A string representing the preferred output file name

- *DescStr*: string (input)
    A string representing the title of the plot

Return value:

- None

The following example shows how to use :func:`PlotSngVec` for :class:`TNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotSngVec(Graph,"my_filename","my_chart_title")


Observations: 

* Apparent error: The chart title shows "right" singular vector as oppsed to "left"
* The C++ code seems to be set up to output both right and left vectors, but only generates the left
* Function documentation specifies that only the first SngVals values will be plotted. Its not clear (to me) that this is the case, nor where this value is set, if at all it is
* Its not clear (to me, encore...) how one sets the default output values (e.g., generate a png file or show directly in aqua vs eps) 