class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LL:
    def __init__(self):
        self.head = None

    def __iter__(self):
        

    def add(self, val):
        node = Node(val)
        if self.head != None:
            old_head = self.head
            node.next = old_head
            self.head = node
        elif self.head == None:
            self.head = node


ll = LL()
ll.add(2)
print(ll.head)
