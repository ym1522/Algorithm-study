import sys

n = int(sys.stdin.readline())
menu = [0, "jjamppong", "jjajangmyeon", "bokkeumbap", "jjajangmyeon"]

tmp = n % 4
if tmp == 0:
    tmp = 4
print(menu[tmp])