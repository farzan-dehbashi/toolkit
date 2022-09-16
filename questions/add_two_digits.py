class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node0 = Node(1)
node1 = Node(2)
node0.next = node1
node2 = Node(3)
node1.next = node2

linked_list1 = LinkedList()
linked_list1.head = node0

node0 = Node(9)
node1 = Node(9)
node0.next = node1
node2 = Node(9)
node1.next = node2

linked_list2 = LinkedList()
linked_list2.head = node0

cursor1 = linked_list1.head
cursor2 = linked_list2.head

digits = []
carry = 0
while cursor1 != None and cursor2 != None:
    digit = int(cursor1.data) + int(cursor2.data)
    digits.append(digit + carry)
    cursor1 = cursor1.next
    cursor2 = cursor2.next

print(digits)