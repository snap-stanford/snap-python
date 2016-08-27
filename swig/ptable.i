// ptable.i
// Templates for SNAP, common functions to TTable

// Basic PTable
%template(PTable) TPt< TTable >;

%pythoncode %{


#
# redefine some methods to use T... class not P... class
#

def Save(self,*args):
    self().Save(*args)

#
# define generator and redirection methods
#

PTable.Save = Save

%}

