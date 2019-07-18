import snap

Graph = snap.GenFull(snap.PNEANet, 10)
print(Graph.GetEI(0,5).GetId())

Src = 0
Dst = 5
EI = Graph.GetEI(Src,Dst)
Src1 = EI.GetSrcNId()
Dst1 = EI.GetDstNId()
EI1 = Graph.GetEI(Src1,Dst1)

if Src != Src1  or  Dst != Dst1:
    print("*** Error1")

if EI.GetId() != EI1.GetId():
    print("*** Error2")

Graph = snap.GenFull(snap.PUNGraph, 10)
print(Graph.GetEI(0,5).GetId())

Src = 0
Dst = 5
EI = Graph.GetEI(Src,Dst)
Src1 = EI.GetSrcNId()
Dst1 = EI.GetDstNId()
EI1 = Graph.GetEI(Src1,Dst1)

if Src != Src1  or  Dst != Dst1:
    print("*** Error1")

if EI.GetId() != EI1.GetId():
    print("*** Error2")

Graph = snap.GenFull(snap.PNGraph, 10)
print(Graph.GetEI(0,5).GetId())

Src = 0
Dst = 5
EI = Graph.GetEI(Src,Dst)
Src1 = EI.GetSrcNId()
Dst1 = EI.GetDstNId()
EI1 = Graph.GetEI(Src1,Dst1)

if Src != Src1  or  Dst != Dst1:
    print("*** Error1")

if EI.GetId() != EI1.GetId():
    print("*** Error2")

