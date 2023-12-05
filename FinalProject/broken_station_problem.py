def isFeasible(mid, arr, n, k):
    pos, elements = arr[0], 1
    for i in range(1, n):
        if arr[i] - pos >= mid:
            pos, elements = arr[i], elements + 1
            if elements == k:
                return True
    return False

def findBestMid(L, n, k):
    left, right = 1, L[-1]
    best_mid = 0

    while left < right:
        mid = (left + right) // 2
        if isFeasible(mid, L, n, k):
            best_mid = max(best_mid, mid)
            left = mid + 1
        else:
            right = mid

    return best_mid

def bsp_value(L, m):
    L.sort()
    return findBestMid(L, len(L), len(L) - m)

def bsp_solution(L, m):
    L.sort()
    best_mid = findBestMid(L, len(L), len(L) - m)
    result, last_added = [L[0]], L[0]

    for i in range(1, len(L)):
        if len(result) < len(L) - m and L[i] - last_added >= best_mid:
            result.append(L[i])
            last_added = L[i]

    return result

# Test the functions
val = bsp_value([2, 4, 6, 7, 10, 14], 2)
print(val)
assert val == 4

sol = bsp_solution([2, 4, 6, 7, 10, 14], 2)
print(sol)
assert sol == [2, 6, 10, 14]