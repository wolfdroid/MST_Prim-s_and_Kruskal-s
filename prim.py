#Library Initiation
import matplotlib.pyplot as plt
import networkx as nx
import sys

# Prim's Algorithm for MST
def prim( weighted_graph ):
    
    listMST = []        # Empty List for storing MST
    visited = []        # Empty List for storing the Node that have been visited
    edge_list = []      # Storing the Edges Values
    
    #Minimum Edge Weight
    min_edge = [0, 1, weighted_graph[0][1]]

    v = 0
    for V in range( vert_cout - 1 ):
    
        # add current vertex to the visited list
        visited.append(v)
    
        # updated the edge list with every current
        # candidate that can be a minimum-weight edge
        for u in range(vert_cout):
            if weighted_graph[v][u] != 0:
                edge_list.append([v, u, weighted_graph[v][u]])
        
        # find a minimum-weight edge among all the edge candidates
        for e in range(1, len(edge_list)):
            if edge_list[e][2] < min_edge[2] and edge_list[e][1] not in visited:
                min_edge = edge_list[e]

        # updated the MST list with the discovered minimum-weight edge
        listMST.append( min_edge )
      
        v = min_edge[1] # traverse to next vertex

        # remove the used minimum-weight edge
        edge_list.remove( min_edge )
        min_edge = edge_list[0]

    return listMST
    # Output: The empty set filled with the minimum spanning tree of G


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

#Array for weighted complete graph ( width and height = vert_cout )
weighted_graph = [[0 for i in range( vert_cout )] for j in range( vert_cout )]

#Filling array with all data founded in input
with open( file_name ) as f:
   for i in f:
       column = i.strip().split(' ')
       weighted_graph[int( vert_list.index(column[0] ) )][int( vert_list.index( column[1] ) )] = int( column[2] )
       weighted_graph[int( vert_list.index(column[1] ) )][int( vert_list.index( column[0] ) )] = int( column[2] )
f.close()

# run prim's algorithm to find the minimum spanning tree
listMST =  prim(weighted_graph)

#Printing the result
total = 0
print("The minimum spanning tree : ")
for a in range( len( listMST ) ):
    print( vert_list[listMST[a][0]], " to ", vert_list[listMST[a][1]], " = ", listMST[a][2], " units.")
    total += listMST[a][2]
print("total weight: ", total, " units.")

#displaying Result
dGraph(listMST)
