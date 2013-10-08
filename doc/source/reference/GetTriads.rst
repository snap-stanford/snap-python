GetTriads
'''''''''

.. function:: GetTriads(Graph, SampleNodes=-1)

.. note::

    This function is not yet supported.

Computes the number of triads in the graph.

Parameters:

 - *Graph*: graph
     A directed or undirected graph, or a network.
 
 - *SampleNodes*: int (optional)
    If !=-1 then compute triads only for a random sample of SampleNodes nodes. Useful for approximate but quick computations.

Return value:

 - Integer: Number of triads

The following code shows an example of GetTriads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

  import snap
  # generate graphs
  G1 = snap.GenRndGnm(snap.PNGraph, 100, 250)
  G2 = snap.GenRndGnm(snap.PUNGraph, 100, 250)
  G3 = snap.GenRndGnm(snap.PNEANet, 100, 250)

  # Print results of GetTriads
  print 'Number of triads in G1 with 50 sample nodes:', snap.GetTriads(G1, 50)
  print 'Number of triads in G1 with 100 sample nodes:', snap.GetTriads(G1, 100)
  print 'Number of triads in G2 without sample nodes:', snap.GetTriads(G1)
  print 'Number of triads in G2:', snap.GetTriads(G2)
  print 'Number of triads in G3:', snap.GetTriads(G3)


