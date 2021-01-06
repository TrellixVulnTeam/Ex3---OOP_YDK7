import unittest

from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_get_graph(self):
        # graph = GraphAlgo()
        # graph.get_graph().add_node(0)
        # graph.get_graph().add_node(1)
        # graph.get_graph().add_node(2)
        # graph.get_graph().add_node(3)
        # graph.get_graph().add_edge(0,1,3)
        # graph.get_graph().add_edge(0,2,3)
        # graph.get_graph().add_edge(1,2,4)
        # self.assertEqual(graph.get_graph().v_size(), 4)
        # self.assertEqual(graph.get_graph().e_size(), 3)
        # file_path = '../data/A5'
        # test_path = "../data/test_save.json"
        # self.assertTrue(graph.save_to_json(test_path))
        # self.assertTrue(graph.load_from_json(file_path))
        file_path = '../data/A5'
        test_path = "../data/test_save.json"
        ga = GraphAlgo()
        self.assertTrue(ga.load_from_json(file_path))
        g = ga.get_graph()
        ga.save_to_json(test_path)
        ga1 = GraphAlgo()
        self.assertTrue(ga1.load_from_json(test_path))
        g1 = ga1.get_graph()
        self.assertEqual(g, g1)

    def test_shortest_dist(self):
        graph = GraphAlgo()
        graph.get_graph().add_node(0)
        graph.get_graph().add_node(1)
        graph.get_graph().add_node(2)
        graph.get_graph().add_node(3)
        graph.get_graph().add_edge(0, 1, 3)
        graph.get_graph().add_edge(0, 2, 10)
        graph.get_graph().add_edge(1, 2, 4)
        self.assertEqual(graph.shortest_path_dist(0, 2), 7)

if __name__ == '__main__':
    unittest.main()
