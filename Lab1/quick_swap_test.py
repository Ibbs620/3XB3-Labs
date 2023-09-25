import bad_sorts as bs
import good_sorts as gs

swaps = [10, 50, 100, 500, 1000, 5000]

list_length = 1000
max_value = 50000
results = {algo.__name__: [] for algo in [gs.quicksort]}
num_runs = 10

for swap in swaps:
    for algorithm in [gs.quicksort]:
        runtimes = []  # empty list for storing runtimes
        for _ in range(num_runs):
            L = bs.create_near_sorted_list(list_length, max_value, swap)
            runtime = bs.measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  # adding to runtime list
        results[algorithm.__name__].append(runtimes)


print("Swaps Quick Sort")
for i, swap in enumerate(swaps):
    selection = results["quicksort"][i]
    print(f"{swap}\t\t{selection}")
