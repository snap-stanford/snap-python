// snap.i

//   PNEANet, PUNGraph, PNGraph are supported,
//     along with standard SNAP functions.

// set to 1 for release to include all the functions (long compile)
// set to 0 for development to include limited functions (shorter compile)
#define SNAP_ALL 0

%pythoncode %{
Version = "5.2.0"
%}

%module snap

%{

#include "Snap.h"
//#include "cliques.h"
//#include "agm.h"
//#include "agmfast.h"
//#include "agmfit.h"
//#include "n2v.h"
 
/* #include "Engine.h" */
#include "snapswig.h"

#include "printgraph.h"
#include "snap_types.h"
#include "goodgraph.cpp"
#include "linkpred_swig.h"

%}

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

%ignore TInt::GetStr;
%ignore TPair::GetStr;

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
%ignore TDirNet::GetEI(int const&) const;
%ignore TUndirNet::GetEI(int const&) const;

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

%ignore TPair< TStr,TAttrType >::Load;
%ignore TPair< TStr,TAttrType >::Save;
%ignore TPair< TStr,TAttrType >::GetMemUsed;
%ignore TPair< TStr,TAttrType >::GetPrimHashCd;
%ignore TPair< TStr,TAttrType >::GetSecHashCd;
%ignore TPair< TStr,TAttrType >::TPair(TSIn &);

//%ignore TVec< TPair< TStr, TAttrType_ >, int >::Load;
//%ignore TVec< TPair< TStr, TAttrType >, int >::Load;
%ignore TVec< TPair< TStr,TAttrType > >::Load;
%ignore TVec< TPair< TStr,TAttrType > >::Save;
%ignore TVec< TPair< TStr,TAttrType > >::GetPrimHashCd;
%ignore TVec< TPair< TStr,TAttrType > >::GetSecHashCd;
//%ignore TVec< TPair< TStr,TAttrType > >::TVec(TSIn *);
%ignore TVec< TPair< TStr,TAttrType > >::TVec(TSIn &);
//%ignore Schema::Load;

%ignore TVec<PNEANet>::Intrs;
%ignore TVec<PNEANet>::IntrsLen;
%ignore TVec<PNEANet>::AddSorted;
%ignore TVec<PNEANet>::AddBackSorted;
%ignore TVec<PNEANet>::AddMerged;
%ignore TVec<PNEANet>::AddVMerged;
%ignore TVec<PNEANet>::AddUnique;
%ignore TVec<PNEANet>::SearchBack;
%ignore TVec<PNEANet>::SearchBin;
%ignore TVec<PNEANet>::SearchBinLeft;
%ignore TVec<PNEANet>::SearchForw;
%ignore TVec<PNEANet>::SearchVForw;
%ignore TVec<PNEANet>::Merge;
%ignore TVec<PNEANet>::Count;
%ignore TVec<PNEANet>::Diff;
%ignore TVec<PNEANet>::Union;
%ignore TVec<PNEANet>::PrevPerm;
%ignore TVec<PNEANet>::NextPerm;
%ignore TVec<PNEANet>::DelAll;
%ignore TVec<PNEANet>::DelIfIn;
%ignore TVec<PNEANet>::GetPivotValN;
%ignore TVec<PNEANet>::BSort;
%ignore TVec<PNEANet>::ISort;
%ignore TVec<PNEANet>::QSort;
%ignore TVec<PNEANet>::Sort;
%ignore TVec<PNEANet>::IsSorted;
%ignore TVec<PNEANet>::IsIn;
%ignore TVec<PNEANet>::IsInBin;
%ignore TVec<PNEANet>::Partition;
%ignore TVec<PNEANet>::operator<;
%ignore TVec<PNEANet>::operator==;
%ignore TVec<PNEANet>::operator!=;
%ignore TVec<PNEANet>::GetPrimHashCd;
%ignore TVec<PNEANet>::GetSecHashCd;
%ignore TVec<PNEANet>::GetDat;
%ignore TVec<PNEANet>::UnionLen;
%ignore TVec<PNEANet>::GetAddDat;
%ignore TVec<PNEANet>::GetMxValN;
%ignore TVec<PNEANet>::CopyUniqueFrom;
// TODO: maybe the line below could work
//%rename("regex:/TVec<PNEANet>::(?!(GetVal|operator\[\]|Len))/$ignore/") "";

// ignore all THash::AddDatId, MarkDelKey, MarkDelKeyId
%ignore THash::AddDatId;
%ignore THash::MarkDelKey;
%ignore THash::MarkDelKeyId;

// ignore overloaded methods for TTable row iterators
%ignore TRowIterator::GetIntAttr(TInt) const;
%ignore TRowIterator::GetFltAttr(TInt) const;
%ignore TRowIterator::GetStrAttr(TInt) const;
%ignore TRowIteratorWithRemove::GetNextIntAttr(TInt) const;
%ignore TRowIteratorWithRemove::GetNextFltAttr(TInt) const;
%ignore TRowIteratorWithRemove::GetNextStrAttr(TInt) const;

// Python-C++ conversion typemaps

%include "snap_types.i"

%include exception.i

%exception {
    try {
        $action
    } catch (PExcept Except) {
        SWIG_exception(SWIG_UnknownError,Except->GetMsgStr().CStr());
    }
}

#define GLib_UNIX
// glib-core
%include "bd.h"
%include "ds.h"
%include "dt.h"
%include "fl.h"
//%include "tm.h"
%include "ut.h"

// SNAP Library
// snap-core
%include "gbase.h"
%include "util.h"

// representations
%include "hash.h"
%include "hashmp.h"
%include "shash.h"
%include "graph.h"
%include "graphmp.h"
%include "network.h"
%include "mmnet.h"
%include "networkmp.h"
%include "table.h"
%include "attr.h"

// algorithms
%include "alg.h"
%include "anf.h"
%include "bfsdfs.h"
%include "centr.h"
%include "cmty.h"
%include "cncom.h"
%include "ff.h"
%include "gsvd.h"
%include "gio.h"
%include "gviz.h"
%include "kcore.h"
%include "ggen.h"
%include "subgraph.h"
%include "util.h"
%include "triad.h"
%include "statplot.h"
//%include "cliques.h"
//%include "agm.h"
//%include "agmfast.h"
//%include "agmfit.h"
//%include "n2v.h"

//%template(Schema) TVec< TPair< TStr, TAttrType> >;
//%template(Schema) TVec< TPair< TStr, TAttrType_> >;

// SNAP type definitions

//%template(Schema) TVec<TPair<TStr, TInt> >;

// ds.h

%template(TIntPr) TPair<TInt, TInt>;
%template(TFltPr) TPair<TFlt, TFlt>;
%template(TStrIntPr) TPair<TStr, TInt>;
%template(TIntTr) TTriple<TInt, TInt, TInt>;
%template(TIntFltKd) TKeyDat<TInt, TFlt>;
%template(TIntStrPr) TPair<TInt, TStr>;

%template(TIntV) TVec<TInt>;
%template(TFltV) TVec<TFlt>;
%template(TStrV) TVec<TStr>;
%template(TIntPrV) TVec<TIntPr>;
%template(TFltPrV) TVec<TFltPr>;
%template(TStrIntPrV) TVec<TStrIntPr>;
%template(TIntTrV) TVec<TIntTr>;
%template(TIntFltKdV) TVec<TIntFltKd>;
%template(TIntIntVV) TVec< TVec< TInt, int >, int >;
%template(TFltVFltV) TVec<TFltV>;
%template(PNEANetV) TVec<PNEANet>;

#if SNAP_ALL
//%template(TBoolChPr) TPair<TBool, TCh>;
%template(TBoolFltPr) TPair<TBool, TFlt>;
//%template(TUChIntPr) TPair<TUCh, TInt>;
//%template(TUChUInt64Pr) TPair<TUCh, TUInt64>;
//%template(TUChStrPr) TPair<TUCh, TStr>;
%template(TIntBoolPr) TPair<TInt, TBool>;
//%template(TIntChPr) TPair<TInt, TCh>;
%template(TIntUInt64Pr) TPair<TInt, TUInt64>;
%template(TIntIntPrPr) TPair<TInt, TIntPr>;
%template(TIntIntVPr) TPair<TInt, TVec<TInt, int> >;
%template(TIntFltPr) TPair<TInt, TFlt>;
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
%template(TUInt64V) TVec<TUInt64>;
%template(TSFltV) TVec<TSFlt>;
%template(TAscFltV) TVec<TAscFlt>;
%template(TStrV) TVec<TStr>;
%template(TChAV) TVec<TChA>;
%template(TIntQuV) TVec<TIntQu>;
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
%template(TIntStrStrTrV) TVec<TIntStrStrTr>;
%template(TIntKdV) TVec<TIntKd>;
%template(TUIntIntKdV) TVec<TUIntIntKd>;
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
#endif

// hash.h

// define hash types
%template(TIntH) THash<TInt, TInt>;
%template(TIntIntH) THash<TInt, TInt>;
%template(TIntFltH) THash<TInt, TFlt>;
%template(TIntStrH) THash<TInt, TStr>;
%template(TIntPrFltH) THash<TIntPr, TFlt>;
%template(TStrIntH) THash<TStr, TInt>;
%template(TStrIntSH) TStrHash<TInt, TStrPool, TDefaultHashFunc<TStr> >;

// define keydat types
%template(TIntHI) THashKeyDatI <TInt, TInt>;
%template(TIntIntHI) THashKeyDatI <TInt, TInt>;
%template(TIntFltHI) THashKeyDatI <TInt, TFlt>;
%template(TIntStrHI) THashKeyDatI <TInt, TStr>;
%template(TIntPrFltHI) THashKeyDatI <TIntPr, TFlt>;
%template(TStrIntHI) THashKeyDatI <TStr, TInt>;
%template(TIntFltVH) THash<TInt, TFltV>;

#if SNAP_ALL
// define hash types
//%template(TChChH) THash<TCh, TCh>;
//%template(TChTrIntH) THash<TChTr, TInt>;
%template(TUInt64H) THash<TUInt64, TInt>;
%template(TIntBoolH) THash<TInt, TBool>;
%template(TIntUInt64H) THash<TInt, TUInt64>;
//%template(TIntIntFltPrH) THash<TInt, TIntFltPr>;
%template(TIntIntVH) THash<TInt, TIntV>;
%template(TIntIntHH) THash<TInt, TIntH>;
%template(TIntFltPrH) THash<TInt, TFltPr>;
%template(TIntFltTrH) THash<TInt, TFltTr>;
%template(TIntStrVH) THash<TInt, TStrV>;
%template(TIntIntPrH) THash<TInt, TIntPr>;
%template(TIntIntPrVH) THash<TInt, TIntPrV>;
%template(TIntStrPrVH) THash<TInt, TStrPrV>;
%template(TUInt64StrVH) THash<TUInt64, TStrV>;
%template(TIntPrIntH) THash<TIntPr, TInt>;
%template(TIntPrIntVH) THash<TIntPr, TIntV>;
%template(TIntPrIntPrVH) THash<TIntPr, TIntPrV>;
%template(TIntTrIntH) THash<TIntTr, TInt>;
%template(TIntVIntH) THash<TIntV, TInt>;
%template(TUIntH) THash<TUInt, TUInt>;
%template(TIntPrIntH) THash<TIntPr, TInt>;
%template(TIntPrIntVH) THash<TIntPr, TIntV>;
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

// define keydat types
//%template(TChChHI) THashKeyDatI <TCh, TCh>;
//%template(TChTrIntHI) THashKeyDatI <TChTr, TInt>;
%template(TUInt64HI) THashKeyDatI <TUInt64, TInt>;
%template(TIntBoolHI) THashKeyDatI <TInt, TBool>;
%template(TIntHI) THashKeyDatI <TInt, TInt>;
%template(TIntUInt64HI) THashKeyDatI <TInt, TUInt64>;
//%template(TIntIntFltPrHI) THashKeyDatI <TInt, TIntFltPr>;
%template(TIntIntVHI) THashKeyDatI <TInt, TIntV>;
%template(TIntIntHHI) THashKeyDatI <TInt, TIntH>;
%template(TIntFltPrHI) THashKeyDatI <TInt, TFltPr>;
%template(TIntFltTrHI) THashKeyDatI <TInt, TFltTr>;
%template(TIntFltVHI) THashKeyDatI <TInt, TFltV>;
%template(TIntStrVHI) THashKeyDatI <TInt, TStrV>;
%template(TIntIntPrHI) THashKeyDatI <TInt, TIntPr>;
%template(TIntIntPrVHI) THashKeyDatI <TInt, TIntPrV>;
%template(TIntStrPrVHI) THashKeyDatI <TInt, TStrPrV>;
%template(TUInt64StrVHI) THashKeyDatI <TUInt64, TStrV>;
%template(TIntPrIntHI) THashKeyDatI <TIntPr, TInt>;
%template(TIntPrIntVHI) THashKeyDatI <TIntPr, TIntV>;
%template(TIntPrIntPrVHI) THashKeyDatI <TIntPr, TIntPrV>;
%template(TIntTrIntHI) THashKeyDatI <TIntTr, TInt>;
%template(TIntVIntHI) THashKeyDatI <TIntV, TInt>;
%template(TUIntHI) THashKeyDatI <TUInt, TUInt>;
%template(TIntPrIntHI) THashKeyDatI <TIntPr, TInt>;
%template(TIntPrIntVHI) THashKeyDatI <TIntPr, TIntV>;
%template(TIntTrFltHI) THashKeyDatI <TIntTr, TFlt>;
%template(TIntPrStrHI) THashKeyDatI <TIntPr, TStr>;
%template(TIntPrStrVHI) THashKeyDatI <TIntPr, TStrV>;
%template(TIntStrPrIntHI) THashKeyDatI <TIntStrPr, TInt>;
%template(TFltFltHI) THashKeyDatI <TFlt, TFlt>;
%template(TStrHI) THashKeyDatI <TStr, TInt>;
%template(TStrBoolHI) THashKeyDatI <TStr, TBool>;
%template(TStrIntHI) THashKeyDatI <TStr, TInt>;
%template(TStrIntPrHI) THashKeyDatI <TStr, TIntPr>;
%template(TStrIntVHI) THashKeyDatI <TStr, TIntV>;
%template(TStrUInt64HI) THashKeyDatI <TStr, TUInt64>;
%template(TStrUInt64VHI) THashKeyDatI <TStr, TUInt64V>;
%template(TStrIntPrVHI) THashKeyDatI <TStr, TIntPrV>;
%template(TStrFltHI) THashKeyDatI <TStr, TFlt>;
%template(TStrFltVHI) THashKeyDatI <TStr, TFltV>;
%template(TStrStrHI) THashKeyDatI <TStr, TStr>;
%template(TStrStrPrHI) THashKeyDatI <TStr, TStrPr>;
%template(TStrStrVHI) THashKeyDatI <TStr, TStrV>;
%template(TStrStrPrVHI) THashKeyDatI <TStr, TStrPrV>;
%template(TStrStrKdVHI) THashKeyDatI <TStr, TStrKdV>;
%template(TStrIntFltPrHI) THashKeyDatI <TStr, TIntFltPr>;
%template(TStrStrIntPrVHI) THashKeyDatI <TStr, TStrIntPrV>;
%template(TStrStrIntKdVHI) THashKeyDatI <TStr, TStrIntKdV>;
//%template(TDbStrIntHI) THashKeyDatI <TDbStr, TInt>;
//%template(TDbStrStrHI) THashKeyDatI <TDbStr, TStr>;
%template(TStrPrBoolHI) THashKeyDatI <TStrPr, TBool>;
%template(TStrPrIntHI) THashKeyDatI <TStrPr, TInt>;
%template(TStrPrFltHI) THashKeyDatI <TStrPr, TFlt>;
%template(TStrPrStrHI) THashKeyDatI <TStrPr, TStr>;
%template(TStrPrStrVHI) THashKeyDatI <TStrPr, TStrV>;
%template(TStrTrIntHI) THashKeyDatI <TStrTr, TInt>;
%template(TStrIntPrIntHI) THashKeyDatI <TStrIntPr, TInt>;
%template(TStrVHI) THashKeyDatI <TStrV, TInt>;
//%template(TStrVIntHI) THashKeyDatI <TStrV, TInt>;
%template(TStrVIntVHI) THashKeyDatI <TStrV, TIntV>;
%template(TStrVStrHI) THashKeyDatI <TStrV, TStr>;
%template(TStrVStrVHI) THashKeyDatI <TStrV, TStrV>;
//%template(TStrSHI) TStrHashKeyDatI <TInt>;
//%template(TStrIntSHI) TStrHashKeyDatI <TInt>;
#endif

// dt.h

%template(TStrV) TVec<TStr, int>;

// cncom.h

%template(TCnComV) TVec<TCnCom>;

// tm.h

//%template(TSecTmV) TVec<TSecTm>;
//%template(TSecTmStrKd) TKeyDat<TSecTm, TStr>;
//%template(TSecTmStrKdV) TVec<TSecTmStrKd>;
//%template(TTmV) TVec<TTm>;
////%template(TTmStrPr) TPair<TTm, TStr>;
////%template(TStrTmPr) TPair<TStr, TTm>;
//%template(TTmStrPrV) TVec<TTmStrPr>;
//%template(TStrTmPrV) TVec<TStrTmPr>;

// table.h

//%template(Schema) TVec<TPair<TStr, TAttrType> >;
//typedef TStrIntPrV Schema;

%template(TStrTAttrPr) TPair< TStr, TAttrType>;
%template(Schema) TVec< TPair< TStr, TAttrType> >;

%template(TIntSet) THashSet<TInt>;
%template(TIntHSI) THashSetKeyI <TInt>;

//----------

// SWIG conversion C++ code

%include "snapswig.h"
%include "goodgraph.cpp"
%include "printgraph.h"
%include "linkpred_swig.h"
%include "conv.h"

%template(GetRndWalkRestart_PUNGraph) GetRndWalkRestart<PUNGraph>;
%template(GetRndWalkRestart_PNGraph) GetRndWalkRestart<PNGraph>;
%template(GetRndWalkRestart_PNEANet) GetRndWalkRestart<PNEANet>;

/* Include other SWIG interface types here. */

/* Vector and hash interface */
%include "tvec.i"
%include "thash.i"
%include "thashset.i"

/* Graph and network interface */
%include "pneanet.i"
%include "tmodenet.i"
%include "tcrossnet.i"
%include "pmmnet.i"
%include "pngraph.i"
%include "pungraph.i"
%include "pdirnet.i"
%include "pundirnet.i"

#ifdef GCC_ATOMIC
%include "pngraphmp.i"
%include "pneanetmp.i"
#endif

%include "pgraph.i"
#ifndef NONUMPY
%include "numpy_swig.i"
#endif

/* table interface */
%include "ptable.i"

/* enhanced Python functionality */
%include "pylayer.i"

%template(PTable) TPt< TTable >;

// note for operator renaming
// %rename(Add) Vector3::operator +;

