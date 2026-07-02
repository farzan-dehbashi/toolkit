class Graph:
    """Graph using adjacency list."""

    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency = {}

    def add_vertex(self, v):
        if v not in self.adjacency:
            self.adjacency[v] = []

    def add_edge(self, u, v, weight=None):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency[u].append((v, weight))
        if not self.directed:
            self.adjacency[v].append((u, weight))

    def remove_edge(self, u, v):
        self.adjacency[u] = [(n, w) for n, w in self.adjacency[u] if n != v]
        if not self.directed:
            self.adjacency[v] = [(n, w) for n, w in self.adjacency[v] if n != u]

    def neighbors(self, v):
        return [n for n, _ in self.adjacency.get(v, [])]

    def __repr__(self):
        return str(self.adjacency)


if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    print(g.neighbors("A"))   # ['B', 'C']
    print(g)
