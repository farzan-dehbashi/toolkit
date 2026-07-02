import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distances[current_node]:
            continue
        for neighbour, weight in graph[current_node].items():
            dist = current_dist + weight
            if dist < distances[neighbour]:
                distances[neighbour] = dist
                heapq.heappush(heap, (dist, neighbour))

    return distances


if __name__ == "__main__":
    graph = {
        'a': {'b': 1, 'c': 4},
        'b': {'a': 1, 'c': 2, 'd': 5},
        'c': {'a': 4, 'b': 2, 'd': 1},
        'd': {'b': 5, 'c': 1},
    }
    print(dijkstra(graph, 'a'))
