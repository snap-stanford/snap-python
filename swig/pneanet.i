// pneanet.i
// Templates for SNAP Ringo
//

/*
  Instanstiates templates from SNAP for inclusion in RINGO.
  Note in Vim, this replaces SNAP Template headers:
 
 :%s#^template.*<class PGraph> \S* \([^(]*\).*#%template(\1) TSnap::\1<PNEANet>;#gc
 :%s#^///.*\n:##g
*/

%extend TNEANet {
        TNEANetNodeI BegNI() {
          return TNEANetNodeI($self->BegNI());
        }
        TNEANetNodeI EndNI() {
          return TNEANetNodeI($self->EndNI());
        }
  
        TNEANetEdgeI BegEI() {
          return TNEANetEdgeI($self->BegEI());
        }
        TNEANetEdgeI EndEI() {
          return TNEANetEdgeI($self->EndEI());
        }
  
        TNEANetAIntI BegNAIntI(const TStr& attr) {
          return TNEANetAIntI($self->BegNAIntI(attr));
        }
        TNEANetAIntI EndNAIntI(const TStr& attr) {
          return TNEANetAIntI($self->EndNAIntI(attr));
        }
  
        TNEANetAStrI BegNAStrI(const TStr& attr) {
          return TNEANetAStrI($self->BegNAStrI(attr));
        }
        TNEANetAStrI EndNAStrI(const TStr& attr) {
          return TNEANetAStrI($self->EndNAStrI(attr));
        }
  
        TNEANetAFltI BegNAFltI(const TStr& attr) {
          return TNEANetAFltI($self->BegNAFltI(attr));
        }
        TNEANetAFltI EndNAFltI(const TStr& attr) {
          return TNEANetAFltI($self->EndNAFltI(attr));
        }
  
        TNEANetAIntI BegEAIntI(const TStr& attr) {
          return TNEANetAIntI($self->BegEAIntI(attr));
        }
        TNEANetAIntI EndEAIntI(const TStr& attr) {
          return TNEANetAIntI($self->EndEAIntI(attr));
        }
        
        TNEANetAStrI BegEAStrI(const TStr& attr) {
          return TNEANetAStrI($self->BegEAStrI(attr));
        }
        TNEANetAStrI EndEAStrI(const TStr& attr) {
          return TNEANetAStrI($self->EndEAStrI(attr));
        }
        
        TNEANetAFltI BegEAFltI(const TStr& attr) {
          return TNEANetAFltI($self->BegEAFltI(attr));
        }
        TNEANetAFltI EndEAFltI(const TStr& attr) {
          return TNEANetAFltI($self->EndEAFltI(attr));
        }
  
};

// Convert a directed graph to a multi-edge attribute graph
//%template(ConvertGraphToPNEANet) ConvertGraph<PNEANet, PNGraph>;

// Use PNEANet as default function name.
%template(PercentDegree) PercentDegree<PNEANet>;
%template(PercentMxWcc) PercentMxWcc<PNEANet>;
%template(PercentMxScc) PercentMxScc<PNEANet>;

%template(LoadEdgeList) TSnap::LoadEdgeList<PNEANet>;
%template(PrintGraphStatTable) PrintGraphStatTable<PNEANet>;
%template(GenRndGnm) TSnap::GenRndGnm<PNEANet>;

%template(NodesGTEDegree) NodesGTEDegree<PNEANet>;
%template(MxDegree) MxDegree<PNEANet>;
%template(MxSccSz) TSnap::GetMxScc<PNEANet>;
%template(MxWccSz) TSnap::GetMxWccSz<PNEANet>;
%template(MxDegree) MxDegree<PNEANet>;
// End Basic Directed Graphs


// Basic PNEANets
%template(PNEANet) TPt< TNEANet >;
%template(GenRndGnm) TSnap::GenRndGnm<PNEANet>;
%template(NodesGTEDegree) NodesGTEDegree<PNEANet>;
%template(MxDegree) MxDegree<PNEANet>;


// cncom.h - PNEANet
%template(GetNodeWcc) TSnap::GetNodeWcc<PNEANet>;
%template(IsConnected) TSnap::IsConnected<PNEANet>;
%template(IsWeaklyConn) TSnap::IsWeaklyConn<PNEANet>;
%template(GetWccSzCnt) TSnap::GetWccSzCnt<PNEANet>;
%template(GetWccs) TSnap::GetWccs<PNEANet>;
%template(GetSccSzCnt) TSnap::GetSccSzCnt<PNEANet>;
%template(GetSccs) TSnap::GetSccs<PNEANet>;
%template(GetMxWccSz) TSnap::GetMxWccSz<PNEANet>;

%template(GetMxWcc) TSnap::GetMxWcc<PNEANet>;
%template(GetMxScc) TSnap::GetMxScc<PNEANet>;
%template(GetMxBiCon) TSnap::GetMxBiCon<PNEANet>;


// alg.h - PNEANet
%template(CntInDegNodes) TSnap::CntInDegNodes<PNEANet>;
%template(CntOutDegNodes) TSnap::CntOutDegNodes<PNEANet>;
%template(CntDegNodes) TSnap::CntDegNodes<PNEANet>;
%template(CntNonZNodes) TSnap::CntNonZNodes<PNEANet>;
%template(CntEdgesToSet) TSnap::CntEdgesToSet<PNEANet>;

%template(GetMxDegNId) TSnap::GetMxDegNId<PNEANet>;
%template(GetMxInDegNId) TSnap::GetMxInDegNId<PNEANet>;
%template(GetMxOutDegNId) TSnap::GetMxOutDegNId<PNEANet>;

%template(GetInDegCnt) TSnap::GetInDegCnt<PNEANet>;
%template(GetOutDegCnt) TSnap::GetOutDegCnt<PNEANet>;
%template(GetDegCnt) TSnap::GetDegCnt<PNEANet>;
%template(GetDegSeqV) TSnap::GetDegSeqV<PNEANet>;

%template(GetNodeInDegV) TSnap::GetNodeInDegV<PNEANet>;
%template(GetNodeOutDegV) TSnap::GetNodeOutDegV<PNEANet>;

%template(CntUniqUndirEdges) TSnap::CntUniqUndirEdges<PNEANet>;
%template(CntUniqDirEdges) TSnap::CntUniqDirEdges<PNEANet>;
%template(CntUniqBiDirEdges) TSnap::CntUniqBiDirEdges<PNEANet>;
%template(CntSelfEdges) TSnap::CntSelfEdges<PNEANet>;


// bfsdfs.h - PNEANet
%template(GetBfsTree) TSnap::GetBfsTree<PNEANet>;
%template(GetSubTreeSz) TSnap::GetSubTreeSz<PNEANet>;
%template(GetNodesAtHop) TSnap::GetNodesAtHop<PNEANet>;
%template(GetNodesAtHops) TSnap::GetNodesAtHops<PNEANet>;
// Shortest paths
%template(GetShortPath) TSnap::GetShortPath<PNEANet>;
// Diameter
%template(GetBfsFullDiam) TSnap::GetBfsFullDiam<PNEANet>;
%template(GetBfsEffDiam) TSnap::GetBfsEffDiam<PNEANet>;


// drawgviz.h
%template(DrawGViz) TSnap::DrawGViz<PNEANet>;

// triad.h - PNEANet
%template(GetClustCf) TSnap::GetClustCf<PNEANet>;
%template(GetNodeClustCf) TSnap::GetNodeClustCf<PNEANet>;

%template(GetTriads) TSnap::GetTriads<PNEANet>;
%template(GetTriadEdges) TSnap::GetTriadEdges<PNEANet>;
//%template(GetNodeTriads) TSnap::GetNodeTriads<PNEANet>;
%template(GetTriadParticip) TSnap::GetTriadParticip<PNEANet>;

%template(GetCmnNbrs) TSnap::GetCmnNbrs<PNEANet>;
//%template(GetLen2Paths) TSnap::GetLen2Paths<PNEANet>;


// cmty.h - PNEANet
%template(GetModularity) TSnap::GetModularity<PNEANet>;
%template(GetEdgesInOut) TSnap::GetEdgesInOut<PNEANet>;


// anf.h - PNEANet
%template(GetAnf) TSnap::GetAnf<PNEANet>;
%template(GetAnfEffDiam) TSnap::GetAnfEffDiam<PNEANet>;

