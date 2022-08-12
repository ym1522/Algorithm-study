def solution(priorities, location):
    priorities = list(enumerate(priorities))

    order = 1
    answer = {}
    while priorities:
        top = priorities[0]
        sorted_priorities = sorted(priorities, key=lambda x: x[-1], reverse=True)
        if top[-1] != sorted_priorities[0][-1]:
            priorities = priorities[1:] + [top]
            continue
        answer[top[0]] = order
        priorities = priorities[1:]
        order += 1

    return answer[location]