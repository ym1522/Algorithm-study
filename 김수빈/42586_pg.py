import math

def solution(progresses, speeds):
    answer = []
    for i, (p, s) in enumerate(zip(progresses, speeds)):
        date = math.ceil((100 - p) / s)
        if i == 0:
            answer.append((date, [i]))
            continue

        top_idx = len(answer)-1
        if answer[top_idx][0] >= date:
            ids = answer[top_idx][1] + [i]
            answer[top_idx] = (answer[top_idx][0], ids)
        else:
            answer.append((date, [i]))

    answer = list(map(lambda x: len(x[-1]), answer))
    return answer