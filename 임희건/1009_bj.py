test_case = []

T = input()

for i in range(0, int(T)):
    a, b = input().split()
    test_case.append(int(a) ** int(b) % 10)

print()

for j in range(0, int(T)):
    print(test_case[j])
