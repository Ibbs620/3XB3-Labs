import csv
from final_project_part1 import DirectedWeightedGraph, a_star

def build_graph(stations_filename, connections_filename, sink):
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
            graph.add_edge(name2, name1, int(time))

    return graph

def compute_h(stations_filename, sink):
    sink_lat = None
    sink_long = None
    h = {}

    with open(stations_filename, 'r') as stations_file:
        reader = csv.reader(stations_file)
        next(reader)  
        for row in reader:
            id, lat, long, name, display_name, zone, total_lines, rail = row
            if name == sink:
                sink_lat = float(lat)
                sink_long = float(long)
        
        stations_file.seek(0)
        next(reader)
        for row in reader:
            id, lat, long, name, display_name, zone, total_lines, rail = row
            lat = float(lat)
            long = float(long)
            h[name] = ((lat - sink_lat) ** 2 + (long - sink_long) ** 2) ** 0.5
    return h


# graph, h = build_graph(stations_filename, connections_filename, 'Ruislip Manor')

# print(graph.number_of_nodes())
# # print(graph.adj)
# print(a_star(graph, 'Clapham South', 'Ruislip Manor', h)[1])