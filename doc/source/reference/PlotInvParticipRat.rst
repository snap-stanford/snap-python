PlotInvParticipRat
''''''''''''''''''

.. function:: PlotInvParticipRat(MaxEigVecs, TimeLimit, FNmPref, DescStr)

A graph method for undirected graphs that plots the inverse participation ratio. See the reference below for more details. The function creates three new files: 1) eigIPR.<*FNmPref*>.plt (the commands used to create the plot), 2) eigIPR.<*FNPref*>.png (the plot), and 3) eigIPR.<*FNmPref*>.tab (the plotting data)..

Parameters:

- *MaxEigVecs*: int
    Maximum number of eigenvectors to return.
    
- *TimeLimit*: int
    Maximum number seconds to search.
    
- *FNmPref*: string
    File name preference for the plotted graph.

- *DescStr*: string
    Description of the graph. The string should be non-empty.
  
Return value:

- None


For more info see: http://www.barabasilab.com/pubs/CCNR-ALB_Publications/200108-01_PhysRevE-SprectraRealWorld/200108-01_PhysRevE-SprectraRealWorld.pdf

The following example shows how to plot the inverse participation ratio of
an undirected graph of type :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    UGraph.PlotInvParticipRat(50, 10, "example", "PlotInvParticipRat")

