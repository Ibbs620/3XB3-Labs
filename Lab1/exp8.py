import tools
from bad_sorts import insertion_sort
from good_sorts import quicksort, mergesort

list_lengths = [i for i in range(10, 101, 10)]

num_runs = 10
max_value = 50000
is_results = tools.initialize_results(list_lengths)
qs_results = tools.initialize_results(list_lengths)
ms_results = tools.initialize_results(list_lengths)


for length in list_lengths:
    # empty lists for storing runtimes
    is_runtimes = []  
    qs_runtimes = []  
    ms_runtimes = []  
    for _ in range(num_runs):
        L = tools.create_random_list(length, max_value)
        is_runtime = tools.measure_runtime(insertion_sort, L.copy())
        ms_runtime = tools.measure_runtime(mergesort, L.copy())
        qs_runtime = tools.measure_runtime(quicksort, L.copy())
        is_runtimes.append(is_runtime)  # adding to runtime list
        qs_runtimes.append(qs_runtime) 
        ms_runtimes.append(ms_runtime)  
    is_results[length] = is_runtimes
    qs_results[length] = qs_runtimes
    ms_results[length] = ms_runtimes

tools.print_results("Insertion Sort Runtimes", is_results, "List Length")
tools.print_results("Quick Sort Runtimes", qs_results, "List Length")
tools.print_results("Merge Sort Runtimes", ms_results, "List Length")
