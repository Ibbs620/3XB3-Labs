# EXPERIMENT 2 -------------------------------------------------------------------------
from graph import *
import matplotlib.pyplot as plt

def experiment_2(num_nodes, num_graphs_per_edge):
    edge_counts = list(range(100, 500, 20))
    connected_probabilities = []

    for edges in edge_counts:
        connected_count = 0
        for _ in range(num_graphs_per_edge):
            G = create_random_graph(num_nodes, edges)
            if is_connected(G):
                connected_count += 1
        probability = round(connected_count / num_graphs_per_edge, 10)
        connected_probabilities.append(probability)
        print("Number of edges: ", edges, "Probability of connectedness: ", probability)

    plt.plot(edge_counts, connected_probabilities, marker='.')
    plt.xlabel('Number of Edges')
    plt.ylabel('Probability of Being Connected')
    plt.title('Edge Count vs Connectedness Probability')
    plt.grid(True)
    plt.show()

# Running the experiment with 100 nodes and generating 500 graphs for each edge count
experiment_2(100, 500)

