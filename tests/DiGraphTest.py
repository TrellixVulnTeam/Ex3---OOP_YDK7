import unittest
import random
from DiGraph import DiGraph


def set_DiGraph_random():
    g = DiGraph()
    for n in range(30):
        g.add_node(n)
    for n in range(30):
        n1 = n
        n2 = n + 1
        weight = random.randint(0, 50)
        g.add_edge(n1, n2, weight)
    return g


def set_Digraph():
    g = DiGraph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 3)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 2, 7)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 1, 8)
    return g


class MyTestCase(unittest.TestCase):

    def test_v_size(self):
        g = set_Digraph()
        g.add_node(4)
        g.add_node(5)
        g.add_node(5)
        self.assertEqual(6, g.v_size())

    def test_e_size(self):
        g = set_Digraph()
        g.add_edge(2, 3, 6)
        self.assertEqual(6, g.e_size())

    def test_get_mc(self):
        g = set_Digraph()
        self.assertEqual(10, g.get_mc())

    def test_add_edge(self):
        g = set_Digraph()
        g.add_edge(3, 9, 5)
        self.assertEqual(6, g.e_size())

    def test_add_node(self):
        g = set_Digraph()
        g.add_node(1)
        g.add_node(20)
        self.assertEqual(5, g.v_size())

    def test_remove_node(self):
        g = set_Digraph()
        g.remove_node(1)
        self.assertEqual(3, g.sizeV)

    def test_remove_edge(self):
        g = set_Digraph()
        g.remove_edge(0, 3)
        g.remove_edge(3, 1)
        g.remove_edge(0, 3)
        self.assertEqual(4, g.e_size())
        self.assertEqual(12, g.get_mc())


if __name__ == '__main__':
    unittest.main()
