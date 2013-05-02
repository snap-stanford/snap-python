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
%include "gviz.h"

%include "kcore.h"
%include "gsvd.h"
%include "centr.h"

// FIXME: gstat.h:51: Error: Syntax error in input(3)
//%include "gstat.h"

%include "cmty.h"
%include "ff.h"
%include "anf.h"

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

// Basic Directed Graphs
%template(PNGraph) TPt< TNGraph >;

%template(PercentDegree_PNGraph) PercentDegree<PNGraph>;
%template(PercentMxWcc_PNGraph) PercentMxWcc<PNGraph>;
%template(PercentMxScc_PNGraph) PercentMxScc<PNGraph>;

%template(LoadEdgeList_PNGraph) TSnap::LoadEdgeList<PNGraph>;
%template(PrintGraphStatTable_PNGraph) PrintGraphStatTable<PNGraph>;
%template(GenRndGnm_PNGraph) TSnap::GenRndGnm<PNGraph>;

%template(NodesGTEDegree_PNGraph) NodesGTEDegree<PNGraph>;
%template(MxDegree_PNGraph) MxDegree<PNGraph>;
%template(MxSccSz_PNGraph) TSnap::GetMxScc<PNGraph>;
%template(MxWccSz_PNGraph) TSnap::GetMxWccSz<PNGraph>;
%template(MxDegree_PNGraph) MxDegree<PNGraph>;
// End Basic Directed Graphs


// Basic Undirected Graphs
%template(PUNGraph) TPt< TUNGraph >;

%template(LoadEdgeList_PUNGraph) TSnap::LoadEdgeList<PUNGraph>;
%template(PrintGraphStatTable_PUNGraph) PrintGraphStatTable<PUNGraph>;

%template(NodesGTEDegree_PUNGraph) NodesGTEDegree<PUNGraph>;
%template(GenRndGnm_PUNGraph) TSnap::GenRndGnm<PUNGraph>;
%template(MxSccSz_PUNGraph) TSnap::GetMxScc<PUNGraph>;
%template(MxWccSz_PUNGraph) TSnap::GetMxWccSz<PUNGraph>;
%template(MxDegree_PUNGraph) MxDegree<PUNGraph>;
// End Basic Undirected Graphs


// Basic PNEAGraphs
%template(PNEAGraph) TPt< TNEAGraph >;
%template(GenRndGnm_PNEAGraph) TSnap::GenRndGnm<PNEAGraph>;
%template(NodesGTEDegree_PNEAGraph) NodesGTEDegree<PNEAGraph>;

%template(MxDegree_PNEAGraph) MxDegree<PNEAGraph>;

// cncom.h - PNEAGraph
%template(GetNodeWcc_PNEAGraph) TSnap::GetNodeWcc<PNEAGraph>;
%template(IsConnected_PNEAGraph) TSnap::IsConnected<PNEAGraph>;
%template(IsWeaklyConn_PNEAGraph) TSnap::IsWeaklyConn<PNEAGraph>;
%template(GetWccSzCnt_PNEAGraph) TSnap::GetWccSzCnt<PNEAGraph>;
%template(GetWccs_PNEAGraph) TSnap::GetWccs<PNEAGraph>;
%template(GetSccSzCnt_PNEAGraph) TSnap::GetSccSzCnt<PNEAGraph>;
%template(GetSccs_PNEAGraph) TSnap::GetSccs<PNEAGraph>;
%template(GetMxWccSz_PNEAGraph) TSnap::GetMxWccSz<PNEAGraph>;

%template(GetMxWcc_PNEAGraph) TSnap::GetMxWcc<PNEAGraph>;
%template(GetMxScc_PNEAGraph) TSnap::GetMxScc<PNEAGraph>;
%template(GetMxBiCon_PNEAGraph) TSnap::GetMxBiCon<PNEAGraph>;

// cncom.h - PNGraph
%template(GetNodeWcc_PNGraph) TSnap::GetNodeWcc<PNGraph>;
%template(IsConnected_PNGraph) TSnap::IsConnected<PNGraph>;
%template(IsWeaklyConn_PNGraph) TSnap::IsWeaklyConn<PNGraph>;
%template(GetWccSzCnt_PNGraph) TSnap::GetWccSzCnt<PNGraph>;
%template(GetWccs_PNGraph) TSnap::GetWccs<PNGraph>;
%template(GetSccSzCnt_PNGraph) TSnap::GetSccSzCnt<PNGraph>;
%template(GetSccs_PNGraph) TSnap::GetSccs<PNGraph>;
%template(GetMxWccSz_PNGraph) TSnap::GetMxWccSz<PNGraph>;

%template(GetMxWcc_PNGraph) TSnap::GetMxWcc<PNGraph>;
%template(GetMxScc_PNGraph) TSnap::GetMxScc<PNGraph>;
%template(GetMxBiCon_PNGraph) TSnap::GetMxBiCon<PNGraph>;
// End cncom.h

// alg.h - PNEAGraph
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
/* End alg.h */

// bfsdfs.h - PNGraph
%template(GetBfsTree_PNGraph) TSnap::GetBfsTree<PNGraph>;
%template(GetSubTreeSz_PNGraph) TSnap::GetSubTreeSz<PNGraph>;
%template(GetNodesAtHop_PNGraph) TSnap::GetNodesAtHop<PNGraph>;
%template(GetNodesAtHops_PNGraph) TSnap::GetNodesAtHops<PNGraph>;
// Shortest paths
%template(GetShortPath_PNGraph) TSnap::GetShortPath<PNGraph>;
// Diameter
%template(GetBfsFullDiam_PNGraph) TSnap::GetBfsFullDiam<PNGraph>;
%template(GetBfsEffDiam_PNGraph) TSnap::GetBfsEffDiam<PNGraph>;

// bfsdfs.h - PNEAGraph
%template(GetBfsTree_PNEAGraph) TSnap::GetBfsTree<PNEAGraph>;
%template(GetSubTreeSz_PNEAGraph) TSnap::GetSubTreeSz<PNEAGraph>;
%template(GetNodesAtHop_PNEAGraph) TSnap::GetNodesAtHop<PNEAGraph>;
%template(GetNodesAtHops_PNEAGraph) TSnap::GetNodesAtHops<PNEAGraph>;
// Shortest paths
%template(GetShortPath_PNEAGraph) TSnap::GetShortPath<PNEAGraph>;
// Diameter
%template(GetBfsFullDiam_PNEAGraph) TSnap::GetBfsFullDiam<PNEAGraph>;
%template(GetBfsEffDiam_PNEAGraph) TSnap::GetBfsEffDiam<PNEAGraph>;

// drawgviz.h
%template(DrawGViz_PNEAGraph) TSnap::DrawGViz<PNEAGraph>;
%template(DrawGViz_PNGraph) TSnap::DrawGViz<PNGraph>;

// triad.h - PNEAGraph
%template(GetClustCf_PNEAGraph) TSnap::GetClustCf<PNEAGraph>;
%template(GetNodeClustCf_PNEAGraph) TSnap::GetNodeClustCf<PNEAGraph>;

%template(GetTriads_PNEAGraph) TSnap::GetTriads<PNEAGraph>;
%template(GetTriadEdges_PNEAGraph) TSnap::GetTriadEdges<PNEAGraph>;
//%template(GetNodeTriads_PNEAGraph) TSnap::GetNodeTriads<PNEAGraph>;
%template(GetTriadParticip_PNEAGraph) TSnap::GetTriadParticip<PNEAGraph>;

%template(GetCmnNbrs_PNEAGraph) TSnap::GetCmnNbrs<PNEAGraph>;
//%template(GetLen2Paths_PNEAGraph) TSnap::GetLen2Paths<PNEAGraph>;

// cmty.h - PNEAGraph
%template(GetModularity_PNEAGraph) TSnap::GetModularity<PNEAGraph>;
%template(GetEdgesInOut_PNEAGraph) TSnap::GetEdgesInOut<PNEAGraph>;

// anf.h - PNEAGraph
%template(GetAnf_PNEAGraph) TSnap::GetAnf<PNEAGraph>;
%template(GetAnfEffDiam_PNEAGraph) TSnap::GetAnfEffDiam<PNEAGraph>;

/* Note in Vim, this replaces SNAP Template headers:
 
 :%s#^template.*<class PGraph> \S* \([^(]*\).*#%template(\1_PNEAGraph) TSnap::\1<PNEAGraph>;#gc
 :%s#^///.*\n:##g
 
*/
