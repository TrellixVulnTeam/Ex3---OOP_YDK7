import unittest
from tests import GraphAlgoTest as gat
from GraphAlgo import GraphAlgo

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = None
        self.graph = GraphAlgo()



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
        # self.assertTrue(graph.load_from_json(file_path10))
        # self.assertEqual(graph.shortest_path(0, 5), (38.26679232313723, [0, 5]))
        # self.assertTrue(graph.load_from_json(file_path10_1))
        # self.assertEqual(graph.shortest_path(5, 9), (37.723507485787174, [5, 3, 9]))
        # self.assertTrue(graph.load_from_json(file_path10_2))
        # self.assertEqual(graph.shortest_path(5, 9), (15.250866713272554, [5, 3, 9]))
        # self.assertTrue(graph.load_from_json(file_path100))
        # self.assertEqual(graph.shortest_path(5, 9), (61.325370289776004, [5, 50, 31, 49, 55, 63, 9]))
        # self.assertTrue(graph.load_from_json(file_path100_1))
        # self.assertEqual(graph.shortest_path(5, 9), (51.07748442582462, [5, 7, 87, 9]))
        # self.assertTrue(graph.load_from_json(file_path100_2))
        # self.assertEqual(graph.shortest_path(5, 9), (71.17147145223024, [5, 38, 96, 70, 45, 53, 1, 9]))
        # self.assertTrue(graph.load_from_json(file_path1000))
        # self.assertEqual(graph.shortest_path(5, 9), (50.49842628124965, [5, 812, 699, 261, 9]))
        # self.assertTrue(graph.load_from_json(file_path1000_1))
        # self.assertEqual(graph.shortest_path(5, 9), (82.73889534441577, [5, 281, 965, 501, 193, 855, 566, 445, 9]))
        # self.assertTrue(graph.load_from_json(file_path1000_2))
        # self.assertEqual(graph.shortest_path(5, 9), (82.73889534441577, [5, 281, 965, 501, 193, 855, 566, 445, 9]))
        self.assertTrue(graph.load_from_json(file_path10000))
        self.assertEqual(graph.shortest_path(5, 9), (88.77008094461154, [5, 584, 6721, 654, 7467, 8921, 658, 8850, 9]))
        # graph.assertTrue(graph.load_from_json(file_path10000_1))
        # graph.assertTrue(graph.load_from_json(file_path10000_2))
        # graph.assertTrue(graph.load_from_json(file_path20000))
        # graph.assertTrue(graph.load_from_json(file_path20000_1))
        # graph.assertTrue(graph.load_from_json(file_path20000_2))
        # graph.assertTrue(graph.load_from_json(file_path30000))
        # graph.assertTrue(graph.load_from_json(file_path30000_1))
        # graph.assertTrue(graph.load_from_json(file_path30000_2))


if __name__ == '__main__':
    unittest.main()
