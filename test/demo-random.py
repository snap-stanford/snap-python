import snap

G = snap.GenFull(snap.PNEANet, 100)

# get a new random generator, provide the seed value
Rnd = snap.TRnd(42)

# randomize the generator, every execution will produce a different sequence.
# Comment out the line to get the same sequence on every execution.
Rnd.Randomize()

for i in range(0,10):
    # provide the random generator as a parameter to the function
    NId = G.GetRndNId(Rnd)
    print(NId)

    # result is not well formed, the following statement fails
    #print(NI.GetId())

