import good_sorts as gs
import bad_sorts as bs
import time
import random

list_lengths = [500, 1000, 2000, 5000, 10000, 50000]
num_runs = 10
max_value = 50000
results = {algo.__name__: [] for algo in [gs.quicksort]}

# ------------------------------------BUBBLE SORT TRADITIONAL---------------------------------

for length in list_lengths:
    for algorithm in [gs.quicksort]:
        runtimes = []  # empty list for storing runtimes
        for _ in range(num_runs):
            L = bs.create_random_list(length, max_value)
            runtime = bs.measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  # adding to runtime list
        results[algorithm.__name__].append(runtimes)


print("List Length Quick Sort")
for i, length in enumerate(list_lengths):
    selection = results["quicksort"][i]
    print(f"{length}\t\t{selection}")
