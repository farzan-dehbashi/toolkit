class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = set(children)

class Trie:
    def __init__(self, head):
        self.head = head
    def __str__(self):
        cursor = self.head



def create_trie(words):
    node0 = Node(None, set())
    trie = Trie(node0)
    for word in words:
        previous_node = None
        for index, char in enumerate(word):
            # print(f'char = {char}, index= {index}')
            node = Node(char, set())
            if index == 0:
                trie.head.children.add(node)
                previous_node = node
            else:
                # print(f'parent_char = {previous_node.val}')
                previous_node.children.add(node)
                previous_node = node
            # print(f'char = {char}')
    return trie

if __name__ == "__main__":
    phone_num = '15195891234'
    words = [ '123', '1234','327926']
    create_trie(words)