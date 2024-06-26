# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
import random
import time


def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


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


# Constants
num_runs = 10
max_value = 50000
list_lengths_gs = [500, 1000, 2000, 5000, 10000, 50000]
list_lengths_bs = [100, 500, 1000, 2000, 5000, 10000]
fixed_list_length = 1000
swaps = [10, 50, 100, 500, 1000, 5000]
