import networkx as nx
G = nx.Graph()
G.add_nodes_from(['a', 'b', 'c', 'd'])
G.add_edges_from([('a','b'), ('b','c'), ('c','d'), ('a','c')])
nx.draw(G, with_labels = True)

list(G.neighbors('b'))

for neighbor in G.neighbors('b'):
    print(neighbor)
    
G.has_node('a')
nx.is_tree(G)
nx.is_connected(G)
G.degree('a')

###drawing graphs###

D = nx.DiGraph()                          
D.add_edges_from([('1','2'), ('2','3'), ('1','4'), ('3','4')])
nx.draw(D, with_labels = True)

X=nx.Graph()
X.add_edges_from([(1,2),(2,3),(1,3),(3,4)])
nx.draw(X,with_labels=True,node_size=500)

dict(X.degree())          
nx.to_numpy_matrix(X)

graph=nx.read_edgelist('graph.txt',nodetype=str,create_using=nx.DiGraph())
nx.draw(graph,with_labels=True,node_size=500)
