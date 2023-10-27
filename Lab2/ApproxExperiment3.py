from graph import *
import matplotlib.pyplot as plt

number_of_nodes = [5,10,15,20,25,30,35,40,45,50]
densities = [1 / x for x in range(1,11)]
results = {"approx1": [], "approx2": [], "approx3": []}

for dense in densities:
    total_sizes = {"approx1": 0, "approx2": 0, "approx3": 0}
    
    for node in number_of_nodes:
        edges = int(node * (node - 1) * 0.5 * dense)
        for _ in range(100):
            graph = create_random_graph(node, edges)
            
            total_sizes["approx1"] += len(approx1(graph)) / node
            total_sizes["approx2"] += len(approx2(graph)) / node
            total_sizes["approx3"] += len(approx3(graph)) / node
        
    results["approx1"].append(total_sizes["approx1"] / 1000)
    results["approx2"].append(total_sizes["approx2"] / 1000)
    results["approx3"].append(total_sizes["approx3"] / 1000)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(densities, results["approx1"], marker='o', label="approx1()")
plt.plot(densities, results["approx2"], marker='o', label="approx2()")
plt.plot(densities, results["approx3"], marker='o', label="approx3()")
plt.xlabel("Graph density")
plt.ylabel("Average % of nodes in vertex cover")
plt.title("Low vs High Density Graph")
plt.legend()
plt.grid(True)
plt.show()
