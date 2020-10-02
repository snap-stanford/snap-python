PlotInvParticipRat (SWIG)
'''''''''''''''''''''''''

.. function:: PlotInvParticipRat(Graph, MaxEigVecs, TimeLimit, FNmPref, DescStr)
   :noindex:

Plots the inverse participation ratio. See the reference below for more details. The function creates three new files: 1) eigIPR.<*FNmPref*>.plt (the commands used to create the plot), 2) eigIPR.<*FNPref*>.png (the plot), and 3) eigIPR.<*FNmPref*>.tab (the plotting data)..

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *MaxEigVecs*: int (input)
    Maximum number of eigenvectors to return.
    
- *TimeLimit*: int (input)
    Maximum number seconds to search.
    
- *FNmPref*: string (input)
    File name preference for the plotted graph.

- *DescStr*: string (input)
    Description of the graph. The string should be non-empty.
  
Return value:

- None


For more info see: http://www.barabasilab.com/pubs/CCNR-ALB_Publications/200108-01_PhysRevE-SprectraRealWorld/200108-01_PhysRevE-SprectraRealWorld.pdf

The following example shows how to plot the inverse participation ratio of
an undirected graph of type :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.PlotInvParticipRat(UGraph, 50, 10, "example", "PlotInvParticipRat")

