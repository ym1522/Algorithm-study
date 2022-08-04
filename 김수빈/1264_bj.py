import sys
from functools import reduce

vowel = ['a' , 'e', 'i', 'o', 'u']
lines = sys.stdin.readlines()
for line in lines[:-1]:
    print(reduce(lambda x, y: x + y, [line.lower().count(c) for c in vowel]))