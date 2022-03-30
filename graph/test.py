from collections import deque

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.children = []
        self.color = False

class Graph:
    def __init__(self, root) -> None:
        self.root = root


class Solution:

    @staticmethod
    def find_max_width(root):
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            print(f'len = {[node.val for node in queue]}')
            cursor = queue.popleft()
            cursor.color = True
            print(cursor.val)
            for child in cursor.children:
                if child.color == False:
                    queue.append(child)


    # Create the tree

nodes = []
for i in range(0, 8):
    node = Node(i)
    nodes.append(node)

nodes[0].children.append(nodes[1])
nodes[0].children.append(nodes[2])
nodes[1].children.append(nodes[3])
nodes[1].children.append(nodes[4])
nodes[2].children.append(nodes[6])

Solution.find_max_width(nodes[0])