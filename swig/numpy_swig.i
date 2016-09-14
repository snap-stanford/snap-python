%{
    #define SWIG_FILE_WITH_INIT
    #include "numpy.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (int* ARGOUT_ARRAY1, int DIM1) {(int* IntNumpyVecOut, int n)}
%apply (float* ARGOUT_ARRAY1, int DIM1) {(float* FltNumpyVecOut, int n)}
%apply (int* IN_ARRAY1, int DIM1) {(int* IntNumpyVecIn, int n)}
%apply (float* IN_ARRAY1, int DIM1) {(float* FltNumpyVecIn, int n)}
%include "numpy.h"
