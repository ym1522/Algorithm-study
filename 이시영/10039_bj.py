from sys import stdin

sum=0
for _ in range(5):
    n = int(stdin.readline())
    if n <40:
        n = 40
    sum+=n
print(sum//5)