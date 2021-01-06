from src.node import NodeData
from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.sizeV = 0
        self.sizeE = 0
        self.mC = 0
        self.inE = {}
        self.outE = {}

    def v_size(self) -> int:
        return self.sizeV

    def e_size(self) -> int:
        return self.sizeE

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.inE[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.outE[id1]

    def get_mc(self) -> int:
        return self.mC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes.keys() or id2 not in self.nodes.keys():
            return False
        if id2 in self.edges[id1].keys():
            return False
        self.edges[id1][id2] = weight
        if id1 not in self.outE:
            self.outE[id1] = dict()
        self.outE[id1][id2] = weight
        if id2 not in self.inE:
            self.inE[id2] = dict()
        self.inE[id2][id1] = weight
        self.sizeE += 1
        self.mC += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.nodes:
            self.nodes[node_id] = NodeData(node_id, pos)
            self.edges[node_id] = dict()
            self.mC += 1
            self.sizeV += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes.keys():
            for n in self.inE.keys():
                if node_id in self.inE[n].keys():
                    # del self.inE[n][node_id]
                    # self.sizeE -= 1
                    self.remove_edge(node_id, n)
            for n in self.outE.keys():
                if node_id in self.outE[n].keys():
                    # del self.outE[n][node_id]
                    # self.sizeE -= 1
                    self.remove_edge(n, node_id)
            del self.nodes[node_id]
            del self.edges[node_id]
            # if node_id in self.inE.keys():
            #     del self.inE[node_id]
            # if node_id in self.inE.keys():
            #     del self.outE[node_id]
            self.sizeV -= 1
            self.mC += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id2 in self.edges[node_id1].keys():
            del self.edges[node_id1][node_id2]
            del self.outE[node_id1][node_id2]
            del self.inE[node_id2][node_id1]
            self.sizeE -= 1
            self.mC += 1
            return True
        return False
