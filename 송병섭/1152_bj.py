a = input()
count  =0

if a[0] != ' ':
    count += 1
for i in range(1,len(a)):
    if a[i - 1] == ' ' and a[i] != ' ':
        count += 1
print(count)

import sys
a , b = map(int,sys.stdin.readline())

'a' "abc"

