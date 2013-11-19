PlotEigValDistr
'''''''''''''''

.. function:: PlotEigValDistr(Graph, NumEigenvalues, FNmPref, DescStr)

Plots the frequency distribution of the leading *NumEigenvalues* eigenvalues of the undirected graph *Graph*. The function creates three new files: 1) eigDistr.<*FNmPref*>.plt (the commands used to create the plot), 2) eigDistr.<*FNPref*>.png (the plot), and 3) eigDistr.<*FNmPref*>.tab (the plotting data).

Parameters:

- *Graph*: undirected graph (input)
    An Snap.py undirected graph

- *NumEigenvalues*: int (input)
    The plot will contain the frequencies of the first *NumEigenvalues* eigenvalues

- *FNmPref*: string (input)
    File name preference for the plotted graph

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.

Return value:

- None

The following example shows how to plot the eigenvalue frequency distribution of
an undirected graph of type :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)

    # Plot the frequencies of the first 10 eigenvalues
    # NOTE: Random graphs are likely to thwart the calculation of eigenvalues
    snap.PlotEigValDistr(Graph, 10, "example", "Random Graph Eigenvalue Distribution")

