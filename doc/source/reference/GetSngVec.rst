GetSngVec
'''''''''

.. function:: GetSngVec(Graph, LeftSV, RightSV)

Computes the leading left and right singular vectors of the adjacency matrix
representing a directed Graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py directed graph

- *LeftSV*: vector of floats (output)
    The left singular vector

- *RightSV*: vector of floats (output)
    The right singular vector

Return value:

- None

For more info see: http://en.wikipedia.org/wiki/Singular_value_decomposition

The following example shows how to calculate the left and right singular
vectors::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    LeftSV = snap.TFltV()
    RightSV = snap.TFltV()
    snap.GetSngVec(Graph, LeftSV, RightSV)

    print "Left singular vector:"
    for v in LeftSV:
      print v

    print "Right singular vector:"
    for v in RightSV:
      print v
