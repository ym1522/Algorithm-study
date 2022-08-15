s = input()
ans = [0] * 26

for i in s:
    ans[ord(i)-97] += 1

for i in range(26):
    print(ans[i], end=' ')