// pungraph.i
// Templates for SNAP TUNGraph, PUNGraph

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

%pythoncode %{
# redefine TUNGraphEdgeI.GetId to return a pair of nodes rather than -1
def GetId(self):
    return (self.GetSrcNId(), self.GetDstNId())

TUNGraphEdgeI.GetId = GetId
%}

// Basic Undirected Graphs

%template(LoadEdgeList_PUNGraph) TSnap::LoadEdgeList<PUNGraph>;
%template(PrintGraphStatTable_PUNGraph) PrintGraphStatTable<PUNGraph>;

//%template(MxSccSz_PUNGraph) TSnap::GetMxScc<PUNGraph>;
//%template(MxWccSz_PUNGraph) TSnap::GetMxWccSz<PUNGraph>;
// End Basic Directed Graphs

// Basic PUNGraphs
%template(PUNGraph) TPt< TUNGraph >;

// cncom.h - PUNGraph
%template(GetNodeWcc_PUNGraph) TSnap::GetNodeWcc<PUNGraph>;
%template(IsConnected_PUNGraph) TSnap::IsConnected<PUNGraph>;
%template(IsWeaklyConn_PUNGraph) TSnap::IsWeaklyConn<PUNGraph>;
%template(GetWccSzCnt_PUNGraph) TSnap::GetWccSzCnt<PUNGraph>;
%template(GetWccs_PUNGraph) TSnap::GetWccs<PUNGraph>;
%template(GetSccSzCnt_PUNGraph) TSnap::GetSccSzCnt<PUNGraph>;
%template(GetSccs_PUNGraph) TSnap::GetSccs<PUNGraph>;
%template(GetMxWccSz_PUNGraph) TSnap::GetMxWccSz<PUNGraph>;

%template(GetMxWcc_PUNGraph) TSnap::GetMxWcc<PUNGraph>;
%template(GetMxScc_PUNGraph) TSnap::GetMxScc<PUNGraph>;
%template(GetMxBiCon_PUNGraph) TSnap::GetMxBiCon<PUNGraph>;


// alg.h - PUNGraph
%template(CntInDegNodes_PUNGraph) TSnap::CntInDegNodes<PUNGraph>;
%template(CntOutDegNodes_PUNGraph) TSnap::CntOutDegNodes<PUNGraph>;
%template(CntDegNodes_PUNGraph) TSnap::CntDegNodes<PUNGraph>;
%template(CntNonZNodes_PUNGraph) TSnap::CntNonZNodes<PUNGraph>;
%template(CntEdgesToSet_PUNGraph) TSnap::CntEdgesToSet<PUNGraph>;

%template(GetMxDegNId_PUNGraph) TSnap::GetMxDegNId<PUNGraph>;
%template(GetMxInDegNId_PUNGraph) TSnap::GetMxInDegNId<PUNGraph>;
%template(GetMxOutDegNId_PUNGraph) TSnap::GetMxOutDegNId<PUNGraph>;

%template(GetInDegCnt_PUNGraph) TSnap::GetInDegCnt<PUNGraph>;
%template(GetOutDegCnt_PUNGraph) TSnap::GetOutDegCnt<PUNGraph>;
%template(GetDegCnt_PUNGraph) TSnap::GetDegCnt<PUNGraph>;
%template(GetDegSeqV_PUNGraph) TSnap::GetDegSeqV<PUNGraph>;

%template(GetNodeInDegV_PUNGraph) TSnap::GetNodeInDegV<PUNGraph>;
%template(GetNodeOutDegV_PUNGraph) TSnap::GetNodeOutDegV<PUNGraph>;

%template(CntUniqUndirEdges_PUNGraph) TSnap::CntUniqUndirEdges<PUNGraph>;
%template(CntUniqDirEdges_PUNGraph) TSnap::CntUniqDirEdges<PUNGraph>;
%template(CntUniqBiDirEdges_PUNGraph) TSnap::CntUniqBiDirEdges<PUNGraph>;
%template(CntSelfEdges_PUNGraph) TSnap::CntSelfEdges<PUNGraph>;


// bfsdfs.h - PUNGraph
%template(GetBfsTree_PUNGraph) TSnap::GetBfsTree<PUNGraph>;
%template(GetSubTreeSz_PUNGraph) TSnap::GetSubTreeSz<PUNGraph>;
%template(GetNodesAtHop_PUNGraph) TSnap::GetNodesAtHop<PUNGraph>;
%template(GetNodesAtHops_PUNGraph) TSnap::GetNodesAtHops<PUNGraph>;
// Shortest paths
%template(GetShortPath_PUNGraph) TSnap::GetShortPath<PUNGraph>;
// Diameter
%template(GetBfsFullDiam_PUNGraph) TSnap::GetBfsFullDiam<PUNGraph>;
%template(GetBfsEffDiam_PUNGraph) TSnap::GetBfsEffDiam<PUNGraph>;


// drawgviz.h
%template(DrawGViz_PUNGraph) TSnap::DrawGViz<PUNGraph>;


// ggen.h
%template(GenGrid_PUNGraph) TSnap::GenGrid<PUNGraph>;
%template(GenStar_PUNGraph) TSnap::GenStar<PUNGraph>;
%template(GenCircle_PUNGraph) TSnap::GenCircle<PUNGraph>;
%template(GenFull_PUNGraph) TSnap::GenFull<PUNGraph>;
%template(GenTree_PUNGraph) TSnap::GenTree<PUNGraph>;
%template(GenBaraHierar_PUNGraph) TSnap::GenBaraHierar<PUNGraph>;
%template(GenRndGnm_PUNGraph) TSnap::GenRndGnm<PUNGraph>;


// triad.h - PUNGraph
%template(GetClustCf_PUNGraph) TSnap::GetClustCf<PUNGraph>;
%template(GetNodeClustCf_PUNGraph) TSnap::GetNodeClustCf<PUNGraph>;
%template(GetTriads_PUNGraph) TSnap::GetTriads<PUNGraph>;
%template(GetTriadEdges_PUNGraph) TSnap::GetTriadEdges<PUNGraph>;
//%template(GetNodeTriads_PUNGraph) TSnap::GetNodeTriads<PUNGraph>;
%template(GetTriadParticip_PUNGraph) TSnap::GetTriadParticip<PUNGraph>;

%template(GetCmnNbrs_PUNGraph) TSnap::GetCmnNbrs<PUNGraph>;
//%template(GetLen2Paths_PUNGraph) TSnap::GetLen2Paths<PUNGraph>;


// cmty.h - PUNGraph
%template(GetModularity_PUNGraph) TSnap::GetModularity<PUNGraph>;
%template(GetEdgesInOut_PUNGraph) TSnap::GetEdgesInOut<PUNGraph>;


// anf.h - PUNGraph
%template(GetAnf_PUNGraph) TSnap::GetAnf<PUNGraph>;
%template(GetAnfEffDiam_PUNGraph) TSnap::GetAnfEffDiam<PUNGraph>;


// goodgraph.cpp - PUNGraph
%template(PercentDegree_PUNGraph) PercentDegree<PUNGraph>;
%template(NodesGTEDegree_PUNGraph) NodesGTEDegree<PUNGraph>;
%template(MxDegree_PUNGraph) MxDegree<PUNGraph>;
%template(PercentMxWcc_PUNGraph) PercentMxWcc<PUNGraph>;
%template(PercentMxScc_PUNGraph) PercentMxScc<PUNGraph>;

