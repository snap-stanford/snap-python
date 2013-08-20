%pythoncode %{

#
# define __getitem__ for [] addressing
#

def getitem(self, i):
    return self.GetVal(i)

#
# define iterator for TVec
#

class IterVec:
    def __init__(self, vec):
        self.vec = vec
        self.count = -1

    def __iter__(self):
        return self

    def next(self):
        if self.count+1 < self.vec.Len():
            self.count += 1
            return self.vec[self.count]

        raise StopIteration

def itervec(self):
    return IterVec(self)

TIntV.__iter__ = itervec

#TBoolV.__getitem__ = getitem
#TChV.__getitem__ = getitem
#TUChV.__getitem__ = getitem
#TUIntV.__getitem__ = getitem
TIntV.__getitem__ = getitem
#TUInt64V.__getitem__ = getitem
#TFltV.__getitem__ = getitem
#TSFltV.__getitem__ = getitem
#TAscFltV.__getitem__ = getitem
#TStrV.__getitem__ = getitem
#TChAV.__getitem__ = getitem
#TIntPrV.__getitem__ = getitem
#TIntTrV.__getitem__ = getitem
#TIntQuV.__getitem__ = getitem
#TFltPrV.__getitem__ = getitem
#TFltTrV.__getitem__ = getitem
#TIntKdV.__getitem__ = getitem
#TUChIntPrV.__getitem__ = getitem
#TUChUInt64PrV.__getitem__ = getitem
#TIntUInt64PrV.__getitem__ = getitem
#TIntUInt64KdV.__getitem__ = getitem
#TIntFltPrV.__getitem__ = getitem
#TIntFltPrKdV.__getitem__ = getitem
#TFltIntPrV.__getitem__ = getitem
#TFltUInt64PrV.__getitem__ = getitem
#TFltStrPrV.__getitem__ = getitem
#TAscFltStrPrV.__getitem__ = getitem
#TIntStrPrV.__getitem__ = getitem
#TIntIntStrTrV.__getitem__ = getitem
#TIntIntFltTrV.__getitem__ = getitem
#TIntFltIntTrV.__getitem__ = getitem
#TIntStrIntTrV.__getitem__ = getitem
#TIntKdV.__getitem__ = getitem
#TUIntIntKdV.__getitem__ = getitem
#TIntFltKdV.__getitem__ = getitem
#TIntPrFltKdV.__getitem__ = getitem
#TIntStrKdV.__getitem__ = getitem
#TIntStrPrPrV.__getitem__ = getitem
#TIntStrVPrV.__getitem__ = getitem
#TIntIntVIntTrV.__getitem__ = getitem
#TIntIntIntVTrV.__getitem__ = getitem
#TUInt64IntPrV.__getitem__ = getitem
#TUInt64FltPrV.__getitem__ = getitem
#TUInt64StrPrV.__getitem__ = getitem
#TUInt64IntKdV.__getitem__ = getitem
#TUInt64FltKdV.__getitem__ = getitem
#TUInt64StrKdV.__getitem__ = getitem
#TFltBoolKdV.__getitem__ = getitem
#TFltIntKdV.__getitem__ = getitem
#TFltUInt64KdV.__getitem__ = getitem
#TFltIntPrKdV.__getitem__ = getitem
#TFltKdV.__getitem__ = getitem
#TFltStrKdV.__getitem__ = getitem
#TFltStrPrPrV.__getitem__ = getitem
#TFltIntIntTrV.__getitem__ = getitem
#TFltFltStrTrV.__getitem__ = getitem
#TAscFltIntPrV.__getitem__ = getitem
#TAscFltIntKdV.__getitem__ = getitem
#TStrPrV.__getitem__ = getitem
#TStrIntPrV.__getitem__ = getitem
#TStrFltPrV.__getitem__ = getitem
#TStrIntKdV.__getitem__ = getitem
#TStrFltKdV.__getitem__ = getitem
#TStrAscFltKdV.__getitem__ = getitem
#TStrTrV.__getitem__ = getitem
#TStrQuV.__getitem__ = getitem
#TStrFltFltTrV.__getitem__ = getitem
#TStrStrIntTrV.__getitem__ = getitem
#TStrKdV.__getitem__ = getitem
#TStrStrVPrV.__getitem__ = getitem
#TStrVIntPrV.__getitem__ = getitem
#TFltIntIntIntQuV.__getitem__ = getitem
#TIntStrIntIntQuV.__getitem__ = getitem
#TIntIntPrPrV.__getitem__ = getitem
#PFltV.__getitem__ = getitem
#PAscFltV.__getitem__ = getitem
#PStrV.__getitem__ = getitem
#TBoolVV.__getitem__ = getitem
#TChVV.__getitem__ = getitem
#TIntVV.__getitem__ = getitem
#TSFltVV.__getitem__ = getitem
#TFltVV.__getitem__ = getitem
#TStrVV.__getitem__ = getitem
#TIntPrVV.__getitem__ = getitem
#TIntVVV.__getitem__ = getitem
#TFltVVV.__getitem__ = getitem
##TIntQV.__getitem__ = getitem
#TStrV.__getitem__ = getitem

%}

