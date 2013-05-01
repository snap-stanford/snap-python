// snap.i
%module snap
%{

#include "Snap.h"

#include "printgraph.h"
#include "snapswig.h"
  
#include "goodgraph.cpp"
#include "getassessment.cpp"
#include "swig-TNEAGraph.cpp"

%}

%module test

%feature("autodoc", "3");

%ignore TOnExeStop;
%ignore TPt::TPt;
%ignore TPt::LoadXml;
%ignore TPt::SaveXml;
%ignore TPt::operator==;
%ignore TPt::operator!=;
%ignore TPt::operator<;
%ignore TPt::GetPrimHashCd;
%ignore TPt::GetSecHashCd;
%ignore TPt::Clone;

%ignore TChA::LoadXml;
%ignore TMem::LoadXml;

%ignore GetStr;

%ignore TFInOut;
%ignore TFRnd;
%ignore TFile::Copy;
%ignore TFile::GetLastAccessTm;
%ignore TFile::GetLastWriteTm;
%ignore TFile::GetCreateTm;
%ignore TFile::GetSize;

%ignore TBPGraph::HasFlag(const TGraphFlag& Flag) const;
%ignore TNEGraph::GetSmallGraph();
%ignore TNEAGraph::GetSmallGraph();
%ignore TBPGraph::GetEI(int const&) const;

%ignore TNGraph::GetEI(int const&) const;
%ignore TUNGraph::GetEI(int const&) const;
%ignore TNEAGraph::GetEI(int const&) const;

// SNAP Library
%include "alg.h"
%include "bd.h"
%include "cncom.h"
%include "dt.h"
%include "fl.h"
%include "ggen.h"
%include "gio.h"
%include "graph.h"
%include "subgraph.h"

%include "bfsdfs.h"
%include "triad.h"

//%ignore TGVizLayout;
%include "gviz.h"

//%include "kcore.h"
//%include "gsvd.h"
//%include "centr.h"
//%include "gstat.h"
//%include "cmty.h"
//%include "ff.h"
//%include "anf.h"


//%include "timenet.h"
//%include "statplot.h"
//%include "bignet.h"
//%include "ghash.h"

//%include "ncp.h"

// Used for SNAP-R Tests
%include "printgraph.h"
%include "snapswig.h"

%include "goodgraph.cpp"
%include "getassessment.cpp"
%include "swig-TNEAGraph.cpp"

%extend TNGraph {
        TNGraphNodeI BegNI() {
                return TNGraphNodeI($self->BegNI());
        }
        TNGraphNodeI EndNI() {
                return TNGraphNodeI($self->EndNI());
        }
        TNGraphEdgeI BegEI() {
                return TNGraphEdgeI($self->BegEI());
        }
        TNGraphEdgeI EndEI() {
                return TNGraphEdgeI($self->EndEI());
        }
};

%extend TUNGraph {
        TUNGraphNodeI BegNI() {
                return TUNGraphNodeI($self->BegNI());
        }
        TUNGraphNodeI EndNI() {
                return TUNGraphNodeI($self->EndNI());
        }
        TUNGraphEdgeI BegEI() {
                return TUNGraphEdgeI($self->BegEI());
        }
        TUNGraphEdgeI EndEI() {
                return TUNGraphEdgeI($self->EndEI());
        }
};

%extend TNEAGraph {
        TNEAGraphNodeI BegNI() {
          return TNEAGraphNodeI($self->BegNI());
        }
        TNEAGraphNodeI EndNI() {
          return TNEAGraphNodeI($self->EndNI());
        }
        TNEAGraphEdgeI BegEI() {
          return TNEAGraphEdgeI($self->BegEI());
        }
        TNEAGraphEdgeI EndEI() {
          return TNEAGraphEdgeI($self->EndEI());
        }
};

// Synthetic graphs for benchmarking
%template(GenSyntheticGraph_PNGraph) GenSyntheticGraph<PNGraph>;
%template(GenSyntheticGraph_PNEGraph) GenSyntheticGraph<PNEGraph>;
%template(GenSyntheticGraph_PNEAGraph) GenSyntheticGraph<PNEAGraph>;

// Convert a directed graph to a multi-edge attribute graph
%template(ConvertGraph_PNGraphToPNEAGraph) ConvertGraph<PNEAGraph, PNGraph>;


// Directed Graphs
%template(PNGraph) TPt< TNGraph >;

%template(PercentDegree_PNGraph) PercentDegree<PNGraph>;
%template(PercentMxWcc_PNGraph) PercentMxWcc<PNGraph>;
%template(PercentMxScc_PNGraph) PercentMxScc<PNGraph>;

%template(LoadEdgeList_PNGraph) TSnap::LoadEdgeList<PNGraph>;
%template(PrintGraphStatTable_PNGraph) PrintGraphStatTable<PNGraph>;
%template(GenRndGnm_PNGraph) TSnap::GenRndGnm<PNGraph>;
%template(MxWccSz_PNGraph) TSnap::GetMxWccSz<PNGraph>;
%template(MxSccSz_PNGraph) TSnap::GetMxScc<PNGraph>;

%template(NodesGTEDegree_PNGraph) NodesGTEDegree<PNGraph>;
%template(MxDegree_PNGraph) MxDegree<PNGraph>;

// Undirected Graphs
%template(PUNGraph) TPt< TUNGraph >;

%template(LoadEdgeList_PUNGraph) TSnap::LoadEdgeList<PUNGraph>;
%template(PrintGraphStatTable_PUNGraph) PrintGraphStatTable<PUNGraph>;

%template(NodesGTEDegree_PUNGraph) NodesGTEDegree<PUNGraph>;
%template(GenRndGnm_PUNGraph) TSnap::GenRndGnm<PUNGraph>;
%template(MxSccSz_PUNGraph) TSnap::GetMxScc<PUNGraph>;
%template(MxWccSz_PUNGraph) TSnap::GetMxWccSz<PUNGraph>;
%template(MxDegree_PUNGraph) MxDegree<PUNGraph>;

// TNEAGraphs
%template(PNEAGraph) TPt< TNEAGraph >;

%template(GenRndGnm_PNEAGraph) TSnap::GenRndGnm<PNEAGraph>;

// TNEAGraph functions for cncom.h
%template(MxWccSz_PNEAGraph) TSnap::GetMxWccSz<PNEAGraph>;
%template(MxSccSz_PNEAGraph) TSnap::GetMxScc<PNEAGraph>;

%template(NodesGTEDegree_PNEAGraph) NodesGTEDegree<PNEAGraph>;
%template(MxDegree_PNEAGraph) MxDegree<PNEAGraph>;

// TNEAGraph functions for alg.h and cncom.h
%template(CntInDegNodes_PNEAGraph) TSnap::CntInDegNodes<PNEAGraph>;
%template(CntOutDegNodes_PNEAGraph) TSnap::CntOutDegNodes<PNEAGraph>;
%template(CntDegNodes_PNEAGraph) TSnap::CntDegNodes<PNEAGraph>;
%template(CntNonZNodes_PNEAGraph) TSnap::CntNonZNodes<PNEAGraph>;
%template(CntEdgesToSet_PNEAGraph) TSnap::CntEdgesToSet<PNEAGraph>;

%template(GetMxDegNId_PNEAGraph) TSnap::GetMxDegNId<PNEAGraph>;
%template(GetMxInDegNId_PNEAGraph) TSnap::GetMxInDegNId<PNEAGraph>;
%template(GetMxOutDegNId_PNEAGraph) TSnap::GetMxOutDegNId<PNEAGraph>;

%template(GetInDegCnt_PNEAGraph) TSnap::GetInDegCnt<PNEAGraph>;
%template(GetOutDegCnt_PNEAGraph) TSnap::GetOutDegCnt<PNEAGraph>;
%template(GetDegCnt_PNEAGraph) TSnap::GetDegCnt<PNEAGraph>;
%template(GetDegSeqV_PNEAGraph) TSnap::GetDegSeqV<PNEAGraph>;

%template(GetNodeInDegV_PNEAGraph) TSnap::GetNodeInDegV<PNEAGraph>;
%template(GetNodeOutDegV_PNEAGraph) TSnap::GetNodeOutDegV<PNEAGraph>;

%template(CntUniqUndirEdges_PNEAGraph) TSnap::CntUniqUndirEdges<PNEAGraph>;
%template(CntUniqDirEdges_PNEAGraph) TSnap::CntUniqDirEdges<PNEAGraph>;
%template(CntUniqBiDirEdges_PNEAGraph) TSnap::CntUniqBiDirEdges<PNEAGraph>;
%template(CntSelfEdges_PNEAGraph) TSnap::CntSelfEdges<PNEAGraph>;

%template(GetBfsTree_PNGraph) TSnap::GetBfsTree<PNGraph>;
%template(DrawGViz_PNGraph) TSnap::DrawGViz<PNGraph>;