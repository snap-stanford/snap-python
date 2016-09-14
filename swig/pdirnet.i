// pdirnet.i
// Templates for SNAP TDirNet, PDirNet

%extend TDirNet {
        TDirNetNodeI BegNI() {
                return TDirNetNodeI($self->BegNI());
        }
        TDirNetNodeI EndNI() {
                return TDirNetNodeI($self->EndNI());
        }
        TDirNetNodeI GetNI(const int &NId) {
                return TDirNetNodeI($self->GetNI(NId));
        }
        TDirNetEdgeI BegEI() {
                return TDirNetEdgeI($self->BegEI());
        }
        TDirNetEdgeI EndEI() {
                return TDirNetEdgeI($self->EndEI());
        }
};

%pythoncode %{
# redefine TDirNetEdgeI.GetId to return a pair of nodes rather than -1
def GetId(self):
    return (self.GetSrcNId(), self.GetDstNId())

TDirNetEdgeI.GetId = GetId
%}


// Basic Undirected Graphs

%template(PrintGraphStatTable_PDirNet) PrintGraphStatTable<PDirNet>;

//%template(MxSccSz_PDirNet) TSnap::GetMxScc<PDirNet>;
//%template(MxWccSz_PDirNet) TSnap::GetMxWccSz<PDirNet>;
// End Basic Directed Graphs

// Basic PDirNets
%template(PDirNet) TPt< TDirNet >;

// gbase.h - PDirNet
%template(PrintInfo_PDirNet) TSnap::PrintInfo<PDirNet>;

// cncom.h - PDirNet
%template(GetNodeWcc_PDirNet) TSnap::GetNodeWcc<PDirNet>;
%template(IsConnected_PDirNet) TSnap::IsConnected<PDirNet>;
%template(IsWeaklyConn_PDirNet) TSnap::IsWeaklyConn<PDirNet>;
%template(GetWccSzCnt_PDirNet) TSnap::GetWccSzCnt<PDirNet>;
%template(GetWccs_PDirNet) TSnap::GetWccs<PDirNet>;
%template(GetSccSzCnt_PDirNet) TSnap::GetSccSzCnt<PDirNet>;
%template(GetSccs_PDirNet) TSnap::GetSccs<PDirNet>;
%template(GetMxWccSz_PDirNet) TSnap::GetMxWccSz<PDirNet>;
%template(GetMxSccSz_PDirNet) TSnap::GetMxSccSz<PDirNet>;

%template(GetMxWcc_PDirNet) TSnap::GetMxWcc<PDirNet>;
%template(GetMxScc_PDirNet) TSnap::GetMxScc<PDirNet>;
%template(GetMxBiCon_PDirNet) TSnap::GetMxBiCon<PDirNet>;

// centr.h - PDirNet
%template(GetNodeEcc_PDirNet) TSnap::GetNodeEcc<PDirNet>;
%template(GetPageRank_PDirNet) TSnap::GetPageRank<PDirNet>;
%template(GetPageRank_v1_PDirNet) TSnap::GetPageRank_v1<PDirNet>;
%template(GetHits_PDirNet) TSnap::GetHits<PDirNet>;
#ifdef _OPENMP
%template(GetPageRankMP_PDirNet) TSnap::GetPageRankMP<PDirNet>;
%template(GetHitsMP_PDirNet) TSnap::GetHitsMP<PDirNet>;
#endif


// alg.h - PDirNet
%template(CntInDegNodes_PDirNet) TSnap::CntInDegNodes<PDirNet>;
%template(CntOutDegNodes_PDirNet) TSnap::CntOutDegNodes<PDirNet>;
%template(CntDegNodes_PDirNet) TSnap::CntDegNodes<PDirNet>;
%template(CntNonZNodes_PDirNet) TSnap::CntNonZNodes<PDirNet>;
%template(CntEdgesToSet_PDirNet) TSnap::CntEdgesToSet<PDirNet>;

%template(GetMxDegNId_PDirNet) TSnap::GetMxDegNId<PDirNet>;
%template(GetMxInDegNId_PDirNet) TSnap::GetMxInDegNId<PDirNet>;
%template(GetMxOutDegNId_PDirNet) TSnap::GetMxOutDegNId<PDirNet>;

%template(GetInDegCnt_PDirNet) TSnap::GetInDegCnt<PDirNet>;
%template(GetOutDegCnt_PDirNet) TSnap::GetOutDegCnt<PDirNet>;
%template(GetDegCnt_PDirNet) TSnap::GetDegCnt<PDirNet>;
%template(GetDegSeqV_PDirNet) TSnap::GetDegSeqV<PDirNet>;

%template(GetNodeInDegV_PDirNet) TSnap::GetNodeInDegV<PDirNet>;
%template(GetNodeOutDegV_PDirNet) TSnap::GetNodeOutDegV<PDirNet>;

%template(CntUniqUndirEdges_PDirNet) TSnap::CntUniqUndirEdges<PDirNet>;
%template(CntUniqDirEdges_PDirNet) TSnap::CntUniqDirEdges<PDirNet>;
%template(CntUniqBiDirEdges_PDirNet) TSnap::CntUniqBiDirEdges<PDirNet>;
%template(CntSelfEdges_PDirNet) TSnap::CntSelfEdges<PDirNet>;

%template(GetUnDir_PDirNet) TSnap::GetUnDir<PDirNet>;
%template(MakeUnDir_PDirNet) TSnap::MakeUnDir<PDirNet>;
%template(AddSelfEdges_PDirNet) TSnap::AddSelfEdges<PDirNet>;
%template(DelSelfEdges_PDirNet) TSnap::DelSelfEdges<PDirNet>;
%template(DelNodes_PDirNet) TSnap::DelNodes<PDirNet>;
%template(DelZeroDegNodes_PDirNet) TSnap::DelZeroDegNodes<PDirNet>;
%template(DelDegKNodes_PDirNet) TSnap::DelDegKNodes<PDirNet>;
%template(IsTree_PDirNet) TSnap::IsTree<PDirNet>;
%template(GetTreeRootNId_PDirNet) TSnap::GetTreeRootNId<PDirNet>;
%template(GetTreeSig_PDirNet) TSnap::GetTreeSig<PDirNet>;


// bfsdfs.h - PDirNet
%template(GetBfsTree_PDirNet) TSnap::GetBfsTree<PDirNet>;
%template(GetSubTreeSz_PDirNet) TSnap::GetSubTreeSz<PDirNet>;
%template(GetNodesAtHop_PDirNet) TSnap::GetNodesAtHop<PDirNet>;
%template(GetNodesAtHops_PDirNet) TSnap::GetNodesAtHops<PDirNet>;
// Shortest paths
%template(GetShortPath_PDirNet) TSnap::GetShortPath<PDirNet>;
// Diameter
%template(GetBfsFullDiam_PDirNet) TSnap::GetBfsFullDiam<PDirNet>;
%template(GetBfsEffDiam_PDirNet) TSnap::GetBfsEffDiam<PDirNet>;


// drawgviz.h
%template(DrawGViz_PDirNet) TSnap::DrawGViz<PDirNet>;


// ggen.h
%template(GenGrid_PDirNet) TSnap::GenGrid<PDirNet>;
%template(GenStar_PDirNet) TSnap::GenStar<PDirNet>;
%template(GenCircle_PDirNet) TSnap::GenCircle<PDirNet>;
%template(GenFull_PDirNet) TSnap::GenFull<PDirNet>;
%template(GenTree_PDirNet) TSnap::GenTree<PDirNet>;
%template(GenBaraHierar_PDirNet) TSnap::GenBaraHierar<PDirNet>;
%template(GenRndGnm_PDirNet) TSnap::GenRndGnm<PDirNet>;


// gio.h
%template(LoadEdgeList_PDirNet) TSnap::LoadEdgeList<PDirNet>;
%template(LoadEdgeListStr_PDirNet) TSnap::LoadEdgeListStr<PDirNet>;
%template(LoadConnList_PDirNet) TSnap::LoadConnList<PDirNet>;
%template(LoadConnListStr_PDirNet) TSnap::LoadConnListStr<PDirNet>;
%template(LoadPajek_PDirNet) TSnap::LoadPajek<PDirNet>;
%template(SaveEdgeList_PDirNet) TSnap::SaveEdgeList<PDirNet>;
%template(SavePajek_PDirNet) TSnap::SavePajek<PDirNet>;
%template(SaveMatlabSparseMtx_PDirNet) TSnap::SaveMatlabSparseMtx<PDirNet>;
%template(SaveGViz_PDirNet) TSnap::SaveGViz<PDirNet>;


// kcore.h
%template(GetKCore_PDirNet) TSnap::GetKCore<PDirNet>;
%template(GetKCoreEdges_PDirNet) TSnap::GetKCoreEdges<PDirNet>;
%template(GetKCoreNodes_PDirNet) TSnap::GetKCoreNodes<PDirNet>;


// subgraph.h
%template(ConvertGraph_PDirNet_PUNGraph) TSnap::ConvertGraph <PDirNet, PUNGraph>;
%template(ConvertGraph_PDirNet_PDirNet) TSnap::ConvertGraph <PDirNet, PDirNet>;
%template(ConvertGraph_PDirNet_PNEANet) TSnap::ConvertGraph <PDirNet, PNEANet>;
%template(ConvertSubGraph_PDirNet_PUNGraph) TSnap::ConvertSubGraph <PDirNet, PUNGraph>;
%template(ConvertSubGraph_PDirNet_PDirNet) TSnap::ConvertSubGraph <PDirNet, PDirNet>;
%template(ConvertSubGraph_PDirNet_PNEANet) TSnap::ConvertSubGraph <PDirNet, PNEANet>;
%template(ConvertESubGraph_PDirNet_PNEANet) TSnap::ConvertESubGraph <PDirNet, PNEANet>;
%template(GetSubGraph_PDirNet) TSnap::GetSubGraph<PDirNet>;
%template(GetRndSubGraph_PDirNet) TSnap::GetRndSubGraph<PDirNet>;
%template(GetRndESubGraph_PDirNet) TSnap::GetRndESubGraph<PDirNet>;


// triad.h - PDirNet
%template(GetClustCf_PDirNet) TSnap::GetClustCf<PDirNet>;
%template(GetNodeClustCf_PDirNet) TSnap::GetNodeClustCf<PDirNet>;
%template(GetTriads_PDirNet) TSnap::GetTriads<PDirNet>;
%template(GetTriadEdges_PDirNet) TSnap::GetTriadEdges<PDirNet>;
%template(GetNodeTriads_PDirNet) TSnap::GetNodeTriads<PDirNet>;
%template(GetTriadParticip_PDirNet) TSnap::GetTriadParticip<PDirNet>;
%template(GetTriangleCnt_PDirNet) TSnap::GetTriangleCnt<PDirNet>;

%template(GetCmnNbrs_PDirNet) TSnap::GetCmnNbrs<PDirNet>;
//%template(GetLen2Paths_PDirNet) TSnap::GetLen2Paths<PDirNet>;


// cmty.h - PDirNet
%template(GetModularity_PDirNet) TSnap::GetModularity<PDirNet>;
%template(GetEdgesInOut_PDirNet) TSnap::GetEdgesInOut<PDirNet>;


// anf.h - PDirNet
%template(GetAnf_PDirNet) TSnap::GetAnf<PDirNet>;
%template(GetAnfEffDiam_PDirNet) TSnap::GetAnfEffDiam<PDirNet>;
%template(TestAnf_PDirNet) TSnap::TestAnf<PDirNet>;

// statplot.h - PDirNet
%template(PlotKCoreEdges_PDirNet) TSnap::PlotKCoreEdges<PDirNet>;
%template(PlotKCoreNodes_PDirNet) TSnap::PlotKCoreNodes<PDirNet>;
%template(PlotShortPathDistr_PDirNet) TSnap::PlotShortPathDistr<PDirNet>;
%template(PlotHops_PDirNet) TSnap::PlotHops<PDirNet>;
%template(PlotClustCf_PDirNet) TSnap::PlotClustCf<PDirNet>;
%template(PlotSccDistr_PDirNet) TSnap::PlotSccDistr<PDirNet>;
%template(PlotWccDistr_PDirNet) TSnap::PlotWccDistr<PDirNet>;
%template(PlotOutDegDistr_PDirNet) TSnap::PlotOutDegDistr<PDirNet>;
%template(PlotInDegDistr_PDirNet) TSnap::PlotInDegDistr<PDirNet>;


// goodgraph.cpp - PDirNet
%template(PercentDegree_PDirNet) PercentDegree<PDirNet>;
%template(NodesGTEDegree_PDirNet) NodesGTEDegree<PDirNet>;
%template(MxDegree_PDirNet) MxDegree<PDirNet>;
%template(PercentMxWcc_PDirNet) PercentMxWcc<PDirNet>;
%template(PercentMxScc_PDirNet) PercentMxScc<PDirNet>;

// conv.h - PDirNet
%template(ToGraph_PDirNet) TSnap::ToGraph<PDirNet>;
