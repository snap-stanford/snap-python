GetLeadSngVec
'''''''''''''

.. function:: GetLeadSngVec()

A graph method that computes the leading left and right singular vectors of the adjacency matrix
representing a directed graph.

Parameters:

- None

Return value:

- *LeftSV*: :class:`TFltV`, a vector of floats
    The left singular vector.

- *RightSV*: :class:`TFltV`, a vector of floats
    The right singular vector.

For more info see: http://en.wikipedia.org/wiki/Singular_value_decomposition

The following example shows how to calculate the left and right singular
vectors::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    LeftSV, RightSV = Graph.GetLeadSngVec()

    print("Left singular vector:")
    for item in LeftSV:
        print(item)

    print("Right singular vector:")
    for item in RightSV:
        print(item)
