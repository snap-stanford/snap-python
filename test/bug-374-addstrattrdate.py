import snap

G1 = snap.GenFull(snap.PNEANet, 5)

G1.AddStrAttrE("sign1")

for edge in G1.Edges():
    edge_Id = G1.GetEId(edge.GetSrcNId(),edge.GetDstNId())
    G1.AddStrAttrDatE(edge_Id,"+",'sign1')

G1.AddStrAttrE("sign2")

# why it works with edge_Id, but does not work with edge
for edge in G1.Edges():
    G1.AddStrAttrDatE(edge,"+",'sign2')

