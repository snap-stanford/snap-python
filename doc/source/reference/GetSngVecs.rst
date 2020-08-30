GetSngVecs
'''''''''''

.. function:: GetSngVecs(SngVecs)

A graph method that computes the singular values and left and right singular vectors of the adjacency matrix representing a directed graph.

Parameters:

- SngVecs: int
    The number of singular values/vectors to compute

Return value:

- SngValV: :class:`TFltV`
    Computed singular values stored as a vector of floats

- LeftSV: :class:`TFltVFltV`
    Computed left singular vectors stored as a vector of vectors of floats

- RightSV: :class:`TFltVTFltV`
    Computed right singular vectors stored as a vector of vectors of floats

The following example shows how to fetch the in-degrees for nodes in
:class:`TNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    SngVecs = 5
    SngValV, LeftSV, RightSV = Graph.GetSngVecs(SngVecs)
    for value in SngValV:
        print("Singular value: %f" % value)
    for vector in LeftSV:
        for value in vector:
            print("Left Singular Vector Value %f" % value)
    for vector in RightSV:
        for value in vector:
            print("Right Singular Vector Value %f" % value)
