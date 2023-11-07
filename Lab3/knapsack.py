from itertools import combinations
from tools import *
from typing import List, Tuple

def ks_brute_force(items: [(int,int)], capacity: int) -> int:
    max_value = 0
    # Generate all possible combinations of items
    for r in range(len(items) + 1):
        for subset in combinations(items, r):
            total_weight, total_value = total_weight_value(subset)
            # If the total weight does not exceed the capacity, check if we have a better value
            if total_weight <= capacity:
                max_value = max(max_value, total_value)

    return max_value

def ks_rec(items: [(int,int)], capacity: int) -> int:
    def recurse(i, j):
       if i <= 0 or j <= 0:
           return 0
       elif items[i - 1][0] > j:
            return recurse(i - 1, j)
       return max(recurse(i - 1, j), recurse(i - 1, j - items[i - 1][0]) + items[i - 1][1])
    
    return recurse(len(items), capacity)
    

def ks_bottom_up(items: List[Tuple[int, int]], capacity: int) -> int:
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            weight, value = items[i - 1]
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def ks_top_down(items: List[Tuple[int, int]], capacity: int) -> int:
    n = len(items)
    memo = {}

    def knapsack_recursive(i, w):
        if i == 0 or w == 0:
            return 0
        if (i, w) in memo:
            return memo[(i, w)]

        weight, value = items[i - 1]

        if weight <= w:
            included = knapsack_recursive(i - 1, w - weight) + value
            excluded = knapsack_recursive(i - 1, w)
            result = max(included, excluded)
        else:
            result = knapsack_recursive(i - 1, w)

        memo[(i, w)] = result
        return result

    return knapsack_recursive(n, capacity)
