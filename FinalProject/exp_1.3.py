import matplotlib.pyplot as plt
import time
import random
from final_project_part1 import *

# Experiment setup
constant_graph_size = 100  # Fixed graph size
edge_densities = [0.1, 0.2, 0.3, 0.4, 0.5]  # Different edge densities
k_value = 5  # Fixed value for k
dijkstra_times = []
bellman_ford_times = []

for density in edge_densities:
    G = DirectedWeightedGraph()
    for node in range(constant_graph_size):
        G.add_node(node)
    for node1 in range(constant_graph_size):
        for node2 in range(constant_graph_size):
            if node1 != node2 and random.random() < density:  # Varying chance to create an edge
                G.add_edge(node1, node2, random.randint(1, 10))

    # Measure time for dijkstra_approx
    start_time = time.time()
    dijkstra_approx(G, 0, k_value)
    dijkstra_times.append(time.time() - start_time)

    # Measure time for bellman_ford_approx
    start_time = time.time()
    bellman_ford_approx(G, 0, k_value)
    bellman_ford_times.append(time.time() - start_time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(edge_densities, dijkstra_times, label='Dijkstra Approx', marker='o')
plt.plot(edge_densities, bellman_ford_times, label='Bellman-Ford Approx', marker='x')
plt.xlabel('Edge Density')
plt.ylabel('Execution Time (Seconds)')
plt.title('Performance of Dijkstra and Bellman-Ford Approximations with Varying Edge Density')
plt.legend()
plt.grid(True)
plt.show()
