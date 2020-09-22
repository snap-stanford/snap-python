PlotEigValRank
''''''''''''''

.. function:: PlotEigValRank(NumEigenvalues, FNmPref, DescStr)

A graph method for undirected graphs that plots the distribution of the ranks of the first *NumEigenvalues* eigenvalues.  The function creates three new files: 1) eigVal.<*FNmPref*>.plt (the commands used to create the plot), 2) eigVal.<*FNPref*>.png (the plot), and 3) eigVal.<*FNmPref*>.tab (the plotting data).

Parameters:

- *NumEigenvalues*: int
    The number of the first *NumEigenvalues* eigenvalues' to include in the plot.

- *FNmPref*: string
    File name preference for the plotted graph.

- *DescStr*: string
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to plot the eigenvalue rank distribution of
an undirected graph of type :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 2000)

    # Plot the ranks of the first 10 eigenvalues
    # NOTE: Random graphs are likely to thwart the calculation of eigenvalues
    UGraph.PlotEigValRank(10, "example", "Random Graph Eigenvalue Rank")

