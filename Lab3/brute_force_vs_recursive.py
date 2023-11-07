from tools import *
from knapsack import ks_brute_force, ks_rec
import matplotlib.pyplot as plt

results_rec = initialize_results(item_set_sizes)
results_bf = initialize_results(item_set_sizes)

for size in item_set_sizes:
    bf, rec = 0, 0
    for _ in range(num_runs):
        items, weight = generate_knapsack(size)
        bf += measure_runtime(ks_brute_force, items, weight) / num_runs
        rec += measure_runtime(ks_rec, items, weight) / num_runs
    results_bf[size] = bf
    results_rec[size] = rec
    
    print(bf, rec)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)

plt.plot(item_set_sizes, results_rec.values(), label = 'Recursive')
plt.plot(item_set_sizes, results_bf.values(), label= 'Brute Force')
plt.xlabel('Number of items in knapsack')
plt.ylabel('Runtime')
plt.title('Brute Force vs Recursive Knapsack')
plt.grid(True)


plt.subplot(1, 2, 2)
plt.plot(item_set_sizes[:5], list(results_rec.values())[:5], label = 'Recursive')
plt.plot(item_set_sizes[:5], list(results_bf.values())[:5], label= 'Brute Force')
plt.xlabel('Number of items in knapsack')
plt.ylabel('Runtime')
plt.title('Brute Force vs Recursive Knapsack  (2 <= size <= 10)')
plt.grid(True)

plt.show()