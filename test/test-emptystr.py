import snap
G = snap.LoadEdgeList(snap.PNGraph, 'wiki-Vote.txt', 0, 1)

print " 1 ----------"
snap.PrintInfo(G, "a")
print " 2 ----------"
snap.PrintInfo(G, "a", "file.txt")
print " 3 ----------"
snap.PrintInfo(G, "a", "file.txt", False)

print " 4 ----------"
snap.PrintInfo(G, "a", "")

#print " 5 ----------"
#snap.PrintInfo(G, "a", "", False)

