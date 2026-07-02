class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f"TreeNode({self.data!r})"


if __name__ == "__main__":
    tree = TreeNode('drinks')
    cold = TreeNode('cold')
    hot = TreeNode('hot')
    tree.add_child(cold)
    tree.add_child(hot)
    print(tree)
    print(tree.children)
