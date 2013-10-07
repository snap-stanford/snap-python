PlotWccDistr
'''''''''''

.. function:: PlotWccDistr(Graph, path, description)

Plots the distribution of sizes of weakly connected components of a Graph.

Parameters:

- *Graph*: PNGraph (input)
    The graph

- *path*: str (input)
    The path where the plot will be saved

- *description*: str (input)
    The graph description to be included in the plot
    
The following example shows how to plot the distribution of sizes of weakly connected components of a Graph::

    G = sn.LoadEdgeList(sn.PNGraph, "/my/graph/path.txt")
    snap.PlotWccDistr(G, "/my/plot/path", "graph description")