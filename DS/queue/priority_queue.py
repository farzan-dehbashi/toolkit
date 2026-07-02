import heapq


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._heap)[-1]

    def peek(self):
        return self._heap[0][-1] if self._heap else None

    def is_empty(self):
        return len(self._heap) == 0


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push('low priority task', 10)
    pq.push('high priority task', 1)
    pq.push('medium priority task', 5)

    while not pq.is_empty():
        print(pq.pop())
