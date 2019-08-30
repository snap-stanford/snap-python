import snap as Snap

h = Snap.TIntIntVH()
print(h.Len())

for i in range(0,10):
    k = h.AddKey(Snap.TInt(i))
    v = h.GetDat(Snap.TInt(i))

    for j in range(0,i+3):
        v.Add(j)
    
    print(i,k)

print(h.Len())

print("-----------")

for i in range(0,10):
    j = h.GetKeyId(Snap.TInt(i))
    print(j)

    v = h.GetDat(Snap.TInt(i))
    #print(type(j), type(v))
    print(v.Len())
    print()

