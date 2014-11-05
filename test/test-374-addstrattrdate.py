import snap

G1 = snap.GenFull(snap.PNEANet, 5)

G1.AddStrAttrE("sign1")

for EI in G1.Edges():
    EId = G1.GetEId(EI.GetSrcNId(),EI.GetDstNId())
    G1.AddStrAttrDatE(EId,"+",'sign1')

G1.AddStrAttrE("sign2")

# why it works with edge_Id, but does not work with edge
for EI in G1.Edges():
    G1.AddStrAttrDatE(EI,"+",'sign2')

