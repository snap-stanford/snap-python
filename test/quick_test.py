import snap

print "Version", snap.Version

i = snap.TInt(5)

if i == 5:
    print "SUCCESS", i.Val
else:
    print "*** ERROR", i.Val

