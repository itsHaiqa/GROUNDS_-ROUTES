import unittest
from math import inf
from routing import build_graph, dijkstra

class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.graph = build_graph()

    def test_same_building(self):
        self.assertEqual(dijkstra(self.graph, 'Rotunda', 'Rotunda'), (['Rotunda'], 0))

    def test_shortest_path(self):
        path, cost = dijkstra(self.graph, 'Rotunda', 'Clemons Library')
        self.assertEqual(cost, 5)
        self.assertEqual(path, ['Rotunda', 'Clemons Library'])

    def test_avoids_closure(self):
        path, _ = dijkstra(self.graph, 'Rotunda', 'Clemons Library', ['Clemons Library'])
        self.assertEqual(path, [])

    def test_unreachable(self):
        path, cost = dijkstra(self.graph, 'Rotunda', 'Rice Hall', ['Thornton Hall', 'Alderman Library'])
        self.assertEqual(path, [])
        self.assertEqual(cost, inf)

    def test_unknown_node(self):
        with self.assertRaises(ValueError):
            dijkstra(self.graph, 'Fake Hall', 'Rotunda')

if __name__ == '__main__':
    unittest.main()
