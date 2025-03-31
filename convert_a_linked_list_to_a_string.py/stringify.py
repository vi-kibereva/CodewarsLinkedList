class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    '''
    Stringify
    '''
    result = ''
    while True:
        if not isinstance(node, Node):
            return 'None'
        result += f'{node.data} -> '
        if node.next is None:
            result += 'None'
            return result
        node = node.next

if __name__ == '__main__':
    print(stringify(Node(1, Node(2, Node(3)))))