import sys

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def build_tree(elements, nodes):
    root = nodes[0]

    for element in elements:
        v, l, r = element
        node = nodes[ord(v) - 65]
        left = nodes[ord(l) - 65] if l != '.' else None
        right = nodes[ord(r) - 65] if r != '.' else None
        node.left = left
        node.right = right
    
    return root

def travel_tree(root, order='pre'):
    if root is None: return ''
    left_result = travel_tree(root.left, order=order)
    right_result = travel_tree(root.right, order=order)
    if order=='pre':
        return root.value + left_result + right_result
    elif order == 'in':
        return left_result + root.value + right_result
    else:
        return left_result + right_result + root.value
        
N = int(sys.stdin.readline())
nodes = [BinaryTree(chr(i + 65)) for i in range(N)]
tree_elements = list(map(lambda x: x.strip().split(), sys.stdin.readlines()))

root = build_tree(elements=tree_elements, nodes=nodes)

print(travel_tree(root, 'pre'))
print(travel_tree(root, 'in'))
print(travel_tree(root, 'post'))