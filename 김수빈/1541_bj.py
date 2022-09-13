import sys

def get_nodes(equation):
    nodes = []
    for op in equation.split('-'):
        node, node_str = 0, ""
        for s in op:
            if s == '+':
                node += int(node_str)
                node_str = ""
            else:
                node_str += s
        if node_str:
            node += int(node_str)
        nodes += [node]
    return nodes

def calculate(nodes):
    if not nodes: return 0
    return nodes[0] + sum(list(map(lambda x: (-1) * x, nodes[1:])))

def solution(equation):
    if not '-' in equation:
        return sum(list(map(int, equation.split('+'))))
    nodes = get_nodes(equation)
    return calculate(nodes)

equation = sys.stdin.readline().strip()
print(solution(equation))