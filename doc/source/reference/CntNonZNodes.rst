CntNonZNodes 
''''''''''''

.. function:: CntNonZNodes (Graph) 

Returns the number of nodes in *Graph* with degree greater than 0.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value: 

- int
    The number of nodes in *Graph* with degree greater than 0

The following example shows how to calculate the number of non-zero nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    CntNonZNodes = snap.CntNonZNodes (Graph)
    print CntNonZNodes

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    CntNonZNodes = snap.CntNonZNodes (Graph)
    print CntNonZNodes

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    CntNonZNodes = snap.CntNonZNodes (Graph)
    print CntNonZNodes

