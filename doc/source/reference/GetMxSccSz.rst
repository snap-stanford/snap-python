GetMxSccSz
''''''''''

.. function:: GetMxSccSz(Graph)

Returns the fraction of nodes in the largest strongly connected component of a *Graph*.

Parameters:

 - *Graph*: graph (input)
     A Snap.py graph or a network.
 
Return value:

 - float
     The fraction of nodes in the largest strongly connected component of a graph.


The following code shows how to calculate the relative size of the maximum strongly connected component for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

  import snap

  Graph = snap.GenRndGnm(snap.PNGraph, 20, 10)
  print 'Size SCC of Directed Graph: %d' % snap.GetMxSccSz(Graph)

  UGraph = snap.GenRndGnm(snap.PUNGraph, 20, 10)
  print 'Size SCC of Undirected Graph: %d' % snap.GetMxSccSz(UGraph)

  Network = snap.GenRndGnm(snap.PNEANet, 20, 10)
  print 'Size SCC of Network: %d' % snap.GetMxSccSz(Network)
