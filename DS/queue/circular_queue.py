class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    def is_empty(self):
        return self.head == -1

    def enqueue(self, val):
        if self.is_full():
            raise OverflowError("Queue is full")
        if self.is_empty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = val

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        val = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


if __name__ == "__main__":
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print(cq.dequeue())   # 1
    cq.enqueue(4)         # wraps around
    print(cq.peek())      # 2
