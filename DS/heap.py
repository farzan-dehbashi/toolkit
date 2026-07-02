class MaxHeap:
    def __init__(self):
        self._heap = []

    def push(self, val):
        self._heap.append(val)
        self._sift_up(len(self._heap) - 1)

    def pop(self):
        if len(self._heap) == 1:
            return self._heap.pop()
        root = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._sift_down(0)
        return root

    def peek(self):
        return self._heap[0] if self._heap else None

    def _sift_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self._heap[i] > self._heap[parent]:
            self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
            self._sift_up(parent)

    def _sift_down(self, i):
        n = len(self._heap)
        largest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and self._heap[left] > self._heap[largest]:
            largest = left
        if right < n and self._heap[right] > self._heap[largest]:
            largest = right
        if largest != i:
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            self._sift_down(largest)


if __name__ == "__main__":
    h = MaxHeap()
    for v in [3, 1, 4, 1, 5, 9, 2, 6]:
        h.push(v)
    while h.peek() is not None:
        print(h.pop(), end=" ")   # 9 6 5 4 3 2 1 1
    print()
