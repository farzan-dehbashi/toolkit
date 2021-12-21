from random import randint


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        cursor = self.head
        while cursor:
            yield cursor
            cursor = cursor.next

    def __str__(self):
        values = [str(x.val) for x in self]
        return '->'.join(values)

    def __len__(self):
        length = 0
        cursor = self.head
        while cursor:
            length += 1
            cursor = cursor.next

    def add(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        return self.tail

    def generage(self, n, min, max):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min,max))
        return self

    def remove_dups(self):
        ll_values = []
        cursor = self.head
        while cursor.next:
            if cursor.next.val in ll_values:
                to_be_removed = cursor.next
                cursor.next = to_be_removed.next
            else:
                ll_values.append(cursor.next.val)
            cursor = cursor.next

linked_list = LinkedList()
linked_list.generage(100,0,10)

print(str(linked_list))
# Remove dups
