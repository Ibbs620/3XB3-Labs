import tools
from exp2 import bubble_sort2, insertion_sort_new, selection_sort2

# SELECTION SORT

ss_results = tools.initialize_results(tools.swaps)

for tools.swaps in tools.swaps:
    runtimes_selection2 = []
    
    for _ in range(tools.num_runs):
        near_sorted_list = tools.create_near_sorted_list(tools.fixed_list_length, tools.max_value, tools.swaps)
        runtime_selection2 = tools.measure_runtime(selection_sort2, near_sorted_list.copy())
        runtimes_selection2.append(runtime_selection2)
    
    ss_results[tools.swaps] = runtimes_selection2

tools.print_results("New Selection Sort Swap Test", ss_results, "Swaps")


# INSERTION SORT

is_results = tools.initialize_results(tools.swaps)

for s in tools.swaps:
    for i in range(tools.num_runs):
        L1 = tools.create_near_sorted_list(tools.fixed_list_length, tools.max_value, s)
        time_taken = tools.measure_runtime(insertion_sort_new, L1)
        is_results[s].append(round(time_taken, 6))

tools.print_results("New Insertion Sort Swap Test", is_results, "Swaps")
# BUBBLE SORT

bb_results = tools.initialize_results(tools.swaps)

for swap in tools.swaps:
        runtimes = [] #empty list for storing runtimes
        for _ in range(tools.num_runs):
            L = tools.create_near_sorted_list(tools.fixed_list_length, tools.max_value, swap)
            runtime = tools.measure_runtime(bubble_sort2, L.copy())
            runtimes.append(runtime)  #adding to runtime list
        bb_results[swap] = runtimes

tools.print_results("New Bubble Sort Swap Test", bb_results, "Swaps")
