import unittest

from GraphAlgo import GraphAlgo

class Comparisons(unittest.TestCase):

    def setUp(self) -> None:
        self.graph = None
        self.ga = GraphAlgo()

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
        self.assertTrue(self.ga.load_from_json(file_path10))
        self.assertTrue(self.ga.save_to_json("test10.json"))
        self.assertTrue(self.ga.load_from_json(file_path10_1))
        self.assertTrue(self.ga.save_to_json("test10_1.json"))
        self.assertTrue(self.ga.load_from_json(file_path10_2))
        self.assertTrue(self.ga.save_to_json("test10_2.json"))
        self.assertTrue(self.ga.load_from_json(file_path100))
        self.assertTrue(self.ga.save_to_json("test100.json"))
        self.assertTrue(self.ga.load_from_json(file_path100_1))
        self.assertTrue(self.ga.save_to_json("test100_1.json"))
        self.assertTrue(self.ga.load_from_json(file_path100_2))
        self.assertTrue(self.ga.save_to_json("test100_2.json"))
        self.assertTrue(self.ga.load_from_json(file_path1000))
        self.assertTrue(self.ga.save_to_json("test1000.json"))
        self.assertTrue(self.ga.load_from_json(file_path1000_1))
        self.assertTrue(self.ga.save_to_json("test1000_1.json"))
        self.assertTrue(self.ga.load_from_json(file_path1000_2))
        self.assertTrue(self.ga.save_to_json("test1000_2.json"))
        self.assertTrue(self.ga.load_from_json(file_path10000))
        self.assertTrue(self.ga.save_to_json("test10000.json"))
        self.assertTrue(self.ga.load_from_json(file_path10000_1))
        self.assertTrue(self.ga.save_to_json("test10000_1.json"))
        self.assertTrue(self.ga.load_from_json(file_path10000_2))
        self.assertTrue(self.ga.save_to_json("test10000_2.json"))
        self.assertTrue(self.ga.load_from_json(file_path20000))
        self.assertTrue(self.ga.save_to_json("test20000.json"))
        self.assertTrue(self.ga.load_from_json(file_path20000_1))
        self.assertTrue(self.ga.save_to_json("test20000_1.json"))
        self.assertTrue(self.ga.load_from_json(file_path20000_2))
        self.assertTrue(self.ga.save_to_json("test20000_2.json"))
        self.assertTrue(self.ga.load_from_json(file_path30000))
        self.assertTrue(self.ga.save_to_json("test30000.json"))
        self.assertTrue(self.ga.load_from_json(file_path30000_1))
        self.assertTrue(self.ga.save_to_json("test30000_1.json"))
        self.assertTrue(self.ga.load_from_json(file_path30000_2))
        self.assertTrue(self.ga.save_to_json("test30000_2.json"))

    def test_shortest_path(self):
        file_path10 = '../data/G_10_80_0.json'
        # file_path10_1 = '../data/G_10_80_1.json'
        # file_path10_2 = '../data/G_10_80_2.json'
        # file_path100 = '../data/G_100_800_0.json'
        # file_path100_1 = '../data/G_100_800_1.json'
        # file_path100_2 = '../data/G_100_800_2.json'
        # file_path1000 = '../data/G_1000_8000_0.json'
        # file_path1000_1 = '../data/G_1000_8000_1.json'
        # file_path1000_2 = '../data/G_1000_8000_2.json'
        # file_path10000 = '../data/G_10000_80000_0.json'
        # file_path10000_1 = '../data/G_10000_80000_1.json'
        # file_path10000_2 = '../data/G_10000_80000_2.json'
        # file_path20000 = '../data/G_20000_160000_0.json'
        # file_path20000_1 = '../data/G_20000_160000_1.json'
        # file_path20000_2 = '../data/G_20000_160000_2.json'
        # file_path30000 = '../data/G_30000_240000_0.json'
        # file_path30000_1 = '../data/G_30000_240000_1.json'
        # file_path30000_2 = '../data/G_30000_240000_2.json'
        self.assertTrue(self.ga.load_from_json(file_path10))
        self.assertEqual(self.ga.shortest_path(0, 5), 6)
        # self.assertTrue(self.ga.load_from_json(file_path10_1))
        # self.assertTrue(self.ga.load_from_json(file_path10_2))
        # self.assertTrue(self.ga.load_from_json(file_path100))
        # self.assertTrue(self.ga.load_from_json(file_path100_1))
        # self.assertTrue(self.ga.load_from_json(file_path100_2))
        # self.assertTrue(self.ga.load_from_json(file_path1000))
        # self.assertTrue(self.ga.load_from_json(file_path1000_1))
        # self.assertTrue(self.ga.load_from_json(file_path1000_2))
        # self.assertTrue(self.ga.load_from_json(file_path10000))
        # self.assertTrue(self.ga.load_from_json(file_path10000_1))
        # self.assertTrue(self.ga.load_from_json(file_path10000_2))
        # self.assertTrue(self.ga.load_from_json(file_path20000))
        # self.assertTrue(self.ga.load_from_json(file_path20000_1))
        # self.assertTrue(self.ga.load_from_json(file_path20000_2))
        # self.assertTrue(self.ga.load_from_json(file_path30000))
        # self.assertTrue(self.ga.load_from_json(file_path30000_1))
        # self.assertTrue(self.ga.load_from_json(file_path30000_2))


if __name__ == '__main__':
    unittest.main()
