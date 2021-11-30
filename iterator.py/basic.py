class Item():
    def __init__(self, val, next = None):
        self.val = val
        self.next = None

    def __iter__(self):
        return self

    def __next__(self):
        return self.next

item = Item(1)
item.next = 'hi'
print(next(item))


