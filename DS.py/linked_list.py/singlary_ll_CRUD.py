class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

    def to_string(self):
        return f'node= {self}, val= {self.val}, next= {self.next}'

#########################
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, node):
        node.next = self.head
        self.head = node

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def pop(self, node):
        pass

    def to_string(self):
        head = self.head
        while head != None:
            print(head.to_string())
            head = head.next
#########################
def main():
    node1 = Node(1)
    node2 = Node(2)

    linked_list = LinkedList()
    linked_list.push(node1)
    linked_list.push(node2)

    linked_list.to_string()

#########################
if __name__ == '__main__':
    main()