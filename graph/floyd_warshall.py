def floyd_warshall(graph, vertices):
    """
    Floyd-Warshall all-pairs shortest paths — O(V^3).
    graph: dict of {(u, v): weight} for edges, missing means inf.
    """
    INF = float('inf')
    n = len(vertices)
    idx = {v: i for i, v in enumerate(vertices)}
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
    for (u, v), w in graph.items():
        dist[idx[u]][idx[v]] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return {(vertices[i], vertices[j]): dist[i][j] for i in range(n) for j in range(n)}


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D']
    graph = {
        ('A', 'B'): 3, ('A', 'C'): 6,
        ('B', 'C'): 2, ('B', 'D'): 5,
        ('C', 'D'): 1,
    }
    result = floyd_warshall(graph, vertices)
    print(result[('A', 'D')])   # 6
