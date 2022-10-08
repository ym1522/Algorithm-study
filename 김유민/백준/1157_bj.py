import sys

s = list(sys.stdin.readline().rstrip().upper())
arr = [0] * 26

for i in range(len(s)):
    s[i] = ord(s[i])
    arr[s[i]-65] += 1

first_max = max(arr)
res = arr.index(first_max)
arr.remove(first_max)

print('?' if first_max in arr else chr(res+65))