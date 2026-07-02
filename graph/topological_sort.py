from collections import deque


def topological_sort_kahn(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbour in graph[node]:
            in_degree[neighbour] += 1

    queue = deque([n for n in in_degree if in_degree[n] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbour in graph[node]:
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    if len(result) != len(graph):
        raise ValueError("Graph has a cycle — topological sort not possible")
    return result


if __name__ == "__main__":
    # Course prerequisites: A->C, A->D, B->D, C->E, D->E
    graph = {
        'A': ['C', 'D'],
        'B': ['D'],
        'C': ['E'],
        'D': ['E'],
        'E': [],
    }
    print(topological_sort_kahn(graph))
