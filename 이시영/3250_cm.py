from sys import stdin
n=int(stdin.readline())
lis=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
day=stdin.readline().strip()
key=lis.index(day)
if key+n>6:
    print(lis[key+n-(7*(n//7))-7])
else:
    print(lis[key+n])