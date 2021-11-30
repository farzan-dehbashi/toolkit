class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

    def __str__(self):
        return f'value ={self.val}, next ={self.next}'

class LinkedList:
    def __init__(self):
        self.head = None


def main():
    node1 = Node(1)

if __name__ == '__main__':
    main()