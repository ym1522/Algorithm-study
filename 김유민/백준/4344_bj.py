import sys

c = int(sys.stdin.readline())

for i in range(c):
    scores = list(map(int, sys.stdin.readline().split()))
    avg = (sum(scores)-scores[0]) / scores[0]
    student = sum(list(map((lambda x: 1 if x > avg else 0), scores[1:])))
    print(f'{(student / scores[0])*100:.3f}%')