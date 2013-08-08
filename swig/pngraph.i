// pngraph.i
// Templates for SNAP TNGraph, PNGraph

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

%pythoncode %{
# redefine TNGraphEdgeI.GetId to return a pair of nodes rather than -1
def GetId(self):
    return (self.GetSrcNId(), self.GetDstNId())

TNGraphEdgeI.GetId = GetId
%}


// Basic Undirected Graphs

%template(PrintGraphStatTable_PNGraph) PrintGraphStatTable<PNGraph>;

//%template(MxSccSz_PNGraph) TSnap::GetMxScc<PNGraph>;
//%template(MxWccSz_PNGraph) TSnap::GetMxWccSz<PNGraph>;
// End Basic Directed Graphs

// Basic PNGraphs
%template(PNGraph) TPt< TNGraph >;

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


// alg.h - PNGraph
%template(CntInDegNodes_PNGraph) TSnap::CntInDegNodes<PNGraph>;
%template(CntOutDegNodes_PNGraph) TSnap::CntOutDegNodes<PNGraph>;
%template(CntDegNodes_PNGraph) TSnap::CntDegNodes<PNGraph>;
%template(CntNonZNodes_PNGraph) TSnap::CntNonZNodes<PNGraph>;
%template(CntEdgesToSet_PNGraph) TSnap::CntEdgesToSet<PNGraph>;

%template(GetMxDegNId_PNGraph) TSnap::GetMxDegNId<PNGraph>;
%template(GetMxInDegNId_PNGraph) TSnap::GetMxInDegNId<PNGraph>;
%template(GetMxOutDegNId_PNGraph) TSnap::GetMxOutDegNId<PNGraph>;

%template(GetInDegCnt_PNGraph) TSnap::GetInDegCnt<PNGraph>;
%template(GetOutDegCnt_PNGraph) TSnap::GetOutDegCnt<PNGraph>;
%template(GetDegCnt_PNGraph) TSnap::GetDegCnt<PNGraph>;
%template(GetDegSeqV_PNGraph) TSnap::GetDegSeqV<PNGraph>;

%template(GetNodeInDegV_PNGraph) TSnap::GetNodeInDegV<PNGraph>;
%template(GetNodeOutDegV_PNGraph) TSnap::GetNodeOutDegV<PNGraph>;

%template(CntUniqUndirEdges_PNGraph) TSnap::CntUniqUndirEdges<PNGraph>;
%template(CntUniqDirEdges_PNGraph) TSnap::CntUniqDirEdges<PNGraph>;
%template(CntUniqBiDirEdges_PNGraph) TSnap::CntUniqBiDirEdges<PNGraph>;
%template(CntSelfEdges_PNGraph) TSnap::CntSelfEdges<PNGraph>;


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


// drawgviz.h
%template(DrawGViz_PNGraph) TSnap::DrawGViz<PNGraph>;


// ggen.h
%template(GenGrid_PNGraph) TSnap::GenGrid<PNGraph>;
%template(GenStar_PNGraph) TSnap::GenStar<PNGraph>;
%template(GenCircle_PNGraph) TSnap::GenCircle<PNGraph>;
%template(GenFull_PNGraph) TSnap::GenFull<PNGraph>;
%template(GenTree_PNGraph) TSnap::GenTree<PNGraph>;
%template(GenBaraHierar_PNGraph) TSnap::GenBaraHierar<PNGraph>;
%template(GenRndGnm_PNGraph) TSnap::GenRndGnm<PNGraph>;


// gio.h
%template(LoadEdgeList_PNGraph) TSnap::LoadEdgeList<PNGraph>;
%template(LoadEdgeListStr_PNGraph) TSnap::LoadEdgeListStr<PNGraph>;
%template(LoadConnList_PNGraph) TSnap::LoadConnList<PNGraph>;
%template(LoadConnListStr_PNGraph) TSnap::LoadConnListStr<PNGraph>;
%template(LoadPajek_PNGraph) TSnap::LoadPajek<PNGraph>;
%template(SaveEdgeList_PNGraph) TSnap::SaveEdgeList<PNGraph>;
%template(SavePajek_PNGraph) TSnap::SavePajek<PNGraph>;
%template(SaveMatlabSparseMtx_PNGraph) TSnap::SaveMatlabSparseMtx<PNGraph>;
%template(SaveGViz_PNGraph) TSnap::SaveGViz<PNGraph>;


// triad.h - PNGraph
%template(GetClustCf_PNGraph) TSnap::GetClustCf<PNGraph>;
%template(GetNodeClustCf_PNGraph) TSnap::GetNodeClustCf<PNGraph>;
%template(GetTriads_PNGraph) TSnap::GetTriads<PNGraph>;
%template(GetTriadEdges_PNGraph) TSnap::GetTriadEdges<PNGraph>;
//%template(GetNodeTriads_PNGraph) TSnap::GetNodeTriads<PNGraph>;
%template(GetTriadParticip_PNGraph) TSnap::GetTriadParticip<PNGraph>;

%template(GetCmnNbrs_PNGraph) TSnap::GetCmnNbrs<PNGraph>;
//%template(GetLen2Paths_PNGraph) TSnap::GetLen2Paths<PNGraph>;


// cmty.h - PNGraph
%template(GetModularity_PNGraph) TSnap::GetModularity<PNGraph>;
%template(GetEdgesInOut_PNGraph) TSnap::GetEdgesInOut<PNGraph>;


// anf.h - PNGraph
%template(GetAnf_PNGraph) TSnap::GetAnf<PNGraph>;
%template(GetAnfEffDiam_PNGraph) TSnap::GetAnfEffDiam<PNGraph>;


// goodgraph.cpp - PNGraph
%template(PercentDegree_PNGraph) PercentDegree<PNGraph>;
%template(NodesGTEDegree_PNGraph) NodesGTEDegree<PNGraph>;
%template(MxDegree_PNGraph) MxDegree<PNGraph>;
%template(PercentMxWcc_PNGraph) PercentMxWcc<PNGraph>;
%template(PercentMxScc_PNGraph) PercentMxScc<PNGraph>;

