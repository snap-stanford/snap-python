GetBfsEffDiamAll (SWIG)
'''''''''''''''''''''''

.. function:: GetBfsEffDiamAll(Graph, NTestNode, IsDir)
   :noindex:

Returns the approximation of the effective diameter, the diameter, and
the average shortest path length in a graph. Does this by performing
BFS from *NTestNodes* random starting nodes.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NTestNodes*: int (input)
    The number of random start nodes to use in the BFS used to calculate the graph diameter and effective diameter.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

Return value:

- list: [ float, float, int, float ]
    The list contains four elements: the first and the second element are
    the effective diameter of the graph, the third element is the diameter,
    and the fourth element is the average shortest path length.

The following example shows how to calculate an effective diameter::

   import snap

   G = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
   result = snap.GetBfsEffDiamAll(G, 10, False)
   print(result)

   G = snap.GenRndGnm(snap.PNGraph, 100, 1000)
   result = snap.GetBfsEffDiamAll(G, 10, False)
   print(result)

   G = snap.GenRndGnm(snap.PNEANet, 100, 1000)
   result = snap.GetBfsEffDiamAll(G, 10, False)
   print(result)

