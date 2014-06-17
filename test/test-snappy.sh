#!/bin/bash

#
# test script for basic Snap.py functionality
#
# input file requirements, files are in "data"
#		p2p-Gnutella08.txt
#

scripts=( quick_test.py snap-test.py test-tnodei.py test-io.py \
    intro.py tutorial.py tneanet.py cncom.py bfs.py attributes.py ) 

for line in "${scripts[@]}"; do
    echo "***" `date` "$line ..."
    python $line
    RETVAL=$?
    if [ $RETVAL -ne 0 ]; then
        echo "***" `date` "ERROR: $line"
        exit $RETVAL
    fi;
done
