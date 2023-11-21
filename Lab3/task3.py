def number_of_wc_runs(n, m):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(2, n + 1):
        dp[1][i] = i - 1

    for i in range(2, m + 1):
        for j in range(1, n + 1):
            min_worst_case = 99999999999
            for k in range(1, j + 1):
                 min_worst_case = min(min_worst_case, max(dp[i - 1][k - 1], dp[i][j - k]))
            dp[i][j] = 1 + min_worst_case

    return dp[m][n]

print(number_of_wc_runs(100,2))