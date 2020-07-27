This folder contains scripts for extending class functions in C++ using swig.
Currently class functions are being added in the Python interface instead, as described in the folder above. 

The class function extensions for C++ were generated as follows: 
genClassFnDef.sh < classFn.txt > classFnDef.txt
python genClassFnExt.py > classFnExt.txt

classFn.txt is the input file containing the names of the class functions, one per row.
classFnExt.txt is the output file that contains the extension templates for the classes: TNGraph, TUNGraph, and TNEANet. The %extend blocks for the graph classes should be placed in their respective swig .i files (pngraph.i, pungraph.i, and pneanet.i in this case)
