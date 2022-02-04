from collections import deque

class Node:
    def __init__(self, val, neighbours):
        self.val = val
        self.neighbours = neighbours
        self.is_visited = False

nodes = []
nodes.append(None)
for i in range(1,8,1):
    node = Node(i, [])
    nodes.append(node)

nodes[1].neighbours = [nodes[2], nodes[3]]
nodes[2].neighbours = [nodes[1], nodes[4], nodes[7]]
nodes[3].neighbours = [nodes[1], nodes[4], nodes[5]]
nodes[5].neighbours = [nodes[3], nodes[6]]
nodes[6].neighbours = [nodes[4], nodes[5], nodes[7]]
nodes[7].neighbours = [nodes[2], nodes[6]]

del nodes[0]

queue = deque()
queue.append(nodes[0])
while len(queue) != 0:
    cursor = queue.popleft()
    if cursor.is_visited == False:
        cursor.is_visited = True
        print(f'visiting node{cursor.val}')
        for neighbour in cursor.neighbours:
            queue.append(neighbour)
    print([node.val for node in queue])

