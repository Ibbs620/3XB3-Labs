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
