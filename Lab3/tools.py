# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
import random
import time
# Helper function to calculate the total weight and value of a subset of items
def total_weight_value(subset):
    total_weight = sum(item[0] for item in subset)
    total_value = sum(item[1] for item in subset)
    return total_weight, total_value

# Returns the runtime of an algorithm on a knapsack problem
def measure_runtime(sorting_algorithm, items, weight):
    start_time = time.perf_counter()
    sorting_algorithm(items, weight)
    end_time = time.perf_counter()
    return end_time - start_time


# Creates a dictionary for storing results
def initialize_results(x_axis):
    return {x: [] for x in x_axis}


# Prints results of a test
def print_results(title, results, axis_title):
    print("-" * 20, title, "-" * 20)
    print(f"{axis_title}\t\tSeconds taken")
    for value, data in results.items():
        data = [round(x, 6) for x in data]
        print(f"{value}\t\t{data}")
    print()

# Generate random knapsack problem
def generate_knapsack(N):
    W = random.randint(N + 1, max(N ** 2 // 2, N + 3))
    possible_weights = list(range(1,W))
    possible_values = list(range(1,W))
    items = []
    for i in range(N):
        weight = random.choice(possible_weights)
        value = random.choice(possible_values)
        possible_weights.remove(weight)
        possible_values.remove(value)
        items.append((weight, value))
        possible_values
    return items, W
# Constants
item_set_sizes = list(range(2, 21, 2))
max_weight = 50
max_value = 100
num_runs = 10
