PlotInDegDistr
'''''''''''

.. function:: PlotInDegDistr(Graph, FNmPref, DescStr=snap.TStr(), PlotCCdf=False, PowerFit=False)

Plots the in-degree distribution of *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *FNmPref*: snap.TStr (input)
    File name

- *DescStr*: snap.TStr (input)
    Description string to be added to the plot title

- *PlotCCdf*: bool (input)
    Plots the distribution as a Complementary Cummulative distribution function

- *PowerFit*: bool (input)
    Fits a Power-Law to the distribution

Return value:

- None

Output:

- inDeg.*FNmPref*.eps 
	Encapsulated PostScript plot

- inDeg.*FNmPref*.plt
	Gnuplot script to generate plot

- inDeg.*FNmPref*.tab
	Table of in-degree count

For more info see: http://www.gnuplot.info

The following example shows how generate a plot of the in-degree distribution for a random graph

    import snap

    G = snap.GenRndGnm(snap.PNGraph, 100, 1000)

    snap.PlotInDegDistr(G, "random_plot", "Plot of in-degree Distribution")
