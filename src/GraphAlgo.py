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
       @return: True if the save was successful, False o.w.
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

    def reset_weights_to(self, prm: float) -> None:
        """
         resets all weights of nodes in the graph to a given value.
         @param prm - the value to reset to.
        """
        nodes = self.g.get_all_v()
        for n in nodes.keys():
            nodes[n].set_weight(prm)

    def min_neighbor(self, id1) -> int:
        """
         finds the min weight neighbor to a node around it (directionally).
         @param id1
         @return the min src node that n is neighbor to.
        """
        neighs = self.g.all_in_edges_of_node(id1)
        nodes = self.g.get_all_v()
        min_weight = nodes[id1].get_weight()
        min_key = id1
        for n in neighs.keys():
            if nodes[n].get_weight() < min_weight and nodes[n].get_weight() != -1:
                min_key = n
        return min_key

    def shortest_path_dist(self, id1: int, id2: int) -> float:
        """
         using the Dijkstra algorithm. The function resets all tags to -1 using resetWeightsTo(-1).
         An iterator sets every node's weight to the distance from the source starting from 0 on source node.
         @param id1 - start node
         @param id2 - end (target) node
         @return  the shortest path's distance to a destination node from the source node
        """
        nodes = self.g.get_all_v()
        if id1 not in nodes.keys() or id2 not in nodes.keys():
            return -1
        if id1 == id2:
            return 0
        self.reset_weights_to(-1)
        nodes[id1].set_weight(0)
        neighs = PriorityQueue()
        edges = self.g.all_out_edges_of_node(id1)
        for n in edges.keys():
            nodes[n].set_weight(edges[n])
            neighs.put(PriorityNode(nodes[n].get_weight(), nodes[n]))
        while not neighs.empty():
            n = neighs.get()
            node = n.get_item()
            if node == nodes[id2]:
                return nodes[id2].get_weight()
            edges = self.g.all_out_edges_of_node(node.get_key())
            for i in edges.keys():
                if nodes[i].get_weight() == -1 or edges[i] + node.get_weight() < nodes[i].get_weight():
                    nodes[i].set_weight(edges[i] + node.get_weight())
                    neighs.put(PriorityNode(nodes[i].get_weight(), nodes[i]))
        return nodes[id2].get_weight()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
         using Dijkstra's algorithm.
         using shortest_path_dist(id1, id2) all the nodes has weights set to the distance from the source to them.
         if there's no such path the function returns null. else, the function
         adds each time a node to a list from the destination node to the source using the weight to decide the path
         (the path must go through each minimal neighbor weight from n to 0 once,
          - n being the distance to destination node).
         @param id1 - start node
         @param id2 - end (target) node
         @return  the shortest path as a list and distance to the destination node from the source node.
        """
        distance = self.shortest_path_dist(id1, id2)
        if distance == -1:
            return None
        path_mirror = [id1]
        if distance == 0:
            return 0, path_mirror
        path_mirror.remove(id1)
        curr = id2
        while curr != id1:
            path_mirror.append(curr)
            curr = self.min_neighbor(curr)
        path_mirror.append(curr)
        path = []
        for x in path_mirror:
            path.append(path_mirror.remove(x))
        return distance, path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        nodes = self.g.get_all_v()
        if id1 not in nodes.keys():
            return []
        neighbors = [id1]
        for n in nodes.keys():
            if self.shortest_path_dist(id1, n) != -1 and self.shortest_path_dist(n, id1) != -1:
                if self.shortest_path_dist(id1, n) != 0:
                    neighbors.append(n)
        return neighbors

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        nodes = self.g.get_all_v()
        all_connected = []
        for n in nodes.keys():
            neighs = self.connected_component(n)
            all_connected.append(neighs)
        return all_connected

    def plot_graph(self) -> None:
        """
       Plots the graph.
       If the nodes have a position, the nodes will be placed there.
       Otherwise, they will be placed in a random but elegant manner.
       @return: None
       """
        pass
