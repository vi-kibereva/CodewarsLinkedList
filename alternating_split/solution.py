class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None: 
        raise ValueError
    first = Node(head.data)
    head_1 = first
    head = head.next 
    second = Node(head.data)
    head_2 = second
    try:
        head = head.next
    except AttributeError:
        return Context(first, second)
    flag = True
    while head:
        if flag:
            first.next = Node(head.data)
            first = first.next
        else:
            second.next = Node(head.data)
            second = second.next
        head = head.next
        flag = not flag
    return Context(head_1, head_2)