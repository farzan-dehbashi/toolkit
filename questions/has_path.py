graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e', 'g'],
    'd' : ['f'],
    'e' : [],
    'f' : [],
    'g' : []
}

def has_path(graph, root, start, end):
    stack = []
    visited = set()
    stack.append(root)
    current = start
    while stack:
        current = stack.pop(len(stack) - 1)
        print(current)
        if current == end:
            return True
        visited.add(current)
        for neighbour in graph[current]:
            if not neighbour in visited:
                stack.append(neighbour)
    return False

print(has_path(graph, 'a', 'b', 'f'))