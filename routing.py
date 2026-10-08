"""Shortest-path algorithms for a weighted, undirected campus graph."""
import heapq
from math import inf

# Illustrative campus connections, NOT surveyed walking distances or accessibility data.
BUILDINGS = {
    'Rotunda': (0.48, 0.50), 'Clemons Library': (0.62, 0.36),
    'Alderman Library': (0.40, 0.38), 'Newcomb Hall': (0.67, 0.54),
    'Rice Hall': (0.19, 0.70), 'Thornton Hall': (0.35, 0.69),
    'Clark Hall': (0.53, 0.72), 'Shannon Library': (0.37, 0.34),
    'Student Health': (0.78, 0.71), 'Memorial Gym': (0.84, 0.44),
}
# Minutes are fictional demonstration weights, not actual travel-time estimates.
EDGES = [
    ('Rotunda','Shannon Library',3), ('Shannon Library','Alderman Library',2),
    ('Rotunda','Clemons Library',5), ('Alderman Library','Clemons Library',4),
    ('Rotunda','Newcomb Hall',4), ('Newcomb Hall','Clemons Library',3),
    ('Rotunda','Thornton Hall',6), ('Thornton Hall','Rice Hall',4),
    ('Thornton Hall','Clark Hall',3), ('Clark Hall','Student Health',5),
    ('Newcomb Hall','Student Health',6), ('Newcomb Hall','Memorial Gym',5),
    ('Memorial Gym','Student Health',4), ('Clark Hall','Newcomb Hall',4),
    ('Rice Hall','Alderman Library',9),
]

def build_graph(edges=EDGES, nodes=BUILDINGS):
    graph = {name: {} for name in nodes}
    for a, b, weight in edges:
        if a not in graph or b not in graph or weight <= 0:
            raise ValueError('Edges must join known buildings with positive weights')
        graph[a][b] = weight
        graph[b][a] = weight
    return graph

def dijkstra(graph, start, end, blocked=None):
    """Return (path, total_cost) or ([], infinity) when no route exists."""
    blocked = set(blocked or [])
    if start not in graph or end not in graph:
        raise ValueError('Unknown building')
    if start in blocked or end in blocked:
        return [], inf
    queue = [(0, start)]
    distances = {start: 0}
    previous = {}
    while queue:
        cost, current = heapq.heappop(queue)
        if cost != distances[current]:
            continue
        if current == end:
            path = [end]
            while path[-1] != start:
                path.append(previous[path[-1]])
            return list(reversed(path)), cost
        for neighbor, weight in graph[current].items():
            if neighbor in blocked:
                continue
            new_cost = cost + weight
            if new_cost < distances.get(neighbor, inf):
                distances[neighbor] = new_cost
                previous[neighbor] = current
                heapq.heappush(queue, (new_cost, neighbor))
    return [], inf
