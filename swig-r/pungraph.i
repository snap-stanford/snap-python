// pungraph.i
// Templates for SNAP

// Note: This file does not include all SNAP templates.

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

// Basic Undirected Graphs
%template(PUNGraph) TPt< TUNGraph >;

%template(LoadEdgeList_PUNGraph) TSnap::LoadEdgeList<PUNGraph>;
%template(PrintGraphStatTable_PUNGraph) PrintGraphStatTable<PUNGraph>;

%template(NodesGTEDegree_PUNGraph) NodesGTEDegree<PUNGraph>;
%template(GenRndGnm_PUNGraph) TSnap::GenRndGnm<PUNGraph>;
%template(MxSccSz_PUNGraph) TSnap::GetMxScc<PUNGraph>;
%template(MxWccSz_PUNGraph) TSnap::GetMxWccSz<PUNGraph>;
%template(MxDegree_PUNGraph) MxDegree<PUNGraph>;
// End Basic Undirected Graphs
