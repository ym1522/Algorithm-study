from sys import stdin

n = int(stdin.readline())
rope = []
for i in range(n):
    rope.append(int(stdin.readline()))
rope = sorted(rope,reverse=True)    
max_we = rope[0]
for i in range(1,n):
    sum = rope[i]*(i+1)
    if max_we <sum:
        max_we = sum
        
print(max_we)