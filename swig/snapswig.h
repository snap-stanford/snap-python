class TNGraphNodeI {
private:
  TNGraph::TNodeI NI;
public:
  TNGraphNodeI() : NI() { }
  TNGraphNodeI(const TNGraph::TNodeI& NodeI) : NI(NodeI) { }
  TNGraphNodeI& operator = (const TNGraph::TNodeI& NodeI) { NI = NodeI; return *this; }
  /// Increment iterator.
  TNGraphNodeI& operator++ (int) { NI++; return *this; }
  TNGraphNodeI& Next() { NI++; return *this; }
  bool operator < (const TNGraphNodeI& NodeI) const { return NI < NodeI.NI; }
  bool operator == (const TNGraphNodeI& NodeI) const { return NI == NodeI.NI; }
  /// Returns C++ node iterator.
  TNGraph::TNodeI GetNI() const { return NI; }
  /// Returns ID of the current node.
  int GetId() const { return NI.GetId(); }
  /// Returns degree of the current node, the sum of in-degree and out-degree.
  int GetDeg() const { return NI.GetDeg(); }
  /// Returns in-degree of the current node.
  int GetInDeg() const { return NI.GetInDeg(); }
  /// Returns out-degree of the current node.
  int GetOutDeg() const { return NI.GetOutDeg(); }
  /// Returns ID of NodeN-th in-node (the node pointing to the current node). ##TNGraph::TNodeI::GetInNId
  int GetInNId(const int& NodeN) const { return NI.GetInNId(NodeN); }
  /// Returns ID of NodeN-th out-node (the node the current node points to). ##TNGraph::TNodeI::GetOutNId
  int GetOutNId(const int& NodeN) const { return NI.GetOutNId(NodeN); }
  /// Returns ID of NodeN-th neighboring node. ##TNGraph::TNodeI::GetNbrNId
  int GetNbrNId(const int& NodeN) const { return NI.GetNbrNId(NodeN); }
  /// Tests whether node with ID NId points to the current node.
  bool IsInNId(const int& NId) const { return NI.IsInNId(NId); }
  /// Tests whether the current node points to node with ID NId.
  bool IsOutNId(const int& NId) const { return NI.IsOutNId(NId); }
  /// Tests whether node with ID NId is a neighbor of the current node.
  bool IsNbrNId(const int& NId) const { return NI.IsOutNId(NId) || NI.IsInNId(NId); }
};

class TDirNetNodeI {
private:
  TDirNet::TNodeI NI;
public:
  TDirNetNodeI() : NI() { }
  TDirNetNodeI(const TDirNet::TNodeI& NodeI) : NI(NodeI) { }
  TDirNetNodeI& operator = (const TDirNet::TNodeI& NodeI) { NI = NodeI; return *this; }
  /// Increment iterator.
  TDirNetNodeI& operator++ (int) { NI++; return *this; }
  TDirNetNodeI& Next() { NI++; return *this; }
  bool operator < (const TDirNetNodeI& NodeI) const { return NI < NodeI.NI; }
  bool operator == (const TDirNetNodeI& NodeI) const { return NI == NodeI.NI; }
  /// Returns ID of the current node.
  int GetId() const { return NI.GetId(); }
  /// Returns degree of the current node, the sum of in-degree and out-degree.
  int GetDeg() const { return NI.GetDeg(); }
  /// Returns in-degree of the current node.
  int GetInDeg() const { return NI.GetInDeg(); }
  /// Returns out-degree of the current node.
  int GetOutDeg() const { return NI.GetOutDeg(); }
  /// Returns ID of NodeN-th in-node (the node pointing to the current node). ##TDirNet::TNodeI::GetInNId
  int GetInNId(const int& NodeN) const { return NI.GetInNId(NodeN); }
  /// Returns ID of NodeN-th out-node (the node the current node points to). ##TDirNet::TNodeI::GetOutNId
  int GetOutNId(const int& NodeN) const { return NI.GetOutNId(NodeN); }
  /// Returns ID of NodeN-th neighboring node. ##TDirNet::TNodeI::GetNbrNId
  int GetNbrNId(const int& NodeN) const { return NI.GetNbrNId(NodeN); }
  /// Tests whether node with ID NId points to the current node.
  bool IsInNId(const int& NId) const { return NI.IsInNId(NId); }
  /// Tests whether the current node points to node with ID NId.
  bool IsOutNId(const int& NId) const { return NI.IsOutNId(NId); }
  /// Tests whether node with ID NId is a neighbor of the current node.
  bool IsNbrNId(const int& NId) const { return NI.IsOutNId(NId) || NI.IsInNId(NId); }
};

#ifdef GCC_ATOMIC
class TNGraphMPNodeI { 
private:
  TNGraphMP::TNodeI NI;
public:
  TNGraphMPNodeI() : NI() { }
  TNGraphMPNodeI(const TNGraphMP::TNodeI& NodeI) : NI(NodeI) { }
  TNGraphMPNodeI& operator = (const TNGraphMP::TNodeI& NodeI) { NI = NodeI; return *this; }
  /// Increment iterator.
  TNGraphMPNodeI& operator++ (int) { NI++; return *this; }
  TNGraphMPNodeI& Next() { NI++; return *this; }
  bool operator < (const TNGraphMPNodeI& NodeI) const { return NI < NodeI.NI; }
  bool operator == (const TNGraphMPNodeI& NodeI) const { return NI == NodeI.NI; }
  /// Returns ID of the current node.
  int GetId() const { return NI.GetId(); }
  /// Returns degree of the current node, the sum of in-degree and out-degree.
  int GetDeg() const { return NI.GetDeg(); }
  /// Returns in-degree of the current node.
  int GetInDeg() const { return NI.GetInDeg(); }
  /// Returns out-degree of the current node.
  int GetOutDeg() const { return NI.GetOutDeg(); }
  /// Returns ID of NodeN-th in-node (the node pointing to the current node). ##TNGraphMP::TNodeI::GetInNId
  int GetInNId(const int& NodeN) const { return NI.GetInNId(NodeN); }
  /// Returns ID of NodeN-th out-node (the node the current node points to). ##TNGraphMP::TNodeI::GetOutNId
  int GetOutNId(const int& NodeN) const { return NI.GetOutNId(NodeN); }
  /// Returns ID of NodeN-th neighboring node. ##TNGraphMP::TNodeI::GetNbrNId
  int GetNbrNId(const int& NodeN) const { return NI.GetNbrNId(NodeN); }
  /// Tests whether node with ID NId points to the current node.
  bool IsInNId(const int& NId) const { return NI.IsInNId(NId); }
  /// Tests whether the current node points to node with ID NId.
  bool IsOutNId(const int& NId) const { return NI.IsOutNId(NId); }
  /// Tests whether node with ID NId is a neighbor of the current node.
  bool IsNbrNId(const int& NId) const { return NI.IsOutNId(NId) || NI.IsInNId(NId); }
};
#endif // GCC_ATOMIC

/// Edge iterator. Only forward iteration (operator++) is supported.
class TNGraphEdgeI {
private:
  TNGraph::TEdgeI EI;
public:
  TNGraphEdgeI() : EI() { }
  TNGraphEdgeI(const TNGraph::TEdgeI& EdgeI) : EI(EdgeI) { }
  TNGraphEdgeI& operator = (const TNGraph::TEdgeI& EdgeI) { EI = EdgeI; return *this; }
  /// Increment iterator.
  TNGraphEdgeI& operator++ (int) { EI++; return *this; }
  TNGraphEdgeI& Next() { EI++; return *this; }
  bool operator < (const TNGraphEdgeI& EdgeI) const { return EI < EdgeI.EI; }
  bool operator == (const TNGraphEdgeI& EdgeI) const { return EI == EdgeI.EI; }
  /// Returns C++ edge iterator.
  TNGraph::TEdgeI GetEI() const { return EI; }
  /// Gets edge ID. Always returns -1, since edges do not have explicit IDs.
  int GetId() const { return EI.GetId(); }
  /// Returns the ID of the source node of the edge.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Returns the ID of the destination node of the edge.
  int GetDstNId() const { return EI.GetDstNId(); }
};

/// Edge iterator. Only forward iteration (operator++) is supported.
class TDirNetEdgeI {
private:
  TDirNet::TEdgeI EI;
public:
  TDirNetEdgeI() : EI() { }
  TDirNetEdgeI(const TDirNet::TEdgeI& EdgeI) : EI(EdgeI) { }
  TDirNetEdgeI& operator = (const TDirNet::TEdgeI& EdgeI) { EI = EdgeI; return *this; }
  /// Increment iterator.
  TDirNetEdgeI& operator++ (int) { EI++; return *this; }
  TDirNetEdgeI& Next() { EI++; return *this; }
  bool operator < (const TDirNetEdgeI& EdgeI) const { return EI < EdgeI.EI; }
  bool operator == (const TDirNetEdgeI& EdgeI) const { return EI == EdgeI.EI; }
  /// Gets edge ID. Always returns -1, since edges do not have explicit IDs.
  int GetId() const { return EI.GetId(); }
  /// Gets the source of an edge.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Gets destination of an edge.
  int GetDstNId() const { return EI.GetDstNId(); }
};

#ifdef GCC_ATOMIC
/// Edge iterator. Only forward iteration (operator++) is supported.
class TNGraphMPEdgeI {
private:
  TNGraphMP::TEdgeI EI;
public:
  TNGraphMPEdgeI() : EI() { }
  TNGraphMPEdgeI(const TNGraphMP::TEdgeI& EdgeI) : EI(EdgeI) { }
  TNGraphMPEdgeI& operator = (const TNGraphMP::TEdgeI& EdgeI) { EI = EdgeI; return *this; }
  /// Increment iterator.
  TNGraphMPEdgeI& operator++ (int) { EI++; return *this; }
  TNGraphMPEdgeI& Next() { EI++; return *this; }
  bool operator < (const TNGraphMPEdgeI& EdgeI) const { return EI < EdgeI.EI; }
  bool operator == (const TNGraphMPEdgeI& EdgeI) const { return EI == EdgeI.EI; }
  /// Gets edge ID. Always returns -1, since edges do not have explicit IDs.
  int GetId() const { return EI.GetId(); }
  /// Gets the source of an edge.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Gets destination of an edge.
  int GetDstNId() const { return EI.GetDstNId(); }
};
#endif // GCC_ATOMIC

class TUNGraphNodeI {
private:
  TUNGraph::TNodeI NI;
public:
  TUNGraphNodeI() : NI() { }
  TUNGraphNodeI(const TUNGraph::TNodeI& NodeI) : NI(NodeI) { }
  TUNGraphNodeI& operator = (const TUNGraph::TNodeI& NodeI) { NI = NodeI; return *this; }
  /// Increment iterator.
  TUNGraphNodeI& operator++ (int) { NI++; return *this; }
  TUNGraphNodeI& Next() { NI++; return *this; }
  bool operator < (const TUNGraphNodeI& NodeI) const { return NI < NodeI.NI; }
  bool operator == (const TUNGraphNodeI& NodeI) const { return NI == NodeI.NI; }
  /// Returns C++ node iterator.
  TUNGraph::TNodeI GetNI() const { return NI; }
  /// Returns ID of the current node.
  int GetId() const { return NI.GetId(); }
  /// Returns degree of the current node, the sum of in-degree and out-degree.
  int GetDeg() const { return NI.GetDeg(); }
  /// Returns in-degree of the current node.
  int GetInDeg() const { return NI.GetInDeg(); }
  /// Returns out-degree of the current node.
  int GetOutDeg() const { return NI.GetOutDeg(); }
  /// Returns ID of NodeN-th in-node (the node pointing to the current node). ##TUNGraph::TNodeI::GetInNId
  int GetInNId(const int& NodeN) const { return NI.GetInNId(NodeN); }
  /// Returns ID of NodeN-th out-node (the node the current node points to). ##TUNGraph::TNodeI::GetOutNId
  int GetOutNId(const int& NodeN) const { return NI.GetOutNId(NodeN); }
  /// Returns ID of NodeN-th neighboring node. ##TUNGraph::TNodeI::GetNbrNId
  int GetNbrNId(const int& NodeN) const { return NI.GetNbrNId(NodeN); }
  /// Tests whether node with ID NId points to the current node.
  bool IsInNId(const int& NId) const { return NI.IsInNId(NId); }
  /// Tests whether the current node points to node with ID NId.
  bool IsOutNId(const int& NId) const { return NI.IsOutNId(NId); }
  /// Tests whether node with ID NId is a neighbor of the current node.
  bool IsNbrNId(const int& NId) const { return NI.IsOutNId(NId) || NI.IsInNId(NId); }
};

class TUndirNetNodeI {
private:
  TUndirNet::TNodeI NI;
public:
  TUndirNetNodeI() : NI() { }
  TUndirNetNodeI(const TUndirNet::TNodeI& NodeI) : NI(NodeI) { }
  TUndirNetNodeI& operator = (const TUndirNet::TNodeI& NodeI) { NI = NodeI; return *this; }
  /// Increment iterator.
  TUndirNetNodeI& operator++ (int) { NI++; return *this; }
  TUndirNetNodeI& Next() { NI++; return *this; }
  bool operator < (const TUndirNetNodeI& NodeI) const { return NI < NodeI.NI; }
  bool operator == (const TUndirNetNodeI& NodeI) const { return NI == NodeI.NI; }
  /// Returns ID of the current node.
  int GetId() const { return NI.GetId(); }
  /// Returns degree of the current node, the sum of in-degree and out-degree.
  int GetDeg() const { return NI.GetDeg(); }
  /// Returns in-degree of the current node.
  int GetInDeg() const { return NI.GetInDeg(); }
  /// Returns out-degree of the current node.
  int GetOutDeg() const { return NI.GetOutDeg(); }
  /// Returns ID of NodeN-th in-node (the node pointing to the current node). ##TUndirNet::TNodeI::GetInNId
  int GetInNId(const int& NodeN) const { return NI.GetInNId(NodeN); }
  /// Returns ID of NodeN-th out-node (the node the current node points to). ##TUndirNet::TNodeI::GetOutNId
  int GetOutNId(const int& NodeN) const { return NI.GetOutNId(NodeN); }
  /// Returns ID of NodeN-th neighboring node. ##TUndirNet::TNodeI::GetNbrNId
  int GetNbrNId(const int& NodeN) const { return NI.GetNbrNId(NodeN); }
  /// Tests whether node with ID NId points to the current node.
  bool IsInNId(const int& NId) const { return NI.IsInNId(NId); }
  /// Tests whether the current node points to node with ID NId.
  bool IsOutNId(const int& NId) const { return NI.IsOutNId(NId); }
  /// Tests whether node with ID NId is a neighbor of the current node.
  bool IsNbrNId(const int& NId) const { return NI.IsOutNId(NId) || NI.IsInNId(NId); }
};

/// Edge iterator. Only forward iteration (operator++) is supported.
class TUNGraphEdgeI {
private:
  TUNGraph::TEdgeI EI;
public:
  TUNGraphEdgeI() : EI() { }
  TUNGraphEdgeI(const TUNGraph::TEdgeI& EdgeI) : EI(EdgeI) { }
  TUNGraphEdgeI& operator = (const TUNGraph::TEdgeI& EdgeI) { EI = EdgeI; return *this; }
  /// Increment iterator.
  TUNGraphEdgeI& operator++ (int) { EI++; return *this; }
  TUNGraphEdgeI& Next() { EI++; return *this; }
  bool operator < (const TUNGraphEdgeI& EdgeI) const { return EI < EdgeI.EI; }
  bool operator == (const TUNGraphEdgeI& EdgeI) const { return EI == EdgeI.EI; }
  /// Returns C++ edge iterator.
  TUNGraph::TEdgeI GetEI() const { return EI; }
  /// Gets edge ID. Always returns -1, since edges do not have explicit IDs.
  int GetId() const { return EI.GetId(); }
  /// Gets the source of an edge. Since the graph is undirected this is the node with smaller ID of the edge endpoints.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Gets destination of an edge. Since the graph is undirected this is the node with greater ID of the edge endpoints.
  int GetDstNId() const { return EI.GetDstNId(); }
};

class TUndirNetEdgeI {
private:
  TUndirNet::TEdgeI EI;
public:
  TUndirNetEdgeI() : EI() { }
  TUndirNetEdgeI(const TUndirNet::TEdgeI& EdgeI) : EI(EdgeI) { }
  TUndirNetEdgeI& operator = (const TUndirNet::TEdgeI& EdgeI) { EI = EdgeI; return *this; }
  /// Increment iterator.
  TUndirNetEdgeI& operator++ (int) { EI++; return *this; }
  TUndirNetEdgeI& Next() { EI++; return *this; }
  bool operator < (const TUndirNetEdgeI& EdgeI) const { return EI < EdgeI.EI; }
  bool operator == (const TUndirNetEdgeI& EdgeI) const { return EI == EdgeI.EI; }
  /// Gets edge ID. Always returns -1 since only edges in multigraphs have explicit IDs.
  int GetId() const { return EI.GetId(); }
  /// Gets the source of an edge. Since the graph is undirected this is the node with smaller ID of the edge endpoints.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Gets destination of an edge. Since the graph is undirected this is the node with greater ID of the edge endpoints.
  int GetDstNId() const { return EI.GetDstNId(); }
};  

class TNEANetNodeI {
private:
  TNEANet::TNodeI NI;
public:
  TNEANetNodeI() : NI() { }
  TNEANetNodeI(const TNEANet::TNodeI& NodeI) : NI(NodeI) { }
  TNEANetNodeI& operator = (const TNEANet::TNodeI& NodeI) { NI = NodeI; return *this; }
  /// Increment iterator.
  TNEANetNodeI& operator++ (int) { NI++; return *this; }
  TNEANetNodeI& Next() { NI++; return *this; }
  bool operator < (const TNEANetNodeI& NodeI) const { return NI < NodeI.NI; }
  bool operator == (const TNEANetNodeI& NodeI) const { return NI == NodeI.NI; }
  /// Returns C++ node iterator.
  TNEANet::TNodeI GetNI() const { return NI; }
  /// Returns ID of the current node.
  int GetId() const { return NI.GetId(); }
  /// Returns degree of the current node, the sum of in-degree and out-degree.
  int GetDeg() const { return NI.GetDeg(); }
  /// Returns in-degree of the current node.
  int GetInDeg() const { return NI.GetInDeg(); }
  /// Returns out-degree of the current node.
  int GetOutDeg() const { return NI.GetOutDeg(); }
  /// Returns ID of NodeN-th in-node (the node pointing to the current node). ##TNEANet::TNodeI::GetInNId
  int GetInNId(const int& NodeN) const { return NI.GetInNId(NodeN); }
  /// Returns ID of NodeN-th out-node (the node the current node points to). ##TNEANet::TNodeI::GetOutNId
  int GetOutNId(const int& NodeN) const { return NI.GetOutNId(NodeN); }
  /// Returns ID of NodeN-th neighboring node. ##TNEANet::TNodeI::GetNbrNId
  int GetNbrNId(const int& NodeN) const { return NI.GetNbrNId(NodeN); }
  /// Tests whether node with ID NId points to the current node.
  bool IsInNId(const int& NId) const { return NI.IsInNId(NId); }
  /// Tests whether the current node points to node with ID NId.
  bool IsOutNId(const int& NId) const { return NI.IsOutNId(NId); }
  /// Tests whether node with ID NId is a neighbor of the current node.
  bool IsNbrNId(const int& NId) const { return NI.IsOutNId(NId) || NI.IsInNId(NId); }
};

/// Edge iterator. Only forward iteration (operator++) is supported.
class TNEANetEdgeI {
private:
  TNEANet::TEdgeI EI;
public:
  TNEANetEdgeI() : EI() { }
  TNEANetEdgeI(const TNEANet::TEdgeI& EdgeI) : EI(EdgeI) { }
  TNEANetEdgeI& operator = (const TNEANet::TEdgeI& EdgeI)
                            { EI = EdgeI; return *this; }
  /// Increment iterator.
  TNEANetEdgeI& operator++ (int) { EI++; return *this; }
  TNEANetEdgeI& Next() { EI++; return *this; }
  bool operator < (const TNEANetEdgeI& EdgeI) const { return EI < EdgeI.EI; }
  bool operator == (const TNEANetEdgeI& EdgeI) const { return EI == EdgeI.EI; }
  /// Returns C++ edge iterator.
  TNEANet::TEdgeI GetEI() const { return EI; }
  /// Returns edge ID. Only multigraphs have explicit edge IDs.
  int GetId() const { return EI.GetId(); }
  /// Returns the ID of the source node of the edge.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Returns the ID of the destination node of the edge.
  int GetDstNId() const { return EI.GetDstNId(); }
};

typedef TIntV::TIter TIntVecIter;

/// Node/edge integer attribute iterator. Iterates through all nodes/edges for one integer attribute.
class TNEANetAIntI {
private:
  TNEANet::TAIntI IntAI;
public:
  TNEANetAIntI() : IntAI() { }
  TNEANetAIntI(const TIntVecIter& HIter, TStr attribute, bool isEdgeIter,
               const TNEANet* GraphPt) :
              IntAI(HIter, attribute, isEdgeIter, GraphPt) { }
  TNEANetAIntI(const TNEANet::TAIntI& I) : IntAI(I) { }
  TNEANetAIntI& operator = (const TNEANetAIntI& I)
              { IntAI = I.IntAI; return *this; }
  TNEANetAIntI& Next() { IntAI++; return *this; }
  bool operator < (const TNEANetAIntI& I) const { return IntAI < I.IntAI; }
  bool operator == (const TNEANetAIntI& I) const { return IntAI == I.IntAI; }
  /// Returns an attribute of the node.
  int GetDat() const { return IntAI.GetDat().Val; }
  /// Returns true if node or edge has been deleted.
  bool IsDeleted() const { return IntAI.IsDeleted(); };
  TNEANetAIntI& operator++(int) { IntAI++; return *this; }
//  friend class TNEANet;
};

typedef TStrV::TIter TStrVecIter;

/// Node/edge string attribute iterator. Iterates through all nodes/edges for one string attribute.
class TNEANetAStrI {
private:
  TNEANet::TAStrI StrAI;
public:
  TNEANetAStrI() : StrAI() { }
  TNEANetAStrI(const TStrVecIter& HIter, TStr attribute, bool isEdgeIter,
               const TNEANet* GraphPt) :
  StrAI(HIter, attribute, isEdgeIter, GraphPt) { }
  TNEANetAStrI(const TNEANet::TAStrI& I) : StrAI(I) { }
  TNEANetAStrI& operator = (const TNEANetAStrI& I)
  { StrAI = I.StrAI; return *this; }
  TNEANetAStrI& Next() { StrAI++; return *this; }
  bool operator < (const TNEANetAStrI& I) const { return StrAI < I.StrAI; }
  bool operator == (const TNEANetAStrI& I) const { return StrAI == I.StrAI; }
  /// Returns an attribute of the node.
  char * GetDat() const { return StrAI.GetDat().CStr(); }
  /// Returns true if node or edge has been deleted.
  bool IsDeleted() const { return StrAI.IsDeleted(); };
  TNEANetAStrI& operator++(int) { StrAI++; return *this; }
  //  friend class TNEANet;
};


typedef TFltV::TIter TFltVecIter;

/// Node/edge float attribute iterator. Iterates through all nodes/edges for one float attribute.
class TNEANetAFltI {
private:
  TNEANet::TAFltI FltAI;
public:
  TNEANetAFltI() : FltAI() { }
  TNEANetAFltI(const TFltVecIter& HIter, TStr attribute, bool isEdgeIter,
               const TNEANet* GraphPt) :
  FltAI(HIter, attribute, isEdgeIter, GraphPt) { }
  TNEANetAFltI(const TNEANet::TAFltI& I) : FltAI(I) { }
  TNEANetAFltI& operator = (const TNEANetAFltI& I)
  { FltAI = I.FltAI; return *this; }
  TNEANetAFltI& Next() { FltAI++; return *this; }
  bool operator < (const TNEANetAFltI& I) const { return FltAI < I.FltAI; }
  bool operator == (const TNEANetAFltI& I) const { return FltAI == I.FltAI; }
  /// Returns an attribute of the node.
  double GetDat() const { return FltAI.GetDat().Val; }
  /// Returns true if node or edge has been deleted.
  bool IsDeleted() const { return FltAI.IsDeleted(); };
  TNEANetAFltI& operator++(int) { FltAI++; return *this; }
  //  friend class TNEANet;
};


#ifdef GCC_ATOMIC
class TNEANetMPNodeI {
private:
  TNEANetMP::TNodeI NI;
public:
  TNEANetMPNodeI() : NI() { }
  TNEANetMPNodeI(const TNEANetMP::TNodeI& NodeI) : NI(NodeI) { }
  TNEANetMPNodeI& operator = (const TNEANetMP::TNodeI& NodeI) { NI = NodeI; return *this; }
  /// Increment iterator.
  TNEANetMPNodeI& operator++ (int) { NI++; return *this; }
  TNEANetMPNodeI& Next() { NI++; return *this; }
  bool operator < (const TNEANetMPNodeI& NodeI) const { return NI < NodeI.NI; }
  bool operator == (const TNEANetMPNodeI& NodeI) const { return NI == NodeI.NI; }
  /// Returns ID of the current node.
  int GetId() const { return NI.GetId(); }
  /// Returns degree of the current node, the sum of in-degree and out-degree.
  int GetDeg() const { return NI.GetDeg(); }
  /// Returns in-degree of the current node.
  int GetInDeg() const { return NI.GetInDeg(); }
  /// Returns out-degree of the current node.
  int GetOutDeg() const { return NI.GetOutDeg(); }
  /// Returns ID of NodeN-th in-node (the node pointing to the current node). ##TNEANetMP::TNodeI::GetInNId
  int GetInNId(const int& NodeN) const { return NI.GetInNId(NodeN); }
  /// Returns ID of NodeN-th out-node (the node the current node points to). ##TNEANetMP::TNodeI::GetOutNId
  int GetOutNId(const int& NodeN) const { return NI.GetOutNId(NodeN); }
  /// Returns ID of NodeN-th neighboring node. ##TNEANetMP::TNodeI::GetNbrNId
  int GetNbrNId(const int& NodeN) const { return NI.GetNbrNId(NodeN); }
  /// Tests whether node with ID NId points to the current node.
  bool IsInNId(const int& NId) const { return NI.IsInNId(NId); }
  /// Tests whether the current node points to node with ID NId.
  bool IsOutNId(const int& NId) const { return NI.IsOutNId(NId); }
  /// Tests whether node with ID NId is a neighbor of the current node.
  bool IsNbrNId(const int& NId) const { return NI.IsOutNId(NId) || NI.IsInNId(NId); }
};

/// Edge iterator. Only forward iteration (operator++) is supported.
class TNEANetMPEdgeI {
private:
  TNEANetMP::TEdgeI EI;
public:
  TNEANetMPEdgeI() : EI() { }
  TNEANetMPEdgeI(const TNEANetMP::TEdgeI& EdgeI) : EI(EdgeI) { }
  TNEANetMPEdgeI& operator = (const TNEANetMP::TEdgeI& EdgeI)
                            { EI = EdgeI; return *this; }
  /// Increment iterator.
  TNEANetMPEdgeI& operator++ (int) { EI++; return *this; }
  TNEANetMPEdgeI& Next() { EI++; return *this; }
  bool operator < (const TNEANetMPEdgeI& EdgeI) const { return EI < EdgeI.EI; }
  bool operator == (const TNEANetMPEdgeI& EdgeI) const { return EI == EdgeI.EI; }
  /// Gets edge ID. Always returns -1 since only edges in multigraphs have explicit IDs.
  int GetId() const { return EI.GetId(); }
  /// Gets the source of an edge. Since the graph is undirected this is the node with smaller ID of the edge endpoints.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Gets destination of an edge. Since the graph is undirected this is the node with greater ID of the edge endpoints.
  int GetDstNId() const { return EI.GetDstNId(); }
};
#endif // GCC_ATOMIC


class TModeNetNodeI {
private:
  TModeNet::TNodeI NI;
public:
  TModeNetNodeI() : NI() { }
  TModeNetNodeI(const TModeNet::TNodeI& NodeI) : NI(NodeI) { }
  TModeNetNodeI& operator = (const TModeNet::TNodeI& NodeI) { NI = NodeI; return *this; }
  /// Increment iterator.
  TModeNetNodeI& operator++ (int) { NI++; return *this; }
  TModeNetNodeI& Next() { NI++; return *this; }
  bool operator < (const TModeNetNodeI& NodeI) const { return NI < NodeI.NI; }
  bool operator == (const TModeNetNodeI& NodeI) const { return NI == NodeI.NI; }
  /// Returns ID of the current node.
  int GetId() const { return NI.GetId(); }
  /// Returns degree of the current node, the sum of in-degree and out-degree.
  int GetDeg() const { return NI.GetDeg(); }
  /// Returns in-degree of the current node.
  int GetInDeg() const { return NI.GetInDeg(); }
  /// Returns out-degree of the current node.
  int GetOutDeg() const { return NI.GetOutDeg(); }
  /// Returns ID of NodeN-th in-node (the node pointing to the current node). ##TNEANet::TNodeI::GetInNId
  int GetInNId(const int& NodeN) const { return NI.GetInNId(NodeN); }
  /// Returns ID of NodeN-th out-node (the node the current node points to). ##TNEANet::TNodeI::GetOutNId
  int GetOutNId(const int& NodeN) const { return NI.GetOutNId(NodeN); }
  /// Returns ID of NodeN-th neighboring node. ##TNEANet::TNodeI::GetNbrNId
  int GetNbrNId(const int& NodeN) const { return NI.GetNbrNId(NodeN); }
  /// Tests whether node with ID NId points to the current node.
  bool IsInNId(const int& NId) const { return NI.IsInNId(NId); }
  /// Tests whether the current node points to node with ID NId.
  bool IsOutNId(const int& NId) const { return NI.IsOutNId(NId); }
  /// Tests whether node with ID NId is a neighbor of the current node.
  bool IsNbrNId(const int& NId) const { return NI.IsOutNId(NId) || NI.IsInNId(NId); }
};

/// Edge iterator. Only forward iteration (operator++) is supported.
class TModeNetEdgeI {
private:
  TNEANet::TEdgeI EI;
public:
  TModeNetEdgeI() : EI() { }
  TModeNetEdgeI(const TNEANet::TEdgeI& EdgeI) : EI(EdgeI) { }
  TModeNetEdgeI& operator = (const TNEANet::TEdgeI& EdgeI)
                            { EI = EdgeI; return *this; }
  /// Increment iterator.
  TModeNetEdgeI& operator++ (int) { EI++; return *this; }
  TModeNetEdgeI& Next() { EI++; return *this; }
  bool operator < (const TModeNetEdgeI& EdgeI) const { return EI < EdgeI.EI; }
  bool operator == (const TModeNetEdgeI& EdgeI) const { return EI == EdgeI.EI; }
  /// Gets edge ID. Always returns -1 since only edges in multigraphs have explicit IDs.
  int GetId() const { return EI.GetId(); }
  /// Gets the source of an edge. Since the graph is undirected this is the node with smaller ID of the edge endpoints.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Gets destination of an edge. Since the graph is undirected this is the node with greater ID of the edge endpoints.
  int GetDstNId() const { return EI.GetDstNId(); }
};

/// Edge iterator. Only forward iteration (operator++) is supported.
class TCrossNetEdgeI {
private:
  TCrossNet::TCrossEdgeI EI;
public:
  TCrossNetEdgeI() : EI() { }
  TCrossNetEdgeI(const TCrossNet::TCrossEdgeI& EdgeI) : EI(EdgeI) { }
  TCrossNetEdgeI& operator = (const TCrossNet::TCrossEdgeI& EdgeI)
                            { EI = EdgeI; return *this; }
  /// Increment iterator.
  TCrossNetEdgeI& operator++ (int) { EI++; return *this; }
  TCrossNetEdgeI& Next() { EI++; return *this; }
  bool operator < (const TCrossNetEdgeI& EdgeI) const { return EI < EdgeI.EI; }
  bool operator == (const TCrossNetEdgeI& EdgeI) const { return EI == EdgeI.EI; }
  /// Gets edge ID. Always returns -1 since only edges in multigraphs have explicit IDs.
  int GetId() const { return EI.GetId(); }
  /// Gets the source of an edge. Since the graph is undirected this is the node with smaller ID of the edge endpoints.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Gets destination of an edge. Since the graph is undirected this is the node with greater ID of the edge endpoints.
  int GetDstNId() const { return EI.GetDstNId(); }
};

/// Node/Edge Attr iterator. Iterate through all node for one attr value.
class TCrossNetAIntI {
private:
  TCrossNet::TAIntI IntAI;
public:
  TCrossNetAIntI() : IntAI() { }
  TCrossNetAIntI(const TIntVecIter& HIter, TStr attribute,
               const TCrossNet* GraphPt) :
              IntAI(HIter, attribute, GraphPt) { }
  TCrossNetAIntI(const TCrossNet::TAIntI& I) : IntAI(I) { }
  TCrossNetAIntI& operator = (const TCrossNetAIntI& I)
              { IntAI = I.IntAI; return *this; }
  TCrossNetAIntI& Next() { IntAI++; return *this; }
  bool operator < (const TCrossNetAIntI& I) const { return IntAI < I.IntAI; }
  bool operator == (const TCrossNetAIntI& I) const { return IntAI == I.IntAI; }
  /// Returns an attribute of the node.
  int GetDat() const { return IntAI.GetDat().Val; }
  /// Returns true if node or edge has been deleted.
  bool IsDeleted() const { return IntAI.IsDeleted(); };
  TCrossNetAIntI& operator++(int) { IntAI++; return *this; }
//  friend class TCrossNet;
};

/// Node/Edge Attr iterator. Iterate through all node for one attr value.
class TCrossNetAStrI {
private:
  TCrossNet::TAStrI StrAI;
public:
  TCrossNetAStrI() : StrAI() { }
  TCrossNetAStrI(const TStrVecIter& HIter, TStr attribute,
               const TCrossNet* GraphPt) :
  StrAI(HIter, attribute, GraphPt) { }
  TCrossNetAStrI(const TCrossNet::TAStrI& I) : StrAI(I) { }
  TCrossNetAStrI& operator = (const TCrossNetAStrI& I)
  { StrAI = I.StrAI; return *this; }
  TCrossNetAStrI& Next() { StrAI++; return *this; }
  bool operator < (const TCrossNetAStrI& I) const { return StrAI < I.StrAI; }
  bool operator == (const TCrossNetAStrI& I) const { return StrAI == I.StrAI; }
  /// Returns an attribute of the node.
  char * GetDat() const { return StrAI.GetDat().CStr(); }
  /// Returns true if node or edge has been deleted.
  bool IsDeleted() const { return StrAI.IsDeleted(); };
  TCrossNetAStrI& operator++(int) { StrAI++; return *this; }
  //  friend class TCrossNet;
};


/// Node/Edge Attr iterator. Iterate through all node for one attr value.
class TCrossNetAFltI {
private:
  TCrossNet::TAFltI FltAI;
public:
  TCrossNetAFltI() : FltAI() { }
  TCrossNetAFltI(const TFltVecIter& HIter, TStr attribute,
               const TCrossNet* GraphPt) :
  FltAI(HIter, attribute, GraphPt) { }
  TCrossNetAFltI(const TCrossNet::TAFltI& I) : FltAI(I) { }
  TCrossNetAFltI& operator = (const TCrossNetAFltI& I)
  { FltAI = I.FltAI; return *this; }
  TCrossNetAFltI& Next() { FltAI++; return *this; }
  bool operator < (const TCrossNetAFltI& I) const { return FltAI < I.FltAI; }
  bool operator == (const TCrossNetAFltI& I) const { return FltAI == I.FltAI; }
  /// Returns an attribute of the node.
  double GetDat() const { return FltAI.GetDat().Val; }
  /// Returns true if node or edge has been deleted.
  bool IsDeleted() const { return FltAI.IsDeleted(); };
  TCrossNetAFltI& operator++(int) { FltAI++; return *this; }
  //  friend class TCrossNet;
};




class TMMNetModeNetI {
private:
  TMMNet::TModeNetI NI;
public:
  TMMNetModeNetI() : NI() { }
  TMMNetModeNetI(const TMMNet::TModeNetI& NodeI) : NI(NodeI) { }
  TMMNetModeNetI& operator = (const TMMNet::TModeNetI& NodeI) { NI = NodeI; return *this; }
  /// Increment iterator.
  TMMNetModeNetI& operator++ (int) { NI++; return *this; }
  TMMNetModeNetI& Next() { NI++; return *this; }

  bool operator < (const TMMNetModeNetI& NodeI) const { return NI < NodeI.NI; }
  bool operator == (const TMMNetModeNetI& NodeI) const { return NI == NodeI.NI; }
  /// Returns ID of the current node.
  int GetModeId() { return NI.GetModeId(); }
  TModeNet& GetModeNet() { return NI.GetModeNet(); }
};



/// Edge iterator. Only forward iteration (operator++) is supported.
class TMMNetCrossNetI {
private:
  TMMNet::TCrossNetI EI;
public:
  TMMNetCrossNetI() : EI() { }
  TMMNetCrossNetI(const TMMNet::TCrossNetI& EdgeI) : EI(EdgeI) { }
  TMMNetCrossNetI& operator = (const TMMNet::TCrossNetI& EdgeI)
                            { EI = EdgeI; return *this; }
  /// Increment iterator.
  TMMNetCrossNetI& operator++ (int) { EI++; return *this; }
  TMMNetCrossNetI& Next() { EI++; return *this; }
  bool operator < (const TMMNetCrossNetI& EdgeI) const { return EI < EdgeI.EI; }
  bool operator == (const TMMNetCrossNetI& EdgeI) const { return EI == EdgeI.EI; }
  /// Gets edge ID. Always returns -1 since only edges in multigraphs have explicit IDs.
  int GetCrossId() { return EI.GetCrossId(); }
  TCrossNet& GetCrossNet() { return EI.GetCrossNet(); }

};
