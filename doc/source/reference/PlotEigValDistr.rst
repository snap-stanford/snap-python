PlotEigValDistr
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: PlotEigValDistr(Graph, NumEigenvalues, NameSuffix, TitlePrefix)

Plots the frequency distribution of the leading *NumEigenvalues* eigenvalues of the undirected
graph, *Graph*.  The plot files will be stored in the current working directory and will
include the following:

* eigDistr.<NameSuffix>.eps: an EPS file containing the rendered plot

* eigDistr.<NameSuffix>.plt: a GNUplot file to (re)create the plot

* eigDistr.<NameSuffix>.tab: a GNUplot data file referenced by eigDistr.*NameSuffix*.plt

The .eps file can be manually recreated from the .plt and .tab files by running
"gnuplot eigDistr.<NameSuffix>.plt" from the directory where the files reside.

The plot contained in the .eps file will have the following information included in the plot title:

* *TitlePrefix*

* The number of nodes and edges in *Graph*

* The largest eigenvalue of *Graph*

Parameters:

- *Graph*: graph (input)
    An undirected Snap.py graph

- *NumEigenvalues*: int (input)
    The plot will contain the frequencies of the first *NumEigenvalues* eigenvalues

- *NameSuffix*: string (input)
    The filenames for all files created will start with eigDistr.*NameSuffix*.

- *TitlePrefix*: string (input)
    The plot title will start with *TitlePrefix*.

Return value:

- None

For more info see: http://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors

The following example shows how to plot the eigenvalue frequency distribution of
an undirected graph of type :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)

    # Plot the frequencies of the first 10 eigenvalues
    # NOTE: Random graphs are likely to thwart the calculation of eigenvalues!
    snap.PlotEigValDistr(Graph, 10, "example", "Random Graph Eigenvalue Distribution")

