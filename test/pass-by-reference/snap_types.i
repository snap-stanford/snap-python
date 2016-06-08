// snap_types.i
//
// Provides type interface between Snap.py Python and SNAP C++
//

%include typemaps.i
%apply int &OUTPUT { int& RootNIdX};
%apply int &OUTPUT { int& TreeSzX};
%apply int &OUTPUT { int& TreeDepthX};
%apply double &OUTPUT { double& EffDiamX};
%apply double &OUTPUT { double& AvgSPLX};
%apply int &OUTPUT { int& FullDiamX};
%apply int &OUTPUT { int& EdgesInX};
%apply int &OUTPUT { int& EdgesOutX};
//%apply int64 &OUTPUT { int64& ClosedTriadsX};
//%apply int64 &OUTPUT { int64& OpenTriadsX};
%apply int &OUTPUT { int& ClosedNTriadsX};
%apply int &OUTPUT { int& OpenNTriadsX};
%apply int &OUTPUT { int& InGroupEdgesX};
%apply int &OUTPUT { int& InOutGroupEdgesX};
%apply int &OUTPUT { int& OutGroupX};

//
// TInt
//

%typemap(in) TInt& {
//%typemap(in) TInt & NId {
  //TInt I = PyInt_AsLong($input);
  //$1 = &I;
  $1 = new TInt(PyInt_AsLong($input));
}

%typemap(freearg) TInt& {
   free($1);
}

%typemap(in) const TInt& {
//%typemap(in) const TInt& value {
  //TInt I = PyInt_AsLong($input);
  //$1 = &I;
  $1 = new TInt(PyInt_AsLong($input));
}

%typemap(freearg) const TInt& {
   free($1);
}

%typemap(in) TInt {
  //TInt I = PyInt_AsLong($input);
  //$1 = I;
  $1 = TInt(PyInt_AsLong($input));
}

%typemap(in) TInt defaultValue {
  //TInt I = PyInt_AsLong($input);
  //$1 = I;
  $1 = TInt(PyInt_AsLong($input));
}

%typemap(out) TInt {
  $result = PyInt_FromLong((long) ($1.Val));
}

%typemap(out) TInt& {
  $result = PyInt_FromLong((long) ($1->Val));
}


%typecheck(SWIG_TYPECHECK_INTEGER)
   int, short, long,
   unsigned int, unsigned short, unsigned long,
   signed char, unsigned char,
   long long, unsigned long long,
   const int &, const short &, const long &,
   const unsigned int &, const unsigned short &, const unsigned long &,
   const long long &, const unsigned long long &,
   enum SWIGTYPE,
         bool, const bool &, TInt, TInt&, const TInt, const TInt&
{
  $1 = (PyInt_Check($input) || PyLong_Check($input)) ? 1 : 0;
}
