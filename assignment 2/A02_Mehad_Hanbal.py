import networkx as nx
import matplotlib.pyplot as plt

# Create a Graph
G = nx.Graph()

# Add family members (nodes)
G.add_node('Mervat')   # Mother
G.add_node('Yasser')   # Father
G.add_node('Mohab')  # Sibling 1
G.add_node('Mohammed')  # Sibling 2
G.add_node('Mehad')  # Sibling 3
G.add_node('Teta')   # Grandmother (Mama's side)
G.add_node('Gedo')   # Grandfather (Mama's side)
G.add_node('May')    # Aunt (Mama's sister)
G.add_node('Mohamed')  # Uncle (Mama's brother)

# Add edges representing family relationships (parents -> children, grandparents -> parents)
G.add_edge('Mervat', 'Mohab')     # Mama and Mohab
G.add_edge('Mervat', 'Mohammed')  # Mama and Mohammed
G.add_edge('Mervat', 'Mehad')     # Mama and Mehad
G.add_edge('Yasser', 'Mohab')     # Baba and Mohab
G.add_edge('Yasser', 'Mohammed') # Baba and Mohammed
G.add_edge('Yasser', 'Mehad')    # Baba and Mehad

# Add relationships with grandparents
G.add_edge('Teta', 'Mervat')  # Teta (Mom's mom) and Mama
G.add_edge('Gedo', 'Mervat')  # Gedo (Mom's dad) and Mama

# Add relationships for Mom's siblings
G.add_edge('Teta', 'May')   # Teta and May
G.add_edge('Gedo', 'May')   # Gedo and May
G.add_edge('Teta', 'Mohamed')  # Teta and Mohammed (Mom's brother)
G.add_edge('Gedo', 'Mohamed')  # Gedo and Mohammed (Mom's brother)

# Define layout for the plot (for visualization)
pos = {
    'Mervat': (0, 1),
    'Yasser': (0, -1),
    'Mohab': (-1, 0),
    'Mohammed': (1, 0),
    'Mehad': (0, 0),
    'Teta': (-2, 2),
    'Gedo': (2, 2),
    'May': (-3, 1),
    'Mohamed': (3, 1),
}

# Draw the graph
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Expanded Family Line Network')

# Draw the graph with labels, nodes, and edges
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='pink', font_size=12, font_weight='bold', edge_color='gray')

# Display the plot
plt.tight_layout()
plt.show()
