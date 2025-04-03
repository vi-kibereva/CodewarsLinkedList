class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    if head is None:
        return Node(data)
    if data < head.data:
        result = Node(data)
        result.next = head
        return result
    probe = head
    while probe.next is not None:
        if probe.data < data < probe.next.data:
            temp = probe.next
            probe.next = Node(data)
            probe = probe.next
            probe.next = temp
            return head
        probe = probe.next
    probe.next = Node(data)
    return head



if __name__ == '__main__':
    head = Node(1, Node(2, Node(3)))
    data = 1.5
    print(sorted_insert(head, 2.5).next.next.next.data)