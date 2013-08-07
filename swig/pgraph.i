// pgraph.i
// Templates for SNAP, common functions to graph, net types

%pythoncode %{

#
# dispatch table for instantiated polymorphic SNAP templates
#

def GetMxScc(gtype, *args):
    if gtype == PNEANet : return GetMxScc_PNEANet(*args)
    if gtype == PUNGraph: return GetMxScc_PUNGraph(*args)
    if gtype == PNGraph : return GetMxScc_PNGraph(*args)
    return None
def GetMxBiCon(gtype, *args):
    if gtype == PNEANet : return GetMxBiCon_PNEANet(*args)
    if gtype == PUNGraph: return GetMxBiCon_PUNGraph(*args)
    if gtype == PNGraph : return GetMxBiCon_PNGraph(*args)
    return None
def CntUniqDirEdges(gtype, *args):
    if gtype == PNEANet : return CntUniqDirEdges_PNEANet(*args)
    if gtype == PUNGraph: return CntUniqDirEdges_PUNGraph(*args)
    if gtype == PNGraph : return CntUniqDirEdges_PNGraph(*args)
    return None
def MxSccSz(gtype, *args):
    if gtype == PNEANet : return MxSccSz_PNEANet(*args)
    if gtype == PUNGraph: return MxSccSz_PUNGraph(*args)
    if gtype == PNGraph : return MxSccSz_PNGraph(*args)
    return None
def PercentMxScc(gtype, *args):
    if gtype == PNEANet : return PercentMxScc_PNEANet(*args)
    if gtype == PUNGraph: return PercentMxScc_PUNGraph(*args)
    if gtype == PNGraph : return PercentMxScc_PNGraph(*args)
    return None
def GetAnfEffDiam(gtype, *args):
    if gtype == PNEANet : return GetAnfEffDiam_PNEANet(*args)
    if gtype == PUNGraph: return GetAnfEffDiam_PUNGraph(*args)
    if gtype == PNGraph : return GetAnfEffDiam_PNGraph(*args)
    return None
def CntUniqBiDirEdges(gtype, *args):
    if gtype == PNEANet : return CntUniqBiDirEdges_PNEANet(*args)
    if gtype == PUNGraph: return CntUniqBiDirEdges_PUNGraph(*args)
    if gtype == PNGraph : return CntUniqBiDirEdges_PNGraph(*args)
    return None
def CntOutDegNodes(gtype, *args):
    if gtype == PNEANet : return CntOutDegNodes_PNEANet(*args)
    if gtype == PUNGraph: return CntOutDegNodes_PUNGraph(*args)
    if gtype == PNGraph : return CntOutDegNodes_PNGraph(*args)
    return None
def GetNodeWcc(gtype, *args):
    if gtype == PNEANet : return GetNodeWcc_PNEANet(*args)
    if gtype == PUNGraph: return GetNodeWcc_PUNGraph(*args)
    if gtype == PNGraph : return GetNodeWcc_PNGraph(*args)
    return None
def GetOutDegCnt(gtype, *args):
    if gtype == PNEANet : return GetOutDegCnt_PNEANet(*args)
    if gtype == PUNGraph: return GetOutDegCnt_PUNGraph(*args)
    if gtype == PNGraph : return GetOutDegCnt_PNGraph(*args)
    return None
def CntEdgesToSet(gtype, *args):
    if gtype == PNEANet : return CntEdgesToSet_PNEANet(*args)
    if gtype == PUNGraph: return CntEdgesToSet_PUNGraph(*args)
    if gtype == PNGraph : return CntEdgesToSet_PNGraph(*args)
    return None
def GenBaraHierar(gtype, *args):
    if gtype == PNEANet : return GenBaraHierar_PNEANet(*args)
    if gtype == PUNGraph: return GenBaraHierar_PUNGraph(*args)
    if gtype == PNGraph : return GenBaraHierar_PNGraph(*args)
    return None
def GetSccs(gtype, *args):
    if gtype == PNEANet : return GetSccs_PNEANet(*args)
    if gtype == PUNGraph: return GetSccs_PUNGraph(*args)
    if gtype == PNGraph : return GetSccs_PNGraph(*args)
    return None
def PercentDegree(gtype, *args):
    if gtype == PNEANet : return PercentDegree_PNEANet(*args)
    if gtype == PUNGraph: return PercentDegree_PUNGraph(*args)
    if gtype == PNGraph : return PercentDegree_PNGraph(*args)
    return None
def GetShortPath(gtype, *args):
    if gtype == PNEANet : return GetShortPath_PNEANet(*args)
    if gtype == PUNGraph: return GetShortPath_PUNGraph(*args)
    if gtype == PNGraph : return GetShortPath_PNGraph(*args)
    return None
def GetSubTreeSz(gtype, *args):
    if gtype == PNEANet : return GetSubTreeSz_PNEANet(*args)
    if gtype == PUNGraph: return GetSubTreeSz_PUNGraph(*args)
    if gtype == PNGraph : return GetSubTreeSz_PNGraph(*args)
    return None
def GetBfsEffDiam(gtype, *args):
    if gtype == PNEANet : return GetBfsEffDiam_PNEANet(*args)
    if gtype == PUNGraph: return GetBfsEffDiam_PUNGraph(*args)
    if gtype == PNGraph : return GetBfsEffDiam_PNGraph(*args)
    return None
def IsWeaklyConn(gtype, *args):
    if gtype == PNEANet : return IsWeaklyConn_PNEANet(*args)
    if gtype == PUNGraph: return IsWeaklyConn_PUNGraph(*args)
    if gtype == PNGraph : return IsWeaklyConn_PNGraph(*args)
    return None
def PercentMxWcc(gtype, *args):
    if gtype == PNEANet : return PercentMxWcc_PNEANet(*args)
    if gtype == PUNGraph: return PercentMxWcc_PUNGraph(*args)
    if gtype == PNGraph : return PercentMxWcc_PNGraph(*args)
    return None
def GetMxInDegNId(gtype, *args):
    if gtype == PNEANet : return GetMxInDegNId_PNEANet(*args)
    if gtype == PUNGraph: return GetMxInDegNId_PUNGraph(*args)
    if gtype == PNGraph : return GetMxInDegNId_PNGraph(*args)
    return None
def GetInDegCnt(gtype, *args):
    if gtype == PNEANet : return GetInDegCnt_PNEANet(*args)
    if gtype == PUNGraph: return GetInDegCnt_PUNGraph(*args)
    if gtype == PNGraph : return GetInDegCnt_PNGraph(*args)
    return None
def GetSccSzCnt(gtype, *args):
    if gtype == PNEANet : return GetSccSzCnt_PNEANet(*args)
    if gtype == PUNGraph: return GetSccSzCnt_PUNGraph(*args)
    if gtype == PNGraph : return GetSccSzCnt_PNGraph(*args)
    return None
def IsConnected(gtype, *args):
    if gtype == PNEANet : return IsConnected_PNEANet(*args)
    if gtype == PUNGraph: return IsConnected_PUNGraph(*args)
    if gtype == PNGraph : return IsConnected_PNGraph(*args)
    return None
def MxWccSz(gtype, *args):
    if gtype == PNEANet : return MxWccSz_PNEANet(*args)
    if gtype == PUNGraph: return MxWccSz_PUNGraph(*args)
    if gtype == PNGraph : return MxWccSz_PNGraph(*args)
    return None
def GetCmnNbrs(gtype, *args):
    if gtype == PNEANet : return GetCmnNbrs_PNEANet(*args)
    if gtype == PUNGraph: return GetCmnNbrs_PUNGraph(*args)
    if gtype == PNGraph : return GetCmnNbrs_PNGraph(*args)
    return None
def GetNodeInDegV(gtype, *args):
    if gtype == PNEANet : return GetNodeInDegV_PNEANet(*args)
    if gtype == PUNGraph: return GetNodeInDegV_PUNGraph(*args)
    if gtype == PNGraph : return GetNodeInDegV_PNGraph(*args)
    return None
def GetTriadEdges(gtype, *args):
    if gtype == PNEANet : return GetTriadEdges_PNEANet(*args)
    if gtype == PUNGraph: return GetTriadEdges_PUNGraph(*args)
    if gtype == PNGraph : return GetTriadEdges_PNGraph(*args)
    return None
def GetMxWccSz(gtype, *args):
    if gtype == PNEANet : return GetMxWccSz_PNEANet(*args)
    if gtype == PUNGraph: return GetMxWccSz_PUNGraph(*args)
    if gtype == PNGraph : return GetMxWccSz_PNGraph(*args)
    return None
def GetMxOutDegNId(gtype, *args):
    if gtype == PNEANet : return GetMxOutDegNId_PNEANet(*args)
    if gtype == PUNGraph: return GetMxOutDegNId_PUNGraph(*args)
    if gtype == PNGraph : return GetMxOutDegNId_PNGraph(*args)
    return None
def GetLen2Paths(gtype, *args):
    if gtype == PNEANet : return GetLen2Paths_PNEANet(*args)
    if gtype == PUNGraph: return GetLen2Paths_PUNGraph(*args)
    if gtype == PNGraph : return GetLen2Paths_PNGraph(*args)
    return None
def GetEdgesInOut(gtype, *args):
    if gtype == PNEANet : return GetEdgesInOut_PNEANet(*args)
    if gtype == PUNGraph: return GetEdgesInOut_PUNGraph(*args)
    if gtype == PNGraph : return GetEdgesInOut_PNGraph(*args)
    return None
def GetBfsTree(gtype, *args):
    if gtype == PNEANet : return GetBfsTree_PNEANet(*args)
    if gtype == PUNGraph: return GetBfsTree_PUNGraph(*args)
    if gtype == PNGraph : return GetBfsTree_PNGraph(*args)
    return None
def GetNodeClustCf(gtype, *args):
    if gtype == PNEANet : return GetNodeClustCf_PNEANet(*args)
    if gtype == PUNGraph: return GetNodeClustCf_PUNGraph(*args)
    if gtype == PNGraph : return GetNodeClustCf_PNGraph(*args)
    return None
def GetBfsFullDiam(gtype, *args):
    if gtype == PNEANet : return GetBfsFullDiam_PNEANet(*args)
    if gtype == PUNGraph: return GetBfsFullDiam_PUNGraph(*args)
    if gtype == PNGraph : return GetBfsFullDiam_PNGraph(*args)
    return None
def PrintGraphStatTable(gtype, *args):
    if gtype == PNEANet : return PrintGraphStatTable_PNEANet(*args)
    if gtype == PUNGraph: return PrintGraphStatTable_PUNGraph(*args)
    if gtype == PNGraph : return PrintGraphStatTable_PNGraph(*args)
    return None
def GetDegSeqV(gtype, *args):
    if gtype == PNEANet : return GetDegSeqV_PNEANet(*args)
    if gtype == PUNGraph: return GetDegSeqV_PUNGraph(*args)
    if gtype == PNGraph : return GetDegSeqV_PNGraph(*args)
    return None
def GetWccs(gtype, *args):
    if gtype == PNEANet : return GetWccs_PNEANet(*args)
    if gtype == PUNGraph: return GetWccs_PUNGraph(*args)
    if gtype == PNGraph : return GetWccs_PNGraph(*args)
    return None
def GenStar(gtype, *args):
    if gtype == PNEANet : return GenStar_PNEANet(*args)
    if gtype == PUNGraph: return GenStar_PUNGraph(*args)
    if gtype == PNGraph : return GenStar_PNGraph(*args)
    return None
def GenTree(gtype, *args):
    if gtype == PNEANet : return GenTree_PNEANet(*args)
    if gtype == PUNGraph: return GenTree_PUNGraph(*args)
    if gtype == PNGraph : return GenTree_PNGraph(*args)
    return None
def NodesGTEDegree(gtype, *args):
    if gtype == PNEANet : return NodesGTEDegree_PNEANet(*args)
    if gtype == PUNGraph: return NodesGTEDegree_PUNGraph(*args)
    if gtype == PNGraph : return NodesGTEDegree_PNGraph(*args)
    return None
def CntNonZNodes(gtype, *args):
    if gtype == PNEANet : return CntNonZNodes_PNEANet(*args)
    if gtype == PUNGraph: return CntNonZNodes_PUNGraph(*args)
    if gtype == PNGraph : return CntNonZNodes_PNGraph(*args)
    return None
def GetClustCf(gtype, *args):
    if gtype == PNEANet : return GetClustCf_PNEANet(*args)
    if gtype == PUNGraph: return GetClustCf_PUNGraph(*args)
    if gtype == PNGraph : return GetClustCf_PNGraph(*args)
    return None
def GetDegCnt(gtype, *args):
    if gtype == PNEANet : return GetDegCnt_PNEANet(*args)
    if gtype == PUNGraph: return GetDegCnt_PUNGraph(*args)
    if gtype == PNGraph : return GetDegCnt_PNGraph(*args)
    return None
def LoadEdgeList(gtype, *args):
    if gtype == PNEANet : return LoadEdgeList_PNEANet(*args)
    if gtype == PUNGraph: return LoadEdgeList_PUNGraph(*args)
    if gtype == PNGraph : return LoadEdgeList_PNGraph(*args)
    return None
def GetNodesAtHops(gtype, *args):
    if gtype == PNEANet : return GetNodesAtHops_PNEANet(*args)
    if gtype == PUNGraph: return GetNodesAtHops_PUNGraph(*args)
    if gtype == PNGraph : return GetNodesAtHops_PNGraph(*args)
    return None
def GetNodeOutDegV(gtype, *args):
    if gtype == PNEANet : return GetNodeOutDegV_PNEANet(*args)
    if gtype == PUNGraph: return GetNodeOutDegV_PUNGraph(*args)
    if gtype == PNGraph : return GetNodeOutDegV_PNGraph(*args)
    return None
def GetAnf(gtype, *args):
    if gtype == PNEANet : return GetAnf_PNEANet(*args)
    if gtype == PUNGraph: return GetAnf_PUNGraph(*args)
    if gtype == PNGraph : return GetAnf_PNGraph(*args)
    return None
def CntSelfEdges(gtype, *args):
    if gtype == PNEANet : return CntSelfEdges_PNEANet(*args)
    if gtype == PUNGraph: return CntSelfEdges_PUNGraph(*args)
    if gtype == PNGraph : return CntSelfEdges_PNGraph(*args)
    return None
def GenCircle(gtype, *args):
    if gtype == PNEANet : return GenCircle_PNEANet(*args)
    if gtype == PUNGraph: return GenCircle_PUNGraph(*args)
    if gtype == PNGraph : return GenCircle_PNGraph(*args)
    return None
def GetModularity(gtype, *args):
    if gtype == PNEANet : return GetModularity_PNEANet(*args)
    if gtype == PUNGraph: return GetModularity_PUNGraph(*args)
    if gtype == PNGraph : return GetModularity_PNGraph(*args)
    return None
def GetNodeTriads(gtype, *args):
    if gtype == PNEANet : return GetNodeTriads_PNEANet(*args)
    if gtype == PUNGraph: return GetNodeTriads_PUNGraph(*args)
    if gtype == PNGraph : return GetNodeTriads_PNGraph(*args)
    return None
def DrawGViz(gtype, *args):
    if gtype == PNEANet : return DrawGViz_PNEANet(*args)
    if gtype == PUNGraph: return DrawGViz_PUNGraph(*args)
    if gtype == PNGraph : return DrawGViz_PNGraph(*args)
    return None
def GenFull(gtype, *args):
    if gtype == PNEANet : return GenFull_PNEANet(*args)
    if gtype == PUNGraph: return GenFull_PUNGraph(*args)
    if gtype == PNGraph : return GenFull_PNGraph(*args)
    return None
def GenGrid(gtype, *args):
    if gtype == PNEANet : return GenGrid_PNEANet(*args)
    if gtype == PUNGraph: return GenGrid_PUNGraph(*args)
    if gtype == PNGraph : return GenGrid_PNGraph(*args)
    return None
def MxDegree(gtype, *args):
    if gtype == PNEANet : return MxDegree_PNEANet(*args)
    if gtype == PUNGraph: return MxDegree_PUNGraph(*args)
    if gtype == PNGraph : return MxDegree_PNGraph(*args)
    return None
def CntUniqUndirEdges(gtype, *args):
    if gtype == PNEANet : return CntUniqUndirEdges_PNEANet(*args)
    if gtype == PUNGraph: return CntUniqUndirEdges_PUNGraph(*args)
    if gtype == PNGraph : return CntUniqUndirEdges_PNGraph(*args)
    return None
def GetTriadParticip(gtype, *args):
    if gtype == PNEANet : return GetTriadParticip_PNEANet(*args)
    if gtype == PUNGraph: return GetTriadParticip_PUNGraph(*args)
    if gtype == PNGraph : return GetTriadParticip_PNGraph(*args)
    return None
def GetMxDegNId(gtype, *args):
    if gtype == PNEANet : return GetMxDegNId_PNEANet(*args)
    if gtype == PUNGraph: return GetMxDegNId_PUNGraph(*args)
    if gtype == PNGraph : return GetMxDegNId_PNGraph(*args)
    return None
def GetWccSzCnt(gtype, *args):
    if gtype == PNEANet : return GetWccSzCnt_PNEANet(*args)
    if gtype == PUNGraph: return GetWccSzCnt_PUNGraph(*args)
    if gtype == PNGraph : return GetWccSzCnt_PNGraph(*args)
    return None
def GetTriads(gtype, *args):
    if gtype == PNEANet : return GetTriads_PNEANet(*args)
    if gtype == PUNGraph: return GetTriads_PUNGraph(*args)
    if gtype == PNGraph : return GetTriads_PNGraph(*args)
    return None
def GetNodesAtHop(gtype, *args):
    if gtype == PNEANet : return GetNodesAtHop_PNEANet(*args)
    if gtype == PUNGraph: return GetNodesAtHop_PUNGraph(*args)
    if gtype == PNGraph : return GetNodesAtHop_PNGraph(*args)
    return None
def CntDegNodes(gtype, *args):
    if gtype == PNEANet : return CntDegNodes_PNEANet(*args)
    if gtype == PUNGraph: return CntDegNodes_PUNGraph(*args)
    if gtype == PNGraph : return CntDegNodes_PNGraph(*args)
    return None
def GenRndGnm(gtype, *args):
    if gtype == PNEANet : return GenRndGnm_PNEANet(*args)
    if gtype == PUNGraph: return GenRndGnm_PUNGraph(*args)
    if gtype == PNGraph : return GenRndGnm_PNGraph(*args)
    return None
def GetMxWcc(gtype, *args):
    if gtype == PNEANet : return GetMxWcc_PNEANet(*args)
    if gtype == PUNGraph: return GetMxWcc_PUNGraph(*args)
    if gtype == PNGraph : return GetMxWcc_PNGraph(*args)
    return None
def CntInDegNodes(gtype, *args):
    if gtype == PNEANet : return CntInDegNodes_PNEANet(*args)
    if gtype == PUNGraph: return CntInDegNodes_PUNGraph(*args)
    if gtype == PNGraph : return CntInDegNodes_PNGraph(*args)
    return None

#
# generators for nodes and edges
#

def Nodes(self):
    NI = self.BegNI()
    while NI < self.EndNI():
        yield NI
        NI.Next()

def Edges(self):
    EI = self.BegEI()
    while EI < self.EndEI():
        yield EI
        EI.Next()

#
# redefine some methods to use T... class not P... class
#

def Clr(self):
    self().Clr()

def Empty(self):
    return self().Empty()

def Save(self,*args):
    self().Save(*args)

#
# define generator and redirection methods
#

PNEANet.Nodes = Nodes
PNEANet.Edges = Edges
PNEANet.Clr = Clr
PNEANet.Empty = Empty
PNEANet.Save = Save

PUNGraph.Nodes = Nodes
PUNGraph.Edges = Edges
PUNGraph.Clr = Clr
PUNGraph.Empty = Empty
PUNGraph.Save = Save

PNGraph.Nodes = Nodes
PNGraph.Edges = Edges
PNGraph.Clr = Clr
PNGraph.Empty = Empty
PNGraph.Save = Save

%}

