import snap

G9 = snap.GenRndGnm(snap.PNGraph, 10000, 1000)

CntV = snap.TIntPrV()
snap.GetWccSzCnt(G9, CntV)
for p in CntV:
    print("size %d: count %d" % (p.GetVal1(), p.GetVal2()))

snap.GetOutDegCnt(G9, CntV)
for p in CntV:
    print("degree %d: count %d" % (p.GetVal1(), p.GetVal2()))

G10 = snap.GenPrefAttach(100, 3)

EigV = snap.TFltV()
snap.GetEigVec(G10, EigV)
nr = 0
for f in EigV:
    nr += 1
    print("%d: %.6f" % (nr, f))

diam = snap.GetBfsFullDiam(G10, 10) 
print("diam", diam)

triads = snap.GetTriads(G10)
print("triads", triads)

cf = snap.GetClustCf(G10)
print("cf", cf)

