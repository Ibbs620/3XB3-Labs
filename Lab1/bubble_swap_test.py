import bad_sorts as bs

swaps = [10, 50, 100, 500, 1000, 5000]
list_length = 1000
max_value = 50000
results = {algo.__name__: [] for algo in [ bs.bubble_sort2]}
num_runs = 10

for swap in swaps:
    for algorithm in [ bs.bubble_sort2]:
        runtimes = [] #empty list for storing runtimes
        for _ in range(num_runs):
            L = bs.create_near_sorted_list(list_length,max_value,swap)
            runtime = bs.measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  #adding to runtime list
        results[algorithm.__name__].append(runtimes)


print("Swaps Bubble Sort 2")
for i, swap in enumerate(swaps):
    selection = results["bubble_sort2"][i]
    print(f"{swap}\t\t{selection}")

