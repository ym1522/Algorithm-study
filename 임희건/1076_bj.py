color = [['black', 0, 1],
         ['brown', 1, 10],
         ['red', 2, 100],
         ['orange', 3, 1000],
         ['yellow', 4, 10000],
         ['green', 5, 100000],
         ['blue', 6, 1000000],
         ['violet', 7, 10000000],
         ['grey', 8, 100000000],
         ['white', 9, 1000000000]]

res = []
ansewr = 0

for i in range(0, 3):
    tmp = input()
    res.append(tmp)

for j in range(0, 10):
    if res[0] == color[j][0]:
        answer = color[j][1] * 10

for k in range(0, 10):
    if res[1] == color[k][0]:
        answer = answer + color[k][1]

for l in range(0, 10):
    if res[2] == color[l][0]:
        answer = answer * color[l][2]

print(answer)
