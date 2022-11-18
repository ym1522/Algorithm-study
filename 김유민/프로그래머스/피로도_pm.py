from itertools import permutations

def solution(K, dungeons):
    answer = []
    res = list(permutations(list(range(len(dungeons)))))
    # res = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)] 가능한 순서 조합 개수
    
    for i in res:
        k, ans = K, 0
        for ii in i:
            if dungeons[ii][0] <= k: 
                k -= dungeons[ii][1]; ans += 1
        answer.append(ans)      # 순서 조합 당 방문 가능한 던전 개수를 answer에 append
    
    return max(answer)