PlotKCoreNodes
''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: PlotKCoreNodes(Graph, FNmPref, DescStr)

Plots the k-Core node-size distribution: Core k vs. number of nodes in k-core.
Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *FNMPref*: TStr (input)
    Additional string to append to the end of the output filename.

- *DescStr*: TStr (input)
    Description String

Return value:

- None


The following example shows how to calculate PageRank scores for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    from snap import *

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    PlotKCoreNodes(Graph, "directed", "Directed")
    
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    PlotKCoreNodes(Graph, "undirected", "Undirected")

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    PlotKCoreNodes(Graph, "network", "Network")
