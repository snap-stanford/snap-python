GetTriads
'''''''''

.. function:: GetTriads(SampleNodes=-1)

A graph method that computes the number of triads in the graph.

Parameters:

 - (optional) *SampleNodes*: int
    If *SampleNodes* is -1 (default value), then compute triads over all the nodes. Otherwise, compute triads using only a random sample of *SampleNodes* nodes. This is useful for quick, but approximate computations.

Return value:

 - int
     Number of triads.


The following code shows an example of GetTriads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

  import snap

  Graph = snap.GenRndGnm(snap.TNGraph, 100, 250)
  NumTriads = Graph.GetTriads(50)
  print('Number of triads with 50 sample nodes: %d' % NumTriads)

  UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 250)
  NumTriads = UGraph.GetTriads(75)
  print('Number of triads with 75 sample nodes: %d' % NumTriads)

  Network = snap.GenRndGnm(snap.TNEANet, 100, 250)
  NumTriads = Network.GetTriads(100)
  print('Number of triads with 100 sample nodes: %d' % NumTriads)


