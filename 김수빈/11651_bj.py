import sys

N = int(sys.stdin.readline())
coords = list(map(lambda x: tuple(map(int, x.split()))[::-1], sys.stdin.readlines()))
coords.sort()
for y, x in coords:
    print(f"{x} {y}")