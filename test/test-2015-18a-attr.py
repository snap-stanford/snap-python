import snap

Gnea = snap.TNEANet.New()    # Create an empty graph
Gnea.AddStrAttrN('name')    # Add a node attribute "name"

# Add some nodes
Gnea.AddNode(0)             
Gnea.AddNode(1)
Gnea.AddNode(2)

# Fill in the attribute "name"
Gnea.AddStrAttrDatN(0, 'zero', 'name') 
Gnea.AddStrAttrDatN(1, 'one', 'name')
Gnea.AddStrAttrDatN(2, 'two', 'name')

# Retrieve  attribute "name"
Gnea.GetStrAttrDatN(0, 'name')        
Gnea.GetStrAttrDatN(1, 'name')
Gnea.GetStrAttrDatN(2, 'name')

# Add some edges
Gnea.AddEdge(0, 1, -1)         
Gnea.AddEdge(1, 2, -1)         
Gnea.AddEdge(2, 0, -1)         

Gnea.AddFltAttrE('posWeight')  # Add an edge attribute "weight"
Gnea.AddFltAttrE('negWeight')  # Add an edge attribute "weight"

# Fill in the edge attributes
for x in Gnea.Edges():              
    Gnea.AddFltAttrDatE(x.GetId(), float(x.GetId()*3+1), 'posWeight')
    Gnea.AddFltAttrDatE(x.GetId(), -1.0*float(x.GetId()*3+1), 'negWeight')

# Retrieve the attribute "weight"
for x in Gnea.Edges():              
    print(Gnea.GetFltAttrDatE(x.GetId(), 'posWeight'))

for x in Gnea.Edges():              
    print(Gnea.GetFltAttrDatE(x.GetId(), 'negWeight'))

for x in Gnea.Edges():              
    if Gnea.GetFltAttrDatE(x.GetId(), 'posWeight') == Gnea.GetFltAttrDatE(x.GetId(), 'negWeight'):
        print("*** Error: attributes are equal")
        sys.exit(1)

