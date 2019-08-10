import networkx as nx

s = [0, 3, 2, 3, 4, 5, 1]
t = [1, 2, 7, 4, 6, 6, 5]
dist = [3, 2, 5, 1, 5, 4, 2]

G = nx.Graph()
for i in range(len(s)):
    G.add_edge(s[i], t[i], weight=dist[i])

list(G)
