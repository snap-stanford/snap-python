// pgraph.i
// Templates for SNAP, common functions to graph, net types

%pythoncode %{

#
# dispatch table for instantiated polymorphic SNAP templates
#

def GetMxScc(tspec, *args):
    if type(tspec) == PNEANet : return GetMxScc_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetMxScc_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetMxScc_PNGraph(tspec, *args)
    return None
def GetMxBiCon(tspec, *args):
    if type(tspec) == PNEANet : return GetMxBiCon_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetMxBiCon_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetMxBiCon_PNGraph(tspec, *args)
    return None
def CntUniqDirEdges(tspec, *args):
    if type(tspec) == PNEANet : return CntUniqDirEdges_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return CntUniqDirEdges_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return CntUniqDirEdges_PNGraph(tspec, *args)
    return None
def MxSccSz(tspec, *args):
    if type(tspec) == PNEANet : return MxSccSz_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return MxSccSz_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return MxSccSz_PNGraph(tspec, *args)
    return None
def PercentMxScc(tspec, *args):
    if type(tspec) == PNEANet : return PercentMxScc_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return PercentMxScc_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return PercentMxScc_PNGraph(tspec, *args)
    return None
def GetAnfEffDiam(tspec, *args):
    if type(tspec) == PNEANet : return GetAnfEffDiam_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetAnfEffDiam_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetAnfEffDiam_PNGraph(tspec, *args)
    return None
def CntUniqBiDirEdges(tspec, *args):
    if type(tspec) == PNEANet : return CntUniqBiDirEdges_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return CntUniqBiDirEdges_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return CntUniqBiDirEdges_PNGraph(tspec, *args)
    return None
def CntOutDegNodes(tspec, *args):
    if type(tspec) == PNEANet : return CntOutDegNodes_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return CntOutDegNodes_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return CntOutDegNodes_PNGraph(tspec, *args)
    return None
def GetNodeWcc(tspec, *args):
    if type(tspec) == PNEANet : return GetNodeWcc_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetNodeWcc_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeWcc_PNGraph(tspec, *args)
    return None
def GetOutDegCnt(tspec, *args):
    if type(tspec) == PNEANet : return GetOutDegCnt_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetOutDegCnt_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetOutDegCnt_PNGraph(tspec, *args)
    return None
def CntEdgesToSet(tspec, *args):
    if type(tspec) == PNEANet : return CntEdgesToSet_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return CntEdgesToSet_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return CntEdgesToSet_PNGraph(tspec, *args)
    return None
def GenBaraHierar(tspec, *args):
    if tspec == PNEANet : return GenBaraHierar_PNEANet(*args)
    if tspec == PUNGraph: return GenBaraHierar_PUNGraph(*args)
    if tspec == PNGraph : return GenBaraHierar_PNGraph(*args)
    return None
def GetSccs(tspec, *args):
    if type(tspec) == PNEANet : return GetSccs_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetSccs_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetSccs_PNGraph(tspec, *args)
    return None
def PercentDegree(tspec, *args):
    if type(tspec) == PNEANet : return PercentDegree_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return PercentDegree_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return PercentDegree_PNGraph(tspec, *args)
    return None
def GetShortPath(tspec, *args):
    if type(tspec) == PNEANet : return GetShortPath_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetShortPath_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetShortPath_PNGraph(tspec, *args)
    return None
def GetSubTreeSz(tspec, *args):
    if type(tspec) == PNEANet : return GetSubTreeSz_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetSubTreeSz_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetSubTreeSz_PNGraph(tspec, *args)
    return None
def GetBfsEffDiam(tspec, *args):
    if type(tspec) == PNEANet : return GetBfsEffDiam_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetBfsEffDiam_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetBfsEffDiam_PNGraph(tspec, *args)
    return None
def IsWeaklyConn(tspec, *args):
    if type(tspec) == PNEANet : return IsWeaklyConn_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return IsWeaklyConn_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return IsWeaklyConn_PNGraph(tspec, *args)
    return None
def PercentMxWcc(tspec, *args):
    if type(tspec) == PNEANet : return PercentMxWcc_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return PercentMxWcc_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return PercentMxWcc_PNGraph(tspec, *args)
    return None
def GetMxInDegNId(tspec, *args):
    if type(tspec) == PNEANet : return GetMxInDegNId_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetMxInDegNId_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetMxInDegNId_PNGraph(tspec, *args)
    return None
def GetInDegCnt(tspec, *args):
    if type(tspec) == PNEANet : return GetInDegCnt_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetInDegCnt_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetInDegCnt_PNGraph(tspec, *args)
    return None
def GetSccSzCnt(tspec, *args):
    if type(tspec) == PNEANet : return GetSccSzCnt_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetSccSzCnt_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetSccSzCnt_PNGraph(tspec, *args)
    return None
def IsConnected(tspec, *args):
    if type(tspec) == PNEANet : return IsConnected_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return IsConnected_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return IsConnected_PNGraph(tspec, *args)
    return None
def MxWccSz(tspec, *args):
    if type(tspec) == PNEANet : return MxWccSz_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return MxWccSz_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return MxWccSz_PNGraph(tspec, *args)
    return None
def GetCmnNbrs(tspec, *args):
    if type(tspec) == PNEANet : return GetCmnNbrs_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetCmnNbrs_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetCmnNbrs_PNGraph(tspec, *args)
    return None
def GetNodeInDegV(tspec, *args):
    if type(tspec) == PNEANet : return GetNodeInDegV_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetNodeInDegV_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeInDegV_PNGraph(tspec, *args)
    return None
def GetTriadEdges(tspec, *args):
    if type(tspec) == PNEANet : return GetTriadEdges_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetTriadEdges_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetTriadEdges_PNGraph(tspec, *args)
    return None
def GetMxWccSz(tspec, *args):
    if type(tspec) == PNEANet : return GetMxWccSz_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetMxWccSz_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetMxWccSz_PNGraph(tspec, *args)
    return None
def GetMxOutDegNId(tspec, *args):
    if type(tspec) == PNEANet : return GetMxOutDegNId_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetMxOutDegNId_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetMxOutDegNId_PNGraph(tspec, *args)
    return None
def GetLen2Paths(tspec, *args):
    if type(tspec) == PNEANet : return GetLen2Paths_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetLen2Paths_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetLen2Paths_PNGraph(tspec, *args)
    return None
def GetEdgesInOut(tspec, *args):
    if type(tspec) == PNEANet : return GetEdgesInOut_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetEdgesInOut_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetEdgesInOut_PNGraph(tspec, *args)
    return None
def GetBfsTree(tspec, *args):
    if type(tspec) == PNEANet : return GetBfsTree_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetBfsTree_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetBfsTree_PNGraph(tspec, *args)
    return None
def GetNodeClustCf(tspec, *args):
    if type(tspec) == PNEANet : return GetNodeClustCf_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetNodeClustCf_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeClustCf_PNGraph(tspec, *args)
    return None
def GetBfsFullDiam(tspec, *args):
    if type(tspec) == PNEANet : return GetBfsFullDiam_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetBfsFullDiam_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetBfsFullDiam_PNGraph(tspec, *args)
    return None
def PrintGraphStatTable(tspec, *args):
    if type(tspec) == PNEANet : return PrintGraphStatTable_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return PrintGraphStatTable_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return PrintGraphStatTable_PNGraph(tspec, *args)
    return None
def GetDegSeqV(tspec, *args):
    if type(tspec) == PNEANet : return GetDegSeqV_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetDegSeqV_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetDegSeqV_PNGraph(tspec, *args)
    return None
def GetWccs(tspec, *args):
    if type(tspec) == PNEANet : return GetWccs_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetWccs_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetWccs_PNGraph(tspec, *args)
    return None
def GenStar(tspec, *args):
    if tspec == PNEANet : return GenStar_PNEANet(*args)
    if tspec == PUNGraph: return GenStar_PUNGraph(*args)
    if tspec == PNGraph : return GenStar_PNGraph(*args)
    return None
def GenTree(tspec, *args):
    if tspec == PNEANet : return GenTree_PNEANet(*args)
    if tspec == PUNGraph: return GenTree_PUNGraph(*args)
    if tspec == PNGraph : return GenTree_PNGraph(*args)
    return None
def NodesGTEDegree(tspec, *args):
    if type(tspec) == PNEANet : return NodesGTEDegree_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return NodesGTEDegree_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return NodesGTEDegree_PNGraph(tspec, *args)
    return None
def CntNonZNodes(tspec, *args):
    if type(tspec) == PNEANet : return CntNonZNodes_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return CntNonZNodes_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return CntNonZNodes_PNGraph(tspec, *args)
    return None
def GetClustCf(tspec, *args):
    if type(tspec) == PNEANet : return GetClustCf_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetClustCf_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetClustCf_PNGraph(tspec, *args)
    return None
def GetDegCnt(tspec, *args):
    if type(tspec) == PNEANet : return GetDegCnt_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetDegCnt_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetDegCnt_PNGraph(tspec, *args)
    return None
def LoadEdgeList(tspec, *args):
    if tspec == PNEANet : return LoadEdgeList_PNEANet(*args)
    if tspec == PUNGraph: return LoadEdgeList_PUNGraph(*args)
    if tspec == PNGraph : return LoadEdgeList_PNGraph(*args)
    return None
def GetNodesAtHops(tspec, *args):
    if type(tspec) == PNEANet : return GetNodesAtHops_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetNodesAtHops_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetNodesAtHops_PNGraph(tspec, *args)
    return None
def GetNodeOutDegV(tspec, *args):
    if type(tspec) == PNEANet : return GetNodeOutDegV_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetNodeOutDegV_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeOutDegV_PNGraph(tspec, *args)
    return None
def GetAnf(tspec, *args):
    if type(tspec) == PNEANet : return GetAnf_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetAnf_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetAnf_PNGraph(tspec, *args)
    return None
def CntSelfEdges(tspec, *args):
    if type(tspec) == PNEANet : return CntSelfEdges_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return CntSelfEdges_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return CntSelfEdges_PNGraph(tspec, *args)
    return None
def GenCircle(tspec, *args):
    if tspec == PNEANet : return GenCircle_PNEANet(*args)
    if tspec == PUNGraph: return GenCircle_PUNGraph(*args)
    if tspec == PNGraph : return GenCircle_PNGraph(*args)
    return None
def GetModularity(tspec, *args):
    if type(tspec) == PNEANet : return GetModularity_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetModularity_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetModularity_PNGraph(tspec, *args)
    return None
def GetNodeTriads(tspec, *args):
    if type(tspec) == PNEANet : return GetNodeTriads_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetNodeTriads_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeTriads_PNGraph(tspec, *args)
    return None
def DrawGViz(tspec, *args):
    if type(tspec) == PNEANet : return DrawGViz_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return DrawGViz_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return DrawGViz_PNGraph(tspec, *args)
    return None
def GenFull(tspec, *args):
    if tspec == PNEANet : return GenFull_PNEANet(*args)
    if tspec == PUNGraph: return GenFull_PUNGraph(*args)
    if tspec == PNGraph : return GenFull_PNGraph(*args)
    return None
def GenGrid(tspec, *args):
    if tspec == PNEANet : return GenGrid_PNEANet(*args)
    if tspec == PUNGraph: return GenGrid_PUNGraph(*args)
    if tspec == PNGraph : return GenGrid_PNGraph(*args)
    return None
def MxDegree(tspec, *args):
    if type(tspec) == PNEANet : return MxDegree_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return MxDegree_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return MxDegree_PNGraph(tspec, *args)
    return None
def CntUniqUndirEdges(tspec, *args):
    if type(tspec) == PNEANet : return CntUniqUndirEdges_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return CntUniqUndirEdges_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return CntUniqUndirEdges_PNGraph(tspec, *args)
    return None
def GetTriadParticip(tspec, *args):
    if type(tspec) == PNEANet : return GetTriadParticip_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetTriadParticip_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetTriadParticip_PNGraph(tspec, *args)
    return None
def GetMxDegNId(tspec, *args):
    if type(tspec) == PNEANet : return GetMxDegNId_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetMxDegNId_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetMxDegNId_PNGraph(tspec, *args)
    return None
def GetWccSzCnt(tspec, *args):
    if type(tspec) == PNEANet : return GetWccSzCnt_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetWccSzCnt_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetWccSzCnt_PNGraph(tspec, *args)
    return None
def GetTriads(tspec, *args):
    if type(tspec) == PNEANet : return GetTriads_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetTriads_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetTriads_PNGraph(tspec, *args)
    return None
def GetNodesAtHop(tspec, *args):
    if type(tspec) == PNEANet : return GetNodesAtHop_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetNodesAtHop_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetNodesAtHop_PNGraph(tspec, *args)
    return None
def CntDegNodes(tspec, *args):
    if type(tspec) == PNEANet : return CntDegNodes_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return CntDegNodes_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return CntDegNodes_PNGraph(tspec, *args)
    return None
def GenRndGnm(tspec, *args):
    if tspec == PNEANet : return GenRndGnm_PNEANet(*args)
    if tspec == PUNGraph: return GenRndGnm_PUNGraph(*args)
    if tspec == PNGraph : return GenRndGnm_PNGraph(*args)
    return None
def GetMxWcc(tspec, *args):
    if type(tspec) == PNEANet : return GetMxWcc_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return GetMxWcc_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return GetMxWcc_PNGraph(tspec, *args)
    return None
def CntInDegNodes(tspec, *args):
    if type(tspec) == PNEANet : return CntInDegNodes_PNEANet(tspec, *args)
    if type(tspec) == PUNGraph: return CntInDegNodes_PUNGraph(tspec, *args)
    if type(tspec) == PNGraph : return CntInDegNodes_PNGraph(tspec, *args)
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

