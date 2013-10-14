PlotKCoreEdges
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: PlotKCoreEdges(Graph, FNmPref, DescStr="")

Plots the k-Core edge-size distribution: Core k vs. number of edges in k-core.

Parameters

- Graph
    A Snap.py graph or network.
    
- FNmPref
    Filename prefix. The generated file has the name "coreEdges.<FNmPref>.png".

- DescStr
    Optional description of plot, incorporated in the title of the plot. If left empty
    the filename prefix is used instead.
    
Return Value

- None (outputs plot to disk as png file)



Source Code

Plot KCore distribution for different types of graphs::

    from snap import *
    
    G1 = GenRndGnm(PUNGraph, 100, 1000)
    PlotKCoreEdges(G1, "UNKCore", "UNKCore Plot")
    
    G1 = GenRndGnm(PNGraph, 100, 1000)
    PlotKCoreEdges(G1, "KCore", "KCore Plot")

    G1 = GenRndGnm(PNEANet, 100, 1000)
    PlotKCoreEdges(G1, "EAKCore", "EAKCore Plot")


