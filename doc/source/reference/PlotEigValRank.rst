PlotEigValRank
''''''''''''''

.. function:: PlotEigValRank(Graph, NumEigenvalues, NameSuffix, TitlePrefix)

Plots the distribution of the ranks of the first *NumEigenvalues* eigenvalues of the undirected
graph, *Graph*.  The plot files will be stored in the current working directory and will
include the following:

* eigVal.<NameSuffix>.eps: an EPS file containing the rendered plot

* eigVal.<NameSuffix>.plt: a GNUplot file to (re)create the plot

* eigVal.<NameSuffix>.tab: a GNUplot data file referenced by eigVal.*NameSuffix*.plt

The .eps file can be manually recreated from the .plt and .tab files by running
"gnuplot eigVal.<NameSuffix>.plt" from the directory where the files reside.

The plot contained in the .eps file will have the following information included in the plot title:

* *TitlePrefix*

* The number of nodes and edges in *Graph*

* The largest eigenvalue of *Graph*

Parameters:

- *Graph*: graph (input)
    An undirected Snap.py graph

- *NumEigenvalues*: int (input)
    The plot will contain the ranks of the first *NumEigenvalues* eigenvalues' ranks

- *NameSuffix*: string (input)
    The filenames for all files created will start with eigVal.*NameSuffix*.

- *TitlePrefix*: string (input)
    The plot title will start with *TitlePrefix*.

Return value:

- None

For more info see: http://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors

The following example shows how to plot the eigenvalue rank distribution of
an undirected graph of type :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)

    # Plot the ranks of the first 10 eigenvalues
    # NOTE: Random graphs are likely to thwart the calculation of eigenvalues!
    snap.PlotEigValRank(Graph, 10, "example", "Random Graph Eigenvalue Rank")

