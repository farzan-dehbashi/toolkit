class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)


if __name__ == "__main__":
    bst = BST()
    for val in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(val)
    print(bst.inorder())       # [1, 3, 4, 5, 6, 7, 8]
    print(bst.search(4))       # True
    print(bst.search(9))       # False
