CntDegNodes
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: int CntDegNodes(Graph, NodeDeg)

Returns the number of nodes in *Graph* with degree *NodeDeg*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network
    
- *NodeDeg*: int (input)
    The degree of the nodes to be counted

Return value:

- int

The following example shows how to get the number of nodes with degree *NodeDeg* in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    nodeCount = snap.CntDegNodes(Graph, 20)
    print nodeCount

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    nodeCount = snap.CntDegNodes(Graph, 20)
    print nodeCount

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    nodeCount = snap.CntDegNodes(Graph, 20)
    print nodeCount
