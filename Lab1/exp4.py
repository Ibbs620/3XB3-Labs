import tools
import good_sorts as gs

# HEAPSORT

hs_results = tools.initialize_results(tools.list_lengths_gs)

for ll in tools.list_lengths_gs:
    for i in range(tools.num_runs):
        L = tools.create_random_list(ll, tools.max_value)
        time_taken = tools.measure_runtime(gs.heapsort, L)
        hs_results[ll].append(round(time_taken, 6))

tools.print_results("Heap Sort Test", hs_results, "List Length")

# MERGESORT

ms_results = tools.initialize_results(tools.list_lengths_gs)

for length in tools.list_lengths_gs:
    runtimes = [] #empty list for storing runtimes
    for _ in range(tools.num_runs):
        L = tools.create_random_list(length, tools.max_value)
        runtime = tools.measure_runtime(gs.mergesort, L.copy())
        runtimes.append(runtime)  #adding to runtime list
    ms_results[length] = runtimes

tools.print_results("Merge Sort Test", ms_results, "List Length")

# QUICKSORT

qs_results = tools.initialize_results(tools.list_lengths_gs)

for length in tools.list_lengths_gs:
    runtimes = []  # empty list for storing runtimes
    for _ in range(tools.num_runs):
        L = tools.create_random_list(length, tools.max_value)
        runtime = tools.measure_runtime(gs.quicksort, L.copy())
        runtimes.append(runtime)  # adding to runtime list
    qs_results[length] = runtimes

tools.print_results("Quick Sort Test", qs_results, "List Length")

