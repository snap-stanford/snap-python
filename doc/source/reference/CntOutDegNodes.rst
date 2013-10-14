CntOutDegNodes
'''''''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: int CntOutDegNodes(Graph, NodeOutDeg)

Returns the number of nodes with out-degree NodeOutDeg.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NodeOutDeg*: int (input)
    The value of out-degree to be found in *Graph*

Return value:

- int


The following example shows how to get the number of nodes with out-degree *NodeOutDeg* in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::
    
    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    nodeCount = snap.CntOutDegNodes(Graph, 10)
    print nodeCount

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    nodeCount = snap.CntOutDegNodes(Graph, 20)
    print nodeCount

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    nodeCount = snap.CntOutDegNodes(Graph, 5)
    print nodeCount
