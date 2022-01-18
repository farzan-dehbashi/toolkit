class Node:
    def __init__(self, val, l_c = None, r_c = None): # Left and right child pointers
        self.value = val # Value
        self.l_c = l_c # Left child
        self.r_c = r_c # Right child

class BinaryTree:
    def __init__(self, root):
        self.root = root

    # def __str__(self):
    #     str_list = []
    #     cursor_node = self.root
    #     while cursor_node != None:
    #         str_list.append(cursor_node.value)

drinks = Node('Drinks')
cold_drinks = Node('Cold drinks')
hot_drinks = Node('Hot drinks')

binary_tree = BinaryTree


