from graph import *
import matplotlib.pyplot as plt

number_of_edges = [10,20,30,40,50,60,70,80,90,100]
results = {"approx1": [], "approx2": [], "approx3": []}
constant_nodes = 20

for edge in number_of_edges:
    total_sizes = {"approx1": 0, "approx2": 0, "approx3": 0}
    
    for _ in range(1000):
        graph = create_random_graph(constant_nodes, edge)
        
        total_sizes["approx1"] += len(approx1(graph))
        total_sizes["approx2"] += len(approx2(graph))
        total_sizes["approx3"] += len(approx3(graph))
        
    results["approx1"].append(total_sizes["approx1"] / 1000)
    results["approx2"].append(total_sizes["approx2"] / 1000)
    results["approx3"].append(total_sizes["approx3"] / 1000)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(number_of_edges, results["approx1"], marker='o', label="approx1")
plt.plot(number_of_edges, results["approx2"], marker='o', label="approx2")
plt.plot(number_of_edges, results["approx3"], marker='o', label="approx3")
plt.xlabel("Number of Edges")
plt.ylabel("Average Vertex Cover Size")
plt.title("Varying Edges vs Nodes")
plt.legend()
plt.grid(True)
plt.show()
