PlotInvParticipRat
''''''''''''''''''

.. function:: PlotInvParticipRat(Graph, MaxEigVecs, TimeLimit, FNmPref, DescStr)

Plots the inverse participation ratio. See Spectra of "real-world" graphs: Beyond the semicircle law by Farkas, Derenyi, Barabasi and Vicsek. The function creates three new files: 1) eigIPR.<*FNmPref*>.plt (the plot), 2) eigIPR.<*FNmPref*>.eps (the plotting description), and 3) eigIPR.<*FNmPref*>.tab (the tab separated plotting data).

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph

- *MaxEigVecs*: int (input)
    Maximum number of eigenvectors to return
    
- *TimeLimit*: int (input)
    Maximum number seconds to search
    
- *FNmPref*: string (input)
    File name preference for the plotted graph

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.
  
Return value:

- None

For more info see: http://www.barabasilab.com/pubs/CCNR-ALB_Publications/200108-01_PhysRevE-SprectraRealWorld/200108-01_PhysRevE-SprectraRealWorld.pdf

The following example shows how to plot the inverse participation ratio of
an undirected graph of type :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotInvParticipRat(Graph, 50, 10, "example", "PlotInvParticipRat")

