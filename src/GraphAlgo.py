import json
from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.g = DiGraph()

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
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
        """
       Saves the graph in JSON format to a file
       @param file_name: The path to the out file
       @return: True if the save was successful, Flase o.w.
       """
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
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        pass

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        pass

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        pass

    def plot_graph(self) -> None:
        """
       Plots the graph.
       If the nodes have a position, the nodes will be placed there.
       Otherwise, they will be placed in a random but elegant manner.
       @return: None
       """
        pass
