GetMxSccSz
''''''''''

.. function:: GetMxSccSz(Graph)

Returns the fraction of nodes in the largest strongly connected component of a Graph.

Parameters:

 - *Graph*: graph (input)
     A Snap.py graph or a network.
 
Return value:

 - float: 
     The fraction of nodes in the largest strongly connected component of a graph

The following code shows how to calculate the relative size of the maximum strongly connected component for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

  import snap

  # Directed Graph
  G1 = snap.GenRndGnm(snap.PNGraph, 20, 10)
  print 'Size SCC of G1:', snap.GetMxSccSz(G1)


  # Undirected Graph
  G2 = snap.GenRndGnm(snap.PUNGraph, 20, 10)
  print 'Size SCC of G2:', snap.GetMxSccSz(G2)


  # Network
  G3 = snap.GenRndGnm(snap.PNEANet, 20, 10)
  print 'Size SCC of G3:', snap.GetMxSccSz(G3)
