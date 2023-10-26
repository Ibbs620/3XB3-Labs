from graph import *

number_of_edges = [10,20,30,40,50,60,70,80,90,100]

for _ in range(1000):
    for node in number_of_edges:
        print(approx3(create_random_graph(node, int(node * 1.5))))