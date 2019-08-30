import snap

edgefilename = "imdb_actor_edges.tsv"
nodefilename = "imdb_actors_key.tsv"
context = snap.TTableContext()

edgeschema = snap.Schema()
edgeschema.Add(snap.TStrTAttrPr("srcID", snap.atStr))
edgeschema.Add(snap.TStrTAttrPr("dstID", snap.atStr))
edgeschema.Add(snap.TStrTAttrPr("edgeattr1", snap.atStr))

nodeschema = snap.Schema()
nodeschema.Add(snap.TStrTAttrPr("nodeID", snap.atStr))
nodeschema.Add(snap.TStrTAttrPr("name", snap.atStr))
nodeschema.Add(snap.TStrTAttrPr("movies", snap.atStr))
nodeschema.Add(snap.TStrTAttrPr("main_genre", snap.atStr))
nodeschema.Add(snap.TStrTAttrPr("genres", snap.atStr))

edge_table = snap.TTable.LoadSS(edgeschema, edgefilename, context, "\t", snap.TBool(False))
print("edge_rows", edge_table.GetNumValidRows())

node_table = snap.TTable.LoadSS(nodeschema, nodefilename, context, "\t", snap.TBool(False))
print("node_rows", node_table.GetNumValidRows())

srcattrv = snap.TStrV()
srcattrv.Add("edgeattr1")

dstattrv = snap.TStrV()
dstattrv.Add("edgeattr1")

edgeattrv = snap.TStrV()
edgeattrv.Add("edgeattr1")

nodeattrv = snap.TStrV()
nodeattrv.Add("name")

net1 = snap.ToNetwork(snap.PNEANet, edge_table, "srcID", "dstID", srcattrv, dstattrv, edgeattrv, snap.aaFirst)
print("nodes1", net1.GetNodes())
print("edges1", net1.GetEdges())

net2 = snap.ToNetwork(snap.PNEANet, edge_table, "srcID", "dstID", snap.aaFirst)
print("nodes2", net2.GetNodes())
print("edges2", net2.GetEdges())

net3 = snap.ToNetwork(snap.PNEANet, edge_table, "srcID", "dstID", edgeattrv, snap.aaFirst)
print("nodes3", net3.GetNodes())
print("edges3", net3.GetEdges())

net4 = snap.ToNetwork(snap.PNEANet, edge_table, "srcID", "dstID", edgeattrv, node_table, "nodeID", nodeattrv, snap.aaFirst)
print("nodes4", net4.GetNodes())
print("edges4", net4.GetEdges())

