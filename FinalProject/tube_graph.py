import csv
from final_project_part1 import DirectedWeightedGraph

def build_graph(stations_filename, connections_filename):
    graph = DirectedWeightedGraph()
    id_to_name = {}

    with open(stations_filename, 'r') as stations_file:
        reader = csv.reader(stations_file)
        next(reader)  
        for row in reader:
            id, lat, long, name, display_name, zone, total_lines, rail = row
            graph.add_node(name)
            id_to_name[int(id)] = name

    with open(connections_filename, 'r') as connections_file:
        reader = csv.reader(connections_file)
        next(reader)  # Skip header row
        for row in reader:
            station1, station2, line, time = row
            name1 = id_to_name[int(station1)]
            name2 = id_to_name[int(station2)]
            graph.add_edge(name1, name2, int(time))

    return graph


stations_filename = 'london_stations.csv'
connections_filename = 'London_connections.csv'

graph = build_graph(stations_filename, connections_filename)

print(graph.number_of_nodes())