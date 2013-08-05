import snap

for item in dir(snap):
    if item.find("Load") >= 0:
        print item

g = snap.LoadEdgeList_PNGraph(snap.TStr("soc-Epinions1.txt"), 0, 1)
print dir(g)
print g.GetNodes()
print g.GetEdges()

