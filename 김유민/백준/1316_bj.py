# 1316 - 그룹 단어 체커
# 메모리: 32460KB, 시간: 92ms

import sys
import collections

n = int(sys.stdin.readline())
check = 0

for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    dict = collections.Counter(word)  # 리스트의 각 요소들이 몇 번 등장했는지 세어 딕셔너리 형태로 반환
    
    # 단어에 등장한 문자 별로 위치들을 각각 저장해줌
    tmp = [[] for _ in range(len(dict))]
    for i, d in enumerate(dict):  # 어떤 문자인지 표시
        tmp[i].append(d)
        
    for w in word:  # 해당 문자마다 위치들 저장
        for i in range(len(tmp)):
            if w == tmp[i][0]: 
                tmp[i].append(word.index(w))
                word[word.index(w)] = 0

    # 그룹 단어인 조건: 같은 문자가 떨어져있으면 안되는데 한 문자가 연속되어 나타나도 가능
    # 그룹 단어가 아닐 조건: 한 문자가 떨어져서 나타나는 경우
    # 그룹 단어가 아닐 조건이 더 쉬울 것이라 판단 -> 그룹 단어가 아닐 때 check += 1
    flag = 0
    for t in tmp:
        if flag == 1: break
        for i in range(1, len(t)-1):
            if t[i+1] - t[i] > 1: 
                check += 1
                flag=1
                break  # 1) break 없으면 틀림
print(n - check)

'''
1) 
입력 예시
------
2
yzyzy
zyzyz
------
인 경우
-> 첫 번째 단어에서 y와 z 모두 떨어져 나타나기 때문에 check가 2가 되기 때문
-> y에서 이미 check += 1 해주었기 때문에 z로 넘어가지 않고 break하여 반복문 탈출
'''

'''
다른 접근 방법?
-> 연속되어 나타나는 문자를 한 문자로 보고, 단어에서 떨어져 나타나는 문자가 있으면 check
-> 이 방법이 더 쉬울지도...?
'''