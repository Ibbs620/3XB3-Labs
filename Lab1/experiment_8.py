import tools
import bad_sorts as bs
import good_sorts as gs
import time
import random

algorithms = ["insertion_sort", "quicksort", "mergesort"]
i = 10
list_lengths = []
while i <= 100:
    list_lengths.append(i)
    i += 10


num_runs = 10
max_value = 50000
results = {algo.__name__: [] for algo in [bs.insertion_sort]}


for length in list_lengths:
    for algorithm in [bs.insertion_sort]:
        runtimes = []  # empty list for storing runtimes
        for _ in range(num_runs):
            L = tools.create_random_list(length, max_value)
            runtime = tools.measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  # adding to runtime list
        results[algorithm.__name__].append(runtimes)


print("List Length Insertion Sort")
for i, length in enumerate(list_lengths):
    selection = results[algorithms[0]][i]
    print(f"{length}\t\t{selection}")
