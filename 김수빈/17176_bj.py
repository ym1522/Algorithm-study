import sys

def convert(c):
    if ord(c) == 32: return 0
    if ord(c) >= 97:
        return ord(c) - 70
    if ord(c) >= 65:
        return ord(c) - 65 + 1

n = int(sys.stdin.readline())
pw = list(map(int, sys.stdin.readline().split()))
pw.sort()

string = sys.stdin.readline().strip()
string = list(map(convert, string))
string.sort()

print("y") if string == pw else print("n")