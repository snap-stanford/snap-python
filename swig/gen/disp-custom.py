def ConvertGraph(toutspec, tinspec, *args):
    if toutspec == PUNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PUNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PUNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PUNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PUNGraph_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    if toutspec == PNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PNGraph_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    if toutspec == PNEANet:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PNEANet_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PNEANet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PNEANet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PNEANet_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    if toutspec == PNGraphMP:
        if type(tinspec) == PUNGraph:
            return ConvertGraph_PNGraphMP_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertGraph_PNGraphMP_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertGraph_PNGraphMP_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertGraph_PNGraphMP_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    raise TypeError('First argument has invalid type')
def ConvertSubGraph(toutspec, tinspec, *args):
    if toutspec == PUNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PUNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PUNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PUNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PUNGraph_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    if toutspec == PNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PNGraph_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    if toutspec == PNEANet:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PNEANet_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PNEANet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PNEANet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PNEANet_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    if toutspec == PNGraphMP:
        if type(tinspec) == PUNGraph:
            return ConvertSubGraph_PNGraphMP_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertSubGraph_PNGraphMP_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertSubGraph_PNGraphMP_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertSubGraph_PNGraphMP_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    raise TypeError('First argument has invalid type')
def ConvertESubGraph(toutspec, tinspec, *args):
    if toutspec == PUNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PUNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PUNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PUNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PUNGraph_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    if toutspec == PNGraph:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PNGraph_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PNGraph_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PNGraph_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PNGraph_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    if toutspec == PNEANet:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PNEANet_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PNEANet_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PNEANet_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PNEANet_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    if toutspec == PNGraphMP:
        if type(tinspec) == PUNGraph:
            return ConvertESubGraph_PNGraphMP_PUNGraph(tinspec, *args)
        if type(tinspec) == PNGraph:
            return ConvertESubGraph_PNGraphMP_PNGraph(tinspec, *args)
        if type(tinspec) == PNEANet:
            return ConvertESubGraph_PNGraphMP_PNEANet(tinspec, *args)
        if type(tinspec) == PNGraphMP:
            return ConvertESubGraph_PNGraphMP_PNGraphMP(tinspec, *args)
        raise TypeError('Second argument has invalid type')
    raise TypeError('First argument has invalid type')
def ToNetwork(tspec, *args):
    if tspec == PNEANet :
        return ToNetwork_PNEANet(*args)
    raise TypeError('First argument has invalid type')
def ToGraph(tspec, *args):
    if tspec == PUNGraph:
        return ToGraph_PUNGraph(*args)
    if tspec == PNGraph:
        return ToGraph_PNGraph(*args)
    if tspec == PUndirNet:
        return ToGraph_PUndirNet(*args)
    if tspec == PDirNet:
        return ToGraph_PDirNet(*args)
    raise TypeError('First argument has invalid type')

