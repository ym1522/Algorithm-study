import sys

entire_trees = list(map(lambda x: x.strip(), sys.stdin.readlines()))
N = len(entire_trees)

# 딕셔너리 자료구조 사용
D = {}
for t in entire_trees:
    if not t in D:
        D[t] = 1
    else:
        D[t] += 1

# 나무의 품종을 사전순으로 정렬
trees = list(D.keys())
trees.sort()

# 분포 계산
for t in trees:
    print("%s %.4f" % (t, 100 * (D[t] / N)))