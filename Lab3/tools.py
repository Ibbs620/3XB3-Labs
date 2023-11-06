# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
import random
import time

# Returns the runtime of a sorting algorithm on L
def measure_runtime(sorting_algorithm, L):
    start_time = time.perf_counter()
    sorting_algorithm(L)
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
    W = random.randint(N + 1, N ** 2 // 2)
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
num_runs = 10
max_value = 50000
list_lengths_gs = [500, 1000, 2000, 5000, 10000, 50000]
list_lengths_bs = [100, 500, 1000, 2000, 5000, 10000]
fixed_list_length = 1000
swaps = [10, 50, 100, 500, 1000, 5000]
