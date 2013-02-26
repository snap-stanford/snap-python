// snap.i
%module snap
%{
#include "Snap.h"

#include "printgraph.h"
#include "snapswig.h"

#include "getassessment.cpp"
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
%ignore TFile::Copy;
%ignore TFile::GetLastAccessTm;
%ignore TFile::GetLastWriteTm;
%ignore TFile::GetCreateTm;
%ignore TFile::GetSize;

%ignore TNGraph::GetEI(int const&) const;
%ignore TBPGraph::HasFlag(const TGraphFlag& Flag) const;
%ignore TNEGraph::GetSmallGraph();
%ignore TBPGraph::GetEI(int const&) const;
%ignore TUNGraph::GetEI(int const&) const;

//%ignore TNGraphNodeI::TNGNodeI;

%include "bd.h"
%include "dt.h"
%include "fl.h"
%include "graph.h"
%include "gio.h"

%include "printgraph.h"
%include "snapswig.h"
%include "getassessment.cpp"    // For code-completion in Xcode

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

%template(PNGraph) TPt< TNGraph >;
%template(LoadEdgeList_PNGraph) TSnap::LoadEdgeList<PNGraph>;
%template(PrintGraphStatTable_PNGraph) PrintGraphStatTable<PNGraph>;
%template(GetStats_PNGraph) TSnap::GetStats<PNGraph>;

