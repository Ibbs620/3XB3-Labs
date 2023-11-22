import matplotlib.pyplot as plt
import time
import random
from final_project_part1 import *

# Experiment setup
graph_sizes = [10, 20, 50, 100, 200]  # Different graph sizes
k_value = 5  # Fixed relaxation limit
dijkstra_times = []
bellman_ford_times = []

for size in graph_sizes:
    # Create a graph with a fixed number of nodes and random edges
    G = DirectedWeightedGraph()
    for node in range(size):
        G.add_node(node)
    for node1 in range(size):
        for node2 in range(size):
            if node1 != node2 and random.random() < 0.3:  # 30% chance to create an edge
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
plt.plot(graph_sizes, dijkstra_times, label='Dijkstra Approx', marker='o')
plt.plot(graph_sizes, bellman_ford_times, label='Bellman-Ford Approx', marker='x')
plt.xlabel('Graph Size (Number of Nodes)')
plt.ylabel('Execution Time (Seconds)')
plt.title('Performance of Dijkstra and Bellman-Ford Approximations with Graph Size')
plt.legend()
plt.grid(True)
plt.show()