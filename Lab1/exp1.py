import tools
import bad_sorts as bs

# BUBBLE SORT

bs_results = tools.initialize_results(tools.list_lengths_bs)

for length in tools.list_lengths_bs:
    runtimes = [] #empty list for storing runtimes
    for _ in range(tools.num_runs):
        L = tools.create_random_list(length, tools.max_value)
        runtime = tools.measure_runtime(bs.bubble_sort, L.copy())
        runtimes.append(runtime)  #adding to runtime list
    bs_results[length] = runtimes

tools.print_results("Bubble Sort", bs_results, "List Length")

# INSERTION SORT

is_results = tools.initialize_results(tools.list_lengths_bs)

for ll in tools.list_lengths_bs:
    for i in range(tools.num_runs):
        L1 = tools.create_random_list(ll, tools.max_value)
        time_taken = tools.measure_runtime(bs.insertion_sort, L1.copy())
        is_results[ll].append(round(time_taken, 6))


tools.print_results("Insertion Sort", bs_results, "List Length")

# SELECTION SORT

ss_results = tools.initialize_results(tools.list_lengths_bs)

for length in tools.list_lengths_bs:
    runtimes = [] #empty list for storing runtimes
    for _ in range(tools.num_runs):
        L = tools.create_random_list(length, tools.max_value)
        runtime = tools.measure_runtime(bs.selection_sort, L.copy())
        runtimes.append(runtime)  #adding to runtime list
    ss_results[length] = runtimes

tools.print_results("Selection Sort", ss_results, "List Length")

