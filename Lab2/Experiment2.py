# EXPERIMENT 2 -------------------------------------------------------------------------
from graph import *
import matplotlib.pyplot as plt

def experiment_2(num_nodes, max_edges, m=1000):
    results_2 = {}
    
    for num_edges in range(num_nodes, max_edges + 1):
        connected_count = 0
        for _ in range(num_graphs_per_edge):
            G = create_random_graph(num_nodes, edges)
            if is_connected(G):
                connected_count += 1

        proportion_of_edges = num_edges / (num_nodes * (num_nodes - 1))
        connected_probability = connected_count / m
        results_2[proportion_of_edges] = connected_probability

    return results_2

# Experiment 2 testing
num_nodes = 100
max_edges = num_nodes * (num_nodes - 1) // 2
results_2 = experiment_2(num_nodes, max_edges)

print(results_2)
