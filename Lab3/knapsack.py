from itertools import combinations
from tools import *

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
    

def ks_bottom_up(items: [(int,int)], capacity: int) -> int:
    pass

def ks_top_down(items: [(int,int)], capacity: int) -> int:
    pass

