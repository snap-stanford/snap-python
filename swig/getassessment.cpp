#include "Snap.h"

// Graph type for random generation
typedef enum {
  SmallWorld, /* Generates an Erdos-Renyi random graph. */
  BiPart,     /* Bipartitite graph type. */
  PowerLaw,   /* Power law graph. */
  PrefAttach, /* Scale-free graph using preferential model. */
  RMat,       /* R-MAT */
  GraphMx
} GraphType;

const char* const GraphAbbr[] = {
  "sw", /* Generates an Erdos-Renyi random graph. */
  "bi",   /* Bipartitite graph type. */
  "pow",   /* Power law graph. */
  "pref", /* Scale-free graph using preferential model. */
  "rmat",       /* R-MAT */
};

const char* const GraphDesc[] = {
  "Small World", /* Generates an Erdos-Renyi random graph. */
  "Bipartite",   /* Bipartitite graph type. */
  "Power Law",   /* Power law graph. */
  "Preferential Attach", /* Scale-free graph using preferential model. */
  "R-MAT",       /* R-MAT */
};

typedef enum {
  Iteration,     /* graph info */
  Triads,   /* get triads */
  PlotDD,   /* degree distribution */
  PlotCDD,  /* cumulative degree */
  PlotHop,  /* hop plot (diameter) */
  PlotWcc,  /* distribution of weakly connected components */
  PlotScc,  /* distribution of strongly connected components */
  PlotClustCoef,  /* clustering coefficient */
  PlotSVal, /* singular values */
  PlotSVec,  /* left and right singular vector */
  BFS,      /* BFS Subset. */
  PlotMx
} PlotType;

const char* const PlotAbbr[] = {
  "iterations", /* basic graph info (e.g. iteration, triads) */
  "triads", /* triads */
  "DD",   /* degree distribution */
  "CDD",  /* cumulative degree */
  "HOP",  /* hop plot (diameter) */
  "Wcc",  /* distribution of weakly connected components */
  "Scc",  /* distribution of strongly connected components */
  "ClustCoef",  /* clustering coefficient */
  "SVal", /* singular values */
  "SVec",  /* left and right singular vector */
  "BFS",  /* BFS Subset. */
};

const char* const PlotDesc[] = {
  "node/edge iteration",
  "triads",
  "dgree distribution",
  "cumulative degree",
  "hop plot (diameter)",
  "distribution of weakly connected components",
  "distribution of strongly connected components",
  "clustering coefficient",
  "singular values",
  "left and right singular vector",
  "Breadth First Search (subset)", 
};

#define NUM_NODES_BFS   10

using namespace TSnap;

typedef TVec<TInt, int> TIntV;
typedef TVec<TIntV, int> TIntIntVV;

template <class PGraph>
void RunBasicInfo(const PGraph& Graph, const TStr& Desc, const TStr& OutFNm) {
  int BiDirEdges=0, ZeroNodes=0, ZeroInNodes=0, ZeroOutNodes=0, SelfEdges=0, NonZIODegNodes=0;
  THash<TIntPr, TInt> UniqDirE, UniqUnDirE;
  for (typename PGraph::TObj::TNodeI NI = Graph->BegNI(); NI < Graph->EndNI(); NI++) {
    if (NI.GetDeg()==0) ZeroNodes++;
    if (NI.GetInDeg()==0) ZeroInNodes++;
    if (NI.GetOutDeg()==0) ZeroOutNodes++;
    if (NI.GetInDeg()!=0 && NI.GetOutDeg()!=0) NonZIODegNodes++;
    const int NId = NI.GetId();
    for (int edge = 0; edge < NI.GetOutDeg(); edge++) {
      const int DstNId = NI.GetOutNId(edge);
      if (Graph->IsEdge(DstNId, NId)) BiDirEdges++;
      if (NId == DstNId) SelfEdges++;
      UniqDirE.AddKey(TIntPr(NId, DstNId));
      UniqUnDirE.AddKey(TIntPr(TInt::GetMn(NId, DstNId), TInt::GetMx(NId, DstNId)));
    }
  }
}

template <class PGraph>
void RunTriads(const PGraph& Graph) {
  int64 Closed=0, Open=0;
  GetTriads(Graph, Closed, Open);
}

template <class PGraph>
void RunClustCf(const PGraph& Graph) {
  TFltPrV DegToCCfV;
  int64 ClosedTriads, OpenTriads;
  const double CCF = GetClustCf(Graph, DegToCCfV, ClosedTriads, OpenTriads);
  #pragma unused(CCF)
}

template <class PGraph>
void RunBFS(const PGraph& Graph) {
  
  // Get BFS tree
  for (int i=0; i < NUM_NODES_BFS; i++) {
    int StartNId = Graph->GetRndNId();
    GetBfsTree(Graph, StartNId, true, true);
  }
}

template<class PGraph>
void RunCalculations(const PGraph& Graph, PlotType PType) {
  
  TStr OutFNm = PlotAbbr[PType], Desc = PlotDesc[PType];
  const int SingularVals = Graph->GetNodes()/2 > 200 ? 200 :
                           Graph->GetNodes()/2;
//  printf("Calculating '%s'\n", PlotDesc[PType]);
  switch (PType) {
    case Iteration:
//      PrintInfo(Graph, Desc, OutFNm, 0); // Not fast option
      RunBasicInfo(Graph, Desc, OutFNm);
      break;
      
    case Triads:
      RunTriads(Graph);
      break;

    case PlotDD:
      PlotOutDegDistr(Graph, OutFNm, Desc, false, false);
      PlotInDegDistr(Graph, OutFNm, Desc, false, false);
      break;
      
    case PlotCDD:
      PlotOutDegDistr(Graph, OutFNm, Desc, true, false);
      PlotInDegDistr(Graph, OutFNm, Desc, true, false);
      break;
      
    case PlotHop:
      PlotHops(Graph, OutFNm, Desc, false, 32);
      break;
      
    case PlotWcc:
      PlotWccDistr(Graph, OutFNm, Desc);
      break;
      
    case PlotScc:
      PlotSccDistr(Graph, OutFNm, Desc);
      break;
      
    case PlotClustCoef:
//      PlotClustCf(Graph, OutFNm, Desc);
      RunClustCf(Graph);
      break;
      
    case PlotSVal:
      PlotSngValRank(ConvertGraph<PNGraph>(Graph, true), SingularVals,
                     OutFNm, Desc);
      break;
      
    case PlotSVec:
      PlotSngVec(ConvertGraph<PNGraph>(Graph, true), OutFNm, Desc);
      break;
      
    case BFS:
      //      PlotClustCf(Graph, OutFNm, Desc);
      RunBFS(Graph);
      break;

    default:
      break;
  }
}

double GetStats(int NNodes, int NEdges, PlotType PType, GraphType RType) {
  
  TExeTm ExeTm;
//  printf("Timing '%s'\n", PlotDesc[PType]);
  
  int StartTime = clock();
  
  PNGraph GN;
  PUNGraph GUn;
  
  switch (RType) {
    case SmallWorld:
//      printf("Generating random graph for %d nodes, %d edges\n",
//             NNodes, NEdges);
      GN = GenRndGnm<PNGraph>(NNodes, NEdges);
      RunCalculations(GN, PType);
      break;
      
    case BiPart:
      break;
      
    case PowerLaw:
      break;

    case PrefAttach:
//      printf("Generating preferential attachment graph for %d nodes, %d edges\n", NNodes, 5);
      GUn = GenPrefAttach(NNodes, 5);
      RunCalculations(GUn, PType);
      break;
      
    case RMat:
//      printf("Generating R-MAT for %d nodes, %d edges\n",
//             NNodes, NEdges);
      GN = GenRMat(NNodes, NEdges, 0.40, 0.25, 0.2);
      RunCalculations(GN, PType);
      break;
      
    default:
      break;
  }
  
  double Elapsed = double(clock() - StartTime) / double(CLOCKS_PER_SEC);
//    printf("\nrun time: %s (%s)\n", ExeTm.GetTmStr(), TSecTm::GetCurTm().GetTmStr().CStr());
//    printf("Elapsed = %.3f\n", Elapsed);
  return Elapsed;
}

//template<class PGraph>
//PGraph GenerateGraph(const int NNodes, const int NEdges) {
//  
//}

const char * GetAttributeDesc(PlotType PType) {
  return PlotDesc[PType];
}

const char * GetAttributeAbbr(PlotType PType) {
  return PlotAbbr[PType];
}

const char * GetGraphDesc(GraphType GType) {
  return GraphDesc[GType];
}

const char * GetGraphAbbr(GraphType GType) {
  return GraphAbbr[GType];
}
