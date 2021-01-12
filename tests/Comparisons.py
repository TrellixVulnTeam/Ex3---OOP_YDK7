import unittest
from timeit import default_timer

import networkx as nx

from GraphAlgo import GraphAlgo

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = None
        self.graph = GraphAlgo()

    def test_save_and_load1(self):
        file_path10 = '../data/G_10_80_0.json'
        file_path10_1 = '../data/G_10_80_1.json'
        file_path10_2 = '../data/G_10_80_2.json'
        file_path100 = '../data/G_100_800_0.json'
        file_path100_1 = '../data/G_100_800_1.json'
        file_path100_2 = '../data/G_100_800_2.json'
        file_path1000 = '../data/G_1000_8000_0.json'
        file_path1000_1 = '../data/G_1000_8000_1.json'
        file_path1000_2 = '../data/G_1000_8000_2.json'
        file_path10000 = '../data/G_10000_80000_0.json'
        file_path10000_1 = '../data/G_10000_80000_1.json'
        file_path10000_2 = '../data/G_10000_80000_2.json'
        file_path20000 = '../data/G_20000_160000_0.json'
        file_path20000_1 = '../data/G_20000_160000_1.json'
        file_path20000_2 = '../data/G_20000_160000_2.json'
        file_path30000 = '../data/G_30000_240000_0.json'
        file_path30000_1 = '../data/G_30000_240000_1.json'
        file_path30000_2 = '../data/G_30000_240000_2.json'
        graph = GraphAlgo()
        self.assertTrue(graph.load_from_json(file_path10))
        self.assertTrue(graph.save_to_json("test10.json"))
        self.assertTrue(graph.load_from_json(file_path10_1))
        self.assertTrue(graph.save_to_json("test10_1.json"))
        self.assertTrue(graph.load_from_json(file_path10_2))
        self.assertTrue(graph.save_to_json("test10_2.json"))
        self.assertTrue(graph.load_from_json(file_path100))
        self.assertTrue(graph.save_to_json("test100.json"))
        self.assertTrue(graph.load_from_json(file_path100_1))
        self.assertTrue(graph.save_to_json("test100_1.json"))
        self.assertTrue(graph.load_from_json(file_path100_2))
        self.assertTrue(graph.save_to_json("test100_2.json"))
        self.assertTrue(graph.load_from_json(file_path1000))
        self.assertTrue(graph.save_to_json("test1000.json"))
        self.assertTrue(graph.load_from_json(file_path1000_1))
        self.assertTrue(graph.save_to_json("test1000_1.json"))
        self.assertTrue(graph.load_from_json(file_path1000_2))
        self.assertTrue(graph.save_to_json("test1000_2.json"))
        self.assertTrue(graph.load_from_json(file_path10000))
        self.assertTrue(graph.save_to_json("test10000.json"))
        self.assertTrue(graph.load_from_json(file_path10000_1))
        self.assertTrue(graph.save_to_json("test10000_1.json"))
        self.assertTrue(graph.load_from_json(file_path10000_2))
        self.assertTrue(graph.save_to_json("test10000_2.json"))
        self.assertTrue(graph.load_from_json(file_path20000))
        self.assertTrue(graph.save_to_json("test20000.json"))
        self.assertTrue(graph.load_from_json(file_path20000_1))
        self.assertTrue(graph.save_to_json("test20000_1.json"))
        self.assertTrue(graph.load_from_json(file_path20000_2))
        self.assertTrue(graph.save_to_json("test20000_2.json"))
        self.assertTrue(graph.load_from_json(file_path30000))
        self.assertTrue(graph.save_to_json("test30000.json"))
        self.assertTrue(graph.load_from_json(file_path30000_1))
        self.assertTrue(graph.save_to_json("test30000_1.json"))
        self.assertTrue(graph.load_from_json(file_path30000_2))
        self.assertTrue(graph.save_to_json("test30000_2.json"))

    def test_shortest_path(self):
        graph = GraphAlgo()
        file_path10 = '../data/G_10_80_0.json'
        file_path10_1 = '../data/G_10_80_1.json'
        file_path10_2 = '../data/G_10_80_2.json'
        file_path100 = '../data/G_100_800_0.json'
        file_path100_1 = '../data/G_100_800_1.json'
        file_path100_2 = '../data/G_100_800_2.json'
        file_path1000 = '../data/G_1000_8000_0.json'
        file_path1000_1 = '../data/G_1000_8000_1.json'
        file_path1000_2 = '../data/G_1000_8000_2.json'
        file_path10000 = '../data/G_10000_80000_0.json'
        file_path10000_1 = '../data/G_10000_80000_1.json'
        file_path10000_2 = '../data/G_10000_80000_2.json'
        file_path20000 = '../data/G_20000_160000_0.json'
        file_path20000_1 = '../data/G_20000_160000_1.json'
        file_path20000_2 = '../data/G_20000_160000_2.json'
        file_path30000 = '../data/G_30000_240000_0.json'
        file_path30000_1 = '../data/G_30000_240000_1.json'
        file_path30000_2 = '../data/G_30000_240000_2.json'

        self.assertTrue(graph.load_from_json(file_path10))
        print(file_path10)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path10_1))
        print(file_path10_1)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path10_2))
        print(file_path10_2)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path100))
        print(file_path100)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path100_1))
        print(file_path100_1)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path100_2))
        print(file_path100_2)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path1000))
        print(file_path1000)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path1000_1))
        print(file_path1000_1)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path1000_2))
        print(file_path1000_2)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path10000))
        print(file_path10000)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path10000_1))
        print(file_path10000_1)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path10000_2))
        print(file_path10000_2)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path20000))
        print(file_path20000)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path20000_1))
        print(file_path20000_1)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path20000_2))
        print(file_path20000_2)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path30000))
        print(file_path30000)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path30000_1))
        print(file_path30000_1)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

        self.assertTrue(graph.load_from_json(file_path30000_2))
        print(file_path30000_2)
        start = default_timer()
        graph.shortest_path(5, 9)
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.dijkstra_path(G, 5, 9)
        end = default_timer()
        print("time = ", end - start)

    def test_connected_component(self):
        graph = GraphAlgo()
        file_path10 = '../data/G_10_80_0.json'
        file_path10_1 = '../data/G_10_80_1.json'
        file_path10_2 = '../data/G_10_80_2.json'
        file_path100 = '../data/G_100_800_0.json'
        file_path100_1 = '../data/G_100_800_1.json'
        file_path100_2 = '../data/G_100_800_2.json'
        file_path1000 = '../data/G_1000_8000_0.json'
        file_path1000_1 = '../data/G_1000_8000_1.json'
        file_path1000_2 = '../data/G_1000_8000_2.json'
        file_path10000 = '../data/G_10000_80000_0.json'
        file_path10000_1 = '../data/G_10000_80000_1.json'
        file_path10000_2 = '../data/G_10000_80000_2.json'
        file_path20000 = '../data/G_20000_160000_0.json'
        file_path20000_1 = '../data/G_20000_160000_1.json'
        file_path20000_2 = '../data/G_20000_160000_2.json'
        file_path30000 = '../data/G_30000_240000_0.json'
        file_path30000_1 = '../data/G_30000_240000_1.json'
        file_path30000_2 = '../data/G_30000_240000_2.json'

        graph.load_from_json(file_path10)
        print(file_path10)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path10_1)
        print(file_path10_1)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path10_2)
        print(file_path10_2)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path100)
        print(file_path100)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path100_1)
        print(file_path100_1)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path100_2)
        print(file_path100_2)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path1000)
        print(file_path1000)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path1000_1)
        print(file_path1000_1)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path1000_2)
        print(file_path1000_2)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path10000)
        print(file_path10000)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path10000_1)
        print(file_path10000_1)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path10000_2)
        print(file_path10000_2)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path20000)
        print(file_path20000)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path20000_1)
        print(file_path20000_1)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path20000_2)
        print(file_path20000_2)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path30000)
        print(file_path30000)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path30000_1)
        print(file_path30000_1)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path30000_2)
        print(file_path30000_2)
        start = default_timer()
        graph.connected_component(5)
        end = default_timer()
        print("time = ", end - start)

    def test_connected_components(self):
        graph = GraphAlgo()
        file_path10 = '../data/G_10_80_0.json'
        file_path10_1 = '../data/G_10_80_1.json'
        file_path10_2 = '../data/G_10_80_2.json'
        file_path100 = '../data/G_100_800_0.json'
        file_path100_1 = '../data/G_100_800_1.json'
        file_path100_2 = '../data/G_100_800_2.json'
        file_path1000 = '../data/G_1000_8000_0.json'
        file_path1000_1 = '../data/G_1000_8000_1.json'
        file_path1000_2 = '../data/G_1000_8000_2.json'
        file_path10000 = '../data/G_10000_80000_0.json'
        file_path10000_1 = '../data/G_10000_80000_1.json'
        file_path10000_2 = '../data/G_10000_80000_2.json'
        file_path20000 = '../data/G_20000_160000_0.json'
        file_path20000_1 = '../data/G_20000_160000_1.json'
        file_path20000_2 = '../data/G_20000_160000_2.json'
        file_path30000 = '../data/G_30000_240000_0.json'
        file_path30000_1 = '../data/G_30000_240000_1.json'
        file_path30000_2 = '../data/G_30000_240000_2.json'

        graph.load_from_json(file_path10)
        print(file_path10)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path10_1)
        print(file_path10_1)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path10_2)
        print(file_path10_2)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path100)
        print(file_path100)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)


        graph.load_from_json(file_path100_1)
        print(file_path100_1)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path100_2)
        print(file_path100_2)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path1000)
        print(file_path1000)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path1000_1)
        print(file_path1000_1)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path1000_2)
        print(file_path1000_2)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path10000)
        print(file_path10000)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path10000_1)
        print(file_path10000_1)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path10000_2)
        print(file_path10000_2)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path20000)
        print(file_path20000)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path20000_1)
        print(file_path20000_1)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path20000_2)
        print(file_path20000_2)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path30000)
        print(file_path30000)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path30000_1)
        print(file_path30000_1)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)

        graph.load_from_json(file_path30000_2)
        print(file_path30000_2)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        G = nx.DiGraph()
        for i in graph.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph.get_graph().get_all_v().keys():
            for j, w in graph.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)
        start = default_timer()
        nx.strongly_connected_components(G)
        end = default_timer()
        print("time = ", end - start)
        print(end)
        print(start)

if __name__ == '__main__':
    unittest.main()
