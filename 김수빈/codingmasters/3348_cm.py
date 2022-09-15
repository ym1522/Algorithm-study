import sys

def solution(N, rects):
    max_iou = 0
    max_iou_idx = None

    for i in range(N):
        x_i, y_i, w_i, h_i = rects[i]
        for j in range(i + 1, N):
            x_j, y_j, w_j, h_j = rects[j]
            if x_j >= x_i + w_i or y_j >= h_i + y_i or x_i >= x_j + w_j or y_i >= h_j + y_j: continue
            w_cands = [(x_i + w_i - x_j), (x_j + w_j - x_i)]
            w_cands = w_cands + [w_i] if x_i >= x_j and x_i + w_i <= x_j + w_j else w_cands
            w_cands = w_cands + [w_j] if x_j >= x_i and x_j + w_j <= x_i + w_i else w_cands            
            w_cands = list(filter(lambda x: x > 0, w_cands))

            h_cands = [(y_i + h_i - y_j), (y_j + h_j - y_i)]
            h_cands = h_cands + [h_i] if y_i >= y_j and y_i + h_i <= y_j + h_j else h_cands
            h_cands = h_cands + [h_j] if y_j >= y_i and y_j + h_j <= y_i + h_i else h_cands
            h_cands = list(filter(lambda y: y > 0, h_cands))
            w, h = min(w_cands), min(h_cands)

            iou = w * h / (w_i * h_i + w_j * h_j - w * h)
            max_iou_idx = (i + 1, j + 1) if iou > max_iou else max_iou_idx
            max_iou = iou if iou > max_iou else max_iou

    return max_iou_idx if max_iou_idx is not None else (1, 2)

N = int(sys.stdin.readline())
rects = []
for i in range(N):
    rects += [tuple(map(int, sys.stdin.readline().split()))]
i, j = solution(N, rects)
print(f"{i} {j}")