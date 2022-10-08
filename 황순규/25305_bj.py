def bubble_sort(a):
    n = len(a)
    
    while True:
        changed = False

        for i in range(0, n - 1):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True

        if changed == False:
            return a

N, k = map(int, input().split())
scores = list(map(int, input().split()))

scores = bubble_sort(scores)

print(scores[k-1])

