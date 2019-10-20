import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edge('man', 'baby', weight=1)
G.add_edge('baby', 'women', weight=0.5)
G.add_edge('man', 'women', weight=0.3)
G.add_edge('women', 'year', weight=1)
G.add_edge('year', 'man', weight=1)

# draw graph
nx.draw(G, with_labels=True, font_color='yellow', node_size=2000)
plt.show()
