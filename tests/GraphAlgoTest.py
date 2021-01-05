import unittest

def graph_creator1():
    g = DiGraph()
    add_node(1)
    add_node(2)
    add_node(g, 3)
    add_node(g, 4)


class MyTestCase(unittest.TestCase):
    def shortest_path_distTest(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
