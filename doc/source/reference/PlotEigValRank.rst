PlotEigValRank
''''''''''''''

.. function:: PlotEigValRank(Graph, NumEigenvalues, FNmPref, DescStr)

Plots the distribution of the ranks of the first *NumEigenvalues* eigenvalues of the undirected graph *Graph*.  The function creates three new files: 1) eigVal.<*FNmPref*>.plt (the commands used to create the plot), 2) eigVal.<*FNPref*>.png (the plot), and 3) eigVal.<*FNmPref*>.tab (the plotting data).

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *NumEigenvalues*: int (input)
    The plot will contain the ranks of the first *NumEigenvalues* eigenvalues'. ranks

- *FNmPref*: string (input)
    File name preference for the plotted graph.

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.

Return value:

- None


The following example shows how to plot the eigenvalue rank distribution of
an undirected graph of type :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 2000)

    # Plot the ranks of the first 10 eigenvalues
    # NOTE: Random graphs are likely to thwart the calculation of eigenvalues
    snap.PlotEigValRank(UGraph, 10, "example", "Random Graph Eigenvalue Rank")

