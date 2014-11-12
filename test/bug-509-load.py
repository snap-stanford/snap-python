import snap

print "LoadEdgeListStr 1"
companyEmployeeGraph = snap.LoadEdgeListStr(snap.PUNGraph, "c.txt", 0, 1)

print "LoadEdgeListStr 2"
mapping = snap.TStrIntH()
companyEmployeeGraph = snap.LoadEdgeListStr(snap.PUNGraph, "c.txt", 0, 1, mapping)

