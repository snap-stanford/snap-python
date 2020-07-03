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
def GetBfsEffDiamAll(tspec, *args):
    if type(tspec) == PUNGraph: return GetBfsEffDiamAll_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetBfsEffDiamAll_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetBfsEffDiamAll_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetBfsEffDiamAll_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetBfsEffDiamAll_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetBfsEffDiamAll_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetBfsEffDiamAll_PNEANetMP(tspec, *args)
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
def GetSubGraphRenumber(tspec, *args):
    if type(tspec) == PUNGraph: return GetSubGraphRenumber_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetSubGraphRenumber_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetSubGraphRenumber_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetSubGraphRenumber_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetSubGraphRenumber_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetSubGraphRenumber_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetSubGraphRenumber_PNEANetMP(tspec, *args)
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
def GetClustCfAll(tspec, *args):
    if type(tspec) == PUNGraph: return GetClustCfAll_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetClustCfAll_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetClustCfAll_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetClustCfAll_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetClustCfAll_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetClustCfAll_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetClustCfAll_PNEANetMP(tspec, *args)
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
def GetNodeTriadsAll(tspec, *args):
    if type(tspec) == PUNGraph: return GetNodeTriadsAll_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetNodeTriadsAll_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetNodeTriadsAll_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetNodeTriadsAll_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetNodeTriadsAll_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetNodeTriadsAll_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetNodeTriadsAll_PNEANetMP(tspec, *args)
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
def GetTriadsAll(tspec, *args):
    if type(tspec) == PUNGraph: return GetTriadsAll_PUNGraph(tspec, *args)
    if type(tspec) == PUndirNet: return GetTriadsAll_PUndirNet(tspec, *args)
    if type(tspec) == PDirNet: return GetTriadsAll_PDirNet(tspec, *args)
    if type(tspec) == PNGraph : return GetTriadsAll_PNGraph(tspec, *args)
    if type(tspec) == PNEANet : return GetTriadsAll_PNEANet(tspec, *args)
    if type(tspec) == PNGraphMP: return GetTriadsAll_PNGraphMP(tspec, *args)
    if type(tspec) == PNEANetMP : return GetTriadsAll_PNEANetMP(tspec, *args)
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

#ifdef GCC_ATOMIC
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


// Add compatibility for Python data types as arguments, moving arguments to output, and overloaded functions

%pythoncode %{

    # This function adds compatility to additional datatypes
    # Works for Python types: list, set, and dict (with their corresponding SNAP types)
    def ConvertToSnapType(args, pos, SnapType, PyType):
        if len(args) > pos:
            arg = args[pos]
            if type(arg) == PyType:
                convertedArgs = list(args)
                convertedArg = SnapType()

                try:
                    if PyType == list:
                        for item in arg:
                            convertedArg.Add(item)
                    elif PyType == set:
                        for item in arg:
                            convertedArg.AddKey(item)
                    elif PyType == dict: 
                        for key in arg:
                            convertedArg[key] = arg[key]
                except TypeError:
                    # Raise TypeError instead of the general SystemError
                    raise

                convertedArgs[pos] = convertedArg

                return tuple(convertedArgs)

        return args


    # This function moves the argument at pos to be returned instead
    def MoveArgToReturn (tspec, args, func, pos, argType):
        if len(args) > pos and type(args[pos]) == argType:
            #For backward compatility
            return func(tspec, *args)
        else:
            returnArg = argType()
            newArgs = list(args)
            newArgs.insert(pos, returnArg)
            oldReturn = func(tspec, *newArgs)
            if oldReturn == None:
                return returnArg
            else:
                return (oldReturn, returnArg)


    _LoadEdgeList = LoadEdgeList
    def LoadEdgeList(GraphType, InFNm, SrcColId = 0, DstColId = 1, Separator = " "):
        if Separator == " ":
            return _LoadEdgeList(GraphType, InFNm, SrcColId, DstColId)
        else:
            return _LoadEdgeList(GraphType, InFNm, SrcColId, DstColId, Separator)


    _LoadEdgeListStr = LoadEdgeListStr
    def LoadEdgeListStr(GraphType, InFNm, SrcColId = 0, DstColId = 1, Mapping = False):
        if Mapping == False:
            return _LoadEdgeListStr(GraphType, InFNm, SrcColId, DstColId)
        else:
            StrToNIdH = TStrIntSH()
            graph = _LoadEdgeListStr(GraphType, InFNm, SrcColId, DstColId, StrToNIdH)
            return (graph, StrToNIdH)


    _LoadConnListStr = LoadConnListStr 
    def LoadConnListStr(GraphType, *args):
        return MoveArgToReturn(GraphType, args, _LoadConnListStr, 1, TStrIntSH)


    _SaveGViz = SaveGViz
    def SaveGViz(Graph, *args):
        args = ConvertToSnapType(args, -1, TIntStrH, dict)
        return _SaveGViz(Graph, *args)


    _SavePajek = SavePajek
    def SavePajek(Graph, OutFNm, NIdColorH = None, NIdLabelH = None, EIdColorH = None):
        if NIdColorH is None:
            NIdColorH = TIntStrH()
        if NIdLabelH is None:
            NIdLabelH = TIntStrH()
        if EIdColorH is None:
            EIdColorH = TIntStrH()
        args = (OutFNm, NIdColorH, NIdLabelH, EIdColorH)
        args = ConvertToSnapType(args, 1, TIntStrH, dict)
        args = ConvertToSnapType(args, 2, TIntStrH, dict)
        args = ConvertToSnapType(args, 3, TIntStrH, dict)
        return _SavePajek(Graph, *args)


    _GetDegCnt = GetDegCnt
    def GetDegCnt(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetDegCnt, 0, TIntPrV)


    _GetInDegCnt = GetInDegCnt
    def GetInDegCnt(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetInDegCnt, 0, TIntPrV)


    _GetOutDegCnt = GetOutDegCnt
    def GetOutDegCnt(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetOutDegCnt, 0, TIntPrV)        


    _GetNodeInDegV = GetNodeInDegV
    def GetNodeInDegV(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetNodeInDegV, 0, TIntPrV)


    _GetNodeOutDegV = GetNodeOutDegV
    def GetNodeOutDegV(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetNodeOutDegV, 0, TIntPrV)


    _GetDegSeqV = GetDegSeqV
    def GetDegSeqV(Graph, *args, **kwargs):
        if len(args) > 0 and type(args[0]) == TIntV:
            #Backward compatibility
            return _GetDegSeqV(Graph, *args)
        else:
            if (len(args) + len(kwargs) == 0) or (len(args) == 1 and args[0] == False) or (len(kwargs) == 1 and kwargs['Dir'] == False):
                # case Dir = False
                DegV = TIntV()
                _GetDegSeqV(Graph, DegV)
                return DegV
            else:
                # case Dir = True
                InDegV = TIntV()
                OutDegV = TIntV()
                _GetDegSeqV(Graph, InDegV, OutDegV)
                return (InDegV, OutDegV)               


    _CntEdgesToSet = CntEdgesToSet
    def CntEdgesToSet(Graph, *args):
        args = ConvertToSnapType(args, 1, TIntSet, set)
        return _CntEdgesToSet(Graph, *args)


    _DelNodes = DelNodes
    def DelNodes(Graph, *args):
        args = ConvertToSnapType(args, 0, TIntV, list)
        return _DelNodes(Graph, *args)


    _ConvertSubGraph = ConvertSubGraph
    def ConvertSubGraph(GraphType, InGraph, *args):
        args = ConvertToSnapType(args, 0, TIntV, list)
        return _ConvertSubGraph(GraphType, InGraph, *args)


    _ConvertESubGraph = ConvertESubGraph
    def ConvertESubGraph(GraphType, InGraph, *args):
        args = ConvertToSnapType(args, 0, TIntV, list)
        return _ConvertESubGraph(GraphType, InGraph, *args)


    _GetSubGraph = GetSubGraph
    def GetSubGraph(Graph, *args):
        args = ConvertToSnapType(args, 0, TIntV, list)
        return _GetSubGraph(Graph, *args)


    _GetSubGraphRenumber = GetSubGraphRenumber
    def GetSubGraphRenumber(Graph, *args):
        args = ConvertToSnapType(args, 0, TIntV, list)
        return _GetSubGraphRenumber(Graph, *args)


    _GetESubGraph = GetESubGraph
    def GetESubGraph(Graph, *args):
        args = ConvertToSnapType(args, 0, TIntV, list)
        return _GetESubGraph(Graph, *args)


    _DrawGViz = DrawGViz
    def DrawGViz(Graph, *args):
        args = ConvertToSnapType(args, -1, TIntStrH, dict)
        return _DrawGViz(Graph, *args)


    _GetSccs = GetSccs
    def GetSccs(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetSccs, 0, TCnComV)


    _GetSccSzCnt = GetSccSzCnt
    def GetSccSzCnt(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetSccSzCnt, 0, TIntPrV)  


    _GetWccs = GetWccs
    def GetWccs(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetWccs, 0, TCnComV)


    _GetWccSzCnt = GetWccSzCnt
    def GetWccSzCnt(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetWccSzCnt, 0, TIntPrV)


    _GetNodeWcc = GetNodeWcc
    def GetNodeWcc(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetNodeWcc, 1, TIntV)


    _Get1CnCom = Get1CnCom
    def Get1CnCom(Graph, *args):
        return MoveArgToReturn(Graph, args, _Get1CnCom, 0, TCnComV)


    _Get1CnComSzCnt = Get1CnComSzCnt
    def Get1CnComSzCnt(Graph, *args):
        return MoveArgToReturn(Graph, args, _Get1CnComSzCnt, 0, TIntPrV)


    _GetBiCon = GetBiCon
    def GetBiCon(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetBiCon, 0, TCnComV)


    _GetBiConSzCnt = GetBiConSzCnt
    def GetBiConSzCnt(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetBiConSzCnt, 0, TIntPrV)


    _GetArtPoints = GetArtPoints
    def GetArtPoints(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetArtPoints, 0, TIntV)


    _GetEdgeBridges = GetEdgeBridges
    def GetEdgeBridges(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetEdgeBridges, 0, TIntPrV)


    _GetNodesAtHop = GetNodesAtHop
    def GetNodesAtHop(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetNodesAtHop, 2, TIntV)


    _GetNodesAtHops = GetNodesAtHops
    def GetNodesAtHops(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetNodesAtHops, 1, TIntPrV)


    def GetShortPathAll(Graph, SrcNId, IsDir = False, MaxDist=TInt.Mx):
        NIdToDistH = TIntH()
        GetShortPath(Graph, SrcNId, NIdToDistH, IsDir, MaxDist)
        return NIdToDistH


    _GetTreeSig = GetTreeSig
    def GetTreeSig(Graph, RootNId, Sig, NodeMap = False):
        if NodeMap:
            map = TIntPrV()
            sig = TIntV()
            _GetTreeSig(Graph, RootNId, sig, map)
            return (sig, map)
        else:
            sig = TIntV()
            _GetTreeSig(Graph, RootNId, sig)
            return sig


    _GetBetweennessCentr = GetBetweennessCentr
    def GetBetweennessCentr(Graph, *args):
        if len(args)>=1 and type(args[0]) == TIntFltH and type(args[1]) == TIntPrFltH:
            #Backward compatibility
            return _GetBetweennessCentr(Graph, *args)
        else:
            NIdBtwH = TIntFltH()
            EdgeBtwH = TIntPrFltH()
            _GetBetweennessCentr (Graph, NIdBtwH, EdgeBtwH, NodeFrac, IsDir)
            return (NIdBtwH, EdgeBtwH)


    _GetPageRank = GetPageRank
    def GetPageRank(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetPageRank, 0, TIntFltH)


    _GetHits = GetHits
    def GetHits(Graph, *args, **kwargs):
        if len(args) >= 2 and (type(args[0]) == TIntFltH) and (type(args[1]) == TIntFltH):
            #Backward compatibility
            return _GetHits(Graph, *args)
        else:
            if len(args) == 1:
                MaxIter = args[0]
            elif "MaxIter" in kwargs:
                MaxIter = kwargs["MaxIter"]
            else:
                #Default value for MaxIter is 20
                MaxIter = 20
                NIdHubH = TIntFltH()
                NIdAuthH = TIntFltH()
                _GetHits(Graph, MaxIter)
                return (NIdHubH, NIdAuthH)


    _GetEigenVectorCentr = GetEigenVectorCentr
    def GetEigenVectorCentr(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetEigenVectorCentr, 0, TIntFltH)


    _CommunityCNM = CommunityCNM
    def CommunityCNM(Graph, *args):
        return MoveArgToReturn(Graph, args, _CommunityCNM, 0, TCnComV)


    _CommunityGirvanNewman = CommunityGirvanNewman
    def CommunityGirvanNewman(Graph, *args):
        return MoveArgToReturn(Graph, args, _CommunityGirvanNewman, 0, TCnComV)


    _GetEdgesInOut = GetEdgesInOut
    def GetEdgesInOut(Graph, *args):
        args = ConvertToSnapType(args, 0, TIntV, list)
        return _GetEdgesInOut(Graph, *args)


    _GetModularity = GetModularity
    def GetModularity(Graph, *args):
        args = ConvertToSnapType(args, 0, TIntV, list)
        return _GetModularity(Graph, *args)


    _GetClustCf = GetClustCf
    def GetClustCf(Graph, *args, **kwargs):
        if len(args) == 2 and (type(args[0]) == TFltPrV):
            #Backward compatibility
            return _GetClustCf(Graph, *args)
        if len(args) == 1 and (type(args[0]) == int or type(args[0]) == TFltPrV):
            #Backward compatibility
            return _GetClustCf(Graph, *args)

        #Default argument values
        CCfByDeg = False
        SampleNodes = -1

        #Populate argument values
        if 'CCfByDeg' in kwargs:
            CCfByDeg = kwargs['CCfByDeg']
        if 'SampleNodes' in kwargs:
            SampleNodes = kwargs['SampleNodes']
        if len(args) == 1:
            CCfByDeg = args[0]
        if len(args) == 2:
            CCfByDeg = args[0]
            SampleNodes = args[1]

        if CCfByDeg:
            DegToCCfV = TFltPrV()
            PrevReturn = _GetClustCf(Graph, DegToCCfV, SampleNodes)
            return (PrevReturn, DegToCCfV)
        else:
            return _GetClustCf(Graph, SampleNodes)        


    _GetCmnNbrs = GetCmnNbrs
    def GetCmnNbrs(Graph, NId1, NId2, NbrList = False):
        if NbrList:
            NbrV = TIntV()
            PrevReturn = _GetCmnNbrs(Graph, NId1, NId2, NbrV)
            return (PrevReturn, NbrV)
        else:
            return _GetCmnNbrs(Graph, NId1, NId2)

    def GetNodeClustCfAll(Graph):
        NIdCCfH = TIntFltH()
        GetNodeClustCf(Graph, NIdCCfH)
        return NIdCCfH


    _GetNodeTriads = GetNodeTriads
    def GetNodeTriads(Graph, *args):
        if len(args) == 2:
            args = ConvertToSnapType(args, 1, TIntSet, set)
        return _GetNodeTriads(Graph, *args)


    _GetTriadParticip = GetTriadParticip
    def GetTriadParticip(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetTriadParticip, 0, TIntPrV)


    _GetKCoreNodes = GetKCoreNodes
    def GetKCoreNodes(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetKCoreNodes, 0, TIntPrV)


    _GetKCoreEdges = GetKCoreEdges
    def GetKCoreEdges(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetKCoreEdges, 0, TIntPrV)


    _GetEigVals = GetEigVals
    def GetEigVals(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetEigVals, 1, TFltV)


    _GetSngVals = GetSngVals
    def GetSngVals(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetSngVals, 1, TFltV)


    _GetInvParticipRat = GetInvParticipRat
    def GetInvParticipRat(Graph, *args):
        return MoveArgToReturn(Graph, args, _GetInvParticipRat, 2, TFltPrV)

    def GetLeadEigVec(Graph):
        EigVec = TFltV()
        GetEigVec(Graph, EigVec)
        return EigVec


    def GetEigVecs(Graph, EigVecs):
        EigVal = TFltV()
        EigVecV = TFltVFltV()
        GetEigVec(Graph, EigVecs, EigVal, EigVecV)
        return (EigVal, EigVecV)


    def GetLeadSngVec(Graph):
        LeftSV = TFltV()
        RightSV = TFltV()
        GetSngVec(Graph, LeftSV, RightSV)
        return (LeftSV, RightSV)


    def GetSngVecs(Graph, SngVecs):
        SngValV = TFltV()
        LeftSV = TFltVFltV()
        RightSV = TFltVFltV()
        GetSngVec(Graph, SngVecs, SngValV, LeftSV, RightSV)
        return (SngValV, LeftSV, RightSV)
%}


// Add class functions

%pythoncode %{
# Add class functions

    def CntDegNodes_classFn(self, *args, **kwargs):
        return CntDegNodes(self, *args, **kwargs)
    PUNGraph.CntDegNodes = CntDegNodes_classFn
    PNGraph.CntDegNodes = CntDegNodes_classFn
    PNEANet.CntDegNodes = CntDegNodes_classFn

    def CntInDegNodes_classFn(self, *args, **kwargs):
        return CntInDegNodes(self, *args, **kwargs)
    PUNGraph.CntInDegNodes = CntInDegNodes_classFn
    PNGraph.CntInDegNodes = CntInDegNodes_classFn
    PNEANet.CntInDegNodes = CntInDegNodes_classFn

    def CntOutDegNodes_classFn(self, *args, **kwargs):
        return CntOutDegNodes(self, *args, **kwargs)
    PUNGraph.CntOutDegNodes = CntOutDegNodes_classFn
    PNGraph.CntOutDegNodes = CntOutDegNodes_classFn
    PNEANet.CntOutDegNodes = CntOutDegNodes_classFn

    def CntNonZNodes_classFn(self, *args, **kwargs):
        return CntNonZNodes(self, *args, **kwargs)
    PUNGraph.CntNonZNodes = CntNonZNodes_classFn
    PNGraph.CntNonZNodes = CntNonZNodes_classFn
    PNEANet.CntNonZNodes = CntNonZNodes_classFn

    def GetDegCnt_classFn(self, *args, **kwargs):
        return GetDegCnt(self, *args, **kwargs)
    PUNGraph.GetDegCnt = GetDegCnt_classFn
    PNGraph.GetDegCnt = GetDegCnt_classFn
    PNEANet.GetDegCnt = GetDegCnt_classFn

    def GetInDegCnt_classFn(self, *args, **kwargs):
        return GetInDegCnt(self, *args, **kwargs)
    PUNGraph.GetInDegCnt = GetInDegCnt_classFn
    PNGraph.GetInDegCnt = GetInDegCnt_classFn
    PNEANet.GetInDegCnt = GetInDegCnt_classFn

    def GetOutDegCnt_classFn(self, *args, **kwargs):
        return GetOutDegCnt(self, *args, **kwargs)
    PUNGraph.GetOutDegCnt = GetOutDegCnt_classFn
    PNGraph.GetOutDegCnt = GetOutDegCnt_classFn
    PNEANet.GetOutDegCnt = GetOutDegCnt_classFn

    def GetMxDegNId_classFn(self, *args, **kwargs):
        return GetMxDegNId(self, *args, **kwargs)
    PUNGraph.GetMxDegNId = GetMxDegNId_classFn
    PNGraph.GetMxDegNId = GetMxDegNId_classFn
    PNEANet.GetMxDegNId = GetMxDegNId_classFn

    def GetMxInDegNId_classFn(self, *args, **kwargs):
        return GetMxInDegNId(self, *args, **kwargs)
    PUNGraph.GetMxInDegNId = GetMxInDegNId_classFn
    PNGraph.GetMxInDegNId = GetMxInDegNId_classFn
    PNEANet.GetMxInDegNId = GetMxInDegNId_classFn

    def GetMxOutDegNId_classFn(self, *args, **kwargs):
        return GetMxOutDegNId(self, *args, **kwargs)
    PUNGraph.GetMxOutDegNId = GetMxOutDegNId_classFn
    PNGraph.GetMxOutDegNId = GetMxOutDegNId_classFn
    PNEANet.GetMxOutDegNId = GetMxOutDegNId_classFn

    def GetNodeInDegV_classFn(self, *args, **kwargs):
        return GetNodeInDegV(self, *args, **kwargs)
    PUNGraph.GetNodeInDegV = GetNodeInDegV_classFn
    PNGraph.GetNodeInDegV = GetNodeInDegV_classFn
    PNEANet.GetNodeInDegV = GetNodeInDegV_classFn

    def GetNodeOutDegV_classFn(self, *args, **kwargs):
        return GetNodeOutDegV(self, *args, **kwargs)
    PUNGraph.GetNodeOutDegV = GetNodeOutDegV_classFn
    PNGraph.GetNodeOutDegV = GetNodeOutDegV_classFn
    PNEANet.GetNodeOutDegV = GetNodeOutDegV_classFn

    def GetDegSeqV_classFn(self, *args, **kwargs):
        return GetDegSeqV(self, *args, **kwargs)
    PUNGraph.GetDegSeqV = GetDegSeqV_classFn
    PNGraph.GetDegSeqV = GetDegSeqV_classFn
    PNEANet.GetDegSeqV = GetDegSeqV_classFn

    def CntSelfEdges_classFn(self, *args, **kwargs):
        return CntSelfEdges(self, *args, **kwargs)
    PUNGraph.CntSelfEdges = CntSelfEdges_classFn
    PNGraph.CntSelfEdges = CntSelfEdges_classFn
    PNEANet.CntSelfEdges = CntSelfEdges_classFn

    def CntUniqBiDirEdges_classFn(self, *args, **kwargs):
        return CntUniqBiDirEdges(self, *args, **kwargs)
    PUNGraph.CntUniqBiDirEdges = CntUniqBiDirEdges_classFn
    PNGraph.CntUniqBiDirEdges = CntUniqBiDirEdges_classFn
    PNEANet.CntUniqBiDirEdges = CntUniqBiDirEdges_classFn

    def CntUniqDirEdges_classFn(self, *args, **kwargs):
        return CntUniqDirEdges(self, *args, **kwargs)
    PUNGraph.CntUniqDirEdges = CntUniqDirEdges_classFn
    PNGraph.CntUniqDirEdges = CntUniqDirEdges_classFn
    PNEANet.CntUniqDirEdges = CntUniqDirEdges_classFn

    def CntUniqUndirEdges_classFn(self, *args, **kwargs):
        return CntUniqUndirEdges(self, *args, **kwargs)
    PUNGraph.CntUniqUndirEdges = CntUniqUndirEdges_classFn
    PNGraph.CntUniqUndirEdges = CntUniqUndirEdges_classFn
    PNEANet.CntUniqUndirEdges = CntUniqUndirEdges_classFn

    def CntEdgesToSet_classFn(self, *args, **kwargs):
        return CntEdgesToSet(self, *args, **kwargs)
    PUNGraph.CntEdgesToSet = CntEdgesToSet_classFn
    PNGraph.CntEdgesToSet = CntEdgesToSet_classFn
    PNEANet.CntEdgesToSet = CntEdgesToSet_classFn

    def AddSelfEdges_classFn(self, *args, **kwargs):
        return AddSelfEdges(self, *args, **kwargs)
    PUNGraph.AddSelfEdges = AddSelfEdges_classFn
    PNGraph.AddSelfEdges = AddSelfEdges_classFn
    PNEANet.AddSelfEdges = AddSelfEdges_classFn

    def DelDegKNodes_classFn(self, *args, **kwargs):
        return DelDegKNodes(self, *args, **kwargs)
    PUNGraph.DelDegKNodes = DelDegKNodes_classFn
    PNGraph.DelDegKNodes = DelDegKNodes_classFn
    PNEANet.DelDegKNodes = DelDegKNodes_classFn

    def DelNodes_classFn(self, *args, **kwargs):
        return DelNodes(self, *args, **kwargs)
    PUNGraph.DelNodes = DelNodes_classFn
    PNGraph.DelNodes = DelNodes_classFn
    PNEANet.DelNodes = DelNodes_classFn

    def DelSelfEdges_classFn(self, *args, **kwargs):
        return DelSelfEdges(self, *args, **kwargs)
    PUNGraph.DelSelfEdges = DelSelfEdges_classFn
    PNGraph.DelSelfEdges = DelSelfEdges_classFn
    PNEANet.DelSelfEdges = DelSelfEdges_classFn

    def DelZeroDegNodes_classFn(self, *args, **kwargs):
        return DelZeroDegNodes(self, *args, **kwargs)
    PUNGraph.DelZeroDegNodes = DelZeroDegNodes_classFn
    PNGraph.DelZeroDegNodes = DelZeroDegNodes_classFn
    PNEANet.DelZeroDegNodes = DelZeroDegNodes_classFn

    def GetUnDir_classFn(self, *args, **kwargs):
        return GetUnDir(self, *args, **kwargs)
    PUNGraph.GetUnDir = GetUnDir_classFn
    PNGraph.GetUnDir = GetUnDir_classFn
    PNEANet.GetUnDir = GetUnDir_classFn

    def MakeUnDir_classFn(self, *args, **kwargs):
        return MakeUnDir(self, *args, **kwargs)
    PUNGraph.MakeUnDir = MakeUnDir_classFn
    PNGraph.MakeUnDir = MakeUnDir_classFn
    PNEANet.MakeUnDir = MakeUnDir_classFn

    def ConvertGraph_classFn(self, *args, **kwargs):
        return ConvertGraph(self, *args, **kwargs)
    PUNGraph.ConvertGraph = ConvertGraph_classFn
    PNGraph.ConvertGraph = ConvertGraph_classFn
    PNEANet.ConvertGraph = ConvertGraph_classFn

    def ConvertSubGraph_classFn(self, *args, **kwargs):
        return ConvertSubGraph(self, *args, **kwargs)
    PUNGraph.ConvertSubGraph = ConvertSubGraph_classFn
    PNGraph.ConvertSubGraph = ConvertSubGraph_classFn
    PNEANet.ConvertSubGraph = ConvertSubGraph_classFn

    def ConvertESubGraph_classFn(self, *args, **kwargs):
        return ConvertESubGraph(self, *args, **kwargs)
    PUNGraph.ConvertESubGraph = ConvertESubGraph_classFn
    PNGraph.ConvertESubGraph = ConvertESubGraph_classFn
    PNEANet.ConvertESubGraph = ConvertESubGraph_classFn

    def GetSubGraph_classFn(self, *args, **kwargs):
        return GetSubGraph(self, *args, **kwargs)
    PUNGraph.GetSubGraph = GetSubGraph_classFn
    PNGraph.GetSubGraph = GetSubGraph_classFn
    PNEANet.GetSubGraph = GetSubGraph_classFn

    def GetSubGraphRenumber_classFn(self, *args, **kwargs):
        return GetSubGraphRenumber(self, *args, **kwargs)
    PUNGraph.GetSubGraphRenumber = GetSubGraphRenumber_classFn
    PNGraph.GetSubGraphRenumber = GetSubGraphRenumber_classFn
    PNEANet.GetSubGraphRenumber = GetSubGraphRenumber_classFn

    def GetSubTreeSz_classFn(self, *args, **kwargs):
        return GetSubTreeSz(self, *args, **kwargs)
    PUNGraph.GetSubTreeSz = GetSubTreeSz_classFn
    PNGraph.GetSubTreeSz = GetSubTreeSz_classFn
    PNEANet.GetSubTreeSz = GetSubTreeSz_classFn

    def GetESubGraph_classFn(self, *args, **kwargs):
        return GetESubGraph(self, *args, **kwargs)
    PUNGraph.GetESubGraph = GetESubGraph_classFn
    PNGraph.GetESubGraph = GetESubGraph_classFn
    PNEANet.GetESubGraph = GetESubGraph_classFn

    def GetRndSubGraph_classFn(self, *args, **kwargs):
        return GetRndSubGraph(self, *args, **kwargs)
    PUNGraph.GetRndSubGraph = GetRndSubGraph_classFn
    PNGraph.GetRndSubGraph = GetRndSubGraph_classFn
    PNEANet.GetRndSubGraph = GetRndSubGraph_classFn

    def GetRndESubGraph_classFn(self, *args, **kwargs):
        return GetRndESubGraph(self, *args, **kwargs)
    PUNGraph.GetRndESubGraph = GetRndESubGraph_classFn
    PNGraph.GetRndESubGraph = GetRndESubGraph_classFn
    PNEANet.GetRndESubGraph = GetRndESubGraph_classFn

    def IsTree_classFn(self, *args, **kwargs):
        return IsTree(self, *args, **kwargs)
    PUNGraph.IsTree = IsTree_classFn
    PNGraph.IsTree = IsTree_classFn
    PNEANet.IsTree = IsTree_classFn

    def PrintInfo_classFn(self, *args, **kwargs):
        return PrintInfo(self, *args, **kwargs)
    PUNGraph.PrintInfo = PrintInfo_classFn
    PNGraph.PrintInfo = PrintInfo_classFn
    PNEANet.PrintInfo = PrintInfo_classFn

    def DrawGViz_classFn(self, *args, **kwargs):
        return DrawGViz(self, *args, **kwargs)
    PUNGraph.DrawGViz = DrawGViz_classFn
    PNGraph.DrawGViz = DrawGViz_classFn
    PNEANet.DrawGViz = DrawGViz_classFn

    def DrawGViz_classFn(self, *args, **kwargs):
        return DrawGViz(self, *args, **kwargs)
    PUNGraph.DrawGViz = DrawGViz_classFn
    PNGraph.DrawGViz = DrawGViz_classFn
    PNEANet.DrawGViz = DrawGViz_classFn

    def PlotSccDistr_classFn(self, *args, **kwargs):
        return PlotSccDistr(self, *args, **kwargs)
    PUNGraph.PlotSccDistr = PlotSccDistr_classFn
    PNGraph.PlotSccDistr = PlotSccDistr_classFn
    PNEANet.PlotSccDistr = PlotSccDistr_classFn

    def PlotWccDistr_classFn(self, *args, **kwargs):
        return PlotWccDistr(self, *args, **kwargs)
    PUNGraph.PlotWccDistr = PlotWccDistr_classFn
    PNGraph.PlotWccDistr = PlotWccDistr_classFn
    PNEANet.PlotWccDistr = PlotWccDistr_classFn

    def PlotClustCf_classFn(self, *args, **kwargs):
        return PlotClustCf(self, *args, **kwargs)
    PUNGraph.PlotClustCf = PlotClustCf_classFn
    PNGraph.PlotClustCf = PlotClustCf_classFn
    PNEANet.PlotClustCf = PlotClustCf_classFn

    def PlotInDegDistr_classFn(self, *args, **kwargs):
        return PlotInDegDistr(self, *args, **kwargs)
    PUNGraph.PlotInDegDistr = PlotInDegDistr_classFn
    PNGraph.PlotInDegDistr = PlotInDegDistr_classFn
    PNEANet.PlotInDegDistr = PlotInDegDistr_classFn

    def PlotOutDegDistr_classFn(self, *args, **kwargs):
        return PlotOutDegDistr(self, *args, **kwargs)
    PUNGraph.PlotOutDegDistr = PlotOutDegDistr_classFn
    PNGraph.PlotOutDegDistr = PlotOutDegDistr_classFn
    PNEANet.PlotOutDegDistr = PlotOutDegDistr_classFn

    def PlotHops_classFn(self, *args, **kwargs):
        return PlotHops(self, *args, **kwargs)
    PUNGraph.PlotHops = PlotHops_classFn
    PNGraph.PlotHops = PlotHops_classFn
    PNEANet.PlotHops = PlotHops_classFn

    def PlotShortPathDistr_classFn(self, *args, **kwargs):
        return PlotShortPathDistr(self, *args, **kwargs)
    PUNGraph.PlotShortPathDistr = PlotShortPathDistr_classFn
    PNGraph.PlotShortPathDistr = PlotShortPathDistr_classFn
    PNEANet.PlotShortPathDistr = PlotShortPathDistr_classFn

    def PlotEigValDistr_classFn(self, *args, **kwargs):
        return PlotEigValDistr(self, *args, **kwargs)
    PUNGraph.PlotEigValDistr = PlotEigValDistr_classFn
    PNGraph.PlotEigValDistr = PlotEigValDistr_classFn
    PNEANet.PlotEigValDistr = PlotEigValDistr_classFn

    def PlotEigValRank_classFn(self, *args, **kwargs):
        return PlotEigValRank(self, *args, **kwargs)
    PUNGraph.PlotEigValRank = PlotEigValRank_classFn
    PNGraph.PlotEigValRank = PlotEigValRank_classFn
    PNEANet.PlotEigValRank = PlotEigValRank_classFn

    def PlotSngValDistr_classFn(self, *args, **kwargs):
        return PlotSngValDistr(self, *args, **kwargs)
    PUNGraph.PlotSngValDistr = PlotSngValDistr_classFn
    PNGraph.PlotSngValDistr = PlotSngValDistr_classFn
    PNEANet.PlotSngValDistr = PlotSngValDistr_classFn

    def PlotSngValRank_classFn(self, *args, **kwargs):
        return PlotSngValRank(self, *args, **kwargs)
    PUNGraph.PlotSngValRank = PlotSngValRank_classFn
    PNGraph.PlotSngValRank = PlotSngValRank_classFn
    PNEANet.PlotSngValRank = PlotSngValRank_classFn

    def PlotSngVec_classFn(self, *args, **kwargs):
        return PlotSngVec(self, *args, **kwargs)
    PUNGraph.PlotSngVec = PlotSngVec_classFn
    PNGraph.PlotSngVec = PlotSngVec_classFn
    PNEANet.PlotSngVec = PlotSngVec_classFn

    def PlotInvParticipRat_classFn(self, *args, **kwargs):
        return PlotInvParticipRat(self, *args, **kwargs)
    PUNGraph.PlotInvParticipRat = PlotInvParticipRat_classFn
    PNGraph.PlotInvParticipRat = PlotInvParticipRat_classFn
    PNEANet.PlotInvParticipRat = PlotInvParticipRat_classFn

    def PlotKCoreEdges_classFn(self, *args, **kwargs):
        return PlotKCoreEdges(self, *args, **kwargs)
    PUNGraph.PlotKCoreEdges = PlotKCoreEdges_classFn
    PNGraph.PlotKCoreEdges = PlotKCoreEdges_classFn
    PNEANet.PlotKCoreEdges = PlotKCoreEdges_classFn

    def PlotKCoreNodes_classFn(self, *args, **kwargs):
        return PlotKCoreNodes(self, *args, **kwargs)
    PUNGraph.PlotKCoreNodes = PlotKCoreNodes_classFn
    PNGraph.PlotKCoreNodes = PlotKCoreNodes_classFn
    PNEANet.PlotKCoreNodes = PlotKCoreNodes_classFn

    def GetSccs_classFn(self, *args, **kwargs):
        return GetSccs(self, *args, **kwargs)
    PUNGraph.GetSccs = GetSccs_classFn
    PNGraph.GetSccs = GetSccs_classFn
    PNEANet.GetSccs = GetSccs_classFn

    def GetSccSzCnt_classFn(self, *args, **kwargs):
        return GetSccSzCnt(self, *args, **kwargs)
    PUNGraph.GetSccSzCnt = GetSccSzCnt_classFn
    PNGraph.GetSccSzCnt = GetSccSzCnt_classFn
    PNEANet.GetSccSzCnt = GetSccSzCnt_classFn

    def GetWccs_classFn(self, *args, **kwargs):
        return GetWccs(self, *args, **kwargs)
    PUNGraph.GetWccs = GetWccs_classFn
    PNGraph.GetWccs = GetWccs_classFn
    PNEANet.GetWccs = GetWccs_classFn

    def GetWccSzCnt_classFn(self, *args, **kwargs):
        return GetWccSzCnt(self, *args, **kwargs)
    PUNGraph.GetWccSzCnt = GetWccSzCnt_classFn
    PNGraph.GetWccSzCnt = GetWccSzCnt_classFn
    PNEANet.GetWccSzCnt = GetWccSzCnt_classFn

    def GetMxBiCon_classFn(self, *args, **kwargs):
        return GetMxBiCon(self, *args, **kwargs)
    PUNGraph.GetMxBiCon = GetMxBiCon_classFn
    PNGraph.GetMxBiCon = GetMxBiCon_classFn
    PNEANet.GetMxBiCon = GetMxBiCon_classFn

    def GetMxScc_classFn(self, *args, **kwargs):
        return GetMxScc(self, *args, **kwargs)
    PUNGraph.GetMxScc = GetMxScc_classFn
    PNGraph.GetMxScc = GetMxScc_classFn
    PNEANet.GetMxScc = GetMxScc_classFn

    def GetMxSccSz_classFn(self, *args, **kwargs):
        return GetMxSccSz(self, *args, **kwargs)
    PUNGraph.GetMxSccSz = GetMxSccSz_classFn
    PNGraph.GetMxSccSz = GetMxSccSz_classFn
    PNEANet.GetMxSccSz = GetMxSccSz_classFn

    def GetMxWcc_classFn(self, *args, **kwargs):
        return GetMxWcc(self, *args, **kwargs)
    PUNGraph.GetMxWcc = GetMxWcc_classFn
    PNGraph.GetMxWcc = GetMxWcc_classFn
    PNEANet.GetMxWcc = GetMxWcc_classFn

    def GetMxWccSz_classFn(self, *args, **kwargs):
        return GetMxWccSz(self, *args, **kwargs)
    PUNGraph.GetMxWccSz = GetMxWccSz_classFn
    PNGraph.GetMxWccSz = GetMxWccSz_classFn
    PNEANet.GetMxWccSz = GetMxWccSz_classFn

    def IsConnected_classFn(self, *args, **kwargs):
        return IsConnected(self, *args, **kwargs)
    PUNGraph.IsConnected = IsConnected_classFn
    PNGraph.IsConnected = IsConnected_classFn
    PNEANet.IsConnected = IsConnected_classFn

    def IsWeaklyConn_classFn(self, *args, **kwargs):
        return IsWeaklyConn(self, *args, **kwargs)
    PUNGraph.IsWeaklyConn = IsWeaklyConn_classFn
    PNGraph.IsWeaklyConn = IsWeaklyConn_classFn
    PNEANet.IsWeaklyConn = IsWeaklyConn_classFn

    def GetNodeWcc_classFn(self, *args, **kwargs):
        return GetNodeWcc(self, *args, **kwargs)
    PUNGraph.GetNodeWcc = GetNodeWcc_classFn
    PNGraph.GetNodeWcc = GetNodeWcc_classFn
    PNEANet.GetNodeWcc = GetNodeWcc_classFn

    def Get1CnCom_classFn(self, *args, **kwargs):
        return Get1CnCom(self, *args, **kwargs)
    PUNGraph.Get1CnCom = Get1CnCom_classFn
    PNGraph.Get1CnCom = Get1CnCom_classFn
    PNEANet.Get1CnCom = Get1CnCom_classFn

    def Get1CnComSzCnt_classFn(self, *args, **kwargs):
        return Get1CnComSzCnt(self, *args, **kwargs)
    PUNGraph.Get1CnComSzCnt = Get1CnComSzCnt_classFn
    PNGraph.Get1CnComSzCnt = Get1CnComSzCnt_classFn
    PNEANet.Get1CnComSzCnt = Get1CnComSzCnt_classFn

    def GetBiCon_classFn(self, *args, **kwargs):
        return GetBiCon(self, *args, **kwargs)
    PUNGraph.GetBiCon = GetBiCon_classFn
    PNGraph.GetBiCon = GetBiCon_classFn
    PNEANet.GetBiCon = GetBiCon_classFn

    def GetBiConSzCnt_classFn(self, *args, **kwargs):
        return GetBiConSzCnt(self, *args, **kwargs)
    PUNGraph.GetBiConSzCnt = GetBiConSzCnt_classFn
    PNGraph.GetBiConSzCnt = GetBiConSzCnt_classFn
    PNEANet.GetBiConSzCnt = GetBiConSzCnt_classFn

    def GetArtPoints_classFn(self, *args, **kwargs):
        return GetArtPoints(self, *args, **kwargs)
    PUNGraph.GetArtPoints = GetArtPoints_classFn
    PNGraph.GetArtPoints = GetArtPoints_classFn
    PNEANet.GetArtPoints = GetArtPoints_classFn

    def GetEdgeBridges_classFn(self, *args, **kwargs):
        return GetEdgeBridges(self, *args, **kwargs)
    PUNGraph.GetEdgeBridges = GetEdgeBridges_classFn
    PNGraph.GetEdgeBridges = GetEdgeBridges_classFn
    PNEANet.GetEdgeBridges = GetEdgeBridges_classFn

    def GetBfsFullDiam_classFn(self, *args, **kwargs):
        return GetBfsFullDiam(self, *args, **kwargs)
    PUNGraph.GetBfsFullDiam = GetBfsFullDiam_classFn
    PNGraph.GetBfsFullDiam = GetBfsFullDiam_classFn
    PNEANet.GetBfsFullDiam = GetBfsFullDiam_classFn

    def GetBfsEffDiam_classFn(self, *args, **kwargs):
        return GetBfsEffDiam(self, *args, **kwargs)
    PUNGraph.GetBfsEffDiam = GetBfsEffDiam_classFn
    PNGraph.GetBfsEffDiam = GetBfsEffDiam_classFn
    PNEANet.GetBfsEffDiam = GetBfsEffDiam_classFn

    def GetBfsEffDiam_classFn(self, *args, **kwargs):
        return GetBfsEffDiam(self, *args, **kwargs)
    PUNGraph.GetBfsEffDiam = GetBfsEffDiam_classFn
    PNGraph.GetBfsEffDiam = GetBfsEffDiam_classFn
    PNEANet.GetBfsEffDiam = GetBfsEffDiam_classFn

    def GetBfsEffDiamAll_classFn(self, *args, **kwargs):
        return GetBfsEffDiamAll(self, *args, **kwargs)
    PUNGraph.GetBfsEffDiamAll = GetBfsEffDiamAll_classFn
    PNGraph.GetBfsEffDiamAll = GetBfsEffDiamAll_classFn
    PNEANet.GetBfsEffDiamAll = GetBfsEffDiamAll_classFn

    def GetNodesAtHop_classFn(self, *args, **kwargs):
        return GetNodesAtHop(self, *args, **kwargs)
    PUNGraph.GetNodesAtHop = GetNodesAtHop_classFn
    PNGraph.GetNodesAtHop = GetNodesAtHop_classFn
    PNEANet.GetNodesAtHop = GetNodesAtHop_classFn

    def GetNodesAtHops_classFn(self, *args, **kwargs):
        return GetNodesAtHops(self, *args, **kwargs)
    PUNGraph.GetNodesAtHops = GetNodesAtHops_classFn
    PNGraph.GetNodesAtHops = GetNodesAtHops_classFn
    PNEANet.GetNodesAtHops = GetNodesAtHops_classFn

    def GetShortPath_classFn(self, *args, **kwargs):
        return GetShortPath(self, *args, **kwargs)
    PUNGraph.GetShortPath = GetShortPath_classFn
    PNGraph.GetShortPath = GetShortPath_classFn
    PNEANet.GetShortPath = GetShortPath_classFn

    def GetShortPath_classFn(self, *args, **kwargs):
        return GetShortPath(self, *args, **kwargs)
    PUNGraph.GetShortPath = GetShortPath_classFn
    PNGraph.GetShortPath = GetShortPath_classFn
    PNEANet.GetShortPath = GetShortPath_classFn

    def GetBfsTree_classFn(self, *args, **kwargs):
        return GetBfsTree(self, *args, **kwargs)
    PUNGraph.GetBfsTree = GetBfsTree_classFn
    PNGraph.GetBfsTree = GetBfsTree_classFn
    PNEANet.GetBfsTree = GetBfsTree_classFn

    def GetTreeRootNId_classFn(self, *args, **kwargs):
        return GetTreeRootNId(self, *args, **kwargs)
    PUNGraph.GetTreeRootNId = GetTreeRootNId_classFn
    PNGraph.GetTreeRootNId = GetTreeRootNId_classFn
    PNEANet.GetTreeRootNId = GetTreeRootNId_classFn

    def GetTreeSig_classFn(self, *args, **kwargs):
        return GetTreeSig(self, *args, **kwargs)
    PUNGraph.GetTreeSig = GetTreeSig_classFn
    PNGraph.GetTreeSig = GetTreeSig_classFn
    PNEANet.GetTreeSig = GetTreeSig_classFn

    def GetTreeSig_classFn(self, *args, **kwargs):
        return GetTreeSig(self, *args, **kwargs)
    PUNGraph.GetTreeSig = GetTreeSig_classFn
    PNGraph.GetTreeSig = GetTreeSig_classFn
    PNEANet.GetTreeSig = GetTreeSig_classFn

    def GetDegreeCentr_classFn(self, *args, **kwargs):
        return GetDegreeCentr(self, *args, **kwargs)
    PUNGraph.GetDegreeCentr = GetDegreeCentr_classFn
    PNGraph.GetDegreeCentr = GetDegreeCentr_classFn
    PNEANet.GetDegreeCentr = GetDegreeCentr_classFn

    def GetBetweennessCentr_classFn(self, *args, **kwargs):
        return GetBetweennessCentr(self, *args, **kwargs)
    PUNGraph.GetBetweennessCentr = GetBetweennessCentr_classFn
    PNGraph.GetBetweennessCentr = GetBetweennessCentr_classFn
    PNEANet.GetBetweennessCentr = GetBetweennessCentr_classFn

    def GetClosenessCentr_classFn(self, *args, **kwargs):
        return GetClosenessCentr(self, *args, **kwargs)
    PUNGraph.GetClosenessCentr = GetClosenessCentr_classFn
    PNGraph.GetClosenessCentr = GetClosenessCentr_classFn
    PNEANet.GetClosenessCentr = GetClosenessCentr_classFn

    def GetFarnessCentr_classFn(self, *args, **kwargs):
        return GetFarnessCentr(self, *args, **kwargs)
    PUNGraph.GetFarnessCentr = GetFarnessCentr_classFn
    PNGraph.GetFarnessCentr = GetFarnessCentr_classFn
    PNEANet.GetFarnessCentr = GetFarnessCentr_classFn

    def GetPageRank_classFn(self, *args, **kwargs):
        return GetPageRank(self, *args, **kwargs)
    PUNGraph.GetPageRank = GetPageRank_classFn
    PNGraph.GetPageRank = GetPageRank_classFn
    PNEANet.GetPageRank = GetPageRank_classFn

    def GetHits_classFn(self, *args, **kwargs):
        return GetHits(self, *args, **kwargs)
    PUNGraph.GetHits = GetHits_classFn
    PNGraph.GetHits = GetHits_classFn
    PNEANet.GetHits = GetHits_classFn

    def GetNodeEcc_classFn(self, *args, **kwargs):
        return GetNodeEcc(self, *args, **kwargs)
    PUNGraph.GetNodeEcc = GetNodeEcc_classFn
    PNGraph.GetNodeEcc = GetNodeEcc_classFn
    PNEANet.GetNodeEcc = GetNodeEcc_classFn

    def GetEigenVectorCentr_classFn(self, *args, **kwargs):
        return GetEigenVectorCentr(self, *args, **kwargs)
    PUNGraph.GetEigenVectorCentr = GetEigenVectorCentr_classFn
    PNGraph.GetEigenVectorCentr = GetEigenVectorCentr_classFn
    PNEANet.GetEigenVectorCentr = GetEigenVectorCentr_classFn

    def CommunityCNM_classFn(self, *args, **kwargs):
        return CommunityCNM(self, *args, **kwargs)
    PUNGraph.CommunityCNM = CommunityCNM_classFn
    PNGraph.CommunityCNM = CommunityCNM_classFn
    PNEANet.CommunityCNM = CommunityCNM_classFn

    def CommunityGirvanNewman_classFn(self, *args, **kwargs):
        return CommunityGirvanNewman(self, *args, **kwargs)
    PUNGraph.CommunityGirvanNewman = CommunityGirvanNewman_classFn
    PNGraph.CommunityGirvanNewman = CommunityGirvanNewman_classFn
    PNEANet.CommunityGirvanNewman = CommunityGirvanNewman_classFn

    def GetEdgesInOut_classFn(self, *args, **kwargs):
        return GetEdgesInOut(self, *args, **kwargs)
    PUNGraph.GetEdgesInOut = GetEdgesInOut_classFn
    PNGraph.GetEdgesInOut = GetEdgesInOut_classFn
    PNEANet.GetEdgesInOut = GetEdgesInOut_classFn

    def GetModularity_classFn(self, *args, **kwargs):
        return GetModularity(self, *args, **kwargs)
    PUNGraph.GetModularity = GetModularity_classFn
    PNGraph.GetModularity = GetModularity_classFn
    PNEANet.GetModularity = GetModularity_classFn

    def GetClustCf_classFn(self, *args, **kwargs):
        return GetClustCf(self, *args, **kwargs)
    PUNGraph.GetClustCf = GetClustCf_classFn
    PNGraph.GetClustCf = GetClustCf_classFn
    PNEANet.GetClustCf = GetClustCf_classFn

    def GetClustCf_classFn(self, *args, **kwargs):
        return GetClustCf(self, *args, **kwargs)
    PUNGraph.GetClustCf = GetClustCf_classFn
    PNGraph.GetClustCf = GetClustCf_classFn
    PNEANet.GetClustCf = GetClustCf_classFn

    def GetClustCfAll_classFn(self, *args, **kwargs):
        return GetClustCfAll(self, *args, **kwargs)
    PUNGraph.GetClustCfAll = GetClustCfAll_classFn
    PNGraph.GetClustCfAll = GetClustCfAll_classFn
    PNEANet.GetClustCfAll = GetClustCfAll_classFn

    def GetTriads_classFn(self, *args, **kwargs):
        return GetTriads(self, *args, **kwargs)
    PUNGraph.GetTriads = GetTriads_classFn
    PNGraph.GetTriads = GetTriads_classFn
    PNEANet.GetTriads = GetTriads_classFn

    def GetTriads_classFn(self, *args, **kwargs):
        return GetTriads(self, *args, **kwargs)
    PUNGraph.GetTriads = GetTriads_classFn
    PNGraph.GetTriads = GetTriads_classFn
    PNEANet.GetTriads = GetTriads_classFn

    def GetTriadsAll_classFn(self, *args, **kwargs):
        return GetTriadsAll(self, *args, **kwargs)
    PUNGraph.GetTriadsAll = GetTriadsAll_classFn
    PNGraph.GetTriadsAll = GetTriadsAll_classFn
    PNEANet.GetTriadsAll = GetTriadsAll_classFn

    def GetCmnNbrs_classFn(self, *args, **kwargs):
        return GetCmnNbrs(self, *args, **kwargs)
    PUNGraph.GetCmnNbrs = GetCmnNbrs_classFn
    PNGraph.GetCmnNbrs = GetCmnNbrs_classFn
    PNEANet.GetCmnNbrs = GetCmnNbrs_classFn

    def GetCmnNbrs_classFn(self, *args, **kwargs):
        return GetCmnNbrs(self, *args, **kwargs)
    PUNGraph.GetCmnNbrs = GetCmnNbrs_classFn
    PNGraph.GetCmnNbrs = GetCmnNbrs_classFn
    PNEANet.GetCmnNbrs = GetCmnNbrs_classFn

    def GetNodeClustCf_classFn(self, *args, **kwargs):
        return GetNodeClustCf(self, *args, **kwargs)
    PUNGraph.GetNodeClustCf = GetNodeClustCf_classFn
    PNGraph.GetNodeClustCf = GetNodeClustCf_classFn
    PNEANet.GetNodeClustCf = GetNodeClustCf_classFn

    def GetNodeClustCf_classFn(self, *args, **kwargs):
        return GetNodeClustCf(self, *args, **kwargs)
    PUNGraph.GetNodeClustCf = GetNodeClustCf_classFn
    PNGraph.GetNodeClustCf = GetNodeClustCf_classFn
    PNEANet.GetNodeClustCf = GetNodeClustCf_classFn

    def GetNodeTriads_classFn(self, *args, **kwargs):
        return GetNodeTriads(self, *args, **kwargs)
    PUNGraph.GetNodeTriads = GetNodeTriads_classFn
    PNGraph.GetNodeTriads = GetNodeTriads_classFn
    PNEANet.GetNodeTriads = GetNodeTriads_classFn

    def GetNodeTriads_classFn(self, *args, **kwargs):
        return GetNodeTriads(self, *args, **kwargs)
    PUNGraph.GetNodeTriads = GetNodeTriads_classFn
    PNGraph.GetNodeTriads = GetNodeTriads_classFn
    PNEANet.GetNodeTriads = GetNodeTriads_classFn

    def GetNodeTriadsAll_classFn(self, *args, **kwargs):
        return GetNodeTriadsAll(self, *args, **kwargs)
    PUNGraph.GetNodeTriadsAll = GetNodeTriadsAll_classFn
    PNGraph.GetNodeTriadsAll = GetNodeTriadsAll_classFn
    PNEANet.GetNodeTriadsAll = GetNodeTriadsAll_classFn

    def GetLen2Path_classFn(self, *args, **kwargs):
        return GetLen2Path(self, *args, **kwargs)
    PUNGraph.GetLen2Path = GetLen2Path_classFn
    PNGraph.GetLen2Path = GetLen2Path_classFn
    PNEANet.GetLen2Path = GetLen2Path_classFn

    def GetLen2Paths_classFn(self, *args, **kwargs):
        return GetLen2Paths(self, *args, **kwargs)
    PUNGraph.GetLen2Paths = GetLen2Paths_classFn
    PNGraph.GetLen2Paths = GetLen2Paths_classFn
    PNEANet.GetLen2Paths = GetLen2Paths_classFn

    def GetTriadEdges_classFn(self, *args, **kwargs):
        return GetTriadEdges(self, *args, **kwargs)
    PUNGraph.GetTriadEdges = GetTriadEdges_classFn
    PNGraph.GetTriadEdges = GetTriadEdges_classFn
    PNEANet.GetTriadEdges = GetTriadEdges_classFn

    def GetTriadParticip_classFn(self, *args, **kwargs):
        return GetTriadParticip(self, *args, **kwargs)
    PUNGraph.GetTriadParticip = GetTriadParticip_classFn
    PNGraph.GetTriadParticip = GetTriadParticip_classFn
    PNEANet.GetTriadParticip = GetTriadParticip_classFn

    def GetKCore_classFn(self, *args, **kwargs):
        return GetKCore(self, *args, **kwargs)
    PUNGraph.GetKCore = GetKCore_classFn
    PNGraph.GetKCore = GetKCore_classFn
    PNEANet.GetKCore = GetKCore_classFn

    def GetKCoreNodes_classFn(self, *args, **kwargs):
        return GetKCoreNodes(self, *args, **kwargs)
    PUNGraph.GetKCoreNodes = GetKCoreNodes_classFn
    PNGraph.GetKCoreNodes = GetKCoreNodes_classFn
    PNEANet.GetKCoreNodes = GetKCoreNodes_classFn

    def GetKCoreEdges_classFn(self, *args, **kwargs):
        return GetKCoreEdges(self, *args, **kwargs)
    PUNGraph.GetKCoreEdges = GetKCoreEdges_classFn
    PNGraph.GetKCoreEdges = GetKCoreEdges_classFn
    PNEANet.GetKCoreEdges = GetKCoreEdges_classFn

    def GetAnf_classFn(self, *args, **kwargs):
        return GetAnf(self, *args, **kwargs)
    PUNGraph.GetAnf = GetAnf_classFn
    PNGraph.GetAnf = GetAnf_classFn
    PNEANet.GetAnf = GetAnf_classFn

    def GetAnf_classFn(self, *args, **kwargs):
        return GetAnf(self, *args, **kwargs)
    PUNGraph.GetAnf = GetAnf_classFn
    PNGraph.GetAnf = GetAnf_classFn
    PNEANet.GetAnf = GetAnf_classFn

    def GetAnfEffDiam_classFn(self, *args, **kwargs):
        return GetAnfEffDiam(self, *args, **kwargs)
    PUNGraph.GetAnfEffDiam = GetAnfEffDiam_classFn
    PNGraph.GetAnfEffDiam = GetAnfEffDiam_classFn
    PNEANet.GetAnfEffDiam = GetAnfEffDiam_classFn

    def GetAnfEffDiam_classFn(self, *args, **kwargs):
        return GetAnfEffDiam(self, *args, **kwargs)
    PUNGraph.GetAnfEffDiam = GetAnfEffDiam_classFn
    PNGraph.GetAnfEffDiam = GetAnfEffDiam_classFn
    PNEANet.GetAnfEffDiam = GetAnfEffDiam_classFn

    def GetEigVals_classFn(self, *args, **kwargs):
        return GetEigVals(self, *args, **kwargs)
    PUNGraph.GetEigVals = GetEigVals_classFn
    PNGraph.GetEigVals = GetEigVals_classFn
    PNEANet.GetEigVals = GetEigVals_classFn

    def GetEigVec_classFn(self, *args, **kwargs):
        return GetEigVec(self, *args, **kwargs)
    PUNGraph.GetEigVec = GetEigVec_classFn
    PNGraph.GetEigVec = GetEigVec_classFn
    PNEANet.GetEigVec = GetEigVec_classFn

    def GetEigVec_classFn(self, *args, **kwargs):
        return GetEigVec(self, *args, **kwargs)
    PUNGraph.GetEigVec = GetEigVec_classFn
    PNGraph.GetEigVec = GetEigVec_classFn
    PNEANet.GetEigVec = GetEigVec_classFn

    def GetSngVals_classFn(self, *args, **kwargs):
        return GetSngVals(self, *args, **kwargs)
    PUNGraph.GetSngVals = GetSngVals_classFn
    PNGraph.GetSngVals = GetSngVals_classFn
    PNEANet.GetSngVals = GetSngVals_classFn

    def GetSngVec_classFn(self, *args, **kwargs):
        return GetSngVec(self, *args, **kwargs)
    PUNGraph.GetSngVec = GetSngVec_classFn
    PNGraph.GetSngVec = GetSngVec_classFn
    PNEANet.GetSngVec = GetSngVec_classFn

    def GetSngVec_classFn(self, *args, **kwargs):
        return GetSngVec(self, *args, **kwargs)
    PUNGraph.GetSngVec = GetSngVec_classFn
    PNGraph.GetSngVec = GetSngVec_classFn
    PNEANet.GetSngVec = GetSngVec_classFn

    def GetInvParticipRat_classFn(self, *args, **kwargs):
        return GetInvParticipRat(self, *args, **kwargs)
    PUNGraph.GetInvParticipRat = GetInvParticipRat_classFn
    PNGraph.GetInvParticipRat = GetInvParticipRat_classFn
    PNEANet.GetInvParticipRat = GetInvParticipRat_classFn
%}
