import tools

runtimes = tools.initialize_results(tools.list_lengths_gs)

def mergesort(L):
    n = len(L)
    window = 1
    while window < n:
        for i in range(0, n, window * 2):
            b = min(i + window, n)
            c = min(i + 2 * window, n)
            merge(L, i, b, c)
        window *= 2

def merge(L, a, b, c):
    L1 = L[a:b]
    L2 = L[b:c]
    L3 = []
    i, j = 0, 0 
    while i < b - a or j < c - b:
        if i == b - a:
            L3.append(L2[j])
            j+=1
        elif j == c - b:
            L3.append(L1[i])
            i+=1
        elif L1[i] <= L2[j]:
            L3.append(L1[i])
            i+=1
        elif L2[j] < L1[i]:
            L3.append(L2[j])
            j+=1
    for i in range(a, c):
        L[i] = L3[i - a]

for ll in tools.list_lengths_gs:
    for i in range(tools.num_runs):
        L = tools.create_random_list(ll, tools.max_value)
        time_taken = tools.measure_runtime(mergesort, L)
        runtimes[ll].append(round(time_taken, 6))   

tools.print_results("Iterative Merge Sort Test", runtimes, "List Length")

    
