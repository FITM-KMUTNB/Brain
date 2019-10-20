import networkx as nx
import matplotlib.pyplot as plot

G = nx.Graph()

G.add_edges_from([('A', 'B'), ('A', 'M'), ('A', 'L'), ('B', 'C'), ('B', 'D'),
                  ('B', 'N'), ('B', 'O'), ('C', 'D'), ('D', 'E'), ('D', 'O'), ('E', 'F'), ('F', 'G'), ('F', 'N'), ('G', 'H'), ('H', 'N'), ('H', 'I'), ('H', 'P'), ('P', 'O'), ('P', 'I'), ('P', 'M'), ('I', 'J'), ('J', 'K'), ('K', 'M'), ('K', 'L')])

print('Shortest path from E to L is :',
      nx.shortest_path(G, source='E', target='L'))

# Draw Graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_color='yellow', node_size=1500)
plot.show()
