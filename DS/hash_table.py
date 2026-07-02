class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        self.table[index] = [p for p in self.table[index] if p[0] != key]

    def keys(self):
        return [pair[0] for bucket in self.table for pair in bucket]


if __name__ == "__main__":
    ht = HashTable()
    ht.set("name", "farzan")
    ht.set("age", 30)
    print(ht.get("name"))   # farzan
    print(ht.keys())
    ht.delete("age")
    print(ht.get("age"))    # None
