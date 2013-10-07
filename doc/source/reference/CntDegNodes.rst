CntDegNodes
'''''''''''''''''''

.. function:: CntDegNodes(Graph, NodeDeg)

Returns the number of nodes with degree NodeDeg.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NodeDeg*: int (input)
    The value of degree to be found in *Graph*

Return value:

- TInt (output)
	Integer with the number of nodes with degree equals to *NodeDeg*


The following example shows how to use CntDegNodes for Graphs in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::
    
	import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    nodeCount = snap.CntDegNodes(Graph, 10)
    print nodeCount

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    nodeCount = snap.CntDegNodes(Graph, 20)
    print nodeCount

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    nodeCount = snap.CntDegNodes(Graph, 5)
    print nodeCount
