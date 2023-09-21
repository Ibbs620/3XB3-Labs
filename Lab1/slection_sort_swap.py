import random
import time

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# Selection sort 2
def selection_sort2(L):
    n = len(L)
    for i in range(n // 2):
        min_idx, max_idx = i, i
        for j in range(i, n - i):
            if L[j] < L[min_idx]:
                min_idx = j
            elif L[j] > L[max_idx]:
                max_idx = j
        L[i], L[min_idx] = L[min_idx], L[i]
        if max_idx == i:
            max_idx = min_idx  # Adjust max index if it's at the beginning
        L[n - i - 1], L[max_idx] = L[max_idx], L[n - i - 1]

list_length = 1000
max_value = 50000
swaps_range = [10, 50, 100, 500, 1000, 5000]  
num_runs = 10

def measure_runtime(sorting_algorithm, L):
    start_time = time.time()
    sorting_algorithm(L)
    end_time = time.time()
    return end_time - start_time

results_selection2 = {}

for swaps in swaps_range:
    runtimes_selection2 = []
    
    for _ in range(num_runs):
        near_sorted_list = create_near_sorted_list(list_length, max_value, swaps)
        runtime_selection2 = measure_runtime(selection_sort2, near_sorted_list.copy())
        runtimes_selection2.append(runtime_selection2)
    
    results_selection2[swaps] = runtimes_selection2

# Print the runtimes for each configuration
for swaps, runtimes in results_selection2.items():
    print(f"Swaps: {swaps}, Runtimes: {runtimes}")
