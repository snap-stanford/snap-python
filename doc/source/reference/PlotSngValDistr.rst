PlotSngValDistr
'''''''''''

.. function:: PlotSngValDistr(Graph,SngVals, FNMPref, DescStr)

Plots a histogram distribution of the top 2x *SngVals* singular values of the *Graph* adjacency matrix.

Parameters:

- *Graph*: graph (input)
    A directed Snap.py graph

- *SngVals*: integer (input)
    Representing one half the desired number of singular values

- *FNmPref*: string (input)
    A string representing the preferred output file name

- *DescStr*: string (input)
    A string representing the title of the plot

Return value:

- None
    The function creates three new files: 1) sngDist.FNmPref.eps (the plot), 2) sngDistr.FNPref.eps (the plotting description), and 3) sngDistr.FNmPref.tab (the tab separated plotting data)

The following example shows how to use PlotSngValDistr on
:class:`PNGraph`::

        from snap import *

        Graph = GenRndGnm(PNGraph, 100, 5000)
        SngVals = 50
        FNmPref = "TitleName"
        DescStr = "Description"
        PlotSngValDistr(Graph, SngVals,FNmPref, DescStr)