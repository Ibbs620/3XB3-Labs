import time
import random
import matplotlib.pyplot as plt
from knapsack import ks_top_down, ks_bottom_up

num_trials = 1

def generate_item_set(num_items, max_weight, max_value, scenario):
    if scenario == "bottom_up_advantage":
        # item set with low weights and high values
        items = [(random.randint(1, 5), random.randint(50, 100)) for _ in range(num_items)]
    else:
        # item set with varying weights and values
        items = [(random.randint(1, max_weight), random.randint(1, max_value)) for _ in range(num_items)]
    return items

def measure_average_runtime(knapsack_func, items, capacity, num_trials):
    total_runtime = 0
    for _ in range(num_trials):
        start_time = time.time()
        knapsack_func(items, capacity)
        end_time = time.time()
        total_runtime += (end_time - start_time)
    return total_runtime / num_trials

item_set_sizes = [100, 200, 300, 400, 500]  

max_weight = 50
max_value = 100

runtimes_td_bottom_up_adv = []
runtimes_bu_bottom_up_adv = []
runtimes_td_top_down_adv = []
runtimes_bu_top_down_adv = []

for num_items in item_set_sizes:
    items_bottom_up_adv = generate_item_set(num_items, max_weight, max_value, "bottom_up_advantage")
    items_top_down_adv = generate_item_set(num_items, max_weight, max_value, "top_down_advantage")
    capacity = num_items * max_weight

    runtime_td_bottom_up_adv = measure_average_runtime(ks_top_down, items_bottom_up_adv, capacity, num_trials)
    runtime_bu_bottom_up_adv = measure_average_runtime(ks_bottom_up, items_bottom_up_adv, capacity, num_trials)
    runtime_td_top_down_adv = measure_average_runtime(ks_top_down, items_top_down_adv, capacity, num_trials)
    runtime_bu_top_down_adv = measure_average_runtime(ks_bottom_up, items_top_down_adv, capacity, num_trials)

    runtimes_td_bottom_up_adv.append(runtime_td_bottom_up_adv)
    runtimes_bu_bottom_up_adv.append(runtime_bu_bottom_up_adv)
    runtimes_td_top_down_adv.append(runtime_td_top_down_adv)
    runtimes_bu_top_down_adv.append(runtime_bu_top_down_adv)



plt.figure(figsize=(12, 6))

# Scenario 1: Bottom-Up Advantage
plt.subplot(1, 2, 1)
plt.plot(item_set_sizes, runtimes_td_bottom_up_adv, label='Top-Down')
plt.plot(item_set_sizes, runtimes_bu_bottom_up_adv, label='Bottom-Up')
plt.xlabel('Number of Items')
plt.ylabel('Runtime (seconds)')
plt.title('Bottom-Up Advantage Scenario')
plt.legend()

# Scenario 2: Top-Down Advantage
plt.subplot(1, 2, 2)
plt.plot(item_set_sizes, runtimes_td_top_down_adv, label='Top-Down')
plt.plot(item_set_sizes, runtimes_bu_top_down_adv, label='Bottom-Up')
plt.xlabel('Number of Items')
plt.ylabel('Runtime (seconds)')
plt.title('Top-Down Advantage Scenario')
plt.legend()

plt.tight_layout()

plt.show()
