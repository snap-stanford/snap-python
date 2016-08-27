// tmodenet.i
// Templates for SNAP TModeNet
//

%extend TModeNet {
        TModeNetNodeI BegMMNI() {
          return TModeNetNodeI($self->BegMMNI());
        }
        TModeNetNodeI EndMMNI() {
          return TModeNetNodeI($self->EndMMNI());
        }
        TModeNetNodeI GetMMNI(const int &NId) {
          return TModeNetNodeI($self->GetMMNI(NId));
        }
};

