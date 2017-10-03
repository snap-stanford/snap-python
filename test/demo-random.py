import snap

G = snap.GenFull(snap.PNEANet, 100)

Rnd = snap.TRnd(42)
Rnd.Randomize()

for i in range(0,10):
    NId = G.GetRndNId()
    print NId

    # result is not well formed, the following statement fails
    #print NI.GetId()

