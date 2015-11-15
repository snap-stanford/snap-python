import snap

# first vector
a = snap.TIntV()
a.Add(1)
a.Add(2)
a.Add(3)
a.Add(4)
a.Add(5)
l = [ str(elem) for elem in a]
print "a =      ", ", ".join(l)

# second vector
b = snap.TIntV()
b.Add(3)
b.Add(4)
b.Add(5)
b.Add(6)
b.Add(7)
l = [ str(elem) for elem in b]
print "b =      ", ", ".join(l)

# third vector
c = snap.TIntV()
c.Add(6)
c.Add(7)
c.Add(8)
c.Add(9)
l = [ str(elem) for elem in c]
print "c =      ", ", ".join(l)
print

# intersection
a.Intrs(b)
l = [ str(elem) for elem in a]
print "a = a^b  ", ", ".join(l)
l = [ str(elem) for elem in b]
print "b =      ", ", ".join(l)
print

# union
a.Union(c)
l = [ str(elem) for elem in a]
print "a = avc  ", ", ".join(l)
l = [ str(elem) for elem in c]
print "c =      ", ", ".join(l)
print

# intersection
i = snap.TIntV()
a.Intrs(c,i)
l = [ str(elem) for elem in i]
print "i = a^c  ", ", ".join(l)
l = [ str(elem) for elem in a]
print "a =      ", ", ".join(l)
l = [ str(elem) for elem in c]
print "c =      ", ", ".join(l)
print

# union
u = snap.TIntV()
b.Union(c,u)
l = [ str(elem) for elem in u]
print "u = bvc  ", ", ".join(l)
l = [ str(elem) for elem in b]
print "b =      ", ", ".join(l)
l = [ str(elem) for elem in c]
print "c =      ", ", ".join(l)

