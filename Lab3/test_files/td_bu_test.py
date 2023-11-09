import time
import random
import matplotlib.pyplot as plt
from knapsack import ks_top_down, ks_bottom_up


def generate_random_items(num_items, max_weight, max_value):
    items = [(random.randint(1, max_weight), random.randint(1, max_value)) for _ in range(num_items)]
    return items


def measure_runtime(knapsack_func, items, capacity):
    start_time = time.time()
    knapsack_func(items, capacity)
    end_time = time.time()
    return end_time - start_time


item_set_sizes = [10, 20, 30, 40, 50]  
max_weight = 50
max_value = 100


runtimes_td = []
runtimes_bu = []

for num_items in item_set_sizes:
    items = generate_random_items(num_items, max_weight, max_value)
    capacity = num_items * max_weight  

    runtime_td = measure_runtime(ks_top_down, items, capacity)
    runtime_bu = measure_runtime(ks_bottom_up, items, capacity)

    runtimes_td.append(runtime_td)
    runtimes_bu.append(runtime_bu)


plt.figure(figsize=(10, 6))
plt.plot(item_set_sizes, runtimes_td, label='Top-Down')
plt.plot(item_set_sizes, runtimes_bu, label='Bottom-Up')
plt.xlabel('Number of Items')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime vs Number of Items')
plt.legend()
plt.grid(True)
plt.show()
