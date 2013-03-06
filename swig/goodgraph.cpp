#include "Snap.h"

//// Graph type for random generation
//typedef enum {
//  SmallWorld, /* Generates an Erdos-Renyi random graph. */
//  BiPart,     /* Bipartitite graph type. */
//  PowerLaw,   /* Power law graph. */
//  PrefAttach, /* Scale-free graph using preferential model. */
//  RMat,       /* R-MAT */
//  GraphMx
//} GraphType;
//
//const char* const GraphAbbr[] = {
//  "sw", /* Generates an Erdos-Renyi random graph. */
//  "bi",   /* Bipartitite graph type. */
//  "pow",   /* Power law graph. */
//  "pref", /* Scale-free graph using preferential model. */
//  "rmat",       /* R-MAT */
//};
//
//const char* const GraphDesc[] = {
//  "Small World", /* Generates an Erdos-Renyi random graph. */
//  "Bipartite",   /* Bipartitite graph type. */
//  "Power Law",   /* Power law graph. */
//  "Preferential Attach", /* Scale-free graph using preferential model. */
//  "R-MAT",       /* R-MAT */
//};
//
//typedef enum {
//  Info,     /* graph info */
//  PlotDD,   /* degree distribution */
//  PlotCDD,  /* cumulative degree */
//  PlotHop,  /* hop plot (diameter) */
//  PlotWcc,  /* distribution of weakly connected components */
//  PlotScc,  /* distribution of strongly connected components */
//  PlotClustCoef,  /* clustering coefficient */
//  PlotSVal, /* singular values */
//  PlotSVec,  /* left and right singular vector */
//  PlotMx
//} PlotType;
//
//const char* const PlotAbbr[] = {
//  "info", /* basic graph info (e.g. iteration, triads) */
//  "DD",   /* degree distribution */
//  "CDD",  /* cumulative degree */
//  "HOP",  /* hop plot (diameter) */
//  "Wcc",  /* distribution of weakly connected components */
//  "Scc",  /* distribution of strongly connected components */
//  "ClustCoef",  /* clustering coefficient */
//  "SVal", /* singular values */
//  "SVec",  /* left and right singular vector */
//};
//
//const char* const PlotDesc[] = {
//  "basic graph info (w. node/edge iteration, triads)",
//  "cumulative degree",
//  "hop plot (diameter)",
//  "distribution of weakly connected components",
//  "distribution of strongly connected components",
//  "clustering coefficient",
//  "singular values",
//  "left and right singular vector"  ,
//};

using namespace TSnap;
  
typedef TVec<TInt, int> TIntV;
typedef TVec<TIntV, int> TIntIntVV;

template<class PGraph>
double PercentDegree(const PGraph& Graph, const int Threshold=0) {

    int Cnt = 0;
  for (typename PGraph::TObj::TNodeI NI = Graph->BegNI(); NI < Graph->EndNI(); NI++) {
    if (NI.GetDeg() >= Threshold) Cnt++;
  }

  return (double)Cnt / (double) Graph->GetNodes();
}

template<class PGraph>
double PercentMxWcc(const PGraph& Graph) {
  
  return GetMxWccSz(Graph);
}

template<class PGraph>
double PercentMxScc(const PGraph& Graph) {
  
  PGraph MxSccSz = GetMxScc(Graph);
  
  return (double) MxSccSz->GetNodes() / (double) Graph->GetNodes();
}