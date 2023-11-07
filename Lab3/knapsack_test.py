from knapsack import *

# Test Knapsack brute force approach
items_example = [(2, 16), (10, 10), (15, 3), (5, 6)]
capacity_example = 15

larger_items_example = [(1, 95),(3, 45),(5, 88),(8, 78),(6, 55),(7, 65),(9, 15),(12, 40),(17, 30),(10, 60),]
larger_capacity_example = 50

assert ks_brute_force(items_example, capacity_example) == 26
assert ks_brute_force(larger_items_example, larger_capacity_example) == 501
