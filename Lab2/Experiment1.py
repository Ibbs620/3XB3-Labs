# EXPERIMENT 1 -------------------------------------------------------------------------
from graph import *

def experiment_1(num_nodes, max_edges, m=1000):
    results = {}

    # Generate edge counts from 100 to max_edges in increments of 100
    edge_counts = list(range(100, max_edges+1, 100))
    
    for num_edges in edge_counts:
        cycle_count = 0
        for _ in range(m):
            G = create_random_graph(num_nodes, num_edges)
            if has_cycle(G):
                cycle_count += 1

        proportion_of_edges = num_edges / (num_nodes * (num_nodes - 1))
        cycle_probability = cycle_count / m
        results[num_edges] = (proportion_of_edges, cycle_probability)

    return results

num_nodes = 100
max_edges = 2000  
results = experiment_1(num_nodes, max_edges)

for num_edges, (proportion, probability) in results.items():
    print(f"Number of Edges: {num_edges}, Proportion of Edges: {proportion:.4f}, Cycle Probability: {probability:.4f}")

# Results obtained - incorrect
# Number of Edges: 100, Proportion of Edges: 0.0101, Cycle Probability: 1.0000
# Number of Edges: 200, Proportion of Edges: 0.0202, Cycle Probability: 1.0000
# Number of Edges: 300, Proportion of Edges: 0.0303, Cycle Probability: 1.0000
# Number of Edges: 400, Proportion of Edges: 0.0404, Cycle Probability: 1.0000
# Number of Edges: 500, Proportion of Edges: 0.0505, Cycle Probability: 1.0000
# Number of Edges: 600, Proportion of Edges: 0.0606, Cycle Probability: 1.0000
# Number of Edges: 700, Proportion of Edges: 0.0707, Cycle Probability: 1.0000
# Number of Edges: 800, Proportion of Edges: 0.0808, Cycle Probability: 1.0000
# Number of Edges: 900, Proportion of Edges: 0.0909, Cycle Probability: 1.0000
# Number of Edges: 1000, Proportion of Edges: 0.1010, Cycle Probability: 1.0000
# Number of Edges: 1100, Proportion of Edges: 0.1111, Cycle Probability: 1.0000
# Number of Edges: 1200, Proportion of Edges: 0.1212, Cycle Probability: 1.0000
# Number of Edges: 1300, Proportion of Edges: 0.1313, Cycle Probability: 1.0000
# Number of Edges: 1400, Proportion of Edges: 0.1414, Cycle Probability: 1.0000
# Number of Edges: 1500, Proportion of Edges: 0.1515, Cycle Probability: 1.0000
# Number of Edges: 1600, Proportion of Edges: 0.1616, Cycle Probability: 1.0000
# Number of Edges: 1700, Proportion of Edges: 0.1717, Cycle Probability: 1.0000
# Number of Edges: 1800, Proportion of Edges: 0.1818, Cycle Probability: 1.0000
# Number of Edges: 1900, Proportion of Edges: 0.1919, Cycle Probability: 1.0000
# Number of Edges: 2000, Proportion of Edges: 0.2020, Cycle Probability: 1.0000