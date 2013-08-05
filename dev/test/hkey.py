import snap

h = snap.TIntIntVH()
print h.Len()

for i in range(0,10):
    k = h.AddKey(snap.TInt(i))
    v = h.GetDat(snap.TInt(i))

    for j in range(0,i+3):
        v.Add(j)
    
    print i,k

print h.Len()

print "-----------"

for i in range(0,10):
    j = h.GetKeyId(snap.TInt(i))
    print j

    v = h.GetDat(snap.TInt(i))
    #print type(j), type(v)
    print v.Len()
    print

