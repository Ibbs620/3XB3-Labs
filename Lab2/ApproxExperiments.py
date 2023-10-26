from graph import *

number_of_nodes = [5,10,15,20,25,30]

for _ in range(1000):
    for node in number_of_nodes:
        print(approx3(create_random_graph(node, int(node * 1.5))))