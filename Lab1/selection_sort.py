import time
import random

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
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


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

#******************TESTING**********************************
#******************TESTING**********************************
#******************TESTING**********************************
#******************TESTING**********************************


def measure_runtime(sorting_algorithm, L):
    start_time = time.time()
    sorting_algorithm(L)
    end_time = time.time()
    return end_time - start_time

list_lengths = [100, 500, 1000, 2000, 5000, 10000]
num_runs = 10
max_value = 50000
results = {algo.__name__: [] for algo in [ selection_sort]}

for length in list_lengths:
    for algorithm in [ selection_sort]:
        runtimes = [] #empty list for storing runtimes
        for _ in range(num_runs):
            L = create_random_list(length, max_value)
            runtime = measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  #adding to runtime list
        results[algorithm.__name__].append(runtimes)


print("List Length Selection Sort")
for i, length in enumerate(list_lengths):
    selection = results["selection_sort"][i]
    print(f"{length}\t\t{selection}")
