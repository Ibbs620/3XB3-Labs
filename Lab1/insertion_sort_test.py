import bad_sorts as bs

runtimes = {x : [] for x in bs.list_lengths}

for ll in bs.list_lengths:
    for i in range(bs.num_runs):
        L = bs.create_random_list(ll, bs.max_value)
        time_taken = bs.measure_runtime(bs.insertion_sort, L)
        runtimes[ll].append(time_taken)

for ll, results in runtimes.items():
    print("List length: ", ll)
    print("Runtimes: ", '\t'.join(map(str, results)))
    print("---------------------------------------------")

