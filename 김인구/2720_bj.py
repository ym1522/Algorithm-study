import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    coin = int(input())
    result = [0, 0, 0, 0]
    changes = [25, 10, 5, 1]
    for c in range(len(changes)):
        result[c] += coin // changes[c]
        coin %= changes[c]
        
    print(*result)