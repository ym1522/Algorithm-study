# lv2 - 스킬트리 

def solution(skill, skill_trees):
    answer = 0
    for trees in skill_trees:                   # skill_trees에 있는 문자열 한 개씩 보기
        flag = 1                                # flag 초기값 1
        for tree in trees:                      # 문자열에서 문자 한 개씩 보기
            if tree not in skill:               # 해당 문자가 있어야할 skill에 없으면 지워줌
                trees = trees.replace(tree, "")
                
        for t, s in zip(trees, skill):          # trees와 skill을 한 문자씩 비교해 다르면 flag = 0
            if t != s: flag = 0
            
        if flag == 1: answer += 1               # flag가 1이면 tress와 skill이 같다는 의미이므로 answer += 1
    
    return answer