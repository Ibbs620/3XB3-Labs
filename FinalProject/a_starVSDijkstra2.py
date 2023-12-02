import time
import matplotlib.pyplot as plt
from final_project_part1 import *
from tube_graph import build_graph, compute_h

def dijkstra(G, source, sink): # Modified Dijkstra to stop when a sink node is found.
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap2.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap2.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        if current_node == sink:
            return dist[sink]
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist[sink]



def test_case(G, pairs, stations_filename):
    for pair in pairs:
        dijkstra_times = []
        a_star_times = []
        source, sink = pair

        for i in range(1000):
            h = compute_h(stations_filename, sink)
            start = time.time()
            a_star(G, source, sink, h)
            end = time.time()
            a_star_times.append(end - start)

        for i in range(1000):
            start = time.time()
            dijkstra(G, source, sink)
            end = time.time()
            dijkstra_times.append(end - start)


    print(f"Dijkstra: {sum(dijkstra_times)}\tA*: {sum(a_star_times)}")

stations_filename = 'london_stations.csv'
connections_filename = 'london_connections.csv'
graph = build_graph(stations_filename, connections_filename, 'Ruislip Manor')

trivial_paths = [["Heathrow Terminal 4", "South Ealing"], ["Colliers Wood", "Clapham North"], ["Upminster", "West Ham"]]
long_paths = [["Beckton", "Chesham"], ["Morden", "Cockfosters"], ["Epping", "Heathrow Terminal 4"]]
dense_paths = [["Paddington", "Leicester Square"], ["Waterloo","South Kensington"], ["Finchley Road", "Embankment"]]

print("Trivial")
test_case(graph, trivial_paths, stations_filename)
print("Long")
test_case(graph, long_paths, stations_filename)
print("Dense")
test_case(graph, dense_paths, stations_filename)

