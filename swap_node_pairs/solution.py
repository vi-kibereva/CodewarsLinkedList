class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    prev = None
    current = head
    while current and current.next:
        next_pair = current.next.next
        second = current.next
        second.next = current
        current.next = next_pair
        if prev:
            prev.next = second
        prev = current
        current = next_pair

    return new_head