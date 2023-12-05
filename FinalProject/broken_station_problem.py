def isFeasible(mid, arr, n, k):
    pos = arr[0]
    elements = 1
    for i in range(1, n):
        if (arr[i] - pos >= mid):
            pos = arr[i]
            elements += 1
            if (elements == k):
                return True
    return False

def bsp_value(L, m):
    n = len(L)
    L.sort()  
    k = n - m
    left = 1
    right = L[n - 1]
    res = -1

    while (left < right):
        mid = (left + right) // 2  
        if (isFeasible(mid, L, n, k)):
            res = max(res, mid)
            left = mid + 1
        else:
            right = mid

    return res

def bsp_solution(L, m):
    n = len(L)
    L.sort()
    k = n - m
    left = 1
    right = L[n - 1]
    res = -1
    best_mid = 0

    while (left < right):
        mid = (left + right) // 2

        if (isFeasible(mid, L, n, k)):
            if mid > best_mid:
                best_mid = mid
                res = mid
            left = mid + 1
        else:
            right = mid

    result = []
    last_added = L[0]
    result.append(last_added)
    elements = 1

    for i in range(1, n):
        if (elements < k) and (L[i] - last_added >= best_mid):
            result.append(L[i])
            last_added = L[i]
            elements += 1

    return result


val = bsp_value([2, 4, 6, 7, 10, 14], 2)
print(val)
assert val == 4

sol = bsp_solution([2, 4, 6, 7, 10, 14], 2)
print(sol)
assert sol == [2, 6, 10, 14]