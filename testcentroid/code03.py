import matplotlib.pyplot as plot
import networkx as nx

G = nx.Graph()

G.add_edge('man', 'baby', weight=1)
G.add_edge('baby', 'women', weight=0.5)
G.add_edge('man', 'women', weight=0.3)
G.add_edge('women', 'year', weight=1)
G.add_edge('year', 'man', weight=1)
G.add_edge('dog', 'baby', weight=1)
G.add_edge('home', 'dog', weight=1)
G.add_edge('home', 'man', weight=1)

edge_labels = nx.get_edge_attributes(G, 'weight')
print(edge_labels)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_color='yellow', node_size=2000)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plot.show()
