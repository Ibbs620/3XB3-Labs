from collections import deque
from tools import *
import random

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False
 

#Use the methods below to determine minimum Vertex Covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


############################################
# PRE-EXPERIMENT IMPLEMENTATIONS 
############################################

#Breadth First Search returning path 
def BFS2(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    parent = {node1 : None}
    node_path = []
    #Initializing all nodes except node1 to False
    for node in G.adj: 
        if node != node1: 
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        #Marking all child nodes of current_node as visited
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                parent[node] = current_node
                #Reconstructing the path from node1 to node2 using the parent relation  
                if node == node2: 
                    while node is not None: 
                        node_path.insert(0, node)
                        node = parent[node]
    return node_path   


#Depth First Search returning path 
def DFS2(G, node1, node2):
    # Initialize the stack with the starting node and its path    
    S = [(node1, [node1])]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node, path = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                # If target node is found, return the path
                if node == node2:
                    return path + [node2]
                # Else, push the adjacent node to the stack with its path
                S.append((node, path + [node]))
    return []

# BFS3 and DFS3 implementations

def BFS3(G, start):
    Q = [start]
    pred = {}
    while Q:
        current = Q[0]
        Q = Q[1:]
        for node in G.adjacent_nodes(current):
            if node not in pred.keys() and node != start:
                Q.append(node)
                pred[node] = current
    return pred

def DFS3(G, start):
    S = [start]
    pred = {}
    while S:
        current = S.pop()
        for node in G.adjacent_nodes(current):
            if node not in pred.keys() and node != start:
                S.append(node)
                pred[node] = current
    return pred

# def has_cycle(G):
#     def DFS_cycle(node, parent):
#         marked[node] = True
#         for neighbor in G.adj[node]:
#             if not marked[neighbor]:
#                 if DFS_cycle(neighbor, node):
#                     return True
#             elif parent != neighbor:
#                 return True
#         return False

#     marked = {node: False for node in G.adj}
#     for node in G.adj:
#         if not marked[node]:
#             if DFS_cycle(node, None):
#                 return True
#     return False

def has_cycle(G):
    visited = {}
    parent = {}
    # The stack will store (node, parent) pairs
    stack = []
    for node in G.adj:
        visited[node] = False
        parent[node] = None

    for start_node in G.adj:
        if not visited[start_node]:
            stack.append((start_node, None))

            while stack:
                node, parent_node = stack.pop()
                visited[node] = True
                parent[node] = parent_node

                for neighbor in G.adj[node]:
                    if not visited[neighbor]:
                        stack.append((neighbor, node))
                    elif parent[node] != neighbor:
                        return True
                        
    return False

def DFS_cycle(G, v, marked, in_path):
        marked[v] = True
        in_path[v] = True
        for neighbour in G.adj[v]:
            if marked[neighbour] == False:
                if DFS_cycle(G, neighbour, marked, in_path) == True:
                    return True
            elif in_path[neighbour] == True:
                return True

        in_path[v] = False
        return False

def has_cycle(G):
    marked = [False] * G.number_of_nodes()
    in_path = [False] * G.number_of_nodes()
    for node in range(G.number_of_nodes()):
        if marked[node] == False:
            if DFS_cycle(G, node, marked, in_path) == True:
                return True
    return False


def is_connected(G):
    start_node = list(G.adj.keys())[0]  # Choose any node as the starting point
    reachable = BFS3(G, start_node)  # Or use DFS3
    return all(reachable.values())

############################################
# EXPERIMENT 1 HELPER CLASSES/FUNCTIONS
############################################

# Directed graph class
class DirectedGraph(Graph):
    def add_edge(self, node1, node2):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)

# Random directed graph generator
def create_random_graph(nodes, edges):
    edges = min(nodes * (nodes - 1), edges) # cap number of edges
    possible_edges = []
    for i in range(nodes):
        for j in range(nodes):
            if i == j: 
                continue # avoid self loops
            possible_edges.append([i, j])
    G = DirectedGraph(nodes)
    random.shuffle(possible_edges)
    for i in range(edges):
        edge = possible_edges.pop()
        G.add_edge(edge[0], edge[1])
    return G

############################################
# VERTEX COVER APPROXIMATIONS
############################################

def approx1(G):
    # C := {}
    C = set()
    G1 = deep_copy(G)
    adj = G1.adj
    while not is_vertex_cover(G, C):
        # Find vertex V with max degree
        V = 0
        max_degree = 0
        for vertex, edges in adj.items():
            degree = len(edges)
            if degree > max_degree:
                max_degree = degree
                V = vertex
        
        # Add V to C
        C.add(V)
        # Delete all edges incident to V
        for vertex in adj[V]:
            adj[vertex].remove(V)
        adj[V] = []
    return C

def approx2(G):
    C = set()  # Initialize an empty set C
    available_vertices = list(G.adj.keys())  
    
    while not is_vertex_cover(G, C):  
        v = random.choice(available_vertices)  # Random vertex from available vertices
        C.add(v)  # Add v to C
        available_vertices.remove(v)  # Remove v from the available vertices list
    return C  # Return the Vertex Cover set C

def approx3(G):
    C = []
  
    graph_copy = Graph(len(G.adj))
    for node in G.adj:
        for neighbor in G.adj[node]:
            if not graph_copy.are_connected(node, neighbor):
                graph_copy.add_edge(node, neighbor)

    while not is_vertex_cover(G, C):
        # Get any edge (u, v) from the graph
        u = next(node for node in graph_copy.adj if graph_copy.adjacent_nodes(node))
        v = graph_copy.adjacent_nodes(u)[0]

        # Add u and v to the vertex cover
        C.append(u)
        C.append(v)
        # Remove u, v, and all their incident edges from the graph
        del graph_copy.adj[u]
        del graph_copy.adj[v]
        for node in graph_copy.adj:
            graph_copy.adj[node] = [neighbor for neighbor in graph_copy.adj[node] if neighbor != u and neighbor != v]

    return C

############################################
# MINIMAL INDEPENDANT SET
############################################

def MIS(G):

    def is_independant_set(G, subset):
        for node in G.adj:
            for neighbor in G.adj[node]:
                if node in subset and neighbor in subset:
                    return False
        return True

    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    max_cover = []
    for subset in subsets:
        if is_independant_set(G, subset):
            if len(subset) > len(max_cover):
                max_cover = subset
    return max_cover

def deep_copy(G):
    graph_copy = Graph(len(G.adj))
    for node in G.adj:
        for neighbor in G.adj[node]:
            if not graph_copy.are_connected(node, neighbor):
                graph_copy.add_edge(node, neighbor)
    return graph_copy