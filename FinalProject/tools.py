# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
import random
import time
from final_project_part1 import DirectedWeightedGraph

# Returns the runtime of an algorithm on a knapsack problem
def measure_runtime(algorithm, graph):
    start_time = time.perf_counter()
    algorithm(graph)
    end_time = time.perf_counter()
    return end_time - start_time

# Creates a random DWG
def create_random_graph(nodes, edges, min_weight = 1, max_weight = 10):
    possible_edges = []
    for i in range(nodes):
        for j in range(nodes):
            if i == j: 
                continue # avoid self loops

            possible_edges.append([i, j, random.randint(min_weight, max_weight)])
    G = DirectedWeightedGraph()
    for i in range(nodes):
        G.add_node(i)
    random.shuffle(possible_edges)
    for i in range(edges):
        edge = possible_edges.pop()
        G.add_edge(edge[0], edge[1], edge[2])
    return G

# Creates a dictionary for storing results
def initialize_results(x_axis):
    return {x: 0 for x in x_axis}

# Prints results of a test
def print_results(title, results, axis_title):
    print("-" * 20, title, "-" * 20)
    print(f"{axis_title}\t\tSeconds taken")
    for value, data in results.items():
        data = [round(x, 6) for x in data]
        print(f"{value}\t\t{data}")
    print()

# Constants
num_runs = 10
