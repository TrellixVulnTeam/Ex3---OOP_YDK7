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

    """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """

    def e_size(self) -> int:
        """
       Returns the number of edges in this graph
       @return: The number of edges in this graph
       """
        return self.sizeE

    def get_all_v(self) -> dict:
        """
        return a dictionary of all the nodes in the Graph, each node is represented using a pair  (key, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        if id1 in self.inE.keys():
            return self.inE[id1]
        else:
            return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """
        if id1 in self.outE.keys():
            return self.outE[id1]
        else:
            return None

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
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
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.nodes:
            self.nodes[node_id] = NodeData(node_id, pos)
            self.edges[node_id] = dict()
            self.mC += 1
            self.sizeV += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
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
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if node_id2 in self.edges[node_id1].keys():
            del self.edges[node_id1][node_id2]
            del self.outE[node_id1][node_id2]
            del self.inE[node_id2][node_id1]
            self.sizeE -= 1
            self.mC += 1
            return True
        return False

    def __eq__(self, other: object):
        return self.nodes.keys() == other.nodes.keys() and self.edges.keys() == other.edges.keys() and\
               self.inE.keys() == other.inE.keys() and self.outE.keys() == other.outE.keys() and\
               self.sizeV == other.sizeV and self.sizeE == other.sizeE
