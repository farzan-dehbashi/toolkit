def kruskal_mst(vertices, edges):
    """
    Kruskal's Minimum Spanning Tree — O(E log E).
    edges: list of (weight, u, v)
    Returns list of edges in the MST.
    """
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True

    mst = []
    for weight, u, v in sorted(edges):
        if union(u, v):
            mst.append((u, v, weight))
            if len(mst) == len(vertices) - 1:
                break

    return mst


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [
        (4, 'A', 'B'), (2, 'A', 'C'), (6, 'B', 'D'),
        (3, 'B', 'E'), (1, 'C', 'E'), (5, 'D', 'F'),
        (8, 'E', 'F'),
    ]
    mst = kruskal_mst(vertices, edges)
    print(mst)
    print(f"Total weight: {sum(w for _, _, w in mst)}")
