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

     .. describe:: ReserveNIdDeg(NId, Deg)

        Reserves memory for node ID *NId* having *Deg* edges. 

     .. describe:: HasFlag(Flag)

        Allows for run-time checking the type of the graph (see the TGraphFlag for flag definitions). 

     .. describe:: Defrag()

        Defragments the graph. After performing many node and edge
        insertions and deletions to a graph, the graph data structure
        can be fragmented in memory. This function compacts down the
        graph data structure and frees unneeded memory. 

     .. describe:: Dump(Outf=sys.stdout)

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

     .. describe:: Dump(Outf=sys.stdout)

        Prints the graph in a human readable form to the output stream *OutF*. 

     .. describe:: GetSmallGraph()

        Returns a small graph on 5 nodes and 6 edges. 

   Below is some code demonstrating the use of the :class:`TUNGraph` class:

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

