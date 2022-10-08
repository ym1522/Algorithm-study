def bubble_sort(a, index):
    n = len(a)
    
    while True:
        changed = False

        for i in range(0, n - 1):
            if a[i][index] > a[i + 1][index]:
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True

        if changed == False:
            return a

N = int(input())

dots = []
for i in range(N):
    dots.append(tuple(map(int, input().split())))
    
dots = bubble_sort(dots, 0)
dots = bubble_sort(dots, 1)
# dots.sort(key = lambda x:(x[1], x[0]))

for i in dots:
    print(i[0], i[1])