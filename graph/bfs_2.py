class MinimalRoute():

    def __init__(self, nodes) -> None:
        self.nodes = nodes

    def get_shortest_path(self, start, end):
        visited = set()
        queue = [[start]]

        if start == end:
            return [start]

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                visited.add(node)
                for neighbour in self.nodes[node]:
                    new_path = list(path) + [neighbour]
                    if neighbour == end:
                        return new_path
                    queue.append(new_path)
        return None


if __name__ == "__main__":
    nodes = {
        'a': {'b', 'c'}, 'b': {'a', 'g', 'd'}, 'c': {'a', 'd', 'e'},
        'd': {'b', 'c', 'f'}, 'e': {'c', 'f'}, 'f': {'d', 'g', 'e'},
        'g': {'b', 'f'}
    }
    route = MinimalRoute(nodes)
    print(route.get_shortest_path('a', 'g'))
