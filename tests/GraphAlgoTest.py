import unittest
import random

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

def setUp1():
    ga = GraphAlgo()
    for i in range(20):
        ga.get_graph().add_node(i)
    for i in range(20):
        weight = random.randint(0, 50)
        n = i
        n1 = i+1
        ga.get_graph().add_edge(n, n1, weight)
    return ga

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = None
        self.ga = GraphAlgo()

    def test_get_graph(self):
        file_path = '../data/A5'
        test_path = "../data/test_save.json"
        ga = GraphAlgo()
        self.assertTrue(ga.load_from_json(file_path))
        self.assertTrue(ga.save_to_json(test_path))
        g = ga.get_graph()
        self.assertTrue(ga.load_from_json(test_path))
        g1 = ga.get_graph()
        self.assertTrue(g.__eq__(g1))

    def test_save_and_load(self):
        file_path1 = '../data/A0'
        file_path2 = '../data/A1'
        file_path3 = '../data/A2'
        file_path4 = '../data/A3'
        file_path5 = '../data/A4'
        file_path6 = '../data/A5'
        file_path7 = '../data/A5_edited'
        file_path8 = '../data/T0.json'
        file_path9 = '../data/T0.json_saved'
        test_json = "../data/test_save.json"
        self.assertTrue(self.ga.load_from_json(file_path1))
        self.assertTrue(self.ga.save_to_json("test1.json"))
        self.assertTrue(self.ga.load_from_json(file_path2))
        self.assertTrue(self.ga.save_to_json("test2.json"))
        self.assertTrue(self.ga.load_from_json(file_path3))
        self.assertTrue(self.ga.save_to_json("test3.json"))
        self.assertTrue(self.ga.load_from_json(file_path4))
        self.assertTrue(self.ga.save_to_json("test4.json"))
        self.assertTrue(self.ga.load_from_json(file_path5))
        self.assertTrue(self.ga.save_to_json("test5.json"))
        self.assertTrue(self.ga.load_from_json(file_path6))
        self.assertTrue(self.ga.save_to_json("test6.json"))
        self.assertTrue(self.ga.load_from_json(file_path7))
        self.assertTrue(self.ga.save_to_json("test7.json"))
        self.assertTrue(self.ga.load_from_json(file_path8))
        self.assertTrue(self.ga.save_to_json("test8.json"))
        self.assertTrue(self.ga.load_from_json(file_path9))
        self.assertTrue(self.ga.save_to_json("test9.json"))
        g = self.ga.get_graph()
        self.ga.save_to_json(test_json)
        ga1 = GraphAlgo()
        self.assertTrue(ga1.load_from_json(test_json))
        g1 = self.ga.get_graph()
        self.assertEqual(g, g1)

    def test_shortest_dist(self):
        graph = GraphAlgo(DiGraph())
        graph.get_graph().add_node(0)
        graph.get_graph().add_node(1)
        graph.get_graph().add_node(2)
        graph.get_graph().add_node(3)
        graph.get_graph().add_edge(0, 1, 3)
        graph.get_graph().add_edge(0, 2, 10)
        graph.get_graph().add_edge(1, 2, 4)
        self.assertEqual(graph.shortest_path_dist(0, 2), 7)

    def test_shortest_path(self):
        graph = GraphAlgo(DiGraph())
        graph.get_graph().add_node(0)
        graph.get_graph().add_node(1)
        graph.get_graph().add_node(2)
        graph.get_graph().add_node(3)
        graph.get_graph().add_edge(0, 1, 3)
        graph.get_graph().add_edge(0, 2, 10)
        graph.get_graph().add_edge(1, 2, 4)
        path = [0, 1, 2]
        self.assertEqual(graph.shortest_path(0, 2), (7, path))

    def test_shortest_path1(self):
        file_path = '../data/G_1000_8000_2.json'
        graph = GraphAlgo()
        graph.load_from_json(file_path)
        self.assertEqual(graph.shortest_path(579, 821), (63.1757198022814, [579, 314, 41, 497, 821]))
        file_path1 = '../data/G_30000_240000_1.json'
        graph.load_from_json(file_path1)
        self.assertEqual(graph.shortest_path(10009, 25), (98.3231525358059, [10009, 13860, 6357, 14834,
                                                                             12949, 27071, 15176, 26170,
                                                                             20714, 14763, 15235, 4750, 25]))

    def test_connected_component(self):
        graph = GraphAlgo(DiGraph())
        graph.get_graph().add_node(0)
        graph.get_graph().add_node(1)
        graph.get_graph().add_node(2)
        graph.get_graph().add_node(3)
        graph.get_graph().add_edge(0, 1, 3)
        graph.get_graph().add_edge(0, 2, 10)
        graph.get_graph().add_edge(1, 2, 4)
        self.assertEqual(graph.connected_component(3), [3])
        graph.get_graph().add_edge(2, 0, 6)
        self.assertEqual(graph.connected_component(0), [0, 1, 2])

    def test_connected_component1(self):
        file_path = '../data/G_10_80_1.json'
        graph = GraphAlgo()
        graph.load_from_json(file_path)
        self.assertEqual(graph.connected_component(1), [1, 0, 2, 3, 4, 5, 6, 7, 8, 9])
        graph.get_graph().add_edge(2, 0, 6)
        self.assertEqual(graph.connected_component(0), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_connected_components(self):
        graph = GraphAlgo(DiGraph())
        graph.get_graph().add_node(0)
        graph.get_graph().add_node(1)
        graph.get_graph().add_node(2)
        graph.get_graph().add_node(3)
        graph.get_graph().add_edge(0, 1, 3)
        graph.get_graph().add_edge(0, 2, 10)
        graph.get_graph().add_edge(1, 2, 4)
        self.assertEqual(graph.connected_component(3), [3])
        self.assertEqual(graph.connected_component(0), [0])
        self.assertEqual(graph.connected_component(1), [1])
        self.assertEqual(graph.connected_component(2), [2])
        graph.get_graph().add_edge(2, 0, 6)
        self.assertEqual(graph.connected_components(), [[0, 1, 2], [3]])
        # graph.load_from_json(file_path1)
        # self.assertEqual(graph.connected_components(), [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])

    def test_plot_graph(self):
        graph = GraphAlgo()
        graph.load_from_json('../data/A5')
        graph.plot_graph()




if __name__ == '__main__':
    unittest.main()
