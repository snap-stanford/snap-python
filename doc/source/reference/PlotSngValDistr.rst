PlotSngValDistr
'''''''''''''''

.. function:: PlotSngValDistr(Graph,SngVals, FNmPref, DescStr=snap.TStr())

Plots a histogram distribution of the top 2x *SngVals* singular values of the *Graph* adjacency matrix. The function creates three new files: 1) sngDistr.*FNmPref*.plt (the plot), 2) sngDistr.*FNPref*.eps (the plotting description), and 3) sngDistr.*FNmPref*.tab (the tab separated plotting data).

Parameters:

- *Graph*: directed graph (input)
    A Snap.py directed graph

- *SngVals*: integer (input)
    Representing one half the desired number of singular values

- *FNmPref*: string (input)
    A string representing the preferred output file name

- *DescStr*: string (input)
    A string representing the title of the plot

Return value:

- None

The following example shows how to use :func:`PlotSngValDistr` for :class:`TNGraph`::

        import snap

        Graph = snap.GenRndGnm(snap.PNGraph, 100, 5000)
        snap.PlotSngValDistr(Graph, 50, "title", "SngVal Distribution")
