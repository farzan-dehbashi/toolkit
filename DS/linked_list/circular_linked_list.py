class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            cursor = self.head
            while cursor.next != self.head:
                cursor = cursor.next
            cursor.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            return []
        result = []
        cursor = self.head
        while True:
            result.append(cursor.val)
            cursor = cursor.next
            if cursor == self.head:
                break
        return result

    def delete(self, val):
        if not self.head:
            return
        if self.head.val == val:
            cursor = self.head
            while cursor.next != self.head:
                cursor = cursor.next
            if cursor == self.head:
                self.head = None
            else:
                cursor.next = self.head.next
                self.head = self.head.next
            return
        prev, cursor = self.head, self.head.next
        while cursor != self.head:
            if cursor.val == val:
                prev.next = cursor.next
                return
            prev, cursor = cursor, cursor.next


if __name__ == "__main__":
    cll = CircularLinkedList()
    for v in [1, 2, 3, 4]:
        cll.append(v)
    print(cll.display())   # [1, 2, 3, 4]
    cll.delete(2)
    print(cll.display())   # [1, 3, 4]
