#include "Snap.h"

using namespace TSnap;
  
typedef TVec<TInt, int> TIntV;
typedef TVec<TIntV, int> TIntIntVV;

template<class PGraph>
double PercentDegree(const PGraph& Graph, const int Threshold=0) {

    int Cnt = 0;
  for (typename PGraph::TObj::TNodeI NI = Graph->BegNI(); NI < Graph->EndNI(); NI++)
  {
    if (NI.GetDeg() >= Threshold) Cnt++;
  }

  return (double)Cnt / (double) Graph->GetNodes();
}

template<class PGraph>
int NodesGTEDegree(const PGraph& Graph, const int Threshold=0) {
  
  int Cnt = 0;
  for (typename PGraph::TObj::TNodeI NI = Graph->BegNI(); NI < Graph->EndNI();
       NI++)
  {
    if (NI.GetDeg() >= Threshold) Cnt++;
  }
  
  return Cnt;
}

template<class PGraph>
int MxDegree(const PGraph& Graph) {
  
  int MaxDeg = 0;
  for (typename PGraph::TObj::TNodeI NI = Graph->BegNI(); NI < Graph->EndNI(); NI++) {
    if (NI.GetDeg() > MaxDeg) {
      MaxDeg = NI.GetDeg();
    }
  }
  
  return MaxDeg;
}

//template<class PGraph>
//bool WriteGraph(const PGraph& Graph, const TStr &OutFNm) {
//  
//  TFOut FOut(OutFNm);
//  FOut.Save(GetNodes());
//}
//
//template<class PGraph>
//PGraph LoadGraph(const TStr& FName) {
//}

template<class PGraph>
double PercentMxWcc(const PGraph& Graph) {
  
  return GetMxWccSz(Graph);
}

template<class PGraph>
double PercentMxScc(const PGraph& Graph) {
  
  PGraph MxSccSz = GetMxScc(Graph);
  
  return (double) MxSccSz->GetNodes() / (double) Graph->GetNodes();
}

