# Directed weighted Graph

## Our project
In this project we presents an implementation of a directed weighted graph using Python.

# Classes

## NodeData:

| Main methods | Explanation |
|------------  | ------------|
| 

## DiGraph:

### Objects:
nodes - Dictionary of nodes in the graph.

edges - Dictionary of all the edges in the graph.

inE - Dictionary of all the nodes that that get an edge from other node.

outE = Dictionary of all the nodes that com out to other node.

sizeV - The number of nodes in the graph.

sizeE - The number of edges in the graph.

| Main methods | Explanation |
|------------  | ------------|
| v_size(self) -> int | Return the number of nodes in the graph. |
| e_size(self) -> int | Return the number of edges in the graph. |
| get_all_v(self) -> dict | Return all the nodes in the graph. |
| all_in_edges_of_node(self, id1: int) -> dict | Return all the edges that come in to a specific node. |
| all_out_edges_of_node(self, id1: int) -> dict | Return all the edges that come out from a specific node. |
| get_mc(self) -> int | Return the mode count of the graph. |
| add_edge(self, id1: int, id2: int, weight: float) -> bool | Add some edge to the graph between two nodes, return true if it success, else return false. |
| add_node(self, node_id: int, pos: tuple = None) -> bool | Add some node to the graph, return true if it success, else return false. |
| remove_node(self, node_id: int) -> bool | Remove a specific node from the graph, return true if it success, else return false. |
| remove_edge(self, node_id1: int, node_id2: int) -> bool | Remove edge between two nodes, return true if it success, else return false. |

## GraphAlgo:

| Main methods | Explanation |
|------------  | -------------|
| get_graph(self) -> GraphInterface  | This method return the directed graph on which the algorithm works on.             |
| load_from_json(self, file_name: str) -> bool| This method loads a graph from a json file, return True if the loading was successful, False o.w.               |
|
