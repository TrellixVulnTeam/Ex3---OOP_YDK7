import unittest
from timeit import default_timer
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
        self.assertEqual(graph.shortest_path(0, 5), (38.26679232313723, [0, 5]))
        self.assertTrue(graph.load_from_json(file_path10_1))
        self.assertEqual(graph.shortest_path(5, 9), (37.723507485787174, [5, 3, 9]))
        self.assertTrue(graph.load_from_json(file_path10_2))
        self.assertEqual(graph.shortest_path(5, 9), (15.250866713272554, [5, 3, 9]))
        self.assertTrue(graph.load_from_json(file_path100))
        self.assertEqual(graph.shortest_path(5, 9), (61.325370289776004, [5, 50, 31, 49, 55, 63, 9]))
        self.assertTrue(graph.load_from_json(file_path100_1))
        self.assertEqual(graph.shortest_path(5, 9), (51.07748442582462, [5, 7, 87, 9]))
        self.assertTrue(graph.load_from_json(file_path100_2))
        self.assertEqual(graph.shortest_path(5, 9), (71.17147145223024, [5, 38, 96, 70, 45, 53, 1, 9]))
        self.assertTrue(graph.load_from_json(file_path1000))
        self.assertEqual(graph.shortest_path(5, 9), (50.49842628124965, [5, 812, 699, 261, 9]))
        self.assertTrue(graph.load_from_json(file_path1000_1))
        self.assertEqual(graph.shortest_path(5, 9), (82.73889534441577, [5, 281, 965, 501, 193, 855, 566, 445, 9]))
        self.assertTrue(graph.load_from_json(file_path1000_2))
        self.assertEqual(graph.shortest_path(5, 9), (82.73889534441577, [5, 281, 965, 501, 193, 855, 566, 445, 9]))
        self.assertTrue(graph.load_from_json(file_path10000))
        self.assertEqual(graph.shortest_path(5, 9), (88.77008094461154, [5, 584, 6721, 654, 7467, 8921, 658, 8850, 9]))
        self.assertTrue(graph.load_from_json(file_path10000_1))
        self.assertEqual(graph.shortest_path(5, 9), (61.51571248523145, [5, 8045, 6969, 5721, 7161, 9]))
        self.assertTrue(graph.load_from_json(file_path10000_2))
        self.assertEqual(graph.shortest_path(5, 9), (101.62397328248102,
                                                     [5, 2280, 1890, 2384, 2206, 621, 97, 543, 3915, 1393, 8501, 1912, 6206, 9]))
        self.assertTrue(graph.load_from_json(file_path20000))
        self.assertEqual(graph.shortest_path(5, 9), (88.59607570108169, [5, 15120, 569, 7470, 14626, 7580, 15174, 9]))
        self.assertTrue(graph.load_from_json(file_path20000_1))
        self.assertEqual(graph.shortest_path(5, 9), (101.19512716343222, [5, 18105, 16333, 18131, 5384, 14100, 10146, 10400, 14687, 13594, 5629, 9]))
        self.assertTrue(graph.load_from_json(file_path20000_2))
        self.assertEqual(graph.shortest_path(5, 9), (91.67365540222936, [5, 9586, 17116, 6712, 17031, 16627, 18157, 5874, 15412, 9]))
        self.assertTrue(graph.load_from_json(file_path30000))
        self.assertEqual(graph.shortest_path(5, 9), (122.34873654355629, [5, 23820, 28126, 7764, 17996, 880, 29782, 5994, 4484, 1291, 23394, 6216, 9]))
        self.assertTrue(graph.load_from_json(file_path30000_1))
        self.assertEqual(graph.shortest_path(5, 9), (104.41002304844527, [5, 29316, 28709, 6060, 23767, 9]))
        self.assertTrue(graph.load_from_json(file_path30000_2))
        self.assertEqual(graph.shortest_path(5, 9), (116.7185542758249, [5, 20134, 26258, 7514, 13529, 17494, 9466, 15888, 15760, 6726, 9]))

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
        # graph.load_from_json(file_path10)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path10_1)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path10_2)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path100)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path100_1)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path100_2)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path1000)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path1000_1)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path1000_2)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path10000)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path10000_1)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path10000_2)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path20000)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path20000_1)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path20000_2)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path30000)
        # print(graph.connected_component(5))
        # graph.load_from_json(file_path30000_1)
        # print(graph.connected_component(5))
        graph.load_from_json(file_path30000_2)
        print(graph.connected_component(5))

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
        # graph.load_from_json(file_path10)
        # print(graph.connected_components())
        # graph.load_from_json(file_path10_1)
        # print(graph.connected_components())
        # graph.load_from_json(file_path10_2)
        # print(graph.connected_components())
        # graph.load_from_json(file_path100)
        # print(graph.connected_components())
        # graph.load_from_json(file_path100_1)
        # print(graph.connected_components())
        # graph.load_from_json(file_path100_2)
        # print(graph.connected_components())
        # graph.load_from_json(file_path1000)
        # print(graph.connected_components())
        # graph.load_from_json(file_path1000_1)
        # print(graph.connected_components())
        # graph.load_from_json(file_path1000_2)
        # print(graph.connected_components())
        graph.load_from_json(file_path30000)
        start = default_timer()
        graph.connected_components()
        end = default_timer()
        print("time = ", end - start)
        # graph.load_from_json(file_path10000_1)
        # print(graph.connected_components())
        # graph.load_from_json(file_path10000_2)
        # print(graph.connected_components())
        # graph.load_from_json(file_path20000)
        # print(graph.connected_components())
        # graph.load_from_json(file_path20000_1)
        # print(graph.connected_components())
        # graph.load_from_json(file_path20000_2)
        # print(graph.connected_components())
        # graph.load_from_json(file_path30000)
        # print(graph.connected_components())
        # graph.load_from_json(file_path30000_1)
        # print(graph.connected_components())
        # graph.load_from_json(file_path30000_2)
        # print(graph.connected_components())


if __name__ == '__main__':
    unittest.main()
