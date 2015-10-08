import snap

G = snap.GenFull(snap.PNEANet, 100)

Rnd = snap.TRnd(0)

for i in range(0,10):
    NId = G.GetRndNId(Rnd)
    print NId

    # result is not well formed, the following statement fails
    #print NI.GetId()

