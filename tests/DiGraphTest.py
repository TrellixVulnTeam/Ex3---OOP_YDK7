import unittest
import random
from DiGraph import DiGraph


def set_DiGraph():
    g = DiGraph()
    for n in range(20):
        g.add_node(n)
    for n in range(30):
        n1 = random.randint(0, 19)
        n2 = random.randint(0, 19)
        weight = random.randint(0, 50)
        g.add_edge(n1, n2, weight)
    return g


class MyTestCase(unittest.TestCase):

    def test_v_size(self):
        g = set_DiGraph()
        self.assertEqual(20, g.sizeV)

    def test_e_size(self):
        g = set_DiGraph()
        self.assertEqual(30, g.sizeE)

    def test_get_mc(self):
        g = set_DiGraph()
        self.assertEqual(50, g.get_mc())

    def test_add_edge(self):
        g = set_DiGraph()
        self.assertTrue(g.add_edge(3, 9, 5))

    def test_add_node(self):
        g = set_DiGraph()
        self.assertFalse(g.add_node(1))
        self.assertTrue(g.add_node(20))

    def test_remove_node(self):
        g = set_DiGraph()
        print(g.sizeE)
        self.assertTrue(g.remove_node(1))
        self.assertEqual(19, g.sizeV)

    def test_remove_edge(self):
        self.g = DiGraph()
        self.g.add_node(0)
        self.g.add_node(1)
        self.g.add_node(2)
        self.g.add_node(3)
        self.g.add_edge(0, 1, 1)
        self.g.add_edge(0, 2, 3)
        self.g.add_edge(0, 2, 3)
        self.g.add_edge(0, 3, 5)
        self.g.add_edge(1, 2, 7)
        self.g.add_edge(3, 1, 2)





if __name__ == '__main__':
    unittest.main()
