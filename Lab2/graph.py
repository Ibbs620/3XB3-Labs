from collections import deque

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

    def number_of_nodes():
        return len()


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
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


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

def has_cycle(G):
    def DFS_cycle(node, parent):
        marked[node] = True
        for neighbor in G.adj[node]:
            if not marked[neighbor]:
                if DFS_cycle(neighbor, node):
                    return True
            elif parent != neighbor:
                return True
        return False

    marked = {node: False for node in G.adj}
    for node in G.adj:
        if not marked[node]:
            if DFS_cycle(node, None):
                return True
    return False

def is_connected(G):
    start_node = list(G.adj.keys())[0]  # Choose any node as the starting point
    reachable = BFS3(G, start_node)  # Or use DFS3
    return all(reachable.values())
