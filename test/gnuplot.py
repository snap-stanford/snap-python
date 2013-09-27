import snap

G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)

snap.PlotInDegDistr(G, "wiki-in-degree", "wiki-Vote in Degree")


