class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def _height(self, node):
        return node.height if node else 0

    def _balance(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, z):
        y = z.left
        z.left = y.right
        y.right = z
        self._update_height(z)
        self._update_height(y)
        return y

    def _rotate_left(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        self._update_height(z)
        self._update_height(y)
        return y

    def insert(self, node, val):
        if not node:
            return Node(val)
        if val < node.val:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        self._update_height(node)
        bf = self._balance(node)
        if bf > 1 and val < node.left.val:
            return self._rotate_right(node)
        if bf < -1 and val > node.right.val:
            return self._rotate_left(node)
        if bf > 1 and val > node.left.val:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if bf < -1 and val < node.right.val:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)
        return result


if __name__ == "__main__":
    avl = AVLTree()
    root = None
    for v in [10, 20, 30, 40, 50, 25]:
        root = avl.insert(root, v)
    print(avl.inorder(root))   # [10, 20, 25, 30, 40, 50]
