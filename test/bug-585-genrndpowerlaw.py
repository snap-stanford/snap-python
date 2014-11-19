import snap

# this fails
G = snap.GenRndPowerLaw(1000, 1.374, True)
print "True works!"

# this works
G = snap.GenRndPowerLaw(1000, 1.374, False)
print "False works!"

