import Lab1.bad_sorts

def measure_runtime(sorting_algorithm, L):
    start_time = time.time()
    sorting_algorithm(L)
    end_time = time.time()
    return end_time - start_time

list_lengths = [10, 50, 100, 200, 500, 1000]
num_runs = 10
max_value = 50000
results = {algo.__name__: [] for algo in [bubble_sort]}

for length in list_lengths:
    for algorithm in [bubble_sort]:
        runtimes = [] #empty list for storing runtimes
        for _ in range(num_runs):
            L = create_random_list(length, max_value)
            runtime = measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  #adding to runtime list
        results[algorithm.__name__].append(runtimes)


print("List Length\tBubble Sort")
for i, length in enumerate(list_lengths):
    bubble_mean = sum(results["bubble_sort"][i]) / num_runs
    print(f"{length}\t{bubble_mean:.6f}")