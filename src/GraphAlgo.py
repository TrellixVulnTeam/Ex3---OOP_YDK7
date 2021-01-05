from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from queue import PriorityQueue
from PriorityNode import PriorityNode
from src.node import NodeData


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.g = DiGraph()

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def reset_weights_to(self, prm: double) -> None:
        nodes = get_all_v(self.g)
        for n in nodes.keys():
            nodes[n].set_weight(prm)

    def shortest_path_dist(self, id1: int, id2: int) -> double:
        nodes = get_all_v(self.g)
        if id1 not in nodes.keys() or id2 not in nodes.keys():
            return -1
        if id1 == id2:
            return 0
        reset_weights_to(self, -1)
        set_weight(nodes[id1], 0)
        neighs = PriorityQueue()
        edges = all_out_edges_of_node(g, id1)
        for n in edges.keys():
            set_weight(nodes[n], edges[n])
            neighs.put(PriorityNode(get_weight(nodes[n]), nodes[n]))
        while not neighs.empty():
            n = neighs.get()
            node = get_item(n)
            if node == nodes[id2]:
                return get_weight(nodes[id2])
            edges = all_out_edges_of_node(g, get_key(node))
            for i in edges.keys():
                if get_weight(nodes[i]) == -1 or edges[i] + get_weight(node) < get_weight(nodes[i]):
                    set_weight(nodes[i], edges[i] + get_weight(node))
                    neighs.put(PriorityNode(get_weight(nodes[i]), nodes[i]))
        return nodes[id2].get_weight()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
