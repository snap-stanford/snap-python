PlotOutDegDistr
'''''''''''''''

.. function:: PlotOutDegDistr(Graph, FNmPref, DescStr, PlotCCdf, PowerFit)

Plots the out-degree distribution of a *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *FNmPref*: string (input)
    Name of the 3 files that are written to the current working directory.
        outDeg.<FNmPref>.plt
        outDeg.<FNmPref>.png
        outDeg.<FNmPref>.tab
        
- *DescStr*: string (input)
    User description or comment
    
- *PlotCCdf*: boolean (input)
    Plots the distribution as a Complementary Cumulative Distribution Function (CCDF). 

- *PowerFit*: boolean (input)
    Fits a Power-Law to the distribution.

Return value:

- None

The following example shows the out-degree distribution for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    import os

    if not os.path.exists("./output"):
        os.makedirs("./output")
    os.chdir("./output")

    vGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotOutDegDistr(vGraph, "test1a", "PlotCCdf=False, PowerFit=False", False, False)
    snap.PlotOutDegDistr(vGraph, "test1b", "PlotCCdf=True, PowerFit=False", True, False)
    snap.PlotOutDegDistr(vGraph, "test1c", "PlotCCdf=False, PowerFit=True", False, True)
    snap.PlotOutDegDistr(vGraph, "test1d", "PlotCCdf=True, PowerFit=True", True, True)

    vGraph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.PlotOutDegDistr(vGraph, "test2a", "PlotCCdf=False, PowerFit=False", False, False)
    snap.PlotOutDegDistr(vGraph, "test2b", "PlotCCdf=True, PowerFit=False", True, False)
    snap.PlotOutDegDistr(vGraph, "test2c", "PlotCCdf=False, PowerFit=True", False, True)
    snap.PlotOutDegDistr(vGraph, "test2d", "PlotCCdf=True, PowerFit=True", True, True)

    vGraph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.PlotOutDegDistr(vGraph, "test3a", "PlotCCdf=False, PowerFit=False", False, False)
    snap.PlotOutDegDistr(vGraph, "test3b", "PlotCCdf=True, PowerFit=False", True, False)
    snap.PlotOutDegDistr(vGraph, "test3c", "PlotCCdf=False, PowerFit=True", False, True)
    snap.PlotOutDegDistr(vGraph, "test3d", "PlotCCdf=True, PowerFit=True", True, True)

    os.chdir("./..")

