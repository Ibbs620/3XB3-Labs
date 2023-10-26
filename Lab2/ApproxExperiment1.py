from graph import *
import matplotlib.pyplot as plt


number_of_nodes = [5,10,15,20,25,30]
results = {"approx1": [], "approx2": [], "approx3": []}

for node in number_of_nodes:
    total_sizes = {"approx1": 0, "approx2": 0, "approx3": 0}
    
    for _ in range(1000):
        graph = create_random_graph(node, int(node * 1.5))
        
        total_sizes["approx1"] += len(approx1(graph))
        total_sizes["approx2"] += len(approx2(graph))
        total_sizes["approx3"] += len(approx3(graph))
        
    results["approx1"].append(total_sizes["approx1"] / 1000)
    results["approx2"].append(total_sizes["approx2"] / 1000)
    results["approx3"].append(total_sizes["approx3"] / 1000)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(number_of_nodes, results["approx1"], marker='o', label="approx1")
plt.plot(number_of_nodes, results["approx2"], marker='o', label="approx2")
plt.plot(number_of_nodes, results["approx3"], marker='o', label="approx3")
plt.xlabel("Number of Nodes")
plt.ylabel("Average Vertex Cover Size")
plt.title("Approximation Experiment 1")
plt.legend()
plt.grid(True)
plt.show()
