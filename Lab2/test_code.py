from graph import *

G = Graph(7)
G.add_edge(1,2)
G.add_edge(2,4)
G.add_edge(4,6)
G.add_edge(3,5)
G.add_edge(1,3)
G.add_edge(3,4)
G.add_edge(4,5)

# DFS3 and BFS3 testing
correct_bfs_pred = {2 : 1, 3 : 1, 4 : 2, 5 : 3, 6 : 4}
correct_dfs_pred = {2 : 1, 3 : 1, 4 : 3, 5 : 3, 6 : 4}
bfs_pred = BFS3(G, 1)
dfs_pred = DFS3(G, 1)
assert correct_bfs_pred == bfs_pred
assert correct_dfs_pred == dfs_pred
print(dfs_pred)
print(bfs_pred)


# DFS2 and BFS2 testing
correct_path_bfs = [1, 2, 4, 6]
correct_path_dfs = [1, 3, 4, 6]
bfs_path = BFS2(G, 1, 6)
dfs_path = DFS2(G, 1, 6)
assert correct_path_bfs == bfs_path
assert correct_path_dfs == dfs_path
print(dfs_path)
print(bfs_path)

# CHECK create_random_graph() OUTPUT
print(create_random_graph(10, 15).adj)

# Test VC approximations (can only test approx1 since the other implementations are random)
correct_VC1 = {1, 3, 4}
VC1 = approx1(G)
assert VC1 == correct_VC1

DG1 = DirectedGraph(7)
DG1.add_edge(1,2)
DG1.add_edge(2,3)
DG1.add_edge(5,6)
DG1.add_edge(4,1)
assert not has_cycle(DG1)

DG2 = DirectedGraph(3)
DG2.add_edge(1,2)
DG2.add_edge(2,0)
DG2.add_edge(0,1)
print(DG2.adj)
assert has_cycle(DG2)