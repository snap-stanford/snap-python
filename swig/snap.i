// snap.i
%module snap
%{
#include "Snap.h"

#include "printgraph.h"
#include "snapswig.h"

#include "goodgraph.cpp"
#include "getassessment.cpp"
//#include "demo-TNEAGraph.cpp"

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
%ignore TNEAGraph::GetSmallGraph();
%ignore TBPGraph::GetEI(int const&) const;
%ignore TUNGraph::GetEI(int const&) const;

%include "bd.h"
%include "dt.h"
%include "fl.h"
%include "graph.h"
%include "cncom.h"
%include "ggen.h"
%include "gio.h"

%include "printgraph.h"
%include "snapswig.h"

%include "goodgraph.cpp"
%include "getassessment.cpp"
//%include "demo-TNEAGraph.cpp"


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

%template(PercentDegree_PNGraph) PercentDegree<PNGraph>;
%template(PercentMxWcc_PNGraph) PercentMxWcc<PNGraph>;
%template(PercentMxScc_PNGraph) PercentMxScc<PNGraph>;

// Directed Graphs
%template(GenRndGnm_PNGraph) TSnap::GenRndGnm<PNGraph>;
//%template(GenRMat) TSnap::GenRMat;

// Undirected Graphs
%template(GenRndGnm_PUNGraph) TSnap::GenRndGnm<PUNGraph>;
//%template(GenPrefAttach) TSnap::GenPrefAttach;
//%template(GenSmallWorld) TSnap::GenSmallWorld;
%template(MxWccSz_PUNGraph) TSnap::GetMxWccSz<PUNGraph>;
%template(MxSccSz_PUNGraph) TSnap::GetMxScc<PUNGraph>;


%template(MxWccSz_PNGraph) TSnap::GetMxWccSz<PNGraph>;
%template(MxSccSz_PNGraph) TSnap::GetMxScc<PNGraph>;

%template(NodesGTEDegree_PNGraph) NodesGTEDegree<PNGraph>;
%template(MxDegree_PNGraph) MxDegree<PNGraph>;

//%template(GetStats_PNGraph) TSnap::GetStats<PNGraph>;

