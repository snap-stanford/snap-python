// snap.i

//   PNEANet, PUNGraph, PNGraph are supported,
//     along with standard SNAP functions.

%pythoncode %{
Version = "0.5.1"
%}

%module snap
%{

#include "Snap.h"
  
/* #include "Engine.h" */
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

%ignore LoadXml;
%ignore SaveXml;

%ignore TTm;
%ignore HashPrimeT;

// ignore all THash::AddDatId, MarkDelKey, MarkDelKeyId
%ignore THash::AddDatId;
%ignore THash::MarkDelKey;
%ignore THash::MarkDelKeyId;

// these are specific instances with errors, g++ still complains
//%ignore THash< TInt, TVec<TInt, int>, TDefaultHashFunc<TInt> >::AddDatId;
//%ignore THash< TInt, THash<TInt, TInt, TDefaultHashFunc<TInt> >, TDefaultHashFunc<TInt> >::AddDatId;
//%ignore THash< TInt, TPair<TFlt, TFlt>, TDefaultHashFunc<TInt> >::AddDatId;
//%ignore THash< TInt, TTriple<TFlt, TFlt, TFlt>, TDefaultHashFunc<TInt> >::AddDatId;
//%ignore THash< TInt, TVec<TFlt, int>, TDefaultHashFunc<TInt> >::AddDatId;
//%ignore THash< TInt, TVec<TStr, int>, TDefaultHashFunc<TInt> >::AddDatId;
//%ignore THash< TInt, TPair<TInt, TInt>, TDefaultHashFunc<TInt> >::AddDatId;
//%ignore THash< TInt, TVec<TPair<TInt, TInt> >, TDefaultHashFunc<TInt> >::AddDatId;
//%ignore THash< TUInt64, TVec<TStr, int>, TDefaultHashFunc<TUInt64> >::AddDatId;
//%ignore THash< TPair<TInt, TInt>, TVec<TInt, int>, TDefaultHashFunc<TPair<TInt, TInt> > >::AddDatId;
//%ignore THash< TPair<TInt, TInt>, TVec<TPair<TInt, TInt>, int>, TDefaultHashFunc<TPair<TInt, TInt> > >::AddDatId;
//%ignore THash< TPair<TInt, TInt>, TVec<TStr, int>, TDefaultHashFunc<TPair<TInt, TInt> > >::AddDatId;
//%ignore THash< TStr, TPair<TInt, TInt>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TVec<TInt, int>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TVec<TUInt64, int>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TVec<TPair<TInt, TInt>, int>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TVec<TFlt, int>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TPair<TStr, TStr>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TVec<TStr, int>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TVec<TPair<TStr, TStr>, int>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TVec<TKeyDat<TStr, TStr>, int>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TPair<TInt, TFlt>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TVec<TPair<TStr, TInt>, int>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TStr, TVec<TKeyDat<TStr, TInt>, int>, TDefaultHashFunc<TStr> >::AddDatId;
//%ignore THash< TVec<TStr, int>, TVec<TInt, int>, TDefaultHashFunc<TVec<TStr, int> > >::AddDatId;
//%ignore THash<  TVec<TStr, int>, TVec<TStr, int>, TDefaultHashFunc<TVec<TStr, int> > >::AddDatId;

%include "snap_types.i"

//%include exception.i
//
//%exception {
//    try {
//        $action
//    }
//    catch (int i) {
//        printf("*** CATCH %d\n", i);
//        PyErr_SetString(PyExc_IndexError,"index out-of-bounds");
//        SWIG_exception(SWIG_UnknownError,"Unknown exception");
//    }
//}

#define GLib_UNIX
// glib-core
%include "bd.h"
%include "ds.h"
%include "dt.h"
%include "fl.h"
//%include "tm.h"
//%include "ut.h"

// SNAP Library
// snap-core
%include "gbase.h"
%include "alg.h"
%include "anf.h"
%include "bfsdfs.h"
%include "centr.h"
%include "cmty.h"
%include "cncom.h"
%include "ff.h"
%include "graph.h"
%include "network.h"
%include "gsvd.h"
%include "gio.h"
%include "gviz.h"
%include "hash.h"
%include "kcore.h"
%include "ggen.h"
%include "subgraph.h"
%include "util.h"
%include "triad.h"

%extend TVec {

        //TSizeTy Add(int Val) {
                //return $self->Add(TInt(Val));
        //}

        //TSizeTy AddMerged(int Val) {
                //return $self->AddMerged(TInt(Val));
        //}
};

%extend THash {
        //int AddKey(int Val) {
                //return $self->AddKey(TInt(Val));
        //}
        //int IsKey(int Val) {
                //return $self->IsKey(TInt(Val));
        //}
        //TDat& GetDat(int Val) {
                //return $self->GetDat(TInt(Val));
        //}
        //TDat& AddDat(int Key, int Val) {
                //return $self->AddDat(TInt(Key),TInt(Val));
        //}
};

//%template(TIntV) TVec< TInt, int >;
//%template(TIntIntVV) TVec< TVec< TInt, int >, int >;
//%template(TIntIntVH) THash< TInt, TVec< TInt, int > >;

%template(TIntH) THash<TInt, TInt>;
%template(TIntHI) THashKeyDatI < TInt, TInt >;

//%template(TStrV) TVec< TStr, int >;

//%template(TIntPrV) TVec< TIntPr >;
//%template(TFltV) TVec< TFlt >;

// SNAP type definitions

// ds.h

//%template(TBoolChPr) TPair<TBool, TCh>;
%template(TBoolFltPr) TPair<TBool, TFlt>;
//%template(TUChIntPr) TPair<TUCh, TInt>;
//%template(TUChUInt64Pr) TPair<TUCh, TUInt64>;
//%template(TUChStrPr) TPair<TUCh, TStr>;
%template(TIntBoolPr) TPair<TInt, TBool>;
//%template(TIntChPr) TPair<TInt, TCh>;
%template(TIntPr) TPair<TInt, TInt>;
%template(TIntUInt64Pr) TPair<TInt, TUInt64>;
%template(TIntIntPrPr) TPair<TInt, TIntPr>;
%template(TIntIntVPr) TPair<TInt, TVec<TInt, int> >;
%template(TIntFltPr) TPair<TInt, TFlt>;
%template(TIntStrPr) TPair<TInt, TStr>;
%template(TIntStrVPr) TPair<TInt, TStrV>;
%template(TIntPrIntPr) TPair<TIntPr, TInt>;
%template(TUIntUIntPr) TPair<TUInt, TUInt>;
%template(TUIntIntPr) TPair<TUInt, TInt>;
%template(TUInt64IntPr) TPair<TUInt64, TInt>;
%template(TUInt64Pr) TPair<TUInt64, TUInt64>;
%template(TUInt64FltPr) TPair<TUInt64, TFlt>;
%template(TUInt64StrPr) TPair<TUInt64, TStr>;
%template(TFltIntPr) TPair<TFlt, TInt>;
%template(TFltUInt64Pr) TPair<TFlt, TUInt64>;
%template(TFltPr) TPair<TFlt, TFlt>;
%template(TFltStrPr) TPair<TFlt, TStr>;
%template(TAscFltIntPr) TPair<TAscFlt, TInt>;
%template(TAscFltPr) TPair<TAscFlt, TAscFlt>;
%template(TFltStrPr) TPair<TFlt, TStr>;
%template(TAscFltStrPr) TPair<TAscFlt, TStr>;
%template(TStrIntPr) TPair<TStr, TInt>;
%template(TStrFltPr) TPair<TStr, TFlt>;
%template(TStrPr) TPair<TStr, TStr>;
%template(TStrStrVPr) TPair<TStr, TStrV>;
%template(TStrVIntPr) TPair<TStrV, TInt>;
%template(TIntIntPrPr) TPair<TInt, TIntPr>;
%template(TIntStrPrPr) TPair<TInt, TStrPr>;
%template(TFltStrPrPr) TPair<TFlt, TStrPr>;
%template(TChTr) TTriple<TCh, TCh, TCh>;
%template(TChIntIntTr) TTriple<TCh, TInt, TInt>;
%template(TUChIntIntTr) TTriple<TUCh, TInt, TInt>;
%template(TIntTr) TTriple<TInt, TInt, TInt>;
%template(TUInt64Tr) TTriple<TUInt64, TUInt64, TUInt64>;
%template(TIntStrIntTr) TTriple<TInt, TStr, TInt>;
%template(TIntIntStrTr) TTriple<TInt, TInt, TStr>;
%template(TIntIntFltTr) TTriple<TInt, TInt, TFlt>;
%template(TIntFltIntTr) TTriple<TInt, TFlt, TInt>;
%template(TIntFltFltTr) TTriple<TInt, TFlt, TFlt>;
%template(TIntIntVIntTr) TTriple<TInt, TVec<TInt, int>, TInt>;
%template(TIntIntIntVTr) TTriple<TInt, TInt, TVec<TInt, int> >;
%template(TFltTr) TTriple<TFlt, TFlt, TFlt>;
%template(TFltIntIntTr) TTriple<TFlt, TInt, TInt>;
%template(TFltFltIntTr) TTriple<TFlt, TFlt, TInt>;
%template(TFltFltStrTr) TTriple<TFlt, TFlt, TStr>;
%template(TChATr) TTriple<TChA, TChA, TChA>;
%template(TStrTr) TTriple<TStr, TStr, TStr>;
%template(TStrIntIntTr) TTriple<TStr, TInt, TInt>;
%template(TStrFltFltTr) TTriple<TStr, TFlt, TFlt>;
%template(TStrStrIntTr) TTriple<TStr, TStr, TInt>;
%template(TStrIntStrVTr) TTriple<TStr, TInt, TStrV>;
%template(TStrStrIntIntQu) TQuad<TStr, TStr, TInt, TInt>;
%template(TStrQu) TQuad<TStr, TStr, TStr, TStr>;
%template(TIntQu) TQuad<TInt, TInt, TInt, TInt>;
%template(TFltQu) TQuad<TFlt, TFlt, TFlt, TFlt>;
%template(TFltIntIntIntQu) TQuad<TFlt, TInt, TInt, TInt>;
%template(TIntStrIntIntQu) TQuad<TInt, TStr, TInt, TInt>;
%template(TIntIntFltFltQu) TQuad<TInt, TInt, TFlt, TFlt>;
%template(TIntKd) TKeyDat<TInt, TInt>;
%template(TIntUInt64Kd) TKeyDat<TInt, TUInt64>;
%template(TIntFltKd) TKeyDat<TInt, TFlt>;
%template(TIntPrFltKd) TKeyDat<TIntPr, TFlt>;
%template(TIntFltPrKd) TKeyDat<TInt, TFltPr>;
%template(TIntSFltKd) TKeyDat<TInt, TSFlt>;
%template(TIntStrKd) TKeyDat<TInt, TStr>;
%template(TUIntIntKd) TKeyDat<TUInt, TInt>;
%template(TUIntKd) TKeyDat<TUInt, TUInt>;
%template(TUInt64IntKd) TKeyDat<TUInt64, TInt>;
%template(TUInt64FltKd) TKeyDat<TUInt64, TFlt>;
%template(TUInt64StrKd) TKeyDat<TUInt64, TStr>;
%template(TFltBoolKd) TKeyDat<TFlt, TBool>;
%template(TFltIntKd) TKeyDat<TFlt, TInt>;
%template(TFltUInt64Kd) TKeyDat<TFlt, TUInt64>;
%template(TFltIntPrKd) TKeyDat<TFlt, TIntPr>;
%template(TFltUIntKd) TKeyDat<TFlt, TUInt>;
%template(TFltKd) TKeyDat<TFlt, TFlt>;
%template(TFltStrKd) TKeyDat<TFlt, TStr>;
%template(TFltBoolKd) TKeyDat<TFlt, TBool>;
%template(TFltIntBoolPrKd) TKeyDat<TFlt, TIntBoolPr>;
%template(TAscFltIntKd) TKeyDat<TAscFlt, TInt>;
%template(TStrBoolKd) TKeyDat<TStr, TBool>;
%template(TStrIntKd) TKeyDat<TStr, TInt>;
%template(TStrFltKd) TKeyDat<TStr, TFlt>;
%template(TStrAscFltKd) TKeyDat<TStr, TAscFlt>;
%template(TStrKd) TKeyDat<TStr, TStr>;
%template(TBoolV) TVec<TBool>;
%template(TChV) TVec<TCh>;
%template(TUChV) TVec<TUCh>;
%template(TUIntV) TVec<TUInt>;

%template(TIntV) TVec<TInt>;

%template(TUInt64V) TVec<TUInt64>;
%template(TFltV) TVec<TFlt>;
%template(TSFltV) TVec<TSFlt>;
%template(TAscFltV) TVec<TAscFlt>;

%template(TStrV) TVec<TStr>;

%template(TChAV) TVec<TChA>;
%template(TIntPrV) TVec<TIntPr>;
%template(TIntTrV) TVec<TIntTr>;
%template(TIntQuV) TVec<TIntQu>;
%template(TFltPrV) TVec<TFltPr>;
%template(TFltTrV) TVec<TFltTr>;
%template(TIntKdV) TVec<TIntKd>;
%template(TUChIntPrV) TVec<TUChIntPr>;
%template(TUChUInt64PrV) TVec<TUChUInt64Pr>;
%template(TIntUInt64PrV) TVec<TIntUInt64Pr>;
%template(TIntUInt64KdV) TVec<TIntUInt64Kd>;
%template(TIntFltPrV) TVec<TIntFltPr>;
%template(TIntFltPrKdV) TVec<TIntFltPrKd>;
%template(TFltIntPrV) TVec<TFltIntPr>;
%template(TFltUInt64PrV) TVec<TFltUInt64Pr>;
%template(TFltStrPrV) TVec<TFltStrPr>;
%template(TAscFltStrPrV) TVec<TAscFltStrPr>;
%template(TIntStrPrV) TVec<TIntStrPr>;
%template(TIntIntStrTrV) TVec<TIntIntStrTr>;
%template(TIntIntFltTrV) TVec<TIntIntFltTr>;
%template(TIntFltIntTrV) TVec<TIntFltIntTr>;
%template(TIntStrIntTrV) TVec<TIntStrIntTr>;
%template(TIntKdV) TVec<TIntKd>;
%template(TUIntIntKdV) TVec<TUIntIntKd>;
%template(TIntFltKdV) TVec<TIntFltKd>;
%template(TIntPrFltKdV) TVec<TIntPrFltKd>;
%template(TIntStrKdV) TVec<TIntStrKd>;
%template(TIntStrPrPrV) TVec<TIntStrPrPr>;
%template(TIntStrVPrV) TVec<TIntStrVPr>;
%template(TIntIntVIntTrV) TVec<TIntIntVIntTr>;
%template(TIntIntIntVTrV) TVec<TIntIntIntVTr>;
%template(TUInt64IntPrV) TVec<TUInt64IntPr>;
%template(TUInt64FltPrV) TVec<TUInt64FltPr>;
%template(TUInt64StrPrV) TVec<TUInt64StrPr>;
%template(TUInt64IntKdV) TVec<TUInt64IntKd>;
%template(TUInt64FltKdV) TVec<TUInt64FltKd>;
%template(TUInt64StrKdV) TVec<TUInt64StrKd>;
%template(TFltBoolKdV) TVec<TFltBoolKd>;
%template(TFltIntKdV) TVec<TFltIntKd>;
%template(TFltUInt64KdV) TVec<TFltUInt64Kd>;
%template(TFltIntPrKdV) TVec<TFltIntPrKd>;
%template(TFltKdV) TVec<TFltKd>;
%template(TFltStrKdV) TVec<TFltStrKd>;
%template(TFltStrPrPrV) TVec<TFltStrPrPr>;
%template(TFltIntIntTrV) TVec<TFltIntIntTr>;
%template(TFltFltStrTrV) TVec<TFltFltStrTr>;
%template(TAscFltIntPrV) TVec<TAscFltIntPr>;
%template(TAscFltIntKdV) TVec<TAscFltIntKd>;
%template(TStrPrV) TVec<TStrPr>;
%template(TStrIntPrV) TVec<TStrIntPr>;
%template(TStrFltPrV) TVec<TStrFltPr>;
%template(TStrIntKdV) TVec<TStrIntKd>;
%template(TStrFltKdV) TVec<TStrFltKd>;
%template(TStrAscFltKdV) TVec<TStrAscFltKd>;
%template(TStrTrV) TVec<TStrTr>;
%template(TStrQuV) TVec<TStrQu>;
%template(TStrFltFltTrV) TVec<TStrFltFltTr>;
%template(TStrStrIntTrV) TVec<TStrStrIntTr>;
%template(TStrKdV) TVec<TStrKd>;
%template(TStrStrVPrV) TVec<TStrStrVPr>;
%template(TStrVIntPrV) TVec<TStrVIntPr>;
%template(TFltIntIntIntQuV) TVec<TFltIntIntIntQu>;
%template(TIntStrIntIntQuV) TVec<TIntStrIntIntQu>;
%template(TIntIntPrPrV) TVec<TIntIntPrPr>;
%template(TIntVecPool) TVecPool<TInt>;
%template(PIntVecPool) TPt<TIntVecPool>;
%template(TFltVP) PVec<TFlt>;
%template(PFltV) TPt<TFltVP>;
%template(TAscFltVP) PVec<TAscFlt>;
%template(PAscFltV) TPt<TAscFltVP>;
%template(TStrVP) PVec<TStr>;
%template(PStrV) TPt<TStrVP>;
%template(TBoolVV) TVVec<TBool>;
%template(TChVV) TVVec<TCh>;
%template(TIntVV) TVVec<TInt>;
%template(TSFltVV) TVVec<TSFlt>;
%template(TFltVV) TVVec<TFlt>;
%template(TStrVV) TVVec<TStr>;
%template(TIntPrVV) TVVec<TIntPr>;
%template(TIntVVV) TVVVec<TInt>;
%template(TFltVVV) TVVVec<TFlt>;
%template(TIntTree) TTree<TInt>;
%template(TFltTree) TTree<TFlt>;
%template(TStrTree) TTree<TStr>;
%template(TStrIntPrTree) TTree<TStrIntPr>;
%template(TStrIntStrVTrTree) TTree<TStrIntStrVTr>;
%template(TIntS) TSStack<TInt>;
%template(TBoolChS) TSStack<TBoolChPr>;
%template(TIntQ) TQQueue<TInt>;
%template(TFltQ) TQQueue<TFlt>;
%template(TStrQ) TQQueue<TStr>;
%template(TIntPrQ) TQQueue<TIntPr>;
%template(TIntStrPrQ) TQQueue<TIntStrPr>;
%template(TFltVQ) TQQueue<TFltV>;
%template(TAscFltVQ) TQQueue<TAscFltV>;
//%template(TIntQV) TVec<TQQueue<TInt> >;
//%template(TIntL) TLst<TInt>;
//%template(TIntKdL) TLst<TIntKd>;
//%template(TFltL) TLst<TFlt>;
//%template(TFltIntKdL) TLst<TFltIntKd>;
//%template(TAscFltIntKdL) TLst<TAscFltIntKd>;
//%template(TStrL) TLst<TStr>;

// hash.h

//%template(TChChH) THash<TCh, TCh>;
//%template(TChTrIntH) THash<TChTr, TInt>;
%template(TIntH) THash<TInt, TInt>;
%template(TUInt64H) THash<TUInt64, TInt>;
%template(TIntBoolH) THash<TInt, TBool>;
%template(TIntIntH) THash<TInt, TInt>;
%template(TIntUInt64H) THash<TInt, TUInt64>;
//%template(TIntIntFltPrH) THash<TInt, TIntFltPr>;
%template(TIntIntVH) THash<TInt, TIntV>;
%template(TIntIntHH) THash<TInt, TIntH>;
%template(TIntFltH) THash<TInt, TFlt>;
%template(TIntFltPrH) THash<TInt, TFltPr>;
%template(TIntFltTrH) THash<TInt, TFltTr>;
%template(TIntFltVH) THash<TInt, TFltV>;
%template(TIntStrH) THash<TInt, TStr>;
%template(TIntStrVH) THash<TInt, TStrV>;
%template(TIntIntPrH) THash<TInt, TIntPr>;
%template(TIntIntPrVH) THash<TInt, TIntPrV>;
%template(TUInt64StrVH) THash<TUInt64, TStrV>;
%template(TIntPrIntH) THash<TIntPr, TInt>;
%template(TIntPrIntVH) THash<TIntPr, TIntV>;
%template(TIntPrIntPrVH) THash<TIntPr, TIntPrV>;
%template(TIntTrIntH) THash<TIntTr, TInt>;
%template(TIntVIntH) THash<TIntV, TInt>;
%template(TUIntH) THash<TUInt, TUInt>;
%template(TIntPrIntH) THash<TIntPr, TInt>;
%template(TIntPrIntVH) THash<TIntPr, TIntV>;
%template(TIntPrFltH) THash<TIntPr, TFlt>;
%template(TIntTrFltH) THash<TIntTr, TFlt>;
%template(TIntPrStrH) THash<TIntPr, TStr>;
%template(TIntPrStrVH) THash<TIntPr, TStrV>;
%template(TIntStrPrIntH) THash<TIntStrPr, TInt>;
%template(TFltFltH) THash<TFlt, TFlt>;
%template(TStrH) THash<TStr, TInt>;
%template(TStrBoolH) THash<TStr, TBool>;
%template(TStrIntH) THash<TStr, TInt>;
%template(TStrIntPrH) THash<TStr, TIntPr>;
%template(TStrIntVH) THash<TStr, TIntV>;
%template(TStrUInt64H) THash<TStr, TUInt64>;
%template(TStrUInt64VH) THash<TStr, TUInt64V>;
%template(TStrIntPrVH) THash<TStr, TIntPrV>;
%template(TStrFltH) THash<TStr, TFlt>;
%template(TStrFltVH) THash<TStr, TFltV>;
%template(TStrStrH) THash<TStr, TStr>;
%template(TStrStrPrH) THash<TStr, TStrPr>;
%template(TStrStrVH) THash<TStr, TStrV>;
%template(TStrStrPrVH) THash<TStr, TStrPrV>;
%template(TStrStrKdVH) THash<TStr, TStrKdV>;
%template(TStrIntFltPrH) THash<TStr, TIntFltPr>;
%template(TStrStrIntPrVH) THash<TStr, TStrIntPrV>;
%template(TStrStrIntKdVH) THash<TStr, TStrIntKdV>;
//%template(TDbStrIntH) THash<TDbStr, TInt>;
//%template(TDbStrStrH) THash<TDbStr, TStr>;
%template(TStrPrBoolH) THash<TStrPr, TBool>;
%template(TStrPrIntH) THash<TStrPr, TInt>;
%template(TStrPrFltH) THash<TStrPr, TFlt>;
%template(TStrPrStrH) THash<TStrPr, TStr>;
%template(TStrPrStrVH) THash<TStrPr, TStrV>;
%template(TStrTrIntH) THash<TStrTr, TInt>;
%template(TStrIntPrIntH) THash<TStrIntPr, TInt>;
%template(TStrVH) THash<TStrV, TInt>;
//%template(TStrVIntH) THash<TStrV, TInt>;
%template(TStrVIntVH) THash<TStrV, TIntV>;
%template(TStrVStrH) THash<TStrV, TStr>;
%template(TStrVStrVH) THash<TStrV, TStrV>;
//%template(TStrSH) TStrHash<TInt>;
//%template(TStrIntSH) TStrHash<TInt>;
//%template(TStrToIntVSH) TStrHash<TIntV>;

// dt.h

%template(TStrV) TVec<TStr, int>;

// tm.h

//%template(TSecTmV) TVec<TSecTm>;
//%template(TSecTmStrKd) TKeyDat<TSecTm, TStr>;
//%template(TSecTmStrKdV) TVec<TSecTmStrKd>;
//%template(TTmV) TVec<TTm>;
////%template(TTmStrPr) TPair<TTm, TStr>;
////%template(TStrTmPr) TPair<TStr, TTm>;
//%template(TTmStrPrV) TVec<TTmStrPr>;
//%template(TStrTmPrV) TVec<TStrTmPr>;

//----------

// Python-SNAP conversion typemaps

%include "snapswig.h"
%include "goodgraph.cpp"
%include "printgraph.h"

/* Include other SWIG interface types here. */

/* Vector and hash interface */
%include "tvec.i"
%include "thash.i"

/* Graph and network interface */
%include "pneanet.i"
%include "pngraph.i"
%include "pungraph.i"
%include "pgraph.i"

