import sys
c_w, c_l, b_w, b_l = 0, 0, 0, 0
N = int(sys.stdin.readline())

for i in range(N):
    g = sys.stdin.readline().strip()
    if g == 'WIN':
        c_w += 1
        c_l = 0
        b_w = c_w if c_w > b_w else b_w
    if g == "LOSE":
        c_l += 1
        c_w = 0
        b_l = c_l if c_l > b_l else b_l
    print(f"{c_w} {c_l} {b_w} {b_l}")
