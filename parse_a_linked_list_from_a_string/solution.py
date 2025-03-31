class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    s = s.split(' -> ')
    node = None
    for i in range(2, len(s)+1):
        node = Node(int(s[-i]), node)
    return node

if __name__ == '__main__':
    s = '1 -> 2 -> 3 -> None'
    print(linked_list_from_string(s).data)