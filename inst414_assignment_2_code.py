import networkx as nx
import praw  
import tweepy 
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(['UserA', 'UserB', 'UserC', 'UserD'])

G.add_edges_from([('UserA', 'UserB'), ('UserA', 'UserC'), ('UserB', 'UserD'), ('UserC', 'UserD')])

degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
pagerank = nx.pagerank(G)

plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_size=3000, node_color='lightblue', edge_color='gray')
plt.title("Network Graph of Online Forum Users")
plt.show()

print("Degree Centrality:", degree_centrality)
print("Betweenness Centrality:", betweenness_centrality)
print("PageRank:", pagerank)