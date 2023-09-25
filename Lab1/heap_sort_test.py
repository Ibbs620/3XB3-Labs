import good_sorts as gs
import tools

list_lengths = [500, 1000, 2000, 5000, 10000, 50000]
num_runs = 10
max_value = 50000
runtimes = {x : [] for x in list_lengths}

for ll in list_lengths:
    for i in range(num_runs):
        L = tools.create_random_list(ll, max_value)
        time_taken = tools.measure_runtime(gs.heapsort, L)
        runtimes[ll].append(round(time_taken, 6))

print("********** HEAP SORT ***********")
for ll, results in runtimes.items():
    print("List length: ", ll)
    print("Runtimes: ", *results)
    print("---------------------------------------------")



