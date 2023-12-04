import WeightedGraph
from typing import Dict, List

class HeuristicGraph(WeightedGraph):
    def __init__(self):
        super().__init__()
        self.heuristic: Dict[int, float] = {}  
    def set_heuristic(self, heuristic: Dict[int, float]):
        self.heuristic = heuristic

    def get_heuristic(self, node: int) -> float:
        return self.heuristic.get(node, 0.0)
