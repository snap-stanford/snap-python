import snap

H = snap.TStrIntSH()
Graph = snap.LoadConnListStr(snap.PNGraph,
            "data/example-LoadConnListStr.txt", H)
# get node ID of "A"
print(H.GetDat("A"))

H = snap.TStrIntSH()
UGraph = snap.LoadConnListStr(snap.PUNGraph,
            "data/example-LoadConnListStr.txt", H)

H = snap.TStrIntSH()
Network = snap.LoadConnListStr(snap.PNEANet,
            "data/example-LoadConnListStr.txt", H)

