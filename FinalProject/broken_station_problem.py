def solve_bsp(stations, m):
    n = len(stations)
    DP = [[float('inf') for _ in range(n)] for _ in range(m+1)]

    # Base case m = 0
    dist = [abs(stations[i] - stations[i-1]) for i in range(1, n)]
    for i in range(1, n):
        DP[0][i] = min(dist[:i])
    
    # Fill out DP table
    for i in range(1, m+1):
        for j in range(i + 1, n):
            DP[i][j] = 0
            for k in range(i + 1):
                DP[i][j] = max(DP[i][j], min(abs(stations[j-k-1] - stations[j]), DP[i - k][j - k - 1]))

            # DP Formula:
            # DP[i][j] = max( min( |station[j - k - 1] - station[j]| ), DP[i - k][j - k - 1] ) for 0 <= k <= i
    
    return DP

def bsp_value(stations, m):
    DP = solve_bsp(stations, m)
    return DP[m][len(stations)-1]

def bsp_solution(stations, m):
    DP = solve_bsp(stations, m)
    solution = stations.copy()

    # Start at bottom right of table
    i = m
    j = len(stations)-1

    while(j >= 0): 
        if i <= 0:
            j -= 1
            i = m
            continue

        for k in range(1, i + 1):
            s = min(abs(stations[j-k-1] - stations[j]), DP[i - k][j - k - 1]) 
            if DP[i][j] == s: # Check if the optimal k for station j is not 0
                j -= k
                m -= k
                i = m
                solution.remove(stations[j]) # If k != 0, station j - 1 is removed
                continue
            
    return solution

# Test
stations = [2, 4, 6, 7, 10, 14]
m = 2

# Print table, value, and solution
for x in solve_bsp(stations, m):
    print('\t'.join(map(str, x)))
print(bsp_value(stations, m))
print(bsp_solution(stations, m))