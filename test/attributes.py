import snap

nodes = 10
G = snap.GenFull(snap.PNEANet,nodes)

# define int, float and str attributes on nodes
G.AddIntAttrN("NValInt", 0)
G.AddFltAttrN("NValFlt", 0.0)
G.AddStrAttrN("NValStr", "0")

# define an int attribute on edges
G.AddIntAttrE("EValInt", 0)

# add attribute values, node ID for nodes, edge ID for edges

for NI in G.Nodes():
    nid = NI.GetId()
    val = nid
    G.AddIntAttrDatN(nid, val, "NValInt")
    G.AddFltAttrDatN(nid, float(val), "NValFlt")
    G.AddStrAttrDatN(nid, str(val), "NValStr")

    for nid1 in NI.GetOutEdges():
        eid = G.GetEId(nid,nid1)
        val = eid
        G.AddIntAttrDatE(eid, val, "EValInt")

# print out attribute values

for NI in G.Nodes():
    nid = NI.GetId()
    ival = G.GetIntAttrDatN(nid, "NValInt")
    fval = G.GetFltAttrDatN(nid, "NValFlt")
    sval = G.GetStrAttrDatN(nid, "NValStr")
    print "node %d, NValInt %d, NValFlt %.2f, NValStr %s" % (nid, ival, fval, sval)

    for nid1 in NI.GetOutEdges():
        eid = G.GetEId(nid, nid1)
        val = G.GetIntAttrDatE(eid, "EValInt")
        print "edge %d (%d,%d), EValInt %d" % (eid, nid, nid1, val)

