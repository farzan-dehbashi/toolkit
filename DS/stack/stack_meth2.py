##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################

# Implementation of stack using Linked List

class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.is_empty():
            return None
        else:
            pop_node = self.head
            self.head = pop_node.next
            pop_node.next = None
            return pop_node

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head

    # def display(self):
    #
    #     iternode = self.head
    #     if self.is_empty():
    #         print("Stack Underflow")
    #
    #     else:
    #
    #         while (iternode != None):
    #             print(iternode.val)
    #             iternode = iternode.next
    #         return

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.display()