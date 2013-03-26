class TIntHI {
public:
  typedef THashKeyDat<TInt, TInt> THKeyDat;
private:
  THKeyDat* KeyDatI;
  THKeyDat* EndI;
public:
  TIntHI(): KeyDatI(NULL), EndI(NULL){}
  TIntHI(const TIntHI& _HashKeyDatI):
    KeyDatI(_HashKeyDatI.KeyDatI), EndI(_HashKeyDatI.EndI){}
  TIntHI(const THKeyDat* _KeyDatI, const THKeyDat* _EndI):
    KeyDatI((THKeyDat*)_KeyDatI), EndI((THKeyDat*)_EndI){}

  TIntHI& operator=(const TIntHI& HashKeyDatI){
    KeyDatI=HashKeyDatI.KeyDatI; EndI=HashKeyDatI.EndI; return *this;}
  bool operator==(const TIntHI& HashKeyDatI) const {
    return KeyDatI==HashKeyDatI.KeyDatI;}
  bool operator<(const TIntHI& HashKeyDatI) const {
    return KeyDatI<HashKeyDatI.KeyDatI;}
  TIntHI& operator++(int){ KeyDatI++; while (KeyDatI < EndI && KeyDatI->HashCd==-1) { KeyDatI++; } return *this; }
  TIntHI& Next(){ KeyDatI++; while (KeyDatI < EndI && KeyDatI->HashCd==-1) { KeyDatI++; } return *this; }
  TIntHI& operator--(int){ do { KeyDatI--; } while (KeyDatI->HashCd==-1); return *this;}

  THKeyDat& operator*() const { return *KeyDatI; }
  THKeyDat& operator()() const { return *KeyDatI; }
  THKeyDat* operator->() const { return KeyDatI; }

  /// Tests whether the iterator has been initialized.
  bool IsEmpty() const { return KeyDatI == NULL; }
  /// Tests whether the iterator is pointing to the past-end element.
  bool IsEnd() const { return EndI == KeyDatI; }

  const TInt& GetKey() const {Assert((KeyDatI!=NULL)&&(KeyDatI->HashCd!=-1)); return KeyDatI->Key;}
  const TInt& GetDat() const {Assert((KeyDatI!=NULL)&&(KeyDatI->HashCd!=-1)); return KeyDatI->Dat;}
  TInt& GetDat() {Assert((KeyDatI!=NULL)&&(KeyDatI->HashCd!=-1)); return KeyDatI->Dat;}
};

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
  /// Gets edge ID. Always returns -1 since only edges in multigraphs have explicit IDs.
  int GetId() const { return EI.GetId(); }
  /// Gets the source of an edge. Since the graph is undirected this is the node with smaller ID of the edge endpoints.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Gets destination of an edge. Since the graph is undirected this is the node with greater ID of the edge endpoints.
  int GetDstNId() const { return EI.GetDstNId(); }
};

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
  /// Gets edge ID. Always returns -1 since only edges in multigraphs have explicit IDs.
  int GetId() const { return EI.GetId(); }
  /// Gets the source of an edge. Since the graph is undirected this is the node with smaller ID of the edge endpoints.
  int GetSrcNId() const { return EI.GetSrcNId(); }
  /// Gets destination of an edge. Since the graph is undirected this is the node with greater ID of the edge endpoints.
  int GetDstNId() const { return EI.GetDstNId(); }
};

