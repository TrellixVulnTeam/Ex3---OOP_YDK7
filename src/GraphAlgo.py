import json
from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from queue import PriorityQueue
from PriorityNode import PriorityNode
from src.node import NodeData
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.g = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name) as file:
                self.g = DiGraph()
                g_f = json.load(file)
                nodes_load = g_f.get('Nodes')
                edges_load = g_f.get('Edges')
                for node in nodes_load:
                    if node.get('pos') is None:
                        self.g.add_node(node.get('id'))
                    else:
                        position = str(node.get('pos')).split(",")
                        position1 = (float(position[0]), float(position[1]), 0.0)
                        self.g.add_node(node.get('id'), position1)
                for edge in edges_load:
                    src = edge.get('src')
                    w = edge.get('w')
                    dest = edge.get('dest')
                    self.g.add_edge(src, dest, w)
                return True
        except FileNotFoundError as fileNotFound:
            print(fileNotFound)
        return False

    def save_to_json(self, file_name: str) -> bool:
        save = dict()
        save["Nodes"] = list()
        save["Edges"] = list()
        for node in self.g.nodes.items():
            if node.location is None:
                pos = '0.0,0.0,0.0'
            else:
                pos = str(node.location[0]) + ',' + str(node.location[1]) + ',' + str(0.0)
            save["Nodes"].append({"pos": pos, "id": node.key})
            for key, w in node.outE.items():
                save["Edges"].append({"src": node.key, "w": w, "dest": key})
        try:
            with open(file_name, 'f') as file:
                json.dump(save, file)
        except IOError as e:
            print(e)
            return False
        return True

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
