import sys

dist = int(sys.stdin.readline())
log_num = int(sys.stdin.readline())
logs = list(map(lambda x: tuple(x.split()), sys.stdin.readlines()))

starts = {}
speeds = []
for n, time in logs:
    if not n in starts:
        starts[n] = time
        continue
    h, m, s = map(int, time.split(':'))
    prev_h, prev_m, prev_s =  map(int, starts[n].split(':'))
    secs = h * 3600 + m * 60 + s - (prev_h * 3600 + prev_m * 60 + prev_s) 
    speeds += [(n, int(dist * 3600 // secs))]
speeds.sort()
print('\n'.join(list(map(lambda x: f"{x[0]} {x[1]}", speeds))))