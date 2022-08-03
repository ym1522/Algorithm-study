way = []
short = 0

x, y, w, h = input().split()

way.append(int(x))
way.append(int(y))
way.append(int(w) - int(x))
way.append(int(h) - int(y))


for i in way:
    if short == 0 or int(short) > i:
        short = i
    
print(short)
