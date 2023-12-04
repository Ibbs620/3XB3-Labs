def bsp_value(L, m):
    if m >= len(L):
        return 0

    max_diff = 0

    for i in range(len(L) - m):
        diff = L[m + i] - L[i]

        if diff > max_diff:
            max_diff = diff

    return max_diff

print(bsp_value([2, 4, 6, 7, 10, 14], 2))