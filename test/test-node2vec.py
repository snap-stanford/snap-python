import snap

# get wiki-Vote.txt from http://snap.stanford.edu/data/wiki-Vote.html
G5 = snap.LoadEdgeList(snap.PNGraph,"wiki-Vote.txt",0,1)

hv = snap.TIntFltVH()

snap.node2vec(G5, 1.0, 1.0, 128, 80, 10, 10, 1, False, hv)

