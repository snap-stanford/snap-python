// pneagraph.i
// Templates for SNAP Ringo
//

/*
  Instanstiates templates from SNAP for inclusion in RINGO.
  Note in Vim, this replaces SNAP Template headers:
 
 :%s#^template.*<class PGraph> \S* \([^(]*\).*#%template(\1_PNEAGraph) TSnap::\1<PNEAGraph>;#gc
 :%s#^///.*\n:##g
*/


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

//%include "getassessment.cpp"
//%template(GenSyntheticGraph_PNEAGraph) GenSyntheticGraph<PNEAGraph>;

// Convert a directed graph to a multi-edge attribute graph
%template(ConvertGraph_PNGraphToPNEAGraph) ConvertGraph<PNEAGraph, PNGraph>;

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
