// snap.i

//   The multi-attribute network graph type, PNEANet is instantiated, along
//   with standard SNAP functions.

%module snap
%{

#include "Snap.h"
  
#include "Engine.h"
#include "snapswig.h"

#include "printgraph.h"
#include "snap_types.h"
#include "goodgraph.cpp"

%}

%module test

%feature("autodoc", "3");

%ignore TOnExeStop;
%ignore TPt::TPt;
%ignore TPt::LoadXml;
%ignore TPt::SaveXml;
%ignore TPt::operator==;
%ignore TPt::operator!=;
%ignore TPt::operator<;
%ignore TPt::GetPrimHashCd;
%ignore TPt::GetSecHashCd;
%ignore TPt::Clone;

%ignore TChA::LoadXml;
%ignore TMem::LoadXml;

%ignore GetStr;

%ignore TFInOut;
%ignore TFRnd;
%ignore TFile::Copy;
%ignore TFile::GetLastAccessTm;
%ignore TFile::GetLastWriteTm;
%ignore TFile::GetCreateTm;
%ignore TFile::GetSize;

%ignore TBPGraph::HasFlag(const TGraphFlag& Flag) const;
%ignore TNEGraph::GetSmallGraph();
%ignore TNEANet::GetSmallGraph();
%ignore TBPGraph::GetEI(int const&) const;

%ignore TNGraph::GetEI(int const&) const;
%ignore TUNGraph::GetEI(int const&) const;
%ignore TNEANet::GetEI(int const&) const;

%ignore TVec<TVec<TInt, int>, int>::Add;
%ignore TVec<TVec<TInt, int>, int>::AddMerged;

%ignore TVec<TStr, int>::Add;
%ignore TVec<TStr, int>::AddMerged;


%ignore THash< TInt, TVec< TInt, int > >::AddDat;
%ignore THash< TInt, TVec< TInt, int > >::HashPrimeT;
%ignore THash< TInt, TVec< TInt, int > >::AddDatId;

%ignore THash< TInt, TInt, TDefaultHashFunc<TInt> >::HashPrimeT;
%ignore THash< TInt, TInt, TDefaultHashFunc<TInt> >::AddDatId;
%ignore THash< TInt, TInt>::HashPrimeT;

// SNAP Library
// snap-core
%include "alg.h"
%include "anf.h"
%include "bfsdfs.h"
%include "bd.h"
%include "centr.h"
%include "cmty.h"
%include "cncom.h"
%include "ff.h"
%include "fl.h"
%include "graph.h"
%include "gsvd.h"
%include "gio.h"
%include "gviz.h"
%include "hash.h"
%include "kcore.h"
%include "ggen.h"
%include "subgraph.h"
%include "util.h"
%include "triad.h"

#define GLib_UNIX
// glib-core
%include "ds.h"
%include "dt.h"

%include "Engine.h"

%extend TVec {

        TSizeTy Add(int Val) {
                return $self->Add(TInt(Val));
        }

        TSizeTy AddMerged(int Val) {
                return $self->AddMerged(TInt(Val));
        }
};

%extend THash {
        int AddKey(int Val) {
                return $self->AddKey(TInt(Val));
        }
        int IsKey(int Val) {
                return $self->IsKey(TInt(Val));
        }
        TDat& GetDat(int Val) {
                return $self->GetDat(TInt(Val));
        }
        TDat& AddDat(int Key, int Val) {
                return $self->AddDat(TInt(Key),TInt(Val));
        }
}

%template(TIntV) TVec< TInt, int >;
%template(TIntIntVV) TVec< TVec< TInt, int >, int >;
%template(TIntIntVH) THash< TInt, TVec< TInt, int > >;
%template(TIntH) THash<TInt, TInt>;
%template(TIntHI) THashKeyDatI < TInt, TInt >;

%template(TStrV) TVec< TStr, int >;

// Python-SNAP conversion typemaps
%include "snapswig.h"
%include "goodgraph.cpp"
%include "printgraph.h"
%include "snap_types.i"

// For TNEANet
%include "network.h"

/* Graph templates - include other SWIG interface types here. */
%include "pneanet.i"
