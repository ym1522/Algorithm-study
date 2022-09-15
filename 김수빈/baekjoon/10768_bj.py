m = int(input())
d = int(input())

answer = "Before" if m < 2 or m == 2 and d < 18 else "After"
answer = "Special" if m == 2 and d == 18 else answer

print(answer)