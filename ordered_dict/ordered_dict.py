from collections import OrderedDict

class LRUCache():
    def __init__(self, capacity) -> None:
        assert capacity > 0, "Capacity size should be positive"
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if not key in self.cache.keys():
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache.keys():
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem()

class LRUTest:
    @staticmethod
    def test():
        cache = LRUCache(3)
        cache.put(1, "one")
        cache.put(2, "two")
        cache.put(3,"three")
        assert cache.get(1) == "one"
        assert cache.get(2) == "two"

if __name__ == "__main__":
    LRUTest.test()

