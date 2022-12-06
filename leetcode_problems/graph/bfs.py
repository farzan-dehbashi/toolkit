class Node:
    def __init__(self, val, children=list()):
        self.val = val
        self.children = children

    def add_child(self, child):
        self.children.append(child)


class Graph:
    def __init__(self, head):
        self.head = head


class DFS:
    @staticmethod
    def traverse(graph):
        visited = set()
        stack = list()
        stack.append(graph.head)
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                print(current.val)
                for child in current.children:
                    stack.append(child)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.add_child(node2)
node1.add_child(node3)
node2.add_child(node4)
node2.add_child(node5)

graph = Graph(node1)


DFS.traverse(graph)
