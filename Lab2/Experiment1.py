# EXPERIMENT 1 -------------------------------------------------------------------------
from graph import *

# def experiment_1(num_nodes, max_edges, m=1000):
#     results = {}

#     # Generate edge counts from 100 to max_edges in increments of 100
#     edge_counts = list(range(100, max_edges+1, 100))
    
#     for num_edges in edge_counts:
#         cycle_count = 0
#         for _ in range(m):
#             G = create_random_graph(num_nodes, num_edges)
#             if has_cycle(G):
#                 cycle_count += 1

#         proportion_of_edges = num_edges / (num_nodes * (num_nodes - 1))
#         cycle_probability = cycle_count / m
#         results[num_edges] = (proportion_of_edges, cycle_probability)

#     return results

# num_nodes = 100
# max_edges = 2000  
# results = experiment_1(num_nodes, max_edges)

# for num_edges, (proportion, probability) in results.items():
#     print(f"Number of Edges: {num_edges}, Proportion of Edges: {proportion:.4f}, Cycle Probability: {probability:.10f}")

import matplotlib.pyplot as plt

def experiment_1(num_nodes, num_graphs_per_edge):
    edge_counts = list(range(100, 2100, 100))  # 100, 200, ..., 2000
    cycle_probabilities = []

    for edges in edge_counts:
        cycle_count = 0
        for _ in range(num_graphs_per_edge):
            G = create_random_graph(num_nodes, edges)
            if has_cycle(G):
                cycle_count += 1
        cycle_probabilities.append(cycle_count / num_graphs_per_edge)

    # Plot the results
    plt.plot(edge_counts, cycle_probabilities, marker='o')
    plt.xlabel('Number of Edges')
    plt.ylabel('Probability of Having a Cycle')
    plt.title('Edge Count vs Cycle Probability')
    plt.grid(True)
    plt.show()

# Running the experiment with 100 nodes and generating 50 graphs for each edge count
experiment_1(100, 50)

