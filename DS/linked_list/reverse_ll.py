class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        result = []
        node = self
        while node:
            result.append(str(node.val))
            node = node.next
        return " -> ".join(result)


def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def make_list(vals):
    dummy = Node(0)
    cursor = dummy
    for v in vals:
        cursor.next = Node(v)
        cursor = cursor.next
    return dummy.next


if __name__ == "__main__":
    ll = make_list([1, 2, 3, 4, 5])
    print(ll)             # 1 -> 2 -> 3 -> 4 -> 5
    print(reverse(ll))    # 5 -> 4 -> 3 -> 2 -> 1
