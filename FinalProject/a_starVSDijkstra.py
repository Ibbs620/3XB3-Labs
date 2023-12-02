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
            break
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist

def run_experiment(graph, stations_filename):
    stations = list(graph.adj.keys())
    a_star_times = []
    dijkstra_times = []
    station_pairs = []  # Store station pairs

    for i in range(len(stations)):
        for j in range(i+1, len(stations)):
            start = stations[i]
            print(start)
            end = stations[j]
            station_pairs.append((start, end))  # Add pair to the list

            # Run Dijkstra
            start_time = time.time()
            dijkstra(graph, start, end)
            dijkstra_time = time.time() - start_time
            dijkstra_times.append(dijkstra_time)

            h = compute_h(stations_filename, end)
            start_time = time.time()
            a_star(graph, start, end, h)
            a_star_time = time.time() - start_time
            a_star_times.append(a_star_time)

    return dijkstra_times, a_star_times, station_pairs

stations_filename = 'london_stations.csv'
connections_filename = 'london_connections.csv'
graph = build_graph(stations_filename, connections_filename, 'Ruislip Manor')

dijkstra_times, a_star_times, station_pairs = run_experiment(graph, stations_filename)

plt.scatter(dijkstra_times, a_star_times)
plt.xlabel('Dijkstra Runtime (s)')
plt.ylabel('A* Runtime (s)')
plt.title('Runtime Comparison between Dijkstra and A*')

plt.show()





