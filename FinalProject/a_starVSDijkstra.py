import time
import matplotlib.pyplot as plt
from final_project_part1 import *
from tube_graph import build_graph, compute_h

def run_experiment(graph, stations_filename):
    stations = list(graph.adj.keys())
    a_star_times = []
    dijkstra_times = []

    for i in range(len(stations)):
        for j in range(i+1, len(stations)):
            print(stations[i], stations[j])
            start = stations[i]
            end = stations[j]

            start_time = time.time()
            dijkstra(graph, start)
            dijkstra_time = time.time() - start_time
            dijkstra_times.append(dijkstra_time)

            start_time = time.time()
            a_star(graph, start, end, compute_h(stations_filename, end))
            a_star_time = time.time() - start_time
            a_star_times.append(a_star_time)
    return dijkstra_times, a_star_times

stations_filename = 'london_stations.csv'
connections_filename = 'london_connections.csv'
graph = build_graph(stations_filename, connections_filename, 'Ruislip Manor')

dijkstra_times, a_star_times = run_experiment(graph, stations_filename)

plt.scatter(dijkstra_times, a_star_times)
plt.xlabel('Dijkstra Runtime (s)')
plt.ylabel('A* Runtime (s)')
plt.title('Runtime Comparison between Dijkstra and A*')
plt.show()

