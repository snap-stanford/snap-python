// pgraph.i
// Templates for SNAP, common functions to graph, net types

%pythoncode %{

#
# dispatch table for instantiated polymorphic SNAP templates
# BELOW INCLUDE out-*.txt
#

def LoadPajek(tspec, *args):
    if tspec == PUNGraph: return LoadPajek_PUNGraph(*args)
    if tspec == PUndirNet: return LoadPajek_PUndirNet(*args)
    if tspec == PDirNet: return LoadPajek_PDirNet(*args)
    if tspec == PNGraph : return LoadPajek_PNGraph(*args)
    if tspec == PNEANet : return LoadPajek_PNEANet(*args)
    if tspec == PNGraphMP: return LoadPajek_PNGraphMP(*args)
    if tspec == PNEANetMP: return LoadPajek_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def SaveGViz(tspec, *args):
    if type(tspec) == PUNGraph: return SaveGViz_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return SaveGViz_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return SaveGViz_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return SaveGViz_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return SaveGViz_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return SaveGViz_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return SaveGViz_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def TestAnf(tspec, *args):
    if type(tspec) == PUNGraph: return TestAnf_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return TestAnf_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return TestAnf_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return TestAnf_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return TestAnf_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return TestAnf_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return TestAnf_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetNodeWcc(tspec, *args):
    if type(tspec) == PUNGraph: return GetNodeWcc_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetNodeWcc_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetNodeWcc_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeWcc_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetNodeWcc_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetNodeWcc_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetNodeWcc_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def DelNodes(tspec, *args):
    if type(tspec) == PUNGraph: return DelNodes_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return DelNodes_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return DelNodes_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return DelNodes_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return DelNodes_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return DelNodes_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return DelNodes_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def CntEdgesToSet(tspec, *args):
    if type(tspec) == PUNGraph: return CntEdgesToSet_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return CntEdgesToSet_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return CntEdgesToSet_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return CntEdgesToSet_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return CntEdgesToSet_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return CntEdgesToSet_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return CntEdgesToSet_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetModularity(tspec, *args):
    if type(tspec) == PUNGraph: return GetModularity_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetModularity_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetModularity_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetModularity_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetModularity_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetModularity_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetModularity_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetBfsEffDiam(tspec, *args):
    if type(tspec) == PUNGraph: return GetBfsEffDiam_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetBfsEffDiam_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetBfsEffDiam_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetBfsEffDiam_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetBfsEffDiam_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetBfsEffDiam_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetBfsEffDiam_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PercentMxWcc(tspec, *args):
    if type(tspec) == PUNGraph: return PercentMxWcc_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PercentMxWcc_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PercentMxWcc_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PercentMxWcc_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PercentMxWcc_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PercentMxWcc_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PercentMxWcc_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetSubGraph(tspec, *args):
    if type(tspec) == PUNGraph: return GetSubGraph_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetSubGraph_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetSubGraph_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetSubGraph_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetSubGraph_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetSubGraph_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetSubGraph_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetBfsTree(tspec, *args):
    if type(tspec) == PUNGraph: return GetBfsTree_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetBfsTree_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetBfsTree_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetBfsTree_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetBfsTree_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetBfsTree_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetBfsTree_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PrintGraphStatTable(tspec, *args):
    if type(tspec) == PUNGraph: return PrintGraphStatTable_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PrintGraphStatTable_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PrintGraphStatTable_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PrintGraphStatTable_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PrintGraphStatTable_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PrintGraphStatTable_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PrintGraphStatTable_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetDegSeqV(tspec, *args):
    if type(tspec) == PUNGraph: return GetDegSeqV_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetDegSeqV_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetDegSeqV_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetDegSeqV_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetDegSeqV_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetDegSeqV_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetDegSeqV_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GenGrid(tspec, *args):
    if tspec == PUNGraph: return GenGrid_PUNGraph(*args)
    if tspec == PUndirNet: return GenGrid_PUndirNet(*args)
    if tspec == PDirNet: return GenGrid_PDirNet(*args)
    if tspec == PNGraph : return GenGrid_PNGraph(*args)
    if tspec == PNEANet : return GenGrid_PNEANet(*args)
    if tspec == PNGraphMP: return GenGrid_PNGraphMP(*args)
    if tspec == PNEANetMP : return GenGrid_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def LoadEdgeList(tspec, *args):
    if tspec == PUNGraph: return LoadEdgeList_PUNGraph(*args)
    if tspec == PUndirNet: return LoadEdgeList_PUndirNet(*args)
    if tspec == PDirNet: return LoadEdgeList_PDirNet(*args)
    if tspec == PNGraph : return LoadEdgeList_PNGraph(*args)
    if tspec == PNEANet : return LoadEdgeList_PNEANet(*args)
    if tspec == PNGraphMP: return LoadEdgeList_PNGraphMP(*args)
    if tspec == PNEANetMP : return LoadEdgeList_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def GetUnDir(tspec, *args):
    if type(tspec) == PUNGraph: return GetUnDir_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetUnDir_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetUnDir_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetUnDir_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetUnDir_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetUnDir_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetUnDir_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def DrawGViz(tspec, *args):
    if type(tspec) == PUNGraph: return DrawGViz_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return DrawGViz_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return DrawGViz_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return DrawGViz_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return DrawGViz_PNEANet(tspec, *args)
    if type(tspec) == PNEANetMP : return DrawGViz_PNEANetMP(tspec, *args)
    if type(tspec) == PNGraphMP: return DrawGViz_PNGraphMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PlotKCoreNodes(tspec, *args):
    if type(tspec) == PUNGraph: return PlotKCoreNodes_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PlotKCoreNodes_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PlotKCoreNodes_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PlotKCoreNodes_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PlotKCoreNodes_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PlotKCoreNodes_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PlotKCoreNodes_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PlotOutDegDistr(tspec, *args):
    if type(tspec) == PUNGraph: return PlotOutDegDistr_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PlotOutDegDistr_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PlotOutDegDistr_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PlotOutDegDistr_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PlotOutDegDistr_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PlotOutDegDistr_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PlotOutDegDistr_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def CntUniqBiDirEdges(tspec, *args):
    if type(tspec) == PUNGraph: return CntUniqBiDirEdges_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return CntUniqBiDirEdges_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return CntUniqBiDirEdges_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return CntUniqBiDirEdges_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return CntUniqBiDirEdges_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return CntUniqBiDirEdges_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return CntUniqBiDirEdges_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetKCoreEdges(tspec, *args):
    if type(tspec) == PUNGraph: return GetKCoreEdges_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetKCoreEdges_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetKCoreEdges_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetKCoreEdges_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetKCoreEdges_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetKCoreEdges_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetKCoreEdges_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetMxDegNId(tspec, *args):
    if type(tspec) == PUNGraph: return GetMxDegNId_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetMxDegNId_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetMxDegNId_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetMxDegNId_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetMxDegNId_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetMxDegNId_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetMxDegNId_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetBfsFullDiam(tspec, *args):
    if type(tspec) == PUNGraph: return GetBfsFullDiam_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetBfsFullDiam_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetBfsFullDiam_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetBfsFullDiam_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetBfsFullDiam_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetBfsFullDiam_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetBfsFullDiam_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def LoadConnList(tspec, *args):
    if tspec == PUNGraph: return LoadConnList_PUNGraph(*args)
    if tspec == PUndirNet: return LoadConnList_PUndirNet(*args)
    if tspec == PDirNet: return LoadConnList_PDirNet(*args)
    if tspec == PNGraph : return LoadConnList_PNGraph(*args)
    if tspec == PNEANet : return LoadConnList_PNEANet(*args)
    if tspec == PNGraphMP: return LoadConnList_PNGraphMP(*args)
    if tspec == PNEANetMP : return LoadConnList_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def GetHitsMP(tspec, *args):
    if type(tspec) == PUNGraph: return GetHitsMP_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetHitsMP_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetHitsMP_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetHitsMP_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetHitsMP_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetHitsMP_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetHitsMP_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetPageRank(tspec, *args):
    if type(tspec) == PUNGraph: return GetPageRank_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetPageRank_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetPageRank_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetPageRank_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetPageRank_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetPageRank_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetPageRank_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetPageRank_v1(tspec, *args):
    if type(tspec) == PUNGraph: return GetPageRank_v1_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetPageRank_v1_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetPageRank_v1_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetPageRank_v1_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetPageRank_v1_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetPageRank_v1_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetPageRank_v1_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def CntInDegNodes(tspec, *args):
    if type(tspec) == PUNGraph: return CntInDegNodes_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return CntInDegNodes_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return CntInDegNodes_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return CntInDegNodes_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return CntInDegNodes_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return CntInDegNodes_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return CntInDegNodes_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetMxScc(tspec, *args):
    if type(tspec) == PUNGraph: return GetMxScc_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetMxScc_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetMxScc_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetMxScc_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetMxScc_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetMxScc_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetMxScc_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def AddSelfEdges(tspec, *args):
    if type(tspec) == PUNGraph: return AddSelfEdges_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return AddSelfEdges_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return AddSelfEdges_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return AddSelfEdges_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return AddSelfEdges_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return AddSelfEdges_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return AddSelfEdges_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def DelDegKNodes(tspec, *args):
    if type(tspec) == PUNGraph: return DelDegKNodes_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return DelDegKNodes_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return DelDegKNodes_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return DelDegKNodes_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return DelDegKNodes_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return DelDegKNodes_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return DelDegKNodes_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PlotSccDistr(tspec, *args):
    if type(tspec) == PUNGraph: return PlotSccDistr_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PlotSccDistr_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PlotSccDistr_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PlotSccDistr_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PlotSccDistr_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PlotSccDistr_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PlotSccDistr_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def IsWeaklyConn(tspec, *args):
    if type(tspec) == PUNGraph: return IsWeaklyConn_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return IsWeaklyConn_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return IsWeaklyConn_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return IsWeaklyConn_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return IsWeaklyConn_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return IsWeaklyConn_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return IsWeaklyConn_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetMxInDegNId(tspec, *args):
    if type(tspec) == PUNGraph: return GetMxInDegNId_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetMxInDegNId_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetMxInDegNId_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetMxInDegNId_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetMxInDegNId_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetMxInDegNId_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetMxInDegNId_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetSccSzCnt(tspec, *args):
    if type(tspec) == PUNGraph: return GetSccSzCnt_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetSccSzCnt_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetSccSzCnt_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetSccSzCnt_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetSccSzCnt_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetSccSzCnt_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetSccSzCnt_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetClosenessCentr(tspec, *args):
    if type(tspec) == PUNGraph: return GetClosenessCentr_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetClosenessCentr_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetClosenessCentr_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetClosenessCentr_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetClosenessCentr_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetClosenessCentr_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetClosenessCentr_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def MxWccSz(tspec, *args):
    if type(tspec) == PUNGraph: return MxWccSz_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return MxWccSz_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return MxWccSz_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return MxWccSz_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return MxWccSz_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return MxWccSz_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return MxWccSz_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetCmnNbrs(tspec, *args):
    if type(tspec) == PUNGraph: return GetCmnNbrs_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetCmnNbrs_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetCmnNbrs_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetCmnNbrs_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetCmnNbrs_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetCmnNbrs_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetCmnNbrs_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetTriadEdges(tspec, *args):
    if type(tspec) == PUNGraph: return GetTriadEdges_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetTriadEdges_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetTriadEdges_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetTriadEdges_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetTriadEdges_PNEANet(tspec, *args)
    if type(tspec) == PNEANetMP : return GetTriadEdges_PNEANetMP(tspec, *args)
    if type(tspec) == PNGraphMP: return GetTriadEdges_PNGraphMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def LoadConnListStr(tspec, *args):
    if tspec == PUNGraph: return LoadConnListStr_PUNGraph(*args)
    if tspec == PUndirNet: return LoadConnListStr_PUndirNet(*args)
    if tspec == PDirNet: return LoadConnListStr_PDirNet(*args)
    if tspec == PNGraph : return LoadConnListStr_PNGraph(*args)
    if tspec == PNEANet : return LoadConnListStr_PNEANet(*args)
    if tspec == PNGraphMP: return LoadConnListStr_PNGraphMP(*args)
    if tspec == PNEANetMP : return LoadConnListStr_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def GetMxWccSz(tspec, *args):
    if type(tspec) == PUNGraph: return GetMxWccSz_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetMxWccSz_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetMxWccSz_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetMxWccSz_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetMxWccSz_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetMxWccSz_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetMxWccSz_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetMxOutDegNId(tspec, *args):
    if type(tspec) == PUNGraph: return GetMxOutDegNId_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetMxOutDegNId_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetMxOutDegNId_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetMxOutDegNId_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetMxOutDegNId_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetMxOutDegNId_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetMxOutDegNId_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetLen2Paths(tspec, *args):
    if type(tspec) == PUNGraph: return GetLen2Paths_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetLen2Paths_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetLen2Paths_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetLen2Paths_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetLen2Paths_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetLen2Paths_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetLen2Paths_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetPageRankMP(tspec, *args):
    if type(tspec) == PUNGraph: return GetPageRankMP_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetPageRankMP_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetPageRankMP_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetPageRankMP_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetPageRankMP_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetPageRankMP_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetPageRankMP_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PrintInfo(tspec, *args):
    if type(tspec) == PUNGraph: return PrintInfo_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PrintInfo_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PrintInfo_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PrintInfo_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PrintInfo_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PrintInfo_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PrintInfo_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetWccs(tspec, *args):
    if type(tspec) == PUNGraph: return GetWccs_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetWccs_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetWccs_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetWccs_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetWccs_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetWccs_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetWccs_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetMxWcc(tspec, *args):
    if type(tspec) == PUNGraph: return GetMxWcc_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetMxWcc_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetMxWcc_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetMxWcc_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetMxWcc_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetMxWcc_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetMxWcc_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetMxSccSz(tspec, *args):
    if type(tspec) == PUNGraph: return GetMxSccSz_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetMxSccSz_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetMxSccSz_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetMxSccSz_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetMxSccSz_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetMxSccSz_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetMxSccSz_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def CntSelfEdges(tspec, *args):
    if type(tspec) == PUNGraph: return CntSelfEdges_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return CntSelfEdges_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return CntSelfEdges_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return CntSelfEdges_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return CntSelfEdges_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return CntSelfEdges_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return CntSelfEdges_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def NodesGTEDegree(tspec, *args):
    if type(tspec) == PUNGraph: return NodesGTEDegree_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return NodesGTEDegree_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return NodesGTEDegree_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return NodesGTEDegree_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return NodesGTEDegree_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return NodesGTEDegree_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return NodesGTEDegree_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PlotShortPathDistr(tspec, *args):
    if type(tspec) == PUNGraph: return PlotShortPathDistr_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PlotShortPathDistr_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PlotShortPathDistr_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PlotShortPathDistr_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PlotShortPathDistr_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PlotShortPathDistr_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PlotShortPathDistr_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetNodesAtHop(tspec, *args):
    if type(tspec) == PUNGraph: return GetNodesAtHop_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetNodesAtHop_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetNodesAtHop_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetNodesAtHop_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetNodesAtHop_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetNodesAtHop_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetNodesAtHop_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PlotInDegDistr(tspec, *args):
    if type(tspec) == PUNGraph: return PlotInDegDistr_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PlotInDegDistr_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PlotInDegDistr_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PlotInDegDistr_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PlotInDegDistr_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PlotInDegDistr_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PlotInDegDistr_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetHits(tspec, *args):
    if type(tspec) == PUNGraph: return GetHits_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetHits_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetHits_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetHits_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetHits_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetHits_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetHits_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetMxBiCon(tspec, *args):
    if type(tspec) == PUNGraph: return GetMxBiCon_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetMxBiCon_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetMxBiCon_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetMxBiCon_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetMxBiCon_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetMxBiCon_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetMxBiCon_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def DelZeroDegNodes(tspec, *args):
    if type(tspec) == PUNGraph: return DelZeroDegNodes_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return DelZeroDegNodes_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return DelZeroDegNodes_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return DelZeroDegNodes_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return DelZeroDegNodes_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return DelZeroDegNodes_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return DelZeroDegNodes_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetRndESubGraph(tspec, *args):
    if type(tspec) == PUNGraph: return GetRndESubGraph_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetRndESubGraph_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetRndESubGraph_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetRndESubGraph_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetRndESubGraph_PNEANet(tspec, *args)
    if type(tspec) == PNEANetMP : return GetRndESubGraph_PNEANetMP(tspec, *args)
    if type(tspec) == PNGraphMP: return GetRndESubGraph_PNGraphMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetSccs(tspec, *args):
    if type(tspec) == PUNGraph: return GetSccs_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetSccs_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetSccs_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetSccs_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetSccs_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetSccs_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetSccs_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PercentDegree(tspec, *args):
    if type(tspec) == PUNGraph: return PercentDegree_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PercentDegree_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PercentDegree_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PercentDegree_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PercentDegree_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PercentDegree_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PercentDegree_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetSubTreeSz(tspec, *args):
    if type(tspec) == PUNGraph: return GetSubTreeSz_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetSubTreeSz_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetSubTreeSz_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetSubTreeSz_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetSubTreeSz_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetSubTreeSz_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetSubTreeSz_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GenFull(tspec, *args):
    if tspec == PUNGraph: return GenFull_PUNGraph(*args)
    if tspec == PUndirNet: return GenFull_PUndirNet(*args)
    if tspec == PDirNet: return GenFull_PDirNet(*args)
    if tspec == PNGraph : return GenFull_PNGraph(*args)
    if tspec == PNEANet : return GenFull_PNEANet(*args)
    if tspec == PNGraphMP: return GenFull_PNGraphMP(*args)
    if tspec == PNEANetMP : return GenFull_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def IsConnected(tspec, *args):
    if type(tspec) == PUNGraph: return IsConnected_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return IsConnected_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return IsConnected_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return IsConnected_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return IsConnected_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return IsConnected_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return IsConnected_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetNodeClustCf(tspec, *args):
    if type(tspec) == PUNGraph: return GetNodeClustCf_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetNodeClustCf_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetNodeClustCf_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeClustCf_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetNodeClustCf_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetNodeClustCf_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetNodeClustCf_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def MxDegree(tspec, *args):
    if type(tspec) == PUNGraph: return MxDegree_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return MxDegree_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return MxDegree_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return MxDegree_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return MxDegree_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return MxDegree_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return MxDegree_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def SavePajek(tspec, *args):
    if type(tspec) == PUNGraph: return SavePajek_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return SavePajek_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return SavePajek_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return SavePajek_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return SavePajek_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return SavePajek_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return SavePajek_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetTreeRootNId(tspec, *args):
    if type(tspec) == PUNGraph: return GetTreeRootNId_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetTreeRootNId_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetTreeRootNId_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetTreeRootNId_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetTreeRootNId_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetTreeRootNId_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetTreeRootNId_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PlotHops(tspec, *args):
    if type(tspec) == PUNGraph: return PlotHops_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PlotHops_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PlotHops_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PlotHops_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PlotHops_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PlotHops_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PlotHops_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def DelSelfEdges(tspec, *args):
    if type(tspec) == PUNGraph: return DelSelfEdges_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return DelSelfEdges_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return DelSelfEdges_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return DelSelfEdges_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return DelSelfEdges_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return DelSelfEdges_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return DelSelfEdges_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetClustCf(tspec, *args):
    if type(tspec) == PUNGraph: return GetClustCf_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetClustCf_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetClustCf_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetClustCf_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetClustCf_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetClustCf_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetClustCf_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetNodesAtHops(tspec, *args):
    if type(tspec) == PUNGraph: return GetNodesAtHops_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetNodesAtHops_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetNodesAtHops_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetNodesAtHops_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetNodesAtHops_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetNodesAtHops_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetNodesAtHops_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetNodeOutDegV(tspec, *args):
    if type(tspec) == PUNGraph: return GetNodeOutDegV_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetNodeOutDegV_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetNodeOutDegV_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeOutDegV_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetNodeOutDegV_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetNodeOutDegV_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetNodeOutDegV_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetAnf(tspec, *args):
    if type(tspec) == PUNGraph: return GetAnf_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetAnf_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetAnf_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetAnf_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetAnf_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetAnf_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetAnf_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PlotClustCf(tspec, *args):
    if type(tspec) == PUNGraph: return PlotClustCf_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PlotClustCf_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PlotClustCf_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PlotClustCf_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PlotClustCf_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PlotClustCf_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PlotClustCf_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GenCircle(tspec, *args):
    if tspec == PUNGraph: return GenCircle_PUNGraph(*args)
    if tspec == PUndirNet: return GenCircle_PUndirNet(*args)
    if tspec == PDirNet: return GenCircle_PDirNet(*args)
    if tspec == PNGraph : return GenCircle_PNGraph(*args)
    if tspec == PNEANet : return GenCircle_PNEANet(*args)
    if tspec == PNGraphMP: return GenCircle_PNGraphMP(*args)
    if tspec == PNEANetMP : return GenCircle_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def MakeUnDir(tspec, *args):
    if type(tspec) == PUNGraph: return MakeUnDir_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return MakeUnDir_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return MakeUnDir_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return MakeUnDir_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return MakeUnDir_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return MakeUnDir_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return MakeUnDir_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetESubGraph(tspec, *args):
    if type(tspec) == PUNGraph: return GetESubGraph_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetESubGraph_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetESubGraph_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetESubGraph_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetESubGraph_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetESubGraph_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetESubGraph_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetBetweennessCentr(tspec, *args):
    if type(tspec) == PUNGraph: return GetBetweennessCentr_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetBetweennessCentr_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetBetweennessCentr_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetBetweennessCentr_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetBetweennessCentr_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetBetweennessCentr_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetBetweennessCentr_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetTriadParticip(tspec, *args):
    if type(tspec) == PUNGraph: return GetTriadParticip_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetTriadParticip_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetTriadParticip_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetTriadParticip_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetTriadParticip_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetTriadParticip_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetTriadParticip_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PercentMxScc(tspec, *args):
    if type(tspec) == PUNGraph: return PercentMxScc_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PercentMxScc_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PercentMxScc_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PercentMxScc_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PercentMxScc_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PercentMxScc_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PercentMxScc_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetWccSzCnt(tspec, *args):
    if type(tspec) == PUNGraph: return GetWccSzCnt_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetWccSzCnt_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetWccSzCnt_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetWccSzCnt_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetWccSzCnt_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetWccSzCnt_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetWccSzCnt_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def CntDegNodes(tspec, *args):
    if type(tspec) == PUNGraph: return CntDegNodes_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return CntDegNodes_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return CntDegNodes_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return CntDegNodes_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return CntDegNodes_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return CntDegNodes_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return CntDegNodes_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def IsTree(tspec, *args):
    if type(tspec) == PUNGraph: return IsTree_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return IsTree_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return IsTree_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return IsTree_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return IsTree_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return IsTree_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return IsTree_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GenRndGnm(tspec, *args):
    if tspec == PUNGraph: return GenRndGnm_PUNGraph(*args)
    if tspec == PUndirNet: return GenRndGnm_PUndirNet(*args)
    if tspec == PDirNet: return GenRndGnm_PDirNet(*args)
    if tspec == PNGraph : return GenRndGnm_PNGraph(*args)
    if tspec == PNEANet : return GenRndGnm_PNEANet(*args)
    if tspec == PNGraphMP: return GenRndGnm_PNGraphMP(*args)
    if tspec == PNEANetMP : return GenRndGnm_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def GetDegCnt(tspec, *args):
    if type(tspec) == PUNGraph: return GetDegCnt_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetDegCnt_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetDegCnt_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetDegCnt_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetDegCnt_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetDegCnt_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetDegCnt_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetFarnessCentr(tspec, *args):
    if type(tspec) == PUNGraph: return GetFarnessCentr_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetFarnessCentr_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetFarnessCentr_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetFarnessCentr_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetFarnessCentr_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetFarnessCentr_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetFarnessCentr_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def SaveMatlabSparseMtx(tspec, *args):
    if type(tspec) == PUNGraph: return SaveMatlabSparseMtx_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return SaveMatlabSparseMtx_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return SaveMatlabSparseMtx_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return SaveMatlabSparseMtx_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return SaveMatlabSparseMtx_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return SaveMatlabSparseMtx_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return SaveMatlabSparseMtx_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def MxSccSz(tspec, *args):
    if type(tspec) == PUNGraph: return MxSccSz_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return MxSccSz_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return MxSccSz_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return MxSccSz_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return MxSccSz_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return MxSccSz_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return MxSccSz_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetAnfEffDiam(tspec, *args):
    if type(tspec) == PUNGraph: return GetAnfEffDiam_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetAnfEffDiam_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetAnfEffDiam_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetAnfEffDiam_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetAnfEffDiam_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetAnfEffDiam_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetAnfEffDiam_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetTreeSig(tspec, *args):
    if type(tspec) == PUNGraph: return GetTreeSig_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetTreeSig_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetTreeSig_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetTreeSig_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetTreeSig_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetTreeSig_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetTreeSig_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def CntOutDegNodes(tspec, *args):
    if type(tspec) == PUNGraph: return CntOutDegNodes_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return CntOutDegNodes_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return CntOutDegNodes_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return CntOutDegNodes_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return CntOutDegNodes_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return CntOutDegNodes_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return CntOutDegNodes_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetTriangleCnt(tspec, *args):
    if type(tspec) == PUNGraph: return GetTriangleCnt_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetTriangleCnt_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetTriangleCnt_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetTriangleCnt_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetTriangleCnt_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetTriangleCnt_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetTriangleCnt_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetOutDegCnt(tspec, *args):
    if type(tspec) == PUNGraph: return GetOutDegCnt_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetOutDegCnt_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetOutDegCnt_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetOutDegCnt_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetOutDegCnt_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetOutDegCnt_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetOutDegCnt_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GenBaraHierar(tspec, *args):
    if tspec == PUNGraph: return GenBaraHierar_PUNGraph(*args)
    if tspec == PUndirNet: return GenBaraHierar_PUndirNet(*args)
    if tspec == PDirNet: return GenBaraHierar_PDirNet(*args)
    if tspec == PNGraph : return GenBaraHierar_PNGraph(*args)
    if tspec == PNEANet : return GenBaraHierar_PNEANet(*args)
    if tspec == PNGraphMP: return GenBaraHierar_PNGraphMP(*args)
    if tspec == PNEANetMP : return GenBaraHierar_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def GenTree(tspec, *args):
    if tspec == PUNGraph: return GenTree_PUNGraph(*args)
    if tspec == PUndirNet: return GenTree_PUndirNet(*args)
    if tspec == PDirNet: return GenTree_PDirNet(*args)
    if tspec == PNGraph : return GenTree_PNGraph(*args)
    if tspec == PNEANet : return GenTree_PNEANet(*args)
    if tspec == PNGraphMP: return GenTree_PNGraphMP(*args)
    if tspec == PNEANetMP : return GenTree_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def GetShortPath(tspec, *args):
    if type(tspec) == PUNGraph: return GetShortPath_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetShortPath_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetShortPath_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetShortPath_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetShortPath_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetShortPath_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetShortPath_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetKCoreNodes(tspec, *args):
    if type(tspec) == PUNGraph: return GetKCoreNodes_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetKCoreNodes_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetKCoreNodes_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetKCoreNodes_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetKCoreNodes_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetKCoreNodes_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetKCoreNodes_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetInDegCnt(tspec, *args):
    if type(tspec) == PUNGraph: return GetInDegCnt_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetInDegCnt_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetInDegCnt_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetInDegCnt_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetInDegCnt_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetInDegCnt_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetInDegCnt_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def CntUniqDirEdges(tspec, *args):
    if type(tspec) == PUNGraph: return CntUniqDirEdges_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return CntUniqDirEdges_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return CntUniqDirEdges_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return CntUniqDirEdges_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return CntUniqDirEdges_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return CntUniqDirEdges_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return CntUniqDirEdges_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetNodeInDegV(tspec, *args):
    if type(tspec) == PUNGraph: return GetNodeInDegV_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetNodeInDegV_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetNodeInDegV_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeInDegV_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetNodeInDegV_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetNodeInDegV_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetNodeInDegV_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetRndSubGraph(tspec, *args):
    if type(tspec) == PUNGraph: return GetRndSubGraph_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetRndSubGraph_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetRndSubGraph_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetRndSubGraph_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetRndSubGraph_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetRndSubGraph_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetRndSubGraph_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def PlotWccDistr(tspec, *args):
    if type(tspec) == PUNGraph: return PlotWccDistr_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PlotWccDistr_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PlotWccDistr_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PlotWccDistr_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PlotWccDistr_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PlotWccDistr_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PlotWccDistr_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetEdgesInOut(tspec, *args):
    if type(tspec) == PUNGraph: return GetEdgesInOut_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetEdgesInOut_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetEdgesInOut_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetEdgesInOut_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetEdgesInOut_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetEdgesInOut_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetEdgesInOut_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetKCore(tspec, *args):
    if type(tspec) == PUNGraph: return GetKCore_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetKCore_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetKCore_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetKCore_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetKCore_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetKCore_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetKCore_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def CntNonZNodes(tspec, *args):
    if type(tspec) == PUNGraph: return CntNonZNodes_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return CntNonZNodes_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return CntNonZNodes_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return CntNonZNodes_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return CntNonZNodes_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return CntNonZNodes_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return CntNonZNodes_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GenStar(tspec, *args):
    if tspec == PUNGraph: return GenStar_PUNGraph(*args)
    if tspec == PUndirNet: return GenStar_PUndirNet(*args)
    if tspec == PDirNet: return GenStar_PDirNet(*args)
    if tspec == PNGraph : return GenStar_PNGraph(*args)
    if tspec == PNEANet : return GenStar_PNEANet(*args)
    if tspec == PNGraphMP: return GenStar_PNGraphMP(*args)
    if tspec == PNEANetMP : return GenStar_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def PlotKCoreEdges(tspec, *args):
    if type(tspec) == PUNGraph: return PlotKCoreEdges_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return PlotKCoreEdges_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return PlotKCoreEdges_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return PlotKCoreEdges_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return PlotKCoreEdges_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return PlotKCoreEdges_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return PlotKCoreEdges_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def SaveEdgeList(tspec, *args):
    if type(tspec) == PUNGraph: return SaveEdgeList_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return SaveEdgeList_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return SaveEdgeList_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return SaveEdgeList_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return SaveEdgeList_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return SaveEdgeList_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return SaveEdgeList_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetNodeTriads(tspec, *args):
    if type(tspec) == PUNGraph: return GetNodeTriads_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetNodeTriads_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetNodeTriads_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeTriads_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetNodeTriads_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetNodeTriads_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetNodeTriads_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetNodeEcc(tspec, *args):
    if type(tspec) == PUNGraph: return GetNodeEcc_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetNodeEcc_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetNodeEcc_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeEcc_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetNodeEcc_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetNodeEcc_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetNodeEcc_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def LoadEdgeListStr(tspec, *args):
    if tspec == PUNGraph: return LoadEdgeListStr_PUNGraph(*args)
    if tspec == PUndirNet: return LoadEdgeListStr_PUndirNet(*args)
    if tspec == PDirNet: return LoadEdgeListStr_PDirNet(*args)
    if tspec == PNGraph : return LoadEdgeListStr_PNGraph(*args)
    if tspec == PNEANet : return LoadEdgeListStr_PNEANet(*args)
    if tspec == PNGraphMP: return LoadEdgeListStr_PNGraphMP(*args)
    if tspec == PNEANetMP : return LoadEdgeListStr_PNEANetMP(*args)
    raise TypeError('First argument has invalid type')
def CntUniqUndirEdges(tspec, *args):
    if type(tspec) == PUNGraph: return CntUniqUndirEdges_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return CntUniqUndirEdges_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return CntUniqUndirEdges_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return CntUniqUndirEdges_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return CntUniqUndirEdges_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return CntUniqUndirEdges_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return CntUniqUndirEdges_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')
def GetTriads(tspec, *args):
    if type(tspec) == PUNGraph: return GetTriads_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetTriads_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetTriads_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetTriads_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetTriads_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetTriads_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetTriads_PNEANetMP(tspec, *args)
    raise TypeError('First argument has invalid type')

#
# BELOW INCLUDE disp-custom.py
#
def ConvertGraph(toutspec, tinspec, *args):
    if toutspec == PUNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PUNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertGraph_PUNGraph_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertGraph_PUNGraph_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PUNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PUNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PUNGraph_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertGraph_PUNGraph_PNEANetMP(tinspec, *args)
    if toutspec == PUndirNet:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PUndirNet_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertGraph_PUndirNet_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertGraph_PUndirNet_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PUndirNet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PUndirNet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PUndirNet_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertGraph_PUndirNet_PNEANetMP(tinspec, *args)
    if toutspec == PDirNet:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PDirNet_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertGraph_PDirNet_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertGraph_PDirNet_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PDirNet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PDirNet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PDirNet_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertGraph_PDirNet_PNEANetMP(tinspec, *args)
    if toutspec == PNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertGraph_PNGraph_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertGraph_PNGraph_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PNGraph_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertGraph_PNGraph_PNEANetMP(tinspec, *args)
    if toutspec == PNEANet:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PNEANet_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertGraph_PNEANet_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertGraph_PNEANet_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PNEANet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PNEANet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PNEANet_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertGraph_PNEANet_PNEANetMP(tinspec, *args)
    if toutspec == PNGraphMP:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PNGraphMP_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertGraph_PNGraphMP_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertGraph_PNGraphMP_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PNGraphMP_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PNGraphMP_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PNGraphMP_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertGraph_PNGraphMP_PNEANetMP(tinspec, *args)
    if toutspec == PNEANetMP:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PNEANetMP_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertGraph_PNEANetMP_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertGraph_PNEANetMP_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PNEANetMP_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PNEANetMP_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PNEANetMP_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertGraph_PNEANetMP_PNEANetMP(tinspec, *args)
    raise TypeError('First argument has invalid type')
def ConvertSubGraph(toutspec, tinspec, *args):
    if toutspec == PUNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PUNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertSubGraph_PUNGraph_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertSubGraph_PUNGraph_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PUNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PUNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PUNGraph_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertSubGraph_PUNGraph_PNEANetMP(tinspec, *args)
    if toutspec == PUndirNet:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PUndirNet_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertSubGraph_PUndirNet_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertSubGraph_PUndirNet_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PUndirNet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PUndirNet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PUndirNet_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertSubGraph_PUndirNet_PNEANetMP(tinspec, *args)
    if toutspec == PDirNet:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PDirNet_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertSubGraph_PDirNet_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertSubGraph_PDirNet_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PDirNet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PDirNet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PDirNet_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertSubGraph_PDirNet_PNEANetMP(tinspec, *args)
    if toutspec == PNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertSubGraph_PNGraph_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertSubGraph_PNGraph_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PNGraph_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertSubGraph_PNGraph_PNEANetMP(tinspec, *args)
    if toutspec == PNEANet:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PNEANet_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertSubGraph_PNEANet_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertSubGraph_PNEANet_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PNEANet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PNEANet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PNEANet_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertSubGraph_PNEANet_PNEANetMP(tinspec, *args)
    if toutspec == PNGraphMP:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PNGraphMP_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertSubGraph_PNGraphMP_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertSubGraph_PNGraphMP_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PNGraphMP_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PNGraphMP_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PNGraphMP_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertSubGraph_PNGraphMP_PNEANetMP(tinspec, *args)
    if toutspec == PNEANetMP:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PNEANetMP_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertSubGraph_PNEANetMP_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertSubGraph_PNEANetMP_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PNEANetMP_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PNEANetMP_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PNEANetMP_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertSubGraph_PNEANetMP_PNEANetMP(tinspec, *args)
    raise TypeError('First argument has invalid type')
def ConvertESubGraph(toutspec, tinspec, *args):
    if toutspec == PUNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PUNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertESubGraph_PUNGraph_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertESubGraph_PUNGraph_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PUNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PUNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PUNGraph_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertESubGraph_PUNGraph_PNEANetMP(tinspec, *args)
    if toutspec == PUndirNet:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PUndirNet_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertESubGraph_PUndirNet_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertESubGraph_PUndirNet_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PUndirNet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PUndirNet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PUndirNet_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertESubGraph_PUndirNet_PNEANetMP(tinspec, *args)
    if toutspec == PDirNet:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PDirNet_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertESubGraph_PDirNet_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertESubGraph_PDirNet_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PDirNet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PDirNet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PDirNet_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertESubGraph_PDirNet_PNEANetMP(tinspec, *args)
    if toutspec == PNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertESubGraph_PNGraph_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertESubGraph_PNGraph_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PNGraph_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertESubGraph_PNGraph_PNEANetMP(tinspec, *args)
    if toutspec == PNEANet:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PNEANet_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertESubGraph_PNEANet_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertESubGraph_PNEANet_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PNEANet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PNEANet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PNEANet_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertESubGraph_PNEANet_PNEANetMP(tinspec, *args)
    if toutspec == PNGraphMP:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PNGraphMP_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertESubGraph_PNGraphMP_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertESubGraph_PNGraphMP_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PNGraphMP_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PNGraphMP_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PNGraphMP_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertESubGraph_PNGraphMP_PNEANetMP(tinspec, *args)
    if toutspec == PNEANetMP:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PNEANetMP_PUNGraph(tinspec, *args)
        if type(tinspec) == PUndirNet:
            return ConvertESubGraph_PNEANetMP_PUndirNet(tinspec, *args)
        if type(tinspec) == PDirNet:
            return ConvertESubGraph_PNEANetMP_PDirNet(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PNEANetMP_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PNEANetMP_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PNEANetMP_PNGraphMP(tinspec, *args)
        if type(tinspec) == PNEANetMP:
            return ConvertESubGraph_PNEANetMP_PNEANetMP(tinspec, *args)
    raise TypeError('First argument has invalid type')
def ToNetwork(tspec, *args):
    if tspec == PNEANet : return ToNetwork_PNEANet(*args)
    raise TypeError('First argument has invalid type')
def ToGraph(tspec, *args):
    if tspec == PUNGraph: return ToGraph_PUNGraph(*args)
    if tspec == PUndirNet: return ToGraph_PUndirNet(*args)
    if tspec == PDirNet: return ToGraph_PDirNet(*args)
    if tspec == PNGraph : return ToGraph_PNGraph(*args)
    raise TypeError('First argument has invalid type')

#
# generators for nodes and edges
#

# iterate through all the nodes
def Nodes(self):
    NI = self.BegNI()
    while NI < self.EndNI():
        yield NI
        NI.Next()

# iterate through all the edges
def Edges(self):
    EI = self.BegEI()
    while EI < self.EndEI():
        yield EI
        EI.Next()

# iterate through out edges of a node
def GetOutEdges(self):
    for e in range(0, self.GetOutDeg()):
        yield self.GetOutNId(e)

# iterate through in edges of a node
def GetInEdges(self):
    for e in range(0, self.GetInDeg()):
        yield self.GetInNId(e)

#
# generators for nodes and edges
#

# iterate through all the nodes
def MMNodes(self):
    NI = self.BegMMNI()
    while NI < self.EndMMNI():
        yield NI
        NI.Next()

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

TModeNet.Nodes = MMNodes
TModeNet.Edges = Edges

PMMNet.Save = Save

PUNGraph.Nodes = Nodes
PUNGraph.Edges = Edges
PUNGraph.Clr = Clr
PUNGraph.Empty = Empty
PUNGraph.Save = Save


PUndirNet.Nodes = Nodes
PUndirNet.Edges = Edges
PUndirNet.Clr = Clr
PUndirNet.Empty = Empty
PUndirNet.Save = Save

PDirNet.Nodes = Nodes
PDirNet.Edges = Edges
PDirNet.Clr = Clr
PDirNet.Empty = Empty
PDirNet.Save = Save

PNGraph.Nodes = Nodes
PNGraph.Edges = Edges
PNGraph.Clr = Clr
PNGraph.Empty = Empty
PNGraph.Save = Save

TNGraphNodeI.GetOutEdges = GetOutEdges
TNGraphNodeI.GetInEdges = GetInEdges

TUNGraphNodeI.GetOutEdges = GetOutEdges
TUNGraphNodeI.GetInEdges = GetInEdges

TDirNetNodeI.GetOutEdges = GetOutEdges
TDirNetNodeI.GetInEdges = GetInEdges

TUndirNetNodeI.GetOutEdges = GetOutEdges
TUndirNetNodeI.GetInEdges = GetInEdges

TNEANetNodeI.GetOutEdges = GetOutEdges
TNEANetNodeI.GetInEdges = GetInEdges

TModeNetNodeI.GetOutEdges = GetOutEdges
TModeNetNodeI.GetInEdges = GetInEdges

%}

#if GCC_ATOMIC
%pythoncode %{

PNGraphMP.Nodes = Nodes
PNGraphMP.Edges = Edges
PNGraphMP.Clr = Clr
PNGraphMP.Empty = Empty
PNGraphMP.Save = Save

PNEANetMP.Nodes = Nodes
PNEANetMP.Edges = Edges
PNEANetMP.Clr = Clr
PNEANetMP.Empty = Empty
PNEANetMP.Save = Save

TNGraphMPNodeI.GetOutEdges = GetOutEdges
TNGraphMPNodeI.GetInEdges = GetInEdges

TNEANetMPNodeI.GetOutEdges = GetOutEdges
TNEANetMPNodeI.GetInEdges = GetInEdges

%}
#endif // GCC_ATOMIC


