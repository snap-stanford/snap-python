GetMxWccSz
''''''''''
.. note::

    This page is a draft and under revision.

.. function:: GetMxWccSz(Graph)

Computes the size of the largest weakly connected component in the graph
as a fraction of total number of nodes.

Parameters:

 - *Graph*: graph (input)
     A Snap.py graph or network.
 
Return value:

 - Float: relative size of the largest weakly connected component.
   Between 0 and 1.

The following code shows how to calculate the size of the maximum weakly connected component for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

  import snap

  # generate different graphs
  G1 = snap.GenRndGnm(snap.PNGraph, 20, 10)
  G2 = snap.GenRndGnm(snap.PUNGraph, 20, 10)
  G3 = snap.GenRndGnm(snap.PNEANet, 20, 10)

  # print results of GetMxWccSz
  print 'Size WCC of G1:', snap.GetMxWccSz(G1)
  print 'Size WCC of G2:', snap.GetMxWccSz(G2)
  print 'Size WCC of G3:', snap.GetMxWccSz(G3)

