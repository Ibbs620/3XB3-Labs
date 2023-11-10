def next_setting(n, m):
    # Initialize a 2D table dp with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # bottom-up dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = float('inf')  # Initialize to a large value
            for k in range(1, j + 1):
                dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]))

    # optimal next value of k 
    next_k = -1
    min_runs = float('inf')
    for k in range(1, n + 1):
        if dp[m][k] < min_runs:
            min_runs = dp[m][k]
            next_k = k

    return next_k


# Test case 1: (Case 2: One Brick)
n1, m1 = 10, 1
next_k1 = next_setting(n1, m1)
print(f"For n={n1} and m={m1}, the optimal next setting is: {next_k1}")

# Test case 2: (Case 3: Two Bricks)
n2, m2 = 10, 2
next_k2 = next_setting(n2, m2)
print(f"For n={n2} and m={m2}, the optimal next setting is: {next_k2}")

# Test case 3: (Larger values)
n3, m3 = 100, 10
next_k3 = next_setting(n3, m3)
print(f"For n={n3} and m={m3}, the optimal next setting is: {next_k3}")
