class TreeNode:
    def __init__(self, data, childeren = []):# how to get it using arks and qarks
        self.data = data
        self.childeren = childeren

    def add_child(self, TreeNode):
        self.childeren.append(TreeNode)

tree = TreeNode('drinks',[])
cold = TreeNode('cold', [])
hot = TreeNode('hot', [])
tree.add_child(hot)
tree.add_child(cold)
print(tree)