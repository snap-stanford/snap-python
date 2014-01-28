%pythoncode %{

#
# define __getitem__ for [] addressing
#

def getitem(self, i):
    return self.GetVal(i)

def setitem(self, i, val):
    self.SetVal(i, val)

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

# expand TVec types with methods __iter__ and __getitem__

TIntV.__getitem__ = getitem
TIntV.__setitem__ = setitem
TIntV.__iter__ = itervec
TFltV.__getitem__ = getitem
TFltV.__setitem__ = setitem
TFltV.__iter__ = itervec
TIntPrV.__getitem__ = getitem
TIntPrV.__setitem__ = setitem
TIntPrV.__iter__ = itervec
TFltPrV.__getitem__ = getitem
TFltPrV.__setitem__ = setitem
TFltPrV.__iter__ = itervec
TIntFltKdV.__getitem__ = getitem
TIntFltKdV.__setitem__ = setitem
TIntFltKdV.__iter__ = itervec
TCnComV.__getitem__ = getitem
TCnComV.__setitem__ = setitem
TCnComV.__iter__ = itervec

TCnCom.__getitem__ = getitem
TCnCom.__setitem__ = setitem
TCnCom.__iter__ = itervec
%}

#if SNAP_ALL
%pythoncode %{
TBoolV.__getitem__ = getitem
TBoolV.__setitem__ = setitem
TBoolV.__iter__ = itervec
TChV.__getitem__ = getitem
TChV.__setitem__ = setitem
TChV.__iter__ = itervec
TUChV.__getitem__ = getitem
TUChV.__setitem__ = setitem
TUChV.__iter__ = itervec
TUIntV.__getitem__ = getitem
TUIntV.__setitem__ = setitem
TUIntV.__iter__ = itervec
TUInt64V.__getitem__ = getitem
TUInt64V.__setitem__ = setitem
TUInt64V.__iter__ = itervec
TSFltV.__getitem__ = getitem
TSFltV.__setitem__ = setitem
TSFltV.__iter__ = itervec
TAscFltV.__getitem__ = getitem
TAscFltV.__setitem__ = setitem
TAscFltV.__iter__ = itervec
TStrV.__getitem__ = getitem
TStrV.__setitem__ = setitem
TStrV.__iter__ = itervec
TChAV.__getitem__ = getitem
TChAV.__setitem__ = setitem
TChAV.__iter__ = itervec
TIntTrV.__getitem__ = getitem
TIntTrV.__setitem__ = setitem
TIntTrV.__iter__ = itervec
TIntQuV.__getitem__ = getitem
TIntQuV.__setitem__ = setitem
TIntQuV.__iter__ = itervec
TFltTrV.__getitem__ = getitem
TFltTrV.__setitem__ = setitem
TFltTrV.__iter__ = itervec
TIntKdV.__getitem__ = getitem
TIntKdV.__setitem__ = setitem
TIntKdV.__iter__ = itervec
TUChIntPrV.__getitem__ = getitem
TUChIntPrV.__setitem__ = setitem
TUChIntPrV.__iter__ = itervec
TUChUInt64PrV.__getitem__ = getitem
TUChUInt64PrV.__setitem__ = setitem
TUChUInt64PrV.__iter__ = itervec
TIntUInt64PrV.__getitem__ = getitem
TIntUInt64PrV.__setitem__ = setitem
TIntUInt64PrV.__iter__ = itervec
TIntUInt64KdV.__getitem__ = getitem
TIntUInt64KdV.__setitem__ = setitem
TIntUInt64KdV.__iter__ = itervec
TIntFltPrV.__getitem__ = getitem
TIntFltPrV.__setitem__ = setitem
TIntFltPrV.__iter__ = itervec
TIntFltPrKdV.__getitem__ = getitem
TIntFltPrKdV.__setitem__ = setitem
TIntFltPrKdV.__iter__ = itervec
TFltIntPrV.__getitem__ = getitem
TFltIntPrV.__setitem__ = setitem
TFltIntPrV.__iter__ = itervec
TFltUInt64PrV.__getitem__ = getitem
TFltUInt64PrV.__setitem__ = setitem
TFltUInt64PrV.__iter__ = itervec
TFltStrPrV.__getitem__ = getitem
TFltStrPrV.__setitem__ = setitem
TFltStrPrV.__iter__ = itervec
TAscFltStrPrV.__getitem__ = getitem
TAscFltStrPrV.__setitem__ = setitem
TAscFltStrPrV.__iter__ = itervec
TIntStrPrV.__getitem__ = getitem
TIntStrPrV.__setitem__ = setitem
TIntStrPrV.__iter__ = itervec
TIntIntStrTrV.__getitem__ = getitem
TIntIntStrTrV.__setitem__ = setitem
TIntIntStrTrV.__iter__ = itervec
TIntIntFltTrV.__getitem__ = getitem
TIntIntFltTrV.__setitem__ = setitem
TIntIntFltTrV.__iter__ = itervec
TIntFltIntTrV.__getitem__ = getitem
TIntFltIntTrV.__setitem__ = setitem
TIntFltIntTrV.__iter__ = itervec
TIntStrIntTrV.__getitem__ = getitem
TIntStrIntTrV.__setitem__ = setitem
TIntStrIntTrV.__iter__ = itervec
TIntKdV.__getitem__ = getitem
TIntKdV.__setitem__ = setitem
TIntKdV.__iter__ = itervec
TUIntIntKdV.__getitem__ = getitem
TUIntIntKdV.__setitem__ = setitem
TUIntIntKdV.__iter__ = itervec
TIntPrFltKdV.__getitem__ = getitem
TIntPrFltKdV.__setitem__ = setitem
TIntPrFltKdV.__iter__ = itervec
TIntStrKdV.__getitem__ = getitem
TIntStrKdV.__setitem__ = setitem
TIntStrKdV.__iter__ = itervec
TIntStrPrPrV.__getitem__ = getitem
TIntStrPrPrV.__setitem__ = setitem
TIntStrPrPrV.__iter__ = itervec
TIntStrVPrV.__getitem__ = getitem
TIntStrVPrV.__setitem__ = setitem
TIntStrVPrV.__iter__ = itervec
TIntIntVIntTrV.__getitem__ = getitem
TIntIntVIntTrV.__setitem__ = setitem
TIntIntVIntTrV.__iter__ = itervec
TIntIntIntVTrV.__getitem__ = getitem
TIntIntIntVTrV.__setitem__ = setitem
TIntIntIntVTrV.__iter__ = itervec
TUInt64IntPrV.__getitem__ = getitem
TUInt64IntPrV.__setitem__ = setitem
TUInt64IntPrV.__iter__ = itervec
TUInt64FltPrV.__getitem__ = getitem
TUInt64FltPrV.__setitem__ = setitem
TUInt64FltPrV.__iter__ = itervec
TUInt64StrPrV.__getitem__ = getitem
TUInt64StrPrV.__setitem__ = setitem
TUInt64StrPrV.__iter__ = itervec
TUInt64IntKdV.__getitem__ = getitem
TUInt64IntKdV.__setitem__ = setitem
TUInt64IntKdV.__iter__ = itervec
TUInt64FltKdV.__getitem__ = getitem
TUInt64FltKdV.__setitem__ = setitem
TUInt64FltKdV.__iter__ = itervec
TUInt64StrKdV.__getitem__ = getitem
TUInt64StrKdV.__setitem__ = setitem
TUInt64StrKdV.__iter__ = itervec
TFltBoolKdV.__getitem__ = getitem
TFltBookKdV.__setitem__ = setitem
TFltBoolKdV.__iter__ = itervec
TFltIntKdV.__getitem__ = getitem
TFltIntKdV.__setitem__ = setitem
TFltIntKdV.__iter__ = itervec
TFltUInt64KdV.__getitem__ = getitem
TFltUInt64KdV.__setitem__ = setitem
TFltUInt64KdV.__iter__ = itervec
TFltIntPrKdV.__getitem__ = getitem
TFltIntPrKdV.__setitem__ = setitem
TFltIntPrKdV.__iter__ = itervec
TFltKdV.__getitem__ = getitem
TFltKdV.__setitem__ = setitem
TFltKdV.__iter__ = itervec
TFltStrKdV.__getitem__ = getitem
TFltStrKdV.__setitem__ = setitem
TFltStrKdV.__iter__ = itervec
TFltStrPrPrV.__getitem__ = getitem
TFltStrPrPrV.__setitem__ = setitem
TFltStrPrPrV.__iter__ = itervec
TFltIntIntTrV.__getitem__ = getitem
TFltIntIntTrV.__setitem__ = setitem
TFltIntIntTrV.__iter__ = itervec
TFltFltStrTrV.__getitem__ = getitem
TFltFltStrTrV.__setitem__ = setitem
TFltFltStrTrV.__iter__ = itervec
TAscFltIntPrV.__getitem__ = getitem
TAscFltIntPrV.__setitem__ = setitem
TAscFltIntPrV.__iter__ = itervec
TAscFltIntKdV.__getitem__ = getitem
TAscFltIntKdV.__setitem__ = setitem
TAscFltIntKdV.__iter__ = itervec
TStrPrV.__getitem__ = getitem
TStrPrV.__setitem__ = setitem
TStrPrV.__iter__ = itervec
TStrIntPrV.__getitem__ = getitem
TStrIntPrV.__setitem__ = setitem
TStrIntPrV.__iter__ = itervec
TStrFltPrV.__getitem__ = getitem
TStrFltPrV.__setitem__ = setitem
TStrFltPrV.__iter__ = itervec
TStrIntKdV.__getitem__ = getitem
TStrIntKdV.__setitem__ = setitem
TStrIntKdV.__iter__ = itervec
TStrFltKdV.__getitem__ = getitem
TStrFltKdV.__setitem__ = setitem
TStrFltKdV.__iter__ = itervec
TStrAscFltKdV.__getitem__ = getitem
TStrAscFltKdV.__setitem__ = setitem
TStrAscFltKdV.__iter__ = itervec
TStrTrV.__getitem__ = getitem
TStrTrV.__setitem__ = setitem
TStrTrV.__iter__ = itervec
TStrQuV.__getitem__ = getitem
TStrQuV.__setitem__ = setitem
TStrQuV.__iter__ = itervec
TStrFltFltTrV.__getitem__ = getitem
TStrFltFltTrV.__setitem__ = setitem
TStrFltFltTrV.__iter__ = itervec
TStrStrIntTrV.__getitem__ = getitem
TStrStrIntTrV.__setitem__ = setitem
TStrStrIntTrV.__iter__ = itervec
TStrKdV.__getitem__ = getitem
TStrKdV.__setitem__ = setitem
TStrKdV.__iter__ = itervec
TStrStrVPrV.__getitem__ = getitem
TStrStrVPrV.__setitem__ = setitem
TStrStrVPrV.__iter__ = itervec
TStrVIntPrV.__getitem__ = getitem
TStrVIntPrV.__setitem__ = setitem
TStrVIntPrV.__iter__ = itervec
TFltIntIntIntQuV.__getitem__ = getitem
TFltIntIntIntQuV.__setitem__ = setitem
TFltIntIntIntQuV.__iter__ = itervec
TIntStrIntIntQuV.__getitem__ = getitem
TIntStrIntIntQuV.__setitem__ = setitem
TIntStrIntIntQuV.__iter__ = itervec
TIntIntPrPrV.__getitem__ = getitem
TIntIntPrPrV.__setitem__ = setitem
TIntIntPrPrV.__iter__ = itervec
PFltV.__getitem__ = getitem
PFltV.__setitem__ = setitem
PFltV.__iter__ = itervec
PAscFltV.__getitem__ = getitem
PAscFltV.__setitem__ = setitem
PAscFltV.__iter__ = itervec
PStrV.__getitem__ = getitem
PStrV.__setitem__ = setitem
PStrV.__iter__ = itervec
TBoolVV.__getitem__ = getitem
TBoolVV.__setitem__ = setitem
TBoolVV.__iter__ = itervec
TChVV.__getitem__ = getitem
TChVV.__setitem__ = setitem
TChVV.__iter__ = itervec
TIntVV.__getitem__ = getitem
TIntVV.__setitem__ = setitem
TIntVV.__iter__ = itervec
TSFltVV.__getitem__ = getitem
TSFltVV.__setitem__ = setitem
TSFltVV.__iter__ = itervec
TFltVV.__getitem__ = getitem
TFltVV.__setitem__ = setitem
TFltVV.__iter__ = itervec
TStrVV.__getitem__ = getitem
TStrVV.__setitem__ = setitem
TStrVV.__iter__ = itervec
TIntPrVV.__getitem__ = getitem
TIntPrVV.__setitem__ = setitem
TIntPrVV.__iter__ = itervec
TIntVVV.__getitem__ = getitem
TIntVVV.__setitem__ = setitem
TIntVVV.__iter__ = itervec
TFltVVV.__getitem__ = getitem
TFltVVV.__setitem__ = setitem
TFltVVV.__iter__ = itervec
#TIntQV.__getitem__ = getitem
#TIntQV.__setitem__ = setitem
#TIntQV.__iter__ = itervec
TStrV.__getitem__ = getitem
TStrV.__setitem__ = setitem
TStrV.__iter__ = itervec
%}
#endif

