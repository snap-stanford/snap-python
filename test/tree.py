import snap

tree = snap.GenTree(snap.PNGraph, 3, 5)
print "nodes %d, edges %d" % (tree.GetNodes(), tree.GetEdges())

#result = snap.IsTree_PNGraph(tree)
result = snap.IsTree(tree)
print "IsTree %s" % (str(result))

istree = result[0]
root = result[1]
print "Result1 %d %d" % (istree, root)

istree, root = snap.IsTree(tree)
print "Result2 %d %d" % (istree, root)

