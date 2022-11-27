# level 1 - 완주하지 못한 선수
# 해시

# ---------- 정확도 50, 효율성 0 => 50점😥 ----------
def solution(participant, completion):
    # 참가자와 완주자 딕셔너리 생성
    dict_participant = {i:0 for i in participant}
    dict_completion = {i:0 for i in completion}
    
    # 참가자와 완주자의 수를 세어 value 값으로 지정
    for p, c in zip(participant, completion):
        if p not in completion:
            dict_completion[p] = 0
        dict_participant[p] += 1
        dict_completion[c] += 1
    
    # 참가자 수 - 완주자 수
    for p in dict_participant:
        dict_participant[p] -= dict_completion[p]
    
    # 완주하지 못한 한 명이 남음
    for k, p in dict_participant.items():
        if p == 1: answer = k
    
    return answer


# ---------- 정확도 50, 효율성 50 => 100점😀 ----------
from collections import Counter
def solution(participant, completion):
    
    # 참가자, 완주자 리스트를 카운터 객체로 생성
    dict_participant = Counter(participant)
    dict_completion = Counter(completion)
    
    # (참가자 - 완주자)를 계산해 tmp에 저장 -> 한 명의 이름만 남음
    tmp = dict_participant - dict_completion
    
    # 남은 한 명의 이름을 가져와 answer에 저장
    answer = list(map(lambda x: x, tmp.keys()))[0]
    return answer


'''
<Counter>
  - 시간복잡도: O(n)
  - 각 원소가 몇 번씩 나오는지 세어 딕셔너리 형태로 반환 (카운터 객체)
  - 산술 연산자 사용 가능! (결과가 음수나 0이 나오면 최종 카운터 객체에서 제외됨)
  - most_common(): 가장 많이 나온 데이터 찾기
'''