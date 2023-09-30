import tools
import bad_sorts as bs

# BUBBLE SORT

results = tools.initialize_results(tools.list_lengths_bs)

for length in tools.list_lengths_bs:
    runtimes = [] #empty list for storing runtimes
    for _ in range(tools.num_runs):
        L = tools.create_random_list(length, tools.max_value)
        runtime = tools.measure_runtime(bs.bubble_sort, L.copy())
        runtimes.append(runtime)  #adding to runtime list
    results[length] = runtimes


print("List Length Bubble Sort")
for i, length in enumerate(tools.list_lengths_bs):
    selection = results[length]
    print(f"{length}\t\t{selection}")

# INSERTION SORT

results = tools.initialize_results(tools.list_lengths_bs)

for ll in tools.list_lengths_bs:
    for i in range(tools.num_runs):
        L1 = tools.create_random_list(ll, tools.max_value)
        time_taken = tools.measure_runtime(bs.insertion_sort, L1.copy())
        results[ll].append(round(time_taken, 6))

print("**********INSERTION SORT***********")
for ll, results in results.items():
    print("List length: ", ll)
    print("Runtimes: ", *results)
    print("---------------------------------------------")

# SELECTION SORT

results = tools.initialize_results(tools.list_lengths_bs)

for length in tools.list_lengths_bs:
    runtimes = [] #empty list for storing runtimes
    for _ in range(tools.num_runs):
        L = tools.create_random_list(length, tools.max_value)
        runtime = tools.measure_runtime(bs.selection_sort, L.copy())
        runtimes.append(runtime)  #adding to runtime list
    results[length] = runtimes

print("List Length Selection Sort")
for i, length in enumerate(tools.list_lengths_bs):
    selection = results[length]
    print(f"{length}\t\t{selection}")

