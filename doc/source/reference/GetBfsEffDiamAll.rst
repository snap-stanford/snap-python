GetBfsEffDiamAll
''''''''''''''''

.. function:: GetBfsEffDiamAll(NTestNode, IsDir)

A graph method that returns the approximation of the effective diameter, the diameter, and the average shortest path length in a graph. Does this by performing
BFS from *NTestNodes* random starting nodes.

Parameters:

- *NTestNodes*: int
    The number of random start nodes to use in the BFS used to calculate the graph diameter and effective diameter.

- *IsDir*: bool
    Indicates whether the edges should be considered directed or undirected.

Return value:

- list: [ float, float, int, float ]
    The list contains four elements: the first and the second element are
    the effective diameter of the graph, the third element is the diameter,
    and the fourth element is the average shortest path length.

The following example shows how to calculate an effective diameter::

   import snap

   Graph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
   result = Graph.GetBfsEffDiamAll(10, False)
   print(result)

   UGraph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
   result = UGraph.GetBfsEffDiamAll(10, False)
   print(result)

   Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
   result = Network.GetBfsEffDiamAll(10, False)
   print(result)

