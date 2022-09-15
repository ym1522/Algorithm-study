# -*- coding: utf-8 -*-
import sys

def get_indices(arr, value='#'):
    result = []
    for i in range(len(arr)):
        indices = list(filter(lambda x: arr[i][x] == value, range(len(arr[i]))))
        result += list(map(lambda x: (i, x), indices))
    return result

def solution(arr):
    indices = get_indices(arr, '#')
    if len(indices) != 4: return "NO"
    x, y = indices[0]

    if indices == [(i, y) for i in range(x, x + 4)] or indices == [(x, j) for j in range(y, y + 4)]:
        return "YES"
    if (x, y + 1) in indices and (x + 1, y) in indices and (x + 1, y + 1) in indices:
        return "YES"

    if (x, y + 1) in indices and (x, y + 2) in indices and (x + 1, y) in indices:
        return "YES"
    elif (x, y + 1) in indices and (x, y + 2) in indices and (x + 1, y + 2) in indices:
        return "YES"
    elif (x + 1, y) in indices and (x + 1, y + 1) in indices and (x + 1, y + 2) in indices:
        return "YES"
    elif (x + 1, y - 2) in indices and (x + 1, y - 1) in indices and (x + 1, y) in indices:
        return "YES"
    elif (x + 1, y) in indices and (x + 2, y) in indices and (x + 2, y + 1) in indices:
        return "YES"
    elif (x + 1, y) in indices and (x + 2, y) in indices and (x + 2, y - 1) in indices:
        return "YES"

    if (x + 1, y) in indices and (x + 1, y + 1) in indices and (x + 2, y + 1) in indices:
        return "YES"
    elif (x + 1, y) in indices and (x + 1, y + 1) in indices and (x + 2, y + 1) in indices:
        return "YES"
    elif (x, y + 1) in indices and (x + 1, y + 1) in indices and (x + 1, y + 2) in indices:
        return "YES"
    elif (x, y + 1) in indices and (x + 1, y - 1) in indices and (x + 1, y) in indices:
        return "YES"

    if (x, y + 1) in indices and (x, y + 2) in indices and (x + 1, y + 1) in indices:
        return "YES"
    elif (x, y + 1) in indices and (x, y + 2) in indices and (x - 1, y + 1) in indices:
        return "YES"
    elif (x + 1, y) in indices and (x + 1, y + 1) in indices and (x + 2, y) in indices:
        return "YES"
    elif (x + 1, y) in indices and (x + 1, y - 1) in indices and (x + 2, y) in indices:
        return "YES"

    return "NO"
    
arr = list(map(lambda x: x.strip(), sys.stdin.readlines()))
print(solution(arr))