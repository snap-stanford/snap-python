import snap
import sys

print("Version", snap.Version)

try:
    G = snap.TUNGraph.New()
    print(snap.GetMxDegNId(G))
except RuntimeError:
    e = sys.exc_info()
    print("1-except1", e)
    print("1-except2", e[0])
    print("1-except3", e[1])

print("after GetMxDegNId")

try:
    G = snap.TUNGraph.New()
    G.AddNode(1)
    G.AddNode(1)
except RuntimeError:
    e = sys.exc_info()
    print("2-except1", e)
    print("2-except2", e[0])
    print("2-except3", e[1])

print("after AddNode")

