# -*- coding: utf-8 -*-
import sys

inputs = list(sys.stdin.readline().strip())
min_island, max_island = 0, 0
min_inputs, max_inputs = "o", "o"

for i in range(1, len(inputs)):
    if inputs[i] == 'x':
        min_inputs += min_inputs[-1]
        max_inputs += 'o' if max_inputs[-1] == 'g' else 'g'
    else:
        min_inputs += inputs[i]
        max_inputs += inputs[i]
    
    if min_inputs[i] == 'g' and min_inputs[i - 1] == 'o':
        min_island += 1
    if max_inputs[i] == 'g' and max_inputs[i - 1] == 'o':
        max_island += 1
print(min_island)
print(max_island)