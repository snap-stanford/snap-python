import snap

#print snap.Version

#G = snap.LoadEdgeList(snap.PNEANet, "g1.edgelist", 0, 1)
#G.AddIntAttrN("NValInt", 0)
#print G.GetIntAttrDatN(1, "NValInt")
#G.AddIntAttrDatN(1, 10, "NValInt")
#print G.GetIntAttrDatN(1, "NValInt")

g1 = snap.LoadEdgeList(snap.PNEANet, "g1.edgelist") 

g1.AddIntAttrN("NValInt", 55) 

nids = sorted([node.GetId() for node in g1.Nodes()])

print g1.GetIntAttrDatN(nids[0], "NValInt") 
print g1.GetIntAttrDatN(nids[1], "NValInt") 
print g1.GetIntAttrDatN(nids[2], "NValInt") 

g1.AddIntAttrDatN(nids[0], 42, "NValInt") 
g1.AddIntAttrDatN(nids[1], 42, "NValInt") 
g1.AddIntAttrDatN(nids[2], 42, "NValInt") 
print g1.GetIntAttrDatN(nids[0], "NValInt") 
print g1.GetIntAttrDatN(nids[1], "NValInt") 
print g1.GetIntAttrDatN(nids[2], "NValInt") 

print snap.Version

