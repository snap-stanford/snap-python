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
set = snap.TIntH()
set[0] = 1
set[1] = 1
set[2] = 1
for Id_A in set:
    for Id_B in set:
        print (Id_A, Id_B)

