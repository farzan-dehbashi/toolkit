import heapq


def prim_mst(graph, start):
    """
    Prim's Minimum Spanning Tree — O((V + E) log V).
    graph: dict of {node: [(weight, neighbor), ...]}
    Returns list of edges in the MST.
    """
    visited = set([start])
    edges = [(w, start, v) for w, v in graph[start]]
    heapq.heapify(edges)
    mst = []

    while edges and len(visited) < len(graph):
        weight, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, weight))
        for w, neighbour in graph[v]:
            if neighbour not in visited:
                heapq.heappush(edges, (w, v, neighbour))

    return mst


if __name__ == "__main__":
    graph = {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(4, 'A'), (6, 'D'), (3, 'E')],
        'C': [(2, 'A'), (1, 'E')],
        'D': [(6, 'B'), (5, 'F')],
        'E': [(3, 'B'), (1, 'C'), (8, 'F')],
        'F': [(5, 'D'), (8, 'E')],
    }
    mst = prim_mst(graph, 'A')
    print(mst)
    print(f"Total weight: {sum(w for _, _, w in mst)}")
