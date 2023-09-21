import time
import random
import bad_sorts as bs

def measure_runtime(sorting_algorithm, L):
    start_time = time.time()
    sorting_algorithm(L)
    end_time = time.time()
    return end_time - start_time

list_lengths = [100, 500, 1000, 2000, 5000, 10000]
num_runs = 10
max_value = 50000
results = {algo.__name__: [] for algo in [ bs.bubble_sort2]}

# ------------------------------------BUBBLE SORT TRADITIONAL---------------------------------

for length in list_lengths:
    for algorithm in [ bs.bubble_sort]:
        runtimes = [] #empty list for storing runtimes
        for _ in range(num_runs):
            L = bs.create_random_list(length, max_value)
            runtime = bs.measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  #adding to runtime list
        results[algorithm.__name__].append(runtimes)


print("List Length Bubble Sort")
for i, length in enumerate(list_lengths):
    selection = results["bubble_sort"][i]
    print(f"{length}\t\t{selection}")


# ------------------------------------BUBBLE SORT NEW---------------------------------


for length in list_lengths:
    for algorithm in [ bs.bubble_sort2]:
        runtimes = [] #empty list for storing runtimes
        for _ in range(num_runs):
            L = bs.create_random_list(length, max_value)
            runtime = bs.measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  #adding to runtime list
        results[algorithm.__name__].append(runtimes)


print("List Length Bubble Sort 2")
for i, length in enumerate(list_lengths):
    selection = results["bubble_sort2"][i]
    print(f"{length}\t\t{selection}")
