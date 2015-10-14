Graph and Network Classes
`````````````````````````

Graphs and networks in SNAP are represented as undirected graphs :class:`TUNGraph`, directed graphs :class:`TNGraph` and multigraphs with attributes :class:`TNEANet`.

TUNGraph
========

.. class:: TUNGraph()
           TUNGraph(Nodes, Edges)
           TUNGraph(Graph)

   Returns a new undirected graph. If no parameters are provided,
   an empty graph is created. If *Nodes* and *Edges* are specified, space
   is preallocated for *Nodes* nodes and *Edges* edges. If *Graph* is specified,
   the new graph is a copy of the input graph.

   Nodes have IDs, which are arbitrary non-negative integers. Nodes and edges
   have no attributes/data associated with them. There is at most one
   undirected edge between a pair of nodes. Self loops (one per node) are
   allowed but multiple (parallel) edges are not. The undirected graph data
   structure is implemented using sorted adjacency lists. This means adding
   a node takes constant time, while adding an edge takes linear time (since
   adjacency list is kept sorted) in the node degree. Accessing arbitrary
   node takes constant time and accessing any edge takes logarithmic time
   in the node degree. 

   :class:`TUNGraph` provides iterators for fast traversal of nodes and edges.
   Iterator classes are :class:`TUNGraphNodeI` for iterating over nodes and
   :class:`TUNGraphEdgeI` for iterating over edges.

   :class:`TUNGraph` provides the following methods:

     .. describe:: New()

        Returns a pointer to a new graph.

     .. describe:: New(Nodes, Edges)

        Returns a pointer to a new graph and reserves enough memory for
        *Nodes* nodes and *Edges* edges.

     .. describe:: Load(SIn)

        Loads a graph from a binary stream *SIn* and returns a pointer to it. 

     .. describe:: Save(SOut)

        Saves the graph to a binary stream *SOut*. 

     .. describe:: Nodes()

        Returns a generator for the nodes in the graph.

     .. describe:: GetNodes()

        Returns the number of nodes in the graph. 

     .. describe:: AddNode(NId)

        Adds a node of ID *NId* to the graph, *NId* is an integer.
        Returns node ID. If NId is -1, node ID is automatically assigned.
        It throws an exception, if a node with ID *NId* already exists. 

     .. describe:: AddNode(NodeI)

        Adds a node of ID *NodeI.GetId()* to the graph. *NodeI* is a node iterator. Returns node ID.

     .. describe:: DelNode(NId)

        Deletes node of ID *NId* from the graph. *NId* is an integer.

     .. describe:: DelNode(NodeI)

        Deletes node of ID *NodeI.GetId()* from the graph. *NodeI* is a node iterator.

     .. describe:: IsNode(NId)

        Returns true, if ID *NId* is a node in the graph.

     .. describe:: BegNI()

        Returns a node iterator referring to the first node in the graph. 

     .. describe:: EndNI()

        Returns a node iterator referring to the past-the-end node in the graph.

     .. describe:: GetNI(NId)

        Returns a node iterator referring to the node of ID *NId* in the graph. 

     .. describe:: GetMxNId()

        Returns the maximum ID of a any node in the graph.

     .. describe:: GetRndNId()

        Returns an ID of a random node in the graph. 

     .. describe:: GetRndNI()

        Returns a node interator referring to a random node in the graph. 

     .. describe:: Edges()

        Returns a generator for the edges in the graph.

     .. describe:: GetEdges()

        Returns the number of edges in the graph. 

     .. describe:: AddEdge(SrcNId, DstNId)

        Adds an edge between node IDs *SrcNId* and *DstNId* to the graph.
        Returns -1, if the edge was successfully added. Returns -2, if the
        edge already exists. The function throws an exception, if *SrcNId*
        or *DstNId* are not nodes in the graph. 

     .. describe:: AddEdge(EdgeI)

        Adds an edge between *EdgeI.GetSrcNId()* and *EdgeI.GetDstNId()* to the graph. *EdgeI* is an edge iterator. Returns -1, if successful. Returns -2, otherwise.

     .. describe:: DelEdge(SrcNId, DstNId)

        Deletes an edge between node IDs *SrcNId* and *DstNId* from the graph.
        If the edge between *SrcNId* and *DstNId* does not exist in the graph,
        function still completes. But the function throws an exception,
        if *SrcNId* or *DstNId* are not nodes in the graph. 

     .. describe:: IsEdge(SrcNId, DstNId)

        Tests whether an edge between node IDs *SrcNId* and *DstNId* exists in the graph. 

     .. describe:: BegEI()

        Returns an edge iterator referring to the first edge in the graph. 

     .. describe:: EndEI()

        Returns an edge iterator referring to the past-the-end edge in the graph.

     .. describe:: GetEI(SrcNId, DstNId)

        Returns an edge iterator referring to edge between node IDs *SrcNId*
        and *DstNId* in the graph. Since this is an undirected graph
        *GetEI(SrcNId, DstNId)* has the same effect as *GetEI(DstNId, SrcNId)*.

     .. describe:: Empty()

        Returns true if the graph is empty, has zero nodes. 

     .. describe:: Clr()

        Deletes all nodes and edges from the graph. 

     .. describe:: Reserve(Nodes, Edges)

        Reserves memory for a graph of *Nodes* nodes and *Edges* edges. 

     .. describe:: ReserveNIdDeg(NId, Deg)

        Reserves memory for node ID *NId* having *Deg* edges. 

     .. describe:: HasFlag(Flag)

        Allows for run-time checking the type of the graph (see the TGraphFlag for flag definitions). 

     .. describe:: Defrag()

        Defragments the graph. After performing many node and edge
        insertions and deletions to a graph, the graph data structure
        can be fragmented in memory. This function compacts down the
        graph data structure and frees unneeded memory. 

     .. describe:: Dump(OutF=sys.stdout)

        Prints the graph in a human readable form to the output stream *OutF*. 

     .. describe:: GetSmallGraph()

        Returns a small graph on 5 nodes and 5 edges. 

   Below is some code demonstrating the use of the :class:`TUNGraph` class:

      >>> G1 = snap.TUNGraph.New()
      >>> G1.AddNode(1)
      1
      >>> G1.AddNode(2)
      2
      >>> G1.AddNode(5)
      5
      >>> G1.AddEdge(1,5)
      -1
      >>> G1.AddEdge(1,2)
      -1
      >>> print G1.Empty()
      False
      >>> print G1.GetNodes()
      3
      >>> print G1.GetEdges()
      2

TUNGraphNodeI
=============

.. class:: TUNGraphNodeI()

    Returns a new node iterator for :class:`TUNGraph`. Normally, these
    objects are not created directly,
    but obtained via a call to the graph class :class:`TUNGraph` method,
    such as :meth:`BegNI()`, that returns a node iterator.

    :class:`TUNGraphNodeI` provides the following methods:

      .. describe:: Next()

        Moves the iterator to the next node in the graph.

      .. describe:: GetId()

        Returns node ID of the current node.

      .. describe:: GetDeg()
                    GetInDeg()
                    GetOutDeg()

        Returns degree of the current node. Since the graph is undirected,
        all three  methods return the same value.

      .. describe:: GetInNId(NodeN)

        Returns ID of *NodeN*-th in-node (the node pointing to the current node).

      .. describe:: GetOutNId(NodeN)

        Returns ID of *NodeN*-th out-node (the node the current node points to).

      .. describe:: GetNbrNId(NodeN)

        Returns ID of *NodeN*-th neighboring node. 

      .. describe:: IsInNId(NId)

        Tests whether node with ID *NId* points to the current node.

      .. describe:: IsOutNId(NId)

        Tests whether the current node points to node with ID *NId*. 

      .. describe:: IsNbrNId(NId)

        Tests whether node with ID *NId* is a neighbor of the current node.

TUNGraphEdgeI
=============

.. class:: TUNGraphEdgeI()

    Returns a new edge iterator for :class:`TUNGraph`. Normally, these
    objects are not created directly,
    but obtained via a call to the graph class :class:`TUNGraph` method,
    such as :meth:`BegEI()`, that returns an edge iterator.

    :class:`TUNGraphEdgeI` provides the following methods:

      .. describe:: Next()

        Moves the iterator to the next edge in the graph.

      .. describe:: GetId()

        Returns a tuple of (*SrcNId*, *DstNId*). No explicit edge IDs are
        assigned to edges in :class:`TUNGraph`.

      .. describe:: GetSrcNId()

        Returns the ID of the source node of the edge.
        Since the graph is undirected,
        this is the node with a smaller ID of the edge endpoints.

      .. describe:: GetDstNId()

        Returns the ID of the destination node of the edge.
        Since the graph is undirected,
        this is the node with a greater ID of the edge endpoints.

TNGraph
=======

.. class:: TNGraph()
           TNGraph(Nodes, Edges)
           TNGraph(Graph)

   Returns a new directed graph. If no parameters are provided,
   an empty graph is created. If *Nodes* and *Edges* are specified, space
   is preallocated for *Nodes* nodes and *Edges* edges. If *Graph* is specified,
   the new graph is a copy of the input graph.

   Nodes have IDs, which are arbitrary non-negative integers. Nodes and edges
   have no attributes/data associated with them. There is at most one
   directed edge from one source node to a destination node. There can be
   an edge between the same pair of nodes in the opposite direction. Self
   loops (one per node) are allowed but multiple (parallel) edges are not.
   The directed graph data structure is implemented using sorted adjacency
   lists. This means adding a node takes constant time, while adding an edge
   takes linear time (since adjacency list is kept sorted) in the node
   degree. Accessing an arbitrary node takes constant time and accessing
   any edge takes logarithmic time in the node degree.

   :class:`TNGraph` provides iterators for fast traversal of nodes and edges.
   Iterator classes are :class:`TNGraphNodeI` for iterating over nodes and
   :class:`TNGraphEdgeI` for iterating over edges.

   :class:`TNGraph` provides the following methods:

     .. describe:: New()

        Returns a pointer to a new graph.

     .. describe:: New(Nodes, Edges)

        Returns a pointer to a new graph and reserves enough memory for
        *Nodes* nodes and *Edges* edges.

     .. describe:: Load(SIn)

        Loads a graph from a binary stream *SIn* and returns a pointer to it. 

     .. describe:: Save(SOut)

        Saves the graph to a binary stream *SOut*. 

     .. describe:: Nodes()

        Returns a generator for the nodes in the graph.

     .. describe:: GetNodes()

        Returns the number of nodes in the graph. 

     .. describe:: AddNode(NId)

        Adds a node of ID *NId* to the graph, *NId* is an integer.
        Returns node ID. If NId is -1, node ID is automatically assigned.
        It throws an exception, if a node with ID *NId* already exists. 

     .. describe:: AddNode(NodeI)

        Adds a node of ID *NodeI.GetId()* to the graph. *NodeI* is a node iterator. Returns node ID.

     .. describe:: DelNode(NId)

        Deletes node of ID *NId* from the graph. *NId* is an integer.
        If the node of ID *NId* does not exist, the function throws an exception. 

     .. describe:: DelNode(NodeI)

        Deletes node of ID *NodeI.GetId()* from the graph. *NodeI* is a node iterator.

     .. describe:: IsNode(NId)

        Returns true, if ID *NId* is a node in the graph.

     .. describe:: BegNI()

        Returns a node iterator referring to the first node in the graph. 

     .. describe:: EndNI()

        Returns a node iterator referring to the past-the-end node in the graph.

     .. describe:: GetNI(NId)

        Returns a node iterator referring to the node of ID *NId* in the graph. 

     .. describe:: GetMxNId()

        Returns the maximum ID of a any node in the graph.

     .. describe:: GetRndNId()

        Returns an ID of a random node in the graph. 

     .. describe:: GetRndNI()

        Returns a node interator referring to a random node in the graph. 

     .. describe:: Edges()

        Returns a generator for the edges in the graph.

     .. describe:: GetEdges()

        Returns the number of edges in the graph. 

     .. describe:: AddEdge(SrcNId, DstNId)

        Adds an edge from node *SrcNId* to node *DstNId* to the graph.
        Returns -1, if the edge was successfully added. Returns -2, if the
        edge already exists. The function throws an exception, if *SrcNId*
        or *DstNId* are not nodes in the graph.

     .. describe:: AddEdge(EdgeI)

        Adds an edge from *EdgeI.GetSrcNId()* to *EdgeI.GetDstNId()* to the graph. *EdgeI* is an edge iterator. Returns -1, if successful. Returns -2, otherwise.

     .. describe:: DelEdge(SrcNId, DstNId)

        Deletes an edge from node IDs *SrcNId* to *DstNId* from the graph. 
        If the edge from *SrcNId* to *DstNId* does not exist in the graph,
        function still completes. But the function throws an exception,
        if *SrcNId* or *DstNId* are not nodes in the graph. 

     .. describe:: IsEdge(SrcNId, DstNId)

        Tests whether an edge from node *SrcNId* to *DstNId* exists in the graph. 

     .. describe:: BegEI()

        Returns an edge iterator referring to the first edge in the graph. 

     .. describe:: EndEI()

        Returns an edge iterator referring to the past-the-end edge in the graph.

     .. describe:: GetEI(SrcNId, DstNId)

        Returns an edge iterator referring to edge between node IDs *SrcNId*
        and *DstNId* in the graph.

     .. describe:: Empty()

        Returns true if the graph is empty, has zero nodes. 

     .. describe:: Clr()

        Deletes all nodes and edges from the graph. 

     .. describe:: Reserve(Nodes, Edges)

        Reserves memory for a graph of *Nodes* nodes and *Edges* edges. 

     .. describe:: ReserveNIdInDeg(NId, Deg)

        Reserves memory for node ID *NId* having *InDeg* in-edges. 

     .. describe:: ReserveNIdOutDeg(NId, Deg)

        Reserves memory for node ID *NId* having *OutDeg* out-edges. 

     .. describe:: HasFlag(Flag)

        Allows for run-time checking the type of the graph (see the TGraphFlag for flag definitions). 

     .. describe:: Defrag()

        Defragments the graph. After performing many node and edge
        insertions and deletions to a graph, the graph data structure
        can be fragmented in memory. This function compacts down the
        graph data structure and frees unneeded memory.

     .. describe:: Dump(OutF=sys.stdout)

        Prints the graph in a human readable form to the output stream *OutF*. 

     .. describe:: GetSmallGraph()

        Returns a small graph on 5 nodes and 6 edges. 

   Below is some code demonstrating the use of the :class:`TNGraph` class:

      >>> G2 = snap.TNGraph.New()
      >>> G2.AddNode(1)
      1
      >>> G2.AddNode(2)
      2
      >>> G2.AddNode(5)
      5
      >>> G2.AddEdge(1,5)
      -1
      >>> G2.AddEdge(1,2)
      -1
      >>> print G2.Empty()
      False
      >>> print G2.GetNodes()
      3
      >>> print G2.GetEdges()
      2

TNGraphNodeI
============

.. class:: TNGraphNodeI()

    Returns a new node iterator for :class:`TNGraph`. Normally, these
    objects are not created directly,
    but obtained via a call to the graph class :class:`TNGraph` method,
    such as :meth:`BegNI()`, that returns a node iterator.

    :class:`TNGraphNodeI` provides the following methods:

      .. describe:: Next()

        Moves the iterator to the next node in the graph.

      .. describe:: GetId()

        Returns node ID of the current node.

      .. describe:: GetDeg()

        Returns degree of the current node, the sum of in-degree and out-degree.

      .. describe:: GetInDeg()

        Returns in-degree of the current node.

      .. describe:: GetOutDeg()

        Returns out-degree of the current node.

      .. describe:: GetInNId(NodeN)

        Returns ID of *NodeN*-th in-node (the node pointing to the current node).

      .. describe:: GetOutNId(NodeN)

        Returns ID of *NodeN*-th out-node (the node the current node points to).

      .. describe:: GetNbrNId(NodeN)

        Returns ID of *NodeN*-th neighboring node. 

      .. describe:: IsInNId(NId)

        Tests whether node with ID *NId* points to the current node.

      .. describe:: IsOutNId(NId)

        Tests whether the current node points to node with ID *NId*. 

      .. describe:: IsNbrNId(NId)

        Tests whether node with ID *NId* is a neighbor of the current node.

TNGraphEdgeI
============

.. class:: TNGraphEdgeI()

    Returns a new edge iterator for :class:`TNGraph`. Normally, these
    objects are not created directly,
    but obtained via a call to the graph class :class:`TNGraph` method,
    such as :meth:`BegEI()`, that returns an edge iterator.

    :class:`TNGraphEdgeI` provides the following methods:

      .. describe:: Next()

        Moves the iterator to the next edge in the graph.

      .. describe:: GetId()

        Returns a tuple of (*SrcNId*, *DstNId*). No explicit edge IDs are
        assigned to edges in :class:`TNGraph`.

      .. describe:: GetSrcNId()

        Returns the ID of the source node of the edge.

      .. describe:: GetDstNId()

        Returns the ID of the destination node of the edge.

TNEANet
=======

.. class:: TNEANet()
           TNEANet(Nodes, Edges)
           TNEANet(Graph)

   Returns a new directed multigraph with node and edge attributes.
   If no parameters are provided,
   an empty graph is created. If *Nodes* and *Edges* are specified, space
   is preallocated for *Nodes* nodes and *Edges* edges. If *Graph* is specified,
   the new graph is a copy of the input graph.

   Nodes have IDs, which are arbitrary non-negative integers. Edges have IDs.
   There can be more than one directed edge from one source node to
   a destination node. Self loops (one per node) are allowed as well as
   multiple (parallel) edges. Nodes and edges can have attributes/data
   associated with them. The attributes can be added dynamically at runtime.
   The directed multigraph data structure is implemented using sorted
   adjacency lists. This means adding a node takes constant time, while
   adding an edge takes linear time (since adjacency list is kept sorted)
   in the node degree. Accessing arbitrary node takes constant time and
   accessing any edge takes logarithmic time in the node degree.
   The attributes are organized in a columnar store, where each attribute
   column is defined for all the nodes or edges in the network. 

   Methods for :class:`TNEANet` are presented in two groups. The first
   group of methods deal with graph structure which includes nodes and edges.
   The second group of methods deal with node and edge attributes.

   :class:`TNEANet` provides iterators for fast traversal of nodes, edges
   and attributes.
   Iterator classes are :class:`TNEANetNodeI` for iterating over nodes,
   :class:`TNEANetEdgeI` for iterating over edges, and
   :class:`TNEANetAIntI`, :class:`TNEANetAFltI`, :class:`TNEANetAStrI`
   for iterating over integer, float or string attributes, respectively.
   Attribute iterators can operate over attributes for nodes or edges.

   :class:`TNEANet` methods for graph structure are the following:

     .. describe:: New()

        Returns a pointer to a new graph.

     .. describe:: New(Nodes, Edges)

        Returns a pointer to a new graph and reserves enough memory for
        *Nodes* nodes and *Edges* edges.

     .. describe:: Load(SIn)

        Loads a graph from a binary stream *SIn* and returns a pointer to it. 

     .. describe:: Save(SOut)

        Saves the graph to a binary stream *SOut*. 

     .. describe:: Nodes()

        Returns a generator for the nodes in the graph.

     .. describe:: GetNodes()

        Returns the number of nodes in the graph. 

     .. describe:: AddNode(NId)

        Adds a node of ID *NId* to the graph, *NId* is an integer.
        Returns node ID. If NId is -1, node ID is automatically assigned.
        It throws an exception, if a node with ID *NId* already exists. 

     .. describe:: AddNode(NodeI)

        Adds a node of ID *NodeI.GetId()* to the graph. *NodeI* is a node iterator. Returns node ID.

     .. describe:: DelNode(NId)

        Deletes node of ID *NId* from the graph. *NId* is an integer.
        If the node of ID *NId* does not exist, the function throws an exception. 

     .. describe:: DelNode(NodeI)

        Deletes node of ID *NodeI.GetId()* from the graph. *NodeI* is a node iterator.

     .. describe:: IsNode(NId)

        Returns true, if ID *NId* is a node in the graph.

     .. describe:: BegNI()

        Returns a node iterator referring to the first node in the graph. 

     .. describe:: EndNI()

        Returns a node iterator referring to the past-the-end node in the graph.

     .. describe:: GetNI(NId)

        Returns a node iterator referring to the node of ID *NId* in the graph. 

     .. describe:: GetMxNId()

        Returns the maximum ID of a any node in the graph.

     .. describe:: GetRndNId()

        Returns an ID of a random node in the graph. 

     .. describe:: GetNIdV(NIdV)

        Returns IDs of all the nodes in vector *NIdV*, which must be of type *TIntV*.

     .. describe:: Edges()

        Returns a generator for the edges in the graph.

     .. describe:: GetEdges()

        Returns the number of edges in the graph. 

     .. describe:: AddEdge(SrcNId, DstNId, EId=-1)

        Adds an edge with ID *EId* between node IDs *SrcNId* and *DstNId*
        to the graph. Returns the ID of the edge being added. If *EId* is -1,
        edge ID is automatically assigned. Throws an exception, if an edge
        with ID *EId* already exists or if either *SrcNId* or *DstNId* does
        not exist.

     .. describe:: AddEdge(EdgeI)

        Adds an edge from *EdgeI.GetSrcNId()* to *EdgeI.GetDstNId()* to
        the graph. *EdgeI* is an edge iterator. Returns the ID of the
        edge being added. If *EId* is -1, edge ID is automatically assigned.
        Throws an exception, if an edge with ID *EId* already exists or
        if either *SrcNId* or *DstNId* does not exist.

     .. describe:: DelEdge(SrcNId, DstNId)

        Deletes an edge from node IDs *SrcNId* to *DstNId* from the graph. 
        If the edge from *SrcNId* to *DstNId* does not exist in the graph,
        function still completes. But the function throws an exception,
        if *SrcNId* or *DstNId* are not nodes in the graph. 

     .. describe:: IsEdge(SrcNId, DstNId)

        Tests whether an edge from node *SrcNId* to *DstNId* exists in the graph. 

     .. describe:: BegEI()

        Returns an edge iterator referring to the first edge in the graph. 

     .. describe:: EndEI()

        Returns an edge iterator referring to the past-the-end edge in the graph.

     .. describe:: GetEI(EId)

        Returns an edge iterator referring to edge with ID *EId*.

     .. describe:: GetEI(SrcNId, DstNId)

        Returns an edge iterator referring to edge between node IDs *SrcNId*
        and *DstNId* in the graph.

     .. describe:: GetRndEId()

        Returns an ID of a random edge in the graph. 

     .. describe:: GetEIdV(EIdV)

        Returns IDs of all the edges in vector *EIdV*, which must be of type *TIntV*.

     .. describe:: Empty()

        Returns true if the graph is empty, has zero nodes. 

     .. describe:: Clr()

        Deletes all nodes and edges from the graph. 

     .. describe:: Reserve(Nodes, Edges)

        Reserves memory for a graph of *Nodes* nodes and *Edges* edges. 

     .. describe:: ReserveNIdInDeg(NId, Deg)

        Reserves memory for node ID *NId* having *InDeg* in-edges. 

     .. describe:: ReserveNIdOutDeg(NId, Deg)

        Reserves memory for node ID *NId* having *OutDeg* out-edges. 

     .. describe:: HasFlag(Flag)

        Allows for run-time checking the type of the graph (see the TGraphFlag for flag definitions). 

     .. describe:: Defrag()

        Defragments the graph. After performing many node and edge
        insertions and deletions to a graph, the graph data structure
        can be fragmented in memory. This function compacts down the
        graph data structure and frees unneeded memory.

     .. describe:: Dump(OutF=sys.stdout)

        Prints the graph in a human readable form to the output stream *OutF*. 

     .. describe:: GetSmallGraph()

        Returns a small multigraph on 5 nodes and 6 edges. 

   :class:`TNEANet` methods for node and edge attributes support
   attributes of different types.
   Integer, float and string attributes are implemented.
   Each attribute type has its own method for a particular task.
   Attributes are named via string names. The sections below describe
   methods for dealing with node attributes first, followed by methods for
   edge attributes.

   :class:`TNEANet` methods for node attributes are the following:

     .. describe:: AddIntAttrN(Attr)
                   AddFltAttrN(Attr)
                   AddStrAttrN(Attr)

        Defines a new integer, float or string node attribute, respectively.

     .. describe:: DelAttrN(Attr)

        Deletes node attribute *Attr*.

     .. describe:: GetAttrIndN(Attr)

        Returns the index of the value vector for node attribute *Attr*.

     .. describe:: AddIntAttrDatN(NodeI, Value, Attr)
                   AddFltAttrDatN(NodeI, Value, Attr)
                   AddStrAttrDatN(NodeI, Value, Attr)

        Sets the value of attribute named *Attr* for the node referred to
        by node iterator *NodeI* to *Value*.
        *Value* is an integer, a float, or a string, respectively.

     .. describe:: AddIntAttrDatN(NId, Value, Attr)
                   AddFltAttrDatN(NId, Value, Attr)
                   AddStrAttrDatN(NId, Value, Attr)

        Sets the value of attribute named *Attr* for the node with
        node id *NId* to *Value*.
        *Value* is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrDatN(NodeI, Attr)
                   GetFltAttrDatN(NodeI, Attr)
                   GetStrAttrDatN(NodeI, Attr)

        Returns the value of attribute named *Attr* for the node referred to
        by node iterator *NodeI*.
        Result is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrDatN(NId, Attr)
                   GetFltAttrDatN(NId, Attr)
                   GetStrAttrDatN(NId, Attr)

        Returns the value of attribute named *Attr* for the node with
        node id *NId*.
        Result is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrIndDatN(NodeI, Index)
                   GetFltAttrIndDatN(NodeI, Index)
                   GetStrAttrIndDatN(NodeI, Index)

        Returns the value of attribute at *Index* for the node referred to
        by node iterator *NodeI*.
        Result is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrIndDatN(NId, Index)
                   GetFltAttrIndDatN(NId, Index)
                   GetStrAttrIndDatN(NId, Index)

        Returns the value of attribute at *Index* for the node with
        node id *NId*.
        Result is an integer, a float, or a string, respectively.

     .. describe:: BegNAIntI(Attr)
                   BegNAFltI(Attr)
                   BegNAStrI(Attr)

        Returns an integer, float, or string attribute iterator, respectively,
        of the attribute named *Attr* referring to the first node.

     .. describe:: EndNAIntI(Attr)
                   EndNAFltI(Attr)
                   EndNAStrI(Attr)

        Returns an integer, float, or string attribute iterator, respectively,
        of the attribute named *Attr* referring to the past-the-end node.

     .. describe:: GetNAIntI(Attr, NId)
                   GetNAFltI(Attr, NId)
                   GetNAStrI(Attr, NId)

        Returns an integer, float, or string attribute iterator, respectively,
        of the attribute named *Attr* referring to the node
        with node ID *NId*.

     .. describe:: DelAttrDatN(NodeI, Attr)

        Deletes the value of attribute named *Attr* for the node referred to
        by node iterator *NodeI*.

     .. describe:: DelAttrDatN(NId, Attr)

        Deletes the value of attribute named *Attr* for the node with
        node ID *NId*.

     .. describe:: IsAttrDeletedN(NId, Attr)

        Returns true, if attribute *Attr* exists for node *NId* and 
        has been deleted -- its value is set to default.

     .. describe:: IsIntAttrDeletedN(NId, Attr)
                   IsFltAttrDeletedN(NId, Attr)
                   IsStrAttrDeletedN(NId, Attr)

        Returns true, if integer, float, or string attribute *Attr* exists
        for node *NId* and has been deleted -- its value is set to default.

     .. describe:: AttrNameNI(NId, NameV)

        Provides names of attributes for the node *NId*. Only attributes
        with an assigned value are provided. Attribute names are returned
        as strings in *NameV*, which must be of type *TStrV*.

     .. describe:: IntAttrNameNI(NId, NameV)
                   FltAttrNameNI(NId, NameV)
                   StrAttrNameNI(NId, NameV)

        Provides names of integer, float, or string attributes for the
        node *NId*, respectively. Only attributes with an assigned value
        are provided. Attribute names are returned as strings in *NameV*,
        which must be of type *TStrV*.

     .. describe:: AttrValueNI(NId, ValueV)

        Provides values of attributes for the node *NId*. Only attributes
        with an assigned value are provided. Attribute values are converted
        to strings and returned in *ValueV*, which must be of type *TStrV*.

     .. describe:: IntAttrValueNI(NId, ValueV)
                   FltAttrValueNI(NId, ValueV)
                   StrAttrValueNI(NId, ValueV)

        Provides values of integer, float, or string attributes for the
        node *NId*, respectively. Only attributes with an assigned value
        are provided. Attribute values are returned as integers, floats, or
        strings in *ValueV*, which must be of type *TIntV*, *TFltV*, or
        *TStrV*, respectively.

     .. describe:: GetAttrNNames(IntAttrNames, FltAttrNames, StrAttrNames)

        Fills *IntAttrNames* with the list of int node attribute names,
        *FltAttrNames* with a list of float node attribute names, and 
        *StrAttrNames* with a list of string node attribute names.
        *IntAttrNames*, *FltAttrNames*, and *StrAttrNames* should all
        be of type *TStrV*.

   :class:`TNEANet` methods for edge attributes are the following:

     .. describe:: AddIntAttrE(Attr)
                   AddFltAttrE(Attr)
                   AddStrAttrE(Attr)

        Defines a new integer, float or string edge attribute, respectively.

     .. describe:: DelAttrE(Attr)

        Deletes edge attribute *Attr*.

     .. describe:: GetAttrIndE(Attr)

        Returns the index of the value vector for edge attribute *Attr*.

     .. describe:: AddIntAttrDatE(EdgeI, Value, Attr)
                   AddFltAttrDatE(EdgeI, Value, Attr)
                   AddStrAttrDatE(EdgeI, Value, Attr)

        Sets the value of attribute named *Attr* for the edge referred to
        by edge iterator *EdgeI* to *Value*.
        *Value* is an integer, a float, or a string, respectively.

     .. describe:: AddIntAttrDatE(EId, Value, Attr)
                   AddFltAttrDatE(EId, Value, Attr)
                   AddStrAttrDatE(EId, Value, Attr)

        Sets the value of attribute named *Attr* for the edge with
        edge id *EId* to *Value*.
        *Value* is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrDatE(EdgeI, Attr)
                   GetFltAttrDatE(EdgeI, Attr)
                   GetStrAttrDatE(EdgeI, Attr)

        Returns the value of attribute named *Attr* for the edge referred to
        by edge iterator *EdgeI*.
        Result is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrDatE(EId, Attr)
                   GetFltAttrDatE(EId, Attr)
                   GetStrAttrDatE(EId, Attr)

        Returns the value of attribute named *Attr* for the edge with
        edge id *EId*.
        Result is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrIndDatE(EdgeI, Index)
                   GetFltAttrIndDatE(EdgeI, Index)
                   GetStrAttrIndDatE(EdgeI, Index)

        Returns the value of attribute at *Index* for the edge referred to
        by edge iterator *EdgeI*.
        Result is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrIndDatE(EId, Index)
                   GetFltAttrIndDatE(EId, Index)
                   GetStrAttrIndDatE(EId, Index)

        Returns the value of attribute at *Index* for the edge with
        edge id *EId*.
        Result is an integer, a float, or a string, respectively.

     .. describe:: BegEAIntI(Attr)
                   BegEAFltI(Attr)
                   BegEAStrI(Attr)

        Returns an integer, float, or string attribute iterator, respectively,
        of the attribute named *Attr* referring to the first edge.

     .. describe:: EndEAIntI(Attr)
                   EndEAFltI(Attr)
                   EndEAStrI(Attr)

        Returns an integer, float, or string attribute iterator, respectively,
        of the attribute named *Attr* referring to the past-the-end edge.

     .. describe:: GetEAIntI(Attr, EId)
                   GetEAFltI(Attr, EId)
                   GetEAStrI(Attr, EId)

        Returns an integer, float, or string attribute iterator, respectively,
        of the attribute named *Attr* referring to the edge
        with edge ID *EId*.

     .. describe:: DelAttrDatE(EdgeI, Attr)

        Deletes the value of attribute named *Attr* for the edge referred to
        by edge iterator *EdgeI*.

     .. describe:: DelAttrDatE(EId, Attr)

        Deletes the value of attribute named *Attr* for the edge with
        edge ID *EId*.

     .. describe:: IsAttrDeletedE(EId, Attr)

        Returns true, if attribute *Attr* exists for edge *EId* and 
        has been deleted -- its value is set to default.

     .. describe:: IsIntAttrDeletedE(EId, Attr)
                   IsFltAttrDeletedE(EId, Attr)
                   IsStrAttrDeletedE(EId, Attr)

        Returns true, if integer, float, or string attribute *Attr* exists
        for edge *EId* and has been deleted -- its value is set to default.

     .. describe:: AttrNameEI(EId, NameV)

        Provides names of attributes for the edge *EId*. Only attributes
        with an assigned value are provided. Attribute names are returned
        as strings in *NameV*, which must be of type *TStrV*.

     .. describe:: IntAttrNameEI(EId, NameV)
                   FltAttrNameEI(EId, NameV)
                   StrAttrNameEI(EId, NameV)

        Provides names of integer, float, or string attributes for the
        edge *EId*, respectively. Only attributes with an assigned value
        are provided. Attribute names are returned as strings in *NameV*,
        which must be of type *TStrV*.

     .. describe:: AttrValueEI(EId, ValueV)

        Provides values of attributes for the edge *EId*. Only attributes
        with an assigned value are provided. Attribute values are converted
        to strings and returned in *ValueV*, which must be of type *TStrV*.

     .. describe:: IntAttrValueEI(EId, ValueV)
                   FltAttrValueEI(EId, ValueV)
                   StrAttrValueEI(EId, ValueV)

        Provides values of integer, float, or string attributes for the
        edge *EId*, respectively. Only attributes with an assigned value
        are provided. Attribute values are returned as integers, floats, or
        strings in *ValueV*, which must be of type *TIntV*, *TFltV*, or
        *TStrV*, respectively.

     .. describe:: AttrValueEI(EId, ValueV)

        Provides values of attributes for the edge *EId*. Only attributes
        with an assigned value are provided. Attribute values are converted
        to strings and returned in *ValueV*, which must be of type *TStrV*.

     .. describe:: GetAttrENames(IntAttrNames, FltAttrNames, StrAttrNames)

        Fills *IntAttrNames* with the list of int edge attribute names,
        *FltAttrNames* with a list of float edge attribute names, and 
        *StrAttrNames* with a list of string edge attribute names.
        *IntAttrNames*, *FltAttrNames*, and *StrAttrNames* should all
        be of type *TStrV*.


   Below is some code demonstrating the use of the :class:`TNEANet` class:

      >>> G3 = snap.TNEANet.New()
      >>> G3.AddNode(1)
      1
      >>> G3.AddNode(2)
      2
      >>> G3.AddNode(5)
      5
      >>> G3.AddEdge(1,5)
      0
      >>> G3.AddEdge(1,2)
      1
      >>> G3.AddEdge(1,2)
      2
      >>> print G3.Empty()
      False
      >>> print G3.GetNodes()
      3
      >>> print G3.GetEdges()
      3

TNEANetNodeI
============

.. class:: TNEANetNodeI()

    Returns a new node iterator for :class:`TNEANet`. Normally, these
    objects are not created directly,
    but obtained via a call to the network class :class:`TNEANet` method,
    such as :meth:`BegNI()`, that returns a node iterator.

    :class:`TNEANetNodeI` provides the following methods:

      .. describe:: Next()

        Moves the iterator to the next node in the graph.

      .. describe:: GetId()

        Returns node ID of the current node.

      .. describe:: GetDeg()

        Returns degree of the current node, the sum of in-degree and out-degree.

      .. describe:: GetInDeg()

        Returns in-degree of the current node.

      .. describe:: GetOutDeg()

        Returns out-degree of the current node.

      .. describe:: GetInNId(NodeN)

        Returns ID of *NodeN*-th in-node (the node pointing to the current node).

      .. describe:: GetOutNId(NodeN)

        Returns ID of *NodeN*-th out-node (the node the current node points to).

      .. describe:: GetNbrNId(NodeN)

        Returns ID of *NodeN*-th neighboring node. 

      .. describe:: IsInNId(NId)

        Tests whether node with ID *NId* points to the current node.

      .. describe:: IsOutNId(NId)

        Tests whether the current node points to node with ID *NId*. 

      .. describe:: IsNbrNId(NId)

        Tests whether node with ID *NId* is a neighbor of the current node.

TNEANetEdgeI
============

.. class:: TNEANetEdgeI()

    Returns a new edge iterator for :class:`TNEANet`. Normally, these
    objects are not created directly,
    but obtained via a call to the graph class :class:`TNEANet` method,
    such as :meth:`BegEI()`, that returns an edge iterator.

    :class:`TNEANetEdgeI` provides the following methods:

      .. describe:: Next()

        Moves the iterator to the next edge in the graph.

      .. describe:: GetId()

        Returns edge ID. 

      .. describe:: GetSrcNId()

        Returns the ID of the source node of the edge.

      .. describe:: GetDstNId()

        Returns the ID of the destination node of the edge.

TNEANetAIntI, TNEANetAFltI, TNEANetAStrI
========================================

.. class:: TNEANetAIntI()
           TNEANetAFltI()
           TNEANetAStrI()

    Returns a new integer, float or string attribute iterator
    for :class:`TNEANet`. Normally, these objects are not created directly,
    but obtained via a call to the graph class :class:`TNEANet` method,
    such as :meth:`BegNAIntI()`, which returns an integer node iterator, or
    :meth:`BegEAFltI()`, which returns a float edge iterator.

    Attribute iterators provide the following methods:

      .. describe:: Next()

        Moves the iterator to the next node or edge in the graph.

      .. describe:: GetDat()

        Returns an attribute of the node or edge.

      .. describe:: IsDeleted()

        Returns true if the attribute has been deleted.

