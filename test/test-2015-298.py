#
#   testing edge iterator
#

import snap
import sys

n = 1000

G = snap.GenFull(snap.PNEANet, n)

for SrcNId in range(1,n):
    for DstNId in range(1,n):
        if SrcNId == DstNId:
            continue

        EI = G.GetEI(SrcNId, DstNId)
        if EI.GetSrcNId() != SrcNId:
            print "*** Error SrcNID (%d, %d), expected %d, got %d" % (
                SrcNId, DstNId, SrcNId, EI.GetSrcNId())

        if EI.GetDstNId() != DstNId:
            print "*** Error DstNID (%d, %d), expected %d, got %d" % (
                SrcNId, DstNId, DstNId, EI.GetDstNId())

