def ks_brute_force(items: [(int,int)], capacity: int) -> int:
    pass

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

