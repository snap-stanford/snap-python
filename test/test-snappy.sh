#!/bin/bash

#
# test script for basic Snap.py functionality
#
# input file requirements, files are in "data"
#		p2p-Gnutella08.txt
#

# TODO
#   bug-328-cnm.py
#   bug-585-genrndpowerlaw.py
#   bug-20150706-pagerank.py
#   bug-2015-18.py
#   bug-2015-130.py
#   bug-GetClosenessCentr.py
scripts=(quick_test.py \
    cncom.py intro.py tutorial.py tneanet.py bfs.py attributes.py \
    test-tnodei.py test-io.py \
    test-131-setiter.py \
    test-346-getei.py \
    test-356-getei.py \
    test-374-addstrattrdate.py \
    test-384-deledge.py \
    test-509-load.py \
    test-582-getnodewcc.py \
    test-585-genrndpowerlaw.py \
    test-613-getbfstree.py \
    snap-test.py) 

for line in "${scripts[@]}"; do
    echo "***" `date` "$line ..."
    python $line
    RETVAL=$?
    if [ $RETVAL -ne 0 ]; then
        echo "***" `date` "ERROR: $line"
        exit $RETVAL
    fi;
done

