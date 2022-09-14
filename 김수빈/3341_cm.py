import sys, re

origin = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()

i, j = 0, 0
origin_stack, stack = [], []
while i < 3:
    reg = re.compile(f'{origin[i]}+')
    s, e = reg.match(origin[i:]).span()
    origin_cnt = e - s
    
    s_t, e_t = reg.match(target[j:]).span()
    target_cnt = e_t - s_t

    stack += [target_cnt]
    origin_stack += [origin_cnt]
    i, j = i + e, j + e_t

count = 0
while stack > origin_stack:
    if len(stack) == 3  and origin_stack[1] * 2 <= stack[1]:
        origin_stack = [min(t * 2, stack[i]) if i in (0, 2) else t * 2 for i, t in enumerate(origin_stack)]
    else:
        cands = []
        cands += [[min(t * 2, stack[i]) if i in (0, 1) else t for i, t in enumerate(origin_stack)]]
        cands += [[min(t * 2, stack[i]) if i in (1, 2) else t for i, t in enumerate(origin_stack)]]
        cands += [[min(t * 2, stack[i]) if i == 0 else t for i, t in enumerate(origin_stack)]]
        cands += [[min(t * 2, stack[i]) if i == 1 else t for i, t in enumerate(origin_stack)]]
        cands += [[min(t * 2, stack[i]) if i == 2 else t for i, t in enumerate(origin_stack)]]
        cands.sort(reverse=True)
        for c in cands:
            if not list(filter(lambda x: x[0] < x[1], zip(stack, c))):
                origin_stack = c
                break               
    count += 1
print(count)