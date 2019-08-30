import snap
#h1 = snap.TIntH()
h1 = snap.TIntStrH()
for i in range(500):
    h1[i] = "a"

it = h1.BegI()
while not it.IsEnd():
    print(it.GetKey(), it.GetDat())
    it.Next()

