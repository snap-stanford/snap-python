// snap.i
%module snap
%{
#include "Snap.h"
#include "snapsw.h"
#include "printgraph.h"
#include "snapswig.h"
%}

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
%ignore TFile::GetLastAccessTm;

%ignore TNGraph::GetEI(int const&) const;
%ignore TBPGraph::HasFlag(const TGraphFlag& Flag) const;
%ignore TNEGraph::GetSmallGraph();
%ignore TBPGraph::GetEI(int const&) const;
%ignore TUNGraph::GetEI(int const&) const;

//%ignore TNGraphNodeI::TNGNodeI;

%ignore TVec<TVec<TInt, int>, int>::Add;
%ignore TVec<TVec<TInt, int>, int>::AddMerged;

%ignore THash< TInt, TVec< TInt, int > >::AddDat;
%ignore THash< TInt, TVec< TInt, int > >::HashPrimeT;
%ignore THash< TInt, TVec< TInt, int > >::AddDatId;

%ignore THash< TInt, TInt, TDefaultHashFunc<TInt> >::HashPrimeT;
%ignore THash< TInt, TInt, TDefaultHashFunc<TInt> >::AddDatId;
%ignore THash< TInt, TInt>::HashPrimeT;

%include "bd.h"
%include "dt.h"
%include "ds.h"
%include "fl.h"
%include "graph.h"
%include "gio.h"
%include "hash.h"
%include "ggen.h"

%include "snapsw.h"
%include "printgraph.h"
%include "snapswig.h"

// TODO can BegNI() be renamed?

%extend TNGraph {
        TNGraphNodeI BegNI() {
                return TNGraphNodeI($self->BegNI());
        }
        TNGraphNodeI EndNI() {
                return TNGraphNodeI($self->EndNI());
        }
        TNGraphEdgeI BegEI() {
                return TNGraphEdgeI($self->BegEI());
        }
        TNGraphEdgeI EndEI() {
                return TNGraphEdgeI($self->EndEI());
        }
};

%extend TUNGraph {
        TUNGraphNodeI BegNI() {
                return TUNGraphNodeI($self->BegNI());
        }
        TUNGraphNodeI EndNI() {
                return TUNGraphNodeI($self->EndNI());
        }
        TUNGraphEdgeI BegEI() {
                return TUNGraphEdgeI($self->BegEI());
        }
        TUNGraphEdgeI EndEI() {
                return TUNGraphEdgeI($self->EndEI());
        }
};

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

%template(PNGraph) TPt< TNGraph >;
%template(LoadEdgeList_PNGraph) TSnap::LoadEdgeList<PNGraph>;
%template(GenRndGnm_PNGraph) TSnap::GenRndGnm<PNGraph>;
%template(PrintGraphStatTable_PNGraph) PrintGraphStatTable<PNGraph>;

