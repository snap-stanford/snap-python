import snap

print "testing snap.TIntSet ..."
set = snap.TIntSet()
set.AddKey(0)
set.AddKey(1)
set.AddKey(2)
for Id_A in set:
    for Id_B in set:
        print (Id_A, Id_B)

print "testing snap.TIntH ..."
hash = snap.TIntH()
hash[0] = 0
hash[1] = 1
hash[2] = 2
for Id_A in hash:
    for Id_B in hash:
        print (Id_A, Id_B)

