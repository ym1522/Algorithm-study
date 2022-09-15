import sys

inputs = list(map(lambda x: x.strip(), sys.stdin.readlines()))

def is_valid(string):
    string = list(filter(lambda x: x in ['(', ')', '[', ']'], string))
    bracket = []
    for s in string:
        if s in ['(', '[']:
            bracket += [s]
        
        elif s == ')':
            if not bracket or bracket[-1] != '(': return False
            bracket.pop()
        elif s == ']':
            if not bracket or bracket[-1] != '[': return False
            bracket.pop()
    return True if not bracket else False

for string in inputs[:-1]:
    print("yes") if is_valid(string) else print("no") 