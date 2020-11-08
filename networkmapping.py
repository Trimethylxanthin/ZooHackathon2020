import matplotlib.pyplot as plt
import networkx as nx

edges = [
    ['Poachers','Habitats'],
    ['Habitats','Wildlife'],
    ['Poachers','City'],
    ['Wildlife','City'],
    ['Climate','City'],
    ['City','People']
]

G = nx.DiGraph()
G.add_edges_from(edges)
pos = nx.spring_layout(G)

plt.figure()    

nx.draw(G, pos, edge_color='black', width=1, linewidths=1, 
        node_size=2000, node_color='#00ff99', alpha=0.9,
        labels={node:node for node in G.nodes()})

nx.draw_networkx_edge_labels(G,pos,edge_labels={
    ('Poachers','Habitats'):'tracked in',
    ('Wildlife','Habitats'):'lives in',
    ('Poachers','City'):'move to',
    ('Wildlife','City'):'has been traded in past',
    ('Climate','City'):'influences',
    ('City','People'):'travel around'
},font_color='red')

plt.axis('off')
plt.show()
