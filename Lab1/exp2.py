import tools

# BUBBLE SORT

results = tools.initialize_results(tools.list_lengths_bs)

def bubble_sort2(L):
    n = len(L)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                tools.swap(L, j, j + 1)
                swapped = True
        if not swapped:
            break

for length in tools.list_lengths_bs:
    for algorithm in [bubble_sort2]:
        runtimes = []  # empty list for storing runtimes
        for _ in range(tools.num_runs):
            L = tools.create_random_list(length, tools.max_value)
            runtime = tools.measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  # adding to runtime list
        results[length] = runtimes

print("List Length Bubble Sort 2")
for length in tools.list_lengths_bs:
    selection = results[length]
    print(f"{length}\t\t{selection}")

# INSERTION SORT

results = tools.initialize_results(tools.list_lengths_bs)

def insertion_sort_new(L):
    for i in range(1, len(L)):
        insert_new(L, i)

def insert_new(L, i):
    num = L[i]
    while i > 0:
        if L[i - 1] > num:
            L[i] = L[i - 1]
            i -= 1
        else:
            break
    L[i] = num

for ll in tools.list_lengths_bs:
    for i in range(tools.num_runs):
        L1 = tools.create_random_list(ll, tools.max_value)
        time_taken = tools.measure_runtime(insertion_sort_new, L1.copy())
        results[ll].append(round(time_taken, 6))

print("**********INSERTION SORT NEW***********")
for ll, results in results.items():
    print("List length: ", ll)
    print("Runtimes: ", *results)
    print("---------------------------------------------")

# SELECTION SORT

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

results = tools.initialize_results(tools.list_lengths_bs)

for length in tools.list_lengths_bs:
    runtimes = [] #empty list for storing runtimes
    for _ in range(tools.num_runs):
        L = tools.create_random_list(length, tools.max_value)
        runtime = tools.measure_runtime(algorithm, L.copy())
        runtimes.append(runtime)  #adding to runtime list
    results[length] = runtimes

print("List Length Selection Sort")
for length in tools.list_lengths_bs:
    selection = results[length]
    print(f"{length}\t\t{selection}")