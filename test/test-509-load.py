import snap

print("LoadEdgeListStr 1")
G1 = snap.LoadEdgeListStr(snap.PUNGraph, "data/test-509.txt", 0, 1)
print("nodes %d, edges %d" % (G1.GetNodes(), G1.GetEdges()))

print("LoadEdgeListStr 2")
#mapping = snap.TStrIntH()
mapping = snap.TStrIntSH()
G2 = snap.LoadEdgeListStr(snap.PUNGraph, "data/test-509.txt", 0, 1, mapping)
print("nodes %d, edges %d" % (G2.GetNodes(), G2.GetEdges()))

