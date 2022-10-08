from calendar import week
import sys

N = int(sys.stdin.readline())
D = sys.stdin.readline().strip()
weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

id = (weekdays.index(D)+N) % 7
print(weekdays[id])