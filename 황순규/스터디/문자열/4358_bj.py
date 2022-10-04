import sys

import sys

eco_dict = {}
total = 0
for line in sys.stdin: 
    if line == '\n':
        break
    
    tree = line.strip()
    
    if tree in eco_dict:
        eco_dict[tree] += 1
    else:
        eco_dict[tree] = 1
    total += 1
    
eco_dict = sorted(eco_dict.items(), key = lambda x:x[0])

for i in eco_dict:
    print(i[0], "{0:0.4f}".format(round((i[1] / total) * 100, 4)))
    