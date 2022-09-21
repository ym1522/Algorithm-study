from sys import stdin
from collections import Counter

tree=[]
count=0
while True:
    a = stdin.readline().rstrip()
    if not a:
        break
    count+=1
    tree.append(a)

tree_dict = sorted(Counter(tree).items())

for i in range(len(tree_dict)):
    print(tree_dict[i][0], "{:.4f}".format(tree_dict[i][1]/count*100))