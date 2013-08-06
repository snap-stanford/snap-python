// pngraph.i
// Templates for SNAP

// Note: This file does not include all SNAP templates.

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

// Basic Directed Graphs
%template(PNGraph) TPt< TNGraph >;

%template(PercentDegree_PNGraph) PercentDegree<PNGraph>;
%template(PercentMxWcc_PNGraph) PercentMxWcc<PNGraph>;
%template(PercentMxScc_PNGraph) PercentMxScc<PNGraph>;

%template(LoadEdgeList_PNGraph) TSnap::LoadEdgeList<PNGraph>;
%template(PrintGraphStatTable_PNGraph) PrintGraphStatTable<PNGraph>;
//%template(GenRndGnm_PNGraph) TSnap::GenRndGnm<PNGraph>;
%template(GenRndGnm_PNGraph) TSnap::GenRndGnm<PNGraph>;

%template(NodesGTEDegree_PNGraph) NodesGTEDegree<PNGraph>;
%template(MxDegree_PNGraph) MxDegree<PNGraph>;
%template(MxSccSz_PNGraph) TSnap::GetMxScc<PNGraph>;
%template(MxWccSz_PNGraph) TSnap::GetMxWccSz<PNGraph>;
%template(MxDegree_PNGraph) MxDegree<PNGraph>;

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
