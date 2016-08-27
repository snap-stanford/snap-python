// pneanetmp.i
// Templates for SNAP TNEANetMP, PNEANetMP

%extend TNEANetMP {
        TNEANetMPNodeI BegNI() {
                return TNEANetMPNodeI($self->BegNI());
        }
        TNEANetMPNodeI EndNI() {
                return TNEANetMPNodeI($self->EndNI());
        }
        TNEANetMPNodeI GetNI(const int &NId) {
                return TNEANetMPNodeI($self->GetNI(NId));
        }
        TNEANetMPEdgeI BegEI() {
                return TNEANetMPEdgeI($self->BegEI());
        }
        TNEANetMPEdgeI EndEI() {
                return TNEANetMPEdgeI($self->EndEI());
        }
};

%pythoncode %{
# redefine TNEANetMPEdgeI.GetId to return a pair of nodes rather than -1
def GetId(self):
    return (self.GetSrcNId(), self.GetDstNId())

TNEANetMPEdgeI.GetId = GetId
%}

#ifdef _OPENMP
%pythoncode %{
def ToNetworkMP(tspec, *args):
    if tspec == PNEANetMP : return ToNetworkMP_PNEANetMP(*args)
    return None

def ToNetworkMP2(tspec, *args):
    if tspec == PNEANetMP : return ToNetworkMP2_PNEANetMP(*args)
    return None
%}
#endif



// Basic Undirected Graphs

%template(PrintGraphStatTable_PNEANetMP) PrintGraphStatTable<PNEANetMP>;

//%template(MxSccSz_PNEANetMP) TSnap::GetMxScc<PNEANetMP>;
//%template(MxWccSz_PNEANetMP) TSnap::GetMxWccSz<PNEANetMP>;
// End Basic Directed Graphs

// Basic PNEANetMPs
%template(PNEANetMP) TPt< TNEANetMP >;
// conv.h - PNGraph
#ifdef _OPENMP
%template(ToNetworkMP_PNEANetMP) TSnap::ToNetworkMP<PNEANetMP>;
%template(ToNetworkMP2_PNEANetMP) TSnap::ToNetworkMP2<PNEANetMP>;
#endif

