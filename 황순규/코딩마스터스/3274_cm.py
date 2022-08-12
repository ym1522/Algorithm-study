import sys

N = int(sys.stdin.readline())
dish = ["jjamppong", "jjajangmyeon", "bokkeumbap", "jjajangmyeon"]
print(dish[(N - 1) % 4])