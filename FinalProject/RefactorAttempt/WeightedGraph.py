from abc import ABC, abstractmethod
from typing import List, Dict

class Graph(ABC):
    @abstractmethod
    def get_adj_nodes(self, node: int) -> List[int]:
        pass

    @abstractmethod
    def add_node(self, node: int):
        pass

    @abstractmethod
    def add_edge(self, start: int, end: int, weight: float):
        pass

    @abstractmethod
    def get_num_of_nodes(self) -> int:
        pass

    @abstractmethod
    def w(self, node1: int, node2: int) -> float:
        pass

class WeightedGraph(Graph):
    def __init__(self):
        self.adj = {}
        self.weights = {}

    def get_adj_nodes(self, node: int) -> List[int]:
        return self.adj.get(node, [])

    def add_node(self, node: int):
        self.adj[node] = []

    def add_edge(self, start: int, end: int, weight: float):
        if start in self.adj: 
            self.adj[start].append(end)
            self.weights[(start, end)] = weight

    def get_num_of_nodes(self) -> int:
        return len(self.adj)

    def w(self, node1: int, node2: int) -> float:
        return self.weights.get((node1, node2), 0.0)
