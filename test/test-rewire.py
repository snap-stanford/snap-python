import snap

def rewire(G_in):
    G = G_in.ConvertGraph(snap.TUNGraph)
    G_rewire = snap.GenRewire(G,1000)
    return G_rewire

G_in = snap.GenFull(snap.TNGraph, 572)
for i in range(500):
    G_rewired = rewire(G_in)
    print(i, G_rewired.GetNodes(), G_rewired.GetEdges())

