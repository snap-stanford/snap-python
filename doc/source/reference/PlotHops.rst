PlotHops
''''''''

.. function:: PlotHops(Graph, FNmPref, DescStr = snap.TStr(), IsDir = false, NApprox = 32)

Plots the cumulative distribution of the shortest path lengths of a Graph. Implementation is based on ANF (Approximate Neighborhood Function).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *FNmFref*: string (input)
    File name prefix for output graphics files

- *DescStr*: string (input)
    Description string for the plot

- *IsDir*: bool (input)
    Whether the input graph is directed or not

- *NApprox*: integer (input)
    Number of ANF approximations, must be a multiple of eight. The larger this value is, the more accurate the distribution is.

Return value:

- None

The following example shows how to plot the cumulative distribution of shortest path lengths
for graphs of types :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotHops(Graph, "PNGraph", snap.TStr(), True, 1024)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotHops(Graph, "PUNGraph")

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotHops(Graph, "PNEANet", "with some comments")
    snap.PlotHops(Graph, "PNEANetDirected", "with some more comments", True)

