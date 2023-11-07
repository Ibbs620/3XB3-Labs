from graph import *
import matplotlib.pyplot as plt

def experiment_2(num_nodes, edge_counts, num_graphs_per_edge):
    connection_probabilities = []

    for edges in edge_counts:
        connected_count = 0
        for _ in range(num_graphs_per_edge):
            G = create_random_graph(num_nodes, edges)
            if is_connected(G):
                connected_count += 1
        probability = round(connected_count / num_graphs_per_edge, 10)
        connection_probabilities.append(probability)
        print("Number of edges: ", edges, "Probability of being connected: ", probability)

    plt.plot(edge_counts, connection_probabilities, marker='.')
    plt.xlabel('Number of Edges')
    plt.ylabel('Probability of Being Connected')
    plt.title('Edge Count vs Connectivity Probability')
    plt.grid(True)
    plt.show()

# Example usage:
# Define your edge_counts and num_nodes
edge_counts = list(range(0, 180, 5))
num_nodes = 100
num_graphs_per_edge = 500

# Run the experiment
experiment_2(num_nodes, edge_counts, num_graphs_per_edge)
