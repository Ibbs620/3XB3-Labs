# EXPERIMENT 1 -------------------------------------------------------------------------
from graph import *
import matplotlib.pyplot as plt

def experiment_1(num_nodes, num_graphs_per_edge):
    edge_counts = list(range(0, 180, 5))
    cycle_probabilities = []

    for edges in edge_counts:
        cycle_count = 0
        for _ in range(num_graphs_per_edge):
            G = create_random_graph(num_nodes, edges)
            if has_cycle(G):
                cycle_count += 1
        probability = round(cycle_count / num_graphs_per_edge, 10)
        cycle_probabilities.append(probability)
        print("Number of edges: ", edges, "Probability of cycle: ", probability)

    plt.plot(edge_counts, cycle_probabilities, marker='.')
    plt.xlabel('Number of Edges')
    plt.ylabel('Probability of Having a Cycle')
    plt.title('Edge Count vs Cycle Probability')
    plt.grid(True)
    plt.show()

# Running the experiment with 100 nodes and generating 500 graphs for each edge count
experiment_1(100, 500)

