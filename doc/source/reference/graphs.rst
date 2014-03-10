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

     .. describe:: GetRndNId()

        Returns an ID of a random node in the graph. 

     .. describe:: GetRndNI()

        Returns a node interator referring to a random node in the graph. 

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

     .. describe:: GetRndNId()

        Returns an ID of a random node in the graph. 

     .. describe:: GetRndNI()

        Returns a node interator referring to a random node in the graph. 

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

     .. describe:: GetEI(SrcNId, DstNId)

        Returns an edge iterator referring to edge between node IDs *SrcNId*
        and *DstNId* in the graph.

     .. describe:: GetRndNId()

        Returns an ID of a random node in the graph. 

     .. describe:: GetRndNI()

        Returns a node interator referring to a random node in the graph. 

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
   Attributes are named via string names.

   :class:`TNEANet` methods for attributes are the following:

     .. describe:: AddIntAttrN(Attr)
                   AddFltAttrN(Attr)
                   AddStrAttrN(Attr)

        Defines a new integer, float or string node attribute, respectively.

     .. describe:: AddIntAttrE(Attr)
                   AddFltAttrE(Attr)
                   AddStrAttrE(Attr)

        Defines a new integer, float or string edge attribute, respectively.

     .. describe:: DelAttrN(Attr)

        Deletes node attribute *Attr*.

     .. describe:: DelAttrE(Attr)

        Deletes edge attribute *Attr*.

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

     .. describe:: GetIntAttrDatN(NodeI, Attr)
                   GetFltAttrDatN(NodeI, Attr)
                   GetStrAttrDatN(NodeI, Attr)

        Returns the value of attribute named *Attr* for the node referred to
        by node iterator *NodeI**.
        Result is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrDatN(NId, Attr)
                   GetFltAttrDatN(NId, Attr)
                   GetStrAttrDatN(NId, Attr)

        Returns the value of attribute named *Attr* for the node with
        node id *NId*.
        Result is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrDatE(EdgeI, Attr)
                   GetFltAttrDatE(EdgeI, Attr)
                   GetStrAttrDatE(EdgeI, Attr)

        Returns the value of attribute named *Attr* for the edge referred to
        by edge iterator *EdgeI**.
        Result is an integer, a float, or a string, respectively.

     .. describe:: GetIntAttrDatE(EId, Attr)
                   GetFltAttrDatE(EId, Attr)
                   GetStrAttrDatE(EId, Attr)

        Returns the value of attribute named *Attr* for the edge with
        edge id *EId*.
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

     .. describe:: DelAttrDatN(NodeI, Attr)

        Deletes the value of attribute named *Attr* for the node referred to
        by node iterator *NodeI*.

     .. describe:: DelAttrDatN(NId, Attr)

        Deletes the value of attribute named *Attr* for the node with
        node ID *NId*.

     .. describe:: DelAttrDatE(EdgeI, Attr)

        Deletes the value of attribute named *Attr* for the edge referred to
        by edge iterator *EdgeI*.

     .. describe:: DelAttrDatE(EId, Attr)

        Deletes the value of attribute named *Attr* for the edge with
        edge ID *EId*.

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

