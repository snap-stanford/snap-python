// snap_types.i
//
// Provides type interface between Snap.py Python and SNAP C++
//

%include typemaps.i
%apply int &OUTPUT { TInt& ValX};

//
// TInt
//

%typemap(in) TInt& {
  $1 = new TInt(PyInt_AsLong($input));
}

%typemap(freearg) TInt& {
   free($1);
}

%typemap(in) const TInt& {
  $1 = new TInt(PyInt_AsLong($input));
}

%typemap(freearg) const TInt& {
   free($1);
}

%typemap(in) TInt {
  $1 = TInt(PyInt_AsLong($input));
}

%typemap(in) TInt defaultValue {
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
