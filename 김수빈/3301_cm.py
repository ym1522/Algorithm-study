import sys

annual, army, YN, cls = sys.stdin.readline().split()
annual = int(annual)
hour = -1
if cls == 'Private':
    if annual == 0: hour = 0
    elif annual < 5:
        if YN == 'N' and army.endswith(('A', 'N')):
            hour = 32
        if (YN == 'Y' and army.endswith(('A', 'N', 'F'))) or (YN == 'N' and army.endswith(('F'))):
            hour = 28
    else:
        hour = 20
else:
    if annual == 0: hour = 0
    else: hour = 28
print(hour)