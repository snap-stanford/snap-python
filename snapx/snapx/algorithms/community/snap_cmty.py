from snap import TCnComV

from snap import CommunityCNM, CommunityGirvanNewman

def community_CNM(graph):
    cmtyV = TCnComV()
    modularity = CommunityCNM(graph.snap_graph, cmtyV)
    return (modularity, cmtyV)

def community_girvan_newman(graph):
    cmtyV = TCnComV()
    modularity = CommunityGirvanNewman(graph.snap_graph, cmtyV)
    return (modularity, cmtyV)
