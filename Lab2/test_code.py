from graph import *

G = Graph(7)
G.add_edge(1,2)
G.add_edge(2,4)
G.add_edge(4,6)
G.add_edge(3,5)
G.add_edge(1,3)
G.add_edge(3,4)
G.add_edge(4,5)

correct_bfs_pred = {2 : 1, 3 : 1, 4 : 2, 5 : 3, 6 : 4}
bfs_pred = BFS3(G, 1)
dfs_pred = DFS3(G, 1)
assert correct_bfs_pred == bfs_pred
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