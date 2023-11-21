import math
from tools import *
from final_project_part1 import DirectedWeightedGraph, mystery, create_random_complete_graph
import matplotlib.pyplot as plt

# Negative Weight Testing (with no negative cycles)
 
G = DirectedWeightedGraph()
for i in range(5):
    G.add_node(i)
G.add_edge(0, 1, 3)
G.add_edge(0, 2, 8)
G.add_edge(0, 4, -4)
G.add_edge(1, 4, 7)
G.add_edge(1, 3, 1)
G.add_edge(2, 1, 4)
G.add_edge(3, 0, 2)
G.add_edge(3, 2, -5)
G.add_edge(4, 3, 6)

d = mystery(G)
correct_d = [[0, 1, -3, 2, -4],
             [3, 0, -4, 1, -1],
             [7, 4, 0, 5, 3],
             [2, -1, -5, 0, -2],
             [8, 5, 1, 6, 0]]

print(d)
print(correct_d)
try:
    assert correct_d == d
except:
    print("Does not work with negative edges")

# Runtime Testing

node_counts = list(range(5,105,5))
results = initialize_results(node_counts)

for nodes in node_counts:
    for _ in range(num_runs):
        G = create_random_complete_graph(nodes, nodes * 2)
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