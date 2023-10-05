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