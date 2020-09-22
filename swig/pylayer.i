//
// This file implements an additional layer over SWIG generated code in order
// to provide improved Python functionality. It includes the following
// enhancements, which are implemented where possible:
//
//  - standalone functions are available as class methods
//  - built-in Python classes (lists, dictionaries) are accepted as 
//    parameters in addition to SNAP C++ based classes
//  - function results are available as return values rather than as
//    reference parameters
//  - support for optional parameters has been enhanced
//

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

# This function converts TNGraph/TUNGraph/TNEANet to PNGraph/PUNGraph/PNEANet
def ConvertGraphArg(GraphType):
    if GraphType == TNGraph:
        GraphType = PNGraph
    elif GraphType == TUNGraph:
        GraphType = PUNGraph
    elif GraphType == TNEANet:
        GraphType = PNEANet
    return GraphType

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

_GenFull = GenFull
def GenFull(GraphType, *args):
    GraphType = ConvertGraphArg(GraphType)
    return _GenFull(GraphType, *args)

_GenCircle = GenCircle
def GenCircle(GraphType, *args):
    GraphType = ConvertGraphArg(GraphType)
    return _GenCircle(GraphType, *args)

_GenGrid = GenGrid
def GenGrid(GraphType, *args):
    GraphType = ConvertGraphArg(GraphType)
    return _GenGrid(GraphType, *args)

_GenStar = GenStar
def GenStar(GraphType, *args):
    GraphType = ConvertGraphArg(GraphType)
    return _GenStar(GraphType, *args)

_GenTree = GenTree
def GenTree(GraphType, *args):
    GraphType = ConvertGraphArg(GraphType)
    return _GenTree(GraphType, *args)

_GenRndGnm = GenRndGnm
def GenRndGnm(GraphType, *args):
    GraphType = ConvertGraphArg(GraphType)
    return _GenRndGnm(GraphType, *args)

_GenBaraHierar = GenBaraHierar
def GenBaraHierar(GraphType, *args):
    GraphType = ConvertGraphArg(GraphType)
    return _GenBaraHierar(GraphType, *args)

_LoadEdgeList = LoadEdgeList
def LoadEdgeList(GraphType, InFNm, SrcColId = 0, DstColId = 1, Separator = " "):
    GraphType = ConvertGraphArg(GraphType)
    if Separator == " ":
        return _LoadEdgeList(GraphType, InFNm, SrcColId, DstColId)
    else:
        return _LoadEdgeList(GraphType, InFNm, SrcColId, DstColId, Separator)

_LoadEdgeListStr = LoadEdgeListStr
def LoadEdgeListStr(GraphType, InFNm, SrcColId = 0, DstColId = 1, Mapping = None):
    GraphType = ConvertGraphArg(GraphType)
    if Mapping == None  or  Mapping == False:
        return _LoadEdgeListStr(GraphType, InFNm, SrcColId, DstColId)

    if Mapping == True:
        StrToNIdH = TStrIntSH()
        graph = _LoadEdgeListStr(GraphType, InFNm, SrcColId, DstColId, StrToNIdH)
        return (graph, StrToNIdH)

    return _LoadEdgeListStr(GraphType, InFNm, SrcColId, DstColId, Mapping)

_LoadConnList = LoadConnList
def LoadConnList(GraphType, *args):
    GraphType = ConvertGraphArg(GraphType)
    return _LoadConnList(GraphType, *args)

_LoadConnListStr = LoadConnListStr 
def LoadConnListStr(GraphType, *args):
    GraphType = ConvertGraphArg(GraphType)
    return MoveArgToReturn(GraphType, args, _LoadConnListStr, 1, TStrIntSH)

_LoadPajek = LoadPajek
def LoadPajek(GraphType, *args):
    GraphType = ConvertGraphArg(GraphType)
    return _LoadPajek(GraphType, *args)

_SaveGViz = SaveGViz
def SaveGViz(Graph, *args):
    args = ConvertToSnapType(args, -1, TIntStrH, dict)
    return _SaveGViz(Graph, *args)

def SaveGVizColor(Graph, OutFNm, Desc, NodeLabels, NIdColorH):
    return SaveGViz(Graph, OutFNm, Desc, NodeLabels, NIdColorH)

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

def DrawGVizColor(Graph, Layout, PltFNm, Desc, NodeLabels, NIdColorH):
    return DrawGViz(Graph, Layout, PltFNm, Desc, NodeLabels, NIdColorH)

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
    oldReturn = GetShortPath(Graph, SrcNId, NIdToDistH, IsDir, MaxDist)
    return oldReturn, NIdToDistH

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
        _GetBetweennessCentr (Graph, NIdBtwH, EdgeBtwH, *args)
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
            _GetHits(Graph, NIdHubH, NIdAuthH, MaxIter)
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

def GetTriadsByNode(Graph, SampleNodes=-1):
    NIdCOTriadV = TIntTrV()
    GetTriads(Graph, NIdCOTriadV, SampleNodes)
    return NIdCOTriadV

_GetClustCfAll = GetClustCfAll
def GetClustCfAll(Graph, *args):
    return MoveArgToReturn(Graph, args, _GetClustCfAll, 0, TFltPrV)

_GetCmnNbrs = GetCmnNbrs
def GetCmnNbrs(Graph, NId1, NId2, NbrList = False):
    if NbrList == None  or  NbrList == False:
        return _GetCmnNbrs(Graph, NId1, NId2)
    elif NbrList == True:
        NbrV = TIntV()
        PrevReturn = _GetCmnNbrs(Graph, NId1, NId2, NbrV)
        return (PrevReturn, NbrV)

    return _GetCmnNbrs(Graph, NId1, NId2, NbrList)

def GetNodeClustCfAll(Graph):
    NIdCCfH = TIntFltH()
    GetNodeClustCf(Graph, NIdCCfH)
    return NIdCCfH

_GetNodeTriads = GetNodeTriads
def GetNodeTriads(Graph, *args):
    if len(args) == 2:
        args = ConvertToSnapType(args, 1, TIntSet, set)
    return _GetNodeTriads(Graph, *args)

def GetNodeTriadsSet(Graph, NId, GroupSet):
    return GetNodeTriads(Graph, NId, GroupSet)

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

def GetAnfNode(Graph, SrcNId, MxDist, IsDir, NApprox=32):
    DistNbrsV = TIntFltKdV()
    GetAnf(Graph, SrcNId, DistNbrsV, MxDist, IsDir, NApprox)
    return DistNbrsV

def GetAnfGraph(Graph, MxDist, IsDir, NApprox=32):
    DistNbrsV = TIntFltKdV()
    GetAnf(Graph, DistNbrsV, MxDist, IsDir, NApprox)
    return DistNbrsV

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


_GenConfModel = GenConfModel
def GenConfModel(*args):
    args = ConvertToSnapType(args, 0, TIntV, list)
    return _GenConfModel(*args)

_GetBfsEffDiam = GetBfsEffDiam
def GetBfsEffDiam(Graph, *args):
    args = ConvertToSnapType(args, 1, TIntV, list)
    return _GetBfsEffDiam(Graph, *args)

_GetLen2Paths = GetLen2Paths
def GetLen2Paths(Graph, *args):
    if type(args[-1]) != bool:
        #Backward compatibility
        return _GetLen2Paths(Graph, *args)
    elif args[-1]:
        NbrV = TIntV()
        paths = _GetLen2Paths(Graph, *args[:-1], NbrV)
        return paths, NbrV
    else:
        return _GetLen2Paths(Graph, *args[:-1])

    return MoveArgToReturn(Graph, args, _GetLen2Paths, 2, TIntV)

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

def ConvertGraph_classFn(self, GraphType, *args, **kwargs):
    GraphType = ConvertGraphArg(GraphType)
    return ConvertGraph(GraphType, self, *args, **kwargs)
PUNGraph.ConvertGraph = ConvertGraph_classFn
PNGraph.ConvertGraph = ConvertGraph_classFn
PNEANet.ConvertGraph = ConvertGraph_classFn

def ConvertSubGraph_classFn(self, GraphType, *args, **kwargs):
    GraphType = ConvertGraphArg(GraphType)
    return ConvertSubGraph(GraphType, self, *args, **kwargs)
PUNGraph.ConvertSubGraph = ConvertSubGraph_classFn
PNGraph.ConvertSubGraph = ConvertSubGraph_classFn
PNEANet.ConvertSubGraph = ConvertSubGraph_classFn

def ConvertESubGraph_classFn(self, GraphType, *args, **kwargs):
    GraphType = ConvertGraphArg(GraphType)
    return ConvertESubGraph(GraphType, self, *args, **kwargs)
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

def DrawGVizColor_classFn(self, *args, **kwargs):
    return DrawGVizColor(self, *args, **kwargs)
PUNGraph.DrawGVizColor = DrawGVizColor_classFn
PNGraph.DrawGVizColor = DrawGVizColor_classFn
PNEANet.DrawGVizColor = DrawGVizColor_classFn

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

def GetTriadsByNode_classFn(self, *args, **kwargs):
    return GetTriadsByNode(self, *args, **kwargs)
PUNGraph.GetTriadsByNode = GetTriadsByNode_classFn
PNGraph.GetTriadsByNode = GetTriadsByNode_classFn
PNEANet.GetTriadsByNode = GetTriadsByNode_classFn

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

def GetNodeClustCf_classFn(self, *args, **kwargs):
    return GetNodeClustCf(self, *args, **kwargs)
PUNGraph.GetNodeClustCf = GetNodeClustCf_classFn
PNGraph.GetNodeClustCf = GetNodeClustCf_classFn
PNEANet.GetNodeClustCf = GetNodeClustCf_classFn

def GetNodeClustCfAll_classFn(self, *args, **kwargs):
    return GetNodeClustCfAll(self, *args, **kwargs)
PUNGraph.GetNodeClustCfAll = GetNodeClustCfAll_classFn
PNGraph.GetNodeClustCfAll = GetNodeClustCfAll_classFn
PNEANet.GetNodeClustCfAll = GetNodeClustCfAll_classFn

def GetNodeTriads_classFn(self, *args, **kwargs):
    return GetNodeTriads(self, *args, **kwargs)
PUNGraph.GetNodeTriads = GetNodeTriads_classFn
PNGraph.GetNodeTriads = GetNodeTriads_classFn
PNEANet.GetNodeTriads = GetNodeTriads_classFn

def GetNodeTriadsSet_classFn(self, *args, **kwargs):
    return GetNodeTriadsSet(self, *args, **kwargs)
PUNGraph.GetNodeTriadsSet = GetNodeTriadsSet_classFn
PNGraph.GetNodeTriadsSet = GetNodeTriadsSet_classFn
PNEANet.GetNodeTriadsSet = GetNodeTriadsSet_classFn

def GetNodeTriadsAll_classFn(self, *args, **kwargs):
    return GetNodeTriadsAll(self, *args, **kwargs)
PUNGraph.GetNodeTriadsAll = GetNodeTriadsAll_classFn
PNGraph.GetNodeTriadsAll = GetNodeTriadsAll_classFn
PNEANet.GetNodeTriadsAll = GetNodeTriadsAll_classFn

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

def GetAnfNode_classFn(self, *args, **kwargs):
    return GetAnfNode(self, *args, **kwargs)
PUNGraph.GetAnfNode = GetAnfNode_classFn
PNGraph.GetAnfNode = GetAnfNode_classFn
PNEANet.GetAnfNode = GetAnfNode_classFn

def GetAnfGraph_classFn(self, *args, **kwargs):
    return GetAnfGraph(self, *args, **kwargs)
PUNGraph.GetAnfGraph = GetAnfGraph_classFn
PNGraph.GetAnfGraph = GetAnfGraph_classFn
PNEANet.GetAnfGraph = GetAnfGraph_classFn

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

def GetEigVecs_classFn(self, *args, **kwargs):
    return GetEigVecs(self, *args, **kwargs)
PUNGraph.GetEigVecs = GetEigVecs_classFn
PNGraph.GetEigVecs = GetEigVecs_classFn
PNEANet.GetEigVecs = GetEigVecs_classFn

def GetLeadEigVec_classFn(self, *args, **kwargs):
    return GetLeadEigVec(self, *args, **kwargs)
PUNGraph.GetLeadEigVec = GetLeadEigVec_classFn
PNGraph.GetLeadEigVec = GetLeadEigVec_classFn
PNEANet.GetLeadEigVec = GetLeadEigVec_classFn

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

def GetSngVecs_classFn(self, *args, **kwargs):
    return GetSngVecs(self, *args, **kwargs)
PUNGraph.GetSngVecs = GetSngVecs_classFn
PNGraph.GetSngVecs = GetSngVecs_classFn
PNEANet.GetSngVecs = GetSngVecs_classFn

def GetLeadSngVec_classFn(self, *args, **kwargs):
    return GetLeadSngVec(self, *args, **kwargs)
PUNGraph.GetLeadSngVec = GetLeadSngVec_classFn
PNGraph.GetLeadSngVec = GetLeadSngVec_classFn
PNEANet.GetLeadSngVec = GetLeadSngVec_classFn

def GetInvParticipRat_classFn(self, *args, **kwargs):
    return GetInvParticipRat(self, *args, **kwargs)
PUNGraph.GetInvParticipRat = GetInvParticipRat_classFn
PNGraph.GetInvParticipRat = GetInvParticipRat_classFn
PNEANet.GetInvParticipRat = GetInvParticipRat_classFn

def GetShortPathAll_classFn(self, *args, **kwargs):
    return GetShortPathAll(self, *args, **kwargs)
PUNGraph.GetShortPathAll = GetShortPathAll_classFn
PNGraph.GetShortPathAll = GetShortPathAll_classFn
PNEANet.GetShortPathAll = GetShortPathAll_classFn

def GenRewire_classFn(self, *args, **kwargs):
    return GenRewire(self, *args, **kwargs)
PUNGraph.GenRewire = GenRewire_classFn
PNGraph.GenRewire = GenRewire_classFn
PNEANet.GenRewire = GenRewire_classFn

def SaveEdgeList_classFn(self, *args, **kwargs):
    return SaveEdgeList(self, *args, **kwargs)
PUNGraph.SaveEdgeList = SaveEdgeList_classFn
PNGraph.SaveEdgeList = SaveEdgeList_classFn
PNEANet.SaveEdgeList = SaveEdgeList_classFn

def SaveMatlabSparseMtx_classFn(self, *args, **kwargs):
    return SaveMatlabSparseMtx(self, *args, **kwargs)
PUNGraph.SaveMatlabSparseMtx = SaveMatlabSparseMtx_classFn
PNGraph.SaveMatlabSparseMtx = SaveMatlabSparseMtx_classFn
PNEANet.SaveMatlabSparseMtx = SaveMatlabSparseMtx_classFn

def SavePajek_classFn(self, *args, **kwargs):
    return SavePajek(self, *args, **kwargs)
PUNGraph.SavePajek = SavePajek_classFn
PNGraph.SavePajek = SavePajek_classFn
PNEANet.SavePajek = SavePajek_classFn

def SaveGViz_classFn(self, *args, **kwargs):
    return SaveGViz(self, *args, **kwargs)
PUNGraph.SaveGViz = SaveGViz_classFn
PNGraph.SaveGViz = SaveGViz_classFn
PNEANet.SaveGViz = SaveGViz_classFn

def SaveGVizColor_classFn(self, *args, **kwargs):
    return SaveGVizColor(self, *args, **kwargs)
PUNGraph.SaveGVizColor = SaveGVizColor_classFn
PNGraph.SaveGVizColor = SaveGVizColor_classFn
PNEANet.SaveGVizColor = SaveGVizColor_classFn

def DrawGViz_classFn(self, *args, **kwargs):
    return DrawGViz(self, *args, **kwargs)
PUNGraph.DrawGViz = DrawGViz_classFn
PNGraph.DrawGViz = DrawGViz_classFn
PNEANet.DrawGViz = DrawGViz_classFn

def ToGraph_classFN(self, GraphType, *args, **kwargs):
    GraphType = ConvertGraphArg(GraphType)
    return ToGraph(GraphType, self, *args, **kwargs)
PTable.ToGraph = ToGraph_classFN

def ToNetwork_classFN(self, GraphType, *args, **kwargs):
    GraphType = ConvertGraphArg(GraphType)
    return ToNetwork(GraphType, self, *args, **kwargs)
PTable.ToNetwork = ToNetwork_classFN

%}

