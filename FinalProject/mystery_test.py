import math
from tools import *
from final_project_part1 import DirectedWeightedGraph, mystery
import matplotlib.pyplot as plt

node_counts = list(range(5,105,5))
results = initialize_results(node_counts)

for nodes in node_counts:
    for _ in range(num_runs):
        G = create_random_graph(nodes, nodes * 2)
        runtime = measure_runtime(mystery, G)
        # print(f"Nodes: {nodes} Run: {_}")
        results[nodes] += runtime/num_runs

logx = list(map(math.log, node_counts))
logy = list(map(math.log, results.values()))

plt.plot(logx, logy)

for xy in list(zip(logx, logy))[0::19]:
    plt.annotate('(%.3f, %.6f)' % xy, xy = xy)

plt.xlabel('Number of Nodes')
plt.ylabel('Runtime')
plt.title('Runtime of Mystery Algorithm')
plt.grid(True)

plt.show()