// tcrossnet.i
// Templates for SNAP TCrossNet, PNEANet
//

%extend TCrossNet {
        TCrossNetEdgeI BegEI() {
          return TCrossNetEdgeI($self->BegEdgeI());
        }
        TCrossNetEdgeI EndEI() {
          return TCrossNetEdgeI($self->EndEdgeI());
        }
  
        TCrossNetAIntI BegEAIntI(const TStr& attr) {
          return TCrossNetAIntI($self->BegEAIntI(attr));
        }
        TCrossNetAIntI EndEAIntI(const TStr& attr) {
          return TCrossNetAIntI($self->EndEAIntI(attr));
        }
        
        TCrossNetAStrI BegEAStrI(const TStr& attr) {
          return TCrossNetAStrI($self->BegEAStrI(attr));
        }
        TCrossNetAStrI EndEAStrI(const TStr& attr) {
          return TCrossNetAStrI($self->EndEAStrI(attr));
        }
        
        TCrossNetAFltI BegEAFltI(const TStr& attr) {
          return TCrossNetAFltI($self->BegEAFltI(attr));
        }
        TCrossNetAFltI EndEAFltI(const TStr& attr) {
          return TCrossNetAFltI($self->EndEAFltI(attr));
        }
  
};
