GetMxWccSz
''''''''''

.. function:: GetMxWccSz(Graph)

Returns the fraction of nodes in the largest weakly connected component of a Graph.

Parameters:

 - *Graph*: graph (input)
     A Snap.py graph or a network.
 
Return value:

 - float 
     The fraction of nodes in the largest weakly connected component of a graph.
     

The following code shows how to calculate the relative size of the maximum weakly connected component for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

  import snap

  Graph = snap.GenRndGnm(snap.PNGraph, 20, 10)
  print 'Relative size of WCC in Directed Graph:', snap.GetMxWccSz(Graph)

  UGraph = snap.GenRndGnm(snap.PUNGraph, 20, 10)
  print 'Relative size of WCC in Undirected Graph:', snap.GetMxWccSz(UGraph)

  Network = snap.GenRndGnm(snap.PNEANet, 20, 10)
  print 'Relative size of WCC in Network:', snap.GetMxWccSz(Network)
