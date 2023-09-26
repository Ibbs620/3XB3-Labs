import time
import random

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


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

# Test the dual pivot quicksort with a random list
if __name__ == '__main__':
    random.seed(42)
    test_list = [random.randint(1, 100) for _ in range(20)]
    print("Original List:")
    print(test_list)
    dual_quicksort(test_list)
    print("Sorted List:")
    print(test_list)


def measure_runtime(sorting_algorithm, L):
    start_time = time.time()
    sorting_algorithm(L)
    end_time = time.time()
    return end_time - start_time

list_lengths = [500, 1000, 2000, 5000, 10000, 50000]
num_runs = 10
max_value = 50000
results_dual_pivot = {algo.__name__: [] for algo in [dual_quicksort]}

for length in list_lengths:
    for algorithm in [dual_quicksort]:
        runtimes = []  # empty list for storing runtimes
        for _ in range(num_runs):
            L = create_random_list(length, max_value)
            runtime = measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  # adding to runtime list
        results_dual_pivot[algorithm.__name__].append(runtimes)

print("List Length\tDual Pivot QuickSort")
for i, length in enumerate(list_lengths):
    dual_pivot_selection = results_dual_pivot["dual_quicksort"][i]
    print(f"{length}\t\t{dual_pivot_selection}")
