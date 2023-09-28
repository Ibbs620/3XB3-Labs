import tools

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
        
L = tools.create_random_list(40, 100)

    
