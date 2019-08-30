import snap
G = snap.GenFull(snap.PNEANet, 1)
G.AddFltAttrN("NValFlt", 0.0)
G.AddFltAttrN("NValFlt2", 0.0)
G.AddFltAttrN("NValFlt3", 0.0)
nid = G.GetNI(0)
G.AddFltAttrDatN(nid, float(1), "NValFlt")
G.AddFltAttrDatN(nid, float(5), "NValFlt2")
G.AddFltAttrDatN(nid, float(10), "NValFlt3")
fval = G.GetFltAttrDatN(nid, "NValFlt")
fval2 = G.GetFltAttrDatN(nid,  "NValFlt2")
fval3 = G.GetFltAttrDatN(nid,  "NValFlt3")
print(fval, fval2, fval3) # prints 10.0, 10.0, 10.0 instead of 1.0, 5.0, 10.0

