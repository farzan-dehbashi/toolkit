class BinaryTree:
    def __init__(self, size):
        self.roster = size * ['None']
        self.max_size = size
        self.last_used_index = 0

    def __str__(self):
        return '-'.join(self.roster)

    def insert(self, value):
        if self.max_size == self.last_used_index + 1:
            return 'Binary tree is full'
        else:
            self.roster[self.last_used_index + 1] = value
            self.last_used_index += 1
            return f'{value} added'

    def serach(self, val):
        if val in self.roster:
            return self.roster.index(val)
        else:
            return 'not found'

binary_tree = BinaryTree(3)
binary_tree.insert('coffee')
binary_tree.insert('water')
print(binary_tree.serach('water'))
print(str(binary_tree))
