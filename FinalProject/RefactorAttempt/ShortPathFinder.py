from WeightedGraph import Graph 
import SPAlgorithm

class ShortPathFinder:
    def __init__(self):
        self.graph = None
        self.algorithm = None

    def set_graph(self, graph: Graph):
        self.graph = graph

    def set_algorithm(self, algorithm: SPAlgorithm):
        self.algorithm = algorithm

    def calc_short_path(self, source: int, dest: int) -> float:
        if not self.graph or not self.algorithm:
            raise ValueError("Graph or algorithm not set")
        return self.algorithm.calc_sp(self.graph, source, dest)
