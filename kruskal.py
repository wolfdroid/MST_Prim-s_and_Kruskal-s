#Library Initiation
import matplotlib.pyplot as plt
import networkx as nx
import sys

#Sorting Edge Function
def sortEdge(weighted_graph):
    sort_graph = []
    sort_graph.append(weighted_graph[0])
    least = weighted_graph[0]
    for i in range(1, len(weighted_graph)):
        val = weighted_graph[i][2]
        j = 0
        while val > sort_graph[j][2] and j < len(sort_graph) -1:
            j += 1
        sort_graph.insert(j , weighted_graph[i])
    temp = sort_graph[len(sort_graph)-1]
    sort_graph.remove(sort_graph[len(sort_graph)-1])
    j = 0
    while temp[2] > sort_graph[j][2] and j < len(sort_graph) -1:
        j += 1
    sort_graph.insert(j , temp)
    return sort_graph

#Parent and Child Function
def find(root, parent):
    while root != parent[root]:
        root = parent[root]
    return root
    
def union(parent, rootv, rootu, size):
    if(size[rootv] > size[rootu]):
        parent[rootu] = rootv
    elif(size[rootv] < size[rootu]):
        parent[rootv] = rootu
    else:
        parent[rootu] = rootv
        size[rootv] += 1

# Kruskal Algorithm for MST
def kruskal(weighted_graph):

    listMST = []                            #Empty List for storing MST
    sort_graph = sortEdge(weighted_graph)   #Sorting the Graph according weight in ascending order
    parent = []                             #Stores the root vertex to each vertex
    size = []                               #Number of edging dependents to each V

    # Initialize each vertex withot dependent edges
    for e in range(vert_cout):
        parent.append(e)
        size.append(0)

    encounter = 0
    k = 0         # initialize the number of processed edges
    while encounter < (vert_cout - 1):
        v = sort_graph[k][0]
        u = sort_graph[k][1]
        k += 1
        rootu = find(v, parent)
        rootv = find(u, parent)
        if rootv != rootu:
            encounter = encounter +1
            listMST.append([v, u, sort_graph[k][2]])
            union(parent, rootv, rootu, size)
            
    return listMST

#Displaying Graph Function
def dGraph( listMST ):
    #Creating Graph to image
    G = nx.Graph()
    #Recursive Function to adding Edge
    for i in range( len( listMST ) ): 
        G.add_edge(
                vert_list[listMST[i][0]],
                vert_list[listMST[i][1]],
                weight = int( listMST[i][2] )
                )
    edge=[( u,v ) for ( u,v,d ) in G.edges( data=True )]
    
    #Formatting Nodes Position
    position=nx.spring_layout( G, k=20, pos=None, fixed=None, iterations=150, weight='weight', scale=1.0 )

    #Reading Weight Edge
    weight = dict( map( lambda x:( ( x[0],x[1] ), str( x[2]['weight'] ) ), G.edges( data = True ) ) )
    nx.draw_networkx_edge_labels(G, position, edge_labels = weight)

    #Find the longest node name
    node_len = 0
    for i in range(vert_cout):
        if len( vert_list[i] ) > node_len:
            node_len = len( vert_list )

    #Drawing Nodes Function
    nx.draw_networkx_nodes( G, position, node_size=node_len * 180,  node_color='#cc0c38' ,node_shape='o', node_len=100, alpha=0.5 )
    
    #Drawing Edges Function
    nx.draw_networkx_edges( G, position, edgelist=edge, width=2, edge_color='black', alpha=0.5 )

    #Drawing Labels
    nx.draw_networkx_labels( G, position, font_size=9, font_family='sans-serif' )

    #Plotting using Matplotlib
    plt.axis('off')
    plt.show()

#Reading input File. Example : python prim.py simple.txt
file_name = sys.argv[1]

#Collecting all set of vertices
vert_set = set()
with open( file_name ) as f:
   for a in f:
       column = a.strip().split(' ')
       vert_set.add(column[0])
       vert_set.add(column[1])
f.close()

#Convert the set into a list
vert_list = list( vert_set )
#Maintaining number of all vertices
vert_cout = ( len( vert_set ) )

# build a weighted complete graph for kurskal's algorithm to run
weighted_graph = []
with open(file_name) as f:
   for i in f:
        column = i.strip().split(' ')
        weighted_graph.append([
            int(vert_list.index(column[0])),
            int(vert_list.index(column[1])),
            int(column[2])])
f.close()

# run kruskal algorithm to find the minimum spanning tree
listMST = kruskal(weighted_graph)

#Printing the result
total = 0
print("The minimum spanning tree : ")
for a in range( len( listMST ) ):
    print( vert_list[listMST[a][0]], " to ", vert_list[listMST[a][1]], " = ", listMST[a][2], " units.")
    total += listMST[a][2]
print("total weight: ", total, " units.")

# display the results
dGraph(listMST)
