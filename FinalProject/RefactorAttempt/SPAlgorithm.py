from abc import ABC, abstractmethod
from typing import List
from WeightedGraph import Graph 
import min_heap2

class SPAlgorithm(ABC):
    @abstractmethod
    def calc_sp(self, graph: Graph, source: int, dest: int) -> List[int]:
        pass

class Dijkstra(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> List[int]:
        pred = {}  # Predecessor dictionary
        dist = {}  # Distance dictionary
        Q = min_heap2.MinHeap([])
        nodes = list(graph.adj.keys())

        for node in nodes:
            Q.insert(min_heap2.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, 0)

        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value

            dist[current_node] = current_element.key
            for neighbour in graph.adj[current_node]:
                if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                    pred[neighbour] = current_node

        
        path = []
        current = dest
        while current != source:
            path.insert(0, current)
            current = pred.get(current)
        path.insert(0, source)
        return path


class Bellman_Ford(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> List[int]:
        pred = {}  # Predecessor dictionary
        dist = {}  # Distance dictionary
        nodes = list(graph.adj.keys())

        for node in nodes:
            dist[node] = float("inf")
        dist[source] = 0

        for _ in range(len(nodes) - 1):  
            for node in nodes:
                for neighbour in graph.adj[node]:
                    if dist[node] + graph.w(node, neighbour) < dist[neighbour]:
                        dist[neighbour] = dist[node] + graph.w(node, neighbour)
                        pred[neighbour] = node

        
        path = []
        current = dest
        while current != source:
            path.insert(0, current)
            current = pred.get(current)
        path.insert(0, source)
        return path
 

class A_Star(SPAlgorithm):
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def calc_sp(self, graph: Graph, source: int, dest: int) -> List[int]:
        pred = {}
        dist = {} 
        Q = min_heap2.MinHeap([])
        nodes = list(graph.adj.keys())

        for node in nodes:
            Q.insert(min_heap2.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, self.heuristic[source])

        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key - self.heuristic[current_node]
            if current_node == dest:
                break
            for neighbour in graph.adj[current_node]:
                if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour) + self.heuristic[neighbour])
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                    pred[neighbour] = current_node

        path = [pred[dest], dest]
        current = pred[dest]
        while current != source:
            current = pred[current]
            path.insert(0, current)
        return path