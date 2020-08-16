PlotSngValDistr
'''''''''''''''

.. function:: PlotSngValDistr(SngVals, FNmPref, DescStr)

A graph method for directed graphs that plots a histogram distribution of the top 2x *SngVals* singular values of the adjacency matrix. The function creates three new files: 1) sngDistr.<*FNmPref*>.plt (the commands used to create the plot), 2) sngDistr.<*FNPref*>.png (the plot), and 3) sngDistr.<*FNmPref*>.tab (the plotting data).

Parameters:

- *SngVals*: integer
    Representing one half the desired number of singular values.

- *FNmPref*: string
    A string representing the preferred output file name.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to use :func:`PlotSngValDistr` for :class:`TNGraph`::

        import snap

        Graph = snap.GenRndGnm(snap.PNGraph, 100, 5000)
        Graph.PlotSngValDistr(50, "title", "SngVal Distribution")
