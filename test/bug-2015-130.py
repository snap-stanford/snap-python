import snap

G = snap.GenFull(snap.PNEANet, 100)
NI = G.GetRndNI()

# result is not well formed, the following statement fails
print NI.GetId()

