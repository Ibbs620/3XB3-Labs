import matplotlib.pyplot as plt
import time
import random
from final_project_part1 import *

# Experiment setup
constant_graph_size = 100  # Fixed graph size
k_values = [1, 2, 5, 10, 20]  # Different values for k
dijkstra_times = []
bellman_ford_times = []

G = DirectedWeightedGraph()
for node in range(constant_graph_size):
    G.add_node(node)
for node1 in range(constant_graph_size):
    for node2 in range(constant_graph_size):
        if node1 != node2 and random.random() < 0.3:
            G.add_edge(node1, node2, random.randint(1, 10))

for k in k_values:
    # Measure time for dijkstra_approx
    start_time = time.time()
    dijkstra_approx(G, 0, k)
    dijkstra_times.append(time.time() - start_time)

    # Measure time for bellman_ford_approx
    start_time = time.time()
    bellman_ford_approx(G, 0, k)
    bellman_ford_times.append(time.time() - start_time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(k_values, dijkstra_times, label='Dijkstra Approx', marker='o')
plt.plot(k_values, bellman_ford_times, label='Bellman-Ford Approx', marker='x')
plt.xlabel('Value of k (Relaxation Limit)')
plt.ylabel('Execution Time (Seconds)')
plt.title('Performance of Dijkstra and Bellman-Ford Approximations Varying k (Graph Size = {})'.format(constant_graph_size))
plt.legend()
plt.grid(True)
plt.show()
