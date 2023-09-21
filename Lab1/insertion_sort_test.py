import bad_sorts as bs

swaps = [10, 50, 100, 500, 1000, 5000]
runtimes_old = {x : [] for x in bs.list_lengths}
runtimes_new = {x : [] for x in bs.list_lengths}
runtimes_swap = {x : [] for x in swaps}

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

# EXPERIMENT 1 AND 2

for ll in bs.list_lengths:
    for i in range(bs.num_runs):
        L1 = bs.create_random_list(ll, bs.max_value)
        L2 = L1.copy()
        time_taken_old = bs.measure_runtime(bs.insertion_sort, L1)
        time_taken_new = bs.measure_runtime(insertion_sort_new, L2)
        runtimes_old[ll].append(round(time_taken_old, 6))
        runtimes_new[ll].append(round(time_taken_new, 6))

print("**********OLD INSERTION SORT***********")
for ll, results in runtimes_old.items():
    print("List length: ", ll)
    print("Runtimes: ", *results)
    print("---------------------------------------------")

print("**********NEW INSERTION SORT***********")
for ll, results in runtimes_new.items():
    print("List length: ", ll)
    print("Runtimes: ", *results)
    print("---------------------------------------------")

#  EXPERIMENT 3 

for s in swaps:
    for i in range(bs.num_runs):
        L1 = bs.create_near_sorted_list(1000, bs.max_value, s)
        L2 = L1.copy()
        time_taken = bs.measure_runtime(insertion_sort_new, L2)
        runtimes_swap[s].append(round(time_taken, 6))

print("**********NEW INSERTION SORT (SWAP TEST)***********")
for s, results in runtimes_swap.items():
    print("Swaps: ", s)
    print("Runtimes: ", *results)
    print("---------------------------------------------")

