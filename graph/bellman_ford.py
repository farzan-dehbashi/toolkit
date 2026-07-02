def bellman_ford(graph, vertices, start):
    """
    Bellman-Ford — shortest path with negative weights detection.
    graph: list of (u, v, weight) edges
    vertices: list of all vertices
    Returns distances dict or raises if negative cycle detected.
    """
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative cycle")

    return dist


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', -1), ('A', 'C', 4),
        ('B', 'C', 3), ('B', 'D', 2), ('B', 'E', 2),
        ('D', 'B', 1), ('D', 'C', 5), ('E', 'D', -3),
    ]
    print(bellman_ford(edges, vertices, 'A'))
