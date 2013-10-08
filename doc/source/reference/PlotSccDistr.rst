PlotSccDistr
''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: PlotSccDistr(Graph, FNmPref, DescStr = '')

Plots the distribution of sizes of strongly connected components of a *Graph*. Saves the resultant plot as a 'scc. *FNmPref* .png' image via GnuPlot.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *FNmPref*: string (input)
    A short description to go into the filename of the plot.

- *DescStr*: string (input)
    A short description to go into the title of the plot. If left blank, or unspecified, will default to *FNmPref*.


Return value:

- None

The following example shows how to obtain example plots using :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`. A more meaningfull example using the http://snap.stanford.edu/data/wiki-Vote.html dataset is also shown::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 100)
    snap.PlotSccDistr(Graph,'ex1', 'PNGraph')
    
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 100)
    snap.PlotSccDistr(Graph,'ex2', 'PUNGraph')

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 100)
    snap.PlotSccDistr(Graph,'ex3', 'PNEANet')

    wiki_votes = snap.LoadEdgeList(snap.PNGraph,'Wiki-Vote.txt',0,1)
    snap.PlotSccDistr(wiki_votes,'ex_wiki', 'PNGraph')

