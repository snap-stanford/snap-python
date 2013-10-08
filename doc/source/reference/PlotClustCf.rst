PlotClustCf
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: PlotClustCf(Graph, FNmPref, DescStr = snap.TStr())

Plots the distribution of clustering coefficient of a Graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *FNmFref*: string (input)
    File name prefix for output graphics files

- *DescStr*: string (input)
    Description string for the plot

Return value:

- None

The following example shows how to plot the distribution of clustering coefficients
for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotClustCf(Graph, "PNGraph")

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotClustCf(Graph, "PUNGraph")

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotClustCf(Graph, "PNEANet", "with some comments")

