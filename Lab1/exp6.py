import tools

def dual_quicksort(L):
    dual_quicksort_helper(L, 0, len(L) - 1)

def dual_quicksort_helper(L, low, high):
    if low < high:
        p1, p2 = dual_partition(L, low, high)
        dual_quicksort_helper(L, low, p1 - 1)
        dual_quicksort_helper(L, p1 + 1, p2 - 1)
        dual_quicksort_helper(L, p2 + 1, high)

def dual_partition(L, low, high):
    if L[low] > L[high]:
        L[low], L[high] = L[high], L[low]

    pivot1, pivot2 = L[low], L[high]
    i = low + 1
    j = high - 1
    k = low + 1

    while k <= j:
        if L[k] < pivot1:
            L[i], L[k] = L[k], L[i]
            i += 1
        elif L[k] >= pivot2:
            while L[j] > pivot2 and k < j:
                j -= 1
            L[k], L[j] = L[j], L[k]
            j -= 1
            if L[k] < pivot1:
                L[i], L[k] = L[k], L[i]
                i += 1
        k += 1

    i -= 1
    j += 1
    L[low], L[i] = L[i], L[low]
    L[high], L[j] = L[j], L[high]

    return i, j

results_dual_pivot = tools.initialize_results(tools.list_lengths_gs)

for length in tools.list_lengths_gs:
    for algorithm in [dual_quicksort]:
        runtimes = []  # empty list for storing runtimes
        for _ in range(tools.num_runs):
            L = tools.create_random_list(length, tools.max_value)
            runtime = tools.measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  # adding to runtime list
        results_dual_pivot[length] = runtimes

tools.print_results("Dual-Pivot Quick Sort Test", results_dual_pivot, "List Length")
