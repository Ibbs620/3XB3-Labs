from graph import *

def experiment_1(num_nodes, max_edges, m=1000):

    results = {}

    for num_edges in range(num_nodes, max_edges + 1):  
        cycle_count = 0
        for _ in range(m):
            G = create_random_graph(num_nodes, num_edges)
            if has_cycle(G):
                cycle_count += 1

        proportion_of_edges = num_edges / (num_nodes * (num_nodes - 1))
        cycle_probability = cycle_count / m
        results[proportion_of_edges] = cycle_probability

    return results



# Experiemnt 1 testing
num_nodes = 100
max_edges = num_nodes * (num_nodes - 1) // 2  
results = experiment_1(num_nodes, max_edges)

print(results)
