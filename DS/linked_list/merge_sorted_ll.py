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


def merge_sorted(l1, l2):
    dummy = Node(0)
    cursor = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cursor.next = l1
            l1 = l1.next
        else:
            cursor.next = l2
            l2 = l2.next
        cursor = cursor.next
    cursor.next = l1 or l2
    return dummy.next


def make_list(vals):
    dummy = Node(0)
    cursor = dummy
    for v in vals:
        cursor.next = Node(v)
        cursor = cursor.next
    return dummy.next


if __name__ == "__main__":
    l1 = make_list([1, 3, 5])
    l2 = make_list([2, 4, 6])
    print(merge_sorted(l1, l2))   # 1 -> 2 -> 3 -> 4 -> 5 -> 6
