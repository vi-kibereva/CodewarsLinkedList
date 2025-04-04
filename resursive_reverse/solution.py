class Node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

def reverse(head):
    if head is None or head.next is None:
        return head
    new_head = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head
if __name__ == '__main__':
    data = Node(1, Node(2, Node(3)))
    print(reverse(data).data)
