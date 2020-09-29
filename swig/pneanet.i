// pneanet.i
// Templates for SNAP TNEANet, PNEANet
//

/*
  Instantiates templates from SNAP for inclusion in RINGO.
  Note in Vim, this replaces SNAP Template headers:
 
 :%s#^template.*<class PGraph> \S* \([^(]*\).*#%template(\1) TSnap::\1<PNEANet>;#gc
 :%s#^///.*\n:##g
*/

%extend TNEANet {
        // node iterator
        TNEANetNodeI BegNI() {
          return TNEANetNodeI($self->BegNI());
        }
        TNEANetNodeI EndNI() {
          return TNEANetNodeI($self->EndNI());
        }
        TNEANetNodeI GetNI(const int &NId) {
          return TNEANetNodeI($self->GetNI(NId));
        }

        // add node attribute value
        int AddIntAttrDatN(const TNEANetNodeI& NI, const TInt& Value, const TStr& Attr) {
          return $self->AddIntAttrDatN(NI.GetNI(), Value, Attr);
        }
        int AddFltAttrDatN(const TNEANetNodeI& NI, const TFlt& Value, const TStr& Attr) {
          return $self->AddFltAttrDatN(NI.GetNI(), Value, Attr);
        }
        int AddStrAttrDatN(const TNEANetNodeI& NI, const TStr& Value, const TStr& Attr) {
          return $self->AddStrAttrDatN(NI.GetNI(), Value, Attr);
        }

        // get node attribute value
        TInt GetIntAttrDatN(const TNEANetNodeI& NI, const TStr& Attr) {
          return $self->GetIntAttrDatN(NI.GetNI(), Attr);
        }
        TFlt GetFltAttrDatN(const TNEANetNodeI& NI, const TStr& Attr) {
          return $self->GetFltAttrDatN(NI.GetNI(), Attr);
        }
        TStr GetStrAttrDatN(const TNEANetNodeI& NI, const TStr& Attr) {
          return $self->GetStrAttrDatN(NI.GetNI(), Attr);
        }

        // get node attribute value by index
        TInt GetIntAttrIndDatN(const TNEANetNodeI& NI, const int& index) {
          return $self->GetIntAttrIndDatN(NI.GetNI(), index);
        }
        TFlt GetFltAttrIndDatN(const TNEANetNodeI& NI, const int& index) {
          return $self->GetFltAttrIndDatN(NI.GetNI(), index);
        }
        TStr GetStrAttrIndDatN(const TNEANetNodeI& NI, const int& index) {
          return $self->GetStrAttrIndDatN(NI.GetNI(), index);
        }

        // delete node attribute value
        int DelAttrDatN(const TNEANetNodeI& NI, const TStr& Attr) {
          return $self->DelAttrDatN(NI.GetNI(), Attr);
        }
  
        // edge iterator
        TNEANetEdgeI BegEI() {
          return TNEANetEdgeI($self->BegEI());
        }
        TNEANetEdgeI EndEI() {
          return TNEANetEdgeI($self->EndEI());
        }
        TNEANetEdgeI GetEI(const int &EId) {
          return TNEANetEdgeI($self->GetEI(EId));
        }
        TNEANetEdgeI GetEI(const int &SrcNId, const int &DstNId) {
          return TNEANetEdgeI($self->GetEI(SrcNId, DstNId));
        }

        // add edge attributes value
        int AddIntAttrDatE(const TNEANetEdgeI& EI, const TInt& Value, const TStr& Attr) {
          return $self->AddIntAttrDatE(EI.GetEI(), Value, Attr);
        }
        int AddFltAttrDatE(const TNEANetEdgeI& EI, const TFlt& Value, const TStr& Attr) {
          return $self->AddFltAttrDatE(EI.GetEI(), Value, Attr);
        }
        int AddStrAttrDatE(const TNEANetEdgeI& EI, const TStr& Value, const TStr& Attr) {
          return $self->AddStrAttrDatE(EI.GetEI(), Value, Attr);
        }

        // get edge attribute value
        TInt GetIntAttrDatE(const TNEANetEdgeI& EI, const TStr& Attr) {
          return $self->GetIntAttrDatE(EI.GetEI(), Attr);
        }
        TFlt GetFltAttrDatE(const TNEANetEdgeI& EI, const TStr& Attr) {
          return $self->GetFltAttrDatE(EI.GetEI(), Attr);
        }
        TStr GetStrAttrDatE(const TNEANetEdgeI& EI, const TStr& Attr) {
          return $self->GetStrAttrDatE(EI.GetEI(), Attr);
        }

        // get edge attribute value by index
        TInt GetIntAttrIndDatE(const TNEANetEdgeI& EI, const int& index) {
          return $self->GetIntAttrIndDatE(EI.GetEI(), index);
        }
        TFlt GetFltAttrIndDatE(const TNEANetEdgeI& EI, const int& index) {
          return $self->GetFltAttrIndDatE(EI.GetEI(), index);
        }
        TStr GetStrAttrIndDatE(const TNEANetEdgeI& EI, const int& index) {
          return $self->GetStrAttrIndDatE(EI.GetEI(), index);
        }

        // delete edge attribute value
        int DelAttrDatE(const TNEANetEdgeI& EI, const TStr& Attr) {
          return $self->DelAttrDatE(EI.GetEI(), Attr);
        }
  
        TNEANetAIntI BegNAIntI(const TStr& Attr) {
          return TNEANetAIntI($self->BegNAIntI(Attr));
        }
        TNEANetAIntI EndNAIntI(const TStr& Attr) {
          return TNEANetAIntI($self->EndNAIntI(Attr));
        }
  
        TNEANetAStrI BegNAStrI(const TStr& Attr) {
          return TNEANetAStrI($self->BegNAStrI(Attr));
        }
        TNEANetAStrI EndNAStrI(const TStr& Attr) {
          return TNEANetAStrI($self->EndNAStrI(Attr));
        }
  
        TNEANetAFltI BegNAFltI(const TStr& Attr) {
          return TNEANetAFltI($self->BegNAFltI(Attr));
        }
        TNEANetAFltI EndNAFltI(const TStr& Attr) {
          return TNEANetAFltI($self->EndNAFltI(Attr));
        }
  
        TNEANetAIntI BegEAIntI(const TStr& Attr) {
          return TNEANetAIntI($self->BegEAIntI(Attr));
        }
        TNEANetAIntI EndEAIntI(const TStr& Attr) {
          return TNEANetAIntI($self->EndEAIntI(Attr));
        }
        
        TNEANetAStrI BegEAStrI(const TStr& Attr) {
          return TNEANetAStrI($self->BegEAStrI(Attr));
        }
        TNEANetAStrI EndEAStrI(const TStr& Attr) {
          return TNEANetAStrI($self->EndEAStrI(Attr));
        }
        
        TNEANetAFltI BegEAFltI(const TStr& Attr) {
          return TNEANetAFltI($self->BegEAFltI(Attr));
        }
        TNEANetAFltI EndEAFltI(const TStr& Attr) {
          return TNEANetAFltI($self->EndEAFltI(Attr));
        }
  
};


// Convert a directed graph to a multi-edge attribute graph
//%template(ConvertGraphToPNEANet) ConvertGraph<PNEANet, PNGraph>;

// Use PNEANet as default function name.

%template(PrintGraphStatTable_PNEANet) PrintGraphStatTable<PNEANet>;

//%template(MxSccSz_PNEANet) TSnap::GetMxScc<PNEANet>;
//%template(MxWccSz_PNEANet) TSnap::GetMxWccSz<PNEANet>;
// End Basic Directed Graphs


// Basic PNEANets
%template(PNEANet) TPt< TNEANet >;


// gbase.h - PNEANet
%template(PrintInfo_PNEANet) TSnap::PrintInfo<PNEANet>;

// cncom.h - PNEANet
%template(GetNodeWcc_PNEANet) TSnap::GetNodeWcc<PNEANet>;
%template(IsConnected_PNEANet) TSnap::IsConnected<PNEANet>;
%template(IsWeaklyConn_PNEANet) TSnap::IsWeaklyConn<PNEANet>;
%template(GetWccSzCnt_PNEANet) TSnap::GetWccSzCnt<PNEANet>;
%template(GetWccs_PNEANet) TSnap::GetWccs<PNEANet>;
%template(GetSccSzCnt_PNEANet) TSnap::GetSccSzCnt<PNEANet>;
%template(GetSccs_PNEANet) TSnap::GetSccs<PNEANet>;
%template(GetMxWccSz_PNEANet) TSnap::GetMxWccSz<PNEANet>;
%template(GetMxSccSz_PNEANet) TSnap::GetMxSccSz<PNEANet>;

%template(GetMxWcc_PNEANet) TSnap::GetMxWcc<PNEANet>;
%template(GetMxScc_PNEANet) TSnap::GetMxScc<PNEANet>;
%template(GetMxBiCon_PNEANet) TSnap::GetMxBiCon<PNEANet>;

// centr.h - PNEANet
%template(GetNodeEcc_PNEANet) TSnap::GetNodeEcc<PNEANet>;
%template(GetPageRank_PNEANet) TSnap::GetPageRank<PNEANet>;
%template(GetPageRank_v1_PNEANet) TSnap::GetPageRank_v1<PNEANet>;
%template(GetHits_PNEANet) TSnap::GetHits<PNEANet>;
%template(GetBetweennessCentr_PNEANet) TSnap::GetBetweennessCentr<PNEANet>;
%template(GetClosenessCentr_PNEANet) TSnap::GetClosenessCentr<PNEANet>;
%template(GetFarnessCentr_PNEANet) TSnap::GetFarnessCentr<PNEANet>;
#ifdef _OPENMP
%template(GetPageRankMP_PNEANet) TSnap::GetPageRankMP<PNEANet>;
%template(GetHitsMP_PNEANet) TSnap::GetHitsMP<PNEANet>;
#endif


// alg.h - PNEANet
%template(CntInDegNodes_PNEANet) TSnap::CntInDegNodes<PNEANet>;
%template(CntOutDegNodes_PNEANet) TSnap::CntOutDegNodes<PNEANet>;
%template(CntDegNodes_PNEANet) TSnap::CntDegNodes<PNEANet>;
%template(CntNonZNodes_PNEANet) TSnap::CntNonZNodes<PNEANet>;
%template(CntEdgesToSet_PNEANet) TSnap::CntEdgesToSet<PNEANet>;

%template(GetMxDegNId_PNEANet) TSnap::GetMxDegNId<PNEANet>;
%template(GetMxInDegNId_PNEANet) TSnap::GetMxInDegNId<PNEANet>;
%template(GetMxOutDegNId_PNEANet) TSnap::GetMxOutDegNId<PNEANet>;

%template(GetInDegCnt_PNEANet) TSnap::GetInDegCnt<PNEANet>;
%template(GetOutDegCnt_PNEANet) TSnap::GetOutDegCnt<PNEANet>;
%template(GetDegCnt_PNEANet) TSnap::GetDegCnt<PNEANet>;
%template(GetDegSeqV_PNEANet) TSnap::GetDegSeqV<PNEANet>;

%template(GetNodeInDegV_PNEANet) TSnap::GetNodeInDegV<PNEANet>;
%template(GetNodeOutDegV_PNEANet) TSnap::GetNodeOutDegV<PNEANet>;

%template(CntUniqUndirEdges_PNEANet) TSnap::CntUniqUndirEdges<PNEANet>;
%template(CntUniqDirEdges_PNEANet) TSnap::CntUniqDirEdges<PNEANet>;
%template(CntUniqBiDirEdges_PNEANet) TSnap::CntUniqBiDirEdges<PNEANet>;
%template(CntSelfEdges_PNEANet) TSnap::CntSelfEdges<PNEANet>;

%template(GetUnDir_PNEANet) TSnap::GetUnDir<PNEANet>;
%template(MakeUnDir_PNEANet) TSnap::MakeUnDir<PNEANet>;
%template(AddSelfEdges_PNEANet) TSnap::AddSelfEdges<PNEANet>;
%template(DelSelfEdges_PNEANet) TSnap::DelSelfEdges<PNEANet>;
%template(DelNodes_PNEANet) TSnap::DelNodes<PNEANet>;
%template(DelZeroDegNodes_PNEANet) TSnap::DelZeroDegNodes<PNEANet>;
%template(DelDegKNodes_PNEANet) TSnap::DelDegKNodes<PNEANet>;
%template(IsTree_PNEANet) TSnap::IsTree<PNEANet>;
%template(GetTreeRootNId_PNEANet) TSnap::GetTreeRootNId<PNEANet>;
%template(GetTreeSig_PNEANet) TSnap::GetTreeSig<PNEANet>;


// bfsdfs.h - PNEANet
%template(GetBfsTree_PNEANet) TSnap::GetBfsTree<PNEANet>;
%template(GetSubTreeSz_PNEANet) TSnap::GetSubTreeSz<PNEANet>;
%template(GetNodesAtHop_PNEANet) TSnap::GetNodesAtHop<PNEANet>;
%template(GetNodesAtHops_PNEANet) TSnap::GetNodesAtHops<PNEANet>;
// Shortest paths
%template(GetShortPath_PNEANet) TSnap::GetShortPath<PNEANet>;
// Diameter
%template(GetBfsFullDiam_PNEANet) TSnap::GetBfsFullDiam<PNEANet>;
%template(GetBfsEffDiam_PNEANet) TSnap::GetBfsEffDiam<PNEANet>;
%template(GetBfsEffDiamAll_PNEANet) TSnap::GetBfsEffDiamAll<PNEANet>;


// drawgviz.h
%template(DrawGViz_PNEANet) TSnap::DrawGViz<PNEANet>;


// ggen.h
%template(GenGrid_PNEANet) TSnap::GenGrid<PNEANet>;
%template(GenStar_PNEANet) TSnap::GenStar<PNEANet>;
%template(GenCircle_PNEANet) TSnap::GenCircle<PNEANet>;
%template(GenFull_PNEANet) TSnap::GenFull<PNEANet>;
%template(GenTree_PNEANet) TSnap::GenTree<PNEANet>;
%template(GenBaraHierar_PNEANet) TSnap::GenBaraHierar<PNEANet>;
%template(GenRndGnm_PNEANet) TSnap::GenRndGnm<PNEANet>;


// gio.h
%template(LoadEdgeList_PNEANet) TSnap::LoadEdgeList<PNEANet>;
%template(LoadEdgeListStr_PNEANet) TSnap::LoadEdgeListStr<PNEANet>;
%template(LoadConnList_PNEANet) TSnap::LoadConnList<PNEANet>;
%template(LoadConnListStr_PNEANet) TSnap::LoadConnListStr<PNEANet>;
%template(LoadPajek_PNEANet) TSnap::LoadPajek<PNEANet>;
%template(SaveEdgeList_PNEANet) TSnap::SaveEdgeList<PNEANet>;
%template(SavePajek_PNEANet) TSnap::SavePajek<PNEANet>;
%template(SaveMatlabSparseMtx_PNEANet) TSnap::SaveMatlabSparseMtx<PNEANet>;
%template(SaveGViz_PNEANet) TSnap::SaveGViz<PNEANet>;


// kcore.h
%template(GetKCore_PNEANet) TSnap::GetKCore<PNEANet>;
%template(GetKCoreEdges_PNEANet) TSnap::GetKCoreEdges<PNEANet>;
%template(GetKCoreNodes_PNEANet) TSnap::GetKCoreNodes<PNEANet>;


// subgraph.h
%template(ConvertGraph_PNEANet_PNEANet) TSnap::ConvertGraph <PNEANet, PNEANet>;
%template(ConvertGraph_PNEANet_PNGraph) TSnap::ConvertGraph <PNEANet, PNGraph>;
%template(ConvertGraph_PNEANet_PUNGraph) TSnap::ConvertGraph <PNEANet, PUNGraph>;
%template(ConvertSubGraph_PNEANet_PNEANet) TSnap::ConvertSubGraph <PNEANet, PNEANet>;
%template(ConvertSubGraph_PNEANet_PNGraph) TSnap::ConvertSubGraph <PNEANet, PNGraph>;
%template(ConvertSubGraph_PNEANet_PUNGraph) TSnap::ConvertSubGraph <PNEANet, PUNGraph>;
%template(ConvertESubGraph_PNEANet_PNEANet) TSnap::ConvertESubGraph <PNEANet, PNEANet>;
%template(GetSubGraph_PNEANet) TSnap::GetSubGraph<PNEANet>;
%template(GetESubGraph_PNEANet) TSnap::GetESubGraph<PNEANet>;
%template(GetRndSubGraph_PNEANet) TSnap::GetRndSubGraph<PNEANet>;
%template(GetRndESubGraph_PNEANet) TSnap::GetRndESubGraph<PNEANet>;
%template(GetEgonetHop_PNEANet) TSnap::GetEgonetHop<PNEANet>;
%template(GetInEgonetHop_PNEANet) TSnap::GetInEgonetHop<PNEANet>;
%template(GetOutEgonetHop_PNEANet) TSnap::GetOutEgonetHop<PNEANet>;
%template(GetInEgonetSub_PNEANet) TSnap::GetInEgonetSub<PNEANet>;



// triad.h - PNEANet
%template(GetClustCf_PNEANet) TSnap::GetClustCf<PNEANet>;
%template(GetClustCfAll_PNEANet) TSnap::GetClustCfAll<PNEANet>;
%template(GetNodeClustCf_PNEANet) TSnap::GetNodeClustCf<PNEANet>;
%template(GetTriads_PNEANet) TSnap::GetTriads<PNEANet>;
%template(GetTriadsAll_PNEANet) TSnap::GetTriadsAll<PNEANet>;
%template(GetTriadEdges_PNEANet) TSnap::GetTriadEdges<PNEANet>;
%template(GetNodeTriads_PNEANet) TSnap::GetNodeTriads<PNEANet>;
%template(GetNodeTriadsAll_PNEANet) TSnap::GetNodeTriadsAll<PNEANet>;
%template(GetTriadParticip_PNEANet) TSnap::GetTriadParticip<PNEANet>;
%template(GetTriangleCnt_PNEANet) TSnap::GetTriangleCnt<PNEANet>;

%template(GetCmnNbrs_PNEANet) TSnap::GetCmnNbrs<PNEANet>;
%template(GetLen2Paths_PNEANet) TSnap::GetLen2Paths<PNEANet>;


// cmty.h - PNEANet
%template(GetModularity_PNEANet) TSnap::GetModularity<PNEANet>;
%template(GetEdgesInOut_PNEANet) TSnap::GetEdgesInOut<PNEANet>;


// anf.h - PNEANet
%template(GetAnf_PNEANet) TSnap::GetAnf<PNEANet>;
%template(GetAnfEffDiam_PNEANet) TSnap::GetAnfEffDiam<PNEANet>;
%template(TestAnf_PNEANet) TSnap::TestAnf<PNEANet>;


// statplot.h - PNEANet
%template(PlotKCoreEdges_PNEANet) TSnap::PlotKCoreEdges<PNEANet>;
%template(PlotKCoreNodes_PNEANet) TSnap::PlotKCoreNodes<PNEANet>;
%template(PlotShortPathDistr_PNEANet) TSnap::PlotShortPathDistr<PNEANet>;
%template(PlotHops_PNEANet) TSnap::PlotHops<PNEANet>;
%template(PlotClustCf_PNEANet) TSnap::PlotClustCf<PNEANet>;
%template(PlotSccDistr_PNEANet) TSnap::PlotSccDistr<PNEANet>;
%template(PlotWccDistr_PNEANet) TSnap::PlotWccDistr<PNEANet>;
%template(PlotOutDegDistr_PNEANet) TSnap::PlotOutDegDistr<PNEANet>;
%template(PlotInDegDistr_PNEANet) TSnap::PlotInDegDistr<PNEANet>;


// goodgraph.cpp - PNEANet
%template(PercentDegree_PNEANet) PercentDegree<PNEANet>;
%template(NodesGTEDegree_PNEANet) NodesGTEDegree<PNEANet>;
%template(MxDegree_PNEANet) MxDegree<PNEANet>;
%template(PercentMxWcc_PNEANet) PercentMxWcc<PNEANet>;
%template(PercentMxScc_PNEANet) PercentMxScc<PNEANet>;

// conv.h - PNEANet
%template(ToNetwork_PNEANet) TSnap::ToNetwork<PNEANet>;

//%rename(ToNetwork_PNEANet) TSnap::ToNetwork<PNEANet>(PTable, const TStr &, const TStr &, TStrV  &, TAttrAggr);
//TSnap::ToNetwork<PNEANet>(PTable, const TStr &, const TStr &, TStrV  &, TAttrAggr);
//%rename(ToNetwork_PNEANet) TSnap::ToNetwork<PNEANet>(PTable, const TStr &, const TStr &, TAttrAggr);
//TSnap::ToNetwork<PNEANet>(PTable, const TStr &, const TStr &, TAttrAggr);
//%rename(ToNetwork_PNEANet) TSnap::ToNetwork<PNEANet>(PTable, const TStr &, const TStr &, TVec<TStr,int> &, TAttrAggr);
//TSnap::ToNetwork<PNEANet>(PTable, const TStr &, const TStr &, TVec<TStr,int> &, TAttrAggr);
//%rename(ToNetwork_PNEANet) TSnap::ToNetwork<PNEANet>(PTable, const TStr &, const TStr &, TVec<TStr,int> &, PTable, const TStr &, TVec<TStr,int> &, TAttrAggr);
//TSnap::ToNetwork<PNEANet>(PTable, const TStr &, const TStr &, TVec<TStr,int> &, PTable, const TStr &, TVec<TStr,int> &, TAttrAggr);

