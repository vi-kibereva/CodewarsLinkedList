class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    for _ in range(index):
        try:
            node = node.next
        except AttributeError:
            raise IndexError
        if node is None:
            raise IndexError
    return node

if __name__ == '__main__':
    print(get_nth(Node(1, Node(2, Node(3, None))), 4).data)  #1 -> 2 -> 3 -> null