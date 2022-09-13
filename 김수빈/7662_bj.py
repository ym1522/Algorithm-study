import sys, heapq

def insert(min_h, max_h, n):
    heapq.heappush(min_h, n)
    heapq.heappush(max_h, -n)

    return min_h, max_h

def remove_max_val(max_h, n, min_inv, max_inv):
    try:
        val = -heapq.heappop(max_h)
        while val in max_inv and max_inv[val] > 0:
            max_inv[val] -= 1
            val = -heapq.heappop(max_h)
        min_inv[val] = 1 if not val in min_inv else min_inv[val] + 1
    except:
        pass
    return max_h, min_inv, max_inv

def remove_min_val(min_h, n, min_inv, max_inv):
    try:
        val = heapq.heappop(min_h)
        while val in min_inv and min_inv[val] > 0:
            min_inv[val] -= 1
            val = heapq.heappop(min_h)
        max_inv[val] = 1 if not val in max_inv else max_inv[val] + 1
    except:
        pass
    return min_h, min_inv, max_inv

def remove(min_h, max_h, n, min_inv, max_inv):
    if n == 1:
        max_h, min_inv, max_inv = remove_max_val(max_h, n, min_inv, max_inv)
    else:
        min_h, min_inv, max_inv = remove_min_val(min_h, n, min_inv, max_inv)
    return min_h, max_h, min_inv, max_inv

def get_max_val(max_h, invalid):
    if not max_h: return None
    try:
        val = -max_h[0]
        while val in invalid and invalid[val] > 0:
            heapq.heappop(max_h)
            invalid[val] -= 1
            val = -max_h[0]
        return val
    except:
        return None
    
def get_min_val(min_h, invalid):
    if not min_h: return None
    try:
        val = min_h[0]
        while val in invalid and invalid[val] > 0:
            heapq.heappop(min_h)
            invalid[val] -= 1
            val = min_h[0]
        return val
    except:
        return None

N = int(sys.stdin.readline())
for _ in range(N):
    k = int(sys.stdin.readline())
    min_h, max_h = [], []
    min_inv, max_inv = {}, {}
    for _ in range(k):
        inst = sys.stdin.readline().split()
        n = int(inst[1])
        if inst[0] == 'D':
            min_h, max_h, min_inv, max_inv = remove(min_h, max_h, n, min_inv, max_inv)
        elif inst[0] == 'I':
            min_h, max_h = insert(min_h, max_h, n)

    max_val = get_max_val(max_h, max_inv)
    min_val = get_min_val(min_h, min_inv)
    
    if max_val is None or min_val is None:
        print("EMPTY")
    else:
        print(f"{max_val} {min_val}")