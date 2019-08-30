import snap

#v = TIntV.GetV(TInt(11),TInt(12),TInt(13),TInt(14),TInt(15))
v = snap.TIntV.GetV(11,12,13,14,15)

print("length", v.Len())
print("v[2]", v[2])


try:
    print(v[5])
except:
    print("*** PYTHON CATCH")

print("--------- 1")
for item in v:
    print(item)

print("--------- 2")
for i in range(0, v.Len()):
    print(v[i])

print("--------- 3")
for i in range(0, v.Len()):
    print("__getval__", v.GetVal(i), v[i])

print("--------- 4")
v = snap.TIntV()

v.Add(1)
v.Add(2)
v.Add(3)
v.Add(4)
v.Add(5)

print(v.Len())
print(v[2])

v.SetVal(3, 2*v[2])
v[4] = 2*v[2]
print("__setval__", v[3], v[4])

print(v[2])

for item in v:
    print(item)

for i in range(0, v.Len()):
    print(i, v[i])

