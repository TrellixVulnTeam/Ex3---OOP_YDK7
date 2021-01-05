import json
from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
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

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
