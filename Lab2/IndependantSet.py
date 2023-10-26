from graph import *
from tools import *

number_of_nodes = [5, 8, 10, 15, 20]
number_of_runs = 10

results_mvc = initialize_results(number_of_nodes)
results_mis = initialize_results(number_of_nodes)
results_sum = initialize_results(number_of_nodes)

for n in number_of_nodes:
    for _ in range(number_of_runs):
        G = create_random_graph(n, int(n * 1.5))
        mvc = MVC(G)
        mis = MIS(G)
        results_mvc[n].append(len(mvc))
        results_mis[n].append(len(mis))
        results_sum[n].append(len(mvc) + len(mis))
        print(mvc)
        print(mis)
        print("------------------------")
        # print("done run", _)
    # print("done", n)

print_results("Minimum Vertex Cover", results_mvc, "Number of Nodes")
print_results("Maximum Independant Set", results_mis, "Number of Nodes")
print_results("Sum of MVC and MIS", results_sum, "Number of Nodes")