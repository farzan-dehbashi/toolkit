class Node:
    def __init__(self, val) -> None:
        self.val = val

nodes = [Node(1), Node(21), Node(13)]

vals = [node.val for node in nodes]
print(sorted(vals))
