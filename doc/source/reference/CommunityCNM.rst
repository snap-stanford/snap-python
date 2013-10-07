.. 55_CommunityCNM.txt

************
CommunityCNM
************

CommunityCNM (Graph, CmtyV)

Clauset-Newman-Moore community detection method for large networks. At every step of the algorithm two communities that contribute maximum positive value to global modularity are merged. See: Finding community structure in very large networks, A. Clauset, M.E.J. Newman, C. Moore, 2004

Parameters:

* Graph: PUNGraph (input)
  A Snap.py PUNGraph or a network

* CmtyV: vector of CnComs (vector of vector of integers) (output)
  A vector of all the communities that are detected by the CNM method. Each community is represented as a vector of node IDs.

Return value:

* Float: The modularity of the network.

The following example shows how to get all the communities detected in a given graph::

  import snap

  Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
  CmtyV = snap.TCnComV()
  QModularity = CommunityCNM(Graph, CmtyV)
  print "The communities are as follows: "
  for Cmty in CmtyV:
    print "Community: "
    for NI in Cmty:
      print NI
  print "The modularity of the network is ", QModularity
