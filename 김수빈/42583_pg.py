import copy
from functools import reduce

def solution(bridge_length, weight, truck_weights):
    waiting = copy.deepcopy(truck_weights)
    crossing = []
    completion = []

    sec = 1
    crossing_weight = 0
    while waiting or crossing:
        if waiting and (crossing_weight + waiting[0] <= weight):
            crossing_weight += waiting[0]
            crossing.append((sec, waiting[0]))
            waiting = waiting[1:]

        sec += 1
        completion += list(filter(lambda x: x[0] + bridge_length == sec, crossing))
        crossing = list(filter(lambda x: x[0] + bridge_length > sec, crossing))
        crossing_weight = reduce(lambda x, y: x + y, list(map(lambda x: x[-1], crossing))) if crossing else 0

    return sec