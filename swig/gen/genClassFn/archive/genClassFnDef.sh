#!/bin/bash

# Input: a list of function names, one on every line
# Output: the corresponding function headers defined in snap-core or snap-adv folders

# Note: 
# this script only works if the function headers are defined on one single line
# cound update this script if needed to catch cases where function headers are defined
# over multiple lines

while read func; do
  grep -h "template.*$func[ \t\n]*(" /home/albert/SNAP/snap/snap-core -r | sed "s/^/$func /"
  grep -h "template.*$func[ \t\n]*(" /home/albert/SNAP/snap/snap-adv -r | sed "s/^/$func /"
done
