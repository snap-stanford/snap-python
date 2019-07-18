import snap
Graph = snap.GenFull(snap.PNEANet, 10)
Src = 1
Dst = 2
EI = Graph.GetEI(Src,Dst)
EId = EI.GetId()
print(EId, Graph.GetEI(Src,Dst).GetId())
print(Graph.GetEI(Src,Dst).GetSrcNId(), Graph.GetEI(Src,Dst).GetDstNId())
print(Graph.GetEI(EId).GetSrcNId(), Graph.GetEI(EId).GetDstNId())

if EId != Graph.GetEI(Src,Dst).GetId():
    print("*** error1")

if Graph.GetEI(Src,Dst).GetSrcNId() != Graph.GetEI(EId).GetSrcNId():
    print("*** error2")

if Graph.GetEI(Src,Dst).GetDstNId() != Graph.GetEI(EId).GetDstNId():
    print("*** error3")

