import snap

Gnea = snap.TNEANet.New()    # Create an empty graph
Gnea.AddStrAttrN('name')    # Add a node attribute "name"

# this code fails
# if works, if the attribute definition is moved to after edges are added
Gnea.AddIntAttrE('weight')  # Add an edge attribute "weight"

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

#Gnea.AddIntAttrE('weight')  # Add an edge attribute "weight"

# Fill in the edge attribute "weight"
for x in Gnea.Edges():              
    Gnea.AddIntAttrDatE(x.GetId(), x.GetId()*3+1, 'weight')

# Retrieve the attribute "weight"
for x in Gnea.Edges():              
    print(Gnea.GetIntAttrDatE(x.GetId(), 'weight'))

