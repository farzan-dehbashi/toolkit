class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head) -> None:
        self.head = head

    def reverse(self):

        cursor = self.head

        old_head = cursor.next
        cursor.next = None
        new_head = cursor

        cursor = cursor.next

        while cursor is not None:
            cursor.next = new_head
            new_head = cursor
            old_head = cursor.next
        

    def print_nodes(self):
        cursor = self.head
        depth = 0
        while cursor != None:
            print(f'depth={depth}, val={cursor.val}')
            cursor = cursor.next
            depth += 1




node2 = Node(2)
node1 = Node(1)
node0 = Node(0)

node0.next = node1
node1.next = node2
node2.next = None

linkedlist = LinkedList(node0)
linkedlist.reverse()
linkedlist.print_nodes()