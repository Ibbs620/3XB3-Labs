import good_sorts as gs
import tools

list_lengths = [500, 1000, 2000, 5000, 10000, 50000]
swaps = [10, 50, 100, 500, 1000, 5000]
num_runs = 10
max_value = 50000
runtimes_exp4 = {x : [] for x in list_lengths}
runtimes_exp5 = {x : [] for x in swaps}

# for ll in list_lengths:
#     for i in range(num_runs):
#         L = tools.create_random_list(ll, max_value)
#         time_taken = tools.measure_runtime(gs.heapsort, L)
#         runtimes_exp4[ll].append(round(time_taken, 6))

# print("********** HEAP SORT ***********")
# for ll, results in runtimes_exp4.items():
#     print("List length: ", ll)
#     print("Runtimes: ", *results)
#     print("---------------------------------------------")

for s in swaps:
    for i in range(num_runs):
        L = tools.create_near_sorted_list(1000, max_value, s)
        time_taken = tools.measure_runtime(gs.heapsort, L)
        runtimes_exp5[s].append(round(time_taken, 6))

print("********** HEAP SORT SWAP TEST ***********")
for s, results in runtimes_exp5.items():
    print("Swaps: ", s)
    print("Runtimes: ", *results)
    print("---------------------------------------------")


