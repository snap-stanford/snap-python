SaveEdgeListNet
'''''''''''''''

.. function:: SaveEdgeList(Graph, Filename, Description)

Saves the *Graph* of type `PNEANet` to the file with name *Filename*.

The saved file will have the following format:

The file begins with the given description and some stats on the network (each line will begin with a '#', designating it as a comment).

The file consists of columns separated by tabs. There will be a node section, which begins with a schema line, and ends with the  sentinel. The node schema line will begin with the term '#NODES', followed by a list of attribute names and type. The keyword 'NId' should be used to designate the column containing the node ids. The schema would look like: #NODES \t NId \t <attribute_1>:<type_1> .... Types will be either 'Int', 'Flt', or 'Str'. If a node has no value for a given attribute, the term '__null__' will be used instead. The sentinel term, '#END', will follow, on a separate line, after all nodes and their attributes have been specified.

The edge section is similar to the nodes section, begining with a schema line and ending with an optional sentinel, '#END'. The edge schema line begins with '#EDGES', followed by a list of attribute names and types. The keywords 'SrcNId' and 'DstNId' are used to designate the columns containing the source and destination node ids for the given edge. An example schema would look like: #EDGES \t SrcNId \t DstNId \t <attribute_1>:<type_1> .... Like with nodes, if an edge does not have a value for a given attribute, the term '__null__' is instead.

Parameters:

- *Graph*: graph (input) 
    A graph of type `PNEANet`.

- *Filename*: string (input)
    The name of the file to save the graph to.
	
- *Description*: string (input)
    An description that will be written to the top of the file in a commented section.

Return value: 

- None


The following example shows how to save edge lists with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Network.AddIntAttrN('Attr1')
    for i in range(100):
      Network.AddIntAttrDatN(i, 2*i, 'Attr1')
    snap.SaveEdgeListNet(Network, 'network_mygraph.txt')
