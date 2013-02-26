#include "Snap.h"

// Graph type for random generation
typedef enum {
  
  SmallWorld, /* Generates an Erdos-Renyi random graph. */
  BiPart,     /* Bipartitite graph type. */
  PowerLaw,   /* Power law graph. */
  PrefAttach, /* Scale-free graph using preferential model. */
  RMat,       /* R-mat */
               
} GraphType;
               
typedef enum {
  Info,     /* graph info */
  PlotDD,   /* degree distribution */
  PlotCDD,  /* cumulative degree */
  PlotHop,  /* hop plot (diameter) */
  PlotWcc,  /* distribution of weakly connected components */
  PlotScc,  /* distribution of strongly connected components */
  PlotClustCoef,  /* clustering coefficient */
  PlotSVal, /* singular values */
  PlotSVec  /* left and right singular vector */
} PlotType;

const char* const PlotAbb[] = {
  "info", /* basic graph info (e.g. iteration, triads) */
  "DD",   /* degree distribution */
  "CDD",  /* cumulative degree */
  "HOP",  /* hop plot (diameter) */
  "Wcc",  /* distribution of weakly connected components */
  "Scc",  /* distribution of strongly connected components */
  "ClustCoef",  /* clustering coefficient */
  "SVal", /* singular values */
  "SVec",  /* left and right singular vector */
};

const char* const PlotDesc[] = {
  "basic graph info (e.g. iteration, triads)",
  "cumulative degree",
  "hop plot (diameter)",
  "distribution of weakly connected components",
  "distribution of strongly connected components",
  "clustering coefficient",
  "singular values",
  "left and right singular vector"  ,
};

namespace TSnap {
  
  typedef TVec<TInt, int> TIntV;
  typedef TVec<TIntV, int> TIntIntVV;
  
  template<class PGraph>
  void RunCalculations(const PGraph& Graph, PlotType PType) {
    
    TStr OutFNm = PlotAbb[PType], Desc = PlotDesc[PType];
    const int SingularVals = Graph->GetNodes()/2 > 200 ? 200 :
    Graph->GetNodes()/2;
    switch (PType) {
      case Info:
        PrintInfo(Graph, Desc, OutFNm, 0); // Not fast option
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
        PlotClustCf(Graph, OutFNm, Desc);
        break;
      case PlotSVal:
        PlotSngValRank(ConvertGraph<PNGraph>(Graph, true), SingularVals,
                       OutFNm, Desc);
        break;
        
      case PlotSVec:
        PlotSngVec(ConvertGraph<PNGraph>(Graph, true), OutFNm, Desc);
        break;
    }
  }
  
  template<class PGraph>
  double GetStats(int NNodes, int NEdges, PlotType PType, GraphType RType) {
    
    TExeTm ExeTm;
    printf("Timing '%s': Time: %s\n", PlotDesc[PType], TExeTm::GetCurTm());
    
    int StartTime = clock();
    PGraph G;
    
    switch (RType) {
      case SmallWorld:
        printf("Generating random graph for %d nodes, %d edges\n",
               NNodes, NEdges);
        G = GenRndGnm<PGraph>(NNodes, NEdges);
        break;
        
      case PrefAttach:
        printf("Generating preferential attachment graph for %d nodes, %d edges\n",
               NNodes, 5);
        G = GenPrefAttach(NNodes, 5);
        break;
        
      case RMat:
        printf("Generating R-MAT for %d nodes, %d edges\n",
               NNodes, NEdges);
        G = GenRMat(NNodes, NEdges, 0.40, 0.25, 0.2);
        break;
        
      default:
        break;
    }
    
    RunCalculations(G, PType);
    double Elapsed = double(clock() - StartTime) / double(CLOCKS_PER_SEC);
    printf("\nrun time: %s (%s)\n", ExeTm.GetTmStr(), TSecTm::GetCurTm().GetTmStr().CStr());
    printf("Elapsed = %.3f\n", Elapsed);
    return Elapsed;
  }
  
  const char * GetDesc(PlotType PType) {
    return PlotDesc[PType];
  }
  
  const char * GetAbbrev(PlotType PType) {
    return PlotAbb[PType];
  }
  
};
