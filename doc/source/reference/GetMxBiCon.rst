GetMxBiCon
'''''''''''

.. function:: GetMxBiCon(Graph, RenumberNodes = false)

Returns a graph representing the largest bi-connected component on an undirected Graph. 

Parameters:

- *Graph*: PUNGraph (input)
    A Snap.py undirected graph

- *RenumberNodes*: Boolean (input)
    Optional renumbering. If true, the nodes in the resulting subgraph are renumbered from 0 to N-1

Return value:

- PUNGraph (output)
    A graph representing the largest bi-connected component on an undirected Graph. 
	
GetMxBiCon currently has a bug which causes an error if GetMxBiCon is called with more than one argument. For example, GetMxBiCon(Graph) will work, but GetMxBiCon(Graph, True) or GetMxBiCon(Graph, False) will cause an error.

An undirected graph is bi-connected if by removing any single node does not disconnect the graph. See http://en.wikipedia.org/wiki/Biconnected_component for more details.

The following example shows how to get the largest bi-connected component::

    from snap import *

    Graph = GenRndGnm(PUNGraph, 10, 10)

    # This executes correctly without an error message
    subGraph = GetMxBiCon(Graph)
    #subGraph = GetMxBiCon(Graph, False)

    print "Original Graph"
    for NI in Graph.Nodes():
        print "Node: %d" % NI.GetId()
        for Id in NI.GetOutEdges():
            print "edge (%d, %d)" % (NI.GetId(), Id)

    print "\nLargest bi-connected component"
    for NI in subGraph.Nodes():
        print "Node: %d" % NI.GetId()
        for Id in NI.GetOutEdges():
            print "edge (%d, %d)" % (NI.GetId(), Id)
        
