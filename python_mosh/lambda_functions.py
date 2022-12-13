class Node:
    def __init__(self, val=None) -> None:
        self.val = val
    def get_val(self):
        return self.val

nodes = [Node(1), Node(2), Node(3)]

nodes.sort(key=lambda item:item.val, reverse=True)
print([node.get_val() for node in nodes])
