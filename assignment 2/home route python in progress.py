import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

# Create a Graph
G = nx.Graph()

# Add nodes representing the locations (Vita Student and ETSAV UPC)
G.add_node('Vita Student, Poblenou', pos=(41.3982, 2.2023))  # Vita Student coordinates (example)
G.add_node('ETSAV UPC', pos=(41.3687, 2.1150))  # ETSAV UPC coordinates (example)

# Add an edge between these two nodes, representing the route
G.add_edge('Vita Student, Poblenou', 'ETSAV UPC')

# Define positions for the nodes based on the coordinates (for visualization purposes)
pos = nx.get_node_attributes(G, 'pos')

# Draw settings
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot()
ax.set_title('Route from Vita Student, Poblenou to ETSAV UPC', fontsize=12)

# Draw the graph
nx.draw(G, pos, node_size=1500, with_labels=True, node_color='blue', font_size=12, font_color='white', edge_color='green', width=2)

# Display the graph
plt.tight_layout()

# Save the plot to a file (replace with your desired file path)
path = r"C:\Users\Nehad\Desktop\route_graph.png"
plt.savefig(path, format="PNG")

# Show the plot (optional)
plt.show()