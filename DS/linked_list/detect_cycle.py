class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def find_cycle_start(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


if __name__ == "__main__":
    # Build: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # cycle

    print(has_cycle(n1))                     # True
    print(find_cycle_start(n1).val)          # 2
