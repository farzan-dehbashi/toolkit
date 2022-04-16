class MinimalRoute():

    def __init__(self, nodes) -> None:
        self.nodes = nodes
    
    def get_shortest_path(self, hub):
        visited = set()
        queue = list()
        routes = dict()

        if hub in self.nodes:
            queue.append(hub)
        
        while queue:
            cursor = queue.pop(0)
            if not cursor in visited:
                visited.add(cursor)
                print(cursor)
                for neighbour in nodes[cursor]:
                    if not neighbour in visited:
                        queue.append(neighbour)
            



nodes = {'a':{'b','c'}, 'b':{'a','g','d'}, 'c':{'a','d','e'}, 'd':{'b','c','f'}, 'e':{'c','f'}, 'f':{'d','g','e'}, 'g':{'b','f'}}
minimal_route = MinimalRoute(nodes)
print(minimal_route.get_shortest_path('a'))
    