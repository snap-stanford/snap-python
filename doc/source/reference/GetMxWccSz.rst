GetMxWccSz
''''''''''

.. function:: GetMxWccSz(Graph)

Returns the fraction of nodes in the largest weakly connected component of a Graph.

Parameters:

 - *Graph*: graph (input)
     A Snap.py graph or a network.
 
Return value:

 - float: 
     The fraction of nodes in the largest weakly connected component of a graph

The following code shows how to calculate the relative size of the maximum weakly connected component for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

  import snap

  # Directed Graph
  G1 = snap.GenRndGnm(snap.PNGraph, 20, 10)
  print 'Size WCC of G1:', snap.GetMxWccSz(G1)

  # Undirected Graph
  G2 = snap.GenRndGnm(snap.PUNGraph, 20, 10)
  print 'Size WCC of G2:', snap.GetMxWccSz(G2)

  # Network
  G3 = snap.GenRndGnm(snap.PNEANet, 20, 10)
  print 'Size WCC of G3:', snap.GetMxWccSz(G3)
