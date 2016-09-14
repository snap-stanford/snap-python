Table to Graph Conversion Functions
```````````````````````````````````

One of the most common operations when processing large datasets in SNAP is to load the dataset into :class:`TTable` objects, and then construct graphs out of the tables to run SNAP's graph algorithms. The conversion functions, defined in namespace TSnap, provide the functionality to do this.

Note that all the functions discussed below have both sequential and parallel implementations. The example code uses the sequential implementations; to use the parallelized functions (on a system which supports OpenMP), simply add MP to the function name (example, ToGraphMP and ToNetworkMP).

.. function:: ToNetwork(GraphType, PTable Table, const TStr& SrcCol, const TStr& DstCol, TStrV& EdgeAttrV, PTable NodeTable, const TStr& NodeCol, TStrV& NodeAttrV, TAttrAggr AggrPolicy)

Converts the edge and node tables to a network in SNAP, by looking at columns *SrcCol* and *DstCol* of *Table*, and at *NodeCol* of *NodeTable*
*EdgeAttrV* specifies a list of columns in *Table* which contain edge attributes. *NodeAttrV* specifies a list of columns in *NodeTable* which correspond to node attributes.
It is recommended to have a separate, explicit, node table, and to use this method, when it is desired to add separate node and edge attributes.

Parameters:

- *GraphType*: module name (input)
    The class of network we want to create (usually snap.PNEANet)

- *Table*: :class:`TTable` (input)
    An instance of :class:`TTable` which contains the edges from which we want to construct a graph.

- *SrcCol*: string (input)
    The name of the column in the edge table which contains the source nodes.

- *DstCol*: string (input)
    The name of the column in the edge table which contains the destination nodes.

- *EdgeAttrV*: TStrV (vector of strings) (input)
    A list of names of columns in the edge table which correspond to edge attributes.

- *NodeTable*: :class:`TTable` (input)
    An instance of :class:`TTable` which contains the nodes of our graph.

- *NodeCol*: string (input)
    The name of the column in the node table which contains the node ids.

- *NodeAttrV*: TStrV (vector of strings) (input)
     A list of names of columns in the node table which correspond to node attributes.

- *AggrPolicy*: :class:`TAttrAggr` (input)
    The aggregation policy for attributes. It is not usually relevant for graphs (as opposed to networks), and can be safely set to snap.aaFirst by default.

Return value:

- *Net*: The constructed network.

The following code shows example usage::
    
    import snap

    edgefilename = "/path/to/edges.txt"  # A file containing the graph, where each row contains an edge
                                         # and each edge is represented with the source and dest node ids,
                                         # and the edge attributes, separated by a tab.

    nodefilename = "/path/to/nodes.txt"  # A file containing the nodes of a graph. Each row contains a node id,
                                         # and (optionally) node attributes.


    context = snap.TTableContext()  # When loading strings from different files, it is important to use the same context
                                    # so that SNAP knows that the same string has been seen before in another table.

    edgeschema = snap.Schema()
    edgeschema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
    edgeschema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
    edgeschema.Add(snap.TStrTAttrPr("edgeattr1", snap.atStr))
    edgeschema.Add(snap.TStrTAttrPr("edgeattr2", snap.atStr))

    nodeschema = snap.Schema()
    nodeschema.Add(snap.TStrTAttrPr("nodeID", snap.atStr))
    nodeschema.Add(snap.TStrTAttrPr("nodeattr1", snap.atStr))
    nodeschema.Add(snap.TStrTAttrPr("nodeattr2", snap.atStr))

    edge_table = snap.TTable.LoadSS(edgeschema, edgefilename, context, "\t", snap.TBool(False))
    node_table = snap.TTable.LoadSS(nodeschema, nodefilename, context, "\t", snap.TBool(False))

    # In this example, we add both edge attributes to the network, but only one node attribute.
    edgeattrv = snap.TStrV()
    edgeattrv.Add("edgeattr1")
    edgeattrv.Add("edgeattr2")

    nodeattrv = snap.TStrV()
    nodeattrv.Add("nodeattr1")

    # net will be an object of type snap.PNEANet
    net = snap.ToNetwork(snap.PNEANet, edge_table, "srcID", "dstID", edgeattrv, node_table, "nodeID", nodeattrv, snap.aaFirst)


.. function:: ToNetwork(GraphType, PTable Table, const TStr& SrcCol, const TStr& DstCol, TStrv& SrcAttrv, TStrV& DstAttrV, TStrV& EdgeAttrV, TAttrAggr AggrPolicy)

Converts the edge table to a network in SNAP, by looking at columns *SrcCol* and *DstCol* of *Table*.
*EdgeAttrV* specifies a list of columns in *Table* which contain edge attributes. *SrcAttrV* and *DstAttrV* specifies the attributes of the source and destination columns.
Note: it is NOT recommended to use this method if there are node attributes to be added. Please see the overloaded method above which has a separate, explicit, node table.

Parameters:

- *GraphType*: module name (input)
    The class of network we want to create (usually snap.PNEANet)

- *Table*: :class:`TTable` (input)
    An instance of :class:`TTable` which contains the edges from which we want to construct a graph.

- *SrcCol*: string (input)
    The name of the column in the edge table which contains the source nodes.

- *DstCol*: string (input)
    The name of the column in the edge table which contains the destination nodes.

- *SrcAttrV*: TStrV (vector of strings) (input)
    A list of names of columns in the edge table which correspond to attributes of the source node.

- *DstAttrV*: TStrV (vector of strings) (input)
    A list of names of columns in the edge table which correspond to attributes of the destination node.

- *EdgeAttrV*: TStrV (vector of strings) (input)
    A list of names of columns in the edge table which correspond to edge attributes.

- *AggrPolicy*: :class:`TAttrAggr` (input)
    The aggregation policy for attributes. Can be safely set to snap.aaFirst by default.

Return value:

- *Net*: The constructed network.

The following code shows example usage::
    
    import snap

    edgefilename = "/path/to/edges.txt"  # A file containing the graph, where each row contains an edge
                                         # and each edge is represented with the source and dest node ids,
                                         # the edge attributes, and the source and destination node attributes
                                         # separated by a tab.


    context = snap.TTableContext()  # When loading strings from different files, it is important to use the same context
                                    # so that SNAP knows that the same string has been seen before in another table.

    schema = snap.Schema()
    schema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
    schema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
    schema.Add(snap.TStrTAttrPr("edgeattr1", snap.atStr))
    schema.Add(snap.TStrTAttrPr("edgeattr2", snap.atStr))
    schema.Add(snap.TStrTAttrPr("srcnodeattr1", snap.atStr))
    schema.Add(snap.TStrTAttrPr("srcnodeattr2", snap.atStr))
    schema.Add(snap.TStrTAttrPr("dstnodeattr1", snap.atStr))
    schema.Add(snap.TStrTAttrPr("dstnodeattr2", snap.atStr))

    table = snap.TTable.LoadSS(chema, edgefilename, context, "\t", snap.TBool(False))

    # In this example, we add both edge attributes to the network, 
    # but only one src node attribute, and no dst node attributes.
    edgeattrv = snap.TStrV()
    edgeattrv.Add("edgeattr1")
    edgeattrv.Add("edgeattr2")

    srcnodeattrv = snap.TStrV()
    srcnodeattrv.Add("srcnodeattr1")

    dstnodeattrv = snap.TStrV()

    # net will be an object of type snap.PNEANet
    net = snap.ToNetwork(snap.PNEANet, table, "srcID", "dstID", srcnodeattrv, dstnodeattrv, edgeattrv, snap.aaFirst)


.. function:: ToGraph(GraphType, PTable Table, const TStr& SrcCol, const TStr& DstCol, TAttrAggr AggrPolicy)

Converts the table to a graph in SNAP, by looking at columns *SrcCol* and *DstCol* of *Table*. Whenever a new node is seen, it is implicitly added to the graph automatically.

Parameters:

- *GraphType*: module name (input)
    The class of graph we want to create (usually snap.PNGraph)

- *Table*: :class:`TTable` (input)
    An instance of :class:`TTable` from which we want to construct a graph.

- *SrcCol*: string (input)
    The name of the column in the table which contains the source nodes.

- *DstCol*: string (input)
    The name of the column in the table which contains the destination nodes.

- *AggrPolicy*: :class:`TAttrAggr` (input)
    The aggregation policy for attributes. It is not usually relevant for graphs (as opposed to networks), and can be safely set to snap.aaFirst by default.

Return value:

- *Graph*: The constructed graph.

The following code shows example usage::
    
    import snap

    graphfilename = "/path/to/graph.txt" # A file containing the graph, where each row contains an edge
                                         # and each edge is represented with the source and dest node ids
                                         # separated by a tab.
    schema = snap.Schema()
    context = snap.TTableContext()
    schema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
    schema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
    sample_table = snap.TTable.LoadSS(schema, graphfilename, context, "\t", snap.TBool(False))

    # graph will be an object of type snap.PNGraph
    graph = snap.ToGraph(snap.PNGraph, sample_table, "srcID", "dstID", snap.aaFirst)

.. function:: LoadModeNetToNet(PMMNet Graph, const TStr& Name, PTable Table, const TStr& NCol, TStrV& NodeAttrV)

Loads a mode, with name Name, into the PMMNet from the TTable. NCol specifies the node id column and NodeAttrV the node attributes.

Parameters:

- *Graph*: :class:`TMMNet` (input)
    The multimodal network to which we want to add the mode.

- *Name*: string (input)
    This specifies the name to use for the constructed :class:`TModeNet`.

- *Table*: :class:`TTable` (input)
    The table from which we load the node ids.

- *NCol*: string (input)
    The column in the table which has the node ids.

- *NodeAttrV*: TStrV (vector of strings)
    A vector of column names corresponding to node attributes.

The following code shows example usage::

    import snap

    # Create an mmnet
    mmnet = snap.TMMNet.New()

    nodefilename = "/path/to/nodes.txt"  # A file containing the nodes of a graph. Each row contains a node id,
                                         # and (optionally) node attributes.


    context = snap.TTableContext() 

    nodeschema = snap.Schema()
    nodeschema.Add(snap.TStrTAttrPr("nodeID", snap.atStr))
    nodeschema.Add(snap.TStrTAttrPr("nodeattr1", snap.atStr))
    nodeschema.Add(snap.TStrTAttrPr("nodeattr2", snap.atStr))

    node_table = snap.TTable.LoadSS(nodeschema, nodefilename, context, "\t", snap.TBool(False))

    # In this example, we add just one of the node attributes from the table to the TMMNet
    nodeattrv = snap.TStrV()
    nodeattrv.Add("nodeattr1")

    # This will add a new mode net called "Mode1" to the mmnet.
    snap.LoadModeNetToNet(mmnet, "Mode1", node_table, "nodeID", nodeattrv)

.. function:: LoadCrossNetToNet(PMMNet Graph, const TStr& Mode1, const TStr& Mode2, const TStr& CrossName, PTable Table, const TStr& SrcCol, const TStr& DstCol, TStrV& EdgeAttrV)

Loads a crossnet from Mode1 to Mode2, with name CrossName, into the PMMNet from the given TTable. SrcCol and DstCol specify the source and destination node id columns, and EdgeAttrV specifies the columns with edge attributs.

Parameters:

- *Graph*: :class:`TMMNet` (input)
    The multimodal network to which we want to add the mode.

- *Mode1*: string (input)
    This specifies the name of the source :class:`TModeNet`.

- *Mode2*: string (input)
    This specifies the name of the destination :class:`TModeNet`.

- *CrossName*: string (input)
    This specifies the name to use for the constructed :class:`TCrossNet`.

- *Table*: :class:`TTable` (input)
    The table from which we load the edges.

- *SrcCol*: string (input)
    The column in the table which has the source node id of each edge.

- *DstCol*: string (input)
    The column in the table which has the destination node id of each edge.

- *EdgeAttrV*: TStrV (vector of strings)
    A vector of column names corresponding to edge attributes.

The following code shows example usage::

    import snap

    # Create an mmnet
    mmnet = snap.TMMNet.New()


    edgefilename = "/path/to/edges.txt"  # A file containing the graph, where each row contains an edge
                                         # and each edge is represented with the source and dest node ids,
                                         # and the edge attributes, separated by a tab.


    context = snap.TTableContext() 

    edgeschema = snap.Schema()
    edgeschema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
    edgeschema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
    edgeschema.Add(snap.TStrTAttrPr("edgeattr1", snap.atStr))
    edgeschema.Add(snap.TStrTAttrPr("edgeattr2", snap.atStr))

    edge_table = snap.TTable.LoadSS(edgeschema, edgefilename, context, "\t", snap.TBool(False))

    # In this example, we add both edge attributes to the network
    edgeattrv = snap.TStrV()
    edgeattrv.Add("edgeattr1")
    edgeattrv.Add("edgeattr2")

    # This will add a new cross net called "Cross1" to the mmnet, from "Mode1" to "Mode2".
    snap.LoadCrossNetToNet(mmnet, "Mode1", "Mode2", "Cross1", edge_table, "srcID", "dstID", edgeattrv)
