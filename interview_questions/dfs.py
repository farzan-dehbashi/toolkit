

graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e', 'g'],
    'd' : ['f'],
    'e' : [],
    'f' : [],
    'g' : []
}


def dfs(graph, root):
    stack = []
    stack.append(root)
    visited = set()
    while stack:
        current = stack.pop(len(stack) - 1)
        print(current)
        visited.add(current)
        for neighbour in graph[current]:
            if not neighbour in visited:
                stack.append(neighbour)

dfs(graph, 'a')