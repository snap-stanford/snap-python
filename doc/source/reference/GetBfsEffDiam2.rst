
GetBfsEffDiam
*************

.. function:: double GetBfsEffDiam(Graph, NTestNode, IsDir, EffDiam, FullDiam, AvgSPL)

.. note::

    This function is not yet supported.

Returns the approximation of the effective diameter, the diameter, and
the average shortest path length in a graph. Does this by performing
BFS from NTestNodes random starting nodes.

Parameters:

* *Graph*: graph (input)

     A Snap.py graph or a network

* "NTestNode*: int

     Node to start BFS from

* *IsDir*: bool (input)

     Whether the graph is directed

* *EffDiam*: float (output)

     The effective diameter

* *FullDam*: int (output)

     The diameter

* *AvgSPL*: float (output)

     Average Shortest Path length

Return value:

* the effective diameter

.. note::

   In C++, you can pass references to doubles and ints.
   You cannot in python. THEREFORE, ONLY RELY ON THE RETURN VALUE FOR THE
   EFFECTIVE DIAMETER. Don't expect the variables you passed in to be
   populated to the correct values. Additionally, the following code will
   not actually run because the fourth argument does not match due to
   type error.

The following example shows how to calculate an effective diameter::

   import snap G = snap.GenRndGnm(snap.PUNGraph, 100, 1000); effDiam =
   snap.GetBfsEffDiam(G, 1, False, 0, 0, 0); print effDiam;
