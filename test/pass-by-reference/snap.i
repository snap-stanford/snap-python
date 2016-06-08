// snap.i

//   PNEANet, PUNGraph, PNGraph are supported,
//     along with standard SNAP functions.

#define SNAP_ALL 0

%pythoncode %{
Version = "2.0.3-dev"
%}

%module snap

%{

#include "Snap.h"

%}

%feature("autodoc", "3");
// Python-C++ conversion typemaps

%include "snap_types.i"

#define GLib_UNIX
%include "int.h"


