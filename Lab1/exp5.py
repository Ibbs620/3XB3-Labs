import tools
import good_sorts as gs

# MERGESORT

ms_results = tools.initialize_results(tools.swaps)

for swaps in tools.swaps:
    runtimes = []
    for _ in range(tools.num_runs):
        near_sorted_list = tools.create_near_sorted_list(tools.fixed_list_length, tools.max_value, swaps)
        runtime = tools.measure_runtime(gs.mergesort, near_sorted_list.copy())
        runtimes.append(runtime)
    ms_results[swaps] = runtimes

tools.print_results("Merge Sort Swap Test", ms_results, "Swaps")

# QUICKSORT

qs_results = tools.initialize_results(tools.swaps)

for swap in tools.swaps:
    for algorithm in [gs.quicksort]:
        runtimes = []  # empty list for storing runtimes
        for _ in range(tools.num_runs):
            L = tools.create_near_sorted_list(tools.fixed_list_length, tools.max_value, swap)
            runtime = tools.measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  # adding to runtime list
        qs_results[swap] = runtimes

tools.print_results("Quick Sort Swap Test", qs_results, "Swaps")

# HEAPSORT

hs_results = tools.initialize_results(tools.swaps)

for s in tools.swaps:
    for i in range(tools.num_runs):
        L = tools.create_near_sorted_list(tools.fixed_list_length, tools.max_value, s)
        time_taken = tools.measure_runtime(gs.heapsort, L)
        hs_results[s].append(round(time_taken, 6))

tools.print_results("Heap Sort Swap Test", hs_results, "Swaps")

        
