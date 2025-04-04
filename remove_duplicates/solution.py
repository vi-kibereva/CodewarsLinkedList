class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

if __name__ == '__main__':
    data = Node(1, Node(2, Node(2, Node(3))))
    print(remove_duplicates(data).next.next.next)