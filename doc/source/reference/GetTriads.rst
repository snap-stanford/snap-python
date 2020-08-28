GetTriads
'''''''''

.. function:: GetTriads(SampleNodes=-1)

Computes the number of triads in the graph.

Parameters:

 - *SampleNodes*: int
    If !=-1 then compute triads only for a random sample of *SampleNodes* nodes. Useful for approximate but quick computations.

Return value:

 - int
     Number of triads.


The following code shows an example of GetTriads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

  import snap

  Graph = snap.GenRndGnm(snap.PNGraph, 100, 250)
  NumTriads = Graph.GetTriads(50)
  print('Number of triads with 50 sample nodes: %d' % NumTriads)

  UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 250)
  NumTriads = UGraph.GetTriads(75)
  print('Number of triads with 75 sample nodes: %d' % NumTriads)

  Network = snap.GenRndGnm(snap.PNEANet, 100, 250)
  NumTriads = Network.GetTriads(100)
  print('Number of triads with 100 sample nodes: %d' % NumTriads)


