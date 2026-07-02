def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(graph[node] - visited)
    return visited


if __name__ == "__main__":
    graph = {
        'a': {'b', 'c'},
        'b': {'a', 'd', 'e'},
        'c': {'a', 'f'},
        'd': {'b'},
        'e': {'b', 'f'},
        'f': {'c', 'e'},
    }
    print("Recursive DFS:")
    dfs(graph, 'a')
    print("\nIterative DFS:")
    dfs_iterative(graph, 'a')
