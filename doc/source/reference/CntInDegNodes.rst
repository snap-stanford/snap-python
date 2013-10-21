CntInDegNodes
'''''''''''''''''''

.. function:: CntInDegNodes(Graph, NodeInDeg)

Returns the number of nodes in *Graph* with in-degree *NodeInDeg*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NodeInDeg*: int (input)
    The in-degree of the nodes to be counted

Return value:

- int
    The number of nodes in *Graph* with in-degree *NodeInDeg*


The following example shows how to get the number of nodes with in-degrees 10, 20 and 5 in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::
    
    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    nodeCount = snap.CntInDegNodes(Graph, 10)
    print nodeCount

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    nodeCount = snap.CntInDegNodes(Graph, 20)
    print nodeCount

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    nodeCount = snap.CntInDegNodes(Graph, 5)
    print nodeCount
