// pundirnet.i
// Templates for SNAP TUndirNet, PUndirNet

%extend TUndirNet {
        TUndirNetNodeI BegNI() {
                return TUndirNetNodeI($self->BegNI());
        }
        TUndirNetNodeI EndNI() {
                return TUndirNetNodeI($self->EndNI());
        }
        TUndirNetNodeI GetNI(const int &NId) {
                return TUndirNetNodeI($self->GetNI(NId));
        }
        TUndirNetEdgeI BegEI() {
                return TUndirNetEdgeI($self->BegEI());
        }
        TUndirNetEdgeI EndEI() {
                return TUndirNetEdgeI($self->EndEI());
        }
};

%pythoncode %{
# redefine TUndirNetEdgeI.GetId to return a pair of nodes rather than -1
def GetId(self):
    return (self.GetSrcNId(), self.GetDstNId())

TUndirNetEdgeI.GetId = GetId
%}

// Basic Undirected Graphs

%template(PrintGraphStatTable_PUndirNet) PrintGraphStatTable<PUndirNet>;

//%template(MxSccSz_PUndirNet) TSnap::GetMxScc<PUndirNet>;
//%template(MxWccSz_PUndirNet) TSnap::GetMxWccSz<PUndirNet>;
// End Basic Directed Graphs

// Basic PUndirNets
%template(PUndirNet) TPt< TUndirNet >;

// gbase.h - PUndirNet
%template(PrintInfo_PUndirNet) TSnap::PrintInfo<PUndirNet>;

// cncom.h - PUndirNet
%template(GetNodeWcc_PUndirNet) TSnap::GetNodeWcc<PUndirNet>;
%template(IsConnected_PUndirNet) TSnap::IsConnected<PUndirNet>;
%template(IsWeaklyConn_PUndirNet) TSnap::IsWeaklyConn<PUndirNet>;
%template(GetWccSzCnt_PUndirNet) TSnap::GetWccSzCnt<PUndirNet>;
%template(GetWccs_PUndirNet) TSnap::GetWccs<PUndirNet>;
%template(GetSccSzCnt_PUndirNet) TSnap::GetSccSzCnt<PUndirNet>;
%template(GetSccs_PUndirNet) TSnap::GetSccs<PUndirNet>;
%template(GetMxWccSz_PUndirNet) TSnap::GetMxWccSz<PUndirNet>;
%template(GetMxSccSz_PUndirNet) TSnap::GetMxSccSz<PUndirNet>;

%template(GetMxWcc_PUndirNet) TSnap::GetMxWcc<PUndirNet>;
%template(GetMxScc_PUndirNet) TSnap::GetMxScc<PUndirNet>;
%template(GetMxBiCon_PUndirNet) TSnap::GetMxBiCon<PUndirNet>;

// centr.h - PUndirNet
%template(GetNodeEcc_PUndirNet) TSnap::GetNodeEcc<PUndirNet>;
%template(GetPageRank_PUndirNet) TSnap::GetPageRank<PUndirNet>;
%template(GetPageRank_v1_PUndirNet) TSnap::GetPageRank_v1<PUndirNet>;
%template(GetHits_PUndirNet) TSnap::GetHits<PUndirNet>;
#ifdef _OPENMP
%template(GetPageRankMP_PUndirNet) TSnap::GetPageRankMP<PUndirNet>;
%template(GetHitsMP_PUndirNet) TSnap::GetHitsMP<PUndirNet>;
#endif

// alg.h - PUndirNet
%template(CntInDegNodes_PUndirNet) TSnap::CntInDegNodes<PUndirNet>;
%template(CntOutDegNodes_PUndirNet) TSnap::CntOutDegNodes<PUndirNet>;
%template(CntDegNodes_PUndirNet) TSnap::CntDegNodes<PUndirNet>;
%template(CntNonZNodes_PUndirNet) TSnap::CntNonZNodes<PUndirNet>;
%template(CntEdgesToSet_PUndirNet) TSnap::CntEdgesToSet<PUndirNet>;

%template(GetMxDegNId_PUndirNet) TSnap::GetMxDegNId<PUndirNet>;
%template(GetMxInDegNId_PUndirNet) TSnap::GetMxInDegNId<PUndirNet>;
%template(GetMxOutDegNId_PUndirNet) TSnap::GetMxOutDegNId<PUndirNet>;

%template(GetInDegCnt_PUndirNet) TSnap::GetInDegCnt<PUndirNet>;
%template(GetOutDegCnt_PUndirNet) TSnap::GetOutDegCnt<PUndirNet>;
%template(GetDegCnt_PUndirNet) TSnap::GetDegCnt<PUndirNet>;
%template(GetDegSeqV_PUndirNet) TSnap::GetDegSeqV<PUndirNet>;

%template(GetNodeInDegV_PUndirNet) TSnap::GetNodeInDegV<PUndirNet>;
%template(GetNodeOutDegV_PUndirNet) TSnap::GetNodeOutDegV<PUndirNet>;

%template(CntUniqUndirEdges_PUndirNet) TSnap::CntUniqUndirEdges<PUndirNet>;
%template(CntUniqDirEdges_PUndirNet) TSnap::CntUniqDirEdges<PUndirNet>;
%template(CntUniqBiDirEdges_PUndirNet) TSnap::CntUniqBiDirEdges<PUndirNet>;
%template(CntSelfEdges_PUndirNet) TSnap::CntSelfEdges<PUndirNet>;

%template(GetUnDir_PUndirNet) TSnap::GetUnDir<PUndirNet>;
%template(MakeUnDir_PUndirNet) TSnap::MakeUnDir<PUndirNet>;
%template(AddSelfEdges_PUndirNet) TSnap::AddSelfEdges<PUndirNet>;
%template(DelSelfEdges_PUndirNet) TSnap::DelSelfEdges<PUndirNet>;
%template(DelNodes_PUndirNet) TSnap::DelNodes<PUndirNet>;
%template(DelZeroDegNodes_PUndirNet) TSnap::DelZeroDegNodes<PUndirNet>;
%template(DelDegKNodes_PUndirNet) TSnap::DelDegKNodes<PUndirNet>;
%template(IsTree_PUndirNet) TSnap::IsTree<PUndirNet>;
%template(GetTreeRootNId_PUndirNet) TSnap::GetTreeRootNId<PUndirNet>;
%template(GetTreeSig_PUndirNet) TSnap::GetTreeSig<PUndirNet>;


// bfsdfs.h - PUndirNet
%template(GetBfsTree_PUndirNet) TSnap::GetBfsTree<PUndirNet>;
%template(GetSubTreeSz_PUndirNet) TSnap::GetSubTreeSz<PUndirNet>;
%template(GetNodesAtHop_PUndirNet) TSnap::GetNodesAtHop<PUndirNet>;
%template(GetNodesAtHops_PUndirNet) TSnap::GetNodesAtHops<PUndirNet>;
// Shortest paths
%template(GetShortPath_PUndirNet) TSnap::GetShortPath<PUndirNet>;
// Diameter
%template(GetBfsFullDiam_PUndirNet) TSnap::GetBfsFullDiam<PUndirNet>;
%template(GetBfsEffDiam_PUndirNet) TSnap::GetBfsEffDiam<PUndirNet>;


// drawgviz.h
%template(DrawGViz_PUndirNet) TSnap::DrawGViz<PUndirNet>;


// ggen.h
%template(GenGrid_PUndirNet) TSnap::GenGrid<PUndirNet>;
%template(GenStar_PUndirNet) TSnap::GenStar<PUndirNet>;
%template(GenCircle_PUndirNet) TSnap::GenCircle<PUndirNet>;
%template(GenFull_PUndirNet) TSnap::GenFull<PUndirNet>;
%template(GenTree_PUndirNet) TSnap::GenTree<PUndirNet>;
%template(GenBaraHierar_PUndirNet) TSnap::GenBaraHierar<PUndirNet>;
%template(GenRndGnm_PUndirNet) TSnap::GenRndGnm<PUndirNet>;


// gio.h
%template(LoadEdgeList_PUndirNet) TSnap::LoadEdgeList<PUndirNet>;
%template(LoadEdgeListStr_PUndirNet) TSnap::LoadEdgeListStr<PUndirNet>;
%template(LoadConnList_PUndirNet) TSnap::LoadConnList<PUndirNet>;
%template(LoadConnListStr_PUndirNet) TSnap::LoadConnListStr<PUndirNet>;
%template(LoadPajek_PUndirNet) TSnap::LoadPajek<PUndirNet>;
%template(SaveEdgeList_PUndirNet) TSnap::SaveEdgeList<PUndirNet>;
%template(SavePajek_PUndirNet) TSnap::SavePajek<PUndirNet>;
%template(SaveMatlabSparseMtx_PUndirNet) TSnap::SaveMatlabSparseMtx<PUndirNet>;
%template(SaveGViz_PUndirNet) TSnap::SaveGViz<PUndirNet>;


// kcore.h
%template(GetKCore_PUndirNet) TSnap::GetKCore<PUndirNet>;
%template(GetKCoreEdges_PUndirNet) TSnap::GetKCoreEdges<PUndirNet>;
%template(GetKCoreNodes_PUndirNet) TSnap::GetKCoreNodes<PUndirNet>;



// subgraph.h
%template(ConvertGraph_PUndirNet_PUndirNet) TSnap::ConvertGraph <PUndirNet, PUndirNet>;
%template(ConvertGraph_PUndirNet_PNGraph) TSnap::ConvertGraph <PUndirNet, PNGraph>;
%template(ConvertGraph_PUndirNet_PNEANet) TSnap::ConvertGraph <PUndirNet, PNEANet>;
%template(ConvertSubGraph_PUndirNet_PUndirNet) TSnap::ConvertSubGraph <PUndirNet, PUndirNet>;
%template(ConvertSubGraph_PUndirNet_PNGraph) TSnap::ConvertSubGraph <PUndirNet, PNGraph>;
%template(ConvertSubGraph_PUndirNet_PNEANet) TSnap::ConvertSubGraph <PUndirNet, PNEANet>;
%template(ConvertESubGraph_PUndirNet_PNEANet) TSnap::ConvertESubGraph <PUndirNet, PNEANet>;
%template(GetSubGraph_PUndirNet) TSnap::GetSubGraph<PUndirNet>;
%template(GetRndSubGraph_PUndirNet) TSnap::GetRndSubGraph<PUndirNet>;
%template(GetRndESubGraph_PUndirNet) TSnap::GetRndESubGraph<PUndirNet>;


// triad.h - PUndirNet
%template(GetClustCf_PUndirNet) TSnap::GetClustCf<PUndirNet>;
%template(GetNodeClustCf_PUndirNet) TSnap::GetNodeClustCf<PUndirNet>;
%template(GetTriads_PUndirNet) TSnap::GetTriads<PUndirNet>;
%template(GetTriadEdges_PUndirNet) TSnap::GetTriadEdges<PUndirNet>;
%template(GetNodeTriads_PUndirNet) TSnap::GetNodeTriads<PUndirNet>;
%template(GetTriadParticip_PUndirNet) TSnap::GetTriadParticip<PUndirNet>;
%template(GetTriangleCnt_PUndirNet) TSnap::GetTriangleCnt<PUndirNet>;

%template(GetCmnNbrs_PUndirNet) TSnap::GetCmnNbrs<PUndirNet>;
//%template(GetLen2Paths_PUndirNet) TSnap::GetLen2Paths<PUndirNet>;


// cmty.h - PUndirNet
%template(GetModularity_PUndirNet) TSnap::GetModularity<PUndirNet>;
%template(GetEdgesInOut_PUndirNet) TSnap::GetEdgesInOut<PUndirNet>;


// anf.h - PUndirNet
%template(GetAnf_PUndirNet) TSnap::GetAnf<PUndirNet>;
%template(GetAnfEffDiam_PUndirNet) TSnap::GetAnfEffDiam<PUndirNet>;
%template(TestAnf_PUndirNet) TSnap::TestAnf<PUndirNet>;


// statplot.h - PUndirNet
%template(PlotKCoreEdges_PUndirNet) TSnap::PlotKCoreEdges<PUndirNet>;
%template(PlotKCoreNodes_PUndirNet) TSnap::PlotKCoreNodes<PUndirNet>;
%template(PlotShortPathDistr_PUndirNet) TSnap::PlotShortPathDistr<PUndirNet>;
%template(PlotHops_PUndirNet) TSnap::PlotHops<PUndirNet>;
%template(PlotClustCf_PUndirNet) TSnap::PlotClustCf<PUndirNet>;
%template(PlotSccDistr_PUndirNet) TSnap::PlotSccDistr<PUndirNet>;
%template(PlotWccDistr_PUndirNet) TSnap::PlotWccDistr<PUndirNet>;
%template(PlotOutDegDistr_PUndirNet) TSnap::PlotOutDegDistr<PUndirNet>;
%template(PlotInDegDistr_PUndirNet) TSnap::PlotInDegDistr<PUndirNet>;


// goodgraph.cpp - PUndirNet
%template(PercentDegree_PUndirNet) PercentDegree<PUndirNet>;
%template(NodesGTEDegree_PUndirNet) NodesGTEDegree<PUndirNet>;
%template(MxDegree_PUndirNet) MxDegree<PUndirNet>;
%template(PercentMxWcc_PUndirNet) PercentMxWcc<PUndirNet>;
%template(PercentMxScc_PUndirNet) PercentMxScc<PUndirNet>;

// conv.h - PUndirNet
%template(ToGraph_PUndirNet) TSnap::ToGraph<PUndirNet>;

