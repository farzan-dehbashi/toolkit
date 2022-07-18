class Node:
    def __init__(self, val, lc, rc):
        self.val = val
        self.lc = lc
        self.rc = rc


class Tree:
    def __init__(self, root):
        self.root = root

node5 = Node(5, None, None)
node4 = Node(4, None, None)
node6 = Node(6, None, None)
node7 = Node(7, None, None)
node3 = Node(3, node6, node7)
node2 = Node(2, node4, node5)
node1 = Node(1, node2, node3)
tree = Tree(node1)


