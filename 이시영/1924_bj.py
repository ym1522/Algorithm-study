from sys import stdin

x, y = map(int,stdin.readline().split())

month=[31,28,31,30,31,30,31,31,30,31,30,31]
day=['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
sum=0
for i in range(x-1):
    sum+=month[i]
sum=(sum+y)%7
print(day[sum])